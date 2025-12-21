"""CLI Parser Generator - generates argument parsers from action context classes.

This module generates Python code for CLI argument parsers by introspecting
action context classes. The generated code is static and debuggable.

Usage:
    python -m agile_bot.bots.base_bot.src.cli.cli_parser_generator

This will generate cli_action_parsers.py in the same directory.
"""

import dataclasses
from dataclasses import fields
from pathlib import Path
from typing import Type, List, Optional, Any, get_type_hints, get_origin, get_args
import inspect
import json

from agile_bot.bots.base_bot.src.actions.action_context import (
    ActionContext,
    ScopeActionContext, 
    ClarifyActionContext,
    StrategyActionContext,
    ValidateActionContext,
    ScopeConfig,
    ScopeType,
)


class CliParserGenerator:
    """Generates CLI argument parser code from action context classes."""
    
    def __init__(self):
        self._generated_lines: List[str] = []
    
    def generate_parsers_for_bot(self, bot) -> str:
        """Generate parser code for all actions in a bot."""
        self._generated_lines = []
        self._add_header()
        self._add_imports()
        
        # Collect all unique context classes
        context_classes_seen = set()
        action_mappings = []
        
        for behavior in bot.behaviors:
            for action in behavior.actions:
                context_class = action.context_class
                action_name = action.action_name
                
                # Generate parser for this context class if not seen
                if context_class not in context_classes_seen:
                    context_classes_seen.add(context_class)
                    self._generate_parser_function(context_class)
                
                # Record mapping
                action_mappings.append((behavior.name, action_name, context_class.__name__))
        
        self._add_blank_line()
        self._generate_context_builder_functions()
        self._add_blank_line()
        self._generate_action_parser_mapping(action_mappings)
        
        return '\n'.join(self._generated_lines)
    
    def generate_parser_for_context_class(self, context_class: Type[ActionContext]) -> str:
        """Generate parser function for a single context class."""
        self._generated_lines = []
        self._add_header()
        self._add_imports()
        self._generate_parser_function(context_class)
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
            '    ScopeConfig,',
            '    ScopeType,',
            ')',
            '',
            '',
        ])
    
    def _add_blank_line(self):
        self._generated_lines.append('')
    
    def _generate_parser_function(self, context_class: Type[ActionContext]):
        """Generate a parser function for a context class."""
        class_name = context_class.__name__
        func_name = f'build_{self._to_snake_case(class_name)}_parser'
        
        self._generated_lines.append(f'def {func_name}() -> argparse.ArgumentParser:')
        self._generated_lines.append(f'    """Build argument parser for {class_name}."""')
        self._generated_lines.append(f'    parser = argparse.ArgumentParser(add_help=False)')
        
        # Get all fields including inherited ones
        all_fields = self._get_all_fields(context_class)
        
        for field_info in all_fields:
            self._add_argument_for_field(field_info)
        
        self._generated_lines.append('    return parser')
        self._generated_lines.append('')
    
    def _get_all_fields(self, context_class: Type[ActionContext]) -> list:
        """Get all dataclass fields including inherited ones."""
        if not dataclasses.is_dataclass(context_class):
            return []
        return list(fields(context_class))
    
    def _add_argument_for_field(self, field_info):
        """Add argparse argument for a dataclass field."""
        name = field_info.name
        field_type = field_info.type
        default = field_info.default
        
        cli_name = f'--{name.replace("_", "-")}'
        
        # Determine argument configuration based on type
        if field_type == bool:
            if default is dataclasses.MISSING:
                default = False
            self._generated_lines.append(
                f"    parser.add_argument('{cli_name}', action='store_true', default={default})"
            )
        elif field_type == Optional[bool] or str(field_type) == 'typing.Optional[bool]':
            self._generated_lines.append(
                f"    parser.add_argument('{cli_name}', action='store_true', default=None)"
            )
        elif field_type == Optional[ScopeConfig] or 'ScopeConfig' in str(field_type):
            self._generated_lines.append(
                f"    parser.add_argument('{cli_name}', type=str, default=None, "
                f"help='JSON scope config: {{type, value, exclude, skiprule}}')"
            )
        elif 'Dict' in str(field_type):
            self._generated_lines.append(
                f"    parser.add_argument('{cli_name}', type=str, default=None, "
                f"help='JSON dict')"
            )
        elif 'List' in str(field_type):
            self._generated_lines.append(
                f"    parser.add_argument('{cli_name}', nargs='*', default=None)"
            )
        else:
            # Default: string argument
            default_str = 'None' if default is dataclasses.MISSING else repr(default)
            self._generated_lines.append(
                f"    parser.add_argument('{cli_name}', type=str, default={default_str})"
            )
    
    def _generate_context_builder_functions(self):
        """Generate functions to build context objects from parsed args."""
        self._generated_lines.extend([
            'def parse_scope_config(json_str: Optional[str]) -> Optional[ScopeConfig]:',
            '    """Parse JSON string into ScopeConfig object."""',
            '    if not json_str:',
            '        return None',
            '    data = json.loads(json_str.replace("\'", \'"\'))',
            '    return ScopeConfig.from_dict(data)',
            '',
            '',
            'def parse_json_dict(json_str: Optional[str]) -> Optional[dict]:',
            '    """Parse JSON string into dict."""',
            '    if not json_str:',
            '        return None',
            '    return json.loads(json_str.replace("\'", \'"\'))',
            '',
            '',
            'def build_context_from_parsed(context_class, parsed_args) -> ActionContext:',
            '    """Build typed context object from parsed argparse namespace."""',
            '    kwargs = {}',
            '    ',
            '    for field_info in __import__("dataclasses").fields(context_class):',
            '        field_name = field_info.name',
            '        cli_name = field_name.replace("_", "-")',
            '        value = getattr(parsed_args, field_name.replace("-", "_"), None)',
            '        ',
            '        # Handle special types',
            '        if "ScopeConfig" in str(field_info.type) and isinstance(value, str):',
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
        """Generate the ACTION_PARSERS mapping dict."""
        self._generated_lines.append('# Mapping from (behavior, action) to parser function')
        self._generated_lines.append('ACTION_PARSERS = {')
        
        for behavior_name, action_name, context_class_name in action_mappings:
            func_name = f'build_{self._to_snake_case(context_class_name)}_parser'
            self._generated_lines.append(
                f"    ('{behavior_name}', '{action_name}'): {func_name},"
            )
        
        self._generated_lines.append('}')
        self._generated_lines.append('')
        
        # Also map to context classes
        self._generated_lines.append('# Mapping from (behavior, action) to context class')
        self._generated_lines.append('ACTION_CONTEXT_CLASSES = {')
        
        for behavior_name, action_name, context_class_name in action_mappings:
            self._generated_lines.append(
                f"    ('{behavior_name}', '{action_name}'): {context_class_name},"
            )
        
        self._generated_lines.append('}')
    
    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case."""
        import re
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def generate_parsers_for_story_bot():
    """Generate parsers for story_bot."""
    from agile_bot.bots.story_bot.src.story_bot_cli import create_story_bot
    
    bot = create_story_bot()
    generator = CliParserGenerator()
    code = generator.generate_parsers_for_bot(bot)
    
    output_path = Path(__file__).parent / 'cli_action_parsers.py'
    output_path.write_text(code, encoding='utf-8')
    print(f'Generated: {output_path}')
    return code


if __name__ == '__main__':
    generate_parsers_for_story_bot()


