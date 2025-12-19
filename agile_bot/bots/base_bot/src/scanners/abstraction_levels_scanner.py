"""Scanner for validating abstraction levels are maintained."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .code_scanner import CodeScanner

logger = logging.getLogger(__name__)


class AbstractionLevelsScanner(CodeScanner):
    """Validates abstraction levels are maintained (no mixing high-level with low-level details)."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    violation = self._check_mixed_abstraction_levels(node, content, file_path, rule_obj)
                    if violation:
                        violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError) as e:
            logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
        
        return violations
    
    def _check_mixed_abstraction_levels(self, func_node: ast.FunctionDef, content: str, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if function mixes abstraction levels."""
        func_source = ast.get_source_segment(content, func_node) or ''
        func_source_lower = func_source.lower()
        
        # High-level indicators
        has_high_level = any(keyword in func_source_lower for keyword in ['process', 'handle', 'orchestrate', 'coordinate', 'manage'])
        
        # Low-level indicators
        has_low_level = any(keyword in func_source_lower for keyword in ['sql', 'query', 'select', 'insert', 'update', 'delete', 'file', 'open', 'close', 'read', 'write'])
        
        # Mixed abstraction: has both high-level and low-level
        if has_high_level and has_low_level:
            line_number = func_node.lineno if hasattr(func_node, 'lineno') else None
            return self._create_violation_with_snippet(
                rule_obj=rule_obj,
                violation_message=f'Function "{func_node.name}" mixes high-level operations with low-level details - extract low-level details to separate functions',
                file_path=file_path,
                line_number=line_number,
                severity='warning',
                content=content,
                ast_node=func_node
            )
        
        return None

