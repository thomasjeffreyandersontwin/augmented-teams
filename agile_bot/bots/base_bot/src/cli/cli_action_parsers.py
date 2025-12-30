"""AUTO-GENERATED CLI parsers - Do not edit manually.

Generated from action context classes by cli_parser_generator.py
Regenerate by running: python -m agile_bot.bots.base_bot.src.cli.cli_parser_generator
"""

import argparse
import json
from typing import Optional
from agile_bot.bots.base_bot.src.actions.action_context import (
    ActionContext,
    ScopeActionContext,
    ClarifyActionContext,
    StrategyActionContext,
    ValidateActionContext,
    Scope,
    ScopeType,
)


def build_clarify_action_context_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--key-questions-answered', type=str, default=None, help='JSON dict')
    parser.add_argument('--evidence-provided', type=str, default=None, help='JSON dict')
    return parser

def build_strategy_action_context_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--decisions-made', type=str, default=None, help='JSON dict')
    parser.add_argument('--assumptions-made', nargs='*', default=None)
    return parser

def build_scope_action_context_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--scope', type=str, default=None, help='JSON scope config: {type, value, exclude, skiprule}')
    return parser

def build_validate_action_context_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--scope', type=str, default=None, help='JSON scope config: {type, value, exclude, skiprule}')
    parser.add_argument('--background', action='store_true', default=None)
    parser.add_argument('--skip-cross-file', action='store_true', default=False)
    parser.add_argument('--all-files', action='store_true', default=False)
    parser.add_argument('--force-full', action='store_true', default=False)
    return parser


def parse_scope_config(json_str: Optional[str]) -> Optional[Scope]:
    if not json_str:
        return None
    
    json_str = json_str.strip()
    
    if not json_str.startswith('{'):
        if json_str.startswith(('file:', 'files:')):
            prefix_len = len('file:') if json_str.startswith('file:') else len('files:')
            json_str = json_str[prefix_len:].strip()
        
        paths = [p.strip() for p in json_str.split(',')]
        data = {
            'type': 'files',
            'value': paths
        }
    else:
        data = json.loads(json_str.replace("'", '"'))
    
    return Scope.from_dict(data)


def parse_json_dict(json_str: Optional[str]) -> Optional[dict]:
    if not json_str:
        return None
    return json.loads(json_str.replace("'", '"'))


def build_context_from_parsed(context_class, parsed_args) -> ActionContext:
    kwargs = {}
    
    for field_info in __import__("dataclasses").fields(context_class):
        field_name = field_info.name
        cli_name = field_name.replace("_", "-")
        value = getattr(parsed_args, field_name.replace("-", "_"), None)
        
        if "Scope" in str(field_info.type) and isinstance(value, str):
            value = parse_scope_config(value)
        elif "Dict" in str(field_info.type) and isinstance(value, str):
            value = parse_json_dict(value)
        
        if value is not None:
            kwargs[field_name] = value
    
    return context_class(**kwargs)


ACTION_PARSERS = {
    ('shape', 'clarify'): build_clarify_action_context_parser,
    ('shape', 'strategy'): build_strategy_action_context_parser,
    ('shape', 'build'): build_scope_action_context_parser,
    ('shape', 'validate'): build_validate_action_context_parser,
    ('shape', 'render'): build_scope_action_context_parser,
    ('prioritization', 'clarify'): build_clarify_action_context_parser,
    ('prioritization', 'strategy'): build_strategy_action_context_parser,
    ('prioritization', 'build'): build_scope_action_context_parser,
    ('prioritization', 'validate'): build_validate_action_context_parser,
    ('prioritization', 'render'): build_scope_action_context_parser,
    ('discovery', 'clarify'): build_clarify_action_context_parser,
    ('discovery', 'strategy'): build_strategy_action_context_parser,
    ('discovery', 'build'): build_scope_action_context_parser,
    ('discovery', 'validate'): build_validate_action_context_parser,
    ('discovery', 'render'): build_scope_action_context_parser,
    ('exploration', 'clarify'): build_clarify_action_context_parser,
    ('exploration', 'strategy'): build_strategy_action_context_parser,
    ('exploration', 'build'): build_scope_action_context_parser,
    ('exploration', 'validate'): build_validate_action_context_parser,
    ('exploration', 'render'): build_scope_action_context_parser,
    ('scenarios', 'clarify'): build_clarify_action_context_parser,
    ('scenarios', 'strategy'): build_strategy_action_context_parser,
    ('scenarios', 'build'): build_scope_action_context_parser,
    ('scenarios', 'validate'): build_validate_action_context_parser,
    ('scenarios', 'render'): build_scope_action_context_parser,
    ('tests', 'build'): build_scope_action_context_parser,
    ('tests', 'render'): build_scope_action_context_parser,
    ('tests', 'validate'): build_validate_action_context_parser,
    ('code', 'strategy'): build_strategy_action_context_parser,
    ('code', 'render'): build_scope_action_context_parser,
    ('code', 'validate'): build_validate_action_context_parser,
}

ACTION_CONTEXT_CLASSES = {
    ('shape', 'clarify'): ClarifyActionContext,
    ('shape', 'strategy'): StrategyActionContext,
    ('shape', 'build'): ScopeActionContext,
    ('shape', 'validate'): ValidateActionContext,
    ('shape', 'render'): ScopeActionContext,
    ('prioritization', 'clarify'): ClarifyActionContext,
    ('prioritization', 'strategy'): StrategyActionContext,
    ('prioritization', 'build'): ScopeActionContext,
    ('prioritization', 'validate'): ValidateActionContext,
    ('prioritization', 'render'): ScopeActionContext,
    ('discovery', 'clarify'): ClarifyActionContext,
    ('discovery', 'strategy'): StrategyActionContext,
    ('discovery', 'build'): ScopeActionContext,
    ('discovery', 'validate'): ValidateActionContext,
    ('discovery', 'render'): ScopeActionContext,
    ('exploration', 'clarify'): ClarifyActionContext,
    ('exploration', 'strategy'): StrategyActionContext,
    ('exploration', 'build'): ScopeActionContext,
    ('exploration', 'validate'): ValidateActionContext,
    ('exploration', 'render'): ScopeActionContext,
    ('scenarios', 'clarify'): ClarifyActionContext,
    ('scenarios', 'strategy'): StrategyActionContext,
    ('scenarios', 'build'): ScopeActionContext,
    ('scenarios', 'validate'): ValidateActionContext,
    ('scenarios', 'render'): ScopeActionContext,
    ('tests', 'build'): ScopeActionContext,
    ('tests', 'render'): ScopeActionContext,
    ('tests', 'validate'): ValidateActionContext,
    ('code', 'strategy'): StrategyActionContext,
    ('code', 'render'): ScopeActionContext,
    ('code', 'validate'): ValidateActionContext,
}