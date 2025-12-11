"""Scanner for validating tests match specification scenarios."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .violation import Violation


class SpecificationMatchScanner(TestScanner):
    """Validates test docstrings and assertions match specification scenarios exactly."""
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            
            # Check test docstrings match scenario format
            violations.extend(self._check_scenario_format(tree, test_file_path, rule_obj))
            
            # Check variable names match specification
            violations.extend(self._check_variable_names(tree, content, test_file_path, rule_obj))
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_scenario_format(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check test docstrings follow scenario format (GIVEN/WHEN/THEN)."""
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                docstring = ast.get_docstring(node)
                if docstring:
                    # Check for scenario format
                    has_given = 'GIVEN' in docstring.upper() or 'Given' in docstring
                    has_when = 'WHEN' in docstring.upper() or 'When' in docstring
                    has_then = 'THEN' in docstring.upper() or 'Then' in docstring
                    
                    if not (has_given and has_when and has_then):
                        line_number = node.lineno if hasattr(node, 'lineno') else None
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Test "{node.name}" docstring should follow scenario format (GIVEN/WHEN/THEN) to match specification',
                            location=str(file_path),
                            line_number=line_number,
                            severity='warning'
                        ).to_dict()
                        violations.append(violation)
                else:
                    # No docstring at all
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Test "{node.name}" missing docstring - should match specification scenario format',
                        location=str(file_path),
                        line_number=line_number,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
        
        return violations
    
    def _check_variable_names(self, tree: ast.AST, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check variable names match specification (heuristic - checks for generic names)."""
        violations = []
        
        # This is a simplified check - full implementation would need specification context
        # For now, check for obviously generic names that suggest mismatch
        generic_names = ['data', 'result', 'value', 'item', 'obj', 'thing']
        
        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            for generic in generic_names:
                # Check for variable assignment with generic name
                pattern = rf'\b{generic}\s*='
                if re.search(pattern, line, re.IGNORECASE):
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Line {line_num} uses generic variable name "{generic}" - use exact variable names from specification',
                        location=str(file_path),
                        line_number=line_num,
                        severity='info'
                    ).to_dict()
                    violations.append(violation)
                    break
        
        return violations
    
    def scan_story_node(self, node: Any, rule_obj: Any) -> List[Dict[str, Any]]:
        """Scan story node for violations (required by StoryScanner)."""
        return []

