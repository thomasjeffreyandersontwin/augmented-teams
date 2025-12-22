from typing import List, Dict, Any, Optional
import logging
from .story_scanner import StoryScanner
from .story_map import StoryNode, Epic, SubEpic, Story
from agile_bot.bots.base_bot.src.scanners.violation import Violation

logger = logging.getLogger(__name__)

try:
    import spacy
    SPACY_AVAILABLE = True
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        nlp = None
        SPACY_AVAILABLE = False
except ImportError:
    SPACY_AVAILABLE = False
    nlp = None

import re


class ActiveLanguageScanner(StoryScanner):
    
    # Common actor patterns that should NOT appear in story names
    ACTOR_PATTERNS = [
        # Human actors
        r'^(User|GM|Admin|Administrator|Customer|Developer|Manager|Operator|Owner)\s+',
        # System actors
        r'^(System|Server|Service|API|Database|Module|Component|Handler|Controller|Processor|Validator|Manager)\s+',
        r'^(The\s+)?(user|admin|system|gm)\s+',
    ]
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        name = node.name
        
        if not name:
            return violations
        
        node_type = self._get_node_type(node)
        
        violation = self._check_actor_in_name(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_passive_voice(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_capability_nouns(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        return violations
    
    def _check_actor_in_name(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        for pattern in self.ACTOR_PATTERNS:
            match = re.match(pattern, name, re.IGNORECASE)
            if match:
                actor = match.group(0).strip()
                location = node.map_location()
                # Suggest the corrected name (without the actor prefix)
                suggested_name = name[len(match.group(0)):].strip()
                if suggested_name:
                    suggested_name = suggested_name[0].upper() + suggested_name[1:] if len(suggested_name) > 1 else suggested_name.upper()
                return Violation(
                    rule=rule_obj,
                    violation_message=f'{node_type.capitalize()} name "{name}" has actor "{actor}" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "{suggested_name}"',
                    location=location,
                    severity='error'
                ).to_dict()
        return None
    
    def _get_node_type(self, node: StoryNode) -> str:
        if isinstance(node, Epic):
            return 'epic'
        elif isinstance(node, SubEpic):
            return 'sub_epic'
        elif isinstance(node, Story):
            return 'story'
        return 'unknown'
    
    def _check_passive_voice(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        return self._check_passive_voice_spacy(name, node, node_type, rule_obj)
    
    def _check_passive_voice_spacy(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return None
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            
            for i, token in enumerate(tokens):
                if token.lemma_.lower() not in ['be', 'is', 'are', 'was', 'were', 'been', 'being']:
                    continue
                
                if i + 1 >= len(tokens):
                    continue
                
                next_token = tokens[i + 1]
                if next_token.tag_ in ['VBN', 'VBD']:
                    return self._create_passive_voice_violation(name, node, node_type, rule_obj)
        except Exception as e:
            logger.debug(f'Spacy NLP failed for passive voice check on "{name}": {e}, falling back to regex')
        
        return None
    
    def _check_passive_voice_regex(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        passive_voice_patterns = [
            r'\b(is|are|was|were|be|been|being)\s+\w+ed\b',
            r'\b(is|are|was|were|be|been|being)\s+\w+en\b',
        ]
        
        for pattern in passive_voice_patterns:
            if re.search(pattern, name, re.IGNORECASE):
                return self._create_passive_voice_violation(name, node, node_type, rule_obj)
        
        return None
    
    def _create_passive_voice_violation(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Dict[str, Any]:
        location = node.map_location()
        return Violation(
            rule=rule_obj,
            violation_message=f'{node_type.capitalize()} name "{name}" uses passive voice - use active voice (e.g., "Places Order" not "Order is placed")',
            location=location,
            severity='error'
        ).to_dict()
    
    def _check_capability_nouns(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        return self._check_capability_nouns_spacy(name, node, node_type, rule_obj)
    
    def _check_capability_nouns_spacy(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return None
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            token_count = len(tokens)
            has_three_or_more_words = token_count >= 3
            
            for idx, token in enumerate(tokens):
                is_last = (idx == token_count - 1)
                
                violation = self._check_gerund_capability_noun(token, is_last, has_three_or_more_words, name, node, node_type, rule_obj)
                if violation:
                    return violation
                
                violation = self._check_abstract_noun_suffix(token, is_last, has_three_or_more_words, name, node, node_type, rule_obj)
                if violation:
                    return violation
        except Exception as e:
            logger.debug(f'Spacy NLP failed for capability noun check on "{name}": {e}, falling back to regex')
        
        return None
    
    def _check_gerund_capability_noun(self, token: Any, is_last: bool, has_three_or_more_words: bool, 
                                      name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if token.tag_ != 'VBG' or token.pos_ != 'NOUN' or not is_last:
            return None
        
        # Allow gerund as last word when name has 3 or more words
        if has_three_or_more_words:
            return None
        
        # Skip if name contains excluded terms
        if any(exclude.lower() in name.lower() for exclude in ["User Story", "Epic", "Feature"]):
            return None
        
        return self._create_capability_noun_violation(name, node, node_type, rule_obj, "gerund")
    
    def _check_abstract_noun_suffix(self, token: Any, is_last: bool, has_three_or_more_words: bool,
                                    name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if token.tag_ not in ['NN', 'NNS'] or not is_last:
            return None
        
        if not any(token.text.endswith(suffix) for suffix in ['ment', 'ance', 'ence']):
            return None
        
        # Allow abstract-noun suffix as last word when name has 3 or more words
        if has_three_or_more_words:
            return None
        
        # Skip if name contains excluded terms
        if any(exclude.lower() in name.lower() for exclude in ["User Story", "Epic", "Feature"]):
            return None
        
        return self._create_capability_noun_violation(name, node, node_type, rule_obj, "abstract noun")
    
    def _check_capability_nouns_regex(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        capability_noun_patterns = [
            r'\b[A-Z]\w+(ing|ment|ance|ence)\b$',
            r'.*\s+[A-Z]\w+(ing|ment|ance|ence)\b$',
        ]
        
        for pattern in capability_noun_patterns:
            if not re.search(pattern, name):
                continue
            
            # Allow when the name has 3 or more words
            if len(name.split()) >= 3:
                break
            
            # Skip if name contains excluded terms
            if any(re.search(r'\b' + exclude + r'\b', name, re.IGNORECASE) for exclude in ["User Story", "Epic", "Feature"]):
                continue
            
            return self._create_capability_noun_violation(name, node, node_type, rule_obj, "capability noun")
        
        return None
    
    def _create_capability_noun_violation(self, name: str, node: StoryNode, node_type: str, rule_obj: Any, noun_type: str) -> Dict[str, Any]:
        location = node.map_location()
        message = f'{node_type.capitalize()} name "{name}" uses capability noun'
        if noun_type == "gerund":
            message += ' (gerund)'
        message += ' - use active behavioral language (e.g., "Processes Payments" not "Payment Processing")'
        
        return Violation(
            rule=rule_obj,
            violation_message=message,
            location=location,
            severity='error'
        ).to_dict()

