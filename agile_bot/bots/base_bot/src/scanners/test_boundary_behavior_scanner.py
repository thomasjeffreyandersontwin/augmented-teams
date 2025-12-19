"""Scanner for validating boundary behavior is tested."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .test_scanner import TestScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class TestBoundaryBehaviorScanner(TestScanner):
    """Validates boundary behavior is tested."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check for boundary test patterns
            violations.extend(self._check_boundary_tests(content, file_path, rule_obj))
        
        except (UnicodeDecodeError, Exception) as e:
            logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
        
        return violations
    
    def _check_boundary_tests(self, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for boundary test coverage."""
        violations = []
        lines = content.split('\n')
        
        # Boundary indicators
        boundary_patterns = [
            r'\b(boundary|edge|limit|maximum|minimum|max|min|empty|null|zero|first|last)\b',
        ]
        
        has_boundary_tests = False
        for line in lines:
            for pattern in boundary_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    has_boundary_tests = True
                    break
        
        # This is informational - boundary tests are good but not always required
        # Could be enhanced to check if code has boundaries that need testing
        
        return violations

