from typing import List, Dict, Any, Optional
from .story_scanner import StoryScanner
from .story_map import StoryNode, Epic, SubEpic, Story
from agile_bot.bots.base_bot.src.scanners.violation import Violation

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


class VerbNounScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        name = node.name
        
        if not name:
            return violations
        
        node_type = self._get_node_type(node)
        
        violation = self._check_task_oriented_language(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_gerund_ending(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_actor_prefix(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        violation = self._check_noun_only(name, node, node_type, rule_obj)
        if violation:
            violations.append(violation)
        
        return violations
    
    def _get_node_type(self, node: StoryNode) -> str:
        if isinstance(node, Epic):
            return 'epic'
        elif isinstance(node, SubEpic):
            return 'sub_epic'
        elif isinstance(node, Story):
            return 'story'
        return 'unknown'
    
    def _check_task_oriented_language(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        task_words = ["implement", "create", "build", "develop", "design", "set up", "configure", "deploy"]
        
        if any(name.lower().startswith(word) for word in task_words):
            location = node.map_location()
            return Violation(
                rule=rule_obj,
                violation_message=f'{node_type.capitalize()} name "{name}" uses task-oriented language instead of verb-noun format (e.g., "Submit Order" not "Implement Order Submission")',
                location=location,
                severity='error'
            ).to_dict()
        
        return None
    
    def _check_verb_noun_order(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return None
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            
            if len(tokens) < 2:
                return None
            
            pos_tags = [token.pos_ for token in tokens]
            
            if pos_tags[0] == "VERB" and pos_tags[1] in ["NOUN", "PROPN"]:
                return None
            
        except Exception:
            pass
        
        return None
    
    def _check_gerund_ending(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return None
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            
            if not tokens:
                return None
            
            if tokens[0].tag_ == "VBG":
                location = node.map_location()
                return Violation(
                    rule=rule_obj,
                    violation_message=f'{node_type.capitalize()} name "{name}" uses gerund (-ing) form - use present tense verb (e.g., "Places Order" not "Placing Order")',
                    location=location,
                    severity='error'
                ).to_dict()
        
        except Exception:
            pass
        
        return None
    
    def _check_noun_verb_noun_pattern(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return None
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            
            if len(tokens) < 3:
                return None
            
            pos_tags = [token.pos_ for token in tokens]
            words = [token.text.lower() for token in tokens]
            
            if pos_tags[0] in ["NOUN", "PROPN"] and pos_tags[1] == "VERB" and pos_tags[2] in ["NOUN", "PROPN"]:
                actor_words = ["customer", "user", "admin", "developer", "system", "api"]
                if words[0] in actor_words:
                    location = node.map_location()
                    return Violation(
                        rule=rule_obj,
                        violation_message=f'{node_type.capitalize()} name "{name}" uses noun-verb-noun pattern (actor prefix) - use verb-noun format without actor (e.g., "Places Order" not "Customer places order")',
                        location=location,
                        severity='error'
                    ).to_dict()
        
        except Exception:
            pass
        
        return None
    
    def _check_noun_verb_pattern(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return self._check_noun_verb_pattern_basic(name, node, node_type, rule_obj)
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            
            if len(tokens) < 2:
                return None
            
            pos_tags = [token.pos_ for token in tokens]
            
            if pos_tags[0] in ["NOUN", "PROPN"] and pos_tags[1] == "VERB":
                location = node.map_location()
                return Violation(
                    rule=rule_obj,
                    violation_message=f'{node_type.capitalize()} name "{name}" uses noun-verb pattern - use verb-noun format (e.g., "Places Order" not "Order places")',
                    location=location,
                    severity='error'
                ).to_dict()
        
        except Exception:
            return self._check_noun_verb_pattern_basic(name, node, node_type, rule_obj)
        
        return None
    
    def _check_noun_verb_pattern_basic(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        name_lower = name.lower().strip()
        words = name_lower.split()
        
        if len(words) < 2:
            return None
        
        verb_suffixes = ['s', 'es', 'ed', 'ing']
        if any(words[1].endswith(suffix) for suffix in verb_suffixes):
            if not any(words[0].endswith(suffix) for suffix in verb_suffixes):
                location = node.map_location()
                return Violation(
                    rule=rule_obj,
                    violation_message=f'{node_type.capitalize()} name "{name}" uses noun-verb pattern - use verb-noun format (e.g., "Places Order" not "Order places")',
                    location=location,
                    severity='error'
                ).to_dict()
        
        return None
    
    def _check_actor_prefix(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        name_lower = name.lower().strip()
        words = name_lower.split()
        
        if not words:
            return None
        
        actor_words = ["customer", "user", "admin", "developer", "system", "api"]
        if words[0] in actor_words:
            location = node.map_location()
            return Violation(
                rule=rule_obj,
                violation_message=f'{node_type.capitalize()} name "{name}" contains actor prefix (e.g., "Customer") - use verb-noun format without actor',
                location=location,
                severity='error'
            ).to_dict()
        
        return None
    
    def _check_noun_only(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
        if not SPACY_AVAILABLE or nlp is None:
            return None
        
        try:
            doc = nlp(name)
            tokens = [token for token in doc if not token.is_punct]
            
            if not tokens:
                return None
            
            pos_tags = [token.pos_ for token in tokens]
            
            if "VERB" not in pos_tags:
                location = node.map_location()
                return Violation(
                    rule=rule_obj,
                    violation_message=f'{node_type.capitalize()} name "{name}" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")',
                    location=location,
                    severity='error'
                ).to_dict()
        
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.warning(f"spaCy POS tagging failed for '{name}': {e}")
        
        return None

