"""Scanner for validating test quality (FIRST principles)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .violation import Violation


class TestQualityScanner(TestScanner):
    """Validates test quality (FIRST principles: Fast, Independent, Repeatable, Self-validating, Timely).
    
    IMPORTANT: This scanner ONLY processes test files. Production code files are automatically skipped.
    Test files are identified by being in test/ or tests/ directories, or having names starting with test_.
    """
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        # Only scan test files - skip production code
        if not self._is_test_file(file_path):
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Check for test quality issues
            violations.extend(self._check_test_independence(tree, content, file_path, rule_obj))
            violations.extend(self._check_test_names_quality(tree, file_path, rule_obj))
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _is_test_file(self, file_path: Path) -> bool:
        """Check if file is a test file.
        
        Test files are identified by:
        - Being in a test/ or tests/ directory (anywhere in path)
        - Having a filename starting with test_
        - Having a filename ending with _test.py
        
        Returns:
            True if file appears to be a test file, False otherwise
        """
        path_str = str(file_path).lower()
        file_name = file_path.name.lower()
        
        # Check if in test directory (using path parts for more reliable matching)
        path_parts = [part.lower() for part in file_path.parts]
        if 'test' in path_parts or 'tests' in path_parts:
            return True
        
        # Check if filename starts with test_
        if file_name.startswith('test_'):
            return True
        
        # Check if filename ends with _test.py
        if file_name.endswith('_test.py'):
            return True
        
        return False
    
    def _check_test_independence(self, tree: ast.AST, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for test independence violations (tests depending on each other)."""
        violations = []
        
        # Check for global state mutations
        lines = content.split('\n')
        for line_num, line in enumerate(lines, 1):
            # Check for global variable assignments
            if re.search(r'global\s+\w+', line, re.IGNORECASE):
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Line {line_num} uses global state - tests should be independent, not share state',
                    location=str(file_path),
                    line_number=line_num,
                    severity='error'
                ).to_dict()
                violations.append(violation)
        
        return violations
    
    def _check_test_names_quality(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check test names are descriptive (not generic)."""
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if node.name.startswith('test_'):
                    # Check for generic test names
                    if node.name in ['test_1', 'test_2', 'test_basic', 'test_simple', 'test_default']:
                        line_number = node.lineno if hasattr(node, 'lineno') else None
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Test "{node.name}" uses generic name - use descriptive name that explains what is being tested',
                            location=str(file_path),
                            line_number=line_number,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
        
        return violations
    
    def scan_story_node(self, node: Any, rule_obj: Any) -> List[Dict[str, Any]]:
        """Scan story node for violations (required by StoryScanner)."""
        # TestQualityScanner focuses on test files, not story graph
        return []

