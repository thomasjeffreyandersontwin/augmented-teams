from pathlib import Path
import json
from typing import Dict, Any
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.cli.cli_code_visitor import CliCodeVisitor
from agile_bot.bots.base_bot.src.generator.orchestrator import Orchestrator
from agile_bot.bots.base_bot.src.bot.bot import Bot

class CliGenerator:

    def __init__(self, workspace_root: Path, bot_location: str=None):
        self.workspace_root = Path(workspace_root)
        self.bot_location = Path(bot_location or 'agile_bot/bots/base_bot')
        self.bot_name = self.bot_location.name
        self.config_path = self.workspace_root / self.bot_location / 'bot_config.json'

    def generate_cli_code(self) -> Dict[str, Any]:
        """Generate CLI scripts (Python, shell, PowerShell). Does not generate Cursor commands."""
        self._validate_config()
        bot = self._create_bot()
        self._generate_cli_scripts(bot)
        
        bot_directory = self.workspace_root / self.bot_location
        cli_python_path = bot_directory / 'src' / f'{self.bot_name}_cli.py'
        cli_script_path = bot_directory / f'{self.bot_name}_cli'
        cli_powershell_path = bot_directory / f'{self.bot_name}_cli.ps1'
        
        return {
            'cli_python': cli_python_path,
            'cli_script': cli_script_path,
            'cli_powershell': cli_powershell_path
        }

    def _validate_config(self) -> None:
        if not self.config_path.exists():
            raise FileNotFoundError(f'Bot Config not found at {self.config_path}')
        try:
            read_json_file(self.config_path)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f'Malformed Bot Config at {self.config_path}: {e.msg}', e.doc, e.pos)

    def _create_bot(self) -> Bot:
        bot_directory = self.workspace_root / self.bot_location
        return Bot(bot_name=self.bot_name, bot_directory=bot_directory, config_path=self.config_path)

    def _generate_cli_scripts(self, bot: Bot) -> None:
        code_visitor = CliCodeVisitor(
            workspace_root=self.workspace_root,
            bot_location=self.bot_location,
            bot=bot
        )
        orchestrator = Orchestrator(code_visitor)
        orchestrator.generate()