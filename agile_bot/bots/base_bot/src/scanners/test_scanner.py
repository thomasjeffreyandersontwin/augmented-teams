"""Base TestScanner class for validating test files."""

from typing import List, Dict, Any, Optional, Tuple, TYPE_CHECKING
from pathlib import Path
import ast
from .scanner import Scanner
from .violation import Violation

if TYPE_CHECKING:
    from pathlib import Path as PathType


class TestScanner(Scanner):
    """Base class for test validation scanners.
    
    TestScanners scan test code files to verify test quality and test-story mapping.
    
    Test scanners validate:
    1. Test code files (test classes match stories, methods match scenarios)
    2. Test code quality (via code scanning)
    
    Unified Architecture:
    - Scanners should override scan_file() to scan individual files
    - The base Scanner.scan() will combine test_files and code_files and call scan_file() for each
    - scan_test_file() is kept for backward compatibility but delegates to scan_file()
    
    Note: TestScanner does NOT scan story nodes - it only scans test files.
    """
    
    def scan(
        self, 
        knowledge_graph: Dict[str, Any], 
        rule_obj: Any = None,
        test_files: Optional[List['Path']] = None,
        code_files: Optional[List['Path']] = None,
        on_file_scanned: Optional[Any] = None
    ) -> List[Dict[str, Any]]:
        """Scan files for violations.
        
        Delegates to base Scanner.scan() which combines files and calls scan_file() for each.
        TestScanner scans all files (test and code) using the unified architecture.
        
        Args:
            knowledge_graph: Story graph structure
            rule_obj: Rule object reference
            test_files: List of test file paths to scan
            code_files: List of code file paths to scan (also scanned by TestScanner)
            on_file_scanned: Optional callback(file_path, violations, rule_obj) called after each file
            
        Returns:
            List of violation dictionaries from file scanning
        """
        # Use base Scanner.scan() which combines files and calls scan_file() for each
        return super().scan(knowledge_graph, rule_obj, test_files, code_files, on_file_scanned=on_file_scanned)
    
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
            rule_obj: Rule object reference
            knowledge_graph: Optional knowledge graph (for context-aware scanning)
            
        Returns:
            List of violation dictionaries
        """
        # Default implementation - subclasses must override
        return []
    
    def scan_cross_file(
        self,
        rule_obj: Any = None,
        test_files: Optional[List[Path]] = None,
        code_files: Optional[List[Path]] = None,
        all_test_files: Optional[List[Path]] = None,
        all_code_files: Optional[List[Path]] = None
    ) -> List[Dict[str, Any]]:
        """Scan across all test files for cross-file violations.
        
        Override this method in subclasses to detect violations that require
        analyzing multiple files together (e.g., duplication, helper function
        placement, inconsistent naming patterns).
        
        Args:
            rule_obj: Rule object reference
            test_files: List of all test file paths to analyze together
            code_files: Not used by TestScanner (for CodeScanner)
            
        Returns:
            List of violation dictionaries for cross-file issues
        """
        # Default implementation - subclasses override
        return []
    
    def _parse_test_file(self, test_file_path: Path) -> Optional[Tuple[str, ast.AST]]:
        """Parse a test file and return its content and AST tree.
        
        Reusable helper method for cross-file scanning.
        
        Args:
            test_file_path: Path to test file
            
        Returns:
            Tuple of (content, tree) or None if file cannot be parsed
        """
        if not test_file_path.exists():
            return None
        
        try:
            content = test_file_path.read_text(encoding='utf-8')
            tree = ast.parse(content, filename=str(test_file_path))
            return (content, tree)
        except (SyntaxError, UnicodeDecodeError):
            return None
    
    def _read_and_parse_file(self, file_path: Path) -> Optional[Tuple[str, List[str], ast.AST]]:
        """Read and parse a file, returning content, lines, and AST tree.
        
        Common helper method used by many test scanners to avoid duplication.
        Handles file existence check, reading, parsing, and exception handling with logging.
        
        Args:
            file_path: Path to file
            
        Returns:
            Tuple of (content, lines, tree) or None if file cannot be read/parsed
        """
        import logging
        logger = logging.getLogger(__name__)
        
        if not file_path.exists():
            return None
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            tree = ast.parse(content, filename=str(file_path))
            return (content, lines, tree)
        except (SyntaxError, UnicodeDecodeError) as e:
            logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
            return None
    
    def _get_all_test_files_parsed(
        self, 
        test_files: Optional[List[Path]]
    ) -> List[Tuple[Path, str, ast.AST]]:
        """Parse all test files and return list of (path, content, tree) tuples.
        
        Reusable helper method for cross-file scanning.
        
        Args:
            test_files: List of test file paths
            
        Returns:
            List of tuples (file_path, content, tree) for successfully parsed files
        """
        parsed_files = []
        if test_files:
            for test_file_path in test_files:
                parsed = self._parse_test_file(test_file_path)
                if parsed:
                    content, tree = parsed
                    parsed_files.append((test_file_path, content, tree))
        return parsed_files

