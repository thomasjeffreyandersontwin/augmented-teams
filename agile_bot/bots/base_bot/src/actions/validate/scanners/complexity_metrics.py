"""Shared complexity metrics calculations for scanners."""

from typing import Dict, List, Set, Optional
import ast


class ComplexityMetrics:
    """Calculate various complexity metrics for AST nodes."""
    
    @staticmethod
    def cyclomatic_complexity(func_node: ast.FunctionDef) -> int:
        """Calculate cyclomatic complexity (number of decision points).
        
        Counts: if, for, while, except, with, assert, boolean operators (and/or)
        """
        complexity = 1  # Base complexity
        
        for node in ast.walk(func_node):
            # Decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler, ast.With)):
                complexity += 1
            # Boolean operators add complexity
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1
            # Assertions add complexity
            elif isinstance(node, ast.Assert):
                complexity += 1
        
        return complexity
    
    @staticmethod
    def cognitive_complexity(func_node: ast.FunctionDef) -> int:
        """Calculate cognitive complexity (nested structures weighted more).
        
        Similar to cyclomatic but penalizes nesting more heavily.
        """
        complexity = 0
        nesting_level = 0
        
        def visit_node(node: ast.AST, level: int):
            nonlocal complexity
            
            # Increment complexity for decision points
            if isinstance(node, (ast.If, ast.For, ast.While, ast.ExceptHandler)):
                complexity += 1 + level  # Nesting adds to complexity
                # Visit children with increased nesting
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.With):
                complexity += 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level + 1)
            elif isinstance(node, ast.BoolOp):
                complexity += len(node.values) - 1 + level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level)
            elif isinstance(node, ast.Assert):
                complexity += 1 + level
            else:
                # Visit children at same nesting level
                for child in ast.iter_child_nodes(node):
                    visit_node(child, level)
        
        for stmt in func_node.body:
            visit_node(stmt, 0)
        
        return complexity
    
    @staticmethod
    def max_nesting_depth(func_node: ast.FunctionDef) -> int:
        """Calculate maximum nesting depth in function."""
        max_depth = 0
        
        def visit_node(node: ast.AST, depth: int):
            nonlocal max_depth
            max_depth = max(max_depth, depth)
            
            # Increase depth for nested structures
            if isinstance(node, (ast.If, ast.For, ast.While, ast.With, ast.Try, ast.FunctionDef)):
                for child in ast.iter_child_nodes(node):
                    visit_node(child, depth + 1)
            else:
                for child in ast.iter_child_nodes(node):
                    visit_node(child, depth)
        
        for stmt in func_node.body:
            visit_node(stmt, 0)
        
        return max_depth
    
    @staticmethod
    def detect_responsibilities(func_node: ast.FunctionDef) -> List[str]:
        """Detect multiple responsibilities in function implementation.
        
        Returns list of responsibility types found:
        - 'I/O': File/network operations
        - 'Validation': Validation/checking logic
        - 'Transformation': Data transformation
        - 'Computation': Calculations
        - 'StateManagement': State changes
        """
        responsibilities = set()
        
        for node in ast.walk(func_node):
            # I/O operations
            if isinstance(node, ast.Call):
                func_name = ComplexityMetrics._get_call_name(node)
                if func_name:
                    io_keywords = ['open', 'read', 'write', 'load', 'save', 'fetch', 'request', 'post', 'get']
                    if any(keyword in func_name.lower() for keyword in io_keywords):
                        responsibilities.add('I/O')
            
            # Validation (assertions, checks, validations)
            if isinstance(node, ast.Assert):
                responsibilities.add('Validation')
            
            # Transformation (assignments with operations)
            if isinstance(node, ast.Assign):
                if ComplexityMetrics._has_transformation(node):
                    responsibilities.add('Transformation')
            
            # Computation (math operations)
            if isinstance(node, (ast.BinOp, ast.UnaryOp)):
                responsibilities.add('Computation')
        
        return sorted(list(responsibilities))
    
    @staticmethod
    def _get_call_name(call_node: ast.Call) -> Optional[str]:
        """Extract function name from call node."""
        if isinstance(call_node.func, ast.Name):
            return call_node.func.id
        elif isinstance(call_node.func, ast.Attribute):
            return call_node.func.attr
        return None
    
    @staticmethod
    def _has_transformation(assign_node: ast.Assign) -> bool:
        """Check if assignment involves transformation."""
        if not assign_node.value:
            return False
        
        # Check for function calls (likely transformations)
        if isinstance(assign_node.value, ast.Call):
            return True
        
        # Check for operations
        if isinstance(assign_node.value, (ast.BinOp, ast.UnaryOp, ast.ListComp, ast.DictComp)):
            return True
        
        return False
    
    @staticmethod
    def calculate_lcom(class_node: ast.ClassDef) -> float:
        """Calculate Lack of Cohesion of Methods (LCOM) metric.
        
        LCOM measures how related methods are. Lower is better (more cohesive).
        Returns value between 0 and 1, where 0 = perfect cohesion.
        """
        methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
        
        if len(methods) < 2:
            return 0.0  # Single method or no methods = perfect cohesion
        
        # Get attributes accessed by each method
        method_attributes = []
        for method in methods:
            attrs = ComplexityMetrics._get_accessed_attributes(method, class_node)
            method_attributes.append(attrs)
        
        # Count pairs of methods that don't share attributes
        non_shared_pairs = 0
        total_pairs = 0
        
        for i in range(len(method_attributes)):
            for j in range(i + 1, len(method_attributes)):
                total_pairs += 1
                if not (method_attributes[i] & method_attributes[j]):
                    non_shared_pairs += 1
        
        if total_pairs == 0:
            return 0.0
        
        # LCOM = ratio of non-shared pairs to total pairs
        return non_shared_pairs / total_pairs
    
    @staticmethod
    def _get_accessed_attributes(method_node: ast.FunctionDef, class_node: ast.ClassDef) -> Set[str]:
        """Get set of class attributes accessed by method."""
        attributes = set()
        
        # Get class attribute names
        class_attrs = set()
        for node in class_node.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        class_attrs.add(target.id)
        
        # Find attribute accesses in method
        for node in ast.walk(method_node):
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name) and node.value.id == 'self':
                    attributes.add(node.attr)
            elif isinstance(node, ast.Name):
                if node.id in class_attrs:
                    attributes.add(node.id)
        
        return attributes
    
    @staticmethod
    def detect_class_responsibilities(class_node: ast.ClassDef) -> List[str]:
        """Detect multiple responsibilities in class by analyzing method groups."""
        methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
        
        if len(methods) == 0:
            return []
        
        # Group methods by responsibility type
        responsibility_groups = {}
        
        for method in methods:
            responsibilities = ComplexityMetrics.detect_responsibilities(method)
            if not responsibilities:
                responsibilities = ['General']
            
            for resp in responsibilities:
                if resp not in responsibility_groups:
                    responsibility_groups[resp] = []
                responsibility_groups[resp].append(method.name)
        
        # If methods are spread across many responsibility types, class has multiple responsibilities
        if len(responsibility_groups) > 3:
            return list(responsibility_groups.keys())
        
        return []








