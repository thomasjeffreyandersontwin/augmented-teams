"""Scanner for validating descriptive function names."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .violation import Violation


class DescriptiveFunctionNamesScanner(TestScanner):
    """Validates helper function names are descriptive and intention-revealing."""
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check helper functions (not test methods)
                    if not node.name.startswith('test_'):
                        violation = self._check_descriptive_name(node, test_file_path, rule_obj)
                        if violation:
                            violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_descriptive_name(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if function name is descriptive."""
        func_name = func_node.name.lower()
        
        # Vague/abbreviated names
        vague_names = ['setup', 'do', 'handle', 'process', 'run', 'main', 'helper', 'util', 'func']
        if func_name in vague_names or len(func_name) < 5:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Helper function "{func_node.name}" uses vague/abbreviated name - use descriptive name that reveals purpose',
                location=str(file_path),
                line_number=line_number,
                severity='error'
            ).to_dict()
        
        # Check for abbreviations
        abbrev_patterns = ['init', 'cfg', 'config', 'var', 'obj', 'param', 'req', 'resp']
        if any(abbrev in func_name for abbrev in abbrev_patterns):
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Helper function "{func_node.name}" contains abbreviations - use full descriptive words',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict()
        
        return None

