"""Scanner for validating import statements are at the top of files."""

from typing import List, Dict, Any, Optional
from pathlib import Path
import ast
import re
from .code_scanner import CodeScanner
from .violation import Violation


class ImportPlacementScanner(CodeScanner):
    """Validates that all import statements are at the top of the file."""
    
    def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """Scan a file for import placement violations.
        
        Args:
            file_path: Path to code file to scan
            rule_obj: Rule object reference
            
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        if not file_path.exists():
            return violations
        
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            
            # Find the end of the import section (after docstrings/comments)
            import_section_end = self._find_import_section_end(lines)
            
            # Find all import statements and check if they're in the import section
            violations.extend(self._check_import_placement(lines, import_section_end, file_path, rule_obj))
        
        except (UnicodeDecodeError, SyntaxError, Exception):
            # Skip binary files, files with encoding issues, or syntax errors
            pass
        
        return violations
    
    def _find_import_section_end(self, lines: List[str]) -> int:
        """Find the line number where the import section ends.
        
        Import section includes:
        - Module docstring (triple-quoted string at start)
        - Comments
        - Blank lines
        - Import statements
        - TYPE_CHECKING blocks (if TYPE_CHECKING: ...)
        
        Returns:
            Line number (1-indexed) where import section ends, or len(lines) if all imports
        """
        import_section_end = 0
        
        # Skip leading blank lines
        while import_section_end < len(lines) and not lines[import_section_end].strip():
            import_section_end += 1
        
        # Skip module docstring (triple-quoted string)
        if import_section_end < len(lines):
            line = lines[import_section_end].strip()
            if line.startswith('"""') or line.startswith("'''"):
                # Find end of docstring
                quote_char = line[:3]
                import_section_end += 1
                while import_section_end < len(lines):
                    if quote_char in lines[import_section_end]:
                        import_section_end += 1
                        break
                    import_section_end += 1
        
        # Skip blank lines, comments, imports, TYPE_CHECKING blocks, and try/except ImportError blocks after docstring
        while import_section_end < len(lines):
            line = lines[import_section_end].strip()
            if not line or line.startswith('#'):
                import_section_end += 1
            elif self._is_import_statement(line):
                import_section_end += 1
            elif self._is_type_checking_block_start(line):
                # Skip through the entire TYPE_CHECKING block
                import_section_end = self._skip_type_checking_block(lines, import_section_end)
            elif self._is_try_import_error_block_start(line):
                # Skip through the entire try/except ImportError block
                import_section_end = self._skip_try_import_error_block(lines, import_section_end)
            else:
                # Found non-import, non-comment, non-blank line - import section ends here
                break
        
        return import_section_end
    
    def _is_type_checking_block_start(self, line: str) -> bool:
        """Check if a line starts a TYPE_CHECKING block.
        
        Args:
            line: Line of code to check
            
        Returns:
            True if line is 'if TYPE_CHECKING:' or similar
        """
        stripped = line.strip()
        # Match 'if TYPE_CHECKING:' pattern (may have comments after colon)
        return stripped.startswith('if TYPE_CHECKING:')
    
    def _skip_type_checking_block(self, lines: List[str], start_line: int) -> int:
        """Skip through a TYPE_CHECKING block and return the line after it ends.
        
        Args:
            lines: All lines in the file
            start_line: Line number (0-indexed) where 'if TYPE_CHECKING:' starts
            
        Returns:
            Line number (0-indexed) after the TYPE_CHECKING block ends
        """
        if start_line >= len(lines):
            return start_line
        
        # Get the indentation level of the 'if TYPE_CHECKING:' line
        type_checking_line = lines[start_line]
        base_indent = len(type_checking_line) - len(type_checking_line.lstrip())
        
        # Start after the 'if TYPE_CHECKING:' line
        current_line = start_line + 1
        
        # Skip through the block (all lines indented more than the 'if' statement)
        while current_line < len(lines):
            line = lines[current_line]
            stripped = line.strip()
            
            # Empty lines are allowed
            if not stripped:
                current_line += 1
                continue
            
            # Comments are allowed
            if stripped.startswith('#'):
                current_line += 1
                continue
            
            # Check indentation - if line is at same or less indentation, block has ended
            line_indent = len(line) - len(line.lstrip())
            if line_indent <= base_indent:
                # Block has ended
                break
            
            # This line is part of the TYPE_CHECKING block
            current_line += 1
        
        return current_line
    
    def _is_try_import_error_block_start(self, line: str) -> bool:
        """Check if a line starts a try/except ImportError block.
        
        Args:
            line: Line of code to check
            
        Returns:
            True if line is 'try:' and likely followed by import in except ImportError
        """
        stripped = line.strip()
        return stripped == 'try:' or stripped.startswith('try:')
    
    def _skip_try_import_error_block(self, lines: List[str], start_line: int) -> int:
        """Skip through a try/except ImportError block and return the line after it ends.
        
        Args:
            lines: All lines in the file
            start_line: Line number (0-indexed) where 'try:' starts
            
        Returns:
            Line number (0-indexed) after the try/except block ends
        """
        if start_line >= len(lines):
            return start_line
        
        # Get the indentation level of the 'try:' line
        try_line = lines[start_line]
        base_indent = len(try_line) - len(try_line.lstrip())
        
        # Start after the 'try:' line
        current_line = start_line + 1
        
        # Skip through the try block (all lines indented more than the 'try' statement)
        while current_line < len(lines):
            line = lines[current_line]
            stripped = line.strip()
            
            # Empty lines are allowed
            if not stripped:
                current_line += 1
                continue
            
            # Comments are allowed
            if stripped.startswith('#'):
                current_line += 1
                continue
            
            # Check indentation - if line is at same indentation, might be except
            line_indent = len(line) - len(line.lstrip())
            if line_indent == base_indent:
                # Check if this is an except ImportError block
                if stripped.startswith('except ImportError:') or stripped.startswith('except ImportError'):
                    # Skip through the except block too
                    current_line += 1
                    while current_line < len(lines):
                        except_line = lines[current_line]
                        except_stripped = except_line.strip()
                        except_indent = len(except_line) - len(except_line.lstrip())
                        
                        # Empty lines and comments in except block are allowed
                        if not except_stripped or except_stripped.startswith('#'):
                            current_line += 1
                            continue
                        
                        # If we're back to base indentation or less, except block is done
                        if except_indent <= base_indent:
                            break
                        
                        current_line += 1
                    # Block has ended
                    break
                else:
                    # Not an except ImportError, block has ended
                    break
            
            # This line is part of the try block
            current_line += 1
        
        return current_line
    
    def _is_import_statement(self, line: str) -> bool:
        """Check if a line is an import statement.
        
        Args:
            line: Line of code to check
            
        Returns:
            True if line is an import statement
        """
        stripped = line.strip()
        
        # Must start with 'import ' or 'from ' (not just contain these words)
        if not (stripped.startswith('import ') or stripped.startswith('from ')):
            return False
        
        # For 'from X import Y' statements, must have ' import ' in the line
        if stripped.startswith('from '):
            return ' import ' in stripped
        
        # For 'import X' statements, must be at the start
        return stripped.startswith('import ')
    
    def _check_import_placement(
        self, 
        lines: List[str], 
        import_section_end: int,
        file_path: Path, 
        rule_obj: Any
    ) -> List[Dict[str, Any]]:
        """Check for imports that appear after the import section.
        
        Args:
            lines: All lines in the file
            import_section_end: Line number (0-indexed) where import section should end
            file_path: Path to file being scanned
            rule_obj: Rule object reference
            
        Returns:
            List of violation dictionaries
        """
        violations = []
        
        # Parse the file with AST to accurately detect imports and their context
        try:
            content = '\n'.join(lines)
            tree = ast.parse(content, filename=str(file_path))
            import_nodes = self._find_import_nodes(tree)
            import_line_numbers = {node.lineno for node in import_nodes}
            function_def_lines = self._find_function_def_lines(tree)
        except (SyntaxError, Exception):
            # If AST parsing fails, fall back to simple line-by-line checking
            import_line_numbers = set()
            function_def_lines = set()
        
        # Check each line after the import section for import statements
        line_num = import_section_end
        while line_num < len(lines):
            line = lines[line_num]
            line_number_1_indexed = line_num + 1
            
            # Skip blank lines and comments
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                line_num += 1
                continue
            
            # Skip TYPE_CHECKING blocks (they're allowed to contain imports)
            if self._is_type_checking_block_start(stripped):
                line_num = self._skip_type_checking_block(lines, line_num)
                continue
            
            # Skip try/except ImportError blocks (they're allowed to contain imports)
            if self._is_try_import_error_block_start(stripped):
                line_num = self._skip_try_import_error_block(lines, line_num)
                continue
            
            # Check if this line is an import statement
            is_import = False
            if import_line_numbers and line_number_1_indexed in import_line_numbers:
                # Use AST-detected imports (more accurate)
                is_import = True
            elif self._is_import_statement(line):
                # Fall back to pattern matching
                is_import = True
            
            if is_import:
                # Check if import is inside a function (allowed pattern for circular imports)
                if function_def_lines and self._is_inside_function(line_number_1_indexed, function_def_lines, lines):
                    # Import inside function is allowed - skip it
                    line_num += 1
                    continue
                
                # Found import after import section - violation!
                violation = Violation(
                    rule=rule_obj,
                    violation_message=f'Import statement found at line {line_number_1_indexed} after non-import code. Move all imports to the top of the file.',
                    location=f'{file_path}:{line_number_1_indexed}',
                    line_number=line_number_1_indexed,
                    severity='error'
                ).to_dict()
                violations.append(violation)
            
            line_num += 1
        
        return violations
    
    def _find_import_nodes(self, tree: ast.AST) -> List[ast.stmt]:
        """Find all import and import-from nodes in the AST."""
        import_nodes = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                import_nodes.append(node)
        return import_nodes
    
    def _find_function_def_lines(self, tree: ast.AST) -> Dict[int, int]:
        """Find function definition line ranges.
        
        Returns:
            Dictionary mapping start line to end line for each function
        """
        function_ranges = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # Get the end line of the function (approximate by finding the next def/class at same level)
                start_line = node.lineno
                end_line = self._find_function_end_line(node, tree)
                function_ranges[start_line] = end_line
        return function_ranges
    
    def _find_function_end_line(self, func_node: ast.FunctionDef, tree: ast.AST) -> int:
        """Find the approximate end line of a function definition."""
        # Use end_lineno if available (Python 3.8+)
        if hasattr(func_node, 'end_lineno') and func_node.end_lineno:
            return func_node.end_lineno
        
        # Fallback: find the last line of the function body
        if func_node.body:
            last_stmt = func_node.body[-1]
            if hasattr(last_stmt, 'end_lineno') and last_stmt.end_lineno:
                return last_stmt.end_lineno
            elif hasattr(last_stmt, 'lineno'):
                return last_stmt.lineno
        
        # Final fallback: estimate based on function start
        return func_node.lineno + 50  # Conservative estimate
    
    def _is_inside_function(self, line_number: int, function_ranges: Dict[int, int], lines: List[str]) -> bool:
        """Check if a line number is inside a function definition."""
        for func_start, func_end in function_ranges.items():
            if func_start <= line_number <= func_end:
                return True
        return False













