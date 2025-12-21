"""CLI Context Builder - builds typed ActionContext from CLI arguments.

This module bridges the CLI and actions by:
1. Looking up the action's context_class
2. Using the generated parser for that context class
3. Parsing CLI args and building a typed context object
"""

import argparse
import json
from typing import Type, List, Optional, Any
from pathlib import Path

from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import (
    ActionContext,
    ScopeConfig,
    ScopeType,
)


class CliContextBuilder:
    """Builds typed ActionContext from CLI arguments."""
    
    def build_context(self, action: Action, cli_args: List[str]) -> ActionContext:
        """Parse CLI args and return typed context for the action.
        
        Args:
            action: The action to build context for
            cli_args: Remaining CLI arguments after behavior/action parsing
            
        Returns:
            Typed ActionContext subclass populated from CLI args
        """
        context_class = action.context_class
        
        # Build parser from context class
        parser = self.build_parser_from_context_class(context_class)
        
        # Parse the args
        parsed, remaining = parser.parse_known_args(cli_args)
        
        if remaining:
            # Check for unrecognized flags
            for arg in remaining:
                if arg.startswith('--'):
                    raise ValueError(
                        f"Unrecognized argument '{arg}' for action '{action.action_name}'. "
                        f"Valid arguments: {self._get_valid_args(context_class)}"
                    )
        
        # Convert to typed context
        return self._build_context_from_parsed(context_class, parsed)
    
    def build_parser_from_context_class(self, context_class: Type[ActionContext]) -> argparse.ArgumentParser:
        """Build argparse parser from context class fields.
        
        This is used at generation time to create static parsers,
        but can also be used at runtime for dynamic parsing.
        """
        import dataclasses
        
        parser = argparse.ArgumentParser(add_help=False)
        
        if not dataclasses.is_dataclass(context_class):
            return parser
        
        for field_info in dataclasses.fields(context_class):
            self._add_argument_for_field(parser, field_info)
        
        return parser
    
    def _add_argument_for_field(self, parser: argparse.ArgumentParser, field_info) -> None:
        """Add argparse argument matching the dataclass field."""
        name = field_info.name
        field_type = field_info.type
        
        cli_name = f'--{name.replace("_", "-")}'
        dest_name = name  # Keep underscores for dest
        
        import dataclasses
        default = field_info.default if field_info.default is not dataclasses.MISSING else None
        
        # Determine argument type based on field type
        if field_type == bool:
            parser.add_argument(cli_name, dest=dest_name, action='store_true', default=default or False)
        elif 'Optional[bool]' in str(field_type):
            parser.add_argument(cli_name, dest=dest_name, action='store_true', default=None)
        elif 'ScopeConfig' in str(field_type):
            parser.add_argument(cli_name, dest=dest_name, type=str, default=None)
        elif 'Dict' in str(field_type):
            parser.add_argument(cli_name, dest=dest_name, type=str, default=None)
        elif 'List' in str(field_type):
            parser.add_argument(cli_name, dest=dest_name, nargs='*', default=None)
        else:
            parser.add_argument(cli_name, dest=dest_name, type=str, default=default)
    
    def _build_context_from_parsed(self, context_class: Type[ActionContext], parsed: argparse.Namespace) -> ActionContext:
        """Build typed context object from parsed argparse namespace."""
        import dataclasses
        
        kwargs = {}
        
        for field_info in dataclasses.fields(context_class):
            field_name = field_info.name
            value = getattr(parsed, field_name, None)
            
            # Handle special type conversions
            if 'ScopeConfig' in str(field_info.type) and isinstance(value, str):
                value = self._parse_scope_config(value)
            elif 'Dict' in str(field_info.type) and isinstance(value, str):
                value = self._parse_json_dict(value)
            
            if value is not None:
                kwargs[field_name] = value
        
        return context_class(**kwargs)
    
    def _parse_scope_config(self, json_str: str) -> Optional[ScopeConfig]:
        """Parse JSON string into ScopeConfig object."""
        if not json_str:
            return None
        # Handle Python dict syntax (single quotes) by replacing with double quotes
        data = json.loads(json_str.replace("'", '"'))
        return ScopeConfig.from_dict(data)
    
    def _parse_json_dict(self, json_str: str) -> Optional[dict]:
        """Parse JSON string into dict."""
        if not json_str:
            return None
        return json.loads(json_str.replace("'", '"'))
    
    def _get_valid_args(self, context_class: Type[ActionContext]) -> List[str]:
        """Get list of valid argument names for a context class."""
        import dataclasses
        
        if not dataclasses.is_dataclass(context_class):
            return []
        
        return [f'--{f.name.replace("_", "-")}' for f in dataclasses.fields(context_class)]





