"""Scanner for validating encapsulation."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation


class EncapsulationScanner(CodeScanner):
    """Validates encapsulation (private fields, minimal public interface, Law of Demeter)."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    violation = self._check_encapsulation(node, content, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_encapsulation(self, class_node: ast.ClassDef, content: str, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if class follows encapsulation principles using AST-based analysis."""
        violations = []
        
        # Check each method in the class for Law of Demeter violations
        for node in class_node.body:
            if isinstance(node, ast.FunctionDef):
                method_violations = self._check_method_encapsulation(node, class_node.name, file_path, rule_obj)
                violations.extend(method_violations)
        
        # Return first violation found
        return violations[0] if violations else None
    
    def _check_method_encapsulation(self, method_node: ast.FunctionDef, class_name: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check method for Law of Demeter violations using AST."""
        violations = []
        
        # Find all method call chains in the method body
        for node in ast.walk(method_node):
            if isinstance(node, ast.Call):
                chain_depth = self._get_method_chain_depth(node)
                if chain_depth >= 3:  # 3+ levels is a violation
                    line_number = node.lineno if hasattr(node, 'lineno') else method_node.lineno
                    violations.append(Violation(
                        rule=rule_obj,
                        violation_message=(
                            f'Method "{method_node.name}" in class "{class_name}" has Law of Demeter violation '
                            f'(method chain depth {chain_depth}) - encapsulate access to related objects'
                        ),
                        location=str(file_path),
                        line_number=line_number,
                        severity='warning'
                    ).to_dict())
        
        return violations
    
    def _get_method_chain_depth(self, call_node: ast.Call) -> int:
        """Calculate the depth of a method call chain using AST.
        
        Returns the number of chained method calls (e.g., obj.method().method().method() = 3)
        
        In AST, a chain like obj.method1().method2().method3() is represented as:
        Call(func=Attribute(value=Call(func=Attribute(value=Call(...), attr='method2'), attr='method3')))
        """
        depth = 1  # The current call counts as 1
        
        # Traverse up the chain by following the func attribute
        current = call_node.func
        while isinstance(current, ast.Attribute):
            # If the value is another Call, that's a chained method call
            if isinstance(current.value, ast.Call):
                depth += 1
                # Continue traversing the inner call's func
                current = current.value.func
            else:
                # Not a method chain, just attribute access
                break
        
        return depth

