"""Scanner for validating business-readable test names."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .violation import Violation


class BusinessReadableTestNamesScanner(TestScanner):
    """Validates test names read like plain English business language.
    
    Use domain language stakeholders understand, not technical jargon.
    Test names should read naturally when spoken aloud.
    """
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if node.name.startswith('test_'):
                        # Check if test name is business-readable
                        violation = self._check_business_readable(node.name, test_file_path, node, rule_obj)
                        if violation:
                            violations.append(violation)
        
        except (SyntaxError, UnicodeDecodeError):
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if test name is business-readable (not technical jargon)."""
        # Remove 'test_' prefix
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
        # Technical jargon indicators
        technical_terms = [
            'constructor', 'init', 'parse', 'serialize', 'deserialize',
            'json', 'xml', 'http', 'api', 'endpoint', 'request', 'response',
            'schema', 'validate', 'transform', 'convert', 'encode', 'decode',
            'execute', 'invoke', 'call', 'method', 'function', 'class',
            'var', 'vars', 'obj', 'data', 'config', 'cfg', 'param', 'params'
        ]
        
        # Check for technical jargon
        name_lower = name_without_prefix.lower()
        for term in technical_terms:
            if term in name_lower:
                line_number = node.lineno if hasattr(node, 'lineno') else None
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Test name "{test_name}" contains technical jargon "{term}" - use business-readable domain language instead',
                    location=str(file_path),
                    line_number=line_number,
                    severity='error'
                ).to_dict()
        
        # Check for abbreviations (often technical)
        if re.search(r'\b(init|cfg|config|var|obj|param|req|resp|api|http|json|xml)\b', name_lower):
            line_number = node.lineno if hasattr(node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Test name "{test_name}" contains abbreviations - use full business-readable words',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict()
        
        # Check if name is too short/vague
        words = name_without_prefix.split('_')
        if len(words) < 3:
            line_number = node.lineno if hasattr(node, 'lineno') else None
            return Violation(
                rule=rule_obj,
                violation_message=f'Test name "{test_name}" is too vague - add context about what happens and when',
                location=str(file_path),
                line_number=line_number,
                severity='warning'
            ).to_dict()
        
        return None

