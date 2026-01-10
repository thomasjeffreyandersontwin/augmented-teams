"""
JSON adapter for Behavior and Behaviors domain objects.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseBehaviorsAdapter, BaseBehaviorAdapter
from agile_bot.src.behaviors.behavior import Behavior
from agile_bot.src.behaviors.behaviors import Behaviors

class JSONBehaviors(BaseBehaviorsAdapter, JSONAdapter):
    """Serializes Behaviors collection to JSON."""
    
    def __init__(self, behaviors: Behaviors):
        """
        Initialize JSON adapter for Behaviors.
        
        Args:
            behaviors: Behaviors collection to serialize
        """
        BaseBehaviorsAdapter.__init__(self, behaviors, 'json')
        self.behaviors = behaviors
    
    def serialize(self) -> str:
        """Convert Behaviors to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
    
    def to_dict(self) -> dict:
        """Convert Behaviors to dict."""
        behaviors_list = []
        for behavior_adapter in self._behavior_adapters:
            if hasattr(behavior_adapter, 'to_dict'):
                behaviors_list.append(behavior_adapter.to_dict())
        return {
            'current': self.behaviors.current.name if self.behaviors.current else None,
            'names': self.behaviors.names,
            'all_behaviors': behaviors_list
        }
    

class JSONBehavior(BaseBehaviorAdapter, JSONAdapter):
    """Serializes Behavior domain object to JSON."""
    
    def __init__(self, behavior: Behavior, is_current: bool = False):
        """
        Initialize JSON adapter for Behavior.
        
        Args:
            behavior: Behavior domain object to serialize
            is_current: Whether this is the current behavior
        """
        self.behavior = behavior
        self.is_current = is_current
        BaseBehaviorAdapter.__init__(self, behavior, 'json', is_current)
    
    def format_behavior_name(self) -> str:
        """JSON doesn't use this - use to_dict instead."""
        return ""
    
    def serialize(self) -> str:
        """Convert Behavior to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
    
    def to_dict(self) -> dict:
        """Convert Behavior to dict."""
        result = {
            'name': self.behavior.name,
            'bot_name': self.behavior.bot_name,
            'description': self.behavior.description,
            'goal': self.behavior.goal,
            'action_names': self.behavior.action_names,
            'is_completed': self.behavior.is_completed,
            'order': self.behavior.order,
            'is_current': self.is_current
        }
        if self.is_current and self._actions_adapter and hasattr(self._actions_adapter, 'to_dict'):
            result['actions'] = self._actions_adapter.to_dict()
        return result
    
    def deserialize(self, data: str) -> Behavior:
        """Reconstruct Behavior from JSON string.
        
        Note: Behavior objects typically require bot_paths and are loaded from config.
        This method is provided for completeness but may not be fully functional.
        """
        behavior_data = json.loads(data)
        # Note: Cannot fully reconstruct a Behavior without bot_paths and config
        # This is a limitation of the domain model
        raise NotImplementedError("Behavior deserialization requires bot_paths and config files")
