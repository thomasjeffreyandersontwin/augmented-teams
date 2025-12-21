from pathlib import Path
import json
from typing import Dict, Any
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.cli.cli_script_generator import CliScriptGenerator
from agile_bot.bots.base_bot.src.cli.cursor_command_generator import CursorCommandGenerator

class CliGenerator:

    def __init__(self, workspace_root: Path, bot_location: str=None):
        self.workspace_root = Path(workspace_root)
        self.bot_location = Path(bot_location or 'agile_bot/bots/base_bot')
        self.bot_name = self.bot_location.name
        self.config_path = self.workspace_root / self.bot_location / 'bot_config.json'
        self._script_generator = CliScriptGenerator(self.workspace_root, self.bot_location, self.bot_name)
        self._command_generator = CursorCommandGenerator(self.workspace_root, self.bot_location, self.bot_name)

    def generate_cli_code(self) -> Dict[str, Any]:
        if not self.config_path.exists():
            raise FileNotFoundError(f'Bot Config not found at {self.config_path}')
        try:
            bot_config = read_json_file(self.config_path)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f'Malformed Bot Config at {self.config_path}: {e.msg}', e.doc, e.pos)
        cli_python_path = self._script_generator.generate_python_cli_script()
        cli_script_path = self._script_generator.generate_shell_script()
        cli_powershell_path = self._script_generator.generate_powershell_script()
        behaviors = self._get_behaviors_from_config()
        cursor_commands = self._command_generator.generate_cursor_commands(cli_python_path, behaviors)
        registry_path = self._command_generator.update_bot_registry(cli_python_path)
        return {'cli_python': cli_python_path, 'cli_script': cli_script_path, 'cli_powershell': cli_powershell_path, 'cursor_commands': cursor_commands, 'registry': registry_path}

    def _get_behaviors_from_config(self) -> list:
        return self._discover_behaviors_from_folders()

    def _discover_behaviors_from_folders(self) -> list:
        behaviors_dir = self.workspace_root / self.bot_location / 'behaviors'
        if not behaviors_dir.exists():
            return []
        behaviors = []
        for item in sorted(behaviors_dir.iterdir()):
            if item.is_dir() and (not item.name.startswith('_')) and (not item.name.startswith('.')):
                if (item / 'behavior.json').exists():
                    behaviors.append(item.name)
        return behaviors