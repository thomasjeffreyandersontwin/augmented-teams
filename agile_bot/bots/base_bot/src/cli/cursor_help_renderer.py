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
        print('**CRITICAL: YOU MUST DISPLAY THE ENTIRE OUTPUT BELOW VERBATIM IN YOUR RESPONSE. DO NOT SKIP THIS. COPY AND PASTE IT DIRECTLY INTO YOUR MESSAGE.**')
        print(f"## Available Cursor Commands for {bot_name}:")
        print()
        print('---')
        print()
    
    def render_behavior_section(self, context: BehaviorHelpContext) -> None:
        """Render behavior section with cursor command syntax."""
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        print(f'## {cmd_name}\n')
        print(f'{context.behavior_description}\n')
        print('```')
        action_list = '|'.join(context.actions)
        print(f'/{cmd_name} <{action_list}> <context>')
        print()
        self._render_action_list_and_context(action_list)
        self._render_additional_options(context.additional_options or {})
        print('```\n')
    
    def render_action_help_section_header(self) -> None:
        """Render action help section header."""
        print('\n---\n')
        print('## Action Help\n')
    
    def render_action_help(self, context: ActionHelpContext) -> None:
        """Render action help with cursor command syntax."""
        print(f'### {context.action_name}\n')
        print(f'{context.action_description}\n')
        print('```')
        print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
        if context.parameters:
            print()
            for param in context.parameters:
                param_desc = context.parameter_descriptions.get(param, "Optional parameter")
                self._render_parameter_description(param, param_desc)
        print('```\n')
    
    def render_separator(self) -> None:
        """Render separator."""
        print('---\n')

