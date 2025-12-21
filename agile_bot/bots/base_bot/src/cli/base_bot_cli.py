import sys
import argparse
import json
import logging
import re
import traceback
from pathlib import Path
from typing import Dict, Any, Tuple, Optional, TYPE_CHECKING
from agile_bot.bots.base_bot.src.bot.bot import Bot, BotResult
from agile_bot.bots.base_bot.src.bot.workspace import get_base_actions_directory, get_bot_directory, get_python_workspace_root
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.cli.cli_command_router import CliCommandRouter
from agile_bot.bots.base_bot.src.cli.cli_help_generator import CliHelpGenerator
from agile_bot.bots.base_bot.src.cli.cli_parameter_parser import CliParameterParser
from agile_bot.bots.base_bot.src.cli.cli_executor import CliExecutor
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior
    from agile_bot.bots.base_bot.src.actions.action import Action
logger = logging.getLogger(__name__)

class CliTerminalFormatter:

    def _format_header_style(self, text: str) -> str:
        return f'## {text}'

    def _format_bold_style(self, text: str) -> str:
        return f'**{text}**'

    def _format_identity(self, text: str) -> str:
        return text

    def format_directive(self, text: str) -> str:
        return self.format_header(text)

    def format_header(self, text: str) -> str:
        return self._format_header_style(text)

    def format_workflow_status_header(self, text: str) -> str:
        return self.format_header(text)

    def format_command(self, text: str) -> str:
        return self._format_bold_style(text)

    def format_label(self, text: str) -> str:
        return self.format_command(text)

    def format_workflow_directory(self, text: str) -> str:
        return self.format_command(text)

    def format_workflow_current_state(self, text: str) -> str:
        return self.format_command(text)

    def format_workflow_next_step(self, text: str) -> str:
        return self.format_command(text)

    def format_workflow_current_marker(self, text: str) -> str:
        return self.format_command(text)

    def format_workflow_active_marker(self, text: str) -> str:
        return self.format_command(text)

    def format_workflow_completed(self, text: str) -> str:
        return self._format_identity(text)

    def format_workflow_pending(self, text: str) -> str:
        return self.format_workflow_completed(text)

    def format_parameter(self, text: str) -> str:
        return f'`{text}`'

    def format_error(self, text: str) -> str:
        return f'[ERROR] **{text}**'

    def format_warning(self, text: str) -> str:
        return f'[WARNING] **{text}**'

    def format_success(self, text: str) -> str:
        return f'[OK] **{text}**'

    def format_info(self, text: str) -> str:
        return f'[INFO] **{text}**'

    def format_separator(self, char: str='=', length: int=70) -> str:
        return '---'

    def format_thin_separator(self) -> str:
        return '------'

