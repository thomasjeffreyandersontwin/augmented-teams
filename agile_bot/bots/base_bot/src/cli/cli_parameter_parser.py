import argparse
import json
from pathlib import Path
from typing import Dict, Tuple, Any

class CliParameterParser:

    @staticmethod
    def parse_arguments(description: str='Bot CLI') -> Tuple[argparse.Namespace, Dict[str, str]]:
        parser = CliParameterParser._create_argument_parser(description)
        args, unknown = parser.parse_known_args()
        unknown = CliParameterParser._handle_file_like_action(args, unknown)
        params = CliParameterParser._build_params_from_args(args, unknown)
        return (args, params)

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
        parser.add_argument('--skiprule', nargs='*', help='Rule names to skip during validation (e.g., eliminate_duplication)')
        parser.add_argument('--exclude', nargs='*', help='File patterns to exclude from validation (e.g., "agile_bot/bots/base_bot/src:*scanner*")')
        parser.add_argument('--skip-cross-file', action='store_true', help='Skip cross-file duplicate checking (default: False, meaning cross-file check runs)')
        parser.add_argument('--scope', nargs='?', help='Scope parameter: JSON dict like {"type": "files", "value": ["path/to/file.py"]} or simple file path')
        parser.add_argument('context', nargs='*', help='Additional context (file paths, parameters, etc.)')
        return parser

    @staticmethod
    def _handle_file_like_action(args: argparse.Namespace, unknown: list) -> list:
        if args.action and CliParameterParser._looks_like_file_path(args.action):
            unknown.append(args.action)
            args.action = None
        return unknown

    @staticmethod
    def _build_params_from_args(args: argparse.Namespace, unknown: list) -> Dict[str, Any]:
        all_args = list(unknown) + (getattr(args, 'context', []) or [])
        params = CliParameterParser._parse_action_parameters(all_args)
        if args.user_message:
            params['user_message'] = args.user_message
        if args.skiprule:
            params['skiprule'] = args.skiprule
        if args.exclude:
            exclude_list = [e for e in args.exclude if e.lower() != 'exclude']
            if exclude_list:
                params['exclude'] = exclude_list
        if args.skip_cross_file:
            params['skip_cross_file'] = True
        if args.scope:
            params['scope'] = args.scope
        
        # Parse JSON strings in parameters
        params = CliParameterParser._parse_json_parameters(params)
        return params

    @staticmethod
    def _looks_like_file_path(arg: str) -> bool:
        if not arg:
            return False
        arg_clean = arg.lstrip('@')
        return '.' in arg_clean and (arg_clean.endswith(('.txt', '.md', '.json', '.yaml', '.yml', '.py', '.js', '.ts')) or '/' in arg_clean or '\\' in arg_clean) or arg_clean.startswith(('./', '../')) or '/' in arg_clean or ('\\' in arg_clean)

    @staticmethod
    def _looks_like_directory_path(arg: str) -> bool:
        if not arg:
            return False
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
    def _parse_key_value_arg(arg: str, unknown_args: list, i: int, params: Dict) -> int:
        """Parse key=value argument. Returns number of arguments consumed."""
        key, value = arg.split('=', 1)
        key = key.lstrip('--')
        # Check if value looks like start of JSON that might be split
        value_stripped = value.strip()
        if (value_stripped.startswith('{') or value_stripped.startswith('[')) and not CliParameterParser._is_complete_json(value_stripped):
            # Try to reconstruct JSON by collecting more arguments
            json_parts = [value]
            j = i + 1
            while j < len(unknown_args):
                next_arg = unknown_args[j]
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
        """Check if a string looks like complete JSON by checking bracket/brace balance."""
        if not value:
            return False
        value = value.strip()
        if not (value.startswith('{') or value.startswith('[')):
            return False
        # Simple balance check
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
    def _looks_like_exclude_pattern(arg: str) -> bool:
        if not arg:
            return False
        if arg.startswith('--'):
            return False
        if '/' in arg or '\\' in arg:
            return False
        if '.' in arg and any((arg.endswith(ext) for ext in ('.py', '.md', '.json', '.txt', '.yaml', '.yml'))):
            return False
        return True

    @staticmethod
    def _parse_action_parameters(unknown_args: list) -> Dict[str, str]:
        params = {}
        i = 0
        has_src_path = False
        while i < len(unknown_args):
            arg = unknown_args[i]
            if not arg:
                i += 1
                continue
            i, has_src_path = CliParameterParser._process_argument(arg, unknown_args, i, params, has_src_path)
        return params

    @staticmethod
    def _process_argument(arg: str, unknown_args: list, i: int, params: Dict, has_src_path: bool) -> tuple:
        if '=' in arg:
            consumed = CliParameterParser._parse_key_value_arg(arg, unknown_args, i, params)
            return (i + consumed, has_src_path)
        if arg.startswith('--'):
            return (i + 1, has_src_path)
        if arg.lower() == 'exclude':
            return CliParameterParser._process_exclude_argument(unknown_args, i, params)
        if CliParameterParser._looks_like_file_path(arg):
            CliParameterParser._parse_file_path_arg(arg, params)
            return (i + 1, True)
        if has_src_path and CliParameterParser._looks_like_exclude_pattern(arg):
            CliParameterParser._add_exclude_pattern(arg, params)
            return (i + 1, has_src_path)
        CliParameterParser._parse_context_arg(arg, params)
        return (i + 1, has_src_path)

    @staticmethod
    def _process_exclude_argument(unknown_args: list, i: int, params: Dict) -> tuple:
        exclude_patterns = []
        i += 1
        while i < len(unknown_args):
            next_arg = unknown_args[i]
            if next_arg.startswith('--') or CliParameterParser._looks_like_file_path(next_arg):
                break
            exclude_patterns.append(next_arg)
            i += 1
        if exclude_patterns:
            CliParameterParser._merge_exclude_patterns(exclude_patterns, params)
        return (i, False)

    @staticmethod
    def _merge_exclude_patterns(exclude_patterns: list, params: Dict):
        if 'exclude' not in params:
            params['exclude'] = exclude_patterns
        else:
            existing = params['exclude']
            if isinstance(existing, list):
                existing.extend(exclude_patterns)
            else:
                params['exclude'] = [existing] + exclude_patterns

    @staticmethod
    def _add_exclude_pattern(arg: str, params: Dict):
        if 'exclude' not in params:
            params['exclude'] = [arg]
        else:
            existing = params['exclude']
            if isinstance(existing, list):
                existing.append(arg)
            else:
                params['exclude'] = [existing, arg]

    @staticmethod
    def _parse_json_parameters(params: Dict[str, Any]) -> Dict[str, Any]:
        """Parse JSON strings in parameters. If a parameter value is a string that looks like JSON, parse it."""
        parsed_params = {}
        for key, value in params.items():
            if isinstance(value, str):
                value = value.strip()
                # Check if it looks like JSON (starts with { or [)
                if value.startswith('{') or value.startswith('['):
                    try:
                        parsed_params[key] = json.loads(value)
                    except (json.JSONDecodeError, ValueError):
                        # Try to fix common issues (unquoted keys/values from PowerShell)
                        fixed_value = CliParameterParser._try_fix_json(value)
                        if fixed_value != value:
                            try:
                                parsed_params[key] = json.loads(fixed_value)
                            except (json.JSONDecodeError, ValueError):
                                # If still can't parse, keep as string
                                parsed_params[key] = value
                        else:
                            # If fixing didn't change it, keep as string
                            parsed_params[key] = value
                else:
                    parsed_params[key] = value
            else:
                parsed_params[key] = value
        return parsed_params

    @staticmethod
    def _try_fix_json(value: str) -> str:
        """Try to fix common JSON issues like unquoted keys/values and Python dict syntax."""
        # Convert Python dict syntax to JSON (single quotes to double quotes)
        # This handles: {'key': 'value'} -> {"key": "value"}
        # For most Python dict strings, this is sufficient
        return value.replace("'", '"')