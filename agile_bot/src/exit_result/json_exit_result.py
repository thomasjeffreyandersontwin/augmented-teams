"""
JSON adapter for ExitResult domain object.
"""

import json
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.exit_result.exit_result import ExitResult


class JSONExitResult(JSONAdapter):
    """Serializes ExitResult to JSON - exposes all ExitResult properties."""
    
    def __init__(self, exit_result: ExitResult):
        self.exit_result = exit_result
    
    # Expose ALL domain properties
    @property
    def should_exit(self):
        return self.exit_result.should_exit
    
    @property
    def message(self):
        return self.exit_result.message
    
    def to_dict(self) -> dict:
        """Convert ExitResult to dict."""
        return {
            'should_exit': self.exit_result.should_exit,
            'message': self.exit_result.message
        }
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
