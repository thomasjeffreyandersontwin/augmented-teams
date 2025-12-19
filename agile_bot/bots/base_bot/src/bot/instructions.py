from pathlib import Path
from typing import Dict, Any, List, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.actions.action import Action
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior

class Instructions:

    def __init__(self, action: 'Action', behavior: 'Behavior'):
        self._action = action
        self._behavior = behavior

    @property
    def base_instructions(self) -> List[str]:
        instructions = self._action._base_config.get('instructions', [])
        if isinstance(instructions, list):
            return instructions
        elif isinstance(instructions, str):
            return [instructions]
        return []

    @property
    def behavior_instructions(self) -> Dict[str, Any]:
        return self._behavior.instructions

    def merge(self) -> Dict[str, Any]:
        merged = {'base_instructions': self.base_instructions, 'behavior_instructions': self.behavior_instructions}
        if isinstance(self.behavior_instructions, dict):
            behavior_instr_list = self.behavior_instructions.get('instructions', [])
            merged['instructions'] = self.base_instructions + behavior_instr_list
        else:
            merged['instructions'] = self.base_instructions
        return merged