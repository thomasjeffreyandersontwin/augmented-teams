"""Scanner for validating intention-revealing names in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class IntentionRevealingNamesScanner(CodeScanner):
    """Validates that names clearly communicate purpose and usage.
    
    Names should answer 'why does this exist?' and be searchable and pronounceable.
    """
    
    def __init__(self):
        super().__init__()
        self.knowledge_graph = None
    
    def scan(self, knowledge_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None) -> List[Dict[str, Any]]:
        """Override scan to store knowledge_graph for use in scan_code_file."""
        self.knowledge_graph = knowledge_graph
        return super().scan(knowledge_graph, rule_obj, test_files=test_files, code_files=code_files)
    
    # Acceptable domain terms that are well-known and intention-revealing
    ACCEPTABLE_DOMAIN_TERMS = {
        'scan', 'scan_test_file', 'scan_code_file', 'scan_cross_file',  # Scanner interface methods
        'parse', 'render', 'build', 'load', 'save', 'read', 'write',  # Common operations
        'get', 'set', 'has', 'is', 'can',  # Common predicate/getter patterns
        'init', '__init__', '__str__', '__repr__', '__eq__',  # Special methods
    }
    
    # Acceptable generic names in specific contexts (e.g., callback parameters, event handlers)
    ACCEPTABLE_CONTEXT_NAMES = {
        'data',  # Acceptable in data processing contexts
        'value',  # Acceptable in transformation contexts
        'item',  # Acceptable in iteration contexts
        'result',  # Acceptable as return value name
    }
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        # Extract domain terms from knowledge graph (using enhanced extraction from CodeScanner base class)
        domain_terms = set()
        if self.knowledge_graph:
            domain_terms = self._extract_domain_terms(self.knowledge_graph)
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            # Build docstring line ranges to exclude from scanning
            docstring_ranges = self._get_docstring_ranges(tree)
            
            # Check variable names
            violations.extend(self._check_variable_names(tree, file_path, rule_obj, content, domain_terms, docstring_ranges))
            
            # Check function names
            violations.extend(self._check_function_names(tree, file_path, rule_obj, domain_terms))
            
            # Check class names
            violations.extend(self._check_class_names(tree, file_path, rule_obj, domain_terms))
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_variable_names(self, tree: ast.AST, file_path: Path, rule_obj: Any, content: str, domain_terms: set = None, docstring_ranges: List[tuple] = None) -> List[Dict[str, Any]]:
        """Check for poor variable names."""
        violations = []
        
        if domain_terms is None:
            domain_terms = set()
        if docstring_ranges is None:
            docstring_ranges = []
        
        # Generic names that should be flagged (excluding acceptable context names and domain terms)
        generic_names = ['info', 'thing', 'stuff', 'temp']
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                var_name = node.id
                
                # Skip if node is inside a docstring or comment
                if self._is_in_docstring_or_comment(node, content, docstring_ranges):
                    continue
                
                # Skip if it's a store context (assignment target) - check if it's acceptable in context
                if isinstance(node.ctx, ast.Store):
                    # Check if it's in an acceptable context (function parameter, callback, etc.)
                    if self._is_acceptable_in_context(node, tree, content):
                        continue
                
                # Check for single-letter names (except common loop counters)
                if len(var_name) == 1 and var_name not in ['i', 'j', 'k', 'n', 'm']:
                    # Check if it's in a small loop or acceptable context
                    if not self._is_in_small_loop(node) and not self._is_acceptable_in_context(node, tree, content):
                        line_number = node.lineno if hasattr(node, 'lineno') else None
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Variable "{var_name}" uses single-letter name - use intention-revealing name',
                            location=str(file_path),
                            line_number=line_number,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                
                # Check for generic names (excluding acceptable context names and domain terms)
                var_name_lower = var_name.lower()
                if var_name_lower in generic_names:
                    # Check if it's a domain term (acceptable)
                    if var_name_lower in domain_terms:
                        continue
                    # Check if it's acceptable in context
                    if not self._is_acceptable_in_context(node, tree, content):
                        line_number = node.lineno if hasattr(node, 'lineno') else None
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Variable "{var_name}" uses generic name - use intention-revealing name',
                            location=str(file_path),
                            line_number=line_number,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                # Also check if variable name matches domain terms using compound term matching
                elif domain_terms:
                    # Use compound term matching (from CodeScanner base class)
                    if self._matches_domain_term(var_name, domain_terms):
                        continue  # Matches domain term - likely acceptable
        
        return violations
    
    def _is_acceptable_in_context(self, node: ast.Name, tree: ast.AST, content: str) -> bool:
        """Check if variable name is acceptable in its context (e.g., callback parameters, event handlers)."""
        # Check if it's a function parameter (acceptable for generic names in some contexts)
        # This is a simplified check - in practice, you'd traverse the AST to find the function definition
        # For now, we'll be more lenient and only flag obvious violations
        
        # Check if variable is used in a lambda or callback context
        # (This is a simplified heuristic - full implementation would require AST traversal)
        return False
    
    def _check_function_names(self, tree: ast.AST, file_path: Path, rule_obj: Any, domain_terms: set = None) -> List[Dict[str, Any]]:
        """Check for poor function names."""
        violations = []
        
        if domain_terms is None:
            domain_terms = set()
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_name = node.name
                func_name_lower = func_name.lower()
                
                # Skip private methods and special methods
                if func_name.startswith('_') and func_name != '__init__':
                    continue
                
                # Check if it's an acceptable domain term
                if func_name_lower in self.ACCEPTABLE_DOMAIN_TERMS:
                    continue
                
                # Check if function name matches domain terms using compound term matching
                if domain_terms:
                    if self._matches_domain_term(func_name, domain_terms):
                        continue  # Matches domain term - likely acceptable
                
                # Check for generic names (excluding acceptable domain terms)
                generic_names = ['process', 'handle', 'do', 'execute', 'run', 'main']
                # Only flag if it's standalone generic name, not part of a descriptive name
                if func_name_lower in generic_names and len(func_name.split('_')) == 1:
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Function "{func_name}" uses generic name - use intention-revealing name that explains purpose',
                        location=str(file_path),
                        line_number=line_number,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
        
        return violations
    
    def _check_class_names(self, tree: ast.AST, file_path: Path, rule_obj: Any, domain_terms: set = None) -> List[Dict[str, Any]]:
        """Check for poor class names."""
        violations = []
        
        if domain_terms is None:
            domain_terms = set()
        
        # Acceptable class name patterns (e.g., Scanner, CodeScanner, TestScanner are OK)
        acceptable_class_patterns = ['Scanner', 'CodeScanner', 'TestScanner', 'StoryScanner']
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                class_name_lower = class_name.lower()
                
                # Check if it matches acceptable patterns (e.g., base class names)
                if any(pattern in class_name for pattern in acceptable_class_patterns):
                    continue
                
                # Check if class name matches domain terms using compound term matching
                if domain_terms:
                    if self._matches_domain_term(class_name, domain_terms):
                        continue  # Matches domain term - likely acceptable
                
                # Check for generic names (only flag if it's a standalone generic name)
                generic_names = ['Manager', 'Handler', 'Processor', 'Util', 'Helper', 'Service']
                # Only flag if class name IS the generic name or ends with it without descriptive prefix
                if class_name in generic_names:
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Class "{class_name}" uses generic name - use intention-revealing name that explains purpose',
                        location=str(file_path),
                        line_number=line_number,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                # Flag if class name ends with generic name without descriptive prefix (e.g., "MyHandler" is OK, "Handler" is not)
                elif any(class_name.endswith(g) and len(class_name) <= len(g) + 2 for g in generic_names):
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Class "{class_name}" uses generic name - use intention-revealing name that explains purpose',
                        location=str(file_path),
                        line_number=line_number,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
        
        return violations
    
    def _is_in_small_loop(self, node: ast.Name) -> bool:
        """Check if variable is used in a small loop (like for i in range(10))."""
        # Check parent nodes for For loops
        parent = getattr(node, 'parent', None)
        if parent and isinstance(parent, ast.For):
            # Check if it's a simple range loop or iteration over a small collection
            if isinstance(parent.iter, ast.Call):
                if isinstance(parent.iter.func, ast.Name) and parent.iter.func.id == 'range':
                    return True
            # Also allow iteration over small lists/tuples (common pattern)
            elif isinstance(parent.iter, (ast.List, ast.Tuple)):
                if len(parent.iter.elts) <= 5:  # Small collection
                    return True
        return False
    
    def _get_docstring_ranges(self, tree: ast.AST) -> List[tuple]:
        """Get line number ranges for all docstrings in the AST.
        
        Returns a list of (start_line, end_line) tuples for each docstring.
        """
        docstring_ranges = []
        
        def visit_node(node):
            """Recursively visit nodes to find docstrings."""
            # Check if this node has a body (function, class, module)
            if hasattr(node, 'body') and isinstance(node.body, list) and len(node.body) > 0:
                # Check if first statement is a docstring
                first_stmt = node.body[0]
                if isinstance(first_stmt, ast.Expr):
                    # Docstring is an expression with a constant string
                    if isinstance(first_stmt.value, (ast.Constant, ast.Str)):
                        # Get the string value
                        if isinstance(first_stmt.value, ast.Constant):
                            docstring_value = first_stmt.value.value
                        else:  # ast.Str (Python < 3.8)
                            docstring_value = first_stmt.value.s
                        
                        if isinstance(docstring_value, str):
                            # Get line numbers
                            start_line = first_stmt.lineno if hasattr(first_stmt, 'lineno') else None
                            if start_line:
                                # Count lines in docstring content
                                docstring_lines = docstring_value.count('\n')
                                # Add 1 for the content itself, and account for triple quotes (2 lines)
                                end_line = start_line + docstring_lines + 2
                                docstring_ranges.append((start_line, end_line))
            
            # Recursively visit child nodes
            for child in ast.iter_child_nodes(node):
                visit_node(child)
        
        visit_node(tree)
        return docstring_ranges
    
    def _is_in_docstring_or_comment(self, node: ast.AST, content: str, docstring_ranges: List[tuple]) -> bool:
        """Check if a node is inside a docstring or comment.
        
        Args:
            node: AST node to check
            content: Source code content
            docstring_ranges: List of (start_line, end_line) tuples for docstrings
            
        Returns:
            True if node is inside a docstring or comment, False otherwise
        """
        if not hasattr(node, 'lineno'):
            return False
        
        line_number = node.lineno
        
        # Check if line is within any docstring range
        for start_line, end_line in docstring_ranges:
            if start_line <= line_number <= end_line:
                return True
        
        # Check if line is a comment
        lines = content.split('\n')
        if line_number <= len(lines):
            line = lines[line_number - 1].strip()
            # Check if line starts with # (comment)
            if line.startswith('#'):
                return True
            # Check if line is part of a multi-line comment block (triple quotes in comments)
            # This is a heuristic - Python doesn't have true multi-line comments, but docstrings can appear as comments
            if line.startswith('"""') or line.startswith("'''"):
                return True
        
        return False

