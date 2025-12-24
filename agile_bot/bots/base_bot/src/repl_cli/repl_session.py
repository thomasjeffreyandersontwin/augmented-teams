import sys
import json
import re
from pathlib import Path
from typing import Optional, List, Dict, Any

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
from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType


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
    
    def set_action_phase(self, phase: str) -> None:
        """Set the current action's phase in the workflow state."""
        action = self.current_action
        if action and hasattr(action, 'phase'):
            action.phase = phase
        # Also update in state file for persistence
        state_file = self.workspace_directory / 'behavior_action_state.json'
        if state_file.exists():
            import json
            try:
                state_data = json.loads(state_file.read_text())
                state_data['action_phase'] = phase
                state_file.write_text(json.dumps(state_data, indent=2))
            except (json.JSONDecodeError, IOError):
                pass
    
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
        
        # Build just the behaviors/actions menu (header already printed by repl_main.py at startup)
        lines = []
        
        # Show behaviors with marker on current
        current_behavior = self.current_behavior_name
        behavior_names = [b.name for b in self.bot.behaviors] if self.bot and self.bot.behaviors else []
        marked_behaviors = [f"[* {name}]" if name == current_behavior else name for name in behavior_names]
        lines.append("Behaviors: " + " | ".join(marked_behaviors))
        
        # Show actions with marker on current
        current_action = self.current_action_name
        if self.bot and self.bot.behaviors:
            behavior = self.bot.behaviors.current
            if behavior:
                action_names = behavior.actions.names
                marked_actions = [f"[* {name}]" if name == current_action else name for name in action_names]
                lines.append("Actions: " + " | ".join(marked_actions))
        
        lines.append("  status        - Show workflow progress")
        lines.append("  back          - Return to previous action")
        lines.append("  current       - Re-execute current operation")
        lines.append("  next          - Advance to next action")
        lines.append("  help          - Show detailed help")
        lines.append("  exit          - Exit CLI")
        lines.append("")
        lines.append("Type 'instructions' to see instructions for this action.")
        
        return REPLStateDisplay(
            output="\n".join(lines),
            state_loaded=True,
            current_behavior=self.current_behavior_state,
            current_action=self.current_action_state,
            breadcrumbs=self.status.breadcrumbs
        )
    
    def get_context_header_for_ai(self) -> str:
        """Build context header showing current position with markers for AI display.
        
        This header should be displayed to the user after showing instructions.
        """
        if not self.has_current_action:
            return ""
        
        lines = []
        lines.append("")
        lines.append("=" * 60)
        
        # Get bot name from bot_directory
        if self.bot and hasattr(self.bot, 'bot_paths'):
            bot_name = self.bot.bot_paths.bot_directory.name
        else:
            bot_name = 'UNKNOWN'
        lines.append(f"{bot_name.upper()} CLI")
        lines.append("-" * 60)
        
        if self.bot:
            bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
            lines.append(f"Bot Path: {bot_path}")
        lines.append(f"Work Path: {self.workspace_directory}")
        lines.append(self.get_progress_line())
        lines.append("=" * 60)
        
        # Show behaviors with marker on current
        current_behavior = self.current_behavior_name
        behavior_names = [b.name for b in self.bot.behaviors] if self.bot and self.bot.behaviors else []
        marked_behaviors = [f"[* {name}]" if name == current_behavior else name for name in behavior_names]
        lines.append("Behaviors: " + " | ".join(marked_behaviors))
        
        # Show actions with marker on current
        current_action = self.current_action_name
        if self.bot and self.bot.behaviors:
            behavior = self.bot.behaviors.current
            if behavior:
                action_names = behavior.actions.names
                marked_actions = [f"[* {name}]" if name == current_action else name for name in action_names]
                lines.append("Actions: " + " | ".join(marked_actions))
        
        lines.append("  status        - Show workflow progress")
        lines.append("  back          - Return to previous action")
        lines.append("  current       - Re-execute current operation")
        lines.append("  next          - Advance to next action")
        lines.append("  help          - Show detailed help")
        lines.append("  exit          - Exit CLI")
        
        return "\n".join(lines)
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        if not command:
            return REPLCommandResponse(output="", response="", status="empty")
        
        # Check for dot notation: first word must contain a dot (behavior.action format)
        # Avoid false positives from dots in arguments like "*.pyc" or file paths
        first_word = command.split()[0] if command.split() else ""
        if '.' in first_word and not first_word.startswith('--'):
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
        
        behavior = self.bot.behaviors.find_by_name(command_verb)
        if behavior:
            return self._commands["behavior"].execute(command_verb)
        
        return REPLCommandResponse(
            output=f"ERROR: Unknown command '{command_verb}'",
            response=f"ERROR: Unknown command '{command_verb}'",
            status="error"
        )
    
    def _handle_action_shortcut(self, action_name: str, args_str: str) -> REPLCommandResponse:
        args_str = args_str.strip()
        
        # Parse CLI-style arguments (--message, --scope, etc.)
        cli_args = []
        subcommand = None
        
        if args_str:
            if args_str.startswith('--'):
                cli_args = self._tokenize_cli_args(args_str)
            else:
                parts = args_str.split(maxsplit=1)
                subcommand = parts[0].lower()
                if len(parts) > 1 and parts[1].startswith('--'):
                    cli_args = self._tokenize_cli_args(parts[1])
        
        if not subcommand:
            phase_map = {'not_started': 'instructions', 'instructions_given': 'submit', 'submitted': 'confirm'}
            subcommand = phase_map.get(self.action_phase, 'instructions')
        
        if subcommand in ("instructions", "run", "execute") or cli_args:
            operation = "instructions" if subcommand == "instructions" else None
            return self._execute_action_with_args(action_name, cli_args, operation=operation)
        
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
    
    def _tokenize_cli_args(self, args_str: str) -> list:
        """Tokenize CLI-style arguments, handling quoted strings."""
        import shlex
        try:
            return shlex.split(args_str)
        except ValueError:
            return args_str.split()
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
        """Execute action with parsed CLI arguments."""
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
        
        # Parse CLI args into context if provided
        context = None
        if cli_args:
            try:
                from agile_bot.bots.base_bot.src.cli.cli_context_builder import CliContextBuilder
                builder = CliContextBuilder()
                context = builder.build_context(action, cli_args)
                
                # Store scope if present in context
                if context and hasattr(context, 'scope') and context.scope:
                    self.store_scope_parameters(context.scope)
            except ValueError as e:
                error_msg = str(e)
                # Invalid scope type is a real validation error
                if "Invalid scope type" in error_msg or "invalid_type" in error_msg:
                    return REPLCommandResponse(
                        output=f"ERROR: {error_msg}",
                        response=f"ERROR: {error_msg}",
                        status="error"
                    )
                # Other errors like unknown parameters - just proceed without context
                context = None
            except Exception:
                # Any other parsing errors - proceed without context
                context = None
        
        # Use the display_instructions method from InstructionDisplayCommand
        # Create a temporary command object to access the display method
        from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import InstructionDisplayCommand
        
        class TempInstructionDisplay(InstructionDisplayCommand):
            """Temporary command to access display_instructions method."""
            def name(self):
                return "temp"
            def execute(self, args=""):
                pass
        
        temp_cmd = TempInstructionDisplay(self)
        return temp_cmd.display_instructions(action=action, context=context, operation=operation)
    
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
    
    def parse_command_parameters(self, args: str) -> Dict[str, Any]:
        """Parse --param value and --param "value with spaces" from command args."""
        params = {}
        if not args:
            return params
        
        # Match --param "quoted value" or --param value
        pattern = r'--(\w+(?:-\w+)*)\s+(?:"([^"]*)"|\'([^\']*)\'|(\S+))'
        for match in re.finditer(pattern, args):
            param_name = match.group(1).replace('-', '_')
            value = match.group(2) or match.group(3) or match.group(4)
            params[param_name] = value
        
        return params
    
    def parse_scope_from_string(self, scope_str: str) -> Optional[Scope]:
        """Parse scope JSON/dict string into Scope object."""
        if not scope_str:
            return None
        try:
            # Handle Python-style dict syntax
            data = json.loads(scope_str.replace("'", '"'))
            return Scope.from_dict(data)
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError(f"Invalid scope format: {e}")
    
    def get_stored_scope(self) -> Optional[Dict[str, Any]]:
        """Get scope parameters from behavior action state file."""
        state_file = self._get_state_file_path()
        if not state_file.exists():
            return None
        try:
            state_data = json.loads(state_file.read_text())
            return state_data.get('scope')
        except (json.JSONDecodeError, KeyError):
            return None
    
    def store_scope_parameters(self, scope: Scope) -> None:
        """Store scope parameters in behavior action state file."""
        state_file = self._get_state_file_path()
        if state_file.exists():
            state_data = json.loads(state_file.read_text())
        else:
            state_data = {}
        
        state_data['scope'] = scope.to_dict()
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(state_data, indent=2))
    
    def _get_state_file_path(self) -> Path:
        """Get the path to behavior_action_state.json."""
        return self.workspace_directory / 'behavior_action_state.json'
