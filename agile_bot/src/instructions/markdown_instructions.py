"""
Markdown adapter for Instructions domain object.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.instructions.instructions import Instructions

class MarkdownInstructions(MarkdownAdapter):
    """Serializes Instructions to Markdown - formats for markdown documents."""
    
    def __init__(self, instructions: Instructions):
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to Markdown string."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # SCOPE SECTION (only show if scope has actual filter values set, or is 'showAll')
        scope = self.instructions.scope
        # Check if scope has filter values (scope.value) - this determines if scope is "empty"
        # When scope.type is 'all', scope.value is empty → don't show scope section
        # When scope.type is 'showAll', scope.value is empty but we show full graph
        # When scope.type is 'story'/'files', scope.value has filter terms → show filtered results
        if scope and (scope.value or scope.type.value == 'showAll'):
            from agile_bot.src.cli.adapters import MarkdownAdapter
            
            output_lines.append("## Scope")
            output_lines.append("")
            if scope.type.value == 'story':
                output_lines.append(f"**Story Scope:** {', '.join(scope.value)}")
            elif scope.type.value == 'files':
                output_lines.append(f"**File Scope:** {', '.join(scope.value)}")
            elif scope.type.value == 'showAll':
                output_lines.append("**Scope:** Show All (entire story graph)")
            else:
                output_lines.append(f"**Scope:** {scope.type.value} - {', '.join(scope.value) if scope.value else 'all'}")
            output_lines.append("")
            
            # Get the filtered results (story graph or files)
            # Show results when scope has filter values OR when type is 'showAll'
            results = scope.results
            if results:
                # Use the appropriate adapter to serialize the scope results
                from agile_bot.src.cli.adapter_factory import AdapterFactory
                try:
                    adapter = AdapterFactory.create(results, 'markdown')
                    scope_content = adapter.serialize()
                    output_lines.append(scope_content)
                except Exception:
                    # Fallback: just show the filter value
                    pass
            
            output_lines.append("")
            output_lines.append("---")
            output_lines.append("")
        
        # BEHAVIOR INSTRUCTIONS SECTION
        behavior_metadata = instructions_dict.get('behavior_metadata', {})
        if behavior_metadata:
            behavior_name = behavior_metadata.get('name', 'unknown')
            output_lines.append(f"# Behavior: {behavior_name}")
            output_lines.append("")
            output_lines.append(f"## Behavior Instructions - {behavior_name}")
            output_lines.append("")
            
            # Add behavior description
            behavior_description = behavior_metadata.get('description', '')
            if behavior_description:
                output_lines.append(f"The purpose of this behavior is to {behavior_description.lower()}")
                output_lines.append("")
            
            # Add behavior-level instructions if present
            behavior_instructions = behavior_metadata.get('instructions', [])
            if behavior_instructions:
                if isinstance(behavior_instructions, list):
                    output_lines.extend(behavior_instructions)
                elif isinstance(behavior_instructions, str):
                    output_lines.append(behavior_instructions)
                output_lines.append("")
        
        # ACTION INSTRUCTIONS SECTION
        action_metadata = instructions_dict.get('action_metadata', {})
        if action_metadata:
            action_name = action_metadata.get('name', 'unknown')
            output_lines.append(f"## Action Instructions - {action_name}")
            output_lines.append("")
            
            # Add action description if available
            action_description = action_metadata.get('description', '')
            if action_description:
                output_lines.append(f"The purpose of this action is to {action_description.lower()}")
                output_lines.append("")
            
            # Add behavior-specific action instructions if present
            action_instructions = action_metadata.get('instructions', [])
            if action_instructions:
                output_lines.extend(action_instructions)
                output_lines.append("")
        
        output_lines.append("---")
        output_lines.append("")
        
        # Add base instructions
        base_instructions = instructions_dict.get('base_instructions', [])
        output_lines.extend(base_instructions)
        
        # Add clarifications (saved answers and evidence, or template questions if none saved)
        clarification_data = instructions_dict.get('clarification', {})
        guardrails_dict = instructions_dict.get('guardrails', {})
        
        # Check for saved clarification data first
        saved_answers = {}
        saved_evidence_provided = {}
        if clarification_data:
            key_questions_data = clarification_data.get('key_questions', {})
            if isinstance(key_questions_data, dict):
                saved_answers = key_questions_data.get('answers', {})
            
            evidence_data = clarification_data.get('evidence', {})
            if isinstance(evidence_data, dict):
                saved_evidence_provided = evidence_data.get('provided', {})
        
        # Show saved answers if they exist, otherwise show template questions
        if saved_answers:
            output_lines.append("")
            output_lines.append("### Key Questions")
            output_lines.append("")
            for question, answer in saved_answers.items():
                output_lines.append(f"- **{question}**: {answer}")
        elif guardrails_dict:
            required_context = guardrails_dict.get('required_context', {})
            if required_context:
                key_questions = required_context.get('key_questions', [])
                if key_questions:
                    output_lines.append("")
                    output_lines.append("### Key Questions")
                    output_lines.append("")
                    if isinstance(key_questions, list):
                        for question in key_questions:
                            output_lines.append(f"- {question}")
                    elif isinstance(key_questions, dict):
                        for question_key, question_text in key_questions.items():
                            output_lines.append(f"- **{question_key}**: {question_text}")
        
        # Show provided evidence if it exists, otherwise show required evidence template
        if saved_evidence_provided:
            output_lines.append("")
            output_lines.append("### Evidence")
            output_lines.append("")
            for evidence_key, evidence_content in saved_evidence_provided.items():
                output_lines.append(f"- **{evidence_key}**: {evidence_content}")
        elif guardrails_dict:
            required_context = guardrails_dict.get('required_context', {})
            if required_context:
                evidence = required_context.get('evidence', [])
                if evidence:
                    output_lines.append("")
                    output_lines.append("### Evidence")
                    output_lines.append("")
                    if isinstance(evidence, list):
                        output_lines.append(', '.join(evidence))
                    elif isinstance(evidence, dict):
                        for evidence_key, evidence_desc in evidence.items():
                            output_lines.append(f"- **{evidence_key}**: {evidence_desc}")
        
        # Strategy action sections - check both 'strategy_criteria' and 'strategy' keys
        strategy_criteria = instructions_dict.get('strategy_criteria', {})
        strategy_data = instructions_dict.get('strategy', {})
        
        # Get strategy_criteria from either location
        if strategy_data and 'strategy_criteria' in strategy_data:
            strategy_criteria = strategy_criteria or strategy_data['strategy_criteria']
        
        # Get saved decisions (check both 'decisions' and 'decisions_made' keys)
        saved_decisions = {}
        if strategy_criteria:
            saved_decisions = strategy_criteria.get('decisions', {}) or strategy_criteria.get('decisions_made', {})
        
        # Show saved decisions if they exist, otherwise show criteria template
        if saved_decisions:
            output_lines.append("")
            output_lines.append("### Decisions")
            output_lines.append("")
            output_lines.append("**Your Decisions:**")
            output_lines.append("")
            for decision_key, decision_value in saved_decisions.items():
                output_lines.append(f"**{decision_key}:**")
                if isinstance(decision_value, list):
                    for item in decision_value:
                        output_lines.append(f"  - {item}")
                else:
                    output_lines.append(f"  {decision_value}")
                output_lines.append("")
        elif strategy_criteria:
            # Show criteria template only if no saved decisions
            criteria_template = strategy_criteria.get('criteria', {})
            if criteria_template:
                output_lines.append("")
                output_lines.append("### Decisions")
                output_lines.append("")
                for criteria_key, criteria_data in criteria_template.items():
                    question = criteria_data.get('question', '')
                    if question:
                        output_lines.append(f"**{criteria_key}:** {question}")
                    else:
                        output_lines.append(f"**{criteria_key}:**")
                    output_lines.append("")
                    options = criteria_data.get('options', [])
                    if options:
                        for option in options:
                            output_lines.extend(self._format_strategy_option(option))
                    output_lines.append("")
        
        # Get assumptions from either 'assumptions' key or from 'strategy' key
        assumptions = instructions_dict.get('assumptions', {})
        if strategy_data and 'assumptions' in strategy_data:
            assumptions = assumptions or strategy_data['assumptions']
        
        # Get saved assumptions (check both 'assumptions' and 'assumptions_made' keys)
        saved_assumptions = []
        if isinstance(assumptions, dict):
            saved_assumptions = assumptions.get('assumptions', []) or assumptions.get('assumptions_made', [])
        elif isinstance(assumptions, list):
            # Legacy format - treat entire list as saved assumptions
            saved_assumptions = assumptions
        
        # Show saved assumptions if they exist, otherwise show template
        if saved_assumptions:
            output_lines.append("")
            output_lines.append("### Assumptions")
            output_lines.append("")
            output_lines.append("**Your Assumptions:**")
            output_lines.append("")
            for assumption in saved_assumptions:
                output_lines.append(f"- {assumption}")
        elif isinstance(assumptions, dict):
            # Show template assumptions only if no saved assumptions
            typical_assumptions = assumptions.get('typical_assumptions', [])
            if typical_assumptions:
                output_lines.append("")
                output_lines.append("### Assumptions")
                output_lines.append("")
                for assumption in typical_assumptions:
                    output_lines.append(f"- {assumption}")
        
        # Add display content
        display_content = instructions_dict.get('display_content', [])
        if display_content:
            output_lines.append("")
            output_lines.extend(display_content)
        
        return "\n".join(output_lines)
    
    def _format_strategy_option(self, option) -> list:
        """Format a single decision criteria option for markdown display."""
        lines = []
        if isinstance(option, dict):
            name = option.get('name', '')
            description = option.get('description', '')
            if name:
                lines.append(f"- **{name}**")
                if description:
                    lines.append(f"  {description}")
            elif description:
                lines.append(f"- {description}")
        elif isinstance(option, str):
            lines.append(f"- {option}")
        return lines
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Instructions)."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower() if parts else ""
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
