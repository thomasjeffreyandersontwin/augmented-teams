"""
TTY adapter for ValidateRulesAction.
"""

from agile_bot.src.actions.tty_action import TTYAction
from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
from agile_bot.src.instructions.instructions import Instructions

class TTYValidateAction(TTYAction):
    """Serializes ValidateRulesAction to TTY - exposes all ValidateRulesAction properties."""
    
    def __init__(self, action: ValidateRulesAction, is_current: bool = False, is_completed: bool = False):
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
    def rules(self):
        """Validate-specific property."""
        return self.action.rules
    
    def serialize(self) -> str:
        """Convert ValidateRulesAction to TTY string - uses base class for status display."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
    
    @staticmethod
    def format_instructions_from_dict(instructions_dict: dict, bot_paths=None, scope=None) -> str:
        """Format instructions dict (from execute results) as text.
        
        This handles the case where validate.execute() returns {'instructions': {...}}
        and converts it to formatted text, consistent with how other actions format instructions.
        """
        # Convert dict to Instructions object
        instructions_obj = Instructions(
            base_instructions=instructions_dict.get('base_instructions', []),
            bot_paths=bot_paths,
            scope=scope
        )
        # Copy all other fields from dict to Instructions object
        for key, value in instructions_dict.items():
            if key != 'base_instructions':
                instructions_obj.set(key, value)
        
        # Use TTYInstructions adapter to format it
        from agile_bot.src.instructions.tty_instructions import TTYInstructions
        instructions_adapter = TTYInstructions(instructions_obj)
        return instructions_adapter.serialize()
