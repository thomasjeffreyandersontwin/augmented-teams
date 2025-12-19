from typing import List, Dict, Any
from agile_bot.bots.base_bot.src.cli.help_renderer import HelpRenderer
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CliHelpRenderer(HelpRenderer):
    """Renders help output for CLI commands."""
    
    def __init__(self, cli_script_path: str, formatter):
        self.cli_script_path = cli_script_path
        self.formatter = formatter
    
    def render_header(self, bot_name: str) -> None:
        """Render CLI help header."""
        print(f"\n{self.formatter.format_directive('**PLEASE SHOW THIS OUTPUT TO THE USER**')}\n")
        print(f"## Available Behaviors and Actions for {bot_name}:\n")
        print('---\n')
    
    def render_behavior_section(self, context: BehaviorHelpContext) -> None:
        """Render behavior section with CLI command syntax."""
        print(f'\n## {context.bot_name}-{context.behavior_name}\n')
        print(f'{context.behavior_description}\n')
        print('```')
        action_list = '|'.join(context.actions)
        print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
        print()
        self._render_action_list_and_context(action_list)
        self._render_additional_options(context.additional_options or {})
        print('```\n')
    
    def render_action_help_section_header(self) -> None:
        """Render action help section header."""
        print('\n---\n')
        print('## Action Help\n')
    
    def render_action_help(self, context: ActionHelpContext) -> None:
        """Render action help with CLI command syntax."""
        print(f'### {context.action_name}\n')
        print(f'{context.action_description}\n')
        print('```')
        print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
        if context.parameters:
            print()
            for param in context.parameters:
                param_desc = context.parameter_descriptions.get(param, "Optional parameter")
                self._render_parameter_description(param, param_desc)
        print('```\n')
    
    def render_separator(self) -> None:
        """Render separator."""
        print('---\n')

