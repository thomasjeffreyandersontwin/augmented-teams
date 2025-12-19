from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import json
from datetime import datetime
from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.utils import read_json_file
import logging
logger = logging.getLogger(__name__)
__all__ = ['Bot', 'BotResult', 'Behavior']

class BotResult:

    def __init__(self, status: str, behavior: str, action: str, data: Dict[str, Any]=None):
        self.status = status
        self.behavior = behavior
        self.action = action
        self.data = data or {}
        self.executed_instructions_from = f'{behavior}/{action}'

class Bot:

    def __init__(self, bot_name: str, bot_directory: Path, config_path: Path):
        self.name = bot_name
        self.bot_name = bot_name
        self.config_path = Path(config_path)
        self.bot_paths = BotPaths(bot_directory=bot_directory)
        bot_config_path = self.bot_paths.bot_directory / 'bot_config.json'
        if not bot_config_path.exists():
            raise FileNotFoundError(f'Bot config not found at {bot_config_path}')
        self._config = read_json_file(bot_config_path)
        self.behaviors = Behaviors(bot_name, self.bot_paths)
        self.behaviors._bot_instance = self
        for behavior in self.behaviors:
            behavior.bot = self

    @property
    def base_actions_path(self) -> Path:
        return self.bot_paths.bot_directory / 'base_actions'

    @property
    def description(self) -> str:
        return self._config.get('description', '')

    @property
    def goal(self) -> str:
        return self._config.get('goal', '')

    @property
    def instructions(self) -> List[str]:
        return self._config.get('instructions', [])

    @property
    def mcp(self) -> Dict[str, Any]:
        return self._config.get('mcp', {})

    @property
    def trigger_words(self) -> List[str]:
        return self._config.get('trigger_words', [])

    @property
    def working_area(self) -> Optional[str]:
        return self._config.get('WORKING_AREA')

    def __getattr__(self, name: str):
        behavior = self.behaviors.find_by_name(name)
        if behavior:
            return behavior
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")