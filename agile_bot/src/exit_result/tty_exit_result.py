"""
TTY adapter for ExitResult domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.exit_result.exit_result import ExitResult

class TTYExitResult(TTYAdapter):
    """Serializes ExitResult to TTY - exposes all ExitResult properties."""
    
    def __init__(self, exit_result: ExitResult):
        self.exit_result = exit_result
    
    # Expose ALL domain properties
    @property
    def should_exit(self):
        return self.exit_result.should_exit
    
    @property
    def message(self):
        return self.exit_result.message
    
    def serialize(self) -> str:
        """Convert ExitResult to TTY string."""
        if self.exit_result.message:
            return self.exit_result.message
        return "Exiting..." if self.exit_result.should_exit else ""
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
