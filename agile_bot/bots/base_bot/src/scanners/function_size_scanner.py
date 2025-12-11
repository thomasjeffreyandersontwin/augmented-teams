"""Scanner for validating function size (keep functions small)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation


class FunctionSizeScanner(CodeScanner):
    """Validates functions are small enough to understand at a glance.
    
    Keep functions under 20 lines when possible.
    """
    
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Skip private methods and special methods
                    if node.name.startswith('_') and node.name != '__init__':
                        continue
                    
                    violation = self._check_function_size(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_function_size(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if function exceeds size limit."""
        # Calculate function size (end_lineno - lineno + 1)
        if hasattr(func_node, 'end_lineno') and func_node.end_lineno:
            func_size = func_node.end_lineno - func_node.lineno + 1
        else:
            # Fallback: estimate from body
            func_size = len(func_node.body) * 3  # Rough estimate
        
        if func_size > 20:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Function "{func_node.name}" is {func_size} lines - should be under 20 lines (extract complex logic to helper functions)',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict()
        
        return None
