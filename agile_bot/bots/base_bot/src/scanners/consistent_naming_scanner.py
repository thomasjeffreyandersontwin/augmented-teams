"""Scanner for validating consistent naming across codebase."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation
from collections import defaultdict


class ConsistentNamingScanner(CodeScanner):
    """Validates naming consistency across codebase."""
    
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Collect naming patterns
            function_names = []
            variable_names = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    function_names.append(node.name)
                elif isinstance(node, ast.Name):
                    if isinstance(node.ctx, ast.Store):
                        variable_names.append(node.id)
            
            # Check for inconsistent naming patterns
            violations.extend(self._check_naming_consistency(function_names, variable_names, file_path, rule_obj))
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_naming_consistency(self, function_names: List[str], variable_names: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for inconsistent naming patterns."""
        violations = []
        
        # Check for mixed naming conventions (snake_case vs camelCase)
        has_snake_case = any('_' in name for name in function_names)
        has_camel_case = any(name[0].isupper() if name else False for name in function_names)
        
        if has_snake_case and has_camel_case:
            violation = Violation(
                rule=rule_obj,
                violation_message='File mixes snake_case and camelCase naming conventions - use consistent naming style',
                location=str(file_path),
                severity='warning'
            ).to_dict()
            violations.append(violation)
        
        return violations

