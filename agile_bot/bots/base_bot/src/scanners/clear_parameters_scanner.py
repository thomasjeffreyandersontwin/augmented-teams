"""Scanner for validating function parameters are clear."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation


class ClearParametersScanner(CodeScanner):
    """Validates function parameters are clear and well-named."""
    
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    violation = self._check_parameters(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_parameters(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if function parameters are clear."""
        # Check for too many parameters (hard to understand)
        if len(func_node.args.args) > 5:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Function "{func_node.name}" has {len(func_node.args.args)} parameters - consider using parameter object or reducing parameters',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict()
        
        # Check for vague parameter names
        vague_names = ['data', 'value', 'item', 'obj', 'thing', 'param', 'arg']
        for arg in func_node.args.args:
            if arg.arg.lower() in vague_names:
                line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Function "{func_node.name}" has vague parameter name "{arg.arg}" - use descriptive name',
                    location=str(file_path),
                    line_number=line_number,
                    severity='warning'
                ).to_dict()
        
        return None

