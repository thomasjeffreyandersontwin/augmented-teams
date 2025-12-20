"""Scanner for validating class size (keep classes small)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import logging
from .code_scanner import CodeScanner
from .violation import Violation
from .complexity_metrics import ComplexityMetrics

logger = logging.getLogger(__name__)


class ClassSizeScanner(CodeScanner):
    """Validates classes are small and free of dead code.
    
    Keep classes under 200-300 lines.
    """
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                violation = self._check_class_size(node, file_path, rule_obj)
                if violation:
                    violations.append(violation)
        
        return violations
    
    def _check_class_size(self, class_node: ast.ClassDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if class exceeds size limit using comprehensive metrics."""
        violations = []
        
        # 1. Line count (existing check)
        if hasattr(class_node, 'end_lineno') and class_node.end_lineno:
            class_size = class_node.end_lineno - class_node.lineno + 1
        else:
            class_size = len(class_node.body) * 10
        
        if class_size > 300:
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=f'Class "{class_node.name}" is {class_size} lines - should be under 300 lines (extract related methods into separate classes)',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict())
        
        # 2. LCOM (Lack of Cohesion of Methods) - measures single responsibility via shared attributes
        # DISABLED: LCOM calculation commented out - not effective enough
        # Threshold 0.8 because LCOM now excludes simple getters and follows delegation
        # lcom = ComplexityMetrics.calculate_lcom(class_node)
        # if lcom > 0.8:
        #     line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
        #     violations.append(Violation(
        #         rule=rule_obj,
        #         violation_message=(
        #             f'Class "{class_node.name}" has low cohesion (LCOM={lcom:.2f}) - '
        #             f'methods don\'t share many attributes, suggesting multiple responsibilities. '
        #             f'Consider splitting into separate classes.'
        #         ),
        #         location=str(file_path),
        #         line_number=line_number,
        #         severity='warning'
        #     ).to_dict())
        
        # 3. Method count - DISABLED per user request
        # method_count = len([n for n in class_node.body if isinstance(n, ast.FunctionDef)])
        # if method_count > 15:
        #     line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
        #     violations.append(Violation(
        #         rule=rule_obj,
        #         violation_message=(
        #             f'Class "{class_node.name}" has {method_count} methods - '
        #             f'consider if it has multiple responsibilities and should be split.'
        #         ),
        #         location=str(file_path),
        #         line_number=line_number,
        #         severity='info'
        #     ).to_dict())
        
        # Return first violation (most critical)
        return violations[0] if violations else None

