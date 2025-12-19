"""Scanner for validating dependency chaining in code."""

from typing import List, Dict, Any, Optional, Set
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation


class DependencyChainingCodeScanner(CodeScanner):
    """Validates that code chains dependencies properly with constructor injection.
    
    Detects:
    - Methods that take parameters already injected in __init__ (should use self.param)
    - Internal methods that receive instance attributes as parameters (should access via self)
    - Method calls that pass self.X as arguments when the method could access it directly
    """
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_violations = self._check_dependency_chaining(node, file_path, rule_obj)
                    violations.extend(class_violations)
        
        except (SyntaxError, UnicodeDecodeError):
            pass
        
        return violations
    
    def _check_dependency_chaining(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check if class chains dependencies properly."""
        violations = []
        
        # Find __init__ method and collect constructor-injected parameters
        init_method = None
        init_params = []
        for node in ast.walk(class_node):
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                init_method = node
                init_params = [arg.arg for arg in node.args.args if arg.arg != 'self']
                break
        
        # Collect all instance attributes (from assignments, properties, etc.)
        instance_attrs = self._collect_instance_attributes(class_node)
        
        # Check other methods for parameters that should be injected
        for node in ast.walk(class_node):
            if isinstance(node, ast.FunctionDef) and node.name != '__init__':
                # Skip classmethods and staticmethods - they legitimately need parameters
                # Check for @classmethod and @staticmethod decorators
                is_classmethod = any(
                    (isinstance(decorator, ast.Name) and decorator.id == 'classmethod') or
                    (isinstance(decorator, ast.Attribute) and decorator.attr == 'classmethod')
                    for decorator in node.decorator_list
                )
                is_staticmethod = any(
                    (isinstance(decorator, ast.Name) and decorator.id == 'staticmethod') or
                    (isinstance(decorator, ast.Attribute) and decorator.attr == 'staticmethod')
                    for decorator in node.decorator_list
                )
                
                if is_classmethod or is_staticmethod:
                    continue
                
                method_params = [arg.arg for arg in node.args.args if arg.arg != 'self']
                
                # Check if method takes parameters that are in __init__ (should use self.param instead)
                for param in method_params:
                    if param in init_params:
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Method "{node.name}" in class "{class_node.name}" takes parameter "{param}" that is already injected in __init__. Use self.{param} instead.',
                                location=str(file_path),
                                line_number=node.lineno,
                                severity='warning'
                            ).to_dict()
                        )
                
                # Check for internal methods passing instance attributes as parameters
                if node.name.startswith('_') and not (node.name.startswith('__') and node.name.endswith('__')):
                    violations.extend(self._check_method_calls_for_instance_attrs(
                        node, class_node.name, file_path, rule_obj, instance_attrs
                    ))
        
        return violations
    
    def _collect_instance_attributes(self, class_node: ast.ClassDef) -> Set[str]:
        """Collect all instance attributes and properties from class."""
        attrs = set()
        
        for node in ast.walk(class_node):
            # Collect self.X assignments
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute):
                        if isinstance(target.value, ast.Name) and target.value.id == 'self':
                            attrs.add(target.attr)
            
            # Collect self.X in expressions (properties, method calls)
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name) and node.value.id == 'self':
                    attrs.add(node.attr)
            
            # Collect property decorators
            if isinstance(node, ast.FunctionDef):
                for decorator in node.decorator_list:
                    if isinstance(decorator, ast.Name) and decorator.id == 'property':
                        attrs.add(node.name)
        
        return attrs
    
    def _check_method_calls_for_instance_attrs(
        self, func_node: ast.FunctionDef, class_name: str, file_path: Path, 
        rule_obj: Any, instance_attrs: Set[str]
    ) -> List[Dict[str, Any]]:
        """Check method calls for passing instance attributes as parameters."""
        violations = []
        
        for node in ast.walk(func_node):
            if isinstance(node, ast.Call):
                # Check if this is a method call on self
                if isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                        # Check arguments for instance attributes
                        for arg in node.args:
                            violation = self._check_argument(
                                arg, node.func.attr, class_name, file_path, rule_obj, instance_attrs, func_node.lineno
                            )
                            if violation:
                                violations.append(violation)
        
        return violations
    
    def _check_argument(
        self, arg_node: ast.AST, method_name: str, class_name: str, file_path: Path, 
        rule_obj: Any, instance_attrs: Set[str], line_num: int
    ) -> Optional[Dict[str, Any]]:
        """Check if argument is an instance attribute that shouldn't be passed."""
        # Check if argument is self.X
        if isinstance(arg_node, ast.Attribute):
            if isinstance(arg_node.value, ast.Name) and arg_node.value.id == 'self':
                attr_name = arg_node.attr
                if attr_name in instance_attrs:
                    return Violation(
                        rule=rule_obj,
                        violation_message=f'Line {line_num}: Passing self.{attr_name} as parameter to {method_name}(). Access it directly in the method through self.{attr_name} instead.',
                        location=str(file_path),
                        line_number=line_num,
                        severity='warning'
                    ).to_dict()
        
        return None




