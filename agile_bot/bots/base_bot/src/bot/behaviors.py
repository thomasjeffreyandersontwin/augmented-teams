from __future__ import annotations
import json
import logging
import traceback
from pathlib import Path
from typing import List, Optional, Iterator, Tuple, Dict, Any, TYPE_CHECKING
from datetime import datetime
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.bot.reminders import inject_reminder_to_instructions
from agile_bot.bots.base_bot.src.bot.behavior import Behavior
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.bot import BotResult
logger = logging.getLogger(__name__)

class Behaviors:

    def __init__(self, bot_name: str, bot_paths: BotPaths):
        self.bot_name = bot_name
        self.bot_paths = bot_paths
        self._behaviors: List['Behavior'] = []
        self._discover_behaviors()
        self._current_index: Optional[int] = None
        self.load_state()

    def _load_behavior_from_dir(self, item: Path) -> tuple:
        behavior_json_path = item / 'behavior.json'
        if not behavior_json_path.exists():
            return None
        try:
            config = read_json_file(behavior_json_path)
            order = config.get('order', 999)
            behavior = Behavior(name=item.name, bot_paths=self.bot_paths, bot_instance=None)
            return (order, behavior)
        except Exception as e:
            logger.warning(f'Failed to load behavior {item.name}: {e}')
            logger.debug(f'Traceback: {traceback.format_exc()}')
            return None

    def _discover_behaviors(self) -> None:
        behaviors_dir = self.bot_paths.bot_directory / 'behaviors'
        if not behaviors_dir.exists():
            return
        behavior_orders = []
        for item in behaviors_dir.iterdir():
            if not item.is_dir() or item.name.startswith('_') or item.name.startswith('.'):
                continue
            result = self._load_behavior_from_dir(item)
            if result:
                behavior_orders.append(result)
        behavior_orders.sort(key=lambda x: x[0])
        self._behaviors = [behavior for _, behavior in behavior_orders]

    @property
    def current(self) -> Optional['Behavior']:
        if self._current_index is not None and 0 <= self._current_index < len(self._behaviors):
            return self._behaviors[self._current_index]
        return None

    @property
    def names(self) -> List[str]:
        return [b.name for b in self._behaviors]

    @property
    def completed_behaviors(self) -> List[str]:
        completed = []
        for behavior in self._behaviors:
            if behavior.is_completed:
                completed.append(behavior.name)
        return completed

    @property
    def remaining_behaviors(self) -> List['Behavior']:
        return [b for b in self._behaviors if not b.is_completed]

    @property
    def next_step_command(self) -> Optional[str]:
        current = self.current
        if not current:
            return None
        remaining_actions = current.actions.remaining_actions
        if remaining_actions:
            return f'/{self.bot_name}-{current.name} {remaining_actions[0]}'
        next_behavior = self.next()
        if next_behavior and next_behavior.actions.names:
            return f'/{self.bot_name}-{next_behavior.name} {next_behavior.actions.names[0]}'
        return None

    @property
    def first(self) -> Optional['Behavior']:
        return self._behaviors[0] if self._behaviors else None

    def is_empty(self) -> bool:
        return len(self._behaviors) == 0

    def find_by_name(self, behavior_name: str) -> Optional['Behavior']:
        for behavior in self._behaviors:
            if behavior.name == behavior_name:
                return behavior
        return None

    def next(self) -> Optional['Behavior']:
        next_index = self._current_index + 1
        if next_index < len(self._behaviors):
            return self._behaviors[next_index]
        return None

    def __iter__(self) -> Iterator['Behavior']:
        for behavior in self._behaviors:
            yield behavior

    def check_exists(self, behavior_name: str) -> bool:
        return self.find_by_name(behavior_name) is not None

    def navigate_to(self, behavior_name: str):
        behavior = self.find_by_name(behavior_name)
        if behavior is None:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        for i, b in enumerate(self._behaviors):
            if b.name == behavior.name:
                self._current_index = i
                return

    def close_current(self):
        if self._current_index is not None:
            next_behavior = self.next()
            if next_behavior:
                self._current_index += 1
                self.save_state()

    def _inject_next_behavior_reminder(self, result: dict, action_name: str=None) -> dict:
        if not self._is_final_behavior():
            return result
        if action_name and self.current:
            action_names = self.current.actions.names
            if action_names and action_name != action_names[-1]:
                return result
        reminder = self._get_next_behavior_reminder()
        if not reminder:
            return result
        return inject_reminder_to_instructions(result, reminder)

    def _is_final_behavior(self) -> bool:
        try:
            if self.current is None:
                return False
            if self.names and self.current.name == self.names[-1]:
                return True
        except Exception as e:
            logger.debug(f'Failed to check if behavior is final: {e}')
            raise
        return False

    def _get_next_behavior_reminder(self) -> str:
        try:
            next_behavior = self.next()
            if next_behavior:
                return f"After completing this behavior, the next behavior in sequence is `{next_behavior.name}`. When the user is ready to continue, remind them: 'The next behavior in sequence is `{next_behavior.name}`. Would you like to continue with `{next_behavior.name}` or work on a different behavior?'"
        except Exception as e:
            logger.debug(f'Failed to get next behavior reminder: {e}')
            raise
        return ''

    def save_state(self):
        if self.current is None or self.bot_paths is None:
            return
        workspace_dir = self.bot_paths.workspace_directory
        state_file = workspace_dir / 'behavior_action_state.json'
        state_data = {}
        if state_file.exists():
            try:
                state_data = json.loads(state_file.read_text(encoding='utf-8'))
            except Exception as e:
                logger.debug(f'Failed to load state file {state_file}: {e}')
                raise
        state_data['current_behavior'] = f'{self.bot_name}.{self.current.name}'
        state_data['timestamp'] = datetime.now().isoformat()
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')

    def _init_to_first_behavior(self) -> None:
        if self._behaviors:
            self._current_index = 0

    def _find_behavior_index(self, behavior_name: str) -> int:
        for i, behavior in enumerate(self._behaviors):
            if behavior.name == behavior_name:
                return i
        return -1

    def _extract_behavior_name_from_state(self, current_behavior_full: str) -> str:
        if not current_behavior_full:
            return None
        parts = current_behavior_full.split('.')
        if len(parts) >= 2:
            return '.'.join(parts[1:])
        return None

    def load_state(self):
        if self.bot_paths is None:
            self._init_to_first_behavior()
            return
        workspace_dir = self.bot_paths.workspace_directory
        state_file = workspace_dir / 'behavior_action_state.json'
        if not state_file.exists() or not self._behaviors:
            self._init_to_first_behavior()
            return
        try:
            state_data = json.loads(state_file.read_text(encoding='utf-8'))
            behavior_name = self._extract_behavior_name_from_state(state_data.get('current_behavior', ''))
            if behavior_name:
                idx = self._find_behavior_index(behavior_name)
                if idx >= 0:
                    self._current_index = idx
                    return
            self._init_to_first_behavior()
        except Exception:
            self._init_to_first_behavior()

    def initialize_state(self, confirmed_behavior: str):
        if self.bot_paths is None:
            raise ValueError('Cannot initialize state without bot_paths')
        behavior_obj = self.find_by_name(confirmed_behavior)
        if behavior_obj is None:
            raise ValueError(f"Behavior '{confirmed_behavior}' not found. Available behaviors: {', '.join(self.names)}.")
        workspace_dir = self.bot_paths.workspace_directory
        state_file = workspace_dir / 'behavior_action_state.json'
        action_names = behavior_obj.actions.names
        first_action = action_names[0] if action_names else 'clarify'
        self.navigate_to(confirmed_behavior)
        state_data = {'current_behavior': f'{self.bot_name}.{behavior_obj.name}', 'current_action': f'{self.bot_name}.{behavior_obj.name}.{first_action}', 'completed_actions': [], 'timestamp': datetime.now().isoformat()}
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')

    def get_entry_state_result(self) -> 'BotResult':
        from agile_bot.bots.base_bot.src.bot.bot import BotResult
        return BotResult(status='requires_confirmation', behavior='', action='', data={'message': f"**ENTRY STATE**\n\nNo behavior state found. Please select a behavior to start:\n\n{chr(10).join((f'- {b}' for b in self.names))}\n\nProvide 'confirmed_behavior' in parameters to proceed.", 'behaviors': self.names, 'requires_confirmation': True})

    def does_requested_match_current(self, requested_behavior: str) -> Tuple[bool, Optional[str], Optional[str]]:
        if not self.current:
            return (True, None, None)
        current_behavior = self.current.name
        requested_behavior_obj = self.find_by_name(requested_behavior)
        requested_matched = requested_behavior_obj.name if requested_behavior_obj else None
        next_behavior_obj = self.next()
        expected_next = next_behavior_obj.name if next_behavior_obj else None
        if requested_matched is None:
            matches = False
        elif requested_matched == current_behavior:
            matches = True
        elif expected_next is None:
            matches = True
        else:
            matches = requested_matched == expected_next
        logger.debug(f'Behavior order check: requested={requested_behavior} ({requested_matched}), current={current_behavior}, expected_next={expected_next}, matches={matches}')
        return (matches, current_behavior, expected_next)