"""Scanner for validating business-readable test names."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
import logging
from .test_scanner import TestScanner
from .violation import Violation
from .resources.ast_elements import Functions

logger = logging.getLogger(__name__)


class BusinessReadableTestNamesScanner(TestScanner):
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        violations = []
        
        parsed = self._read_and_parse_file(file_path)
        if not parsed:
            return violations
        
        content, lines, tree = parsed
        domain_language = self._extract_domain_language(knowledge_graph)
        
        functions = Functions(tree)
        for function in functions.get_many_functions:
            self._check_test_function_node(function.node, file_path, rule_obj, domain_language, violations)
        
        return violations
    
    def _check_test_function_node(self, node: Any, file_path: Path, rule_obj: Any, domain_language: set, violations: list) -> None:
        if not isinstance(node, ast.FunctionDef):
            return
        
        if not node.name.startswith('test_'):
            return
        
        violation = self._check_business_readable(node.name, file_path, node, rule_obj, domain_language)
        if violation:
            violations.append(violation)
    
    def _extract_domain_language(self, knowledge_graph: Dict[str, Any]) -> set:
        domain_terms = set()
        
        common_domain_terms = {
            'json', 'data', 'param', 'params', 'parameter', 'parameters',
            'var', 'vars', 'variable', 'variables',
            'method', 'methods', 'class', 'classes', 'call', 'calls',
            'config', 'configuration', 'configurations',
            'agent', 'bot', 'workflow', 'story', 'epic', 'scenario', 'action',
            'behavior', 'rule', 'rules', 'validation', 'validate', 'scanner',
            'file', 'files', 'directory', 'directories', 'path', 'paths',
            'state', 'states', 'tool', 'tools', 'server', 'catalog', 'metadata'
        }
        domain_terms.update(common_domain_terms)
        
        if not knowledge_graph:
            return domain_terms
        
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            if isinstance(epic, dict):
                self._extract_domain_terms_from_epic(epic, domain_terms)
        
        return domain_terms
    
    def _extract_domain_terms_from_epic(self, epic: dict, domain_terms: set) -> None:
        epic_name = epic.get('name', '')
        if epic_name:
            domain_terms.update(self._extract_words_from_text(epic_name))
        
        sub_epics = epic.get('sub_epics', [])
        for sub_epic in sub_epics:
            if isinstance(sub_epic, dict):
                self._extract_domain_terms_from_sub_epic(sub_epic, domain_terms)
    
    def _extract_domain_terms_from_sub_epic(self, sub_epic: dict, domain_terms: set) -> None:
        sub_epic_name = sub_epic.get('name', '')
        if sub_epic_name:
            domain_terms.update(self._extract_words_from_text(sub_epic_name))
        
        story_groups = sub_epic.get('story_groups', [])
        for story_group in story_groups:
            if isinstance(story_group, dict):
                self._extract_domain_terms_from_story_group(story_group, domain_terms)
    
    def _extract_domain_terms_from_story_group(self, story_group: dict, domain_terms: set) -> None:
        stories = story_group.get('stories', [])
        for story in stories:
            if isinstance(story, dict):
                self._extract_domain_terms_from_story(story, domain_terms)
    
    def _extract_domain_terms_from_story(self, story: dict, domain_terms: set) -> None:
        story_name = story.get('name', '')
        if story_name:
            domain_terms.update(self._extract_words_from_text(story_name))
        
        acceptance_criteria = story.get('acceptance_criteria', [])
        for ac in acceptance_criteria:
            if isinstance(ac, dict):
                ac_text = ac.get('criterion', '')
                if ac_text:
                    domain_terms.update(self._extract_words_from_text(ac_text))
    
    def _extract_words_from_text(self, text: str) -> set:
        if not text:
            return set()
        
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return set(words)
    
    def _check_business_readable(self, test_name: str, file_path: Path, node: ast.FunctionDef, rule_obj: Any, domain_language: set) -> Optional[Dict[str, Any]]:
        name_without_prefix = test_name[5:] if test_name.startswith('test_') else test_name
        
        test_words = self._extract_words_from_text(name_without_prefix)
        
        # If ANY domain term matches, consider it business-readable and skip all technical jargon checks
        if domain_language and test_words:
            matching_domain_terms = test_words.intersection(domain_language)
            # If ANY domain term matches, skip all technical jargon checks
            # This prevents false positives for legitimate domain terms like 'param', 'method', 'data'
            if len(matching_domain_terms) >= 1:
                # Test name uses domain language - consider it business-readable
                return None
        
        # Read file content for snippet extraction
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception:
            content = None
        
        # Technical jargon indicators - only flag truly technical terms that are NOT domain language
        # These are implementation details, not domain concepts
        # Note: Terms like 'json', 'data', 'param', 'method', 'class', 'call' are now considered
        # legitimate domain terms when used in context (e.g., "agent_json", "planning_data")
        technical_terms = [
            'constructor', 'init', 'parse', 'serialize', 'deserialize',
            'xml', 'http', 'api', 'endpoint', 'request', 'response',
            'schema', 'transform', 'convert', 'encode', 'decode',
            'execute', 'invoke', 'function', 'obj', 'cfg'
        ]
        
        name_lower = name_without_prefix.lower()
        for term in technical_terms:
            if term in name_lower:
                if term in domain_language:
                    continue  # Skip - it's domain language
                
                # Only flag if it's clearly technical jargon (not part of a compound domain term)
                # For example, "parse_json" is technical, but "agent_json" is domain
                if self._is_clearly_technical_jargon(term, name_lower, domain_language):
                    line_number = node.lineno if hasattr(node, 'lineno') else None
                    if content:
                        return self._create_violation_with_snippet(
                            rule_obj=rule_obj,
                            violation_message=f'Test name "{test_name}" contains technical jargon "{term}" - use business-readable domain language instead',
                            file_path=file_path,
                            line_number=line_number,
                            severity='error',
                            content=content,
                            ast_node=node,
                            max_lines=3
                        )
                    else:
                        return Violation(
                            rule=rule_obj,
                            violation_message=f'Test name "{test_name}" contains technical jargon "{term}" - use business-readable domain language instead',
                            location=str(file_path),
                            line_number=line_number,
                            severity='error'
                        ).to_dict()
        
        # Only flag truly technical abbreviations, not domain terms
        technical_abbrevs = r'\b(init|cfg|obj|req|resp|api|http|xml)\b'
        if re.search(technical_abbrevs, name_lower):
            abbrev_matches = re.findall(technical_abbrevs, name_lower)
            is_domain_abbrev = any(abbrev in domain_language for abbrev in abbrev_matches)
            
            if not is_domain_abbrev:
                line_number = node.lineno if hasattr(node, 'lineno') else None
                if content:
                    return self._create_violation_with_snippet(
                        rule_obj=rule_obj,
                        violation_message=f'Test name "{test_name}" contains abbreviations - use full business-readable words',
                        file_path=file_path,
                        line_number=line_number,
                        severity='warning',
                        content=content,
                        ast_node=node,
                        max_lines=3
                    )
                else:
                    return Violation(
                        rule=rule_obj,
                        violation_message=f'Test name "{test_name}" contains abbreviations - use full business-readable words',
                        location=str(file_path),
                        line_number=line_number,
                        severity='warning'
                    ).to_dict()
        
        words = name_without_prefix.split('_')
        if len(words) < 3:
            line_number = node.lineno if hasattr(node, 'lineno') else None
            if content:
                return self._create_violation_with_snippet(
                    rule_obj=rule_obj,
                    violation_message=f'Test name "{test_name}" is too vague - add context about what happens and when',
                    file_path=file_path,
                    line_number=line_number,
                    severity='warning',
                    content=content,
                    ast_node=node,
                    max_lines=3
                )
            else:
                return Violation(
                    rule=rule_obj,
                    violation_message=f'Test name "{test_name}" is too vague - add context about what happens and when',
                    location=str(file_path),
                    line_number=line_number,
                    severity='warning'
                ).to_dict()
        
        return None
    
    def _is_clearly_technical_jargon(self, term: str, test_name_lower: str, domain_language: set) -> bool:
        # If term is in domain language, it's not technical jargon
        if term in domain_language:
            return False
        
        # Look for patterns like: <domain_term>_<term> or <term>_<domain_term>
        # Examples: "agent_json", "workflow_json", "planning_data", "story_graph_json"
        domain_prefixes = ['agent', 'bot', 'workflow', 'story', 'epic', 'scenario', 
                          'action', 'behavior', 'rule', 'validation', 'planning',
                          'config', 'state', 'tool', 'server', 'catalog']
        
        for prefix in domain_prefixes:
            if f'{prefix}_{term}' in test_name_lower:
                return False
            # Check if term precedes a domain term (e.g., "json_file" - but this is less common)
            if f'{term}_{prefix}' in test_name_lower and prefix in domain_language:
                return False
        
        domain_compound_patterns = [
            r'agent[_\s]json', r'workflow[_\s]json', r'story[_\s]graph[_\s]json',
            r'planning[_\s]data', r'config[_\s]data', r'validation[_\s]data',
            r'environment[_\s]var', r'working[_\s]area', r'bot[_\s]config',
            r'action[_\s]method', r'behavior[_\s]action', r'close[_\s]current[_\s]action'
        ]
        
        for pattern in domain_compound_patterns:
            if re.search(pattern, test_name_lower):
                # If the term appears near domain language, it's likely domain, not technical
                return False
        
        # If we get here, it's likely technical jargon
        return True

