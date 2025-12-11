from typing import List, Dict, Any, Optional
from .story_scanner import StoryScanner
from .story_map import StoryNode, Epic, SubEpic, Story
from agile_bot.bots.base_bot.src.scanners.violation import Violation


class StorySizingScanner(StoryScanner):
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Epic):
            violation = self._check_epic_sub_epic_count(node, rule_obj)
            if violation:
                violations.append(violation)
        
        elif isinstance(node, SubEpic):
            violation = self._check_sub_epic_story_count(node, rule_obj)
            if violation:
                violations.append(violation)
        
        elif isinstance(node, Story):
            violation = self._check_story_acceptance_criteria_count(node, rule_obj)
            if violation:
                violations.append(violation)
        
        return violations
    
    def _check_epic_sub_epic_count(self, epic: Epic, rule_obj: Any) -> Optional[Dict[str, Any]]:
        sub_epics = epic.data.get('sub_epics', [])
        story_groups = epic.data.get('story_groups', [])
        total_children = len(sub_epics) + len(story_groups)
        
        if total_children == 0:
            return None
        
        count = total_children
        severity, message = self._get_size_violation(count, 'sub-epics/story groups')
        
        if severity:
            location = epic.map_location()
            return Violation(
                rule=rule_obj,
                violation_message=f'Epic "{epic.name}" has {count} {message}',
                location=location,
                severity=severity
            ).to_dict()
        
        return None
    
    def _check_sub_epic_story_count(self, sub_epic: SubEpic, rule_obj: Any) -> Optional[Dict[str, Any]]:
        nested_sub_epics = sub_epic.data.get('sub_epics', [])
        story_groups = sub_epic.data.get('story_groups', [])
        
        total_stories = 0
        for story_group in story_groups:
            stories = story_group.get('stories', [])
            total_stories += len(stories)
        
        total_children = len(nested_sub_epics) + total_stories
        
        if total_children == 0:
            return None
        
        count = total_children
        severity, message = self._get_size_violation(count, 'nested sub-epics/stories')
        
        if severity:
            location = sub_epic.map_location()
            return Violation(
                rule=rule_obj,
                violation_message=f'Sub-epic "{sub_epic.name}" has {count} {message}',
                location=location,
                severity=severity
            ).to_dict()
        
        return None
    
    def _check_story_acceptance_criteria_count(self, story: Story, rule_obj: Any) -> Optional[Dict[str, Any]]:
        acceptance_criteria = story.data.get('acceptance_criteria', [])
        count = len(acceptance_criteria)
        
        if count == 0:
            return None
        
        severity, message = self._get_size_violation(count, 'acceptance criteria')
        
        if severity:
            location = story.map_location('acceptance_criteria')
            return Violation(
                rule=rule_obj,
                violation_message=f'Story "{story.name}" has {count} {message}',
                location=location,
                severity=severity
            ).to_dict()
        
        return None
    
    def _get_size_violation(self, count: int, item_type: str) -> tuple[Optional[str], str]:
        if 5 <= count <= 9:
            return None, f'{count} {item_type} (perfect)'
        elif count == 4 or count == 10:
            return 'warning', f'{count} {item_type} (should be 5-9)'
        elif count <= 2 or count >= 12:
            return 'error', f'{count} {item_type} (should be 5-9)'
        else:
            return 'warning', f'{count} {item_type} (should be 5-9)'

