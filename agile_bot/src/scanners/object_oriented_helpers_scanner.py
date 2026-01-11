"""Scanner to ensure tests use object-oriented helpers/factories instead of parameter soup."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast

from .test_scanner import TestScanner
from .violation import Violation


class ObjectOrientedHelpersScanner(TestScanner):
    """Detect tests with many parameters/parametrize columns but no helper/factory usage."""

    PARAM_THRESHOLD = 5  # number of parameters before flagging
    PARAMETRIZE_THRESHOLD = 5  # number of parametrize columns before flagging

    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations: List[Dict[str, Any]] = []

        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations

        content, lines, tree = parsed

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test"):
                helper_used = self._uses_helper(node)
                param_count = self._count_params(node)
                parametrize_cols = self._parametrize_column_count(node)

                if (param_count >= self.PARAM_THRESHOLD or parametrize_cols >= self.PARAMETRIZE_THRESHOLD) and not helper_used:
                    message = (
                        f'Test "{node.name}" has many parameters ({max(param_count, parametrize_cols)}) '
                        f"but no helper/factory usage - consolidate with BotTestHelper or shared helper object."
                    )
                    violations.append(
                        Violation(
                            rule=rule_obj,
                            violation_message=message,
                            line_number=node.lineno,
                            location=str(file_path),
                            severity="warning",
                        ).to_dict()
                    )

        return violations

    def _count_params(self, func_node: ast.FunctionDef) -> int:
        """Count parameters excluding self/cls."""
        return sum(
            1
            for arg in func_node.args.args
            if arg.arg not in ("self", "cls")
        )

    def _parametrize_column_count(self, func_node: ast.FunctionDef) -> int:
        """Estimate number of parametrize columns from decorators."""
        for decorator in func_node.decorator_list:
            if isinstance(decorator, ast.Call):
                if isinstance(decorator.func, ast.Attribute) and decorator.func.attr == "parametrize":
                    if decorator.args:
                        first_arg = decorator.args[0]
                        if isinstance(first_arg, (ast.Constant, ast.Str)) and isinstance(first_arg.value, str):
                            columns = [c.strip() for c in first_arg.value.split(",") if c.strip()]
                            return len(columns)
        return 0

    def _uses_helper(self, func_node: ast.FunctionDef) -> bool:
        """Detect Helper/Factory usage inside a test function."""
        for inner in ast.walk(func_node):
            if isinstance(inner, ast.Call):
                # direct call name
                if isinstance(inner.func, ast.Name) and "helper" in inner.func.id.lower():
                    return True
                if isinstance(inner.func, ast.Attribute) and "helper" in inner.func.attr.lower():
                    return True
            if isinstance(inner, ast.Assign):
                for target in inner.targets:
                    if isinstance(target, ast.Name) and "helper" in target.id.lower():
                        return True
        return False
