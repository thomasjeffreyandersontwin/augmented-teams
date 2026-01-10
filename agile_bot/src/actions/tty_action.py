"""
TTY adapter for Action domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter


class TTYAction(TTYAdapter):
    """Serializes Action to TTY - exposes all Action properties."""
    
    def __init__(self, action, is_current: bool = False, is_completed: bool = False):
        """
        Initialize TTY adapter for Action.
        
        Args:
            action: Action to serialize
            is_current: Whether this is the current action
            is_completed: Whether this action is completed
        """
        self.action = action
        self.is_current = is_current
        self._is_completed = is_completed
    
    # Expose ALL domain properties as FORMATTED display strings
    @property
    def action_name(self):
        """Returns formatted action name with icon and description."""
        if self.is_current:
            icon = "➤ "
        elif self._is_completed:
            icon = "☑ "  # Checked box
        else:
            icon = "☐ "  # Empty box to align with chevron + space
        
        # Get description if available
        description = getattr(self.action, 'description', '')
        
        # Show description for current action
        if description and self.is_current:
            return f"  {icon}{self.add_bold(self.action.action_name)} - {description}"
        elif self.is_current:
            return f"  {icon}{self.add_bold(self.action.action_name)}"
        else:
            return f"  {icon}{self.action.action_name}"
    
    @property
    def operations(self):
        """Returns formatted operations (instructions/confirm) for current action."""
        if not self.is_current:
            return ""
        
        lines = []
        
        # Get current phase/stage if available
        stage = getattr(self.action, 'phase', None) or getattr(self.action, 'stage', None) or 'not_started'
        is_completed = getattr(self.action, 'is_completed', False)
        
        # Instructions operation
        if stage == 'instructions' or stage == 'not_started':
            instr_icon = "➤ "
            instr_text = self.add_bold("instructions")
        elif stage in ('confirming', 'complete'):
            instr_icon = "☑ "  # Checked box
            instr_text = "instructions"
        else:
            instr_icon = "☐ "  # Empty box to align with chevron + space
            instr_text = "instructions"
        lines.append(f"    {instr_icon}{instr_text}")
        
        # Confirm operation
        if stage == 'confirming':
            confirm_icon = "➤ "
            confirm_text = self.add_bold("confirm")
        elif stage == 'complete' or self._is_completed:
            confirm_icon = "☑ "  # Checked box
            confirm_text = "confirm"
        else:
            confirm_icon = "☐ "  # Empty box to align with chevron + space
            confirm_text = "confirm"
        lines.append(f"    {confirm_icon}{confirm_text}")
        
        return '\n'.join(lines)
    
    @property
    def name(self):
        """Returns action name."""
        return self.action.action_name
    
    @property
    def domain_action(self):
        """Returns underlying domain action (raw)."""
        return self.action
    
    def serialize(self) -> str:
        """Convert Action to TTY string - returns formatted properties."""
        lines = []
        lines.append(self.action_name)
        
        # Show operations (instructions/confirm) for current action
        if self.is_current:
            ops = self.operations
            if ops:
                lines.append(ops)
        
        return '\n'.join(lines)
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text into verb and args."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
