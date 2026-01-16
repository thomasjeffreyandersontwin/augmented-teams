
from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseActionsAdapter

class TTYActions(BaseActionsAdapter, TTYAdapter):
    
    def __init__(self, actions):
        BaseActionsAdapter.__init__(self, actions, 'tty')
        self.actions = actions
    
    @property
    def current(self):
        if self.actions.current:
            from agile_bot.src.actions.tty_action import TTYAction
            action_adapter = TTYAction(self.actions.current, is_current=True)
            return action_adapter.serialize()
        return ""
    
    @property
    def names(self):
        current_action_name = self.actions.current.action_name if self.actions.current else None
        names_list = []
        
        for name in self.actions.names:
            if name == current_action_name:
                names_list.append(self.add_bold(name))
            else:
                names_list.append(name)
        
        if hasattr(self.actions, '_non_workflow_actions'):
            for action in self.actions._non_workflow_actions:
                name = action.action_name
                names_list.append(name)
        
        return " | ".join(names_list)
    
    @property
    def all_actions(self):
        return self.serialize()
    
    def serialize(self) -> str:
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
