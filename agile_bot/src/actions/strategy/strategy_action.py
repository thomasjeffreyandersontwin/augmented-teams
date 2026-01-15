from pathlib import Path
from typing import Dict, Any, Type
from ..action import Action
from ..action_context import ActionContext, StrategyActionContext
from .strategy import Strategy
from .strategy_decision import StrategyDecision

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
    
    def _prepare_instructions(self, instructions, context: StrategyActionContext):
        """Add strategy data (criteria, assumptions) and saved decisions to instructions.
        
        Note: Workflow instructions come from base_actions/strategy/action_config.json.
        This method adds only the behavior-specific data.
        """
        strategy_data = self.strategy.instructions
        
        # Load saved strategy decisions if they exist
        saved_data = StrategyDecision.load_all(self.behavior.bot_paths)
        saved_behavior_data = saved_data.get(self.behavior.name, {}) if saved_data else {}
        
        # Build combined strategy structure that includes both template and saved data
        combined_strategy_criteria = {}
        combined_assumptions = {}
        
        if strategy_data:
            # Get criteria template
            criteria_template = strategy_data.get('strategy_criteria', {})
            combined_strategy_criteria['criteria'] = criteria_template
            
            # Get assumptions template
            assumptions_template = strategy_data.get('assumptions', {})
            if isinstance(assumptions_template, dict):
                # If it has 'typical_assumptions' key already, use it
                if 'typical_assumptions' in assumptions_template:
                    combined_assumptions['typical_assumptions'] = assumptions_template.get('typical_assumptions', [])
                else:
                    # Otherwise, treat the whole dict as the typical assumptions list
                    combined_assumptions['typical_assumptions'] = assumptions_template
            elif isinstance(assumptions_template, list):
                combined_assumptions['typical_assumptions'] = assumptions_template
        
        # Add saved decisions
        saved_decisions = saved_behavior_data.get('strategy_criteria', {}).get('decisions_made', {})
        if saved_decisions:
            combined_strategy_criteria['decisions_made'] = saved_decisions
        
        # Add saved assumptions
        saved_assumptions = saved_behavior_data.get('assumptions', {}).get('assumptions_made', [])
        if saved_assumptions:
            combined_assumptions['assumptions_made'] = saved_assumptions
        
        # Set combined data in instructions
        if combined_strategy_criteria:
            instructions.set('strategy_criteria', combined_strategy_criteria)
        if combined_assumptions:
            instructions.set('assumptions', combined_assumptions)
    
        # Also load saved clarifications so they're visible on strategy page
        try:
            from ..clarify.requirements_clarifications import RequirementsClarifications
            from ..clarify.required_context import RequiredContext
            
            required_context = RequiredContext(self.behavior.folder)
            clarifications = RequirementsClarifications(
                behavior_name=self.behavior.name,
                bot_paths=self.behavior.bot_paths,
                required_context=required_context,
                key_questions_answered={},
                evidence_provided={}
            )
            saved_clarifications = clarifications.load()
            if saved_clarifications and self.behavior.name in saved_clarifications:
                instructions.set('clarification', saved_clarifications[self.behavior.name])
        except Exception:
            pass  # Silently skip if can't load clarifications
    
    def _format_instructions_for_display(self, instructions) -> str:
        """Format strategy data for REPL display."""
        # Get base formatting first (includes scope warning if set)
        output_lines = super()._format_instructions_for_display(instructions).split('\n')
        
        # Get the instruction data
        instructions_dict = instructions.to_dict()
        
        # Format strategy criteria
        strategy_criteria = instructions_dict.get('strategy_criteria', {})
        if strategy_criteria:
            output_lines.append("")
            output_lines.append("**Decisions:**")
            for criteria_key, criteria_data in strategy_criteria.items():
                output_lines.append("")
                question = criteria_data.get('question', '')
                if question:
                    output_lines.append(f"**{criteria_key}:** {question}")
                else:
                    output_lines.append(f"**{criteria_key}:**")
                options = criteria_data.get('options', [])
                if options:
                    for option in options:
                        output_lines.extend(self._format_option(option))
        
        # Format assumptions
        assumptions = instructions_dict.get('assumptions', [])
        if assumptions:
            output_lines.append("")
            output_lines.append("**Assumptions:**")
            for assumption in assumptions:
                output_lines.append(f"- {assumption}")
        
        return "\n".join(output_lines)

    def _format_option(self, option) -> list:
        """Format a single decision criteria option for display."""
        lines = []
        if isinstance(option, dict):
            name = option.get('name', option.get('id', 'Unknown'))
            description = option.get('description', '')
            when_to_use = option.get('when_to_use', '')
            example = option.get('example', '')
            
            lines.append(f"  [{name}]")
            if description:
                lines.append(f"    {description}")
            if when_to_use:
                lines.append(f"    When: {when_to_use}")
            if example:
                lines.append(f"    Example:")
                for example_line in example.split('\n'):
                    lines.append(f"      {example_line}")
        else:
            lines.append(f"  - {option}")
        return lines

    def do_execute(self, context: StrategyActionContext = None):
        """Execute strategy action - get instructions and save if decisions provided."""
        if context is None:
            context = StrategyActionContext()
        result = self.get_instructions(context)
        decisions = context.get_decisions()
        if decisions or context.assumptions:
            self.save_strategy(context)
        return result

    def save_strategy(self, context: StrategyActionContext):
        strategy_decision = StrategyDecision(
            behavior_name=self.behavior.name,
            bot_paths=self.behavior.bot_paths,
            strategy=self.strategy,
            decisions_made=context.get_decisions(),
            assumptions_made=context.assumptions or []
        )
        strategy_decision.save()