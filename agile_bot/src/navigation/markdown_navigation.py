"""
Markdown adapter for NavigationResult domain object.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.navigation.navigation import NavigationResult

class MarkdownNavigation(MarkdownAdapter):
    """Serializes NavigationResult to Markdown."""
    
    def __init__(self, nav_result: NavigationResult):
        self.nav_result = nav_result
    
    def serialize(self) -> str:
        """Convert NavigationResult to Markdown string."""
        lines = []
        
        # Status header
        status = "✓ Success" if self.nav_result.success else "✗ Failed"
        lines.append(self.format_header(2, f"Navigation: {status}"))
        lines.append("")
        
        # Message if present
        if self.nav_result.message:
            lines.append(self.nav_result.message)
            lines.append("")
        
        # New position
        if self.nav_result.new_position:
            lines.append(f"**Position:** `{self.nav_result.new_position}`")
            lines.append("")
        
        return ''.join(lines)
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
