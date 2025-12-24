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
    
    def _prepare_instructions(self, instructions, context: StrategyActionContext):
        """Add strategy data (criteria, assumptions, activities) to instructions."""
        instructions.update(self.strategy.instructions)
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Format strategy data for REPL display."""
        # Get base formatting first
        output_lines = super()._format_instructions_for_display(instructions).split('\n')
        
        # Get the instruction data
        instructions_dict = instructions.to_dict()
        
        # Format strategy criteria
        strategy_criteria = instructions_dict.get('strategy_criteria', {})
        if strategy_criteria:
            output_lines.append("")
            output_lines.append("**DECISION CRITERIA:**")
            for criteria_key, criteria_data in strategy_criteria.items():
                output_lines.append("")
                output_lines.append(f"**{criteria_key}:**")
                question = criteria_data.get('question', '')
                if question:
                    output_lines.append(f"  Question: {question}")
                options = criteria_data.get('options', [])
                if options:
                    output_lines.append("  Options:")
                    for option in options:
                        output_lines.append(f"    - {option}")
                outcome = criteria_data.get('outcome', '')
                if outcome:
                    output_lines.append(f"  Outcome: {outcome}")
        
        # Format assumptions
        assumptions = instructions_dict.get('assumptions', [])
        if assumptions:
            output_lines.append("")
            output_lines.append("**TYPICAL ASSUMPTIONS:**")
            for assumption in assumptions:
                output_lines.append(f"- {assumption}")
        
        # Format recommended activities
        recommended_activities = instructions_dict.get('recommended_activities', [])
        if recommended_activities:
            output_lines.append("")
            output_lines.append("**RECOMMENDED HUMAN ACTIVITIES:**")
            for activity in recommended_activities:
                output_lines.append(f"- {activity}")
        
        return "\n".join(output_lines)

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