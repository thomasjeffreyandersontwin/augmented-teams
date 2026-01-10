"""
TTY adapter for Guardrails domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter

class TTYGuardrails(TTYAdapter):
    """Serializes Guardrails to TTY - delegates to RequiredContext and Strategy adapters."""
    
    def __init__(self, guardrails):
        self.guardrails = guardrails
    
    def serialize(self) -> str:
        """Convert Guardrails to TTY string - delegates to sub-adapters."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        
        lines = []
        
        # Delegate to RequiredContext adapter
        if self.guardrails.required_context:
            required_context_adapter = AdapterFactory.create(self.guardrails.required_context, 'tty')
            lines.append(required_context_adapter.serialize())
        
        # Note: Strategy is handled separately in Instructions for action-specific display
        
        return '\n'.join(lines)
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Guardrails)."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower() if parts else ""
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
