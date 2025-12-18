from pathlib import Path
import json
import sys
from typing import Dict, Any, Optional


def read_json_file(file_path: Path) -> Dict[str, Any]:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return json.loads(file_path.read_text(encoding='utf-8'))


class TerminalFormatter:
    """
    ANSI color codes and formatting utilities for terminal output.
    Can be used by CLI, actions, and any code that needs formatted terminal output.
    """
    # Reset
    RESET = '\033[0m'
    
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Text styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    
    def __init__(self, enabled: Optional[bool] = None):
        """
        Initialize formatter with color support detection.
        
        Args:
            enabled: Force enable/disable colors. If None, auto-detect.
        """
        if enabled is None:
            enabled = self._supports_color()
        
        if not enabled:
            self._disable_colors()
    
    @staticmethod
    def _supports_color() -> bool:
        """Check if terminal supports ANSI color codes."""
        if sys.platform == 'win32':
            # Windows 10+ supports ANSI colors
            # Check if we're in a modern terminal (not cmd.exe on old Windows)
            return True  # Assume modern Windows terminal
        # Unix-like systems typically support colors if stdout is a TTY
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    
    def _disable_colors(self):
        """Disable all colors (for non-terminal output or when colors not supported)."""
        for attr in dir(self):
            if not attr.startswith('_') and attr.isupper():
                setattr(self, attr, '')
    
    def format(self, text: str, *styles: str) -> str:
        """
        Apply formatting styles to text.
        
        Args:
            text: Text to format
            *styles: Style names (e.g., 'BOLD', 'GREEN', 'CYAN')
            
        Returns:
            Formatted text with reset code at end
        """
        style_codes = ''.join(getattr(self, style, '') for style in styles)
        return f"{style_codes}{text}{self.RESET}"
    
    def header(self, text: str) -> str:
        """Format as a header (bold, cyan)."""
        return self.format(text, 'BOLD', 'CYAN')
    
    def command(self, text: str) -> str:
        """Format as a command (bold, green)."""
        return self.format(text, 'BOLD', 'GREEN')
    
    def label(self, text: str) -> str:
        """Format as a label (dim)."""
        return self.format(text, 'DIM')
    
    def success(self, text: str) -> str:
        """Format as success (green)."""
        return self.format(text, 'GREEN')
    
    def error(self, text: str) -> str:
        """Format as error (red)."""
        return self.format(text, 'RED')
    
    def warning(self, text: str) -> str:
        """Format as warning (yellow)."""
        return self.format(text, 'YELLOW')
    
    def info(self, text: str) -> str:
        """Format as info (blue)."""
        return self.format(text, 'BLUE')
    
    def separator(self, char: str = '=', length: int = 70) -> str:
        """Format as separator line."""
        return self.format(char * length, 'BRIGHT_BLACK')


# Default instance for easy import
_default_formatter = None

def get_formatter(enabled: Optional[bool] = None) -> TerminalFormatter:
    """
    Get the default terminal formatter instance.
    
    Args:
        enabled: Force enable/disable colors. If None, auto-detect.
        
    Returns:
        TerminalFormatter instance
    """
    global _default_formatter
    if _default_formatter is None or enabled is not None:
        _default_formatter = TerminalFormatter(enabled=enabled)
    return _default_formatter






























