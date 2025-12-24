import dataclasses
from typing import List, Optional
from dataclasses import dataclass


@dataclass
class ActionDescription:
    name: str
    description: str


@dataclass
class CommandExample:
    pattern: str
    description: str


class ActionHelp:
    def __init__(self, action, action_name: str):
        self.action = action
        self.action_name = action_name
    
    @property
    def help_text(self) -> str:
        lines = [
            f"## {self.action_name}",
            "",
            "Hierarchy: behavior → action → stage",
            "",
            "Usage:",
            f"  {self.action_name} [instructions|submit|confirm]",
            "",
            "Action Stages (three steps):",
            "",
        ]
        
        for stage in self._stages:
            lines.extend(stage)
        
        lines.extend([
            "Note: Calling action name without stage cycles through: instructions → submit → confirm",
            "",
        ])
        
        if self._context_parameters:
            lines.append("Context Parameters (when confirming):")
            for param in self._context_parameters:
                lines.append(f"  --{param} <value>")
            lines.append("")
        
        return "\n".join(lines)
    
    @property
    def _stages(self) -> List[List[str]]:
        return [
            [
                "  1. instructions",
                "     Request: Get instructions for the action",
                "     Response: Shows instructions, questions to answer, evidence to provide",
                f"     Example: {self.action_name} instructions  (or just: {self.action_name})",
                "",
            ],
            [
                "  2. submit",
                "     Request: Submit answers and evidence",
                "     Response: Shows acknowledgment of submission",
                f"     Example: {self.action_name} submit  (or call {self.action_name} again to cycle)",
                "",
            ],
            [
                "  3. confirm",
                "     Request: Confirm action complete and advance to next",
                "     Response: Auto-executes next action and shows its instructions",
                f"     Example: {self.action_name} confirm  (or call {self.action_name} again to cycle)",
                "",
            ],
        ]
    
    @property
    def _context_parameters(self) -> List[str]:
        if dataclasses.is_dataclass(self.action.context_class):
            return [f.name for f in dataclasses.fields(self.action.context_class)]
        return []


class BehaviorHelp:
    def __init__(self, behavior):
        self.behavior = behavior
    
    @property
    def name(self) -> str:
        return self.behavior.name
    
    @property
    def action_names(self) -> List[str]:
        return [a.action_name for a in self.behavior.actions]
    
    @property
    def actions_list(self) -> str:
        lines = [f"Available Actions for behavior: {self.name}"]
        for name in self.action_names:
            lines.append(f"  {name}")
        return "\n".join(lines)
    
    def action(self, action_name: str) -> Optional[ActionHelp]:
        for action in self.behavior.actions._actions:
            if action.action_name == action_name:
                return ActionHelp(action, action_name)
        return None


class REPLHelp:
    def __init__(self, bot):
        self.bot = bot
    
    @property
    def behavior_names(self) -> List[str]:
        if not self.bot or not self.bot.behaviors:
            return []
        return [b.name for b in self.bot.behaviors]
    
    @property
    def action_descriptions(self) -> List[ActionDescription]:
        return [
            ActionDescription("clarify", "Gather context and answer key questions"),
            ActionDescription("strategy", "Plan the approach for this behavior"),
            ActionDescription("build", "Execute the main work of this behavior"),
            ActionDescription("validate", "Verify work meets requirements"),
            ActionDescription("render", "Generate final outputs and artifacts"),
        ]
    
    @property
    def command_examples(self) -> List[CommandExample]:
        return [
            CommandExample(".", "Execute current behavior.action.operation"),
            CommandExample("behavior", "e.g., shape - jump to behavior and execute first action.operation"),
            CommandExample("action", "e.g., build - jump to action and execute first operation"),
            CommandExample("operation", "e.g., submit - jump to operation and execute"),
            CommandExample("behavior.action", "e.g., shape.build - jump to behavior.action and execute first operation"),
            CommandExample("behavior.action.operation", "e.g., shape.build.submit - jump and execute"),
        ]
    
    @property
    def other_commands(self) -> List[CommandExample]:
        return [
            CommandExample("status", "Show full workflow hierarchy"),
            CommandExample("back", "Go back to previous action"),
            CommandExample("current", "Re-execute current operation"),
            CommandExample("next", "Advance to next action"),
            CommandExample("help", "Show this help"),
            CommandExample("exit", "Exit CLI"),
        ]
    
    @property
    def main_help(self) -> str:
        behaviors_list = " | ".join(self.behavior_names)
        
        lines = [
            "Core Commands:",
            "  [behavior][.action][.operation]  - Navigate workflow and perform current",
            "",
            "  Available Components:",
            f"    behaviors   -> {behaviors_list}",
            "",
            "    actions:"
        ]
        
        for action in self.action_descriptions:
            lines.append(f"      {action.name:12} - {action.description}")
        
        lines.extend([
            "",
            "    operations  -> instructions | submit | confirm",
            "",
            "  Examples:"
        ])
        
        for example in self.command_examples:
            lines.append(f"    {example.pattern:27} -> {example.description}")
        
        lines.append("")
        lines.append("  Other Commands:")
        
        for cmd in self.other_commands:
            lines.append(f"    {cmd.pattern:11} - {cmd.description}")
        
        return "\n".join(lines)
    
    def behavior_help(self, behavior_name: str) -> Optional[BehaviorHelp]:
        behavior = self.bot.behaviors.find_by_name(behavior_name)
        if not behavior:
            return None
        return BehaviorHelp(behavior)
    
    def action_help(self, behavior_name: str, action_name: str) -> Optional[ActionHelp]:
        bh = self.behavior_help(behavior_name)
        if not bh:
            return None
        return bh.action(action_name)
