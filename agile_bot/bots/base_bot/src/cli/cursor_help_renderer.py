from typing import List, Dict, Any
from pathlib import Path
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CursorHelpVisitor(Visitor):
    
    def __init__(self, bot_name: str, formatter):
        self.bot_name = bot_name
        self.formatter = formatter
    
    def visit_header(self, bot_name: str) -> None:
        name = bot_name if bot_name is not None else self.bot_name
        print(f"## Available Cursor Commands for {name}:")
        print()
        print('---')
        print()
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        print(f'\n## {cmd_name}\n')
        print(f'{context.behavior_description}\n')
        print('```')
        action_list = '|'.join(context.actions)
        print(f'/{cmd_name} <{action_list}> <context>')
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
        print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
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
