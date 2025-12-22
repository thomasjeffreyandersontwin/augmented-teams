"""Scanner for detecting swallowed exceptions."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation


class SwallowedExceptionsScanner(CodeScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        violations.extend(self._check_swallowed_exceptions(tree, file_path, rule_obj, content))
        
        return violations
    
    def _check_swallowed_exceptions(self, tree: ast.AST, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        violations = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Try):
                for handler in node.handlers:
                    handler_body = handler.body
                    if len(handler_body) == 0:
                        line_number = handler.lineno if hasattr(handler, 'lineno') else None
                        violation = self._create_violation_with_snippet(
                            rule_obj=rule_obj,
                            violation_message=f'Empty except block at line {line_number} - exceptions must be logged or rethrown, never swallowed',
                            file_path=file_path,
                            line_number=line_number,
                            severity='error',
                            content=content,
                            ast_node=handler
                        )
                        violations.append(violation)
                    elif len(handler_body) == 1:
                        if isinstance(handler_body[0], ast.Pass):
                            line_number = handler.lineno if hasattr(handler, 'lineno') else None
                            violation = self._create_violation_with_snippet(
                                rule_obj=rule_obj,
                                violation_message=f'Except block only contains pass at line {line_number} - exceptions must be logged or rethrown, never swallowed',
                                file_path=file_path,
                                line_number=line_number,
                                severity='error',
                                content=content,
                                ast_node=handler
                            )
                            violations.append(violation)
        
        return violations

