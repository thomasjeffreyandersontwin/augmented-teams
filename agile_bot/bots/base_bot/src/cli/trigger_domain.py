"""
Domain objects for trigger patterns.

These objects wrap trigger pattern collections to provide type safety
and domain semantics instead of raw Dict/List primitives.
"""
from typing import List, Dict, Optional
from dataclasses import dataclass, field


@dataclass
class BotTriggers:
    """Domain object for bot-level trigger patterns."""
    patterns: List[str] = field(default_factory=list)
    
    def __iter__(self):
        return iter(self.patterns)
    
    def __len__(self):
        return len(self.patterns)
    
    def __contains__(self, item):
        return item in self.patterns


@dataclass
class BehaviorTriggers:
    """Domain object for behavior-level trigger patterns.
    
    Maps behavior names to their trigger patterns.
    """
    triggers: Dict[str, List[str]] = field(default_factory=dict)
    
    def get(self, behavior_name: str) -> List[str]:
        """Get trigger patterns for a behavior."""
        return self.triggers.get(behavior_name, [])
    
    def __getitem__(self, behavior_name: str) -> List[str]:
        return self.triggers[behavior_name]
    
    def __contains__(self, behavior_name: str) -> bool:
        return behavior_name in self.triggers
    
    def items(self):
        return self.triggers.items()
    
    def keys(self):
        return self.triggers.keys()
    
    def values(self):
        return self.triggers.values()


@dataclass
class ActionTriggers:
    """Domain object for action-level trigger patterns.
    
    Maps behavior -> action -> trigger patterns.
    """
    triggers: Dict[str, Dict[str, List[str]]] = field(default_factory=dict)
    
    def get(self, behavior_name: str) -> Dict[str, List[str]]:
        """Get action triggers for a behavior."""
        return self.triggers.get(behavior_name, {})
    
    def get_action(self, behavior_name: str, action_name: str) -> List[str]:
        """Get trigger patterns for a specific action."""
        behavior_triggers = self.triggers.get(behavior_name, {})
        return behavior_triggers.get(action_name, [])
    
    def __getitem__(self, behavior_name: str) -> Dict[str, List[str]]:
        return self.triggers[behavior_name]
    
    def __contains__(self, behavior_name: str) -> bool:
        return behavior_name in self.triggers
    
    def items(self):
        return self.triggers.items()
    
    def keys(self):
        return self.triggers.keys()

