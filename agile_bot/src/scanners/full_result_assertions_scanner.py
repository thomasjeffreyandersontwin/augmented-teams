"""Scanner to ensure tests assert full domain results, not single cherry-picked fields."""

from typing import List, Dict, Any, Optional, Set
from pathlib import Path
import ast

from .test_scanner import TestScanner
from .violation import Violation


class FullResultAssertionsScanner(TestScanner):
    """Detect assertions that only check a single field of complex objects instead of the whole result."""

    TARGET_NAMES: Set[str] = {
        "state",
        "log",
        "activity_log",
        "result",
        "results",
        "response",
        "story_graph",
        "graph",
        "data",
        "output",
    }

    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for func in [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test")]:
            for node in ast.walk(func):
                if isinstance(node, ast.Assert):
                    if self._is_single_field_assert(node.test):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message="Assertion checks a single field of a complex result - assert the full object (or dataclass equality) using standard data.",
                                line_number=node.lineno,
                                location=str(file_path),
                                severity="warning",
                            ).to_dict()
                        )

        return violations

    def _is_single_field_assert(self, test_expr: ast.AST) -> bool:
        # assert obj['field'] == ...
        if isinstance(test_expr, ast.Compare):
            left = test_expr.left
            if self._is_subscript_or_attr_on_target(left):
                return True
        # assert len(obj) == ...
        if isinstance(test_expr, ast.Compare):
            if isinstance(test_expr.left, ast.Call):
                call = test_expr.left
                if isinstance(call.func, ast.Name) and call.func.id == "len":
                    if call.args and self._is_target_name(call.args[0]):
                        return True
        return False

    def _is_subscript_or_attr_on_target(self, node: ast.AST) -> bool:
        if isinstance(node, ast.Subscript):
            if self._is_target_name(node.value):
                return True
        if isinstance(node, ast.Attribute):
            if self._is_target_name(node.value):
                return True
        return False

    def _is_target_name(self, node: ast.AST) -> bool:
        return isinstance(node, ast.Name) and node.id in self.TARGET_NAMES
