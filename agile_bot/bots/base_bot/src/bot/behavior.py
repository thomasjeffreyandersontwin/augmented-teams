from __future__ import annotations
from pathlib import Path
from typing import TYPE_CHECKING, Dict, Any
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.bot import BotResult

class Behavior:

    def __init__(self, name: str, bot_paths: BotPaths, bot_instance=None):
        if not isinstance(bot_paths, BotPaths):
            raise TypeError('bot_paths must be an instance of BotPaths')
        self.bot_name = bot_paths.bot_directory.name
        self.name = name
        self.bot_paths = bot_paths
        self.bot = bot_instance
        self._load_config()
        self._initialize_from_config()
        self._guardrails = None
        self._content = None
        self._rules = None
        self._actions = None
        self._trigger_words_obj = None

    def _load_config(self):
        self.behavior_directory = self.bot_paths.bot_directory / 'behaviors' / self.name
        self.config_path = self.behavior_directory / 'behavior.json'
        if not self.config_path.exists():
            raise FileNotFoundError(f'Behavior config not found at {self.config_path}. Each behavior must define its own behavior.json.')
        self._config = read_json_file(self.config_path)

    def _initialize_from_config(self):
        self.description = self._config.get('description', '')
        self.goal = self._config.get('goal', '')
        self.inputs = self._config.get('inputs', [])
        self.outputs = self._config.get('outputs', [])
        self.instructions = self._config.get('instructions', {})
        self.trigger_words = self._config.get('trigger_words', [])
        self.order = self._config.get('order', 999)

    @property
    def base_actions_path(self) -> Path:
        return self.bot_paths.base_actions_directory

    @property
    def actions_workflow(self) -> list:
        actions = self._config.get('actions_workflow', {}).get('actions', [])
        if not isinstance(actions, list):
            return []
        return sorted(actions, key=lambda a: a.get('order', 0))

    @property
    def action_names(self) -> list:
        return [action.get('name', '') for action in self.actions_workflow if action.get('name')]

    @property
    def folder(self) -> Path:
        return self.behavior_directory

    @property
    def is_completed(self) -> bool:
        if not self.actions.names:
            return False
        return all((self.actions.is_action_completed(name) for name in self.actions.names))

    def matches_trigger(self, text: str) -> bool:
        return self.trigger_words.matches(text)

    def does_requested_action_match_current(self, requested_action: str) -> tuple[bool, str | None, str | None]:
        self.actions.load_state()
        current_action = self.actions.current
        current_action_name = current_action.action_name if current_action else None
        if current_action_name == requested_action:
            return (True, current_action_name, None)
        expected_next = None
        if current_action:
            next_action = self.actions.next()
            if next_action:
                expected_next = next_action.action_name
        return (False, current_action_name, expected_next)

    @property
    def guardrails(self):
        if self._guardrails is None:
            from agile_bot.bots.base_bot.src.actions.guardrails import Guardrails
            self._guardrails = Guardrails(self)
        return self._guardrails

    @property
    def content(self):
        if self._content is None:
            from agile_bot.bots.base_bot.src.actions.content import Content
            self._content = Content(self)
        return self._content

    @property
    def rules(self):
        if self._rules is None:
            from agile_bot.bots.base_bot.src.actions.validate.rules import Rules
            self._rules = Rules(behavior=self, bot_paths=self.bot_paths)
        return self._rules

    @property
    def actions(self):
        if self._actions is None:
            from agile_bot.bots.base_bot.src.actions.actions import Actions
            self._actions = Actions(self)
        return self._actions

    @property
    def trigger_words_obj(self):
        if self._trigger_words_obj is None:
            from agile_bot.bots.base_bot.src.bot.trigger_words import TriggerWords
            self._trigger_words_obj = TriggerWords(self)
        return self._trigger_words_obj