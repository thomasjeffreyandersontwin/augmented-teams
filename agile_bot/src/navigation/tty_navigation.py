"""
TTY adapter for NavigationResult domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.navigation.navigation import NavigationResult

class TTYNavigation(TTYAdapter):
    """Serializes NavigationResult to TTY - exposes all NavigationResult properties."""
    
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
    
    def serialize(self) -> str:
        """Convert NavigationResult to TTY string."""
        lines = []
        
        # Status indicator
        if self.nav_result.success:
            lines.append(self.add_color("✓ Navigation successful", 'green'))
        else:
            lines.append(self.add_color("✗ Navigation failed", 'red'))
        
        # Message if present
        if self.nav_result.message:
            lines.append(self.nav_result.message)
        
        # New position
        if self.nav_result.new_position:
            lines.append(f"Position: {self.nav_result.new_position}")
        
        return '\n'.join(lines)
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
