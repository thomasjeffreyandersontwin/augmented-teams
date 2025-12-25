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
    def __init__(self, bot, session=None):
        self.bot = bot
        self.session = session
    
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
            CommandExample("echo '.' | python repl_main.py", "Execute current behavior.action.operation"),
            CommandExample("echo 'shape' | python repl_main.py", "Jump to behavior and execute first action.operation"),
            CommandExample("echo 'build' | python repl_main.py", "Jump to action and execute first operation"),
            CommandExample("echo 'submit scope=\"s1\"' | python repl_main.py", "Jump to operation with params and execute"),
            CommandExample("echo 'shape.build' | python repl_main.py", "Jump to behavior.action and execute first operation"),
            CommandExample("echo 'shape.build.submit' | python repl_main.py", "Jump to behavior.action.operation and execute"),
        ]
    
    @property
    def other_commands(self) -> List[CommandExample]:
        return [
            CommandExample("echo 'status' | python repl_main.py", "Show full workflow hierarchy"),
            CommandExample("echo 'back' | python repl_main.py", "Go back to previous action"),
            CommandExample("echo 'current' | python repl_main.py", "Re-execute current operation"),
            CommandExample("echo 'next' | python repl_main.py", "Advance to next action"),
            CommandExample("echo 'path [dir]' | python repl_main.py", "Show/set working directory"),
            CommandExample("echo 'scope [filter]' | python repl_main.py", "Show/set/clear scope filter"),
            CommandExample("echo 'help' | python repl_main.py", "Show this help"),
            CommandExample("echo 'exit' | python repl_main.py", "Exit CLI"),
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
        
        # Show actions with their parameter hints
        if self.session and self.session.has_current_behavior:
            behavior = self.session.current_behavior
            for action in behavior.actions._actions:
                action_name = action.action_name
                action_desc = next((a.description for a in self.action_descriptions if a.name == action_name), "")
                
                # Get parameter hints for this action
                instructions_hint = self.session._get_instructions_params_hint(action)
                submit_hint = self.session._get_submit_params_hint(action)
                
                # Combine hints
                hints = []
                if instructions_hint:
                    hints.append(instructions_hint)
                if submit_hint:
                    hints.append(submit_hint)
                
                params_line = " | ".join(hints) if hints else ""
                
                lines.append(f"      {action_name:12} - {action_desc}")
                if params_line:
                    lines.append(f"                     {params_line}")
        else:
            # Fallback if no current behavior
            for action in self.action_descriptions:
                lines.append(f"      {action.name:12} - {action.description}")
        
        lines.append("")
        lines.append("    operations:")
        
        # Show operations with parameter hints if we have a current action
        if self.session and self.session.has_current_action:
            action_obj = self.session.current_action
            instructions_hint = self.session._get_instructions_params_hint(action_obj)
            submit_hint = self.session._get_submit_params_hint(action_obj)
            
            if instructions_hint:
                lines.append(f"      instructions  {instructions_hint}")
            else:
                lines.append(f"      instructions")
            
            if submit_hint:
                lines.append(f"      submit        {submit_hint}")
            else:
                lines.append(f"      submit")
            
            lines.append(f"      confirm")
        else:
            lines.append(f"      instructions  [context, scope, or action-specific params]")
            lines.append(f"      submit        [scope, decisions, assumptions, or action-specific params]")
            lines.append(f"      confirm")
        
        lines.extend([
            "",
            "  Examples:"
        ])
        
        for example in self.command_examples:
            lines.append(f"    {example.pattern:45} -> {example.description}")
        
        lines.append("")
        lines.append("  Other Commands:")
        
        for cmd in self.other_commands:
            lines.append(f"    {cmd.pattern:45} - {cmd.description}")
        
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
