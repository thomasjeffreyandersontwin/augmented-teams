"""Violation resource representing a rule violation."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .block import Block
    from .scan import Scan
    from agile_bot.bots.base_bot.src.actions.rules.rule import Rule


class Violation:
    """Represents a rule violation found in a block."""
    
    def __init__(
        self,
        rule: 'Rule',
        block: 'Block',
        scan: 'Scan',
        violation_message: str,
        line_number: int = None,
        severity: str = 'error'
    ):
        """Initialize violation.
        
        Args:
            rule: Rule that was violated
            block: Block where violation occurs
            scan: Scan that found this violation
            violation_message: Description of violation
            line_number: Line number where violation occurs
            severity: Severity level ('error', 'warning', 'info')
        """
        if not hasattr(rule, 'name') or not hasattr(rule, 'rule_file'):
            raise TypeError(f"rule must be a Rule object, got {type(rule)}")
        
        self._rule = rule
        self._block = block
        self._scan = scan
        self._violation_message = violation_message
        self._line_number = line_number
        self._severity = severity
        
        # Add violation to block and scan
        block.add_violation(self)
        scan.add_violation(self)
    
    @property
    def rule(self) -> 'Rule':
        """Get rule that was violated."""
        return self._rule
    
    @property
    def block(self) -> 'Block':
        """Get block where violation occurs."""
        return self._block
    
    @property
    def scan(self) -> 'Scan':
        """Get scan that found this violation."""
        return self._scan
    
    @property
    def violation_message(self) -> str:
        """Get violation message."""
        return self._violation_message
    
    @property
    def line_number(self) -> int:
        """Get line number where violation occurs."""
        return self._line_number or self._block.start_line
    
    @property
    def severity(self) -> str:
        """Get severity level."""
        return self._severity
    
    @classmethod
    def create_from_rule_and_context(
        cls,
        rule: 'Rule',
        block: 'Block',
        scan: 'Scan',
        message: str,
        line_number: int = None,
        severity: str = 'error'
    ) -> 'Violation':
        """Create violation from rule and context.
        
        Args:
            rule: Rule that was violated
            block: Block where violation occurs
            scan: Scan that found this violation
            message: Violation message
            line_number: Line number
            severity: Severity level
            
        Returns:
            New Violation instance
        """
        return cls(rule, block, scan, message, line_number, severity)
    
    def to_dict(self) -> dict:
        """Convert violation to dictionary format.
        
        Returns:
            Dictionary representation of violation
        """
        result = {
            'rule': self._rule.name,
            'rule_file': self._rule.rule_file,
            'violation_message': self._violation_message,
            'severity': self._severity,
            'line_number': self.line_number,
            'location': str(self._block.file.path)
        }
        return result








