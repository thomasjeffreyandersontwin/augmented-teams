"""Base Scanner class for validation rule scanners."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path
    from .resources.scan import Scan
    from .resources.scope import Scope
    from .resources.violation import Violation
    from agile_bot.bots.base_bot.src.actions.validate.rule import Rule
    from .resources.block import Block
    from .resources.file import File


class Scanner(ABC):
    """Base class for validation rule scanners.
    
    Scanners validate knowledge graphs against rules and return violations.
    Each scanner is associated with a specific rule and implements the scan method.
    
    Unified Architecture:
    - Scanners should implement scan_file() to scan individual files
    - The scan() method combines test_files and code_files, then calls scan_file() for each
    - This eliminates the distinction between test_files and code_files at the scanner level
    """
    
    def scan(
        self, 
        knowledge_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        """Scan knowledge graph for rule violations (file-by-file pass).
        
        This is the first pass where each file is scanned individually.
        
        Default implementation combines test_files and code_files, then calls scan_file()
        for each file. Subclasses can override to customize behavior.
        
        Args:
            knowledge_graph: The knowledge graph to validate (typically story-graph.json structure)
            rule_obj: Optional Rule object reference (for creating Violations with rule reference)
            test_files: Optional list of test file paths
            code_files: Optional list of code file paths
            on_file_scanned: Optional callback(file_path, violations) called after each file is scanned
            
        Returns:
            List of violation dictionaries or Violation objects, each containing:
            - rule: Rule object reference or rule name string
            - line_number: Line number where violation occurs (if applicable)
            - location: Location in knowledge graph (e.g., 'epics[0].name')
            - violation_message: Description of the violation
            - severity: Severity level ('error', 'warning', 'info')
            
        Raises:
            Exception: If scanner execution fails (exceptions should not be swallowed)
        """
        violations = []
        
        # Combine all files - unified architecture
        all_files = []
        if test_files:
            all_files.extend(test_files)
        if code_files:
            all_files.extend(code_files)
        
        # Scan each file using unified scan_file() method
        for file_path in all_files:
            if file_path and file_path.exists() and file_path.is_file():
                file_violations = self.scan_file(file_path, rule_obj, knowledge_graph)
                file_violations_list = file_violations if isinstance(file_violations, list) else [file_violations] if file_violations else []
                
                if file_violations_list:
                    violations.extend(file_violations_list)
                
                # Call callback immediately after each file is scanned
                if on_file_scanned:
                    on_file_scanned(file_path, file_violations_list, rule_obj)
        
        return violations
    
    def scan_file(
        self,
        file_path: 'Path',
        rule_obj: Any = None,
        knowledge_graph: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Scan a single file for violations (unified method for all file types).
        
        This is the unified method that replaces scan_test_file() and scan_code_file().
        Subclasses should override this method to implement file scanning logic.
        
        Default implementation returns empty list. Subclasses must override.
        
        Args:
            file_path: Path to file to scan (test or code file)
            rule_obj: Rule object reference (for creating Violations)
            knowledge_graph: Optional knowledge graph (for context-aware scanning)
            
        Returns:
            List of violation dictionaries for this file
        """
        # Default implementation - subclasses should override
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None
    ) -> List[Dict[str, Any]]:
        """Scan across all files for cross-file violations (second pass).
        
        This is the second pass where all files are analyzed together to detect
        patterns that span multiple files (e.g., duplication, inconsistent naming,
        helper functions that should be moved to different scope levels).
        
        Default implementation returns empty list. Override in subclasses to enable
        cross-file scanning.
        
        Args:
            rule_obj: Optional Rule object reference
            test_files: List of all test file paths to analyze together
            code_files: List of all code file paths to analyze together
            
        Returns:
            List of violation dictionaries or Violation objects for cross-file issues
        """
        return []
    
    def _is_test_file(self, file_path: 'Path') -> bool:
        """Check if a file is a test file (for context-aware scanning).
        
        This is a helper method for scanners that need to differentiate behavior
        between test and code files. The unified architecture scans all files,
        but scanners can use this to apply different rules or thresholds.
        
        Args:
            file_path: Path to file to check
            
        Returns:
            True if file appears to be a test file, False otherwise
        """
        if not file_path:
            return False
        
        path_str = str(file_path).lower()
        file_name = file_path.name.lower()
        
        # Check for test directories
        if '/test' in path_str or '/tests' in path_str or '\\test' in path_str or '\\tests' in path_str:
            return True
        
        # Check for test file patterns
        if file_name.startswith('test_') or file_name == 'conftest.py':
            return True
        
        return False
    
    # New resource-oriented methods
    
    def performs_scan_for_one_rule(
        self,
        scan: 'Scan',
        scope: 'Scope',
        rule: 'Rule'
    ) -> List['Violation']:
        """Perform scan for one rule (resource-oriented interface).
        
        This is the new resource-oriented method that works with Scan, Scope, and Rule.
        Scanners should override this method to implement their scanning logic.
        
        Args:
            scan: Scan instance to populate with violations
            scope: Scope containing files and blocks to scan
            rule: Rule to validate against
            
        Returns:
            List of Violation objects
        """
        violations = []
        
        # Iterate through files in scope
        for file in scope.files:
            # Parse file if needed
            if not file.parse_safely():
                continue
            
            # Get blocks from file
            for block in file.blocks:
                # Scan block for violations
                block_violations = self._scan_block(block, rule, scan)
                violations.extend(block_violations)
        
        return violations
    
    def _scan_block(
        self,
        block: 'Block',
        rule: 'Rule',
        scan: 'Scan'
    ) -> List['Violation']:
        """Scan a single block for violations.
        
        Subclasses should override this to implement block-level scanning.
        
        Args:
            block: Block to scan
            rule: Rule to validate against
            scan: Scan instance
            
        Returns:
            List of Violation objects
        """
        # Default implementation - subclasses should override
        return []
    
    def associated_with_rule(self, rule: 'Rule') -> bool:
        """Check if scanner is associated with rule.
        
        Args:
            rule: Rule to check
            
        Returns:
            True if scanner handles this rule
        """
        # Default implementation - subclasses can override
        return True
    
    # Helper methods for domain model responsibilities
    
    def checks_file_naming(self, file: 'File', file_naming_checker) -> List['Violation']:
        """Check file naming using FileNamingChecker.
        
        Args:
            file: File to check
            file_naming_checker: FileNamingChecker instance
            
        Returns:
            List of violations
        """
        return file.check_file_naming(file_naming_checker)
    
    def checks_class_naming(self, block: 'Block', class_naming_checker) -> List['Violation']:
        """Check class naming using ClassNamingChecker.
        
        Args:
            block: Block to check
            class_naming_checker: ClassNamingChecker instance
            
        Returns:
            List of violations
        """
        return block.check_class_naming(class_naming_checker)
    
    def checks_method_naming(self, block: 'Block', method_naming_checker) -> List['Violation']:
        """Check method naming using MethodNamingChecker.
        
        Args:
            block: Block to check
            method_naming_checker: MethodNamingChecker instance
            
        Returns:
            List of violations
        """
        return block.check_method_naming(method_naming_checker)
    
    def analyzes_code_structure(
        self,
        block: 'Block',
        code_structure_analyzer,
        pattern_collection = None
    ) -> List['Violation']:
        """Analyze code structure using CodeStructureAnalyzer.
        
        Args:
            block: Block to analyze
            code_structure_analyzer: CodeStructureAnalyzer instance
            pattern_collection: Optional PatternCollection for pattern matching
            
        Returns:
            List of violations
        """
        return block.analyze_structure(code_structure_analyzer)
    
    def examines_ast_for_violations(
        self,
        block: 'Block',
        code_structure_analyzer
    ) -> List['Violation']:
        """Examine AST for violations using CodeStructureAnalyzer.
        
        Args:
            block: Block to examine
            code_structure_analyzer: CodeStructureAnalyzer instance
            
        Returns:
            List of violations
        """
        return block.analyze_structure(code_structure_analyzer)
    
    def identifies_code_patterns(
        self,
        block: 'Block',
        pattern_collection,
        code_structure_analyzer
    ) -> List['Violation']:
        """Identify code patterns using PatternCollection and CodeStructureAnalyzer.
        
        Args:
            block: Block to analyze
            pattern_collection: PatternCollection instance
            code_structure_analyzer: CodeStructureAnalyzer instance
            
        Returns:
            List of violations
        """
        # This would use pattern_collection to match patterns in block content
        violations = []
        if pattern_collection and pattern_collection.matches_text(block.content):
            # Create violation if pattern matches
            pass
        return violations

