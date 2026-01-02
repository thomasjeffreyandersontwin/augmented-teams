import sys
from .output_formatter import OutputFormatter
from .terminal_formatter import TerminalFormatter
from .markdown_formatter import MarkdownFormatter
from .json_formatter import JSONFormatter


class FormatterFactory:
    
    @staticmethod
    def create_formatter(tty_detected: bool = None, format_type: str = None) -> OutputFormatter:
        """Create formatter based on environment or explicit format type.
        
        Args:
            tty_detected: Whether terminal is a TTY (None = auto-detect)
            format_type: Explicit format type ('json', 'markdown', 'terminal', None = auto-detect)
        """
        if format_type == 'json':
            return JSONFormatter()
        elif format_type == 'markdown':
            return MarkdownFormatter()
        elif format_type == 'terminal':
            return TerminalFormatter()
        
        # Auto-detect based on TTY
        if tty_detected is None:
            tty_detected = sys.stdout.isatty()
        
        if tty_detected:
            return TerminalFormatter()
        else:
            return MarkdownFormatter()
    
    @staticmethod
    def create_terminal_formatter() -> OutputFormatter:
        return TerminalFormatter()
    
    @staticmethod
    def create_markdown_formatter() -> OutputFormatter:
        return MarkdownFormatter()
    
    @staticmethod
    def create_json_formatter() -> OutputFormatter:
        return JSONFormatter()

