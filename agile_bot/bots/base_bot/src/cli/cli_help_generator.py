import sys
from pathlib import Path
from agile_bot.bots.base_bot.src.bot.workspace import get_python_workspace_root
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.cli.parameter_info_builder import ParameterInfoBuilder
from agile_bot.bots.base_bot.src.generator.orchestrator import Orchestrator
from agile_bot.bots.base_bot.src.cli.cli_help_renderer_visitor import CliHelpRendererVisitor
from agile_bot.bots.base_bot.src.cli.cursor.help_renderer_visitor import CursorHelpRendererVisitor
from agile_bot.bots.base_bot.src.actions.instructions import Instructions

class CliHelpGenerator:

    def __init__(self, bot, bot_name, bot_directory, formatter):
        self.bot = bot
        self.bot_name = bot_name
        self.bot_directory = bot_directory
        self.formatter = formatter
        description_extractor = DescriptionExtractor(bot_name, bot_directory, formatter)
        self.parameter_builder = ParameterInfoBuilder(bot_name, bot_directory, description_extractor)
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
            renderer = CliHelpRendererVisitor(
                self.cli_script_path,
                bot=self.bot
            )
            generator = Orchestrator(renderer)
            generator.generate()
            formatter = renderer.formatter if hasattr(renderer, 'formatter') else None
            self._print_usage_section(formatter)
        except Exception as e:
            raise e

    def _print_usage_section(self, fmt):
        print('---\n')

    def help_cursor_commands(self, get_breadcrumbs_fn):
        try:
            help_inst = self._build_help_instructions()
            help_file = help_inst.write_display_to_file('help.md')
            status_file = self._write_breadcrumbs_to_file(get_breadcrumbs_fn)
            print(f'Read and display the contents of `{help_file}`')
            print()
            print(f'Read and display the contents of `{status_file}`')
            sys.stdout.flush()
        except Exception as e:
            raise e

    def _build_help_instructions(self) -> Instructions:
        help_inst = Instructions(bot_paths=self.bot.bot_paths)
        visitor = CursorHelpRendererVisitor(
            bot=self.bot,
            instructions=help_inst
        )
        orchestrator = Orchestrator(visitor)
        orchestrator.generate()
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
