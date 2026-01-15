"""
JSON adapter for Bot domain object.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseBotAdapter
from agile_bot.src.bot.bot import Bot


class JSONBot(BaseBotAdapter, JSONAdapter):
    """Serializes Bot domain object to JSON - exposes all Bot properties."""
    
    def __init__(self, bot: Bot):
        """
        Initialize JSON adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'json')
        self.bot = bot
    
    # Expose ALL domain properties
    @property
    def name(self):
        return self.bot.name
    
    @property
    def bot_name(self):
        return self.bot.bot_name
    
    @property
    def bot_directory(self):
        return self.bot.bot_directory
    
    @property
    def workspace_directory(self):
        return self.bot.workspace_directory
    
    @property
    def bot_paths(self):
        return self.bot.bot_paths
    
    @property
    def behaviors(self):
        return self.bot.behaviors
    
    def format_header(self) -> str:
        """JSON doesn't need header."""
        return ""
    
    def format_bot_info(self) -> str:
        """JSON doesn't use this - use to_dict instead."""
        return ""
    
    def format_footer(self) -> str:
        """JSON doesn't need footer."""
        return ""
    
    def serialize(self) -> str:
        """Convert Bot to JSON string - overrides base to use to_dict."""
        return json.dumps(self.to_dict(), indent=2)
    
    def to_dict(self) -> dict:
        """Convert Bot to dict - ensures current_behavior is always included."""
        result = {
            'name': self.bot.name,
            'bot_directory': str(self.bot.bot_directory),
            'workspace_directory': str(self.bot.workspace_directory),
            'behavior_names': self.bot.behaviors.names if self.bot.behaviors else [],
            'current_behavior': self.bot.behaviors.current.name if self.bot.behaviors and self.bot.behaviors.current else None
        }
        if self._behaviors_adapter:
            result['behaviors'] = self._behaviors_adapter.to_dict() if hasattr(self._behaviors_adapter, 'to_dict') else {}
        
        # Include scope if available
        if hasattr(self.bot, '_scope') and self.bot._scope:
            # Serialize scope using its adapter
            from agile_bot.src.cli.adapter_factory import AdapterFactory
            scope_adapter = AdapterFactory.create(self.bot._scope, 'json')
            result['scope'] = scope_adapter.to_dict()
        
        return result
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
