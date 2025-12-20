from pathlib import Path
from typing import Dict, Any, Optional, TYPE_CHECKING, List
import json
import logging
import re
import sys
import traceback
from agile_bot.bots.base_bot.src.actions.activity_tracker import ActivityTracker, ActionState
from agile_bot.bots.base_bot.src.actions.workflow_status_builder import BehaviorActionStatusBuilder
from agile_bot.bots.base_bot.src.actions.context_data_injector import ContextDataInjector
from agile_bot.bots.base_bot.src.actions.instructions import Instructions
from agile_bot.bots.base_bot.src.bot.reminders import inject_reminder_to_instructions
from agile_bot.bots.base_bot.src.bot.workspace import get_base_actions_directory
from agile_bot.bots.base_bot.src.utils import read_json_file
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.bot import Bot
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior
    from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors
logger = logging.getLogger(__name__)

class Action:

    def __init__(self, behavior: 'Behavior', action_config: Dict[str, Any]=None, action_name: str=None):
        self.behavior = behavior
        self.action_config = action_config
        action_name = action_name or self._derive_action_name_from_class()
        self._action_name = action_name
        self._activity_tracker = ActivityTracker(behavior.bot_paths, behavior.bot_name)
        self._workflow_status_builder = BehaviorActionStatusBuilder(behavior)
        self._context_data_injector = ContextDataInjector(behavior)
        self._base_config = self._load_base_config()
        if action_config:
            self._apply_action_config()
        self._initialize_properties()

    def _load_base_config(self) -> Dict[str, Any]:
        final_action_name = self.action_name
        base_actions_dir = get_base_actions_directory()
        base_config_path = base_actions_dir / final_action_name / 'action_config.json'
        base_config = read_json_file(base_config_path)
        base_config['name'] = final_action_name
        return base_config

    def _apply_action_config(self) -> None:
        action_config = self.action_config
        if 'order' in action_config:
            self._base_config['order'] = action_config['order']
        behavior_instructions = action_config.get('instructions', [])
        base_instructions = self._base_config.get('instructions', [])
        self._base_config['instructions'] = self._merge_instructions(base_instructions, behavior_instructions)
        self._base_config['custom_class'] = action_config.get('action_class') or action_config.get('custom_class')
        if 'next_action' in action_config:
            self._base_config['next_action'] = action_config['next_action']

    def _initialize_properties(self) -> None:
        self.order = self._base_config.get('order', 0)
        self.next_action = self._base_config.get('next_action')
        self.action_class = self._base_config.get('action_class') or self._base_config.get('custom_class')
        self.workflow = self._base_config.get('workflow', True)

    def _derive_action_name_from_class(self) -> str:
        class_name = self.__class__.__name__
        if class_name.endswith('Action'):
            base_name = class_name[:-6]
        else:
            base_name = class_name
        snake_case = re.sub('(?<!^)(?=[A-Z])', '_', base_name).lower()
        normalization_map = {'render_output': 'render', 'build_knowledge': 'build', 'validate_rules': 'validate', 'clarify_context': 'clarify'}
        return normalization_map.get(snake_case, snake_case)

    @property
    def action_name(self) -> str:
        return self._action_name

    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError("action_name is read-only. It's derived from the class name.")

    def _merge_instructions(self, base_instructions, behavior_instructions) -> List:
        if isinstance(base_instructions, list) and isinstance(behavior_instructions, list):
            return base_instructions + behavior_instructions
        elif isinstance(base_instructions, list):
            return base_instructions + [behavior_instructions] if behavior_instructions else base_instructions
        else:
            return behavior_instructions if behavior_instructions else base_instructions

    def _inject_clarification_data(self, instructions: Dict[str, Any]) -> list:
        return self._context_data_injector.inject_clarification_data(instructions)

    def _inject_strategy_data(self, instructions: Dict[str, Any]) -> list:
        return self._context_data_injector.inject_strategy_data(instructions)

    def _inject_context_files(self, instructions: Dict[str, Any]) -> list:
        return self._context_data_injector.inject_context_files(instructions)

    def get_workflow_status_breadcrumbs(self) -> list:
        return self._workflow_status_builder.get_behavior_action_status_breadcrumbs()

    def _inject_status_update_breadcrumbs(self, instructions: Dict[str, Any]) -> list:
        breadcrumbs = self.get_workflow_status_breadcrumbs()
        return breadcrumbs

    @property
    def instructions(self) -> Instructions:
        base_instructions = self._base_config.get('instructions', [])
        inst = Instructions(base_instructions if isinstance(base_instructions, list) else [], bot_paths=self.behavior.bot_paths)
        
        # Add context instructions (clarification, strategy, context files) at the beginning
        context_instructions = []
        try:
            context_instructions.extend(self._inject_clarification_data({}))
            context_instructions.extend(self._inject_strategy_data({}))
        except FileNotFoundError as e:
            logger.debug(f'Clarification or strategy data files not found: {e}')
            raise
        context_instructions.extend(self._inject_context_files({}))
        
        # Add context instructions to the beginning
        for line in reversed(context_instructions):
            inst._data['base_instructions'].insert(0, line)
        
        # Add workflow status breadcrumbs to display_content (for deterministic display)
        breadcrumbs = self._inject_status_update_breadcrumbs({})
        for line in breadcrumbs:
            inst.add_display(line)
        
        return inst

    @property
    def tracker(self) -> ActivityTracker:
        return self._activity_tracker

    @property
    def base_actions_dir(self) -> Path:
        return get_base_actions_directory()

    @property
    def working_dir(self) -> Path:
        return self.behavior.bot_paths.workspace_directory

    @property
    def bot_dir(self) -> Path:
        return self.behavior.bot_paths.bot_directory

    def track_activity_on_start(self):
        state = ActionState(self.behavior.bot_name, self.behavior.name, self.action_name)
        self.tracker.track_start(state)

    def track_activity_on_completion(self, outputs: dict=None, duration: int=None):
        state = ActionState(self.behavior.bot_name, self.behavior.name, self.action_name, outputs=outputs, duration=duration)
        self.tracker.track_completion(state)

    def execute(self, parameters: Dict[str, Any]=None) -> Dict[str, Any]:
        self.track_activity_on_start()
        try:
            result = self.do_execute(parameters or {})
            
            # Write display content to file after action completes
            result = self._finalize_display_content(result)
            
            if not result.get('_background_execution', False):
                self.track_activity_on_completion(outputs=result)
            return self._inject_reminders_if_final(result)
        except Exception as e:
            self._handle_execution_error(e, parameters)
            raise
    
    def _finalize_display_content(self, result: Dict[str, Any]) -> Dict[str, Any]:
        if 'instructions' not in result or not isinstance(result['instructions'], dict):
            return result
        
        instructions_dict = result['instructions']
        
        # Check if there's display content (stored in the dict from Instructions.to_dict())
        display_content_list = instructions_dict.get('display_content', [])
        if not display_content_list:
            return result
        
        # Write display content to file
        inst = Instructions(bot_paths=self.behavior.bot_paths)
        for line in display_content_list:
            inst.add_display(line)
        
        display_file = inst.write_display_to_file('status.md')
        if display_file:
            # Add instruction to read the file
            if 'base_instructions' not in instructions_dict:
                instructions_dict['base_instructions'] = []
            instructions_dict['base_instructions'].append('')
            instructions_dict['base_instructions'].append(f'CRITICAL: You MUST read the file `{display_file}` and display its ENTIRE contents in a markdown code fence to the user.')
            instructions_dict['base_instructions'].append(f'Use the read_file tool to read `{display_file}` and then display the full contents.')
            instructions_dict['base_instructions'].append(f'DO NOT just reference the file - actually READ it and SHOW its contents to the user.')
        
        return result

    def _handle_execution_error(self, e: Exception, parameters: Dict[str, Any]) -> None:
        error_type = type(e).__name__
        error_message = str(e)
        full_traceback = traceback.format_exc()
        error_instructions = self._build_error_instructions(error_type, error_message, full_traceback, parameters)
        self.track_activity_on_completion(outputs={'error': error_message})
        print('\n'.join(error_instructions), file=sys.stdout)
        sys.stdout.flush()

    def _build_error_instructions(self, error_type: str, error_message: str, full_traceback: str, parameters: Dict[str, Any]) -> List[str]:
        return ['', '=' * 70, '**ERROR OCCURRED DURING ACTION EXECUTION**', '=' * 70, '', f'**Exception Type:** {error_type}', f'**Exception Message:** {error_message}', '', '**Full Traceback:**', '-' * 70, full_traceback, '-' * 70, '', '**Action Details:**', f"- Behavior: {(self.behavior.name if self.behavior else 'unknown')}", f'- Action: {self.action_name}', f'- Parameters: {parameters}', '=' * 70, '', '**AI ASSISTANT: YOU MUST DISPLAY THE ABOVE ERROR TO THE USER.**', '']

    def _inject_reminders_if_final(self, result: Dict[str, Any]) -> Dict[str, Any]:
        if not self.behavior or not self.behavior.actions:
            return result
        action_names = self.behavior.actions.names
        if not action_names or self.action_name != action_names[-1]:
            return result
        if not self.behavior.bot:
            if hasattr(self.behavior, 'actions') and hasattr(self.behavior.actions, 'behavior'):
                behavior_from_actions = self.behavior.actions.behavior
                if hasattr(behavior_from_actions, 'bot_paths'):
                    logger.debug(f'Behavior {self.behavior.name} has no bot reference - reminder will be skipped. This may indicate the behavior was not created through Bot.__init__')
                return result
        reminder = self.behavior.actions._get_next_behavior_reminder()
        if not reminder:
            logger.debug(f'Reminder is empty for action {self.action_name} in behavior {(self.behavior.name if self.behavior else None)}. behavior.bot={(self.behavior.bot if self.behavior else None)}, behavior.bot.behaviors.names={(self.behavior.bot.behaviors.names if self.behavior and self.behavior.bot else None)}')
            return result
        if 'instructions' not in result:
            result['instructions'] = {}
        instructions = result['instructions']
        if isinstance(instructions, dict):
            base_instructions = instructions.get('base_instructions', [])
            if not base_instructions and isinstance(self.instructions, dict) and ('base_instructions' in self.instructions):
                instructions['base_instructions'] = list(self.instructions['base_instructions'])
                result['instructions'] = instructions
        return inject_reminder_to_instructions(result, reminder)

    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError('Subclasses must implement do_execute()')