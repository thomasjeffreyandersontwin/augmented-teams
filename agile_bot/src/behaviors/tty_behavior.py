"""
TTY adapter for Behavior and Behaviors domain objects.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseBehaviorsAdapter, BaseBehaviorAdapter
from agile_bot.src.behaviors.behavior import Behavior
from agile_bot.src.behaviors.behaviors import Behaviors

class TTYBehaviors(BaseBehaviorsAdapter, TTYAdapter):
    """Serializes Behaviors collection to TTY with hierarchy."""
    
    def __init__(self, behaviors: Behaviors):
        """
        Initialize TTY adapter for Behaviors.
        
        Args:
            behaviors: Behaviors collection to serialize
        """
        BaseBehaviorsAdapter.__init__(self, behaviors, 'tty')
        self.behaviors = behaviors
    
    # Expose domain properties as FORMATTED display strings
    @property
    def current(self):
        """Returns formatted current behavior display."""
        if self.behaviors.current:
            behavior_adapter = TTYBehavior(self.behaviors.current, is_current=True)
            return behavior_adapter.serialize()
        return ""
    
    @property
    def names(self):
        """Returns pipe-separated list of behavior names with current behavior bolded."""
        current_behavior_name = self.behaviors.current.name if self.behaviors.current else None
        names_list = []
        # Iterate through all behaviors directly, not through behaviors.names property
        for behavior in self.behaviors:
            name = behavior.name
            if name == current_behavior_name:
                names_list.append(self.add_bold(name))
            else:
                names_list.append(name)
        return " | ".join(names_list)
    
    @property
    def all_behaviors(self):
        """Returns formatted list of all behaviors."""
        return self.serialize()
    
    def serialize(self) -> str:
        """Convert Behaviors to TTY string - uses base class serialization."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args

class TTYBehavior(BaseBehaviorAdapter, TTYAdapter):
    """Serializes single Behavior to TTY - delegates to TTYActions."""
    
    def __init__(self, behavior: Behavior, is_current: bool = False):
        """
        Initialize TTY adapter for Behavior.
        
        Args:
            behavior: Behavior to serialize
            is_current: Whether this is the current behavior
        """
        self.behavior = behavior
        self.is_current = is_current
        BaseBehaviorAdapter.__init__(self, behavior, 'tty', is_current)
    
    def format_behavior_name(self) -> str:
        """Returns formatted behavior name with icon."""
        if self.is_current:
            icon = "➤ "
            name = self.add_bold(self.behavior.name)
        else:
            icon = "☐ "  # Empty box to align with chevron + space
            name = self.behavior.name
        return f"- {icon}{name}"
    
    def serialize(self) -> str:
        """Convert Behavior to TTY string - uses base class serialization."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
