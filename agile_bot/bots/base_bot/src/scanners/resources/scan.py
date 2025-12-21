"""Scan resource representing a scan operation."""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .scope import Scope
    from .violation import Violation
    from agile_bot.bots.base_bot.src.actions.rules.rule import Rule


class Scan:
    """Represents a scan operation that finds violations."""
    
    def __init__(self, scope: 'Scope', rule: 'Rule'):
        """Initialize scan.
        
        Args:
            scope: Scope to scan
            rule: Rule to validate against
        """
        self._scope = scope
        self._rule = rule
        self._violations: List['Violation'] = []
    
    @property
    def scope(self) -> 'Scope':
        """Get scope being scanned."""
        return self._scope
    
    @property
    def rule(self) -> 'Rule':
        """Get rule being validated."""
        return self._rule
    
    @property
    def violations(self) -> List['Violation']:
        """Get violations found in this scan."""
        return self._violations
    
    def add_violation(self, violation: 'Violation'):
        """Add a violation to this scan."""
        self._violations.append(violation)
    
    def add_violations(self, violations: List['Violation']):
        """Add multiple violations to this scan."""
        self._violations.extend(violations)
    
    def undergoes_scan(self, scanner) -> List['Violation']:
        """Undergo a scan using a Scanner.
        
        Args:
            scanner: Scanner instance to perform the scan
            
        Returns:
            List of violations found
        """
        # The scanner will call back to add violations
        scanner.performs_scan_for_one_rule(self, self._scope, self._rule)
        return self._violations








