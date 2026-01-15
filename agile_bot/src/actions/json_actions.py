"""
JSON adapter for Actions collection.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseActionsAdapter

class JSONActions(BaseActionsAdapter, JSONAdapter):
    """Serializes Actions collection to JSON - delegates to JSONAction for each action."""
    
    def __init__(self, actions):
        """
        Initialize JSON adapter for Actions.
        
        Args:
            actions: Actions collection to serialize
        """
        BaseActionsAdapter.__init__(self, actions, 'json')
        self.actions = actions
    
    def serialize(self) -> str:
        """Convert Actions to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
    
    def to_dict(self) -> dict:
        """Convert Actions to dict."""
        actions_list = []
        for action_adapter in self._action_adapters:
            if hasattr(action_adapter, 'to_dict'):
                action_dict = action_adapter.to_dict()
            elif hasattr(action_adapter, 'action'):
                action_dict = {
                    'action_name': getattr(action_adapter.action, 'action_name', 'unknown')
                }
            else:
                action_dict = {}
            
            # Ensure current/completed flags are always present for the panel
            action_dict['is_current'] = getattr(action_adapter, 'is_current', False)
            action_dict['is_completed'] = getattr(action_adapter, 'is_completed', False)
            
            actions_list.append(action_dict)
        return {
            'current': self.actions.current.action_name if self.actions.current else None,
            'names': self.actions.names,
            'all_actions': actions_list
        }
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
