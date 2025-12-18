"""Scanner for validating domain-specific language in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class DomainLanguageCodeScanner(CodeScanner):
    """Validates that code uses domain-specific language, not generic terms.
    
    Uses knowledge graph to extract domain terms and validates that names match domain concepts.
    """
    
    GENERATE_PATTERNS = [r'^generate_', r'^calculate_']
    
    def __init__(self):
        super().__init__()
        self.knowledge_graph = None
    
    def scan(self, knowledge_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None) -> List[Dict[str, Any]]:
        """Override scan to store knowledge_graph for use in scan_code_file."""
        self.knowledge_graph = knowledge_graph
        return super().scan(knowledge_graph, rule_obj, test_files=test_files, code_files=code_files)
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        # Extract domain terms from knowledge graph
        domain_terms = set()
        if self.knowledge_graph:
            domain_terms = self._extract_domain_terms(self.knowledge_graph)
        
        # Generic names that are acceptable in specific contexts
        generic_names = {'self', 'result', 'value', 'data', 'item', 'obj', 'workspace', 'root', 'path', 'config'}
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    class_violations = self._check_domain_language(node, file_path, rule_obj, domain_terms, generic_names)
                    violations.extend(class_violations)
                elif isinstance(node, ast.FunctionDef):
                    func_violations = self._check_function_domain_language(node, file_path, rule_obj, domain_terms, generic_names)
                    violations.extend(func_violations)
        
        except (SyntaxError, UnicodeDecodeError):
            pass
        
        return violations
    
    def _check_domain_language(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any, 
                               domain_terms: set, generic_names: set) -> List[Dict[str, Any]]:
        """Check if class uses domain-specific language."""
        violations = []
        class_name = class_node.name
        
        # Skip if class name is in generic names (acceptable)
        if class_name.lower() in generic_names:
            return violations
        
        # Check if class name matches domain terms (using compound term matching)
        if domain_terms and not self._matches_domain_term(class_name, domain_terms):
            # Get sample domain terms for error message
            sample_terms = sorted(list(domain_terms))[:10]
            violations.append(
                Violation(
                    rule=rule_obj,
                    violation_message=(
                        f'Class "{class_name}" doesn\'t match domain terms. '
                        f'Use domain-specific language from specification: {", ".join(sample_terms)}...'
                    ),
                    location=str(file_path),
                    line_number=class_node.lineno,
                    severity='info'
                ).to_dict()
            )
        
        return violations
    
    def _check_function_domain_language(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any,
                                      domain_terms: set, generic_names: set) -> List[Dict[str, Any]]:
        """Check if function uses domain-specific language."""
        violations = []
        func_name_lower = func_node.name.lower()
        
        # Check for generate/calculate patterns
        for pattern in self.GENERATE_PATTERNS:
            if re.search(pattern, func_name_lower):
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Function "{func_node.name}" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").',
                        location=str(file_path),
                        line_number=func_node.lineno,
                        severity='warning'
                    ).to_dict()
                )
        
        # Check function name matches domain terms
        if domain_terms and not self._matches_domain_term(func_node.name, domain_terms):
            # Skip if function name is in generic names (acceptable)
            if func_node.name.lower() not in generic_names:
                sample_terms = sorted(list(domain_terms))[:10]
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=(
                            f'Function "{func_node.name}" doesn\'t match domain terms. '
                            f'Use domain-specific language from specification: {", ".join(sample_terms)}...'
                        ),
                        location=str(file_path),
                        line_number=func_node.lineno,
                        severity='info'
                    ).to_dict()
                )
        
        # Check parameters for generic terms (only if not matching domain terms)
        for arg in func_node.args.args:
            arg_name_lower = arg.arg.lower()
            # Skip if parameter is in generic names (acceptable)
            if arg_name_lower in generic_names:
                continue
            
            # Check if parameter matches domain terms
            if domain_terms and not self._matches_domain_term(arg.arg, domain_terms):
                sample_terms = sorted(list(domain_terms))[:10]
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=(
                            f'Function "{func_node.name}" uses parameter name "{arg.arg}" that doesn\'t match domain terms. '
                            f'Use domain-specific language: {", ".join(sample_terms)}...'
                        ),
                        location=str(file_path),
                        line_number=func_node.lineno,
                        severity='info'
                    ).to_dict()
                )
        
        return violations




