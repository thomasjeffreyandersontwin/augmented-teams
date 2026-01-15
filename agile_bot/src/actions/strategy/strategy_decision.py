from typing import Dict, Any
from ...bot_path import BotPath
from .json_persistent import JsonPersistent
from .strategy import Strategy

class StrategyDecision(JsonPersistent):

    def __init__(self, behavior_name: str, bot_paths: BotPath, strategy: Strategy, decisions_made: Dict[str, Any]=None, assumptions_made: list=None):
        super().__init__(bot_paths, 'strategy.json')
        self.behavior_name = behavior_name
        self.strategy = strategy
        self.decisions_made = decisions_made or {}
        self.assumptions_made = assumptions_made or []

    def save(self):
        existing_data = self.load()
        
        # Get existing decisions and assumptions for this behavior
        behavior_data = existing_data.get(self.behavior_name, {})
        existing_decisions = behavior_data.get('strategy_criteria', {}).get('decisions_made', {})
        existing_assumptions = behavior_data.get('assumptions', {}).get('assumptions_made', [])
        
        # Merge new decisions with existing (new decisions override existing ones)
        merged_decisions = {**existing_decisions, **self.decisions_made}
        
        # Merge assumptions - for now, replace with new assumptions if provided
        # (Could be extended to append instead of replace)
        merged_assumptions = self.assumptions_made if self.assumptions_made else existing_assumptions
        
        # Only save the user's decisions and assumptions, not the criteria template
        new_data = {
            'strategy_criteria': {
                'decisions_made': merged_decisions
            }, 
            'assumptions': {
                'assumptions_made': merged_assumptions
            }
        }
        merged_data = self.merge(existing_data, new_data, self.behavior_name)
        super().save(merged_data)

    @classmethod
    def load_all(cls, bot_paths: BotPath) -> Dict[str, Any]:
        instance = cls.__new__(cls)
        instance.bot_paths = bot_paths
        instance.filename = 'strategy.json'
        return instance.load()