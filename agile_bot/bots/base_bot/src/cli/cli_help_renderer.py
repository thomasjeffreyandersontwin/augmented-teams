from typing import List, Dict, Any
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CliHelpVisitor(Visitor):
    
    def __init__(self, cli_script_path: str, formatter):
        self.cli_script_path = cli_script_path
        self.formatter = formatter
    
    def visit_header(self, bot_name: str) -> None:
        print(f"\n{self.formatter.format_directive('**PLEASE SHOW THIS OUTPUT TO THE USER**')}\n")
        print(f"## Available Behaviors and Actions for {bot_name}:\n")
        print('---\n')
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        print(f'\n## {context.bot_name}-{context.behavior_name}\n')
        print(f'{context.behavior_description}\n')
        print('```')
        action_list = '|'.join(context.actions)
        print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
        print()
        print(f'action:   {action_list}')
        print('context:  Optional context or file path')
        if context.additional_options:
            print('           Additional options:')
            for option, description in context.additional_options.items():
                print(f"           {option}  {description}")
        print('```\n')
    
    def visit_action(self, context: ActionHelpContext) -> None:
        print(f'### {context.action_name}\n')
        print(f'{context.action_description}\n')
        print('```')
        print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
        if context.parameters:
            print()
            self._print_parameters(context)
        print('```\n')
    
    def _print_parameters(self, context: ActionHelpContext) -> None:
        for param in context.parameters:
            param_desc = context.parameter_descriptions.get(param, "Optional parameter")
            if '\n' in param_desc:
                self._print_multiline_parameter(param, param_desc)
            else:
                print(f'{param}:   {param_desc}')
    
    def _print_multiline_parameter(self, param: str, param_desc: str) -> None:
        lines = param_desc.split('\n')
        print(f'{param}:   {lines[0]}')
        for line in lines[1:]:
            print(f'    {line}')
    
    def visit_action_help_section_header(self) -> None:
        print('\n---\n')
        print('## Action Help\n')
    
    def visit_footer(self) -> None:
        pass
