"""Base TestScanner class for validating test files and story graph mapping."""

from typing import List, Dict, Any, Optional
from pathlib import Path
from .story_scanner import StoryScanner
from .violation import Violation


class TestScanner(StoryScanner):
    """Base class for test validation scanners.
    
    TestScanners extend StoryScanner to validate story graph structure,
    but also scan test code files to verify test-story mapping.
    
    Test scanners validate:
    1. Story graph structure (via StoryScanner)
    2. Test code files (test classes match stories, methods match scenarios)
    3. Test code quality (via code scanning)
    """
    
    def scan(self, knowledge_graph: Dict[str, Any], rule_obj: Any = None) -> List[Dict[str, Any]]:
        """Scan story graph and test files for violations.
        
        Args:
            knowledge_graph: Story graph structure + test file paths
            rule_obj: Rule object reference
            
        Returns:
            List of violation dictionaries from both story graph and test code
        """
        violations = []
        
        # First, scan story graph (via parent StoryScanner)
        story_violations = super().scan(knowledge_graph, rule_obj)
        violations.extend(story_violations)
        
        # Then, scan test files if provided
        test_files = knowledge_graph.get('test_files', [])
        for test_file_path in test_files:
            test_path = Path(test_file_path)
            if test_path.exists():
                code_violations = self.scan_test_file(test_path, rule_obj, knowledge_graph)
                violations.extend(code_violations)
        
        return violations
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Scan a test file for violations.
        
        Args:
            test_file_path: Path to test file
            rule_obj: Rule object reference
            knowledge_graph: Story graph for mapping verification
            
        Returns:
            List of violation dictionaries
        """
        # Default implementation - subclasses override
        return []

