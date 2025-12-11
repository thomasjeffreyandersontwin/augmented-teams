"""Scanner for validating helpers are inline (not shared)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .test_scanner import TestScanner
from .violation import Violation


class InlineHelpersScanner(TestScanner):
    """Validates helper functions are inline in test file, not in separate shared helper file."""
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            
            # Check for imports from test_helpers or helper modules
            violations.extend(self._check_helper_imports(tree, test_file_path, rule_obj))
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_helper_imports(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for imports from test_helpers or helper modules."""
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                module_name = node.module or ''
                if 'test_helpers' in module_name.lower() or 'helper' in module_name.lower():
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Line {line_number} imports helpers from "{module_name}" - helpers must be inline in test file, not imported from separate helper modules',
                        location=str(file_path),
                        line_number=line_number,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
        
        return violations

