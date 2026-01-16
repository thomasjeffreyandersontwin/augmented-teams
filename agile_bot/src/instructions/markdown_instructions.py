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
        
        # Add guardrails
        guardrails_dict = instructions_dict.get('guardrails', {})
        if guardrails_dict:
            required_context = guardrails_dict.get('required_context', {})
            if required_context:
                key_questions = required_context.get('key_questions', [])
                evidence = required_context.get('evidence', [])
                
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
                
                if evidence:
                    output_lines.append("")
                    output_lines.append("### Evidence")
                    output_lines.append("")
                    if isinstance(evidence, list):
                        output_lines.append(', '.join(evidence))
                    elif isinstance(evidence, dict):
                        for evidence_key, evidence_desc in evidence.items():
                            output_lines.append(f"- **{evidence_key}**: {evidence_desc}")
        
        # Strategy action sections
        strategy_criteria = instructions_dict.get('strategy_criteria', {})
        if strategy_criteria:
            output_lines.append("")
            output_lines.append("### Decisions")
            output_lines.append("")
            
            # First show criteria template (if available)
            criteria_template = strategy_criteria.get('criteria', {})
            if criteria_template:
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
            
            # Then show saved decisions
            saved_decisions = strategy_criteria.get('decisions', {})
            if saved_decisions:
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
        
        assumptions = instructions_dict.get('assumptions', {})
        if assumptions:
            output_lines.append("")
            output_lines.append("### Assumptions")
            output_lines.append("")
            
            # Show template assumptions
            if isinstance(assumptions, dict):
                typical_assumptions = assumptions.get('typical_assumptions', [])
                if typical_assumptions:
                    for assumption in typical_assumptions:
                        output_lines.append(f"- {assumption}")
                
                # Show saved assumptions
                saved_assumptions = assumptions.get('assumptions', [])
                if saved_assumptions:
                    output_lines.append("")
                    output_lines.append("**Your Assumptions:**")
                    output_lines.append("")
                    for assumption in saved_assumptions:
                        output_lines.append(f"- {assumption}")
            elif isinstance(assumptions, list):
                # Legacy format - just a list of assumptions
                for assumption in assumptions:
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
