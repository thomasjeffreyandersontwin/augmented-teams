from typing import List, Dict, Any, Optional
import logging
import re
from .story_scanner import StoryScanner
from .story_map import StoryNode, Epic, SubEpic, Story
from agile_bot.bots.base_bot.src.scanners.violation import Violation
from .vocabulary_helper import VocabularyHelper

logger = logging.getLogger(__name__)


class ActiveLanguageScanner(StoryScanner):
    """
    Validates that story names use active language without actor prefixes.
    Uses NLTK to detect actor/role words at the beginning of story names.
    """
    
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
        # Tokenize the name and check if first word is an actor/role
        words = name.split()
        if not words:
            return None
        
        first_word = words[0].lower()
        actor_index = 0
        
        # Skip "the" if present
        if first_word == 'the' and len(words) > 1:
            first_word = words[1].lower()
            actor_index = 1
        
        # Check if first word is an actor/role using NLTK
        if VocabularyHelper.is_actor_or_role(first_word):
            actor = words[actor_index]
            location = node.map_location()
            # Suggest the corrected name (without the actor prefix)
            suggested_name = ' '.join(words[actor_index + 1:])
            if suggested_name:
                suggested_name = suggested_name[0].upper() + suggested_name[1:] if len(suggested_name) > 1 else suggested_name.upper()
            else:
                suggested_name = "[Verb Noun]"
            
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

