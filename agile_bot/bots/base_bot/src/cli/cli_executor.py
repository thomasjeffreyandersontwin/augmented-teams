import sys
import json
import logging
from pathlib import Path
from typing import Dict, Any, List
import argparse

from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
from agile_bot.bots.base_bot.src.repl_cli.headless.headless_config import HeadlessConfig
from agile_bot.bots.base_bot.src.repl_cli.headless.non_recoverable_error import NonRecoverableError

logger = logging.getLogger(__name__)


class CliExecutor:

    def __init__(self, cli_instance):
        self.cli = cli_instance

    def execute_and_output(self, args: argparse.Namespace, cli_args: List[str]):
        self._log_execution_info(args, cli_args)
        try:
            if getattr(args, 'headless', False):
                result = self._execute_headless(args)
            else:
                result = self._execute_command(args, cli_args)
            self._output_result(result)
            return result
        except Exception as e:
            self.cli._handle_error(e)

    def _log_execution_info(self, args: argparse.Namespace, cli_args: List[str]):
        logger.info(f'Executing: behavior={args.behavior}, action={args.action}')
        logger.info(f'CLI args: {cli_args}')
        if getattr(args, 'headless', False):
            logger.info('Headless mode enabled')

    def _execute_headless(self, args: argparse.Namespace) -> Dict[str, Any]:
        workspace_dir = self.cli.bot.bot_paths.workspace_directory
        
        config = HeadlessConfig.load()
        if not config.is_configured:
            raise NonRecoverableError(
                'Headless mode requires API key. Set CURSOR_API_KEY env var or add key to agile_bot/secrets/cursor_api_key.txt'
            )
        
        session = HeadlessSession(workspace_directory=workspace_dir, config=config)
        
        context_file = None
        context_file_path = getattr(args, 'context_file', None)
        if context_file_path:
            context_file = Path(context_file_path)
        else:
            default_context = workspace_dir / 'headless-context.md'
            if default_context.exists():
                context_file = default_context
        
        message = getattr(args, 'message', None)
        behavior = getattr(args, 'behavior', None)
        action = getattr(args, 'action', None)
        
        if message:
            result = session.invokes(message=message, context_file=context_file)
        elif behavior and action:
            result = session.invokes_action(
                behavior=behavior,
                action=action,
                context_file=context_file
            )
        elif behavior:
            result = session.invokes_behavior(
                behavior=behavior,
                context_file=context_file
            )
        else:
            raise NonRecoverableError(
                'Headless mode requires --message, --behavior, or --behavior and --action'
            )
        
        return self._format_headless_result(result)
    
    def _format_headless_result(self, result) -> Dict[str, Any]:
        return {
            'status': result.status,
            'completed': result.completed,
            'log_path': str(result.log_path) if result.log_path else None,
            'session_id': result.session_id,
            'loop_count': result.loop_count,
            'message': result.message,
            'blocked': result.blocked,
            'block_reason': result.block_reason,
            'exit_code': result.exit_code,
            'behavior': result.behavior,
            'action': result.action,
            'operation': result.operation,
            'action_completed': result.action_completed,
            'behavior_completed': result.behavior_completed,
            'operations_executed': result.operations_executed,
            'actions_executed': result.actions_executed,
        }

    def _execute_command(self, args: argparse.Namespace, cli_args: List[str]):
        if args.close:
            logger.info('Closing current action...')
            return self.cli.close_current_action()
        action_name = args.action
        if action_name in ('get_working_dir', 'set_working_dir'):
            return self._handle_working_dir_command(action_name, cli_args)
        logger.info(f'Running action: {action_name} in behavior: {args.behavior}')
        result = self.cli.run(behavior_name=args.behavior, action_name=action_name, cli_args=cli_args)
        logger.info('Action execution completed')
        return result

    def _handle_working_dir_command(self, action_name: str, cli_args: List[str]) -> Dict[str, Any]:
        if action_name == 'get_working_dir':
            working_dir = self.cli.bot.bot_paths.workspace_directory
            return {'working_dir': str(working_dir), 'message': f'Working directory from WORKING_AREA: {working_dir}'}
        new_path = None
        for arg in cli_args:
            if arg.startswith('--working-dir='):
                new_path = arg.split('=', 1)[1]
                break
            if arg.startswith('--path='):
                new_path = arg.split('=', 1)[1]
                break
        if not new_path and cli_args and not cli_args[0].startswith('--'):
            new_path = cli_args[0]
        if not new_path:
            raise ValueError('set_working_dir requires a path parameter (e.g., --path=/path/to/project)')
        updated = self.cli.bot.bot_paths.update_workspace_directory(new_path)
        return {'working_dir': str(updated), 'message': f'Working directory updated to {updated}'}

    def _output_result(self, result: Dict[str, Any]):
        result_json = json.dumps(result, indent=2)
        print(result_json)
        sys.stdout.flush()
