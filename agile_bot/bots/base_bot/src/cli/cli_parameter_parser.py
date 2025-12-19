import argparse
from pathlib import Path
from typing import Dict, Tuple

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
        parser.add_argument('context', nargs='*', help='Additional context (file paths, parameters, etc.)')
        return parser

    @staticmethod
    def _handle_file_like_action(args: argparse.Namespace, unknown: list) -> list:
        if args.action and CliParameterParser._looks_like_file_path(args.action):
            unknown.append(args.action)
            args.action = None
        return unknown

    @staticmethod
    def _build_params_from_args(args: argparse.Namespace, unknown: list) -> Dict[str, str]:
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
    def _parse_key_value_arg(arg: str, params: Dict) -> None:
        key, value = arg.split('=', 1)
        key = key.lstrip('--')
        if key in ['test', 'src'] and ',' in value:
            params[key] = [f.strip() for f in value.split(',')]
        else:
            params[key] = value

    @staticmethod
    def _parse_file_list_arg(unknown_args: list, start_idx: int, key: str, params: Dict) -> int:
        file_list = []
        i = start_idx
        while i < len(unknown_args):
            next_arg = unknown_args[i]
            if not CliParameterParser._looks_like_file_path(next_arg) and (not CliParameterParser._looks_like_directory_path(next_arg)):
                break
            file_list.append(next_arg.lstrip('@'))
            i += 1
        if file_list:
            params[key] = file_list if len(file_list) > 1 else file_list[0]
        return i

    @staticmethod
    def _parse_file_path_arg(arg: str, params: Dict) -> None:
        file_path = arg.lstrip('@')
        if CliParameterParser._looks_like_directory_path(arg):
            CliParameterParser._append_to_param(params, 'src', file_path)
            return
        if file_path.endswith('.py'):
            file_name = Path(file_path).name
            is_test_file = file_name.startswith('test_') or file_name.endswith('_test.py')
            target_key = 'test' if is_test_file else 'src'
            CliParameterParser._append_to_param(params, target_key, file_path)
            return
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
            CliParameterParser._parse_key_value_arg(arg, params)
            return (i + 1, has_src_path)
        if arg in ['--test', '--src']:
            key = arg.lstrip('--')
            new_i = CliParameterParser._parse_file_list_arg(unknown_args, i + 1, key, params)
            return (new_i, has_src_path or key == 'src')
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