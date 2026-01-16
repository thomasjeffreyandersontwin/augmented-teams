
from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseActionsAdapter

class MarkdownActions(BaseActionsAdapter, MarkdownAdapter):
    
    def __init__(self, actions):
        BaseActionsAdapter.__init__(self, actions, 'markdown')
        self.actions = actions
    
    def serialize(self) -> str:
        return super().serialize()
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
