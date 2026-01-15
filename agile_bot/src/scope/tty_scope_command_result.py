"""
TTY adapter for ScopeCommandResult domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.scope.scope_command_result import ScopeCommandResult


class TTYScopeCommandResult(TTYAdapter):
    """Serializes ScopeCommandResult to TTY format."""
    
    def __init__(self, scope_result: ScopeCommandResult):
        self.scope_result = scope_result
    
    def serialize(self) -> str:
        """Convert ScopeCommandResult to TTY string."""
        from agile_bot.src.scope.tty_scope import TTYScope
        
        lines = []
        
        # Display status and message
        status_color = 'green' if self.scope_result.status == 'success' else 'red'
        lines.append(self.add_color(f"Status: {self.scope_result.status}", status_color))
        
        if self.scope_result.message:
            lines.append(self.scope_result.message)
        
        lines.append("")
        
        # Serialize the scope using TTYScope adapter
        scope_adapter = TTYScope(self.scope_result.scope)
        scope_output = scope_adapter.serialize()
        lines.append(scope_output)
        
        return '\n'.join(lines)
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and params."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
