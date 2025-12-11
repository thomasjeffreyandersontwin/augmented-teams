"""Scanner for validating scenarios are on story docs."""

from typing import List, Dict, Any, Optional
from pathlib import Path
from .story_scanner import StoryScanner
from .story_map import StoryNode, Story
from .violation import Violation


class ScenariosOnStoryDocsScanner(StoryScanner):
    """Validates scenarios are on story docs (not separate files)."""
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if isinstance(node, Story):
            story_data = node.data
            scenarios = story_data.get('scenarios', [])
            
            # Check if story has scenarios
            if not scenarios or len(scenarios) == 0:
                location = node.map_location()
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story "{node.name}" has no scenarios - scenarios should be on story document',
                    location=location,
                    severity='error'
                ).to_dict()
                violations.append(violation)
        
        return violations

