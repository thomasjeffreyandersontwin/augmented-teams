"""BlockExtractor helper for extracting code blocks from files."""

from typing import List
import ast
import logging
from .file import File
from .block import Block

logger = logging.getLogger(__name__)


class BlockExtractor:
    """Extracts code blocks from files."""
    
    def extract_blocks_from_file(self, file: File) -> List[Block]:
        """Extract blocks from file.
        
        Args:
            file: File to extract blocks from
            
        Returns:
            List of Block objects
        """
        blocks = []
        
        # Parse file if not already parsed
        ast_tree = file.parse_python_file()
        if not ast_tree:
            return blocks
        
        # Extract function and class definitions as blocks
        for node in ast.walk(ast_tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                block = self._create_block_from_node(file, node)
                if block:
                    blocks.append(block)
        
        return blocks
    
    def identifies_code_blocks(self, file: File) -> List[Block]:
        """Identify code blocks in file (alias for extract_blocks_from_file)."""
        return self.extract_blocks_from_file(file)
    
    def _create_block_from_node(self, file: File, node: ast.AST) -> Block:
        """Create Block from AST node.
        
        Args:
            file: File containing the node
            node: AST node (FunctionDef, ClassDef, etc.)
            
        Returns:
            Block object
        """
        start_line = getattr(node, 'lineno', 1)
        end_line = self._get_end_line(node, file.content if file.content else '')
        
        # Get source code for this node
        content = self._get_node_source(node, file.content if file.content else '')
        
        return Block(file, content, start_line, end_line)
    
    def _get_end_line(self, node: ast.AST, content: str) -> int:
        """Get end line number for node."""
        # Try to get end_lineno if available (Python 3.8+)
        if hasattr(node, 'end_lineno') and node.end_lineno:
            return node.end_lineno
        
        # Fallback: count lines in content
        start_line = getattr(node, 'lineno', 1)
        if not content:
            return start_line
        
        lines = content.splitlines()
        if start_line <= len(lines):
            # Estimate end line based on node structure
            # This is a simplification - in reality we'd need to parse more carefully
            return start_line + 10  # Default estimate
        
        return start_line
    
    def _get_node_source(self, node: ast.AST, content: str) -> str:
        """Get source code for node."""
        if not content:
            return ''
        
        try:
            # Try to use ast.unparse if available (Python 3.9+)
            if hasattr(ast, 'unparse'):
                return ast.unparse(node)
        except Exception as e:
            logger.debug(f'Could not unparse AST node at line {getattr(node, "lineno", "unknown")}: {type(e).__name__}: {e}')
        
        # Fallback: extract from content using line numbers
        start_line = getattr(node, 'lineno', 1)
        end_line = self._get_end_line(node, content)
        
        lines = content.splitlines(keepends=True)
        if start_line <= len(lines):
            selected_lines = lines[start_line - 1:end_line]
            return ''.join(selected_lines)
        
        return ''


