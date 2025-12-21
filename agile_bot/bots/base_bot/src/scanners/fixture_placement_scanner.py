"""Scanner for validating fixtures are defined in test file."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .test_scanner import TestScanner
from .violation import Violation


class FixturePlacementScanner(TestScanner):
    """Validates fixtures are defined in test file (not imported from elsewhere)."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Check for fixture imports (should be defined in file)
        violations.extend(self._check_fixture_imports(tree, file_path, rule_obj))
        
        return violations
    
    def _check_fixture_imports(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for fixture imports (fixtures should be defined in file)."""
        violations = []
        
        # Check for pytest fixture imports
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module and 'fixture' in node.module.lower():
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Fixtures imported from "{node.module}" - fixtures should be defined in test file, not imported',
                        location=str(file_path),
                        line_number=line_number,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
        
        return violations

