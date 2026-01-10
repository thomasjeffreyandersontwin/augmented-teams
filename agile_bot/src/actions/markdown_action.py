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
    
    @property
    def operations(self):
        """Returns formatted operations (instructions/confirm) for current action."""
        if not self.is_current:
            return ""
        
        lines = []
        stage = getattr(self.action, 'phase', None) or getattr(self.action, 'stage', None) or 'not_started'
        is_completed = getattr(self.action, 'is_completed', False)
        
        if stage == 'instructions' or stage == 'not_started':
            instr_marker = "➤"
            instr_text = "**instructions**"
        elif stage in ('confirming', 'complete'):
            instr_marker = "[X]"
            instr_text = "instructions"
        else:
            instr_marker = "[ ]"
            instr_text = "instructions"
        lines.append(f"    {instr_marker} {instr_text}")
        
        if stage == 'confirming':
            confirm_marker = "➤"
            confirm_text = "**confirm**"
        elif stage == 'complete' or is_completed:
            confirm_marker = "[X]"
            confirm_text = "confirm"
        else:
            confirm_marker = "[ ]"
            confirm_text = "confirm"
        lines.append(f"    {confirm_marker} {confirm_text}")
        
        return '\n'.join(lines)
    
    def serialize(self) -> str:
        """Convert Action to Markdown string - returns formatted properties."""
        lines = []
        lines.append(self.action_name)
        
        if self.is_current:
            ops = self.operations
            if ops:
                lines.append(ops)
        
        return '\n'.join(lines)
