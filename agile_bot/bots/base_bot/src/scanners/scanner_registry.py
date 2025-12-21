"""ScannerRegistry for finding and loading scanner helpers by rule."""

from typing import Optional, Dict, Type
import importlib
import re
from .scanner import Scanner


class ScannerRegistry:
    """Registry for finding and loading scanner helpers."""
    
    def __init__(self, bot_name: str = None):
        """Initialize registry.
        
        Args:
            bot_name: Name of bot (for bot-specific scanner paths)
        """
        self._bot_name = bot_name
        self._scanner_cache: Dict[str, Type[Scanner]] = {}
    
    def finds_scanner_by_rule(self, rule) -> Optional[Type[Scanner]]:
        """Find scanner helper by rule.
        
        Args:
            rule: Rule object with scanner_path attribute
            
        Returns:
            Scanner class if found, None otherwise
        """
        if not hasattr(rule, 'scanner_path') or not rule.scanner_path:
            return None
        
        # Check cache first
        if rule.scanner_path in self._scanner_cache:
            return self._scanner_cache[rule.scanner_path]
        
        # Load scanner class
        scanner_class = self.loads_scanner_class(rule.scanner_path)
        if scanner_class:
            self._scanner_cache[rule.scanner_path] = scanner_class
        
        return scanner_class
    
    def loads_scanner_class(self, scanner_module_path: str) -> Optional[Type[Scanner]]:
        """Load scanner class from module path.
        
        Args:
            scanner_module_path: Module path to scanner class (e.g., 'scanners.import_placement_scanner.ImportPlacementScanner')
            
        Returns:
            Scanner class if found, None otherwise
        """
        scanner_class, _ = self.loads_scanner_class_with_error(scanner_module_path)
        return scanner_class
    
    def loads_scanner_class_with_error(self, scanner_module_path: str) -> tuple[Optional[Type[Scanner]], Optional[str]]:
        """Load scanner class from module path with error information.
        
        Args:
            scanner_module_path: Module path to scanner class (e.g., 'scanners.import_placement_scanner.ImportPlacementScanner')
            
        Returns:
            Tuple of (scanner class if found, error message if not found)
        """
        if not scanner_module_path:
            return None, None
        
        try:
            module_path, class_name = scanner_module_path.rsplit('.', 1)
            
            # Extract scanner name from class name (handle camelCase)
            scanner_name = re.sub(r'(?<!^)(?=[A-Z])', '_', class_name).lower().replace('_scanner', '').replace('scanner', '')
            
            # Build paths to try
            paths_to_try = [
                module_path,  # Exact path from config
                f'agile_bot.bots.base_bot.src.scanners.{scanner_name}_scanner'
            ]
            
            # Add bot-specific path if not base_bot
            if self._bot_name and self._bot_name != 'base_bot':
                paths_to_try.append(f'agile_bot.bots.{self._bot_name}.src.scanners.{scanner_name}_scanner')
            
            for path in paths_to_try:
                try:
                    module = importlib.import_module(path)
                    if hasattr(module, class_name):
                        scanner_class = getattr(module, class_name)
                        
                        if isinstance(scanner_class, type) and hasattr(scanner_class, 'scan'):
                            if issubclass(scanner_class, Scanner):
                                return scanner_class, None
                except (ImportError, AttributeError):
                    continue
            
            return None, f"Scanner class not found: {scanner_module_path}"
        except Exception as e:
            return None, f"Error loading scanner {scanner_module_path}: {e}"
    
    def registers_helper(self, scanner_class: Type[Scanner], rule_name: str = None):
        """Register a scanner helper.
        
        Args:
            scanner_class: Scanner class to register
            rule_name: Optional rule name to associate with this scanner
        """
        if rule_name:
            # Register by rule name
            self._scanner_cache[rule_name] = scanner_class
        else:
            # Register by class name
            class_name = scanner_class.__name__
            self._scanner_cache[class_name] = scanner_class

