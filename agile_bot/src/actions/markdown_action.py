"""
Base Markdown adapter for Action domain objects.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter

class MarkdownAction(MarkdownAdapter):
    """Base Markdown adapter for Action - provides common serialization for status display."""
    
    def __init__(self, action, is_current: bool = False, is_completed: bool = False):
        self.action = action
        self.is_current = is_current
        self.is_completed = is_completed
    
    @property
    def action_name(self):
        """Returns formatted action name with marker."""
        is_completed = getattr(self.action, 'is_completed', False)
        
        if self.is_current:
            marker = "➤"
        elif is_completed:
            marker = "[X]"
        else:
            marker = "[ ]"
        
        description = getattr(self.action, 'description', '')
        
        if description and self.is_current:
            return f"  {marker} **{self.action.action_name}** - {description}"
        elif self.is_current:
            return f"  {marker} **{self.action.action_name}**"
        else:
            return f"  {marker} {self.action.action_name}"
    
    
    def serialize(self) -> str:
        """Convert Action to Markdown string - returns formatted properties."""
        return self.action_name
