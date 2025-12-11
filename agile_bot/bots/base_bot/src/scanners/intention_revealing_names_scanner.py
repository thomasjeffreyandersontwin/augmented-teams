"""Scanner for validating intention-revealing names in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class IntentionRevealingNamesScanner(CodeScanner):
    """Validates that names clearly communicate purpose and usage.
    
    Names should answer 'why does this exist?' and be searchable and pronounceable.
    """
    
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Check variable names
            violations.extend(self._check_variable_names(tree, file_path, rule_obj))
            
            # Check function names
            violations.extend(self._check_function_names(tree, file_path, rule_obj))
            
            # Check class names
            violations.extend(self._check_class_names(tree, file_path, rule_obj))
            
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_variable_names(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for poor variable names."""
        violations = []
        
        # Single-letter names (except i, j in small loops)
        single_letter_patterns = ['d', 'x', 'temp', 'data', 'val', 'obj', 'item', 'thing', 'stuff']
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                var_name = node.id
                
                # Check for single-letter names (except common loop counters)
                if len(var_name) == 1 and var_name not in ['i', 'j', 'k']:
                    # Check if it's in a small loop
                    if not self._is_in_small_loop(node):
                        line_number = node.lineno if hasattr(node, 'lineno') else None
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Variable "{var_name}" uses single-letter name - use intention-revealing name',
                            location=str(file_path),
                            line_number=line_number,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                
                # Check for generic names
                if var_name.lower() in ['data', 'info', 'value', 'thing', 'stuff', 'temp', 'result', 'obj']:
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Variable "{var_name}" uses generic name - use intention-revealing name',
                        location=str(file_path),
                        line_number=line_number,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
        
        return violations
    
    def _check_function_names(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for poor function names."""
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                
                # Skip private methods and special methods
                if func_name.startswith('_') and func_name != '__init__':
                    continue
                
                # Check for generic names
                generic_names = ['process', 'handle', 'do', 'execute', 'get', 'set', 'run', 'main']
                if func_name.lower() in generic_names:
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Function "{func_name}" uses generic name - use intention-revealing name that explains purpose',
                        location=str(file_path),
                        line_number=line_number,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
        
        return violations
    
    def _check_class_names(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for poor class names."""
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                
                # Check for generic names
                generic_names = ['Manager', 'Handler', 'Processor', 'Util', 'Helper', 'Service']
                if class_name in generic_names or any(g in class_name for g in generic_names):
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Class "{class_name}" uses generic name - use intention-revealing name that explains purpose',
                        location=str(file_path),
                        line_number=line_number,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
        
        return violations
    
    def _is_in_small_loop(self, node: ast.Name) -> bool:
        """Check if variable is used in a small loop (like for i in range(10))."""
        # Check parent nodes for For loops
        parent = getattr(node, 'parent', None)
        if parent and isinstance(parent, ast.For):
            # Check if it's a simple range loop
            if isinstance(parent.iter, ast.Call):
                if isinstance(parent.iter.func, ast.Name) and parent.iter.func.id == 'range':
                    return True
        return False

