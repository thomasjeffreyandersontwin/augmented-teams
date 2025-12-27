from typing import List, Dict, Any, Optional
from pathlib import Path
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.generator.help_context import BehaviorHelpContext, ActionHelpContext
from agile_bot.bots.base_bot.src.generator.action_data_collector import ActionDataCollector
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.cli.formatter import CliTerminalFormatter

class CursorHelpRendererVisitor(Visitor):
    
    def __init__(self, bot=None, instructions=None):
        super().__init__(bot=bot)
        self.instructions = instructions
        self._output_lines = []
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
    
    def _add_line(self, line: str) -> None:
        if self.instructions:
            self.instructions.add_display(line)
        else:
            self._output_lines.append(line)
            print(line)
    
    def visit_header(self, bot_name: str) -> None:
        name = bot_name if bot_name is not None else self.bot_name
        self._add_line(f"## Available Cursor Commands for {name}:")
        self._add_line('')
        self._add_line('---')
        self._add_line('')
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        cmd_name = f'{context.bot_name}-{context.behavior_name}'
        self._add_line(f'## {cmd_name}')
        self._add_line('')
        self._add_line(f'{context.behavior_description}')
        self._add_line('')
        self._add_line('```')
        action_list = '|'.join(context.actions)
        self._add_line(f'/{cmd_name} <{action_list}> <context>')
        self._add_line('')
        self._add_line(f'action:   {action_list}')
        self._add_line('context:  Optional context or file path')
        if context.additional_options:
            self._add_line('           Additional options:')
            for option, description in context.additional_options.items():
                self._add_line(f"           {option}  {description}")
        self._add_line('```')
        self._add_line('')
    
    def visit_action(self, context: ActionHelpContext) -> None:
        self._add_line(f'### {context.action_name}')
        self._add_line('')
        self._add_line(f'{context.action_description}')
        self._add_line('')
        self._add_line('```')
        self._add_line(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
        if context.parameters:
            self._add_line('')
            self._add_parameters(context)
        self._add_line('```')
        self._add_line('')
    
    def _add_parameters(self, context: ActionHelpContext) -> None:
        for param in context.parameters:
            param_desc = context.parameter_descriptions.get(param, "Optional parameter")
            if '\n' in param_desc:
                self._add_multiline_parameter(param, param_desc)
            else:
                self._add_line(f'{param}:   {param_desc}')
    
    def _add_multiline_parameter(self, param: str, param_desc: str) -> None:
        lines = param_desc.split('\n')
        self._add_line(f'{param}:   {lines[0]}')
        for line in lines[1:]:
            self._add_line(f'    {line}')
    
    def visit_action_help_section_header(self) -> None:
        self._add_line('---')
        self._add_line('')
        self._add_line('## Action Help')
        self._add_line('')
    
    def visit_footer(self) -> None:
        pass
    
    def get_output_lines(self) -> List[str]:
        return self._output_lines




