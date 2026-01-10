"""
Markdown adapter for Actions collection.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseActionsAdapter

class MarkdownActions(BaseActionsAdapter, MarkdownAdapter):
    """Serializes Actions collection to Markdown - delegates to MarkdownAction for each action."""
    
    def __init__(self, actions):
        """
        Initialize Markdown adapter for Actions.
        
        Args:
            actions: Actions collection to serialize
        """
        BaseActionsAdapter.__init__(self, actions, 'markdown')
        self.actions = actions
    
    def serialize(self) -> str:
        """Convert Actions to Markdown string - uses base class serialization."""
        return super().serialize()
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
