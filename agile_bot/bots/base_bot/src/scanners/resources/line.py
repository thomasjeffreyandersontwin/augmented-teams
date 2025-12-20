"""Line resource representing a line in a file."""

from typing import Optional


class Line:
    """Represents a line in a file."""
    
    def __init__(self, file: 'File', number: int, content: str):
        """Initialize line.
        
        Args:
            file: File this line belongs to
            number: Line number (1-based)
            content: Line content
        """
        self._file = file
        self._number = number
        self._content = content
    
    @property
    def file(self) -> 'File':
        """Get file this line belongs to."""
        return self._file
    
    @property
    def number(self) -> int:
        """Get line number."""
        return self._number
    
    @property
    def content(self) -> str:
        """Get line content."""
        return self._content
    
    def extract_from_ast_node(self, node) -> Optional[int]:
        """Extract line number from AST node.
        
        Args:
            node: AST node
            
        Returns:
            Line number if available, None otherwise
        """
        return getattr(node, 'lineno', None)
    
    def extract_from_position(self, position: int) -> int:
        """Extract line number from file position.
        
        Args:
            position: Character position in file
            
        Returns:
            Line number (1-based)
        """
        # Count newlines before position
        content_before = self._file.content[:position] if hasattr(self._file, 'content') else ''
        return content_before.count('\n') + 1




