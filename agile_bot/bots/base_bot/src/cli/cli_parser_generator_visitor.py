"""CLI Parser Generator Visitor - generates argument parsers using visitor pattern.

This visitor generates Python code for CLI argument parsers by visiting
action context classes through the standard bot traversal pattern.
"""

import dataclasses
from dataclasses import fields
from typing import Type, List, Any

from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.generator.help_context import BehaviorHelpContext, ActionHelpContext
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext, Scope


class CliParserGeneratorVisitor(Visitor):
    
    def __init__(self, bot):
        super().__init__(bot=bot)
        self._generated_lines: List[str] = []
        self._context_classes_seen = set()
        self._action_mappings = []
    
    def visit_header(self, bot_name: str) -> None:
        self._add_header()
        self._add_imports()
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        pass
    
    def visit_action(self, context: ActionHelpContext) -> None:
        action = context.action
        if action is None:
            return
        
        context_class = action.context_class
        if context_class not in self._context_classes_seen:
            self._context_classes_seen.add(context_class)
            self._generate_parser_function(context_class)
        
        self._action_mappings.append((
            context.behavior_name,
            context.action_name,
            context_class.__name__
        ))
    
    def visit_action_help_section_header(self) -> None:
        pass
    
    def visit_footer(self) -> None:
        self._add_blank_line()
        self._generate_context_builder_functions()
        self._add_blank_line()
        self._generate_action_parser_mapping(self._action_mappings)
    
    def get_generated_code(self) -> str:
        return '\n'.join(self._generated_lines)
    
    def _add_header(self):
        self._generated_lines.extend([
            '"""AUTO-GENERATED CLI parsers - Do not edit manually.',
            '',
            'Generated from action context classes by cli_parser_generator.py',
            'Regenerate by running: python -m agile_bot.bots.base_bot.src.cli.cli_parser_generator',
            '"""',
            '',
        ])
    
    def _add_imports(self):
        self._generated_lines.extend([
            'import argparse',
            'import json',
            'from typing import Optional',
            'from agile_bot.bots.base_bot.src.actions.action_context import (',
            '    ActionContext,',
            '    ScopeActionContext,',
            '    ClarifyActionContext,',
            '    StrategyActionContext,',
            '    ValidateActionContext,',
            '    Scope,',
            '    ScopeType,',
            ')',
            '',
            '',
        ])
    
    def _add_blank_line(self):
        self._generated_lines.append('')
    
    def _generate_parser_function(self, context_class: Type[ActionContext]):
        class_name = context_class.__name__
        func_name = f'build_{self._to_snake_case(class_name)}_parser'
        
        self._generated_lines.append(f'def {func_name}() -> argparse.ArgumentParser:')
        self._generated_lines.append(f'    parser = argparse.ArgumentParser(add_help=False)')
        
        all_fields = self._get_all_fields(context_class)
        
        for field_info in all_fields:
            self._add_argument_for_field(field_info)
        
        self._generated_lines.append('    return parser')
        self._generated_lines.append('')
    
    def _get_all_fields(self, context_class: Type[ActionContext]) -> list:
        if not dataclasses.is_dataclass(context_class):
            return []
        return list(fields(context_class))
    
    def _add_argument_for_field(self, field_info):
        name = field_info.name
        field_type = field_info.type
        default = field_info.default
        cli_name = f'--{name.replace("_", "-")}'
        
        if field_type == bool:
            self._add_bool_argument(cli_name, default)
            return
        
        if str(field_type) == 'typing.Optional[bool]':
            self._add_optional_bool_argument(cli_name)
            return
        
        if 'Scope' in str(field_type):
            self._add_scope_config_argument(cli_name)
            return
        
        if 'Dict' in str(field_type):
            self._add_dict_argument(cli_name)
            return
        
        if 'List' in str(field_type):
            self._add_list_argument(cli_name)
            return
        
        self._add_string_argument(cli_name, default)
    
    def _add_bool_argument(self, cli_name: str, default: Any) -> None:
        if default is dataclasses.MISSING:
            default = False
        self._generated_lines.append(
            f"    parser.add_argument('{cli_name}', action='store_true', default={default})"
        )
    
    def _add_optional_bool_argument(self, cli_name: str) -> None:
        self._generated_lines.append(
            f"    parser.add_argument('{cli_name}', action='store_true', default=None)"
        )
    
    def _add_scope_config_argument(self, cli_name: str) -> None:
        self._generated_lines.append(
            f"    parser.add_argument('{cli_name}', type=str, default=None, "
            f"help='JSON scope config: {{type, value, exclude, skiprule}}')"
        )
    
    def _add_dict_argument(self, cli_name: str) -> None:
        self._generated_lines.append(
            f"    parser.add_argument('{cli_name}', type=str, default=None, "
            f"help='JSON dict')"
        )
    
    def _add_list_argument(self, cli_name: str) -> None:
        self._generated_lines.append(
            f"    parser.add_argument('{cli_name}', nargs='*', default=None)"
        )
    
    def _add_string_argument(self, cli_name: str, default: Any) -> None:
        default_str = 'None' if default is dataclasses.MISSING else repr(default)
        self._generated_lines.append(
            f"    parser.add_argument('{cli_name}', type=str, default={default_str})"
        )
    
    def _generate_context_builder_functions(self):
        self._generated_lines.extend([
            'def parse_scope_config(json_str: Optional[str]) -> Optional[Scope]:',
            '    if not json_str:',
            '        return None',
            '    data = json.loads(json_str.replace("\'", \'"\'))',
            '    return Scope.from_dict(data)',
            '',
            '',
            'def parse_json_dict(json_str: Optional[str]) -> Optional[dict]:',
            '    if not json_str:',
            '        return None',
            '    return json.loads(json_str.replace("\'", \'"\'))',
            '',
            '',
            'def build_context_from_parsed(context_class, parsed_args) -> ActionContext:',
            '    kwargs = {}',
            '    ',
            '    for field_info in __import__("dataclasses").fields(context_class):',
            '        field_name = field_info.name',
            '        cli_name = field_name.replace("_", "-")',
            '        value = getattr(parsed_args, field_name.replace("-", "_"), None)',
            '        ',
            '        if "Scope" in str(field_info.type) and isinstance(value, str):',
            '            value = parse_scope_config(value)',
            '        elif "Dict" in str(field_info.type) and isinstance(value, str):',
            '            value = parse_json_dict(value)',
            '        ',
            '        if value is not None:',
            '            kwargs[field_name] = value',
            '    ',
            '    return context_class(**kwargs)',
            '',
        ])
    
    def _generate_action_parser_mapping(self, action_mappings: list):
        self._generated_lines.append('ACTION_PARSERS = {')
        
        for behavior_name, action_name, context_class_name in action_mappings:
            func_name = f'build_{self._to_snake_case(context_class_name)}_parser'
            self._generated_lines.append(
                f"    ('{behavior_name}', '{action_name}'): {func_name},"
            )
        
        self._generated_lines.append('}')
        self._generated_lines.append('')
        
        self._generated_lines.append('ACTION_CONTEXT_CLASSES = {')
        
        for behavior_name, action_name, context_class_name in action_mappings:
            self._generated_lines.append(
                f"    ('{behavior_name}', '{action_name}'): {context_class_name},"
            )
        
        self._generated_lines.append('}')
    
    def _to_snake_case(self, name: str) -> str:
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

