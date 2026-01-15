"""
JSON adapter for ScopeCommandResult domain object.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.scope.scope_command_result import ScopeCommandResult


class JSONScopeCommandResult(JSONAdapter):
    """Serializes ScopeCommandResult to JSON with full scope data."""
    
    def __init__(self, scope_result: ScopeCommandResult):
        self.scope_result = scope_result
    
    def to_dict(self) -> dict:
        """Convert ScopeCommandResult to dict for JSON serialization."""
        from agile_bot.src.scope.json_scope import JSONScope
        
        # Serialize the scope using JSONScope adapter (which includes content and graphLinks)
        scope_adapter = JSONScope(self.scope_result.scope)
        scope_dict = scope_adapter.to_dict()
        
        return {
            'status': self.scope_result.status,
            'message': self.scope_result.message,
            'scope': scope_dict
        }
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
