"""Scanner for validating meaningful context is provided in names."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .code_scanner import CodeScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class MeaningfulContextScanner(CodeScanner):
    """Validates names provide meaningful context (no magic numbers, appropriate scope-based naming)."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Check for magic numbers
        violations.extend(self._check_magic_numbers(lines, file_path, rule_obj))
        
        # Check for numbered variables (data1, data2)
        violations.extend(self._check_numbered_variables(content, file_path, rule_obj))
        
        return violations
    
    def _check_magic_numbers(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for magic numbers (should be named constants)."""
        violations = []
        
        # Common magic numbers that should be constants
        magic_number_patterns = [
            r'\b(200|404|500)\b',  # HTTP status codes
            r'\b(86400|3600|60)\b',  # Time constants (seconds in day/hour/minute)
            r'\b(1024|2048|4096)\b',  # Size constants
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern in magic_number_patterns:
                if re.search(pattern, line):
                    # Check if it's already a constant definition
                    if '=' in line and ('const' in line or 'final' in line):
                        continue  # It's a constant definition, not magic number
                    
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Line {line_num} contains magic number - replace with named constant',
                        location=str(file_path),
                        line_number=line_num,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
                    break
        
        return violations
    
    def _check_numbered_variables(self, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for numbered variables (data1, data2, etc.) - ONLY actual variable names/identifiers, not strings, comments, or values."""
        violations = []
        
        try:
            # Parse the file as AST to get actual variable names (AST automatically excludes comments and string literals)
            tree = ast.parse(content, filename=str(file_path))
            
            numbered_var_pattern = re.compile(r'^\w+\d+$')  # word followed by number (entire match)
            
            def check_name(var_name: str, lineno: int):
                """Helper to check if a variable name matches the numbered pattern."""
                if numbered_var_pattern.match(var_name):
                    # Exclude common test patterns
                    if var_name.startswith('test') or var_name in ['test1', 'test2']:
                        return
                    violations.append(Violation(
                        rule=rule_obj,
                        violation_message=f'Line {lineno} uses numbered variable "{var_name}" - use meaningful descriptive name',
                        location=str(file_path),
                        line_number=lineno,
                        severity='warning'
                    ).to_dict())
            
            for node in ast.walk(tree):
                # Check variable names in assignments (left side only - the target)
                if isinstance(node, ast.Assign):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            check_name(target.id, target.lineno)
                        # Handle tuple unpacking: a, b = ...
                        elif isinstance(target, ast.Tuple):
                            for elt in target.elts:
                                if isinstance(elt, ast.Name):
                                    check_name(elt.id, elt.lineno)
                        # Handle attribute assignments: obj.attr = ... (check attr name)
                        elif isinstance(target, ast.Attribute):
                            if isinstance(target.attr, str) and numbered_var_pattern.match(target.attr):
                                check_name(target.attr, target.lineno)
                
                # Check function parameter names
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    for arg in node.args.args:
                        check_name(arg.arg, arg.lineno)
                    # Check keyword-only args
                    for arg in node.args.kwonlyargs:
                        check_name(arg.arg, arg.lineno)
                
                # Check for loop variables
                elif isinstance(node, (ast.For, ast.AsyncFor)):
                    if isinstance(node.target, ast.Name):
                        check_name(node.target.id, node.target.lineno)
                    elif isinstance(node.target, ast.Tuple):
                        for elt in node.target.elts:
                            if isinstance(elt, ast.Name):
                                check_name(elt.id, elt.lineno)
                
                # Check comprehension variables
                elif isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp)):
                    for generator in node.generators:
                        if isinstance(generator.target, ast.Name):
                            check_name(generator.target.id, generator.target.lineno)
                        elif isinstance(generator.target, ast.Tuple):
                            for elt in generator.target.elts:
                                if isinstance(elt, ast.Name):
                                    check_name(elt.id, elt.lineno)
                
                # Check class attributes (but not their values)
                elif isinstance(node, ast.ClassDef):
                    for item in node.body:
                        if isinstance(item, ast.Assign):
                            for target in item.targets:
                                if isinstance(target, ast.Name):
                                    check_name(target.id, target.lineno)
                                elif isinstance(target, ast.Attribute):
                                    if isinstance(target.attr, str) and numbered_var_pattern.match(target.attr):
                                        check_name(target.attr, target.lineno)
        
        except (SyntaxError, ValueError) as e:
            logger.debug(f'AST parsing failed for {file_path}, skipping numbered variable check: {type(e).__name__}: {e}')
        
        return violations
