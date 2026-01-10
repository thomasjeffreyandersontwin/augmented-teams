"""
JSON adapter for Instructions domain object.
"""

from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.instructions.instructions import Instructions

class JSONInstructions(JSONAdapter):
    """Serializes Instructions to JSON - returns structured instruction data."""
    
    def __init__(self, instructions: Instructions):
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to JSON string."""
        import json
        return json.dumps(self.to_dict(), indent=2)
    
    def to_dict(self) -> dict:
        """Convert Instructions to dictionary for JSON serialization."""
        return self.instructions.to_dict()
