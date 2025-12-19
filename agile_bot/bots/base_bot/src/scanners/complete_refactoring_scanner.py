"""Scanner for detecting incomplete refactoring (fallback/legacy support code)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import re
import logging
from .code_scanner import CodeScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class CompleteRefactoringScanner(CodeScanner):
    """Detects fallback/legacy support code that should be removed."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # Check for fallback/legacy support code with explicit comments
            violations.extend(self._check_fallback_legacy_support(lines, file_path, rule_obj))
        
        except (UnicodeDecodeError, Exception) as e:
            logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
        
        return violations
    
    def _check_fallback_legacy_support(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for fallback/legacy support code with explicit comments above it."""
        violations = []
        
        # Pattern to match comments that explicitly mention fallback or legacy
        fallback_comment_pattern = re.compile(
            r'#\s*(fallback|legacy).*',
            re.IGNORECASE
        )
        
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Check if this line is a comment mentioning fallback/legacy
            if fallback_comment_pattern.match(stripped):
                # Look ahead to find the actual code (not just more comments)
                code_line_num = None
                for next_line_num in range(line_num, min(line_num + 5, len(lines) + 1)):
                    if next_line_num > len(lines):
                        break
                    next_line = lines[next_line_num - 1].strip()
                    # Skip empty lines and comments
                    if next_line and not next_line.startswith('#'):
                        code_line_num = next_line_num
                        break
                
                if code_line_num:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Fallback/legacy support code found (comment at line {line_num}, code at line {code_line_num}) - complete refactoring by removing old pattern support',
                        location=str(file_path),
                        line_number=line_num,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
        
        return violations

