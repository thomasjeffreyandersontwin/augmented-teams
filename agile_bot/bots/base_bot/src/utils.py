from pathlib import Path
import json
import sys
from typing import Dict, Any, Optional

def read_json_file(file_path: Path) -> Dict[str, Any]:
    if not file_path.exists():
        raise FileNotFoundError(f'File not found: {file_path}')
    return json.loads(file_path.read_text(encoding='utf-8'))

class TerminalFormatter:
    RESET = '\x1b[0m'
    BLACK = '\x1b[30m'
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'
    BLUE = '\x1b[34m'
    MAGENTA = '\x1b[35m'
    CYAN = '\x1b[36m'
    WHITE = '\x1b[37m'
    BRIGHT_BLACK = '\x1b[90m'
    BRIGHT_RED = '\x1b[91m'
    BRIGHT_GREEN = '\x1b[92m'
    BRIGHT_YELLOW = '\x1b[93m'
    BRIGHT_BLUE = '\x1b[94m'
    BRIGHT_MAGENTA = '\x1b[95m'
    BRIGHT_CYAN = '\x1b[96m'
    BRIGHT_WHITE = '\x1b[97m'
    BOLD = '\x1b[1m'
    DIM = '\x1b[2m'
    UNDERLINE = '\x1b[4m'

    def __init__(self, enabled: Optional[bool]=None):
        should_enable = enabled if enabled is not None else self._supports_color()
        if not should_enable:
            self._disable_colors()

    @staticmethod
    def _supports_color() -> bool:
        if sys.platform == 'win32':
            return True
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

    def _disable_colors(self):
        for attr in dir(self):
            if not attr.startswith('_') and attr.isupper():
                setattr(self, attr, '')

    def format(self, text: str, *styles: str) -> str:
        style_codes = ''.join((getattr(self, style, '') for style in styles))
        return f'{style_codes}{text}{self.RESET}'

    def header(self, text: str) -> str:
        return self.format(text, 'BOLD', 'CYAN')

    def command(self, text: str) -> str:
        return self.format(text, 'BOLD', 'GREEN')

    def label(self, text: str) -> str:
        return self.format(text, 'DIM')

    def success(self, text: str) -> str:
        return self.format(text, 'GREEN')

    def error(self, text: str) -> str:
        return self.format(text, 'RED')

    def warning(self, text: str) -> str:
        return self.format(text, 'YELLOW')

    def info(self, text: str) -> str:
        return self.format(text, 'BLUE')

    def separator(self, char: str='=', length: int=70) -> str:
        return self.format(char * length, 'BRIGHT_BLACK')
_default_formatter = None

def get_formatter(enabled: Optional[bool]=None) -> TerminalFormatter:
    global _default_formatter
    if _default_formatter is None or enabled is not None:
        _default_formatter = TerminalFormatter(enabled=enabled)
    return _default_formatter