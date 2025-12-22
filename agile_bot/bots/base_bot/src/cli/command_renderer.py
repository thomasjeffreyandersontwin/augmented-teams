from pathlib import Path
from typing import List
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class CursorCommandVisitor(Visitor):
    
    def __init__(self, python_command: str, bot_name: str, behavior_name: str, output_lines: List[str]):
        self.python_command = python_command
        self.bot_name = bot_name
        self.behavior_name = behavior_name
        self.output_lines = output_lines
    
    def visit_header(self, bot_name: str) -> None:
        pass
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        pass
    
    def visit_action(self, context: ActionHelpContext) -> None:
        short_desc = self._extract_short_description(context)
        self.output_lines.append(f"### {context.action_name} - {short_desc}")
        self.output_lines.append(f"{self.python_command} --behavior {self.behavior_name} --action {context.action_name}")
        
        if not context.parameters:
            self.output_lines.append("  # (No optional parameters)")
            self.output_lines.append("")
            return
        
        self._append_parameter_help(context)
        self._append_example_command(context)
        self.output_lines.append("")
    
    def _extract_short_description(self, context: ActionHelpContext) -> str:
        if not context.action_description:
            return context.action_name
        return context.action_description.split('\n')[0].split('.')[0]
    
    def _append_parameter_help(self, context: ActionHelpContext) -> None:
        for param in context.parameters:
            self.output_lines.append(f"  # Optional: {param}")
            if param in context.parameter_descriptions:
                desc = context.parameter_descriptions[param]
                for desc_line in desc.split('\n'):
                    self.output_lines.append(f"  #   {desc_line}")
    
    def _append_example_command(self, context: ActionHelpContext) -> None:
        example_params = self._build_example_params(context.parameters[:2])
        if not example_params:
            return
        
        self.output_lines.append("  #")
        self.output_lines.append("  # Full example:")
        example_cmd = f"{self.python_command} --behavior {self.behavior_name} --action {context.action_name} {' '.join(example_params)}"
        self.output_lines.append(f"  # {example_cmd}")
    
    def _build_example_params(self, params: List[str]) -> List[str]:
        example_params = []
        for param in params:
            param_name = param.split()[0]
            if '<dict>' in param:
                example_params.append(f"{param_name} '{{\"key\": \"value\"}}'")
            elif '<list>' in param:
                example_params.append(f'{param_name} "value1" "value2"')
            elif '<flag>' in param:
                example_params.append(param_name)
            else:
                example_params.append(f'{param_name} "value"')
        return example_params
    
    def visit_action_help_section_header(self) -> None:
        pass
    
    def visit_footer(self) -> None:
        scope_epic = "{'type': 'epic', 'value': ['Epic Name']}"
        self.output_lines.extend([
            "## Common Patterns:",
            "  # Work on specific epic:",
            f"  {self.python_command} --behavior {self.behavior_name} --action build --scope \"{scope_epic}\"",
            "",
            "  # Validate with exclusions:",
            f"  {self.python_command} --behavior {self.behavior_name} --action validate --skiprule rule_to_skip",
            "",
            "  # Work on multiple stories:",
            f"  {self.python_command} --behavior {self.behavior_name} --action build --scope \"{{'type': 'story', 'value': ['Story 1', 'Story 2']}}\"",
        ])
