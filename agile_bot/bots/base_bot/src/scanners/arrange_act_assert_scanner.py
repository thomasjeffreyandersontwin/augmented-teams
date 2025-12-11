"""Scanner for validating Arrange-Act-Assert structure in tests."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .test_scanner import TestScanner
from .violation import Violation


class ArrangeActAssertScanner(TestScanner):
    """Validates tests follow Arrange-Act-Assert structure."""
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if node.name.startswith('test_'):
                        violation = self._check_aaa_structure(node, content, test_file_path, rule_obj)
                        if violation:
                            violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_aaa_structure(self, test_node: ast.FunctionDef, content: str, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if test follows AAA structure."""
        # Get test function source
        test_lines = content.split('\n')
        start_line = test_node.lineno - 1
        end_line = test_node.end_lineno if hasattr(test_node, 'end_lineno') else start_line + 20
        
        test_body_lines = test_lines[start_line:end_line]
        test_body = '\n'.join(test_body_lines)
        
        # Check for AAA comments/sections
        has_given = any('# Given' in line or '# Arrange' in line for line in test_body_lines)
        has_when = any('# When' in line or '# Act' in line for line in test_body_lines)
        has_then = any('# Then' in line or '# Assert' in line for line in test_body_lines)
        
        if not (has_given and has_when and has_then):
            line_number = test_node.lineno if hasattr(test_node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Test "{test_node.name}" does not follow Arrange-Act-Assert structure - add # Given/When/Then or # Arrange/Act/Assert comments',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict()
        
        return None

