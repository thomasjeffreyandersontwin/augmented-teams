"""Scanner for detecting bad comments (commented-out code, outdated, misleading)."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import re
from .code_scanner import CodeScanner
from .violation import Violation


class BadCommentsScanner(CodeScanner):
    """Detects bad comments: commented-out code, outdated comments, misleading comments.
    
    CRITICAL: Some comments actively harm readability. Delete commented-out code (it's in git),
    remove misleading or outdated comments, and eliminate redundant noise.
    """
    
    def scan_code_file(self, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # Check for commented-out code blocks
            violations.extend(self._check_commented_code(lines, file_path, rule_obj))
            
            # Check for HTML markup in comments
            violations.extend(self._check_html_in_comments(lines, file_path, rule_obj))
            
            # Check for misleading TODO comments
            violations.extend(self._check_misleading_todos(lines, file_path, rule_obj))
        
        except (UnicodeDecodeError, Exception):
            # Skip binary files or files with encoding issues
            pass
        
        return violations
    
    def _check_commented_code(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for commented-out code blocks."""
        violations = []
        commented_block_start = None
        
        for line_num, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Check for commented-out function/class definitions
            if stripped.startswith('//') or stripped.startswith('#'):
                comment_content = stripped[2:].strip()
                
                # Check for function/class definitions in comments
                if re.search(r'\b(function|def|class|const|let|var)\s+\w+', comment_content):
                    if commented_block_start is None:
                        commented_block_start = line_num
                elif commented_block_start and (stripped.startswith('//') or stripped.startswith('#')):
                    # Continue commented block
                    pass
                else:
                    # End of commented block
                    if commented_block_start:
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Commented-out code block found (lines {commented_block_start}-{line_num-1}) - delete it, code is in git history',
                            location=str(file_path),
                            line_number=commented_block_start,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                        commented_block_start = None
            else:
                # Not a comment line - end any commented block
                if commented_block_start:
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Commented-out code block found (lines {commented_block_start}-{line_num-1}) - delete it, code is in git history',
                        location=str(file_path),
                        line_number=commented_block_start,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                    commented_block_start = None
        
        return violations
    
    def _check_html_in_comments(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for HTML markup in comments."""
        violations = []
        
        html_patterns = [
            r'<p>', r'</p>', r'<ul>', r'</ul>', r'<li>', r'</li>',
            r'<div>', r'</div>', r'<span>', r'</span>', r'<br>', r'<br/>'
        ]
        
        for line_num, line in enumerate(lines, 1):
            if '//' in line or '#' in line or '/*' in line:
                for pattern in html_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Line contains HTML markup in comment - remove HTML, use plain text',
                            location=str(file_path),
                            line_number=line_num,
                            severity='error'
                        ).to_dict()
                        violations.append(violation)
                        break
        
        return violations
    
    def _check_misleading_todos(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for misleading TODO comments."""
        violations = []
        
        for line_num, line in enumerate(lines, 1):
            if 'TODO' in line.upper() or 'FIXME' in line.upper():
                # Check if TODO says "needs to be implemented" but code exists
                if 'needs to be implemented' in line.lower() or 'not implemented' in line.lower():
                    # Check next few lines for actual implementation
                    next_lines = lines[line_num:line_num+5]
                    has_implementation = any(
                        re.search(r'\b(function|def|class|return|if|for|while)\b', l)
                        for l in next_lines
                    )
                    
                    if has_implementation:
                        violation = Violation(
                            rule=rule_obj,
                            violation_message=f'Misleading TODO comment: "{line.strip()}" - code IS implemented, update or delete TODO',
                            location=str(file_path),
                            line_number=line_num,
                            severity='warning'
                        ).to_dict()
                        violations.append(violation)
        
        return violations

