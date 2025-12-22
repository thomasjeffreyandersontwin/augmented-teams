"""Scanner for validating that calculation timing is hidden in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class CalculationTimingCodeScanner(CodeScanner):
    
    TIMING_EXPOSURE_PATTERNS = [
        r'^calculate_',
        r'^compute_',
        r'^derive_',
        r'_cached_',
        r'_precomputed_',
        r'_pre_computed_',
        r'_on_demand_',
    ]
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                violation = self._check_timing_exposure(node, file_path, rule_obj)
                if violation:
                    violations.append(violation)
        
        return violations
    
    def _check_timing_exposure(self, func_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        func_name_lower = func_node.name.lower()
        
        for pattern in self.TIMING_EXPOSURE_PATTERNS:
            if re.search(pattern, func_name_lower):
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Function "{func_node.name}" exposes calculation timing. Use property with "get_" or no prefix instead (e.g., "total_value" not "calculate_total_value").',
                    location=str(file_path),
                    line_number=func_node.lineno,
                    severity='warning'
                ).to_dict()
        
        return None




