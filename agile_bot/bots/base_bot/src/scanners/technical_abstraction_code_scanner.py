"""Scanner for validating avoidance of technical abstractions in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class TechnicalAbstractionCodeScanner(CodeScanner):
    """Validates that code stays at domain level, avoiding unnecessary technical abstractions."""
    
    TECHNICAL_ABSTRACTION_PATTERNS = ['Saver', 'Loader', 'Storage']
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                violation = self._check_technical_abstraction(node, file_path, rule_obj)
                if violation:
                    violations.append(violation)
        
        return violations
    
    def _check_technical_abstraction(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if class separates technical abstraction."""
        class_name = class_node.name
        
        for pattern in self.TECHNICAL_ABSTRACTION_PATTERNS:
            if class_name.endswith(pattern):
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Class "{class_name}" separates technical abstraction. Keep technical details (saving, loading) as part of domain concepts instead.',
                    location=str(file_path),
                    line_number=class_node.lineno,
                    severity='warning'
                ).to_dict()
        
        return None




