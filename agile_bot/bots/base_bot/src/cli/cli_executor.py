import sys
import json
import logging
from pathlib import Path
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
        if action_name in ('get_working_dir', 'set_working_dir'):
            return self._handle_working_dir_command(action_name, params)
        logger.info(f'Running action: {action_name} in behavior: {args.behavior}')
        result = self.cli.run(behavior_name=args.behavior, action_name=action_name, **params)
        logger.info('Action execution completed')
        return result

    def _handle_working_dir_command(self, action_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if action_name == 'get_working_dir':
            working_dir = self.cli.bot.bot_paths.workspace_directory
            return {'working_dir': str(working_dir), 'message': f'Working directory from WORKING_AREA: {working_dir}'}
        new_path = params.get('working_dir') or params.get('working_path') or params.get('working_folder') or params.get('path') or params.get('dir') or params.get('folder')
        context_value = params.get('context')
        if not new_path and isinstance(context_value, list) and context_value:
            new_path = context_value[0]
        elif not new_path and isinstance(context_value, str):
            new_path = context_value
        if not new_path:
            raise ValueError('set_working_dir requires a path parameter (e.g., working_dir=/path/to/project)')
        updated = self.cli.bot.bot_paths.update_workspace_directory(new_path)
        return {'working_dir': str(updated), 'message': f'Working directory updated to {updated}'}

    def _output_result(self, result: Dict[str, Any]):
        # Extract and remove base_instructions from result before printing JSON
        data = result.get('data', {})
        instructions = data.get('instructions', {})
        base_instructions = []
        if isinstance(instructions, dict):
            base_instructions = instructions.pop('base_instructions', [])
        
        # Print the JSON result (without base_instructions to keep it smaller)
        result_json = json.dumps(result, indent=2)
        print(result_json)
        sys.stdout.flush()
        
        # Print base_instructions at the END so they're always visible
        if isinstance(base_instructions, list) and len(base_instructions) > 0:
            # Write instructions to log file in background (non-blocking)
            try:
                import threading
                def write_instructions_log():
                    try:
                        log_file = Path(self.cli.bot.bot_paths.workspace_directory) / 'docs' / 'stories' / 'build-instructions.txt'
                        log_file.parent.mkdir(parents=True, exist_ok=True)
                        with log_file.open('w', encoding='utf-8') as f:
                            f.write('\n'.join(base_instructions))
                    except Exception:
                        pass  # Don't block if log write fails
                threading.Thread(target=write_instructions_log, daemon=True).start()
            except Exception:
                pass  # Don't block if threading fails
            
            # Print instructions immediately so AI can execute them
            print()  # blank line separator
            for instruction in base_instructions:
                try:
                    print(instruction)
                except UnicodeEncodeError:
                    safe_instruction = instruction.encode('ascii', errors='replace').decode('ascii')
                    print(safe_instruction)
            sys.stdout.flush()
        # #region agent log
        Path(r'c:\dev\augmented-teams\.cursor\debug.log').open('a').write(json.dumps({'sessionId':'debug-session','runId':'initial','hypothesisId':'E','location':'cli_executor.py:87','message':'Output complete - NO FILE GENERATION CODE HERE','data':{'instructions_printed':len(base_instructions)},'timestamp':__import__('time').time()*1000})+'\n')
        # #endregion

    def _print_instructions(self, result: Dict[str, Any]):
        # Deprecated - now handled in _output_result
        pass