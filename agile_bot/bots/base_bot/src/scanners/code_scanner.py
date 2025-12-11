"""Base CodeScanner class for validating source code files."""

from abc import abstractmethod
from typing import List, Dict, Any, Optional
from pathlib import Path
from .scanner import Scanner
from .violation import Violation


class CodeScanner(Scanner):
    """Base class for code validation scanners.
    
    CodeScanners validate Python/JavaScript source code files against rules.
    Each scanner implements scan_code_file() to check a single file.
    """
    
    def scan(self, knowledge_graph: Dict[str, Any], rule_obj: Any = None) -> List[Dict[str, Any]]:
        """Scan code files for rule violations.
        
        Args:
            knowledge_graph: Not used for code scanners (code scanners work on files)
            rule_obj: Rule object reference (for creating Violations)
            
        Returns:
            List of violation dictionaries
        """
        if not rule_obj:
            raise ValueError("rule_obj parameter is required for CodeScanner")
        
        violations = []
        
        # Code scanners need to find code files to scan
        # This will be provided via content_to_validate or workspace context
        # For now, return empty list - subclasses should override scan() to find files
        return violations
    
    @abstractmethod
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Scan a single code file for violations.
        
        Args:
            file_path: Path to code file to scan
            rule_obj: Rule object reference
            
        Returns:
            List of violation dictionaries
        """
        pass

