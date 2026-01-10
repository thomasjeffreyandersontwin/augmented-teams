"""
TTY adapter for Actions collection.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseActionsAdapter

class TTYActions(BaseActionsAdapter, TTYAdapter):
    """Serializes Actions collection to TTY - delegates to TTYAction for each action."""
    
    def __init__(self, actions):
        """
        Initialize TTY adapter for Actions.
        
        Args:
            actions: Actions collection to serialize
        """
        BaseActionsAdapter.__init__(self, actions, 'tty')
        self.actions = actions
    
    # Expose ALL domain properties as FORMATTED display strings
    @property
    def current(self):
        """Returns formatted current action display."""
        if self.actions.current:
            from agile_bot.src.actions.tty_action import TTYAction
            action_adapter = TTYAction(self.actions.current, is_current=True)
            return action_adapter.serialize()
        return ""
    
    @property
    def names(self):
        """Return pipe-separated list of action names with current action bolded.
        
        Includes workflow actions first, then non-workflow actions (like 'rules') at the end.
        """
        current_action_name = self.actions.current.action_name if self.actions.current else None
        names_list = []
        
        # Add workflow actions first
        for name in self.actions.names:
            if name == current_action_name:
                names_list.append(self.add_bold(name))
            else:
                names_list.append(name)
        
        # Add non-workflow actions at the end (like 'rules')
        if hasattr(self.actions, '_non_workflow_actions'):
            for action in self.actions._non_workflow_actions:
                name = action.action_name
                # Non-workflow actions can't be current (they don't participate in workflow)
                names_list.append(name)
        
        return " | ".join(names_list)
    
    @property
    def all_actions(self):
        """Returns formatted list of all actions."""
        return self.serialize()
    
    def serialize(self) -> str:
        """Convert Actions to TTY string - uses base class serialization."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
