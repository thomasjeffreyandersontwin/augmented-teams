from typing import Dict, Any, TYPE_CHECKING
from agile_bot.bots.base_bot.src.bot.bot import BotResult
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior
    from agile_bot.bots.base_bot.src.actions.action import Action

class CliCommandRouter:

    def __init__(self, bot, formatter):
        self.bot = bot
        self.formatter = formatter

    def route_to_action(self, behavior_name: str, action_name: str, parameters: Dict[str, Any]):
        if action_name:
            behavior_obj = self.bot.behaviors.find_by_name(behavior_name) if behavior_name else None
            if not behavior_obj:
                raise ValueError(f"Behavior '{behavior_name}' not found")
            action_obj = behavior_obj.actions.find_by_name(action_name)
            if not action_obj:
                raise ValueError(f"Action '{action_name}' not found in behavior '{behavior_name}'")
            return self._route_to_specific_action(behavior_obj, action_obj, parameters)
        return self._route_to_behavior(behavior_name)
        return self._route_to_current_behavior_and_action()

    def _route_to_specific_action(self, behavior: 'Behavior', action: 'Action', parameters: Dict[str, Any]):
        behavior.actions.navigate_to(action.action_name)
        result_data = action.execute(parameters or {})
        result = BotResult('completed', behavior.name, action.action_name, result_data)
        return self._format_result(result)

    def _route_to_behavior(self, behavior_name: str):
        behavior_obj = self.bot.behaviors.find_by_name(behavior_name)
        if not behavior_obj:
            raise ValueError(f"Behavior '{behavior_name}' not found")
        return self._execute_current_action(behavior_obj)

    def _route_to_current_behavior_and_action(self):
        current_behavior = self._navigate_to_first_behavior_if_needed()
        return self._execute_current_action(current_behavior)

    def _navigate_to_first_behavior_if_needed(self):
        current_behavior = self.bot.behaviors.current
        if current_behavior is None:
            if self.bot.behaviors.first:
                self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
                current_behavior = self.bot.behaviors.current
            else:
                raise ValueError('No behaviors available')
        if current_behavior is None:
            raise ValueError('No current behavior')
        return current_behavior

    def _execute_current_action(self, behavior):
        action = behavior.actions.forward_to_current()
        if action is None:
            raise ValueError(f'No current action found for behavior {behavior.name}')
        result_data = action.execute()
        result = BotResult('completed', behavior.name, action.action_name, result_data)
        return self._format_result(result)

    def _format_result(self, result) -> Dict[str, Any]:
        status = 'success' if result.status == 'completed' else result.status
        return {'status': status, 'behavior': result.behavior, 'action': result.action, 'data': result.data}