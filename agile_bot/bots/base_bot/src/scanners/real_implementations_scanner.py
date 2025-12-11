"""Scanner for validating tests use real implementations."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .violation import Violation


class RealImplementationsScanner(TestScanner):
    """Detects fake/stub implementations and commented-out code.
    
    Tests should call production code directly, even if API doesn't exist yet.
    """
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # Check for fake/stub implementations
            violations.extend(self._check_fake_implementations(lines, test_file_path, rule_obj))
            
            # Check for commented-out production code calls
            violations.extend(self._check_commented_code(lines, test_file_path, rule_obj))
        
        except (UnicodeDecodeError, Exception):
            # Skip binary files or files with encoding issues
            pass
        
        return violations
    
    def _check_fake_implementations(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for fake/stub implementations."""
        violations = []
        
        fake_patterns = [
            r'\bfake\s*\w+',  # fake_user, fake_data
            r'\bstub\s*\w+',  # stub_service
            r'\bmock\s*\w+.*=.*Mock\(\)',  # mock_service = Mock()
            r'return\s+\{\}',  # return {} (stub return)
        ]
        
        for line_num, line in enumerate(lines, 1):
            for pattern in fake_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Line {line_num} uses fake/stub implementation - tests should call real production code directly',
                        location=str(file_path),
                        line_number=line_num,
                        severity='error'
                    ).to_dict()
                    violations.append(violation)
                    break
        
        return violations
    
    def _check_commented_code(self, lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check for commented-out production code calls."""
        violations = []
        
        for line_num, line in enumerate(lines, 1):
            # Check for commented-out function calls (production code)
            if line.strip().startswith('#') and ('(' in line and ')' in line):
                # Might be commented-out production code
                if not any(keyword in line.lower() for keyword in ['# given', '# when', '# then', '# arrange', '# act', '# assert']):
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=f'Line {line_num} has commented-out code - call production code directly, even if API doesn\'t exist yet',
                        location=str(file_path),
                        line_number=line_num,
                        severity='warning'
                    ).to_dict()
                    violations.append(violation)
        
        return violations

