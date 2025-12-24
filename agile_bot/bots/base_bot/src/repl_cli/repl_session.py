import sys
from pathlib import Path
from typing import Optional, List

from agile_bot.bots.base_bot.src.repl_cli.repl_results import (
    REPLStateDisplay,
    REPLCommandResponse,
    TTYDetectionResult
)
from agile_bot.bots.base_bot.src.repl_cli.repl_help import REPLHelp
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus
from agile_bot.bots.base_bot.src.repl_cli.repl_commands import (
    register_commands,
    ACTION_SHORTCUTS,
    DotNotationCommand
)


class REPLSession:
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    }
    
    def __init__(self, bot, workspace_directory: Path):
        self.bot = bot
        self.workspace_directory = Path(workspace_directory)
        self.help = REPLHelp(bot)
        self.status = REPLStatus(bot, self)
        self._commands = register_commands(self)
        self._dot_notation_handler = DotNotationCommand(self)
    
    @property
    def current_behavior(self):
        return self.bot.behaviors.current
    
    @property
    def current_action(self):
        behavior = self.current_behavior
        return behavior.actions.current if behavior else None
    
    @property
    def has_current_behavior(self) -> bool:
        return self.current_behavior is not None
    
    @property
    def has_current_action(self) -> bool:
        return self.current_action is not None
    
    @property
    def current_behavior_name(self) -> Optional[str]:
        behavior = self.current_behavior
        return behavior.name if behavior else None
    
    @property
    def current_action_name(self) -> Optional[str]:
        action = self.current_action
        return action.action_name if action else None
    
    @property
    def current_action_state(self) -> Optional[str]:
        if not self.has_current_action:
            return None
        return f"{self.bot.bot_name}.{self.current_behavior_name}.{self.current_action_name}"
    
    @property
    def current_behavior_state(self) -> Optional[str]:
        if not self.has_current_behavior:
            return None
        return f"{self.bot.bot_name}.{self.current_behavior_name}"
    
    @property
    def action_phase(self) -> str:
        action = self.current_action
        if action and hasattr(action, 'phase'):
            return action.phase
        return 'not_started'
    
    @property
    def stage_name(self) -> str:
        return self.STAGE_MAP.get(self.action_phase, self.action_phase)
    
    @property
    def progress_path(self) -> str:
        if not self.has_current_action:
            return ""
        return f"{self.current_behavior_name}.{self.current_action_name}"
    
    @property
    def behavior_names(self) -> List[str]:
        return self.bot.behaviors.names if self.bot and self.bot.behaviors else []
    
    @property
    def completed_action_names(self) -> set:
        behavior = self.current_behavior
        if not behavior:
            return set()
        return {name for name in behavior.actions.names if behavior.actions.is_action_completed(name)}
    
    @property
    def completed_behaviors(self) -> List[str]:
        return self.bot.behaviors.completed_behaviors if self.bot else []
    
    def detect_tty(self) -> TTYDetectionResult:
        tty_detected = sys.stdin.isatty()
        return TTYDetectionResult(
            tty_detected=tty_detected,
            interactive_prompts_enabled=tty_detected
        )
    
    def get_progress_line(self) -> str:
        if not self.has_current_action:
            if not self._initialize_to_first_behavior_action():
                return "No active workflow"
            return self.get_progress_line()
        return f"Progress: {self.progress_path}.{self.stage_name}"
    
    def _initialize_to_first_behavior_action(self) -> bool:
        if not self.bot or not self.bot.behaviors or self.bot.behaviors.is_empty():
            return False
        first_behavior = self.bot.behaviors.first
        if not first_behavior or not first_behavior.actions.names:
            return False
        self.bot.behaviors.navigate_to(first_behavior.name)
        first_behavior.actions.navigate_to(first_behavior.actions.names[0])
        return True
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        if not self.has_current_action:
            if not self._initialize_to_first_behavior_action():
                return REPLStateDisplay(
                    output="No behaviors available\n\n  help          - Show detailed help\n  exit          - Exit REPL",
                    state_loaded=False
                )
            return self.display_current_state(full=full)
        
        breadcrumbs = self.status.breadcrumbs
        output_lines = self.status.full_status if full else self.status.compact_status
        
        return REPLStateDisplay(
            output="\n".join(output_lines),
            state_loaded=True,
            current_behavior=self.current_behavior_state,
            current_action=self.current_action_state,
            breadcrumbs=breadcrumbs
        )
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        if not command:
            return REPLCommandResponse(output="", response="", status="empty")
        
        if '.' in command:
            return self._dot_notation_handler.execute(command)
        
        return self._handle_simple_command(command)
    
    def _handle_simple_command(self, command: str) -> REPLCommandResponse:
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
        
        if command_verb in self._commands:
            cmd = self._commands[command_verb]
            return cmd.execute(command_args) if cmd.takes_args else cmd.execute()
        
        if command_verb in ACTION_SHORTCUTS:
            return self._handle_action_shortcut(command_verb, command_args)
        
        if self.bot.behaviors.find_by_name(command_verb):
            return self._commands["behavior"].execute(command_verb)
        
        return REPLCommandResponse(
            output=f"ERROR: Unknown command '{command_verb}'",
            response=f"ERROR: Unknown command '{command_verb}'",
            status="error"
        )
    
    def _handle_action_shortcut(self, action_name: str, subcommand: str) -> REPLCommandResponse:
        subcommand = subcommand.strip().lower()
        if not subcommand:
            phase_map = {'not_started': 'instructions', 'instructions_given': 'submit', 'submitted': 'confirm'}
            subcommand = phase_map.get(self.action_phase, 'instructions')
        
        if subcommand in ("instructions", "run", "execute"):
            return self._commands["action"].execute(action_name)
        
        if subcommand in ("submit", "confirm"):
            if not self.has_current_behavior:
                return REPLCommandResponse(
                    output="ERROR: No current behavior set. Please select a behavior first.",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            behavior = self.current_behavior
            action = behavior.actions.find_by_name(action_name)
            if not action:
                available = ", ".join(behavior.actions.names) if behavior else ""
                return REPLCommandResponse(
                    output=f"ERROR: action '{action_name}' not found\nAvailable actions: {available}",
                    response=f"ERROR: action '{action_name}' not found",
                    status="error"
                )
            behavior.actions.navigate_to(action_name)
            return self._commands[subcommand].execute()
        
        return REPLCommandResponse(
            output=f"ERROR: Unknown subcommand '{subcommand}'. Use 'instructions', 'submit', or 'confirm'.",
            response=f"ERROR: Unknown subcommand '{subcommand}'",
            status="error"
        )
    
    def display_confirm_prompt(self) -> REPLStateDisplay:
        if not self.has_current_action:
            return REPLStateDisplay(output="ERROR: No current action", state_loaded=False)
        
        behavior = self.current_behavior
        if not behavior:
            return REPLStateDisplay(output="ERROR: behavior not found", state_loaded=False)
        
        next_action = behavior.actions.next()
        next_action_name = next_action.action_name if next_action else "none"
        
        output = "\n".join([
            f"EXECUTED {self.current_behavior_name}.{self.current_action_name}",
            "Results:",
            "[Mock results - not executing real action]",
            f"Continue to next action ({next_action_name})? (y/n/review)"
        ])
        
        return REPLStateDisplay(
            output=output,
            state_loaded=True,
            current_behavior=self.current_behavior_state,
            current_action=self.current_action_state
        )
