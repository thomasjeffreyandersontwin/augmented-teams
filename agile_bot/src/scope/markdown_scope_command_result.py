"""
Markdown adapter for ScopeCommandResult domain object.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.scope.scope_command_result import ScopeCommandResult


class MarkdownScopeCommandResult(MarkdownAdapter):
    """Serializes ScopeCommandResult to markdown format."""
    
    def __init__(self, scope_result: ScopeCommandResult):
        self.scope_result = scope_result
    
    def serialize(self) -> str:
        """Convert ScopeCommandResult to markdown string."""
        from agile_bot.src.scope.markdown_scope import MarkdownScope
        
        # Serialize the scope using MarkdownScope adapter
        scope_adapter = MarkdownScope(self.scope_result.scope)
        scope_markdown = scope_adapter.serialize()
        
        # Return the markdown representation
        return scope_markdown
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and params."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args