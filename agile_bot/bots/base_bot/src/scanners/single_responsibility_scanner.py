"""Scanner for validating single responsibility principle."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation


class SingleResponsibilityScanner(CodeScanner):
    """Validates functions/classes follow single responsibility principle."""
    
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    violation = self._check_function_sr(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
                elif isinstance(node, ast.ClassDef):
                    violation = self._check_class_sr(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_function_sr(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if function has single responsibility."""
        # Check function name for multiple responsibilities
        func_name = func_node.name.lower()
        
        # Multiple responsibility indicators
        multi_resp_patterns = [
            r'\b(and|or|then|also|plus)\b',  # "process_and_validate", "save_and_send"
            r'_(and|or|then|also|plus)_',  # Multiple actions
        ]
        
        import re
        for pattern in multi_resp_patterns:
            if re.search(pattern, func_name):
                line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Function "{func_node.name}" appears to have multiple responsibilities - split into separate functions',
                    location=str(file_path),
                    line_number=line_number,
                    severity='warning'
                ).to_dict()
        
        return None
    
    def _check_class_sr(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if class has single responsibility."""
        # Count methods - too many methods might indicate multiple responsibilities
        method_count = len([n for n in class_node.body if isinstance(n, ast.FunctionDef)])
        
        if method_count > 15:
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Class "{class_node.name}" has {method_count} methods - consider if it has multiple responsibilities',
                location=str(file_path),
                line_number=line_number,
                severity='info'
            ).to_dict()
        
        return None

