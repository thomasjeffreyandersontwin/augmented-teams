"""Scanner for validating tests match specification scenarios."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .test_scanner import TestScanner
from .violation import Violation

logger = logging.getLogger(__name__)


class SpecificationMatchScanner(TestScanner):
    """Validates test methods, variables, and assertions match specification scenarios exactly."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        
        # Check test method names match specification
        violations.extend(self._check_test_method_names(tree, file_path, rule_obj))
        
        # Check variable names match specification (exact names)
        violations.extend(self._check_variable_names(tree, content, file_path, rule_obj))
        
        # Check assertions match specification exactly
        violations.extend(self._check_assertions(tree, content, file_path, rule_obj))
        
        # NEW: Knowledge graph integration - match tests to specification
        if knowledge_graph:
            violations.extend(self._check_specification_matches(tree, content, file_path, rule_obj, knowledge_graph))
        
        return violations
    
    def _check_test_method_names(self, tree: ast.AST, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check test method names describe behavior from specification.
        
        Test method names should clearly describe what behavior is being tested,
        matching the specification scenario. Vague names like 'test_init' or 'test_agent'
        are flagged.
        """
        violations = []
        
        vague_patterns = [
            r'^test_(init|setup|create|new|get|set|run|execute|do|handle|process|check|verify|test)$',
            r'^test_\w+_(init|setup|create|new|get|set|run|execute|do|handle|process|check|verify)$',
        ]
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                # Check if method name is too vague
                is_vague = False
                for pattern in vague_patterns:
                    if re.match(pattern, node.name, re.IGNORECASE):
                        is_vague = True
                        break
                
                # Also check if it's a thin wrapper delegating to helper
                # (these are acceptable even if name is vague)
                is_thin_wrapper = self._is_thin_wrapper(node)
                
                if is_vague and not is_thin_wrapper:
                    violations.append(self._create_violation_with_line_number(
                        rule_obj, file_path, node,
                        f'Test method "{node.name}" has vague name - should clearly describe behavior from specification scenario'
                    ))
        
        return violations
    
    def _is_thin_wrapper(self, test_node: ast.FunctionDef) -> bool:
        """Check if test method is a thin wrapper delegating to a helper function."""
        # If body is just a single statement (likely a function call), it's a thin wrapper
        if len(test_node.body) == 1:
            stmt = test_node.body[0]
            # Check if it's a function call or expression statement with a call
            if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Call):
                return True
            if isinstance(stmt, ast.Return) and isinstance(stmt.value, ast.Call):
                return True
        return False
    
    def _create_violation_with_line_number(
        self,
        rule_obj: Any,
        file_path: Path,
        node: ast.AST,
        message: str,
        severity: str = 'warning'
    ) -> Dict[str, Any]:
        """Create a violation with line number from AST node.
        
        Args:
            rule_obj: Rule object
            file_path: Path to file
            node: AST node (for line number)
            message: Violation message
            severity: Severity level ('error', 'warning', 'info')
            
        Returns:
            Violation dictionary
        """
        line_number = node.lineno if hasattr(node, 'lineno') else None
        return Violation(
            rule=rule_obj,
            violation_message=message,
            location=str(file_path),
            line_number=line_number,
            severity=severity
        ).to_dict()
    
    def _check_variable_names(self, tree: ast.AST, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check variable names match specification exactly.
        
        Flags generic variable names that don't match specification terminology.
        Test variables should use exact names from specification (e.g., 'agent_name' not 'name').
        """
        violations = []
        
        # Generic names that suggest mismatch with specification
        generic_names = ['data', 'result', 'value', 'item', 'obj', 'thing', 'name', 'root', 'path', 'config']
        
        # Extract test methods to check variable names within them
        test_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                test_methods.append(node)
        
        for test_method in test_methods:
            # Check variable assignments in this test method
            for child in ast.walk(test_method):
                if isinstance(child, ast.Assign):
                    for target in child.targets:
                        if isinstance(target, ast.Name):
                            var_name = target.id
                            # Check if it's a generic name
                            if var_name.lower() in generic_names:
                                # Check if it's part of a helper function call (these are OK)
                                if not self._is_in_helper_call(child, test_method):
                                    violations.append(self._create_violation_with_line_number(
                                        rule_obj, file_path, child,
                                        f'Line {child.lineno if hasattr(child, "lineno") else "?"} uses generic variable name "{var_name}" - use exact variable names from specification'
                                    ))
        
        return violations
    
    def _is_in_helper_call(self, assign_node: ast.Assign, test_method: ast.FunctionDef) -> bool:
        """Check if assignment is part of a helper function call (like verify_* or given_*)."""
        # Check if assignment value is a function call
        if isinstance(assign_node.value, ast.Call):
            func = assign_node.value.func
            if isinstance(func, ast.Name):
                func_name = func.id
                # Helper functions typically start with verify_, given_, when_, then_
                if func_name.startswith(('verify_', 'given_', 'when_', 'then_', 'create_', 'setup_')):
                    return True
            elif isinstance(func, ast.Attribute):
                func_name = func.attr
                if func_name.startswith(('verify_', 'given_', 'when_', 'then_', 'create_', 'setup_')):
                    return True
        return False
    
    def _check_assertions(self, tree: ast.AST, content: str, file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
        """Check assertions verify exactly what specification states.
        
        Flags assertions that check implementation details (private attributes, internal flags)
        or things not mentioned in specification.
        """
        violations = []
        
        # Patterns that suggest implementation detail assertions
        implementation_patterns = [
            r'\._(private|internal|_flag|_state|_cache)',
            r'\.called\b',  # Mock call checks
            r'\.assert_called',  # Mock assertion
            r'\._validate',  # Internal validation
        ]
        
        # Extract test methods to check assertions within them
        test_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                test_methods.append(node)
        
        for test_method in test_methods:
            # Check assertions in this test method
            for child in ast.walk(test_method):
                if isinstance(child, ast.Assert):
                    # Get the assertion as a string for pattern matching
                    assertion_line = self._get_assertion_line(child, content, child.lineno)
                    
                    # Check for implementation detail patterns
                    for pattern in implementation_patterns:
                        if re.search(pattern, assertion_line, re.IGNORECASE):
                            violations.append(self._create_violation_with_line_number(
                                rule_obj, file_path, child,
                                f'Line {child.lineno if hasattr(child, "lineno") else "?"} assertion checks implementation detail - verify exactly what specification states, no more, no less'
                            ))
                            break
        
        return violations
    
    def _get_assertion_line(self, assert_node: ast.Assert, content: str, line_num: int) -> str:
        """Get the line containing the assertion as a string."""
        lines = content.split('\n')
        if 1 <= line_num <= len(lines):
            return lines[line_num - 1]
        return ""
    
    def _check_specification_matches(self, tree: ast.AST, content: str, file_path: Path, 
                                    rule_obj: Any, knowledge_graph: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check if tests match specification scenarios from knowledge graph."""
        violations = []
        
        # Extract test methods
        test_methods = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_'):
                test_methods.append(node)
        
        # Extract domain terms from knowledge graph
        domain_terms = self._extract_domain_terms(knowledge_graph)
        
        for test_method in test_methods:
            # Extract scenario from docstring
            scenario = self._extract_scenario_from_docstring(test_method)
            
            # Find matching story/scenario in knowledge graph
            matching_story = self._find_matching_story(scenario, test_method.name, knowledge_graph)
            
            if matching_story:
                # Check if test variables match story terms
                variable_matches = self._check_variable_matches(test_method, matching_story, domain_terms, rule_obj, file_path)
                violations.extend(variable_matches)
                
                # Check if assertions match acceptance criteria
                assertion_matches = self._check_assertion_matches(test_method, matching_story, rule_obj, file_path)
                violations.extend(assertion_matches)
            elif scenario:
                # Test has scenario but no matching story found
                violations.append(self._create_violation_with_line_number(
                    rule_obj, file_path, test_method,
                    f'Test "{test_method.name}" has scenario but no matching story found in specification. '
                    f'Scenario: {scenario[:100]}...'
                ))
        
        return violations
    
    def _extract_domain_terms(self, knowledge_graph: Dict[str, Any]) -> set:
        """Extract domain terms from knowledge graph."""
        domain_terms = set()
        
        if not knowledge_graph:
            return domain_terms
        
        # Extract from epics and stories
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            if isinstance(epic, dict):
                epic_name = epic.get('name', '')
                if epic_name:
                    domain_terms.update(self._extract_words_from_text(epic_name))
                
                # Extract from domain_concepts in epic - CRITICAL: Must extract all domain terms
                domain_concepts = epic.get('domain_concepts', [])
                for concept in domain_concepts:
                    if isinstance(concept, dict):
                        concept_name = concept.get('name', '')
                        if concept_name:
                            # Add full concept name (lowercase) and snake_case version
                            domain_terms.add(concept_name.lower())
                            domain_terms.add(concept_name.lower().replace(' ', '_'))
                            # Add individual words
                            domain_terms.update(self._extract_words_from_text(concept_name))
                            
                            # Extract from responsibilities (contains domain terminology)
                            responsibilities = concept.get('responsibilities', [])
                            for resp in responsibilities:
                                if isinstance(resp, dict):
                                    resp_name = resp.get('name', '')
                                    if resp_name:
                                        domain_terms.update(self._extract_words_from_text(resp_name))
                            
                            # Extract from collaborators (other domain concepts)
                            collaborators = concept.get('collaborators', [])
                            for collab in collaborators:
                                if isinstance(collab, str):
                                    domain_terms.add(collab.lower())
                                    domain_terms.update(self._extract_words_from_text(collab))
                
                sub_epics = epic.get('sub_epics', [])
                for sub_epic in sub_epics:
                    if isinstance(sub_epic, dict):
                        sub_epic_name = sub_epic.get('name', '')
                        if sub_epic_name:
                            domain_terms.update(self._extract_words_from_text(sub_epic_name))
                        
                        # Extract from domain_concepts in sub_epic - CRITICAL: Must extract all domain terms
                        sub_epic_concepts = sub_epic.get('domain_concepts', [])
                        for concept in sub_epic_concepts:
                            if isinstance(concept, dict):
                                concept_name = concept.get('name', '')
                                if concept_name:
                                    # Add full concept name (lowercase) and snake_case version
                                    domain_terms.add(concept_name.lower())
                                    domain_terms.add(concept_name.lower().replace(' ', '_'))
                                    # Add individual words
                                    domain_terms.update(self._extract_words_from_text(concept_name))
                                    
                                    # Extract from responsibilities (contains domain terminology)
                                    responsibilities = concept.get('responsibilities', [])
                                    for resp in responsibilities:
                                        if isinstance(resp, dict):
                                            resp_name = resp.get('name', '')
                                            if resp_name:
                                                domain_terms.update(self._extract_words_from_text(resp_name))
                                    
                                    # Extract from collaborators (other domain concepts)
                                    collaborators = concept.get('collaborators', [])
                                    for collab in collaborators:
                                        if isinstance(collab, str):
                                            domain_terms.add(collab.lower())
                                            domain_terms.update(self._extract_words_from_text(collab))
                        
                        story_groups = sub_epic.get('story_groups', [])
                        for story_group in story_groups:
                            if isinstance(story_group, dict):
                                stories = story_group.get('stories', [])
                                for story in stories:
                                    if isinstance(story, dict):
                                        story_name = story.get('name', '')
                                        if story_name:
                                            domain_terms.update(self._extract_words_from_text(story_name))
                                        
                                        acceptance_criteria = story.get('acceptance_criteria', [])
                                        for ac in acceptance_criteria:
                                            if isinstance(ac, dict):
                                                ac_text = ac.get('criterion', '')
                                                if ac_text:
                                                    domain_terms.update(self._extract_words_from_text(ac_text))
                                            elif isinstance(ac, str):
                                                domain_terms.update(self._extract_words_from_text(ac))
                                        
                                        # Extract from scenario steps
                                        scenarios = story.get('scenarios', [])
                                        for scenario in scenarios:
                                            if isinstance(scenario, dict):
                                                steps = scenario.get('steps', [])
                                                for step in steps:
                                                    if isinstance(step, str):
                                                        domain_terms.update(self._extract_words_from_text(step))
        
        return domain_terms
    
    def _extract_words_from_text(self, text: str) -> set:
        """Extract individual words from text."""
        import re
        if not text:
            return set()
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return set(words)
    
    def _extract_scenario_from_docstring(self, test_method: ast.FunctionDef) -> Optional[str]:
        """Extract scenario text from test method docstring."""
        if not test_method.body:
            return None
        
        # Check first statement for docstring
        first_stmt = test_method.body[0]
        if isinstance(first_stmt, ast.Expr):
            if isinstance(first_stmt.value, ast.Constant) and isinstance(first_stmt.value.value, str):
                return first_stmt.value.value
            elif hasattr(ast, 'Str') and isinstance(first_stmt.value, ast.Str):
                return first_stmt.value.s
        
        return None
    
    def _find_matching_story(self, scenario: Optional[str], test_name: str, knowledge_graph: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Find matching story in knowledge graph based on scenario or test name."""
        if not knowledge_graph:
            return None
        
        # Extract scenario name from docstring if available
        scenario_name = None
        if scenario:
            # Look for "SCENARIO: <name>" pattern in docstring
            scenario_match = re.search(r'SCENARIO:\s*(.+?)(?:\n|$)', scenario, re.IGNORECASE)
            if scenario_match:
                scenario_name = scenario_match.group(1).strip()
        
        # Extract keywords from test name
        test_keywords = set(self._extract_words_from_text(test_name))
        
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            if isinstance(epic, dict):
                sub_epics = epic.get('sub_epics', [])
                for sub_epic in sub_epics:
                    if isinstance(sub_epic, dict):
                        story_groups = sub_epic.get('story_groups', [])
                        for story_group in story_groups:
                            if isinstance(story_group, dict):
                                stories = story_group.get('stories', [])
                                for story in stories:
                                    if isinstance(story, dict):
                                        # First, try to match by scenario name if we have one
                                        if scenario_name:
                                            story_scenarios = story.get('scenarios', [])
                                            for story_scenario in story_scenarios:
                                                if isinstance(story_scenario, dict):
                                                    story_scenario_name = story_scenario.get('name', '')
                                                    # Normalize both names for comparison (lowercase, remove extra spaces)
                                                    normalized_test_scenario = re.sub(r'\s+', ' ', scenario_name.lower().strip())
                                                    normalized_story_scenario = re.sub(r'\s+', ' ', story_scenario_name.lower().strip())
                                                    if normalized_test_scenario == normalized_story_scenario:
                                                        return story
                                        
                                        # Fallback: Check if test name matches story name
                                        story_name = story.get('name', '')
                                        story_keywords = set(self._extract_words_from_text(story_name))
                                        
                                        # Check if test name matches story name (significant overlap)
                                        if len(test_keywords.intersection(story_keywords)) >= 2:
                                            return story
        
        return None
    
    def _check_variable_matches(self, test_method: ast.FunctionDef, story: Dict[str, Any], 
                                domain_terms: set, rule_obj: Any, file_path: Path) -> List[Dict[str, Any]]:
        """Check if test variables match domain terms from story."""
        violations = []
        
        # Extract variable names from test
        variable_names = []
        for node in ast.walk(test_method):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variable_names.append((target.id, node.lineno if hasattr(node, 'lineno') else None))
        
        # Check if variables use domain terms
        for var_name, line_number in variable_names:
            var_name_lower = var_name.lower()
            
            # Skip generic names that are OK
            generic_names = {'self', 'result', 'value', 'data', 'item', 'obj', 'workspace', 'root', 'path', 'config'}
            if var_name_lower in generic_names:
                continue
            
            # Check if variable name contains domain terms
            # Extract words from variable name (handles snake_case, camelCase, etc.)
            var_words = set(self._extract_words_from_text(var_name))
            
            # Also check if any domain term appears as substring in variable name
            # (e.g., "assigned_strategy" contains "strategy", "template_manager" contains "template" and "manager")
            matches_domain_term = False
            for domain_term in domain_terms:
                # Check if domain term is a word in the variable name
                if domain_term in var_words:
                    matches_domain_term = True
                    break
                # Check if domain term appears as substring (for compound terms)
                if domain_term in var_name_lower or var_name_lower in domain_term:
                    matches_domain_term = True
                    break
            
            # Only flag if variable doesn't match any domain terms
            if not matches_domain_term:
                # Get sample domain terms for error message
                sample_terms = sorted(list(domain_terms))[:10]
                violations.append(self._create_violation_with_line_number(
                    rule_obj, file_path, test_method,
                    f'Variable "{var_name}" in test "{test_method.name}" doesn\'t match domain terms. '
                    f'Use terms from specification: {", ".join(sample_terms)}...',
                    'info'
                ))
        
        return violations
    
    def _check_assertion_matches(self, test_method: ast.FunctionDef, story: Dict[str, Any], 
                                 rule_obj: Any, file_path: Path) -> List[Dict[str, Any]]:
        """Check if assertions match acceptance criteria from story."""
        violations = []
        
        # Extract acceptance criteria from story
        acceptance_criteria = story.get('acceptance_criteria', [])
        if not acceptance_criteria:
            return violations
        
        # Extract assertions from test - including various forms
        assertions = []
        has_pytest_raises = False
        has_helper_assertions = False
        
        for node in ast.walk(test_method):
            # Direct assert statements
            if isinstance(node, ast.Assert):
                assertions.append(node)
            
            # pytest.raises() context managers (these are assertions)
            if isinstance(node, ast.With):
                for item in node.items:
                    if isinstance(item.context_expr, ast.Call):
                        func = item.context_expr.func
                        if isinstance(func, ast.Attribute):
                            if func.attr == 'raises':
                                # Check if it's pytest.raises
                                if isinstance(func.value, ast.Name) and func.value.id == 'pytest':
                                    has_pytest_raises = True
                        elif isinstance(func, ast.Name):
                            if func.id == 'raises':
                                has_pytest_raises = True
            
            # Helper function calls that contain assertions (then_*, verify_*, check_*)
            if isinstance(node, ast.Call):
                func = node.func
                func_name = None
                if isinstance(func, ast.Name):
                    func_name = func.id
                elif isinstance(func, ast.Attribute):
                    func_name = func.attr
                
                if func_name:
                    # Helper functions that typically contain assertions
                    if func_name.startswith(('then_', 'verify_', 'check_', 'assert_')):
                        has_helper_assertions = True
        
        # Count total assertion-like constructs
        total_assertions = len(assertions)
        if has_pytest_raises:
            total_assertions += 1
        if has_helper_assertions:
            total_assertions += 1
        
        # If test has no assertions but story has acceptance criteria, that's a violation
        if total_assertions == 0 and len(acceptance_criteria) > 0:
            violations.append(self._create_violation_with_line_number(
                rule_obj, file_path, test_method,
                f'Test "{test_method.name}" has no assertions but story has {len(acceptance_criteria)} acceptance criteria. '
                f'Add assertions to verify acceptance criteria.'
            ))
        
        return violations
    
    def scan_story_node(self, node: Any, rule_obj: Any) -> List[Dict[str, Any]]:
        """Scan story node for violations (required by StoryScanner)."""
        return []

