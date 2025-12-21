"""Scanner for detecting useless comments in code."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import re
import logging
from agile_bot.bots.base_bot.src.scanners.code_scanner import CodeScanner
from agile_bot.bots.base_bot.src.scanners.violation import Violation

logger = logging.getLogger(__name__)


class UselessCommentsScanner(CodeScanner):
    """Detects useless AI-generated comments and docstrings.
    
    CRITICAL: Most comments are useless. Kill AI-generated docstrings that just
    repeat function names and parameters. Only write comments for complex
    non-obvious algorithms, business rules, warnings, or legal notices.
    """
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Check for useless docstrings
        violations.extend(self._check_useless_docstrings(content, file_path, rule_obj))
        
        # Check for useless inline comments
        violations.extend(self._check_useless_comments(lines, file_path, rule_obj))
        
        return violations
    
    def _check_useless_docstrings(self, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        # Pattern for docstrings (triple quotes)
        docstring_pattern = r'"""(.*?)"""'
        matches = re.finditer(docstring_pattern, content, re.DOTALL)
        
        for match in matches:
            docstring_content = match.group(1).strip()
            
            # Check if docstring is useless
            if self._is_useless_docstring(docstring_content, content, match.start()):
                line_number = content[:match.start()].count('\n') + 1
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT',
                    location=str(file_path),
                    line_number=line_number,
                    severity='error'
                ).to_dict()
                violations.append(violation)
        
        return violations
    
    def _check_useless_comments(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        
        useless_patterns = [
            r'#\s*(Load|Get|Set|Return|Execute|Perform|Handle|Process|Create|Delete|Update)\s+\w+',  # Obvious action comments
            r'#\s*(This|The)\s+(function|method|class|variable)\s+(does|gets|sets|returns)',  # "This function does X"
            r'#\s*(end|End)\s+(if|for|while|class|function)',  # Closing brace comments
            r'#\s*={10,}',  # Section dividers (10 or more = characters)
            r'#\s*(Changed|Modified|Added|Removed)\s+by:',  # Change history
        ]
        
        for line_num, line in enumerate(lines, 1):
            line_stripped = line.strip()
            
            # Skip empty lines and non-comment lines
            if not line_stripped.startswith('#'):
                continue
            
            # Check if comment is actually useful (explains WHY, not WHAT)
            if self._is_useful_comment(line_stripped, lines, line_num):
                continue
            
            # Check against useless patterns
            for pattern in useless_patterns:
                if re.search(pattern, line_stripped, re.IGNORECASE):
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Useless comment: "{line_stripped[:60]}" - delete it or improve the code instead',
                        location=str(file_path),
                        line_number=line_num,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                    break
        
        return violations
    
    def _is_useful_comment(self, comment_line: str, lines: List[str], line_num: int) -> bool:
        comment_lower = comment_line.lower()
        
        # Check for useful comment patterns
        useful_patterns = [
            r'\?',  # Questions indicate reasoning or explanation
            r'(because|since|due to|as|when|if|unless)',  # Explains reason
            r'(warning|caution|note|important|critical)',  # Warnings/notes
            r'(todo|fixme|hack|workaround)',  # TODO/FIXME with context
            r'(license|copyright|legal)',  # Legal notices
            r'(algorithm|complex|non-obvious)',  # Complex logic explanation
            r'(business rule|domain|requirement)',  # Business logic
        ]
        
        for pattern in useful_patterns:
            if re.search(pattern, comment_lower):
                return True
        
        # Check if comment explains something non-obvious in the following code
        if line_num < len(lines):
            next_line = lines[line_num].strip() if line_num < len(lines) else ""
            if re.search(r'\b(if|for|while|with)\s+[^:]+:', next_line):
                return True
        
        return False
    
    def _is_useless_docstring(self, docstring: str, content: str, docstring_start: int) -> bool:
        # Get the text immediately before the docstring (last 200 chars)
        before_docstring = content[:docstring_start]
        recent_context = before_docstring[-200:] if len(before_docstring) > 200 else before_docstring
        
        # Check if there's a function or class definition immediately before this docstring
        lines = recent_context.split('\n')
        
        # Check last few lines before docstring
        for i in range(len(lines) - 1, max(0, len(lines) - 5), -1):
            line = lines[i].strip()
            
            # Found a function or class definition
            if line.startswith('def ') or line.startswith('class '):
                # This docstring is under a function/class - KILL IT
                return True
            
            # If we hit actual code (not just whitespace/comments), stop looking
            if line and not line.startswith('#'):
                break
        
        # Check if this is a module-level docstring (very first thing in file)
        lines_before = before_docstring.strip()
        if not lines_before or lines_before.count('\n') == 0:
            # Module docstring at top of file is OK
            return False
        
        return False





