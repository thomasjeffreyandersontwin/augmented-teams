from typing import List, Dict, Any
from agile_bot.bots.base_bot.src.cli.help_renderer import HelpRenderer
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CliHelpRenderer(HelpRenderer):
    
    def __init__(self, cli_script_path: str, formatter):
        self.cli_script_path = cli_script_path
        self.formatter = formatter
    
    def render_header(self, bot_name: str) -> None:
        print(f"\n{self.formatter.format_directive('**PLEASE SHOW THIS OUTPUT TO THE USER**')}\n")
        print(f"## Available Behaviors and Actions for {bot_name}:\n")
        print('---\n')
    
    def _format_behavior_title(self, context: BehaviorHelpContext) -> str:
        return f'## {context.bot_name}-{context.behavior_name}'
    
    def _format_behavior_command(self, context: BehaviorHelpContext, action_list: str) -> str:
        return f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]'
    
    def _format_action_command(self, context: ActionHelpContext) -> str:
        return f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]'

