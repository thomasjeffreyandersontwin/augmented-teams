from abc import ABC, abstractmethod
from typing import List, Dict, Any
from pathlib import Path
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.generator.help_context import BehaviorHelpContext, ActionHelpContext

class HelpRenderer(Visitor):
    
    def visit_header(self, bot_name: str) -> None:
        self.render_header(bot_name)
    
    @abstractmethod
    def render_header(self, bot_name: str) -> None:
        pass
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        self.render_behavior_section(context)
    
    def visit_action(self, context: ActionHelpContext) -> None:
        self.render_action_help(context)
    
    def visit_action_help_section_header(self) -> None:
        self.render_action_help_section_header()
    
    @abstractmethod
    def _format_behavior_command(self, context: BehaviorHelpContext, action_list: str) -> str:
        pass
    
    @abstractmethod
    def _format_behavior_title(self, context: BehaviorHelpContext) -> str:
        pass
    
    @abstractmethod
    def _format_action_command(self, context: ActionHelpContext) -> str:
        pass
    
    def render_behavior_section(self, context: BehaviorHelpContext) -> None:
        print(f'\n{self._format_behavior_title(context)}\n')
        print(f'{context.behavior_description}\n')
        print('```')
        action_list = '|'.join(context.actions)
        print(self._format_behavior_command(context, action_list))
        print()
        self._render_action_list_and_context(action_list)
        self._render_additional_options(context.additional_options or {})
        print('```\n')
    
    def render_action_help_section_header(self) -> None:
        print('\n---\n')
        print('## Action Help\n')
    
    def render_action_help(self, context: ActionHelpContext) -> None:
        print(f'### {context.action_name}\n')
        print(f'{context.action_description}\n')
        print('```')
        print(self._format_action_command(context))
        if context.parameters:
            print()
            for param in context.parameters:
                param_desc = context.parameter_descriptions.get(param, "Optional parameter")
                self._render_parameter_description(param, param_desc)
        print('```\n')
    
    def render_separator(self) -> None:
        print('---\n')
    
    def _render_parameter_description(self, param: str, param_desc: str) -> None:
        if '\n' in param_desc:
            lines = param_desc.split('\n')
            print(f'{param}:   {lines[0]}')
            for line in lines[1:]:
                print(f'    {line}')
        else:
            print(f'{param}:   {param_desc}')
    
    def _render_action_list_and_context(self, action_list: str) -> None:
        print(f'action:   {action_list}')
        print('context:  Optional context or file path')
    
    def _render_additional_options(self, additional_options: Dict[str, str]) -> None:
        if additional_options:
            print('           Additional options:')
            for option, description in additional_options.items():
                print(f"           {option}  {description}")
