"""
TTY adapter for StrategyAction.
"""

from agile_bot.src.actions.tty_action import TTYAction
from agile_bot.src.actions.strategy.strategy_action import StrategyAction

class TTYStrategyAction(TTYAction):
    """Serializes StrategyAction to TTY - exposes all StrategyAction properties."""
    
    def __init__(self, action: StrategyAction, is_current: bool = False, is_completed: bool = False):
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
    def strategy(self):
        """Strategy-specific property."""
        return self.action.strategy
    
    @property
    def strategy_criteria(self):
        """Strategy-specific property."""
        return self.action.strategy_criteria
    
    @property
    def typical_assumptions(self):
        """Strategy-specific property."""
        return self.action.typical_assumptions
    
    def serialize(self) -> str:
        """Convert StrategyAction to TTY string - uses base class for status display."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
