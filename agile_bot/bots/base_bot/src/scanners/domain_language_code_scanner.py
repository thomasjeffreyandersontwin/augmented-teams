"""Scanner for validating domain-specific language in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .code_scanner import CodeScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class DomainLanguageCodeScanner(CodeScanner):
    """Validates that code uses domain-specific language, not generic terms.
    
    Uses knowledge graph to extract domain terms and validates that names match domain concepts.
    
    Exception: Classes ending with verb suffixes (Generator, Calculator, Builder, etc.) that have
    a domain-meaningful prefix (e.g., MCPServerGenerator, ComplexityCalculator) are allowed to use 
    generate_/calculate_ method names since building/generation is their domain purpose.
    Classes named just "Generator" or "Calculator" without a domain prefix are NOT exempt.
    """
    
    GENERATE_PATTERNS = [r'^generate_', r'^calculate_']
    
    # Common verb suffixes for builder/processor classes
    # e.g., MCPServerGenerator, ComplexityCalculator, BotToolBuilder, RequestHandler
    # These are allowed to use generate_/calculate_ methods IF they have a domain-meaningful prefix
    BUILDER_VERB_SUFFIXES = (
        'Generator', 'Calculator', 'Builder', 'Processor', 
        'Handler', 'Factory', 'Creator', 'Producer', 'Compiler'
    )
    
    def __init__(self):
        super().__init__()
        self.knowledge_graph = None
    
    def _is_builder_class_with_domain_prefix(self, class_name: Optional[str]) -> bool:
        """Check if class is a builder/generator class with a domain-meaningful prefix.
        
        Returns True for classes like MCPServerGenerator, ComplexityCalculator, BotToolBuilder
        Returns False for classes like Generator, Calculator (no domain prefix)
        """
        if not class_name:
            return False
        
        for suffix in self.BUILDER_VERB_SUFFIXES:
            if class_name.endswith(suffix):
                # Check that there's a prefix before the suffix (not just the suffix alone)
                prefix = class_name[:-len(suffix)]
                if prefix:  # Has a domain-meaningful prefix
                    return True
        return False
    
    def scan(self, knowledge_graph: Dict[str, Any], rule_obj: Any = None, test_files: Optional[List['Path']] = None, code_files: Optional[List['Path']] = None, on_file_scanned: Optional[Any] = None) -> List[Dict[str, Any]]:
        """Override scan to store knowledge_graph for use in scan_code_file."""
        self.knowledge_graph = knowledge_graph
        return super().scan(knowledge_graph, rule_obj, test_files=test_files, code_files=code_files, on_file_scanned=on_file_scanned)
    
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
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Process classes and their methods with context
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                class_violations = self._check_domain_language(node, file_path, rule_obj, domain_terms, generic_names)
                violations.extend(class_violations)
                
                # Check methods within this class, passing class context
                for child in node.body:
                    if isinstance(child, ast.FunctionDef):
                        func_violations = self._check_function_domain_language(
                            child, file_path, rule_obj, domain_terms, generic_names,
                            enclosing_class=node.name
                        )
                        violations.extend(func_violations)
        
        # Check module-level functions (no enclosing class)
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef):
                func_violations = self._check_function_domain_language(
                    node, file_path, rule_obj, domain_terms, generic_names,
                    enclosing_class=None
                )
                violations.extend(func_violations)
        
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
                                      domain_terms: set, generic_names: set, 
                                      enclosing_class: Optional[str] = None) -> List[Dict[str, Any]]:
        """Check if function uses domain-specific language."""
        violations = []
        func_name_lower = func_node.name.lower()
        
        # Skip generate/calculate check for builder/generator classes with domain prefix
        # e.g., MCPServerGenerator.generate_server() is legitimate
        skip_generate_check = self._is_builder_class_with_domain_prefix(enclosing_class)
        
        # Check for generate/calculate patterns (unless in a builder class)
        if not skip_generate_check:
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




