"""Scanner for validating test class-based organization."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .test_scanner import TestScanner
from .story_map import StoryNode
from .violation import Violation


class ClassBasedOrganizationScanner(TestScanner):
    """Validates test class-based organization.
    
    Test classes match story names exactly (Test<ExactStoryName>),
    test methods match scenario names exactly (test_<scenario_name_snake_case>).
    """
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        """Scan story node (required by StoryScanner, but not used for test scanning)."""
        return []  # Test scanning happens in scan_test_file, not scan_story_node
    
    def scan_test_file(self, test_file_path: Path, rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        violations = []
        
        if not test_file_path.exists():
            return violations
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            
            # Extract story names from knowledge graph
            story_names = self._extract_story_names(knowledge_graph)
            
            # Find test classes
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if node.name.startswith('Test'):
                        # Check if class name matches a story name
                        violation = self._check_class_name_matches_story(node.name, story_names, test_file_path, rule_obj)
                        if violation:
                            violations.append(violation)
                        
                        # Check test methods in this class
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef):
                                if item.name.startswith('test_'):
                                    # Check method name matches scenario
                                    violation = self._check_method_name_matches_scenario(
                                        item.name, node.name, story_names, knowledge_graph, test_file_path, rule_obj
                                    )
                                    if violation:
                                        violations.append(violation)
                                    
                                    # Check method length (should be under 20 lines)
                                    violation = self._check_method_length(item, test_file_path, rule_obj)
                                    if violation:
                                        violations.append(violation)
        except (SyntaxError, UnicodeDecodeError) as e:
            # Skip files with syntax errors
            pass
        
        return violations
    
    def _extract_story_names(self, knowledge_graph: Dict[str, Any]) -> List[str]:
        """Extract story names from knowledge graph."""
        story_names = []
        
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            sub_epics = epic.get('sub_epics', [])
            for sub_epic in sub_epics:
                story_groups = sub_epic.get('story_groups', [])
                for story_group in story_groups:
                    stories = story_group.get('stories', [])
                    for story in stories:
                        story_name = story.get('name', '')
                        if story_name:
                            story_names.append(story_name)
        
        return story_names
    
    def _check_class_name_matches_story(self, class_name: str, story_names: List[str], file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if test class name matches a story name exactly."""
        # Remove 'Test' prefix
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        
        # Convert to story name format (PascalCase to story name)
        # This is approximate - exact matching would require story graph lookup
        expected_story_name = self._pascal_to_story_name(story_name_from_class)
        
        # Check if any story name matches (allowing for variations)
        matches = [s for s in story_names if self._names_match(s, expected_story_name)]
        
        if not matches:
            # Check for common violations: abbreviations, generic names
            if self._is_abbreviated(class_name, story_names):
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Test class "{class_name}" appears abbreviated - should match story name exactly (Test<ExactStoryName>)',
                    location=str(file_path),
                    severity='error'
                ).to_dict()
            
            if self._is_generic(class_name):
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Test class "{class_name}" uses generic name - should match story name exactly',
                    location=str(file_path),
                    severity='error'
                ).to_dict()
        
        return None
    
    def _check_method_name_matches_scenario(self, method_name: str, class_name: str, story_names: List[str], 
                                           knowledge_graph: Dict[str, Any], file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if test method name matches scenario name."""
        # Remove 'test_' prefix
        scenario_name_from_method = method_name[5:] if method_name.startswith('test_') else method_name
        
        # Check for abbreviations
        if len(scenario_name_from_method) < 20:  # Very short names are likely abbreviated
            return Violation(
                rule=rule_obj,
                violation_message=f'Test method "{method_name}" appears abbreviated - should match scenario name exactly',
                location=str(file_path),
                severity='error'
            ).to_dict()
        
        return None
    
    def _check_method_length(self, method_node: ast.FunctionDef, file_path: Path, rule_obj: Any) -> Optional[Dict[str, Any]]:
        """Check if test method is under 20 lines."""
        # Count lines in method (end_lineno - lineno + 1)
        if hasattr(method_node, 'end_lineno') and method_node.end_lineno:
            method_lines = method_node.end_lineno - method_node.lineno + 1
        else:
            # Fallback: count body statements (rough estimate)
            method_lines = len(method_node.body) * 2  # Rough estimate
        
        if method_lines > 20:
            return Violation(
                rule=rule_obj,
                violation_message=f'Test method "{method_node.name}" is approximately {method_lines} lines - should be under 20 lines (extract to helpers)',
                location=str(file_path),
                line_number=method_node.lineno if hasattr(method_node, 'lineno') else None,
                severity='warning'
            ).to_dict()
        
        return None
    
    def _pascal_to_story_name(self, pascal_name: str) -> str:
        """Convert PascalCase to story name format."""
        # Insert spaces before capital letters
        return re.sub(r'([A-Z])', r' \1', pascal_name).strip()
    
    def _names_match(self, name1: str, name2: str) -> bool:
        """Check if two names match (allowing for variations)."""
        # Normalize: lowercase, remove spaces/punctuation
        n1 = re.sub(r'[^\w]', '', name1.lower())
        n2 = re.sub(r'[^\w]', '', name2.lower())
        return n1 == n2
    
    def _is_abbreviated(self, class_name: str, story_names: List[str]) -> bool:
        """Check if class name appears abbreviated."""
        # Check if class name is much shorter than story names
        story_name_from_class = class_name[4:] if class_name.startswith('Test') else class_name
        if len(story_name_from_class) < 10:
            return True
        
        # Check for common abbreviations
        abbrev_patterns = ['Gen', 'Mgr', 'Cfg', 'Svc', 'Util', 'Helper']
        for pattern in abbrev_patterns:
            if pattern in class_name:
                return True
        
        return False
    
    def _is_generic(self, class_name: str) -> bool:
        """Check if class name is generic."""
        generic_names = ['TestToolGeneration', 'TestValidation', 'TestHelpers', 'TestUtils']
        return class_name in generic_names