class BaseBotCli:

    def __init__(self, bot: Bot=None, bot_name: str=None, bot_config_path: Path=None):
        if bot:
            self.bot = bot
            self.bot_name = bot.name
            self.bot_directory = bot.bot_paths.bot_directory
        elif bot_name and bot_config_path:
            self.bot_name = bot_name
            self.bot_config_path = bot_config_path
            self.bot_directory = get_bot_directory()
            self.bot = self._create_bot_instance()
        else:
            raise ValueError('Must provide either bot instance or (bot_name and bot_config_path)')
        self.formatter = CliTerminalFormatter()
        self.router = CliCommandRouter(self.bot, self.formatter)
        self.help_generator = CliHelpGenerator(self.bot, self.bot_name, self.bot_directory, self.formatter)
        self.executor = CliExecutor(self)

    def _create_bot_instance(self) -> Bot:
        return Bot(bot_name=self.bot_name, bot_directory=self.bot_directory, config_path=self.bot_config_path)

    def run(self, behavior_name: str=None, action_name: str=None, cli_args: list=None) -> Dict[str, Any]:
        """Run an action with typed context parsing.
        
        Args:
            behavior_name: Name of behavior to run
            action_name: Name of action to run  
            cli_args: Remaining CLI arguments for action-specific parameter parsing
        """
        try:
            result = self.router.route_to_action(behavior_name, action_name, cli_args or [])
            return result
        except Exception as e:
            self._handle_error(e)

    def close_current_action(self) -> Dict[str, Any]:
        try:
            current_behavior = self.router._navigate_to_first_behavior_if_needed()
            current_behavior.actions.load_state()
            current_action = current_behavior.actions.current
            if current_action:
                current_behavior.actions.close_current()
            return self.router._execute_current_action(current_behavior)
        except Exception as e:
            self._handle_error(e)

    def list_behaviors(self):
        try:
            fmt = self.formatter
            print(fmt.format_header(f'Available behaviors for {self.bot_name}:'))
            for behavior in self.bot.behaviors:
                print(f"  {fmt.format_command(f'- {behavior.name}')}")
            sys.stdout.flush()
        except Exception as e:
            self._handle_error(e)

    def list_actions(self, behavior_name: str):
        try:
            fmt = self.formatter
            behavior_obj = self.bot.behaviors.find_by_name(behavior_name)
            if not behavior_obj:
                raise ValueError(f"Behavior '{behavior_name}' not found")
            actions = self.help_generator._get_behavior_actions(behavior_obj)
            print(fmt.format_header(f'Available actions for {behavior_name}:'))
            for action in actions:
                print(f"  {fmt.format_command(f'- {action}')}")
            sys.stdout.flush()
        except Exception as e:
            self._handle_error(e)

    def help_behaviors_and_actions(self):
        try:
            self.help_generator.help_behaviors_and_actions()
            breadcrumbs = self._get_breadcrumbs_from_action()
            if breadcrumbs:
                print()
                self.help_generator._output_breadcrumbs(breadcrumbs)
        except Exception as e:
            self._handle_error(e)

    def help_cursor_commands(self):
        """Route help to the help action."""
        try:
            # Create help action directly (doesn't need a behavior workflow)
            from agile_bot.bots.base_bot.src.actions.help_action import HelpAction
            from agile_bot.bots.base_bot.src.utils import read_json_file
            from agile_bot.bots.base_bot.src.bot.workspace import get_base_actions_directory
            
            # Load help action config from base_actions
            base_actions_dir = get_base_actions_directory()
            help_config_path = base_actions_dir / 'help' / 'action_config.json'
            help_config = read_json_file(help_config_path)
            
            # Create a minimal behavior wrapper for the help action
            # Help action needs access to bot_name and bot_paths
            class HelpBehaviorWrapper:
                def __init__(self, bot, bot_name, bot_paths):
                    self.bot = bot
                    self.bot_name = bot_name
                    self.name = 'help'
                    self.bot_paths = bot_paths
                    self.actions = None  # Help action doesn't participate in workflow
            
            behavior_wrapper = HelpBehaviorWrapper(self.bot, self.bot_name, self.bot.bot_paths)
            help_action = HelpAction(behavior_wrapper, help_config, 'help')
            
            # Execute the help action with empty context
            result = help_action.execute()
            
            # Output the result
            self.executor._output_result(result)
            return result
        except Exception as e:
            self._handle_error(e)

    @staticmethod
    def parse_arguments(description: str='Bot CLI', custom_help_handler=None) -> Tuple[argparse.Namespace, Dict[str, str]]:
        return CliParameterParser.parse_arguments(description)

    def main(self):
        self._configure_logging()
        logger.info(f'=== CLI Starting === Bot: {self.bot_name}')
        try:
            args, cli_args = BaseBotCli.parse_arguments(description=f'{self.bot_name} CLI')
        except Exception as e:
            self._handle_error(e)
            sys.exit(1)
        try:
            return self._dispatch_command(args, cli_args)
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            self._print_main_error(e)
            sys.exit(1)

    def _configure_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler(sys.stdout)], force=True)

    def _dispatch_command(self, args, cli_args):
        if args.help:
            self.help_behaviors_and_actions()
            return None
        if args.help_cursor:
            self.help_cursor_commands()
            return None
        if args.list:
            self._handle_list_command(args.behavior)
            return None
        return self.executor.execute_and_output(args, cli_args)

    def _print_main_error(self, e: Exception):
        error_lines = ['\n---', '**ERROR OCCURRED IN MAIN**', '---', f'\n**Exception Type:** {type(e).__name__}', f'**Exception Message:** {str(e)}', '\n**Full Traceback:**', '-' * 70]
        for line in error_lines:
            print(line, file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        print('-' * 70 + '\n---\n', file=sys.stderr)
        for line in error_lines:
            print(line)
        traceback.print_exc()
        print('-' * 70 + '\n---\n')
        sys.stdout.flush()
        sys.stderr.flush()

    def _handle_list_command(self, behavior_name: str=None):
        try:
            if behavior_name:
                self.list_actions(behavior_name)
            else:
                self.list_behaviors()
        except Exception as e:
            self._handle_error(e)

    def _handle_error(self, error: Exception):
        print('\n' + '=' * 70)
        print('**ERROR OCCURRED**')
        print('=' * 70)
        print(f'\nException Type: {type(error).__name__}')
        print(f'Exception Message: {str(error)}')
        print('\nFull Traceback:')
        print('-' * 70)
        traceback.print_exc()
        print('-' * 70)
        print('=' * 70 + '\n')
        sys.stdout.flush()
        raise error

    def _infer_parameter_description(self, cmd_name: str, param_num: str, cmd_content: str) -> str:
        return self.help_generator.parameter_builder.infer_parameter_description(cmd_name, param_num, cmd_content)

    def _get_breadcrumbs_from_action(self) -> list:
        if not self.bot:
            return []
        try:
            current_behavior = self.bot.behaviors.current
            if not current_behavior:
                if self.bot.behaviors.first:
                    self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
                    current_behavior = self.bot.behaviors.current
                if not current_behavior:
                    return []
            current_behavior.actions.load_state()
            current_action = current_behavior.actions.current
            if not current_action:
                return []
            breadcrumbs = current_action.get_workflow_status_breadcrumbs()
            return breadcrumbs if breadcrumbs else []
        except Exception as e:
            logger.debug(f'Failed to get breadcrumbs from action: {e}')
            return []