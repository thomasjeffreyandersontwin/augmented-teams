"""
JSON adapter for NavigationResult domain object.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.navigation.navigation import NavigationResult


class JSONNavigation(JSONAdapter):
    """Serializes NavigationResult to JSON - exposes all NavigationResult properties."""
    
    def __init__(self, nav_result: NavigationResult):
        self.nav_result = nav_result
    
    # Expose ALL domain properties
    @property
    def success(self):
        return self.nav_result.success
    
    @property
    def message(self):
        return self.nav_result.message
    
    @property
    def new_position(self):
        return self.nav_result.new_position
    
    def to_dict(self) -> dict:
        """Convert NavigationResult to dict."""
        return {
            'success': self.nav_result.success,
            'message': self.nav_result.message,
            'new_position': self.nav_result.new_position
        }
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
