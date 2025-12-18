"""Scanner for validating single responsibility principle."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation
from .complexity_metrics import ComplexityMetrics


class SingleResponsibilityScanner(CodeScanner):
    """Validates functions/classes follow single responsibility principle.
    
    Scans all files (test and production code) using AST-based responsibility detection.
    """
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    violation = self._check_function_sr(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
                elif isinstance(node, ast.ClassDef):
                    violation = self._check_class_sr(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_function_sr(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if function has single responsibility using AST analysis.
        
        Uses both name patterns and AST-based responsibility detection.
        """
        func_name = func_node.name.lower()
        
        # Skip test helper functions (even if they somehow got through)
        if func_name.startswith(('given_', 'when_', 'then_', 'test_')):
            return None
        
        violations = []
        
        # 1. Check name patterns (existing logic)
        name_violation = self._check_name_patterns(func_node, file_path, rule_obj)
        if name_violation:
            violations.append(name_violation)
        
        # 2. AST-based responsibility detection
        responsibilities = ComplexityMetrics.detect_responsibilities(func_node)
        if len(responsibilities) > 2:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=(
                    f'Function "{func_node.name}" has multiple responsibilities detected: {", ".join(responsibilities)}. '
                    f'Split into separate functions, each with a single responsibility.'
                ),
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict())
        
        # 3. Complexity metrics as indicators
        cyclomatic = ComplexityMetrics.cyclomatic_complexity(func_node)
        cognitive = ComplexityMetrics.cognitive_complexity(func_node)
        
        if cyclomatic > 10 or cognitive > 15:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=(
                    f'Function "{func_node.name}" has high complexity (cyclomatic={cyclomatic}, cognitive={cognitive}) - '
                    f'high complexity often indicates multiple responsibilities. Consider splitting.'
                ),
                location=str(file_path),
                line_number=line_number,
                severity='info'
            ).to_dict())
        
        # Return first violation (most specific)
        return violations[0] if violations else None
    
    def _check_name_patterns(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check function name for multiple responsibility patterns."""
        func_name = func_node.name.lower()
        
        action_verbs = [
            'validate', 'save', 'load', 'process', 'send', 'create', 'update', 'delete',
            'calculate', 'compute', 'transform', 'convert', 'parse', 'format', 'render',
            'execute', 'run', 'invoke', 'call', 'fetch', 'retrieve', 'store', 'write',
            'read', 'parse', 'build', 'generate', 'compile', 'extract', 'merge', 'split'
        ]
        
        # Check for pattern: action_verb_and_action_verb
        verbs_pattern = '|'.join(action_verbs)
        for verb in action_verbs:
            pattern = rf'\b{verb}_and_({verbs_pattern})\b'
            if re.search(pattern, func_name):
                line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Function "{func_node.name}" appears to have multiple responsibilities - split into separate functions',
                    location=str(file_path),
                    line_number=line_number,
                    severity='warning'
                ).to_dict()
        
        # Check camelCase pattern
        camel_case_pattern = r'([a-z]+)And([A-Z][a-z]+)'
        match = re.search(camel_case_pattern, func_node.name)
        if match:
            verb1 = match.group(1).lower()
            verb2 = match.group(2).lower()
            if verb1 in action_verbs and verb2 in action_verbs:
                line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Function "{func_node.name}" appears to have multiple responsibilities - split into separate functions',
                    location=str(file_path),
                    line_number=line_number,
                    severity='warning'
                ).to_dict()
        
        return None
    
    def _check_class_sr(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if class has single responsibility using AST analysis."""
        violations = []
        
        # 1. Method count (existing check)
        method_count = len([n for n in class_node.body if isinstance(n, ast.FunctionDef)])
        if method_count > 15:
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=f'Class "{class_node.name}" has {method_count} methods - consider if it has multiple responsibilities',
                location=str(file_path),
                line_number=line_number,
                severity='info'
            ).to_dict())
        
        # 2. LCOM (Lack of Cohesion of Methods) - measures how related methods are
        lcom = ComplexityMetrics.calculate_lcom(class_node)
        if lcom > 0.7:  # Low cohesion threshold
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=(
                    f'Class "{class_node.name}" has low cohesion (LCOM={lcom:.2f}) - '
                    f'methods don\'t share many attributes, suggesting multiple responsibilities. '
                    f'Consider splitting into separate classes.'
                ),
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict())
        
        # 3. Responsibility detection
        responsibilities = ComplexityMetrics.detect_class_responsibilities(class_node)
        if len(responsibilities) > 3:
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=(
                    f'Class "{class_node.name}" has multiple responsibilities detected: {", ".join(responsibilities)}. '
                    f'Split into separate classes, each with a single responsibility.'
                ),
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict())
        
        # Return first violation (most specific)
        return violations[0] if violations else None

