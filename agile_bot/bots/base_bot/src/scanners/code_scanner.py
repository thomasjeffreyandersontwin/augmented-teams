"""Base CodeScanner class for validating source code files."""

from abc import abstractmethod
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path  # Needed at runtime for Path operations
import ast
from .scanner import Scanner
from .violation import Violation


class CodeScanner(Scanner):
    """Base class for code validation scanners.
    
    CodeScanners validate Python/JavaScript source code files against rules.
    Each scanner implements scan_file() (or scan_code_file() for backward compatibility) to check a single file.
    
    Unified Architecture:
    - Scanners should override scan_file() to scan individual files
    - The base Scanner.scan() will combine test_files and code_files and call scan_file() for each
    - scan_code_file() is kept for backward compatibility but delegates to scan_file()
    """
    
    def scan(
        self, 
        knowledge_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        """Scan files for rule violations.
        
        Validates rule_obj is provided, then delegates to base Scanner.scan() which
        combines files and calls scan_file() for each.
        
        Args:
            knowledge_graph: Story graph structure
            rule_obj: Rule object reference (required)
            test_files: List of file paths to scan
            code_files: List of file paths to scan
            on_file_scanned: Optional callback(file_path, violations, rule_obj) called after each file
            
        Returns:
            List of violation dictionaries
        """
        if not rule_obj:
            raise ValueError("rule_obj parameter is required for CodeScanner")
        
        # Use base Scanner.scan() which combines files and calls scan_file() for each
        violations = super().scan(knowledge_graph, rule_obj, test_files, code_files, on_file_scanned=on_file_scanned)
        return violations
    
    def scan_file(
        self,
        file_path: Path,
        rule_obj: Any = None,
        knowledge_graph: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Scan a single file for violations.
        
        Subclasses must override this method to implement scanning logic.
        
        Args:
            file_path: Path to file to scan (test or code file)
            rule_obj: Rule object reference (required)
            knowledge_graph: Optional knowledge graph (for context-aware scanning)
            
        Returns:
            List of violation dictionaries
        """
        if not rule_obj:
            raise ValueError("rule_obj parameter is required for CodeScanner")
        
        # Store knowledge_graph in instance for scanners that need it
        if knowledge_graph is not None:
            self.knowledge_graph = knowledge_graph
        
        # Default implementation - subclasses must override
        return []
    
    def _extract_domain_terms(self, knowledge_graph: Dict[str, Any]) -> set:
        """Extract domain language terms from story graph, epics, and stories.
        
        Enhanced version that extracts from domain_concepts, responsibilities, collaborators, and scenario steps.
        This matches the enhanced extraction from SpecificationMatchScanner.
        """
        domain_terms = set()
        
        # Add common domain terms that are legitimate in this codebase context
        # These are domain concepts, not technical jargon
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
        """Extract individual words from text, converting to lowercase.
        
        This method extracts words from text using regex to find word boundaries.
        """
        if not text:
            return set()
        
        import re
        # Split on spaces, underscores, hyphens, and other separators
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        return set(words)
    
    def _matches_domain_term(self, name: str, domain_terms: set) -> bool:
        """Check if a name matches any domain term using compound term matching.
        
        This method implements the same compound term matching logic from SpecificationMatchScanner.
        It checks if:
        1. Any word in the name matches a domain term
        2. Any domain term appears as a substring in the name (for compound terms)
        
        Args:
            name: Variable, function, or class name to check
            domain_terms: Set of domain terms from knowledge graph
            
        Returns:
            True if name matches any domain term, False otherwise
        """
        if not name or not domain_terms:
            return False
        
        name_lower = name.lower()
        
        # Extract words from name (handles snake_case, camelCase, etc.)
        name_words = self._extract_words_from_text(name)
        
        # Check if any domain term is a word in the name
        for domain_term in domain_terms:
            # Check if domain term is a word in the name
            if domain_term in name_words:
                return True
            # Check if domain term appears as substring (for compound terms)
            # e.g., "assigned_strategy" contains "strategy", "template_manager" contains "template"
            if domain_term in name_lower or name_lower in domain_term:
                return True
        
        return False
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None
    ) -> List[Dict[str, Any]]:
        """Scan across all code files for cross-file violations.
        
        Override this method in subclasses to detect violations that require
        analyzing multiple files together (e.g., duplication, inconsistent patterns,
        architectural violations).
        
        Args:
            rule_obj: Rule object reference
            test_files: List of test file paths to analyze together
            code_files: List of code file paths to analyze together
            
        Returns:
            List of violation dictionaries for cross-file issues
        """
        # Default implementation - subclasses override
        return []
    
    def _parse_code_file(self, file_path: Path) -> Optional[Tuple[str, ast.AST]]:
        """Parse a code file and return its content and AST tree.
        
        Reusable helper method for cross-file scanning.
        
        Args:
            file_path: Path to code file
            
        Returns:
            Tuple of (content, tree) or None if file cannot be parsed
        """
        if not file_path.exists():
            return None
        
        try:
            content = file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(file_path))
            return (content, tree)
        except (SyntaxError, UnicodeDecodeError):
            return None
    
    def _get_all_code_files_parsed(
        self, 
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None
    ) -> List[Tuple[Path, str, ast.AST]]:
        """Parse all code files and return list of (path, content, tree) tuples.
        
        Reusable helper method for cross-file scanning.
        Combines test_files and code_files into a single list.
        
        Args:
            test_files: List of test file paths
            code_files: List of code file paths
            
        Returns:
            List of tuples (file_path, content, tree) for successfully parsed files
        """
        parsed_files = []
        all_files = []
        if code_files:
            all_files.extend(code_files)
        if test_files:
            all_files.extend(test_files)
        
        for file_path in all_files:
            parsed = self._parse_code_file(file_path)
            if parsed:
                content, tree = parsed
                parsed_files.append((file_path, content, tree))
        
        return parsed_files
    
    def _extract_code_snippet(self, content: str, ast_node: Optional[ast.AST] = None, 
                             start_line: Optional[int] = None, end_line: Optional[int] = None,
                             context_before: int = 2, max_lines: int = 50) -> str:
        """Extract code snippet from an AST node or line range for display in violation messages.
        
        Works for both single-file (AST-based) and cross-file (line-based) scanners.
        
        Args:
            content: Full source code content as string
            ast_node: AST node to extract code for (FunctionDef, ClassDef, If, etc.) - optional
            start_line: Start line number (1-indexed) - used if ast_node not provided
            end_line: End line number (1-indexed) - used if ast_node not provided
            context_before: Number of lines before the node to include for context
            max_lines: Maximum number of lines to include (truncates if longer)
            
        Returns:
            Code snippet string formatted for markdown display
        """
        lines = content.split('\n')
        
        # Determine start and end lines
        if ast_node is not None:
            # Use AST node to determine lines
            start_line_0 = ast_node.lineno - 1 if hasattr(ast_node, 'lineno') and ast_node.lineno else 0
            
            # Get end line - use end_lineno if available (Python 3.8+), otherwise estimate
            if hasattr(ast_node, 'end_lineno') and ast_node.end_lineno:
                end_line_0 = ast_node.end_lineno  # end_lineno is 1-indexed, exclusive
            else:
                # Estimate end by finding the maximum line number in the subtree
                end_line_0 = start_line_0 + 1
                for node in ast.walk(ast_node):
                    if hasattr(node, 'lineno') and node.lineno:
                        end_line_0 = max(end_line_0, node.lineno)
        elif start_line is not None:
            # Use provided line numbers (1-indexed, convert to 0-indexed)
            start_line_0 = start_line - 1
            if end_line is not None:
                end_line_0 = end_line  # end_line is 1-indexed, exclusive (like end_lineno)
            else:
                end_line_0 = start_line_0 + 1
        else:
            # No information provided, return empty
            return ""
        
        # Extract code with context
        snippet_start = max(0, start_line_0 - context_before)
        snippet_end = min(len(lines), end_line_0 + 1)
        code_snippet = '\n'.join(lines[snippet_start:snippet_end])
        
        # Truncate if too long
        code_lines = code_snippet.split('\n')
        if len(code_lines) > max_lines:
            code_snippet = '\n'.join(code_lines[:max_lines]) + '\n    # ... (truncated)'
        
        return code_snippet
    
    def _create_violation_with_snippet(
        self, 
        rule_obj: Any,
        violation_message: str,
        file_path: Path,
        line_number: Optional[int] = None,
        severity: str = 'warning',
        content: Optional[str] = None,
        ast_node: Optional[ast.AST] = None,
        start_line: Optional[int] = None,
        end_line: Optional[int] = None,
        context_before: int = 2,
        max_lines: int = 50
    ) -> Dict[str, Any]:
        """Create a violation with code snippet automatically included.
        
        This helper method extracts code snippets and includes them in violation messages
        for both single-file (AST-based) and cross-file (line-based) scanners.
        
        Args:
            rule_obj: Rule object reference
            violation_message: Base violation message (snippet will be appended)
            file_path: Path to file where violation occurs
            line_number: Line number where violation occurs (1-indexed)
            severity: Severity level ('error', 'warning', 'info')
            content: Source code content (required if ast_node or start_line provided)
            ast_node: AST node to extract snippet from (for single-file scanners)
            start_line: Start line number (1-indexed) for snippet (for cross-file scanners)
            end_line: End line number (1-indexed) for snippet (for cross-file scanners)
            context_before: Number of lines before to include for context
            max_lines: Maximum number of lines to include
            
        Returns:
            Violation dictionary with code snippet included in message
        """
        from .violation import Violation
        
        # Extract code snippet if content and location info provided
        code_snippet = ""
        if content is not None:
            if ast_node is not None or start_line is not None:
                code_snippet = self._extract_code_snippet(
                    content=content,
                    ast_node=ast_node,
                    start_line=start_line,
                    end_line=end_line,
                    context_before=context_before,
                    max_lines=max_lines
                )
        
        # Build final message with snippet
        if code_snippet:
            final_message = f"{violation_message}\n\n```python\n{code_snippet}\n```"
        else:
            final_message = violation_message
        
        return Violation(
            rule=rule_obj,
            violation_message=final_message,
            location=str(file_path),
            line_number=line_number,
            severity=severity
        ).to_dict()

