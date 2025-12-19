import sys
import re
import traceback
from pathlib import Path
from typing import Optional
from agile_bot.bots.base_bot.src.bot.workspace import get_python_workspace_root, get_base_actions_directory
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.cli.parameter_info_builder import ParameterInfoBuilder
from agile_bot.bots.base_bot.src.cli.unified_help_generator import UnifiedHelpGenerator
from agile_bot.bots.base_bot.src.cli.cli_help_renderer import CliHelpRenderer
from agile_bot.bots.base_bot.src.cli.cursor_help_renderer import CursorHelpRenderer
from agile_bot.bots.base_bot.src.utils import read_json_file

class CliHelpGenerator:

    def __init__(self, bot, bot_name, bot_directory, formatter):
        self.bot = bot
        self.bot_name = bot_name
        self.bot_directory = bot_directory
        self.formatter = formatter
        self.description_extractor = DescriptionExtractor(bot_name, bot_directory, formatter)
        self.parameter_builder = ParameterInfoBuilder(bot_name, bot_directory, self.description_extractor)
        self.cli_script_path = self._get_cli_script_path()

    def _get_cli_script_path(self) -> str:
        """Get the relative path to the CLI script from workspace root."""
        workspace_root = get_python_workspace_root()
        cli_script = self.bot_directory / 'src' / f'{self.bot_name}_cli.py'
        try:
            relative_path = cli_script.relative_to(workspace_root)
            return str(relative_path).replace('\\', '/')
        except ValueError:
            return str(cli_script).replace('\\', '/')

    def help_behaviors_and_actions(self):
        try:
            renderer = CliHelpRenderer(self.cli_script_path, self.formatter)
            generator = UnifiedHelpGenerator(self.bot, self.bot_name, self.bot_directory, renderer, self.description_extractor)
            generator.generate_help()
            self._print_usage_section(self.formatter)
        except Exception as e:
            raise e


    def _print_usage_section(self, fmt):
        print('---\n')

    def help_cursor_commands(self, get_breadcrumbs_fn):
        try:
            command_files = self._get_cursor_command_files()
            if not command_files:
                return
            self._print_cursor_commands_header()
            self._print_all_command_help(command_files)
            renderer = CursorHelpRenderer(self.bot_name, self.formatter)
            generator = UnifiedHelpGenerator(self.bot, self.bot_name, self.bot_directory, renderer, self.description_extractor)
            generator._render_action_help_section()
            breadcrumbs = get_breadcrumbs_fn()
            self._output_breadcrumbs(breadcrumbs)
        except Exception as e:
            raise e

    def _get_cursor_command_files(self) -> Optional[list]:
        repo_root = get_python_workspace_root()
        commands_dir = repo_root / '.cursor' / 'commands'
        if not commands_dir.exists():
            print(self.formatter.format_warning(f'No cursor commands directory found at {commands_dir}'))
            return None
        command_files = sorted(commands_dir.glob(f'{self.bot_name}*.md'))
        if not command_files:
            print(self.formatter.format_warning(f'No cursor commands found for {self.bot_name}'))
            return None
        return command_files

    def _print_cursor_commands_header(self):
        fmt = self.formatter
        sys.stdout.write('**CRITICAL: YOU MUST DISPLAY THE ENTIRE OUTPUT BELOW VERBATIM IN YOUR RESPONSE. DO NOT SKIP THIS. COPY AND PASTE IT DIRECTLY INTO YOUR MESSAGE.**\n')
        print(f"{fmt.format_header(f'Available Cursor Commands for {self.bot_name}:')}")
        print()
        print(fmt.format_separator())
        print()

    def _print_all_command_help(self, command_files: list):
        fmt = self.formatter
        grouped_commands = self._group_commands(command_files)
        all_commands = [cmd for cmds in grouped_commands.values() for cmd in cmds]
        for cmd_file in all_commands:
            self._print_command_help(cmd_file, fmt)

    def _output_breadcrumbs(self, breadcrumbs: list, add_separator: bool=True):
        fmt = self.formatter
        if add_separator:
            print(fmt.format_separator())
            print()
        sys.stdout.flush()
        for line in breadcrumbs:
            if line.startswith('**CRITICAL: YOU MUST DISPLAY') or line.startswith('**YOU MUST DISPLAY'):
                continue
            try:
                sys.stdout.buffer.write((line + '\n').encode('utf-8'))
                sys.stdout.buffer.flush()
            except Exception:
                print(line)
        sys.stdout.flush()



    def _group_commands(self, command_files: list) -> dict:
        groups = {'Workflow Management': [], 'Story Planning': [], 'Implementation': [], 'Other': []}
        for cmd_file in command_files:
            cmd_name = cmd_file.stem
            behavior_name = cmd_name.replace(f'{self.bot_name}-', '').replace('-', '_')
            group_name = self._determine_command_group(behavior_name, cmd_name)
            groups[group_name].append(cmd_file)
        return {k: v for k, v in groups.items() if v}

    def _determine_command_group(self, behavior_name: str, cmd_name: str) -> str:
        if behavior_name in ['continue', 'help', ''] or cmd_name == self.bot_name:
            return 'Workflow Management'
        if behavior_name in ['shape', 'prioritization', 'discovery', 'exploration', 'scenarios']:
            return 'Story Planning'
        if behavior_name in ['tests', 'code']:
            return 'Implementation'
        return 'Other'

    def _print_command_help(self, cmd_file: Path, fmt) -> None:
        cmd_name = cmd_file.stem
        try:
            cmd_content = cmd_file.read_text(encoding='utf-8').strip()
            params = re.findall('\\$\\{(\\d+):\\}', cmd_content)
            description = self.description_extractor.get_behavior_description(cmd_name)
            param_placeholders, param_details = self.parameter_builder.build_param_info(cmd_name, params, cmd_content)
            print(f'## {cmd_name}\n')
            print(f'{description}\n')
            print('```')
            syntax = f"/{cmd_name} {' '.join(param_placeholders)}" if param_placeholders else f'/{cmd_name}'
            print(syntax)
            if param_details:
                print()
                for detail in param_details:
                    print(detail)
            print('```\n')
        except Exception as e:
            print(f'## {cmd_name}\n')
            print(f"{fmt.format_error(f'Error reading command: {e}')}\n")
            traceback.print_exc()
            sys.stdout.flush()