"""Scanner for validating resource-oriented design in domain models."""

from typing import List, Dict, Any, Optional
from .domain_scanner import DomainScanner
from .domain_concept_node import DomainConceptNode
from .violation import Violation


class ResourceOrientedDesignScanner(DomainScanner):
    
    MANAGER_PATTERNS = ['manager', 'loader', 'handler', 'doer', 'processor', 'executor']
    
    def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        node_name_lower = node.name.lower()
        for pattern in self.MANAGER_PATTERNS:
            if pattern in node_name_lower and node_name_lower.endswith(pattern):
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Domain concept "{node.name}" uses manager/doer/loader pattern. Use resource-oriented design instead (e.g., "{node.name.replace(pattern, "").title()}").',
                        location=node.map_location('name'),
                        line_number=None,
                        severity='error'
                    ).to_dict()
                )
        
        return violations




