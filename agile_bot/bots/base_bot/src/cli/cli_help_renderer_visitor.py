from typing import List, Dict, Any, Optional
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.generator.help_context import BehaviorHelpContext, ActionHelpContext
from agile_bot.bots.base_bot.src.generator.action_data_collector import ActionDataCollector
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.cli.formatter import CliTerminalFormatter

class CliHelpRendererVisitor(Visitor):
    
    def __init__(self, cli_script_path: str, bot=None):
        super().__init__(bot=bot)
        self.cli_script_path = cli_script_path
        self._formatter: Optional[CliTerminalFormatter] = None
        self._description_extractor: Optional[DescriptionExtractor] = None
        self._data_collector: Optional[ActionDataCollector] = None
    
    @property
    def formatter(self) -> CliTerminalFormatter:
        if self._formatter is None:
            self._formatter = CliTerminalFormatter()
        return self._formatter
    
    @property
    def description_extractor(self) -> DescriptionExtractor:
        if self._description_extractor is None:
            self._description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, self.formatter)
        return self._description_extractor
    
    @property
    def data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            self._data_collector = ActionDataCollector(
                bot=self.bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_directory,
                description_extractor=self.description_extractor
            )
        return self._data_collector
    
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
            if self._has_dict_or_value_params(context.parameters):
                print()
                print('Note: PowerShell users must use = syntax: --parameter="value"')
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
    
    def _has_dict_or_value_params(self, parameters: List[str]) -> bool:
        """Check if any parameters take values (not just flags)."""
        for param in parameters:
            if '<flag>' not in param:
                return True
        return False
    
    def visit_action_help_section_header(self) -> None:
        print('\n---\n')
        print('## Action Help\n')
    
    def visit_footer(self) -> None:
        pass

