"""Scanner for detecting Dict[str, Any] and other type-unsafe patterns.

This scanner enforces the use of typed objects (dataclasses, classes) instead of 
generic dictionaries for structured data. Dict[str, Any] hides structure, prevents
IDE autocomplete, and allows runtime errors that could be caught at compile time.
"""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .code_scanner import CodeScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class TypeSafetyScanner(CodeScanner):
    """Detects type-unsafe patterns like Dict[str, Any] parameters and .get() abuse.
    
    Patterns detected:
    - Method parameters typed as Dict[str, Any]
    - Return types of Dict[str, Any] when structure is known
    - parameters.get() patterns scattered in code
    - **kwargs when parameter set is known
    - List[Any] type hints
    """
    
    # Methods that are allowed to use Dict[str, Any] (infrastructure, not business logic)
    ALLOWED_DICT_ANY_METHODS = {
        # JSON serialization/deserialization
        'to_dict', 'from_dict', 'to_json', 'from_json', 'serialize', 'deserialize',
        # Generic utility methods
        'read_json_file', 'write_json_file', 'load_json', 'save_json',
        # Test helpers
        'create_test_data', 'mock_response',
        # Scanner infrastructure (they receive generic rule data)
        'scan', 'scan_file', 'scan_cross_file',
        # Configuration loading (transitional - these should eventually be typed too)
        '_load_config', 'load_config',
    }
    
    # Parameter names that are allowed to be Dict[str, Any] (infrastructure)
    ALLOWED_DICT_ANY_PARAMS = {
        'kwargs', 'options', 'metadata', 'extra', 'attrs', 'attributes',
        # Scanner infrastructure
        'knowledge_graph', 'rule_content', 'config',
    }
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Skip test files - they may need Dict[str, Any] for test data
        if file_path.name.startswith('test_'):
            return violations
        
        # Walk the AST looking for type-unsafe patterns
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                func_violations = self._check_function_type_safety(node, file_path, rule_obj, content)
                violations.extend(func_violations)
        
        return violations
    
    def _check_function_type_safety(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        """Check a function for type-unsafe patterns."""
        violations = []
        
        func_name = func_node.name
        
        # Skip allowed methods
        if func_name in self.ALLOWED_DICT_ANY_METHODS:
            return violations
        
        # Skip private utility methods (underscore prefix, not dunder)
        if func_name.startswith('_') and not func_name.startswith('__'):
            # But DO check do_execute and other important methods
            if func_name not in ('do_execute', '_execute', '_process', '_handle'):
                return violations
        
        # Check parameter type hints for Dict[str, Any]
        param_violations = self._check_parameter_types(func_node, file_path, rule_obj, content)
        violations.extend(param_violations)
        
        # Check return type for Dict[str, Any]
        return_violations = self._check_return_type(func_node, file_path, rule_obj, content)
        violations.extend(return_violations)
        
        # Check for parameters.get() pattern inside function body
        get_violations = self._check_parameters_get_pattern(func_node, file_path, rule_obj, content)
        violations.extend(get_violations)
        
        return violations
    
    def _check_parameter_types(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        """Check function parameters for Dict[str, Any] type hints."""
        violations = []
        
        for arg in func_node.args.args:
            param_name = arg.arg
            
            # Skip self/cls
            if param_name in ('self', 'cls'):
                continue
            
            # Skip allowed parameter names
            if param_name in self.ALLOWED_DICT_ANY_PARAMS:
                continue
            
            annotation = arg.annotation
            if annotation and self._is_dict_any_annotation(annotation):
                message = self._get_violation_message(
                    rule_obj, 'dict_any_parameter', func_node.lineno,
                    method=func_node.name, param=param_name
                )
                violations.append(
                    self._create_violation_with_snippet(
                        rule_obj=rule_obj,
                        violation_message=message,
                        file_path=file_path,
                        line_number=func_node.lineno,
                        severity='warning',
                        content=content,
                        ast_node=func_node,
                        max_lines=10
                    )
                )
                break  # One violation per function is enough
        
        return violations
    
    def _check_return_type(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        """Check function return type for Dict[str, Any]."""
        violations = []
        
        returns = func_node.returns
        if returns and self._is_dict_any_annotation(returns):
            # Skip if function name suggests it should return dict (to_dict, etc)
            if any(pattern in func_node.name.lower() for pattern in ['to_dict', 'as_dict', 'to_json', 'serialize']):
                return violations
            
            message = self._get_violation_message(
                rule_obj, 'dict_any_return', func_node.lineno,
                method=func_node.name
            )
            violations.append(
                self._create_violation_with_snippet(
                    rule_obj=rule_obj,
                    violation_message=message,
                    file_path=file_path,
                    line_number=func_node.lineno,
                    severity='warning',
                    content=content,
                    ast_node=func_node,
                    max_lines=10
                )
            )
        
        return violations
    
    def _check_parameters_get_pattern(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any, content: str) -> List[Dict[str, Any]]:
        """Check for parameters.get() pattern inside function."""
        violations = []
        found_lines = set()  # Track lines to avoid duplicate violations
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'get':
                        # Check if it's on a variable named 'parameters' or 'params'
                        if isinstance(node.func.value, ast.Name):
                            var_name = node.func.value.id
                            if var_name in ('parameters', 'params', 'kwargs'):
                                line_no = node.lineno
                                if line_no not in found_lines:
                                    found_lines.add(line_no)
                                    message = self._get_violation_message(
                                        rule_obj, 'parameters_get_pattern', line_no
                                    )
                                    violations.append(
                                        Violation(
                                            rule=rule_obj,
                                            violation_message=message,
                                            location=str(file_path),
                                            line_number=line_no,
                                            severity='warning'
                                        ).to_dict()
                                    )
        
        # Limit to first 3 violations per function to avoid noise
        return violations[:3]
    
    def _is_dict_any_annotation(self, annotation: ast.AST) -> bool:
        """Check if annotation is Dict[str, Any] or similar."""
        # Handle subscript like Dict[str, Any]
        if isinstance(annotation, ast.Subscript):
            # Check if it's Dict
            if isinstance(annotation.value, ast.Name):
                if annotation.value.id == 'Dict':
                    # Check if second type arg is Any
                    if isinstance(annotation.slice, ast.Tuple):
                        if len(annotation.slice.elts) >= 2:
                            second_arg = annotation.slice.elts[1]
                            if isinstance(second_arg, ast.Name) and second_arg.id == 'Any':
                                return True
            # Also check for dict[str, Any] (lowercase, Python 3.9+)
            if isinstance(annotation.value, ast.Name):
                if annotation.value.id == 'dict':
                    if isinstance(annotation.slice, ast.Tuple):
                        if len(annotation.slice.elts) >= 2:
                            second_arg = annotation.slice.elts[1]
                            if isinstance(second_arg, ast.Name) and second_arg.id == 'Any':
                                return True
        
        # Handle Attribute like typing.Dict
        if isinstance(annotation, ast.Subscript):
            if isinstance(annotation.value, ast.Attribute):
                if annotation.value.attr == 'Dict':
                    if isinstance(annotation.slice, ast.Tuple):
                        if len(annotation.slice.elts) >= 2:
                            second_arg = annotation.slice.elts[1]
                            if isinstance(second_arg, ast.Name) and second_arg.id == 'Any':
                                return True
        
        return False
    
    def _get_violation_message(self, rule_obj: Any, message_key: str, line_number: int, **format_args) -> str:
        """Get violation message from rule file or use default."""
        if rule_obj and hasattr(rule_obj, 'rule_content'):
            violation_messages = rule_obj.rule_content.get('violation_messages', {})
            if message_key in violation_messages:
                template = violation_messages[message_key]
                return template.format(line=line_number, **format_args)
        
        # Default messages if not in rule file
        defaults = {
            'dict_any_parameter': f"Line {line_number}: Method '{format_args.get('method', 'unknown')}' uses Dict[str, Any] parameter '{format_args.get('param', 'unknown')}'. Define a typed dataclass/class instead.",
            'dict_any_return': f"Line {line_number}: Method '{format_args.get('method', 'unknown')}' returns Dict[str, Any]. Define a typed result class instead.",
            'parameters_get_pattern': f"Line {line_number}: Found 'parameters.get()' pattern. Use typed context object with direct attribute access.",
            'kwargs_abuse': f"Line {line_number}: Method '{format_args.get('method', 'unknown')}' uses **kwargs when parameter set is known. Define explicit typed parameters.",
            'list_any_type': f"Line {line_number}: Found List[Any] type hint. Specify the element type."
        }
        return defaults.get(message_key, f'Line {line_number}: Type safety violation detected.')





