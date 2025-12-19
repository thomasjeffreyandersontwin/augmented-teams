import sys
import json
import logging
from typing import Dict, Any
import argparse
logger = logging.getLogger(__name__)

class CliExecutor:

    def __init__(self, cli_instance):
        self.cli = cli_instance

    def execute_and_output(self, args: argparse.Namespace, params: Dict[str, str]):
        params = self._resolve_paths(params)
        self._log_execution_info(args, params)
        try:
            result = self._execute_command(args, params)
            self._output_result(result)
            return result
        except Exception as e:
            self.cli._handle_error(e)

    def _resolve_paths(self, params: Dict[str, str]) -> Dict[str, str]:
        if self.cli.bot and self.cli.bot.bot_paths:
            return self.cli.bot.bot_paths.resolve_path_parameters(params)
        return params

    def _log_execution_info(self, args: argparse.Namespace, params: Dict[str, str]):
        logger.info(f'Executing: behavior={args.behavior}, action={args.action}')
        logger.info(f'Parameters: {params}')
        if 'src' in params:
            logger.info(f"  src paths: {params['src']}")

    def _execute_command(self, args: argparse.Namespace, params: Dict[str, str]):
        if args.close:
            logger.info('Closing current action...')
            return self.cli.close_current_action()
        action_name = args.action
        logger.info(f'Running action: {action_name} in behavior: {args.behavior}')
        result = self.cli.run(behavior_name=args.behavior, action_name=action_name, **params)
        logger.info('Action execution completed')
        return result

    def _output_result(self, result: Dict[str, Any]):
        self._print_instructions(result)
        result_json = json.dumps(result, indent=2)
        print(result_json)
        sys.stdout.flush()

    def _print_instructions(self, result: Dict[str, Any]):
        data = result.get('data', {})
        instructions = data.get('instructions', {})
        if isinstance(instructions, dict):
            base_instructions = instructions.get('base_instructions', [])
        elif isinstance(instructions, list):
            base_instructions = instructions
        else:
            base_instructions = []
        if isinstance(base_instructions, list) and len(base_instructions) > 0:
            for instruction in base_instructions:
                try:
                    print(instruction)
                except UnicodeEncodeError:
                    safe_instruction = instruction.encode('ascii', errors='replace').decode('ascii')
                    print(safe_instruction)
            sys.stdout.flush()