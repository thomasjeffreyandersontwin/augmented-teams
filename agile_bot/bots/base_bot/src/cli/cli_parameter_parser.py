import argparse
import json
from pathlib import Path
from typing import Dict, Tuple, Any, List

class CliParameterParser:

    @staticmethod
    def parse_arguments(description: str='Bot CLI') -> Tuple[argparse.Namespace, List[str]]:
        parser = CliParameterParser._create_argument_parser(description)
        args, unknown = parser.parse_known_args()
        unknown = CliParameterParser._relocate_file_path_from_action(args, unknown)
        
        remaining_args = CliParameterParser._build_remaining_args(args, unknown)
        return (args, remaining_args)
    
    @staticmethod
    def _build_remaining_args(args: argparse.Namespace, unknown: List[str]) -> List[str]:
        remaining = list(unknown)
        
        context_args = getattr(args, 'context', []) or []
        for ctx_arg in context_args:
            if ctx_arg not in remaining:
                remaining.append(ctx_arg)
        
        if args.skip_cross_file:
            remaining.append('--skip-cross-file')
        if args.all_files:
            remaining.append('--all-files')
        if args.scope:
            remaining.append(f'--scope={args.scope}')
        
        return remaining

    @staticmethod
    def _create_argument_parser(description: str) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description=description, add_help=False)
        parser.add_argument('--behavior', nargs='?', help='Behavior name (optional)')
        parser.add_argument('--action', nargs='?', help='Action name (optional)')
        parser.add_argument('--user_message', nargs='?', help='User message from Cursor (optional)')
        parser.add_argument('--close', action='store_true', help='Close current action')
        parser.add_argument('--list', action='store_true', help='List available options')
        parser.add_argument('--help-cursor', action='store_true', help='List all cursor commands and parameters')
        parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
        parser.add_argument('--skip-cross-file', action='store_true', help='Skip cross-file duplicate checking (default: False, meaning cross-file check runs)')
        parser.add_argument('--all-files', action='store_true', help='Scan all files instead of only changed files (default: False, meaning incremental scan)')
        parser.add_argument('--scope', nargs='?', help='Scope parameter: JSON dict like {"type": "files", "value": ["path/to/file.py"], "exclude": ["pattern"], "skiprule": ["rule"]}')
        parser.add_argument('context', nargs='*', help='Additional context (file paths, parameters, etc.)')
        return parser

    @staticmethod
    def _relocate_file_path_from_action(args: argparse.Namespace, unknown: list) -> list:
        if args.action and CliParameterParser._looks_like_file_path(args.action):
            unknown.append(args.action)
            args.action = None
        return unknown

    @staticmethod
    def _build_params_from_args(args: argparse.Namespace, unrecognized_flags: list) -> Dict[str, Any]:
        params = {}
        
        CliParameterParser._process_unrecognized_flags(unrecognized_flags, params)
        
        context_args = getattr(args, 'context', []) or []
        CliParameterParser._process_context_args(context_args, params)
        
        # Overlay explicit named flags
        if args.user_message:
            params['user_message'] = args.user_message
        if args.skip_cross_file:
            params['skip_cross_file'] = True
        if args.all_files:
            params['all_files'] = True
        if args.scope:
            params['scope'] = args.scope
        
        params = CliParameterParser._parse_json_parameters(params)
        return params

    @staticmethod
    def _looks_like_file_path(arg: str) -> bool:
        arg_clean = arg.lstrip('@')
        return '.' in arg_clean and (arg_clean.endswith(('.txt', '.md', '.json', '.yaml', '.yml', '.py', '.js', '.ts')) or '/' in arg_clean or '\\' in arg_clean) or arg_clean.startswith(('./', '../')) or '/' in arg_clean or ('\\' in arg_clean)

    @staticmethod
    def _looks_like_directory_path(arg: str) -> bool:
        arg_clean = arg.lstrip('@')
        has_separator = '/' in arg_clean or '\\' in arg_clean
        has_extension = '.' in arg_clean and any((arg_clean.endswith(ext) for ext in ('.txt', '.md', '.json', '.yaml', '.yml', '.py', '.js', '.ts', '.ps1', '.sh', '.bat')))
        return has_separator and (not has_extension)

    @staticmethod
    def _append_to_param(params: Dict, key: str, value: str) -> None:
        if key not in params:
            params[key] = [value]
        elif isinstance(params[key], str):
            params[key] = [params[key], value]
        else:
            params[key].append(value)

    @staticmethod
    def _parse_key_value_arg(arg: str, arg_list: list, i: int, params: Dict) -> int:
        key, value = arg.split('=', 1)
        key = key.lstrip('--')
        value_stripped = value.strip()
        if (value_stripped.startswith('{') or value_stripped.startswith('[')) and not CliParameterParser._is_complete_json(value_stripped):
            # Try to reconstruct JSON by collecting more arguments
            json_parts = [value]
            j = i + 1
            while j < len(arg_list):
                next_arg = arg_list[j]
                # Stop if we hit another key=value or flag
                if '=' in next_arg or next_arg.startswith('--'):
                    break
                json_parts.append(next_arg)
                combined = ' '.join(json_parts)
                if CliParameterParser._is_complete_json(combined.strip()):
                    params[key] = combined.strip()
                    return j - i + 1
                j += 1
            # If we couldn't complete it, use what we have
            params[key] = ' '.join(json_parts).strip()
            return j - i
        params[key] = value
        return 1

    @staticmethod
    def _is_complete_json(value: str) -> bool:
        value = value.strip()
        if not (value.startswith('{') or value.startswith('[')):
            return False
        open_braces = value.count('{')
        close_braces = value.count('}')
        open_brackets = value.count('[')
        close_brackets = value.count(']')
        # Also check if it ends with } or ]
        if value.startswith('{'):
            return open_braces == close_braces and value.rstrip().endswith('}')
        elif value.startswith('['):
            return open_brackets == close_brackets and value.rstrip().endswith(']')
        return False

    @staticmethod
    def _parse_file_path_arg(arg: str, params: Dict) -> None:
        file_path = arg.lstrip('@')
        if 'increment_file' not in params:
            params['increment_file'] = file_path
        else:
            CliParameterParser._append_to_param(params, 'context_files', file_path)

    @staticmethod
    def _parse_context_arg(arg: str, params: Dict) -> None:
        if 'context' not in params:
            params['context'] = arg
        elif isinstance(params['context'], str):
            params['context'] = [params['context'], arg]
        else:
            params['context'].append(arg)

    @staticmethod
    def _process_unrecognized_flags(unrecognized_flags: list, params: Dict) -> None:
        i = 0
        while i < len(unrecognized_flags):
            arg = unrecognized_flags[i]
            
            if arg.startswith('--'):
                raise ValueError(f"Unrecognized flag: {arg}")
            
            if '=' in arg:
                consumed = CliParameterParser._parse_key_value_arg(arg, unrecognized_flags, i, params)
                i += consumed
            elif CliParameterParser._looks_like_file_path(arg):
                CliParameterParser._parse_file_path_arg(arg, params)
                i += 1
            else:
                CliParameterParser._parse_context_arg(arg, params)
                i += 1

    @staticmethod
    def _process_context_args(context_args: list, params: Dict) -> None:
        i = 0
        while i < len(context_args):
            arg = context_args[i]
            
            if '=' in arg:
                consumed = CliParameterParser._parse_key_value_arg(arg, context_args, i, params)
                i += consumed
            elif CliParameterParser._looks_like_file_path(arg):
                CliParameterParser._parse_file_path_arg(arg, params)
                i += 1
            else:
                CliParameterParser._parse_context_arg(arg, params)
                i += 1

    @staticmethod
    def _parse_json_parameters(params: Dict[str, Any]) -> Dict[str, Any]:
        parsed_params = {}
        for key, value in params.items():
            parsed_params[key] = CliParameterParser._parse_single_parameter(value)
        return parsed_params
    
    @staticmethod
    def _parse_single_parameter(value: Any) -> Any:
        if not isinstance(value, str):
            return value
        
        value = value.strip()
        
        if not (value.startswith('{') or value.startswith('[')):
            return value
        
        return CliParameterParser._parse_json_string(value)
    
    @staticmethod
    def _parse_json_string(value: str) -> Any:
        parsed = CliParameterParser._try_parse_json(value)
        if parsed is not None:
            return parsed
        
        fixed_value = CliParameterParser._try_fix_json(value)
        parsed = CliParameterParser._try_parse_json(fixed_value)
        
        return parsed if parsed is not None else value
    
    @staticmethod
    def _try_parse_json(value: str) -> Any:
        try:
            return json.loads(value)
        except (json.JSONDecodeError, ValueError):
            return None

    @staticmethod
    def _try_fix_json(value: str) -> str:
        return value.replace("'", '"')