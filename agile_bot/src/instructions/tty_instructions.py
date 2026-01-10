"""
TTY adapter for Instructions domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.instructions.instructions import Instructions

class TTYInstructions(TTYAdapter):
    """Serializes Instructions to TTY - formats all instruction components."""
    
    def __init__(self, instructions: Instructions):
        self.instructions = instructions
    
    def serialize(self) -> str:
        """Convert Instructions to TTY string - assembles all instruction sections."""
        instructions_dict = self.instructions.to_dict()
        output_lines = []
        
        # BEHAVIOR INSTRUCTIONS SECTION
        behavior_metadata = instructions_dict.get('behavior_metadata', {})
        if behavior_metadata:
            behavior_name = behavior_metadata.get('name', 'unknown')
            output_lines.append(f"{self.add_bold(f'Behavior Instructions - {behavior_name}')}")
            
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
            output_lines.append(f"{self.add_bold(f'Action Instructions - {action_name}')}")
            
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
        
        # Add base instructions (context sources + base action instructions)
        base_instructions = instructions_dict.get('base_instructions', [])
        output_lines.extend(base_instructions)
        
        # Add guardrails (delegate to Guardrails adapter)
        guardrails_dict = instructions_dict.get('guardrails', {})
        if guardrails_dict:
            # Check if we have a domain object or dict (backward compatibility)
            if hasattr(self.instructions, '_guardrails') and self.instructions._guardrails:
                # New pattern: delegate to Guardrails adapter
                from agile_bot.src.cli.adapter_factory import AdapterFactory
                guardrails_adapter = AdapterFactory.create(self.instructions._guardrails, 'tty')
                output_lines.append(guardrails_adapter.serialize())
            else:
                # Old pattern: format dict manually (fallback for backward compatibility)
                required_context = guardrails_dict.get('required_context', {})
                if required_context:
                    key_questions = required_context.get('key_questions', [])
                    evidence = required_context.get('evidence', [])
                    
                    if key_questions:
                        output_lines.append("")
                        output_lines.append(self.add_bold("Key Questions:"))
                        if isinstance(key_questions, list):
                            for question in key_questions:
                                output_lines.append(f"- {question}")
                        elif isinstance(key_questions, dict):
                            for question_key, question_text in key_questions.items():
                                output_lines.append(f"- {self.add_bold(f'{question_key}:')} {question_text}")
                    
                    if evidence:
                        output_lines.append("")
                        output_lines.append(self.add_bold("Evidence:"))
                        if isinstance(evidence, list):
                            output_lines.append(', '.join(evidence))
                        elif isinstance(evidence, dict):
                            for evidence_key, evidence_desc in evidence.items():
                                output_lines.append(f"- {self.add_bold(f'{evidence_key}:')} {evidence_desc}")
        
        # ACTION-SPECIFIC SECTIONS
        
        # Strategy action: delegate to Strategy adapter if available
        strategy_criteria = instructions_dict.get('strategy_criteria', {})
        assumptions = instructions_dict.get('assumptions', [])
        
        if hasattr(self.instructions, '_strategy') and self.instructions._strategy:
            # New pattern: delegate to Strategy adapter
            from agile_bot.src.cli.adapter_factory import AdapterFactory
            strategy_adapter = AdapterFactory.create(self.instructions._strategy, 'tty')
            output_lines.append(strategy_adapter.serialize())
        elif strategy_criteria or assumptions:
            # Old pattern: format dict manually (fallback for backward compatibility)
            if strategy_criteria:
                output_lines.append("")
                output_lines.append(self.add_bold("Decisions:"))
                for criteria_key, criteria_data in strategy_criteria.items():
                    output_lines.append("")
                    question = criteria_data.get('question', '')
                    if question:
                        output_lines.append(f"{self.add_bold(f'{criteria_key}:')} {question}")
                    else:
                        output_lines.append(self.add_bold(f"{criteria_key}:"))
                    options = criteria_data.get('options', [])
                    if options:
                        for option in options:
                            output_lines.extend(self._format_strategy_option(option))
            
            if assumptions:
                output_lines.append("")
                output_lines.append(self.add_bold("Assumptions:"))
                for assumption in assumptions:
                    output_lines.append(f"- {assumption}")
        
        # Add display content (action-specific formatted content)
        display_content = instructions_dict.get('display_content', [])
        if display_content:
            output_lines.append("")
            output_lines.extend(display_content)
        
        return "\n".join(output_lines)
    
    def _format_strategy_option(self, option) -> list:
        """Format a single decision criteria option for display."""
        lines = []
        if isinstance(option, dict):
            name = option.get('name', '')
            description = option.get('description', '')
            if name:
                lines.append(f"  - {self.add_bold(name)}")
                if description:
                    lines.append(f"    {description}")
            elif description:
                lines.append(f"  - {description}")
        elif isinstance(option, str):
            lines.append(f"  - {option}")
        return lines
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text (not used for Instructions)."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower() if parts else ""
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
