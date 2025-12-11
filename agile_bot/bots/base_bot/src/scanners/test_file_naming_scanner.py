"""Scanner for validating test file naming matches sub-epic names."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .violation import Violation


class TestFileNamingScanner(TestScanner):
    """Validates test file names match sub-epic names."""
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        # Extract sub-epic names from knowledge graph
        sub_epic_names = self._extract_sub_epic_names(knowledge_graph)
        
        # Get expected file name from sub-epic
        file_name = test_file_path.stem  # Without .py extension
        
        # Check if file name matches a sub-epic name
        violation = self._check_file_name_matches_sub_epic(file_name, sub_epic_names, test_file_path, rule_obj)
        if violation:
            violations.append(violation)
        
        return violations
    
    def _extract_sub_epic_names(self, knowledge_graph: Dict[str, Any]) -> List[str]:
        """Extract sub-epic names from knowledge graph."""
        sub_epic_names = []
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            sub_epics = epic.get('sub_epics', [])
            for sub_epic in sub_epics:
                sub_epic_name = sub_epic.get('name', '')
                if sub_epic_name:
                    # Convert to snake_case for comparison
                    snake_case = self._to_snake_case(sub_epic_name)
                    sub_epic_names.append(snake_case)
        return sub_epic_names
    
    def _to_snake_case(self, name: str) -> str:
        """Convert name to snake_case."""
        # Insert underscores before capital letters
        name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
        return name.lower().replace(' ', '_')
    
    def _check_file_name_matches_sub_epic(self, file_name: str, sub_epic_names: List[str], file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if test file name matches a sub-epic name."""
        # Remove 'test_' prefix if present
        name_without_prefix = file_name[5:] if file_name.startswith('test_') else file_name
        
        # Check if matches any sub-epic name
        matches = [name for name in sub_epic_names if name_without_prefix == name or name_without_prefix in name]
        
        if not matches:
            return Violation(
                rule=rule_obj,
                violation_message=f'Test file name "{file_name}" does not match any sub-epic name - file should be named test_<sub_epic_name>.py',
                location=str(file_path),
                severity='error'
            ).to_dict()
        
        return None

