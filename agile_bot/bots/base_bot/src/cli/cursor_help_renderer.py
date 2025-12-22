from typing import List, Dict, Any
from pathlib import Path
from agile_bot.bots.base_bot.src.cli.help_renderer import HelpRenderer
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CursorHelpRenderer(HelpRenderer):
    
    def __init__(self, bot_name: str, formatter):
        self.bot_name = bot_name
        self.formatter = formatter
    
    def render_header(self, bot_name: str = None) -> None:
        name = bot_name if bot_name is not None else self.bot_name
        print(f"## Available Cursor Commands for {name}:")
        print()
        print('---')
        print()
    
    def _format_behavior_title(self, context: BehaviorHelpContext) -> str:
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        return f'## {cmd_name}'
    
    def _format_behavior_command(self, context: BehaviorHelpContext, action_list: str) -> str:
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        return f'/{cmd_name} <{action_list}> <context>'
    
    def _format_action_command(self, context: ActionHelpContext) -> str:
        return f'/{context.bot_name}-<behavior> {context.action_name} [parameters]'

