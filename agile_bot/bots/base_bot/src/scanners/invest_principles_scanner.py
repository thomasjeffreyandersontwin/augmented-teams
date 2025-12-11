"""Scanner for validating stories follow INVEST principles."""

from typing import List, Dict, Any
from .story_scanner import StoryScanner
from .story_map import StoryNode, Story
from .violation import Violation


class InvestPrinciplesScanner(StoryScanner):
    """Validates stories follow INVEST principles (Independent, Negotiable, Valuable, Estimable, Small, Testable)."""
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Only check Story nodes (not epics/sub-epics)
        if not isinstance(node, Story):
            return violations
        
        if not hasattr(node, 'name') or not node.name:
            return violations
        
        # Check Testable: Story should have scenarios or acceptance criteria
        if not hasattr(node, 'scenarios') or not node.scenarios:
            if not hasattr(node, 'acceptance_criteria') or not node.acceptance_criteria:
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Story "{node.name}" lacks scenarios or acceptance criteria - INVEST principle "Testable" requires clear testable outcomes',
                    location=node.name,
                    severity='warning'
                ).to_dict()
                violations.append(violation)
        
        # Small: Check sizing (already handled by StorySizingScanner, but we can add a reminder)
        # Independent: Hard to validate programmatically (requires dependency analysis)
        # Negotiable: Hard to validate programmatically
        # Valuable: Hard to validate programmatically
        # Estimable: Hard to validate programmatically (related to clarity)
        
        return violations

