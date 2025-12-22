from pathlib import Path
from typing import Dict, Optional
from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.generator.orchestrator import Orchestrator
from agile_bot.bots.base_bot.src.cli.cursor_command_file_visitor import CursorCommandFileVisitor
import json
from agile_bot.bots.base_bot.src.utils import read_json_file

class CursorCommandGenerator:

    def __init__(self, workspace_root: Path, bot_location: Path, bot_name: str):
        self.workspace_root = workspace_root
        self.bot_location = bot_location
        self.bot_name = bot_name
        self._bot: Optional[Bot] = None
    
    def _get_bot(self) -> Bot:
        if self._bot is None:
            bot_directory = self.workspace_root / self.bot_location
            config_path = bot_directory / 'bot_config.json'
            self._bot = Bot(bot_name=self.bot_name, bot_directory=bot_directory, config_path=config_path)
        return self._bot

    def generate_cursor_commands(self, cli_script_path: Path, bot: Bot) -> Dict[str, Path]:
        visitor = CursorCommandFileVisitor(
            workspace_root=self.workspace_root,
            cli_script_path=cli_script_path,
            bot=bot
        )
        orchestrator = Orchestrator(visitor)
        orchestrator.generate()
        return visitor.get_commands()

    def update_bot_registry(self, cli_script_path: Path) -> Path:
        registry_path = self._get_registry_path()
        registry = self._load_registry(registry_path)
        rel_cli_path = self._get_relative_cli_path(cli_script_path)
        registry[self.bot_name] = {'trigger_patterns': self._load_bot_trigger_patterns(), 'cli_path': rel_cli_path}
        registry_path.write_text(json.dumps(registry, indent=2, sort_keys=True), encoding='utf-8')
        return registry_path

    def _get_registry_path(self) -> Path:
        registry_path = self.workspace_root / 'agile_bot' / 'bots' / 'registry.json'
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        return registry_path

    def _load_registry(self, registry_path: Path) -> dict:
        if registry_path.exists():
            try:
                return read_json_file(registry_path)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}

    def _get_relative_cli_path(self, cli_script_path: Path) -> str:
        if cli_script_path.is_absolute():
            return str(cli_script_path.relative_to(self.workspace_root)).replace('\\', '/')
        return str(self.bot_location / 'src' / cli_script_path.name).replace('\\', '/')

    def _load_bot_trigger_patterns(self) -> list:
        trigger_file = self.workspace_root / self.bot_location / 'trigger_words.json'
        try:
            trigger_data = read_json_file(trigger_file)
            return trigger_data.get('patterns', [])
        except (json.JSONDecodeError, FileNotFoundError):
            return []