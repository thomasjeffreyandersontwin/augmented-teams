"""
Markdown adapter for StrategyAction.
"""

from agile_bot.src.actions.markdown_action import MarkdownAction
from agile_bot.src.actions.strategy.strategy_action import StrategyAction

class MarkdownStrategyAction(MarkdownAction):
    """Serializes StrategyAction to Markdown - uses base class for status display."""
    
    def __init__(self, action: StrategyAction, is_current: bool = False, is_completed: bool = False):
        super().__init__(action, is_current, is_completed)
    
    def serialize(self) -> str:
        """Convert StrategyAction to Markdown string - uses base class for status display."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
