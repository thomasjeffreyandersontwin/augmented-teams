"""Scanner Orchestrator for coordinating scans across multiple rules."""

from typing import List, TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from .scan import Scan
    from .scope import Scope
    from agile_bot.bots.base_bot.src.actions.validate.rule import Rule
    from .scanner import Scanner
    from .scanner_registry import ScannerRegistry

from .resources.scope import Scope
from .resources.scan import Scan
from .scanner_registry import ScannerRegistry


class ScannerOrchestrator:
    """Orchestrates scanning operations across multiple rules."""
    
    def __init__(self, scanner_registry: ScannerRegistry = None, bot_name: str = None):
        """Initialize orchestrator.
        
        Args:
            scanner_registry: ScannerRegistry instance (creates one if not provided)
            bot_name: Bot name for registry
        """
        self._scanner_registry = scanner_registry or ScannerRegistry(bot_name=bot_name)
    
    @property
    def scanner_registry(self) -> ScannerRegistry:
        """Get scanner registry."""
        return self._scanner_registry
    
    def selects_scanner_helpers_by_rule(
        self,
        rule: 'Rule',
        scanner_registry: ScannerRegistry = None
    ) -> 'Scanner':
        """Select scanner helper by rule.
        
        Args:
            rule: Rule to find scanner for
            scanner_registry: Optional ScannerRegistry (uses instance default if not provided)
            
        Returns:
            Scanner instance
        """
        registry = scanner_registry or self._scanner_registry
        scanner_class = registry.finds_scanner_by_rule(rule)
        
        if not scanner_class:
            raise ValueError(f"No scanner found for rule: {rule.name}")
        
        return scanner_class()
    
    def performs_scan_on_scope(
        self,
        scan: 'Scan',
        scope: 'Scope',
        rule: 'Rule',
        scanner: 'Scanner' = None
    ) -> 'Scan':
        """Perform scan on scope.
        
        Args:
            scan: Scan instance to populate
            scope: Scope to scan
            rule: Rule to validate against
            scanner: Optional Scanner instance (will be selected if not provided)
            
        Returns:
            Scan with violations populated
        """
        if scanner is None:
            scanner = self.selects_scanner_helpers_by_rule(rule)
        
        # Perform the scan
        scan.undergoes_scan(scanner)
        
        return scan
    
    def returns_scan(
        self,
        scope: 'Scope',
        rule: 'Rule'
    ) -> 'Scan':
        """Create and return a scan for scope and rule.
        
        Args:
            scope: Scope to scan
            rule: Rule to validate against
            
        Returns:
            Scan instance with violations
        """
        scan = Scan(scope, rule)
        self.performs_scan_on_scope(scan, scope, rule)
        return scan

