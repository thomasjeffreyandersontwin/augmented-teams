"""Scanner for validating class size (keep classes small)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
from .code_scanner import CodeScanner
from .violation import Violation
from .complexity_metrics import ComplexityMetrics


class ClassSizeScanner(CodeScanner):
    """Validates classes are small and free of dead code.
    
    Keep classes under 200-300 lines.
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
                    violation = self._check_class_size(node, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
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
        
        # 2. LCOM (Lack of Cohesion of Methods)
        lcom = ComplexityMetrics.calculate_lcom(class_node)
        if lcom > 0.7:
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=(
                    f'Class "{class_node.name}" has low cohesion (LCOM={lcom:.2f}) - '
                    f'methods don\'t share many attributes. Consider splitting into separate classes.'
                ),
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict())
        
        # 3. Method count
        method_count = len([n for n in class_node.body if isinstance(n, ast.FunctionDef)])
        if method_count > 20:
            line_number = class_node.lineno if hasattr(class_node, 'lineno') else None
            violations.append(Violation(
                rule=rule_obj,
                violation_message=(
                    f'Class "{class_node.name}" has {method_count} methods - '
                    f'consider if it has multiple responsibilities and should be split.'
                ),
                location=str(file_path),
                line_number=line_number,
                severity='info'
            ).to_dict())
        
        # 4. Responsibility detection
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
        
        # Return first violation (most critical)
        return violations[0] if violations else None

