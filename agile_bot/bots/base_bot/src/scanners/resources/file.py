"""File resource representing a file to be scanned."""

from typing import List, Optional, TYPE_CHECKING
from pathlib import Path
import ast
import logging

if TYPE_CHECKING:
    from .line import Line
    from .block import Block
    from .scope import Scope
    from .violation import Violation

logger = logging.getLogger(__name__)


class File:
    """Represents a file to be scanned."""
    
    def __init__(self, path: Path, scope: 'Scope'):  # type: ignore
        """Initialize file.
        
        Args:
            path: Path to the file
            scope: Scope this file belongs to
        """
        self._path = path
        self._scope = scope
        self._lines: List['Line'] = []
        self._blocks: List['Block'] = []
        self._content: Optional[str] = None
        self._ast: Optional[ast.AST] = None
        self._block_extractor = None  # Will be set when needed
    
    @property
    def path(self) -> Path:
        """Get file path."""
        return self._path
    
    @property
    def scope(self) -> 'Scope':
        """Get scope this file belongs to."""
        return self._scope
    
    @property
    def lines(self) -> List['Line']:  # type: ignore
        """Get lines in this file."""
        if not self._lines and self._content:
            from .line import Line
            self._lines = [
                Line(self, i + 1, line_content)
                for i, line_content in enumerate(self._content.splitlines(keepends=True))
            ]
        return self._lines
    
    @property
    def blocks(self) -> List['Block']:
        """Get blocks in this file."""
        if not self._blocks:
            self._extract_blocks()
        return self._blocks
    
    @property
    def content(self) -> Optional[str]:
        """Get file content."""
        if self._content is None:
            self._load_content()
        return self._content
    
    def parse_safely(self) -> bool:
        """Parse file safely, handling errors.
        
        Returns:
            True if parsing succeeded, False otherwise
        """
        try:
            if self._content is None:
                self._load_content()
            
            if self._path.suffix == '.py' and self._content:
                self._ast = ast.parse(self._content, filename=str(self._path))
                return True
        except (SyntaxError, UnicodeDecodeError) as e:
            logger.debug(f'Skipping file {self._path} due to {type(e).__name__}: {e}')
            return False
        except Exception as e:
            logger.warning(f'Error parsing file {self._path}: {e}')
            return False
        
        return False
    
    def parse_python_file(self) -> Optional[ast.AST]:
        """Parse Python file and return AST.
        
        Returns:
            AST if successful, None otherwise
        """
        if self.parse_safely():
            return self._ast
        return None
    
    def is_test_file(self) -> bool:
        """Check if this is a test file.
        
        Returns:
            True if test file, False otherwise
        """
        path_str = str(self._path).lower()
        file_name = self._path.name.lower()
        
        # Check for test directories
        if '/test' in path_str or '/tests' in path_str or '\\test' in path_str or '\\tests' in path_str:
            return True
        
        # Check for test file patterns
        if file_name.startswith('test_') or file_name == 'conftest.py':
            return True
        
        return False
    
    def check_file_naming(self, file_naming_checker) -> List['Violation']:  # type: ignore
        """Check file naming using FileNamingChecker.
        
        Args:
            file_naming_checker: FileNamingChecker instance
            
        Returns:
            List of violations
        """
        return file_naming_checker.check_file_name_matches_sub_epic(self) + \
               file_naming_checker.validate_file_naming_conventions(self)
    
    def _load_content(self):
        """Load file content."""
        try:
            with open(self._path, 'r', encoding='utf-8') as f:
                self._content = f.read()
        except Exception as e:
            logger.warning(f'Error loading file {self._path}: {e}')
            self._content = ''
    
    def _extract_blocks(self):
        """Extract blocks from file using BlockExtractor."""
        from .block_extractor import BlockExtractor
        
        if self._block_extractor is None:
            self._block_extractor = BlockExtractor()
        
        self._blocks = self._block_extractor.extract_blocks_from_file(self)
        # Also set blocks on scope
        self._scope._blocks.extend(self._blocks)  # type: ignore

