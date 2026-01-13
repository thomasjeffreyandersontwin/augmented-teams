"""
Base adapter classes for channel-specific serialization.

All domain adapters inherit from these base classes.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class ChannelAdapter(ABC):
    """Base for all channel adapters."""
    
    @abstractmethod
    def serialize(self) -> str:
        """Serialize domain object to string format."""
        pass

class TextAdapter(ChannelAdapter):
    """Base for text-based adapters (TTY, Markdown)."""
    
    @abstractmethod
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and params."""
        pass


class TTYAdapter(TextAdapter):
    """Base for terminal output adapters."""
    
    def add_color(self, text: str, color: str) -> str:
        """Add ANSI color codes."""
        colors = {
            'green': '\033[92m',
            'yellow': '\033[93m',
            'red': '\033[91m',
            'blue': '\033[94m',
            'reset': '\033[0m'
        }
        return f"{colors.get(color, '')}{text}{colors['reset']}"
    
    def add_bold(self, text: str) -> str:
        """Add ANSI bold formatting."""
        return f"\033[1m{text}\033[0m"
    
    def format_indentation(self, level: int) -> str:
        """Format indentation for hierarchy."""
        return "  " * level
    
    def section_separator(self) -> str:
        """Return heavy separator for major sections."""
        return "━" * 100
    
    def subsection_separator(self) -> str:
        """Return light separator for subsections."""
        return "─" * 60
    
    @abstractmethod
    def serialize(self) -> str:
        """Convert domain object to TTY string."""
        pass
    
    @abstractmethod
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args


class JSONAdapter(ChannelAdapter):
    """Base for JSON adapters."""
    
    @abstractmethod
    def to_dict(self) -> Dict:
        """Convert domain object to dict."""
        pass
    
    def serialize(self) -> str:
        """Convert to JSON string."""
        import json
        return json.dumps(self.to_dict(), indent=2)


class MarkdownAdapter(TextAdapter):
    """Base for Markdown adapters."""
    
    def format_header(self, level: int, text: str) -> str:
        """Format markdown header."""
        return f"{'#' * level} {text}\n"
    
    def format_list_item(self, text: str, indent: int = 0) -> str:
        """Format markdown list item."""
        return f"{'  ' * indent}- {text}\n"
    
    def format_code_block(self, content: str, language: str = "") -> str:
        """Format markdown code block."""
        return f"```{language}\n{content}\n```\n"
    
    @abstractmethod
    def serialize(self) -> str:
        """Convert domain object to Markdown string."""
        pass
    
    @abstractmethod
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args


class JSONProgressAdapter(JSONAdapter):
    """Base for JSON adapters that track progress."""
    
    def include_progress_fields(self, is_completed: bool, is_current: bool) -> Dict:
        """Standard progress fields."""
        return {
            'is_completed': is_completed,
            'is_current': is_current,
            'completion_marker': '[X]' if is_completed else '[ ]'
        }


class TTYProgressAdapter(TTYAdapter):
    """Base for TTY adapters that track progress."""
    
    def render_marker(self, is_completed: bool, is_current: bool) -> str:
        """Render progress marker."""
        if is_completed:
            return self.add_color('[X]', 'green')
        elif is_current:
            return self.add_color('[>]', 'yellow')
        else:
            return '[ ]'


class MarkdownProgressAdapter(MarkdownAdapter):
    """Base for Markdown adapters that track progress."""
    
    def render_progress_marker(self, is_completed: bool, is_current: bool) -> str:
        """Render markdown progress marker."""
        if is_completed:
            return '[X]'
        elif is_current:
            return '[>]'
        else:
            return '[ ]'


class GenericAdapter(ChannelAdapter):
    """
    Generic adapter for dict/list objects that don't have custom domain objects yet.
    Used as a fallback during refactoring.
    """
    
    def __init__(self, data: Any, channel: str):
        """
        Initialize generic adapter.
        
        Args:
            data: Dict or list to adapt
            channel: Output channel ('json', 'tty', 'markdown')
        """
        self.data = data
        self.channel = channel
    
    def serialize(self) -> str:
        """Serialize data based on channel."""
        if self.channel == 'json':
            import json
            return json.dumps(self.data, indent=2)
        elif self.channel == 'tty':
            return self._format_tty()
        elif self.channel == 'markdown':
            return self._format_markdown()
        else:
            import json
            return json.dumps(self.data, indent=2)
    
    def deserialize(self, data: str) -> Any:
        """Deserialize string to data."""
        import json
        return json.loads(data)
    
    def _format_tty(self) -> str:
        """Format data for TTY output with ANSI formatting."""
        # For execution results (dicts with status/behavior/action), format nicely
        if isinstance(self.data, dict):
            # Check if it's an execution result
            if 'status' in self.data and 'behavior' in self.data and 'action' in self.data:
                lines = []
                lines.append(f"\x1b[1mStatus:\x1b[0m {self.data['status']}")
                lines.append(f"\x1b[1mBehavior:\x1b[0m {self.data['behavior']}")
                lines.append(f"\x1b[1mAction:\x1b[0m {self.data['action']}")
                if 'message' in self.data:
                    lines.append(f"\x1b[1mMessage:\x1b[0m {self.data['message']}")
                if 'result' in self.data:
                    lines.append(f"\x1b[1mResult:\x1b[0m {self.data['result']}")
                return '\n'.join(lines)
            else:
                # Generic dict formatting
                lines = []
                for key, value in self.data.items():
                    lines.append(f"\x1b[1m{key}:\x1b[0m {value}")
                return '\n'.join(lines)
        # For lists/other types, use JSON as fallback
        import json
        return json.dumps(self.data, indent=2)
    
    def _format_markdown(self) -> str:
        """Format data for Markdown output."""
        import json
        return f"```json\n{json.dumps(self.data, indent=2)}\n```"
