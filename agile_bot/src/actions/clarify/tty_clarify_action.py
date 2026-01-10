"""
TTY adapter for ClarifyContextAction.
"""

from agile_bot.src.actions.tty_action import TTYAction
from agile_bot.src.actions.clarify.clarify_action import ClarifyContextAction

class TTYClarifyAction(TTYAction):
    """Serializes ClarifyContextAction to TTY - exposes all ClarifyContextAction properties."""
    
    def __init__(self, action: ClarifyContextAction, is_current: bool = False, is_completed: bool = False):
        super().__init__(action, is_current, is_completed)
    
    # Expose ALL domain properties
    @property
    def description(self):
        return self.action.description
    
    @property
    def order(self):
        return self.action.order
    
    @property
    def next_action(self):
        return self.action.next_action
    
    @property
    def workflow(self):
        return self.action.workflow
    
    @property
    def auto_confirm(self):
        return self.action.auto_confirm
    
    @property
    def skip_confirm(self):
        return self.action.skip_confirm
    
    @property
    def behavior(self):
        return self.action.behavior
    
    @property
    def required_context(self):
        """Clarify-specific property."""
        return self.action.required_context
    
    @property
    def key_questions(self):
        """Clarify-specific property."""
        return self.action.key_questions
    
    @property
    def evidence(self):
        """Clarify-specific property."""
        return self.action.evidence
    
    def serialize(self) -> str:
        """Convert ClarifyContextAction to TTY string - uses base class for status display."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
