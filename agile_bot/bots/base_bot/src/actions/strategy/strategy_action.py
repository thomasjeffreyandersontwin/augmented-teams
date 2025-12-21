from pathlib import Path
from typing import Dict, Any, Type
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext, StrategyActionContext
from agile_bot.bots.base_bot.src.actions.strategy.strategy import Strategy
from agile_bot.bots.base_bot.src.actions.strategy.strategy_decision import StrategyDecision

class StrategyAction(Action):
    context_class: Type[ActionContext] = StrategyActionContext

    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        self._strategy = Strategy(self.behavior.folder)

    @property
    def action_name(self) -> str:
        return 'strategy'

    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError('action_name is read-only for StrategyAction')

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @property
    def strategy_criteria(self):
        return self.strategy.strategy_criterias.strategy_criterias

    @property
    def typical_assumptions(self):
        return self.strategy.assumptions.assumptions

    @property
    def recommended_activities(self):
        return self.strategy.recommended_activities.recommended_activities

    def do_execute(self, context: StrategyActionContext) -> Dict[str, Any]:
        instructions = self.instructions.copy()
        instructions.update(self.strategy.instructions)
        if context.decisions_made or context.assumptions_made:
            self.save_strategy(context)
        return {'instructions': instructions.to_dict()}

    def save_strategy(self, context: StrategyActionContext):
        strategy_decision = StrategyDecision(
            behavior_name=self.behavior.name,
            bot_paths=self.behavior.bot_paths,
            strategy=self.strategy,
            decisions_made=context.decisions_made or {},
            assumptions_made=context.assumptions_made or []
        )
        strategy_decision.save()