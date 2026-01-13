"""
JSON adapter for Scope domain object.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.scope.scope import Scope


class JSONScope(JSONAdapter):
    """Serializes Scope to JSON - exposes all Scope properties."""
    
    def __init__(self, scope: Scope):
        self.scope = scope
    
    # Expose ALL domain properties
    @property
    def type(self):
        return self.scope.type
    
    @property
    def value(self):
        return self.scope.value
    
    @property
    def exclude(self):
        return self.scope.exclude
    
    @property
    def skiprule(self):
        return self.scope.skiprule
    
    @property
    def story_graph_filter(self):
        return self.scope.story_graph_filter
    
    @property
    def file_filter(self):
        return self.scope.file_filter
    
    def to_dict(self) -> dict:
        """Convert Scope to dict."""
        return self.scope.to_dict()
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
