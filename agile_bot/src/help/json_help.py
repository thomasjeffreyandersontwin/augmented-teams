"""
JSON adapter for Help domain object.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.help.help import Help


class JSONHelp(JSONAdapter):
    """Serializes Help domain object to JSON."""
    
    def __init__(self, help_obj: Help):
        """
        Initialize JSON adapter for Help.
        
        Args:
            help_obj: Help domain object to serialize
        """
        self.help_obj = help_obj
    
    def to_dict(self) -> dict:
        """Convert Help to dict - mirrors TTYHelp structure."""
        return {
            'core_commands': {
                'navigation_pattern': self.help_obj.commands.core.navigation_pattern,
                'short_navigation_pattern': self.help_obj.commands.core.short_navigation_pattern,
                'description_full': self.help_obj.commands.core.description_full,
                'description_short': self.help_obj.commands.core.description_short,
            },
            'components': {
                'behaviors': self.help_obj.components.behaviors,
                'actions': [{'name': name, 'description': desc} for name, desc in self.help_obj.components.actions],
                'operations': [{'operation': op, 'params': params} for op, params in self.help_obj.components.operations.operations],
            },
            'examples': [{'command': cmd, 'description': desc} for cmd, desc in self.help_obj.commands.examples.examples],
            'other_commands': [{'command': cmd, 'description': desc} for cmd, desc in self.help_obj.commands.other.commands],
            'scope': {
                'important_rules': self.help_obj.scope.important_rules,
                'usage_patterns': [{'pattern': pattern, 'description': desc} for pattern, desc in self.help_obj.scope.usage_patterns],
                'correct_examples': [{'example': example, 'description': desc} for example, desc in self.help_obj.scope.correct_examples],
                'incorrect_examples': [{'example': example, 'reason': reason} for example, reason in self.help_obj.scope.incorrect_examples],
            },
            'available_commands': self.help_obj.available_commands,
        }
    
    def serialize(self) -> str:
        """Convert Help to JSON string."""
        return json.dumps(self.to_dict(), indent=2)
    
    def deserialize(self, data: str) -> Help:
        """Reconstruct Help from JSON string."""
        help_data = json.loads(data)
        # Note: Help constructor doesn't support deserialization from dict
        # This method is kept for interface compatibility
        return Help()
