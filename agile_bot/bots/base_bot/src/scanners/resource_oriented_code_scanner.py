"""Scanner for validating resource-oriented design in code."""

from typing import List, Dict, Any, Optional, Set, Tuple
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class ResourceOrientedCodeScanner(CodeScanner):
    """Validates that code uses resource-oriented design instead of standalone manager/doer/loader patterns.
    
    Allows manager/loader/doer classes IF they are properties/attributes of a domain object.
    Only flags violations when these classes are standalone (not owned by a domain object).
    
    Ownership checking is done in cross-file scan to detect usage across different files.
    """
    
    MANAGER_PATTERNS = ['Manager', 'Loader', 'Handler', 'Doer', 'Processor', 'Executor', 'Builder']
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Scan single file - just collect classes with manager patterns.
        
        Ownership checking is deferred to scan_cross_file() to check across all files.
        """
        # No violations in single-file scan - all checking happens in cross-file scan
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None
    ) -> List[Dict[str, Any]]:
        """Scan across all files to check if loader/manager classes are owned by domain objects."""
        violations = []
        
        # Combine all files
        all_files = []
        if code_files:
            all_files.extend(code_files)
        if test_files:
            all_files.extend(test_files)
        
        if not all_files:
            return violations
        
        # First pass: collect all loader/manager classes and all classes
        loader_classes = {}  # class_name -> (file_path, class_node, pattern)
        all_classes = {}  # (file_path, class_name) -> class_node
        
        for file_path in all_files:
            if not file_path.exists():
                continue
            
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content, filename=str(file_path))
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        all_classes[(file_path, node.name)] = node
                        
                        # Check if it's a loader/manager pattern
                        for pattern in self.MANAGER_PATTERNS:
                            if node.name.endswith(pattern):
                                loader_classes[node.name] = (file_path, node, pattern)
                                break
            except (SyntaxError, UnicodeDecodeError):
                continue
        
        # Second pass: check if each loader class is owned by a domain object
        for loader_class_name, (loader_file, loader_node, pattern) in loader_classes.items():
            if not self._is_owned_by_domain_object(loader_class_name, loader_node, all_files, all_classes):
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Class "{loader_class_name}" uses manager/doer/loader pattern but is not owned by a domain object. Use resource-oriented design instead (e.g., make it a property of a domain object like "{loader_class_name.replace(pattern, "")}").',
                    location=str(loader_file),
                    line_number=loader_node.lineno,
                    severity='error'
                ).to_dict()
                violations.append(violation)
        
        return violations
    
    def _is_owned_by_domain_object(
        self, 
        loader_class_name: str, 
        loader_node: ast.ClassDef,
        all_files: List[Path],
        all_classes: Dict[Tuple[Path, str], ast.ClassDef]
    ) -> bool:
        """Check if the loader/manager class is used as a property/attribute of another class (domain object).
        
        Checks across all files to find if any class uses this loader as an instance attribute.
        """
        # Check all classes in all files to see if they use this loader as an attribute
        for (file_path, class_name), class_node in all_classes.items():
            # Skip the loader class itself
            if class_node == loader_node:
                continue
            
            # Check if this class uses the loader as an instance attribute
            if self._class_uses_as_attribute(class_node, loader_class_name, file_path):
                return True
        
        return False
    
    def _class_uses_as_attribute(self, class_node: ast.ClassDef, loader_class_name: str, file_path: Path) -> bool:
        """Check if a class uses the loader class as an instance attribute."""
        # Check imports first - if the loader class isn't imported, it can't be used
        try:
            content = file_path.read_text(encoding='utf-8')
            # Simple check: see if loader class name appears in the file
            if loader_class_name not in content:
                return False
        except (UnicodeDecodeError, IOError):
            return False
        
        for node in class_node.body:
            # Check __init__ for assignments like self.loader = LoaderClass()
            if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                for stmt in ast.walk(node):
                    if isinstance(stmt, ast.Assign):
                        for target in stmt.targets:
                            if isinstance(target, ast.Attribute):
                                if isinstance(target.value, ast.Name) and target.value.id == 'self':
                                    # Check if the assigned value is the loader class
                                    if isinstance(stmt.value, ast.Call):
                                        # Check direct call: LoaderClass()
                                        if isinstance(stmt.value.func, ast.Name) and stmt.value.func.id == loader_class_name:
                                            return True
                                        # Check attribute call: self.something.LoaderClass() or module.LoaderClass()
                                        if isinstance(stmt.value.func, ast.Attribute):
                                            if isinstance(stmt.value.func.attr, str) and stmt.value.func.attr == loader_class_name:
                                                return True
                                    # Also check for direct assignment: self.loader = LoaderClass
                                    if isinstance(stmt.value, ast.Name) and stmt.value.id == loader_class_name:
                                        return True
            
            # Check for type hints like loader: LoaderClass
            if isinstance(node, ast.AnnAssign):
                if isinstance(node.annotation, ast.Name) and node.annotation.id == loader_class_name:
                    return True
                # Check for self.loader: LoaderClass
                if isinstance(node.target, ast.Attribute):
                    if isinstance(node.target.value, ast.Name) and node.target.value.id == 'self':
                        if isinstance(node.annotation, ast.Name) and node.annotation.id == loader_class_name:
                            return True
                        # Check for qualified names like render_config_loader.RenderConfigLoader
                        if isinstance(node.annotation, ast.Attribute):
                            if node.annotation.attr == loader_class_name:
                                return True
            
            # Check for properties that return the loader type
            if isinstance(node, ast.FunctionDef):
                # Check if it's a property decorator
                is_property = any(
                    isinstance(dec, ast.Name) and dec.id == 'property'
                    for dec in node.decorator_list
                )
                if is_property:
                    # Check return type annotation
                    if node.returns:
                        if isinstance(node.returns, ast.Name) and node.returns.id == loader_class_name:
                            return True
                        # Check for qualified names
                        if isinstance(node.returns, ast.Attribute):
                            if node.returns.attr == loader_class_name:
                                return True
        
        return False




