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
from agile_bot.bots.base_bot.src.repl_cli.cli_bot import CLIBot


class REPLSession:
    STAGE_MAP = {
        'not_started': 'instructions',
        'instructions_given': 'instructions',
        'submitted': 'submitted'
    }
    
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        self.help = REPLHelp(bot)
        self.status = REPLStatus(self.cli_bot, self)
        self._commands = register_commands(self)
        self._dot_notation_handler = DotNotationCommand(self)
    
    @property
    def bot(self):
        return self.cli_bot.domain_bot
    
    @property
    def current_behavior(self):
        return self.cli_bot.behaviors.current
    
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
        return action.name if action else None
    
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
        if action and hasattr(action.domain_action, 'phase'):
            return action.domain_action.phase
        return 'not_started'
    
    def set_action_phase(self, phase: str) -> None:
        action = self.current_action
        if action and hasattr(action.domain_action, 'phase'):
            action.domain_action.phase = phase
        state_file = self.workspace_directory / 'behavior_action_state.json'
        if state_file.exists():
            try:
                state_data = json.loads(state_file.read_text())
                state_data['action_phase'] = phase
                state_file.write_text(json.dumps(state_data, indent=2))
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not update action phase in state file: {e}", file=sys.stderr)
    
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
        
        # Build hierarchical status display
        lines = []
        
        # In piped mode, add piped mode instructions header
        tty_result = self.detect_tty()
        if not tty_result.tty_detected:
            lines.append("=" * 60)
            lines.append("AI AGENT INSTRUCTIONS - PIPED MODE")
            lines.append("=" * 60)
            lines.append("")
        
        # Show hierarchical breadcrumbs
        lines.append(self.status.hierarchical_status)
        
        return REPLStateDisplay(
            output="\n".join(lines),
            state_loaded=True,
            current_behavior=self.current_behavior_state,
            current_action=self.current_action_state,
            breadcrumbs=self.status.breadcrumbs
        )
    
    def get_context_header_for_ai(self) -> str:
        if not self.has_current_action:
            return ""
        
        lines = []
        lines.append("-" * 80)
        
        # Get bot name from bot_directory
        if self.bot and hasattr(self.bot, 'bot_paths'):
            bot_name = self.bot.bot_paths.bot_directory.name
        else:
            bot_name = 'UNKNOWN'
        lines.append(f"{bot_name.upper()} CLI")
        
        # Detect piped mode and add explicit AI instruction
        tty_result = self.detect_tty()
        if not tty_result.tty_detected:
            lines.append("")
            lines.append("*** PIPED MODE DETECTED ***")
            lines.append("This command will EXIT upon processing.")
            lines.append("AI: Please follow ALL instructions below.")
            lines.append("")
        
        if self.bot:
            bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
            lines.append(f"Bot Path: {bot_path}")
        lines.append(f"Work Path: {self.workspace_directory}")
        lines.append(self.get_progress_line())
        
        # Show hierarchical breadcrumbs
        lines.append(self.status.hierarchical_status)
        
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
        import shlex
        try:
            return shlex.split(args_str)
        except ValueError:
            return args_str.split()
    
    def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
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
        
        from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import InstructionDisplayCommand
        
        class TempInstructionDisplay(InstructionDisplayCommand):
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
        if not scope_str:
            return None
        try:
            data = json.loads(scope_str.replace("'", '"'))
            return Scope.from_dict(data)
        except (json.JSONDecodeError, ValueError) as e:
            raise ValueError(f"Invalid scope format: {e}")
    
    def get_stored_scope(self) -> Optional[Dict[str, Any]]:
        state_file = self._get_state_file_path()
        if not state_file.exists():
            return None
        try:
            state_data = json.loads(state_file.read_text())
            return state_data.get('scope')
        except (json.JSONDecodeError, KeyError):
            return None
    
    def store_scope_parameters(self, scope: Scope) -> None:
        state_file = self._get_state_file_path()
        if state_file.exists():
            state_data = json.loads(state_file.read_text())
        else:
            state_data = {}
        
        state_data['scope'] = scope.to_dict()
        state_file.parent.mkdir(parents=True, exist_ok=True)
        state_file.write_text(json.dumps(state_data, indent=2))
    
    def clear_scope(self) -> None:
        state_file = self._get_state_file_path()
        if state_file.exists():
            state_data = json.loads(state_file.read_text())
            if 'scope' in state_data:
                del state_data['scope']
                state_file.write_text(json.dumps(state_data, indent=2))
    
    def _get_scope_display_lines(self) -> List[str]:
        scope_data = self.get_stored_scope()
        if not scope_data:
            return []
        
        lines = []
        scope_type = scope_data.get('type', 'unknown')
        scope_value = scope_data.get('value', [])
        
        # Show the scope filter value
        filter_str = ', '.join(scope_value) if isinstance(scope_value, list) else str(scope_value)
        lines.append(f"Scope Filter: {filter_str}")
        
        if scope_type == 'story':
            story_graph_path = self.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
            if story_graph_path.exists():
                graph_data = json.loads(story_graph_path.read_text(encoding='utf-8'))
                matched_items = self._find_scope_matches(graph_data, scope_value)
                for item in matched_items:
                    lines.append(item)
            else:
                for item in (scope_value if isinstance(scope_value, list) else [scope_value]):
                    lines.append(f"  - {item}")
        else:
            if isinstance(scope_value, list):
                for item in scope_value:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"  - {scope_value}")
        
        return lines
    
    def _find_scope_matches(self, graph_data: Dict[str, Any], scope_values: List[str]) -> List[str]:
        lines = []
        epics = graph_data.get('epics', [])
        
        for scope_val in scope_values:
            match_lines = self._search_for_scope_match(epics, scope_val)
            if match_lines:
                lines.extend(match_lines)
            else:
                lines.append(f"  - {scope_val} (no match)")
        
        return lines
    
    def _search_for_scope_match(self, epics: List[Dict], scope_val: str) -> Optional[List[str]]:
        for epic in epics:
            if self._matches_name(epic.get('name', ''), scope_val):
                return self._format_node_with_children(epic, 'epic', 0)
            
            match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
            if match_lines:
                return match_lines
        
        return None
    
    def _search_sub_epics(self, sub_epics: List[Dict], scope_val: str) -> Optional[List[str]]:
        for sub_epic in sub_epics:
            if self._matches_name(sub_epic.get('name', ''), scope_val):
                return self._format_node_with_children(sub_epic, 'sub epic', 0)
            
            match_lines = self._search_stories(sub_epic, scope_val)
            if match_lines:
                return match_lines
        
        return None
    
    def _search_stories(self, sub_epic: Dict, scope_val: str) -> Optional[List[str]]:
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                if self._matches_name(story.get('name', ''), scope_val):
                    return self._format_node_with_children(story, 'story', 0)
        
        for story in sub_epic.get('stories', []):
            if self._matches_name(story.get('name', ''), scope_val):
                return self._format_node_with_children(story, 'story', 0)
        
        return None
    
    def _matches_name(self, name: str, pattern: str) -> bool:
        return pattern.lower() in name.lower()
    
    def _format_node_with_children(self, node: Dict[str, Any], node_type: str, indent: int) -> List[str]:
        lines = []
        prefix = "  " * indent
        name = node.get('name', 'Unknown')
        lines.append(f"{prefix}[{node_type}] {name}")
        
        # Don't recurse into stories - stop at story level
        if node_type == 'story':
            return lines
        
        # Add sub_epics (features)
        for sub_epic in node.get('sub_epics', []):
            lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
        
        # Add stories from story_groups
        for story_group in node.get('story_groups', []):
            for story in story_group.get('stories', []):
                lines.extend(self._format_node_with_children(story, 'story', indent + 1))
        
        # Add direct stories (some structures have this)
        for story in node.get('stories', []):
            lines.extend(self._format_node_with_children(story, 'story', indent + 1))
        
        return lines
    
    def _get_state_file_path(self) -> Path:
        return self.workspace_directory / 'behavior_action_state.json'
