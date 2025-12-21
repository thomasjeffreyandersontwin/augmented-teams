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
from agile_bot.bots.base_bot.src.actions.instructions import Instructions

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
            help_inst = self._build_help_instructions(command_files)
            help_file = help_inst.write_display_to_file('help.md')
            status_file = self._write_breadcrumbs_to_file(get_breadcrumbs_fn)
            print(f'Read and display the contents of `{help_file}`')
            print()
            print(f'Read and display the contents of `{status_file}`')
            sys.stdout.flush()
        except Exception as e:
            raise e

    def _build_help_instructions(self, command_files: list) -> Instructions:
        help_inst = Instructions(bot_paths=self.bot.bot_paths)
        help_inst.add_display(f"## Available Cursor Commands for {self.bot_name}:")
        help_inst.add_display('')
        help_inst.add_display('---')
        help_inst.add_display('')
        self._add_all_command_help_to_display(command_files, help_inst)
        help_inst.add_display('---')
        help_inst.add_display('')
        help_inst.add_display('## Action Help')
        help_inst.add_display('')
        self._add_action_help_to_display(help_inst)
        return help_inst

    def _write_breadcrumbs_to_file(self, get_breadcrumbs_fn) -> Path:
        breadcrumbs = get_breadcrumbs_fn()
        status_inst = Instructions(bot_paths=self.bot.bot_paths)
        filtered_breadcrumbs = [
            line for line in breadcrumbs 
            if not line.startswith('**CRITICAL: YOU MUST DISPLAY') and not line.startswith('**YOU MUST DISPLAY')
        ]
        for line in filtered_breadcrumbs:
            status_inst.add_display(line)
        return status_inst.write_display_to_file('status.md')

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

    def _add_all_command_help_to_display(self, command_files: list, inst: Instructions):
        sorted_commands = self._sort_commands_by_behavior_order(command_files)
        for cmd_file in sorted_commands:
            self._add_command_help_to_display(cmd_file, inst)
    
    def _sort_commands_by_behavior_order(self, command_files: list) -> list:
        def get_command_order(cmd_file: Path) -> tuple:
            cmd_name = cmd_file.stem
            behavior_name = cmd_name.replace(f'{self.bot_name}-', '').replace('-', '_')
            if behavior_name in ['', 'continue', 'help', 'get_working_dir', 'set_working_dir'] or cmd_name == self.bot_name:
                return (0, cmd_name)
            order = self._get_behavior_order_from_config(behavior_name)
            return (1, order, cmd_name)
        return sorted(command_files, key=get_command_order)
    
    def _get_behavior_order_from_config(self, behavior_name: str) -> int:
        behavior_json_path = self.bot_directory / 'behaviors' / behavior_name / 'behavior.json'
        if not behavior_json_path.exists():
            return 999
        try:
            config = read_json_file(behavior_json_path)
            return config.get('order', 999)
        except Exception:
            return 999
    
    def _add_command_help_to_display(self, cmd_file: Path, inst: Instructions):
        cmd_name = cmd_file.stem
        try:
            cmd_content = cmd_file.read_text(encoding='utf-8').strip()
            params = re.findall('\\$\\{(\\d+):\\}', cmd_content)
            description = self.description_extractor.get_behavior_description(cmd_name)
            param_placeholders, param_details = self.parameter_builder.build_param_info(cmd_name, params, cmd_content)
            inst.add_display(f'## {cmd_name}')
            inst.add_display('')
            inst.add_display(description)
            inst.add_display('')
            inst.add_display('```')
            syntax = f"/{cmd_name} {' '.join(param_placeholders)}" if param_placeholders else f'/{cmd_name}'
            inst.add_display(syntax)
            if param_details:
                inst.add_display('')
                for detail in param_details:
                    inst.add_display(detail)
            inst.add_display('```')
            inst.add_display('')
        except Exception as e:
            inst.add_display(f'## {cmd_name}')
            inst.add_display('')
            inst.add_display(f'[ERROR] Error reading command: {e}')
            inst.add_display('')
    
    def _add_action_help_to_display(self, inst: Instructions):
        renderer = CursorHelpRenderer(self.bot_name, self.formatter)
        generator = UnifiedHelpGenerator(self.bot, self.bot_name, self.bot_directory, renderer, self.description_extractor)
        import io
        old_stdout = sys.stdout
        sys.stdout = captured_output = io.StringIO()
        try:
            generator._render_action_help_section()
            action_help_text = captured_output.getvalue()
            for line in action_help_text.splitlines():
                inst.add_display(line)
        finally:
            sys.stdout = old_stdout

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
