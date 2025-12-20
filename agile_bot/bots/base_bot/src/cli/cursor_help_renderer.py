from typing import List, Dict, Any
from pathlib import Path
from agile_bot.bots.base_bot.src.cli.help_renderer import HelpRenderer
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CursorHelpRenderer(HelpRenderer):
    """Renders help output for cursor commands."""
    
    def __init__(self, bot_name: str, formatter):
        self.bot_name = bot_name
        self.formatter = formatter
    
    def render_header(self, bot_name: str) -> None:
        """Render cursor help header."""
        print(f"## Available Cursor Commands for {bot_name}:")
        print()
        print('---')
        print()
    
    def _format_behavior_title(self, context: BehaviorHelpContext) -> str:
        """Format the behavior section title for cursor commands."""
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        return f'## {cmd_name}'
    
    def _format_behavior_command(self, context: BehaviorHelpContext, action_list: str) -> str:
        """Format the command line for a behavior (cursor format)."""
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        return f'/{cmd_name} <{action_list}> <context>'
    
    def _format_action_command(self, context: ActionHelpContext) -> str:
        """Format the command line for an action (cursor format)."""
        return f'/{context.bot_name}-<behavior> {context.action_name} [parameters]'

