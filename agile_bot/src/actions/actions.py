from __future__ import annotations
import json
import logging
from pathlib import Path
from typing import List, Optional, Iterator, Dict, Any, TYPE_CHECKING
from datetime import datetime
from .action_state_manager import ActionStateManager
from .action_factory import ActionFactory
if TYPE_CHECKING:
    from .action import Action
    from agile_bot.src.bot.behavior import Behavior

class Actions:

    def __init__(self, behavior: 'Behavior'):
        self.behavior = behavior
        actions_workflow = behavior._config.get('actions_workflow', {})
        actions_list = actions_workflow.get('actions', [])
        
        # Separate workflow actions (have order) from non-workflow actions (no order)
        workflow_actions = [a for a in actions_list if a.get('order') is not None]
        non_workflow_actions = [a for a in actions_list if a.get('order') is None]
        
        # Sort workflow actions by order
        workflow_actions = sorted(workflow_actions, key=lambda x: x.get('order', 0))
        
        self._factory = ActionFactory(behavior)
        self._state_manager = ActionStateManager(behavior)
        
        # _actions contains only workflow actions (for sequencing)
        self._actions: List[Action] = []
        for action_dict in workflow_actions:
            action_name = action_dict.get('name', '')
            if action_name:
                action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                self._actions.append(action_instance)
        
        # _non_workflow_actions contains actions that can be invoked but don't participate in workflow
        self._non_workflow_actions: List[Action] = []
        for action_dict in non_workflow_actions:
            action_name = action_dict.get('name', '')
            if action_name:
                action_instance = self._factory.create_action_instance(action_name=action_name, action_config=action_dict)
                self._non_workflow_actions.append(action_instance)
        
        # Automatically add 'rules' as a non-workflow action if not already present
        # This makes 'rules' available for all behaviors without needing to explicitly add it to behavior.json
        has_rules = any(action.action_name == 'rules' for action in self._non_workflow_actions)
        if not has_rules:
            try:
                rules_action_instance = self._factory.create_action_instance(action_name='rules', action_config=None)
                self._non_workflow_actions.append(rules_action_instance)
            except Exception as e:
                # If rules action can't be created (e.g., action_config.json doesn't exist), skip it
                logging.getLogger(__name__).debug(f'Could not auto-add rules action: {e}')
        
        self._current_index: Optional[int] = None
        self.load_state()

    @property
    def current(self) -> Optional[Action]:
        if self._current_index is not None and 0 <= self._current_index < len(self._actions):
            return self._actions[self._current_index]
        return None

    @property
    def names(self) -> List[str]:
        return [action.action_name for action in self._actions]

    @property
    def current_action_name(self) -> Optional[str]:
        current = self.current
        return current.action_name if current else None

    @property
    def remaining_actions(self) -> List[str]:
        if not self.current:
            return self.names
        current_name = self.current.action_name
        if current_name not in self.names:
            return self.names
        current_idx = self.names.index(current_name)
        remaining = self.names[current_idx + 1:]
        return [name for name in remaining if not self.is_action_completed(name)]

    def find_by_name(self, action_name: str) -> Optional[Action]:
        # First check workflow actions
        for action in self._actions:
            if action.action_name == action_name:
                return action
        # Then check non-workflow actions
        for action in self._non_workflow_actions:
            if action.action_name == action_name:
                return action
        return None

    def find_by_order(self, order: int) -> Optional[Action]:
        for action in self._actions:
            if action.order == order:
                return action
        return None

    def next(self) -> Optional[Action]:
        next_index = self._current_index + 1
        if next_index < len(self._actions):
            return self._actions[next_index]
        return None

    def __iter__(self) -> Iterator[Action]:
        for action in self._actions:
            yield action

    def __getattr__(self, name: str):
        action = self.find_by_name(name)
        if action:
            return action
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def navigate_to(self, action_name: str):
        action = self.find_by_name(action_name)
        if action is None:
            raise ValueError(f"Action '{action_name}' not found")
        
        # Check if this is a non-workflow action (no order)
        is_non_workflow = action in self._non_workflow_actions
        if is_non_workflow:
            # Non-workflow actions don't affect workflow state
            return
        
        for i, a in enumerate(self._actions):
            if a.action_name == action_name:
                self._current_index = i
                break
        
        self.save_state()

    def close_current(self):
        # Ensure we have a current action before trying to close it
        if self.current is None:
            # No current action to close - ensure we're at the first action
            if self._actions:
                self._current_index = 0
            else:
                # No actions available
                return
        
        # Now that we've ensured _current_index is set, get the current action
        current_action = self.current
        if current_action is None:
            # Still no current action after setting index - something is wrong
            return
        
        state_file = self._state_manager.get_state_file_path()
        state_data = self._state_manager.load_or_create_state(state_file)
        self._ensure_current_behavior_in_state(state_data)
        self._mark_action_completed(state_data)
        self._advance_to_next_action()
        self._update_current_action_in_state(state_data)
        self._save_state_file(state_file, state_data)

    def _ensure_current_behavior_in_state(self, state_data):
        if 'current_behavior' not in state_data:
            state_data['current_behavior'] = f'{self.behavior.bot_name}.{self.behavior.name}'

    def _mark_action_completed(self, state_data):
        if 'completed_actions' not in state_data:
            state_data['completed_actions'] = []
        completed_actions_list = state_data.get('completed_actions', [])
        # Note: This method should only be called when self.current is not None
        # (caller should ensure this via close_current() logic)
        if self.current is None:
            # No current action to mark as completed - skip
            return
        action_state = f'{self.behavior.bot_name}.{self.behavior.name}.{self.current.action_name}'
        is_already_completed = any((a.get('action_state') == action_state for a in completed_actions_list))
        if not is_already_completed:
            new_completed_action_entry = {'action_state': action_state, 'timestamp': datetime.now().isoformat()}
            state_data['completed_actions'] = completed_actions_list + [new_completed_action_entry]
        else:
            state_data['completed_actions'] = completed_actions_list

    def _advance_to_next_action(self):
        next_action_obj = self.next()
        if next_action_obj:
            self._current_index += 1

    def _update_current_action_in_state(self, state_data):
        current_action_obj = self.current
        if current_action_obj:
            state_data['current_action'] = f'{self.behavior.bot_name}.{self.behavior.name}.{current_action_obj.action_name}'
        state_data['timestamp'] = datetime.now().isoformat()

    def _save_state_file(self, state_file, state_data):
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')

    def forward_to_current(self) -> Optional['Action']:
        self.load_state()
        return self.current

    def is_final_action(self) -> bool:
        try:
            action_names = self.names
            if not action_names:
                return False
            # If we have a current action, check position
            if self.current is not None:
                return self.current.action_name == action_names[-1]
            # If no current action, fall back to state file: consider final if last action is marked completed
            state_file = self._state_manager.get_state_file_path()
            if state_file.exists():
                state_data = json.loads(state_file.read_text(encoding='utf-8'))
                completed = state_data.get('completed_actions', [])
                last_action_state = f'{self.behavior.bot_name}.{self.behavior.name}.{action_names[-1]}'
                return any(a.get('action_state') == last_action_state for a in completed if isinstance(a, dict))
        except Exception as e:
            logging.getLogger(__name__).debug(f'Failed to check if action is final: {e}')
            raise
        return False

    def _get_next_behavior_reminder(self) -> str:
        try:
            behavior_names = self.behavior.bot.behaviors.names
            return self._build_behavior_reminder(behavior_names)
        except Exception as e:
            logging.getLogger(__name__).debug(f'Failed to get next behavior reminder: {e}')
            raise
        return ''

    def _build_behavior_reminder(self, behavior_names: list) -> str:
        try:
            current_index = behavior_names.index(self.behavior.name)
        except (ValueError, IndexError) as e:
            logging.getLogger(__name__).debug(f'Failed to get next behavior reminder (ValueError/IndexError): {e}')
            raise
        if current_index + 1 >= len(behavior_names):
            return ''
        next_behavior_name = behavior_names[current_index + 1]
        next_behavior = self.behavior.bot.behaviors.find_by_name(next_behavior_name)
        first_action_name = self._get_first_action_name(next_behavior)
        if first_action_name:
            return f"After completing this action, the next behavior in sequence is `{next_behavior_name}`. The first action in `{next_behavior_name}` is `{first_action_name}`. When the user is ready to continue, remind them: 'The next behavior in sequence is `{next_behavior_name}`. Would you like to continue with `{next_behavior_name}` or work on a different behavior?'"
        return f"After completing this behavior, the next behavior in sequence is `{next_behavior_name}`. When the user is ready to continue, remind them: 'The next behavior in sequence is `{next_behavior_name}`. Would you like to continue with `{next_behavior_name}` or work on a different behavior?'"

    def _get_first_action_name(self, next_behavior) -> Optional[str]:
        if not next_behavior:
            return None
        if not next_behavior.actions.names:
            return None
        return next_behavior.actions.names[0]

    def save_state(self):
        state_file = self._state_manager.get_state_file_path()
        self._state_manager.save_state(self.current, state_file)

    def load_state(self):
        current_index_ref = [self._current_index]
        self._state_manager.load_state(self._actions, current_index_ref)
        self._current_index = current_index_ref[0]

    def is_action_completed(self, action_name: str) -> bool:
        """
        Check if an action is completed.
        
        Previous behavior marked all earlier actions as completed when the current
        index moved forward. That caused the panel to show checkmarks on every prior
        action, which we no longer want. Until we have explicit completion state,
        treat actions as not completed unless a real completion flag exists.
        """
        return False