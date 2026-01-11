"""Scanner to ensure tests reuse standard data sets instead of ad-hoc inline dicts."""

from typing import List, Dict, Any, Optional, Set
from pathlib import Path
import ast

from .test_scanner import TestScanner
from .violation import Violation


class StandardDataReuseScanner(TestScanner):
    """Detect repeated ad-hoc inline data instead of shared canonical fixtures/constants."""

    CANONICAL_KEYS: Set[str] = {
        "current",
        "completed_actions",
        "stories",
        "events",
        "action",
        "state",
        "log",
        "results",
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
                if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
                    if self._dict_has_canonical_keys(node.value):
                        if not self._is_uppercase_constant(node.targets):
                            violations.append(
                                Violation(
                                    rule=rule_obj,
                                    violation_message="Inline dict with standard test data fields - reuse a shared standard data set (e.g., STANDARD_STATE) instead of recreating ad-hoc.",
                                    line_number=node.lineno,
                                    location=str(file_path),
                                    severity="warning",
                                ).to_dict()
                            )

        return violations

    def _is_uppercase_constant(self, targets: List[ast.expr]) -> bool:
        for target in targets:
            if isinstance(target, ast.Name) and target.id.isupper():
                return True
        return False

    def _dict_has_canonical_keys(self, dict_node: ast.Dict) -> bool:
        for key in dict_node.keys:
            if isinstance(key, ast.Constant) and isinstance(key.value, str):
                if key.value in self.CANONICAL_KEYS:
                    return True
        return False
