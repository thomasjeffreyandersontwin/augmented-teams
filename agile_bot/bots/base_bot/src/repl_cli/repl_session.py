import json
import sys
from pathlib import Path
from typing import Optional, Dict, List
from datetime import datetime

from agile_bot.bots.base_bot.src.repl_cli import (
    REPLStateDisplay,
    REPLCommandResponse,
    TTYDetectionResult
)


class REPLSession:
    
    def __init__(self, bot, workspace_directory: Path):
        self.bot = bot
        self.workspace_directory = Path(workspace_directory)
        self.state_file = workspace_directory / 'behavior_action_state.json'
        self.current_state = self._load_state()
    
    def _load_state(self) -> Optional[Dict]:
        if not self.state_file.exists():
            return None
        try:
            return json.loads(self.state_file.read_text(encoding='utf-8'))
        except Exception:
            return None
    
    def _save_state(self, state_data: Dict) -> None:
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps(state_data, indent=2), encoding='utf-8')
        self.current_state = state_data
    
    def detect_tty(self) -> TTYDetectionResult:
        tty_detected = sys.stdin.isatty()
        return TTYDetectionResult(
            tty_detected=tty_detected,
            interactive_prompts_enabled=tty_detected
        )
    
    def get_progress_line(self) -> str:
        """Get just the progress line for display in header"""
        if self.current_state is None:
            self.current_state = self._load_state()
        
        if self.current_state is None:
            # Initialize to first behavior/action/operation
            if self.bot and self.bot.behaviors and len(self.bot.behaviors._behaviors) > 0:
                first_behavior = self.bot.behaviors._behaviors[0]
                first_action = first_behavior.actions._actions[0] if first_behavior.actions._actions else None
                
                if first_action:
                    state_data = {
                        'current_behavior': f'{self.bot.bot_name}.{first_behavior.name}',
                        'current_action': f'{self.bot.bot_name}.{first_behavior.name}.{first_action.action_name}',
                        'action_phase': 'not_started',
                        'working_directory': str(self.workspace_directory),
                        'completed_actions': [],
                        'completed_behaviors': []
                    }
                    self._save_state(state_data)
                    self.current_state = state_data
                    # Now get the progress line from the initialized state
                    return self.get_progress_line()
            
            # Fallback
            return "No active workflow"
        
        current_action = self.current_state.get('current_action', '')
        action_phase = self.current_state.get('action_phase', 'not_started')
        
        # Map action_phase to stage name
        stage_map = {
            'not_started': 'instructions',
            'instructions_given': 'instructions',
            'submitted': 'submitted'
        }
        stage_name = stage_map.get(action_phase, action_phase)
        
        # Remove bot name prefix from current_action for cleaner display
        progress_path = current_action.split('.', 1)[1] if '.' in current_action else current_action
        
        return f"Progress: {progress_path}.{stage_name}"
    
    def display_current_state(self, full=False) -> REPLStateDisplay:
        if self.current_state is None:
            # Initialize to first behavior, first action, first operation
            if self.bot and self.bot.behaviors and len(self.bot.behaviors._behaviors) > 0:
                first_behavior = self.bot.behaviors._behaviors[0]
                first_action = first_behavior.actions._actions[0] if first_behavior.actions._actions else None
                
                if first_action:
                    full_behavior = f"{self.bot.bot_name}.{first_behavior.name}"
                    full_action = f"{full_behavior}.{first_action.action_name}"
                    
                    state_data = {
                        'current_behavior': full_behavior,
                        'current_action': full_action,
                        'action_state': 'not_started',
                        'action_phase': 'not_started',
                        'working_directory': str(self.workspace_directory),
                        'timestamp': datetime.now().isoformat(),
                        'completed_actions': [],
                        'completed_behaviors': []
                    }
                    self._save_state(state_data)
                    self.current_state = state_data
                    # Now display the initialized state
                    return self.display_current_state(full=full)
            
            # Fallback if no behaviors available
            output_lines = [
                "No behaviors available",
                "",
                "  help          - Show detailed help",
                "  exit          - Exit REPL"
            ]
            return REPLStateDisplay(
                output="\n".join(output_lines),
                state_loaded=False
            )
        
        current_behavior = self.current_state.get('current_behavior', '')
        current_action = self.current_state.get('current_action', '')
        working_dir = self.current_state.get('working_directory', '')
        action_phase = self.current_state.get('action_phase', 'not_started')
        
        behavior_name = current_behavior.split('.')[-1] if current_behavior else None
        action_name = current_action.split('.')[-1] if current_action else None
        
        # Map action_phase to stage name
        stage_map = {
            'not_started': 'instructions',
            'instructions_given': 'instructions',
            'submitted': 'submitted'
        }
        stage_name = stage_map.get(action_phase, action_phase)
        
        breadcrumbs = self._generate_breadcrumbs(behavior_name, action_name)
        
        output_lines = []
        
        # Show full hierarchy if requested (for status command)
        if full:
            # Remove bot name prefix from current_action for cleaner display
            progress_path = current_action.split('.', 1)[1] if '.' in current_action else current_action
            
            # Add progress section for status command
            output_lines.append(f"Progress: {progress_path}.{stage_name}")
            
            # Get completed behaviors from state
            completed_behaviors = self.current_state.get('completed_behaviors', [])
            
            # Level 1: Show all behaviors in horizontal flow
            if self.bot and self.bot.behaviors:
                behavior_parts = []
                current_behavior_obj = None
                
                for behavior_obj in self.bot.behaviors:
                    behavior_obj_name = behavior_obj.name
                    
                    if behavior_obj_name in completed_behaviors:
                        behavior_parts.append(f"{behavior_obj_name} [OK]")
                    elif behavior_obj_name == behavior_name:
                        behavior_parts.append(f"{behavior_obj_name} [*]")
                        current_behavior_obj = behavior_obj
                    else:
                        behavior_parts.append(f"{behavior_obj_name} [ ]")
                
                output_lines.append("Behaviors: " + " -> ".join(behavior_parts))
                
                # Level 2: Show actions for current behavior
                if current_behavior_obj:
                    completed_action_names = []
                    completed_actions = self.current_state.get('completed_actions', [])
                    for completed in completed_actions:
                        action_state = completed.get('action_state', '')
                        action_only = action_state.split('.')[-1] if action_state else ''
                        if action_only:
                            completed_action_names.append(action_only)
                    
                    action_parts = []
                    for action_obj in current_behavior_obj.actions._actions:
                        action_name_str = action_obj.action_name
                        
                        if action_name_str in completed_action_names:
                            action_parts.append(f"{action_name_str} [OK]")
                        elif action_name_str == action_name:
                            action_parts.append(f"{action_name_str} [*]")
                        else:
                            action_parts.append(f"{action_name_str} [ ]")
                    
                    output_lines.append("  Actions: " + " -> ".join(action_parts))
                    
                    # Level 3: Show operations for current action
                    if action_name:
                        operation_parts = []
                        if stage_name == 'instructions':
                            operation_parts = ["instructions [*]", "submit [ ]", "confirm [ ]"]
                        elif stage_name == 'submitted':
                            operation_parts = ["instructions [OK]", "submit [*]", "confirm [ ]"]
                        elif stage_name == 'not started':
                            operation_parts = ["instructions [ ]", "submit [ ]", "confirm [ ]"]
                        
                        if operation_parts:
                            output_lines.append("    Operations: " + " -> ".join(operation_parts))
            
            # Add legend
            output_lines.append("")
            output_lines.append("[*] current  [OK] done  [ ] not started")
        else:
            # Compact view - show behaviors and actions lists
            output_lines.append("")
            
            # Show behaviors list
            if self.bot and self.bot.behaviors:
                behavior_names = [b.name for b in self.bot.behaviors]
                output_lines.append("Behaviors: " + " | ".join(behavior_names))
            
            # Show actions list (standard actions for all behaviors)
            output_lines.append("Actions: clarify | strategy | build | validate | render")
            
            output_lines.append("")
            output_lines.append("  status        - Show workflow progress")
            output_lines.append("  back          - Return to previous action")
            output_lines.append("  current       - Re-execute current operation")
            output_lines.append("  next          - Advance to next action")
            output_lines.append("  help          - Show detailed help")
            output_lines.append("  exit          - Exit CLI")
        
        return REPLStateDisplay(
            output="\n".join(output_lines),
            state_loaded=True,
            current_behavior=current_behavior,
            current_action=current_action,
            breadcrumbs=breadcrumbs
        )
    
    def _generate_breadcrumbs(self, behavior_name: Optional[str], current_action_name: Optional[str]) -> str:
        if not behavior_name:
            return ""
        
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return ""
        
        completed_actions = self.current_state.get('completed_actions', []) if self.current_state else []
        completed_action_names = set()
        
        behavior_prefix = f"{self.bot.bot_name}.{behavior_name}."
        for completed in completed_actions:
            action_state = completed.get('action_state', '')
            if action_state.startswith(behavior_prefix):
                completed_action_names.add(action_state.split('.')[-1])
        
        breadcrumb_parts = []
        for action in behavior.actions:
            action_name = action.action_name
            if action_name in completed_action_names:
                breadcrumb_parts.append(f"{action_name} [OK]")
            elif action_name == current_action_name:
                breadcrumb_parts.append(f"{action_name}*")
            else:
                breadcrumb_parts.append(action_name)
        
        return " -> ".join(breadcrumb_parts)
    
    def _get_behavior(self, behavior_name: str):
        return self.bot.behaviors.find_by_name(behavior_name)
    
    def read_and_execute_command(self, command: str) -> REPLCommandResponse:
        command = command.strip()
        
        if not command:
            return REPLCommandResponse(
                output="",
                response="",
                status="empty"
            )
        
        # Handle dot notation: behavior.action or behavior.action.operation
        if '.' in command:
            dot_parts = command.split('.')
            if len(dot_parts) == 2:
                # behavior.action
                behavior_name, action_name = dot_parts
                behavior = self._get_behavior(behavior_name)
                if behavior:
                    action = self._find_action(behavior, action_name)
                    if action:
                        # Navigate to behavior.action and execute instructions
                        full_action = f"{self.bot.bot_name}.{behavior_name}.{action_name}"
                        return self._update_state_and_generate_response(behavior_name, action_name, full_action)
                    else:
                        return REPLCommandResponse(
                            output=f"ERROR: Action '{action_name}' not found in behavior '{behavior_name}'",
                            response=f"ERROR: Action '{action_name}' not found",
                            status="error"
                        )
                else:
                    return REPLCommandResponse(
                        output=f"ERROR: Behavior '{behavior_name}' not found",
                        response=f"ERROR: Behavior '{behavior_name}' not found",
                        status="error"
                    )
            elif len(dot_parts) == 3:
                # behavior.action.operation
                behavior_name, action_name, operation = dot_parts
                behavior = self._get_behavior(behavior_name)
                if behavior:
                    action = self._find_action(behavior, action_name)
                    if action:
                        # Navigate to behavior.action first
                        full_action = f"{self.bot.bot_name}.{behavior_name}.{action_name}"
                        self._navigate_to_action(behavior_name, action_name, full_action)
                        
                        # Then execute the specific operation
                        if operation == "instructions":
                            return self._execute_action_instructions(action_name)
                        elif operation == "submit":
                            return self._handle_submit_command()
                        elif operation == "confirm":
                            return self._handle_confirm_command()
                        else:
                            return REPLCommandResponse(
                                output=f"ERROR: Unknown operation '{operation}'. Use: instructions, submit, or confirm",
                                response=f"ERROR: Unknown operation '{operation}'",
                                status="error"
                            )
                    else:
                        return REPLCommandResponse(
                            output=f"ERROR: Action '{action_name}' not found in behavior '{behavior_name}'",
                            response=f"ERROR: Action '{action_name}' not found",
                            status="error"
                        )
                else:
                    return REPLCommandResponse(
                        output=f"ERROR: Behavior '{behavior_name}' not found",
                        response=f"ERROR: Behavior '{behavior_name}' not found",
                        status="error"
                    )
        
        parts = command.split(maxsplit=1)
        command_verb = parts[0].lower()
        command_args = parts[1] if len(parts) > 1 else ""
        
        if command_verb == "behavior":
            return self._handle_behavior_command(command_args)
        elif command_verb == "action":
            return self._handle_action_command(command_args)
        elif command_verb == "help":
            return self._handle_help_command(command_args)
        elif command_verb == "status":
            return self._handle_status_command()
        elif command_verb == "current":
            return self._handle_current_command()
        elif command_verb == "exit":
            return self._handle_exit_command()
        elif command_verb == "no":
            return self._handle_loop_back_command()
        elif command_verb == "workspace":
            return self._handle_workspace_command(command_args)
        elif command_verb == "go":
            return self._handle_go_command()
        elif command_verb == "scope":
            return self._handle_scope_command(command_args)
        elif command_verb == "instructions":
            return self._handle_instructions_command()
        elif command_verb == "submit":
            return self._handle_submit_command()
        elif command_verb == "confirm":
            return self._handle_confirm_command()
        elif command_verb == "back":
            return self._handle_back_command()
        elif command_verb == "next":
            return self._handle_next_command()
        elif command_verb == "clarify":
            return self._handle_action_shortcut("clarify", command_args)
        elif command_verb == "strategy":
            return self._handle_action_shortcut("strategy", command_args)
        elif command_verb == "build":
            return self._handle_action_shortcut("build", command_args)
        elif command_verb == "validate":
            return self._handle_action_shortcut("validate", command_args)
        elif command_verb == "render":
            return self._handle_action_shortcut("render", command_args)
        else:
            # Check if it's a behavior name (allow behavior name as shortcut)
            behavior = self._get_behavior(command_verb)
            if behavior:
                return self._handle_behavior_command(command_verb)
            
            return REPLCommandResponse(
                output=f"ERROR: Unknown command '{command_verb}'",
                response=f"ERROR: Unknown command '{command_verb}'",
                status="error"
            )
    
    def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
        behavior_name = behavior_name.strip()
        
        if not behavior_name:
            return REPLCommandResponse(
                output="ERROR: No behavior specified",
                response="ERROR: No behavior specified",
                status="error"
            )
        
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            available_behaviors = [b.name for b in self.bot.behaviors]
            behaviors_list = ", ".join(available_behaviors)
            output_lines = [
                f"ERROR: behavior '{behavior_name}' not found",
                f"Available behaviors: {behaviors_list}"
            ]
            return REPLCommandResponse(
                output="\n".join(output_lines),
                response=f"ERROR: behavior '{behavior_name}' not found",
                status="error"
            )
        
        actions = behavior.actions._actions
        if not actions:
            return REPLCommandResponse(
                output=f"ERROR: behavior '{behavior_name}' has no actions",
                response=f"ERROR: behavior '{behavior_name}' has no actions",
                status="error"
            )
        
        first_action = actions[0]
        full_behavior = f"{self.bot.bot_name}.{behavior_name}"
        full_action = f"{full_behavior}.{first_action.action_name}"
        
        state_data = {
            'current_behavior': full_behavior,
            'current_action': full_action,
            'action_phase': 'not_started',
            'action_state': 'not_started',
            'working_directory': str(self.workspace_directory),
            'timestamp': datetime.now().isoformat(),
            'completed_actions': []  # Reset when selecting new behavior
        }
        self._save_state(state_data)
        self.current_state = state_data
        
        # Execute the first action's first operation (instructions)
        return self._execute_action_instructions(first_action.action_name)
    
    def _navigate_to_action(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None):
        """Navigate to an action without executing. Updates state only."""
        state_data = dict(self.current_state) if self.current_state else {}
        state_data['current_action'] = full_action
        state_data['action_phase'] = 'not_started'
        state_data['timestamp'] = datetime.now().isoformat()
        
        if state_updates:
            state_data.update(state_updates)
        
        self._save_state(state_data)
        self.current_state = state_data
    
    def _update_state_and_generate_response(self, behavior_name: str, action_name: str, full_action: str, state_updates: Dict = None) -> REPLCommandResponse:
        """Navigate to an action and execute instructions operation."""
        self._navigate_to_action(behavior_name, action_name, full_action, state_updates)
        
        # Execute the action's first operation (instructions)
        return self._execute_action_instructions(action_name)
    
    def _ensure_state_exists(self) -> None:
        if not self.current_state:
            self.current_state = {
                'current_behavior': '',
                'current_action': '',
                'completed_actions': [],
                'timestamp': datetime.now().isoformat()
            }
    
    def _update_and_save_state(self, **fields) -> None:
        self._ensure_state_exists()
        state_data = dict(self.current_state)
        state_data.update(fields)
        state_data['timestamp'] = datetime.now().isoformat()
        self._save_state(state_data)
    
    def _handle_action_command(self, action_name: str) -> REPLCommandResponse:
        action_name = action_name.strip()
        
        if not action_name:
            return REPLCommandResponse(
                output="ERROR: No action specified",
                response="ERROR: No action specified",
                status="error"
            )
        
        if not self.current_state or not self.current_state.get('current_behavior'):
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
        
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return REPLCommandResponse(
                output=f"ERROR: Current behavior '{behavior_name}' not found",
                response=f"ERROR: behavior '{behavior_name}' not found",
                status="error"
            )
        
        action = self._find_action(behavior, action_name)
        if not action:
            available_actions = [a.action_name for a in behavior.actions._actions]
            actions_list = ", ".join(available_actions)
            output_lines = [
                f"ERROR: action '{action_name}' not found in behavior '{behavior_name}'",
                f"Available actions: {actions_list}"
            ]
            return REPLCommandResponse(
                output="\n".join(output_lines),
                response=f"ERROR: action '{action_name}' not found in behavior '{behavior_name}'",
                status="error"
            )
        
        full_action = f"{self.current_state['current_behavior']}.{action_name}"
        return self._update_state_and_generate_response(behavior_name, action_name, full_action)
    
    def _find_action(self, behavior, action_name: str):
        for action in behavior.actions._actions:
            if action.action_name == action_name:
                return action
        return None
    
    def _handle_help_command(self, args: str) -> REPLCommandResponse:
        args = args.strip()
        
        # With no args, always show all available behaviors
        if not args:
            output = self._render_available_behaviors()
        # With args, show detailed help for that action within current behavior
        else:
            if not self.current_state or not self.current_state.get('current_behavior'):
                return REPLCommandResponse(
                    output="ERROR: No current behavior set. Please select a behavior first.",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            
            behavior_name = self.current_state['current_behavior'].split('.')[-1]
            output = self._render_action_parameters(behavior_name, args)
        
        return REPLCommandResponse(
            output=output,
            response=output,
            status="success"
        )
    
    def _render_available_behaviors(self) -> str:
        behavior_names = [b.name for b in self.bot.behaviors]
        behaviors_list = " | ".join(behavior_names)
        
        output_lines = ["Core Commands:"]
        output_lines.append("  [behavior][.action][.operation]  - Navigate workflow and perform current")
        output_lines.append("")
        output_lines.append("  Available Components:")
        output_lines.append(f"    behaviors   -> {behaviors_list}")
        output_lines.append("    actions     -> clarify | strategy | build | validate | render")
        output_lines.append("    operations  -> instructions | submit | confirm")
        output_lines.append("")
        output_lines.append("  Examples:")
        output_lines.append("    .                           -> Execute current behavior.action.operation")
        output_lines.append("    behavior                    -> e.g., shape - jump to behavior and execute first action.operation")
        output_lines.append("    action                      -> e.g., build - jump to action and execute first operation")
        output_lines.append("    operation                   -> e.g., submit - jump to operation and execute")
        output_lines.append("    behavior.action             -> e.g., shape.build - jump to behavior.action and execute first operation")
        output_lines.append("    behavior.action.operation   -> e.g., shape.build.submit - jump and execute")
        output_lines.append("")
        output_lines.append("  Other Commands:")
        output_lines.append("    status      - Show full workflow hierarchy")
        output_lines.append("    back        - Go back to previous action")
        output_lines.append("    current     - Re-execute current operation")
        output_lines.append("    next        - Advance to next action")
        output_lines.append("    help        - Show this help")
        output_lines.append("    exit        - Exit CLI")
        return "\n".join(output_lines)
    
    def _render_behavior_actions(self, behavior_name: str) -> str:
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return f"ERROR: behavior '{behavior_name}' not found"
        
        action_names = [a.action_name for a in behavior.actions._actions]
        output_lines = [f"Available Actions for behavior: {behavior_name}"]
        for action_name in action_names:
            output_lines.append(f"  {action_name}")
        return "\n".join(output_lines)
    
    def _render_action_parameters(self, behavior_name: str, action_name: str) -> str:
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return f"ERROR: behavior '{behavior_name}' not found"
        
        action = self._find_action(behavior, action_name)
        if not action:
            return f"ERROR: Action '{action_name}' not found"
        
        # Extract parameter names from action's context class
        import dataclasses
        output_lines = [
            f"## {action_name}",
            "",
            "Hierarchy: behavior → action → stage",
            "",
            "Usage:",
            f"  {action_name} [instructions|submit|confirm]",
            "",
            "Action Stages (three steps):",
            "",
            "  1. instructions",
            "     Request: Get instructions for the action",
            "     Response: Shows instructions, questions to answer, evidence to provide",
            f"     Example: {action_name} instructions  (or just: {action_name})",
            "",
            "  2. submit",
            "     Request: Submit answers and evidence",
            "     Response: Shows acknowledgment of submission",
            f"     Example: {action_name} submit  (or call {action_name} again to cycle)",
            "",
            "  3. confirm",
            "     Request: Confirm action complete and advance to next",
            "     Response: Auto-executes next action and shows its instructions",
            f"     Example: {action_name} confirm  (or call {action_name} again to cycle)",
            "",
            "Note: Calling action name without stage cycles through: instructions → submit → confirm",
            "",
        ]
        
        # Show context parameters that can be provided
        if dataclasses.is_dataclass(action.context_class):
            params = [f.name for f in dataclasses.fields(action.context_class)]
            if params:
                output_lines.append("Context Parameters (when confirming):")
                for param in params:
                    output_lines.append(f"  --{param} <value>")
                output_lines.append("")
        
        return "\n".join(output_lines)
    
    def _handle_status_command(self) -> REPLCommandResponse:
        state_display = self.display_current_state(full=True)
        return REPLCommandResponse(
            output=state_display.output,
            response=state_display.output,
            status="success"
        )
    
    def _handle_current_command(self) -> REPLCommandResponse:
        """Re-execute the current operation based on action_phase."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        action_phase = self.current_state.get('action_phase', 'not_started')
        
        # Execute the appropriate operation based on current phase
        if action_phase == 'not_started' or action_phase == 'instructions_given':
            # Re-execute instructions
            return self._handle_instructions_command()
        elif action_phase == 'submitted':
            # Re-execute submit
            return self._handle_submit_command()
        else:
            # Default to instructions
            return self._handle_instructions_command()
    
    def _handle_instructions_command(self) -> REPLCommandResponse:
        """Get instructions for current action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action to get instructions for",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action = self.current_state['current_action']
        action_name = current_action.split('.')[-1]
        
        # Execute to get instructions
        return self._execute_action_instructions(action_name)
    
    def _handle_submit_command(self) -> REPLCommandResponse:
        """Submit answers/evidence for current action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action to submit for",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action = self.current_state['current_action']
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        action_name = current_action.split('.')[-1]
        
        # Check if instructions were given
        action_phase = self.current_state.get('action_phase', 'not_started')
        if action_phase == 'not_started':
            return REPLCommandResponse(
                output=f"ERROR: Must get instructions first. Type '{action_name} instructions' or just '{action_name}'",
                response="ERROR: Instructions not received yet",
                status="error"
            )
        
        # Mark as submitted
        self.current_state['action_phase'] = 'submitted'
        self.current_state['timestamp'] = datetime.now().isoformat()
        self._save_state(self.current_state)
        
        output_lines = [
            f"EXECUTING {behavior_name}.{action_name}.submit",
            "",
            "[ACKNOWLEDGMENT]",
            "- Answers received",
            "- Evidence recorded",
            "- Ready for confirmation",
            "",
            f"Next: Type '{action_name} confirm' to mark complete and advance (or just '{action_name}' to continue)"
        ]
        
        return REPLCommandResponse(
            output="\n".join(output_lines),
            response="\n".join(output_lines),
            status="success",
            action=action_name
        )
    
    def _handle_confirm_command(self) -> REPLCommandResponse:
        """Confirm/complete current action and advance to next."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action to confirm",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action_name = self.current_state['current_action'].split('.')[-1]
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return REPLCommandResponse(
                output=f"ERROR: behavior '{behavior_name}' not found",
                response="ERROR: behavior not found",
                status="error"
            )
        
        # Check if work was submitted
        action_phase = self.current_state.get('action_phase', 'not_started')
        if action_phase != 'submitted':
            # Allow confirm anyway for backwards compatibility
            pass
        
        # Mark current action as complete
        completed_actions = self.current_state.get('completed_actions', [])
        completed_actions.append({
            'action_state': self.current_state['current_action'],
            'timestamp': datetime.now().isoformat()
        })
        
        # Get next action
        actions = behavior.actions._actions
        current_index = -1
        for i, action in enumerate(actions):
            if action.action_name == current_action_name:
                current_index = i
                break
        
        is_final_action = current_index >= len(actions) - 1
        
        if is_final_action:
            # This was the final action - mark behavior as complete
            self.current_state['completed_actions'] = completed_actions
            
            # Add behavior to completed_behaviors list
            completed_behaviors = self.current_state.get('completed_behaviors', [])
            if behavior_name not in completed_behaviors:
                completed_behaviors.append(behavior_name)
            self.current_state['completed_behaviors'] = completed_behaviors
            
            self._save_state(self.current_state)
            
            # Find next behavior
            behaviors_list = [b for b in self.bot.behaviors]
            current_behavior_index = -1
            for i, b in enumerate(behaviors_list):
                if b.name == behavior_name:
                    current_behavior_index = i
                    break
            
            # Check if there's a next behavior
            if current_behavior_index >= len(behaviors_list) - 1:
                # No more behaviors - truly complete
                return REPLCommandResponse(
                    output=f"EXECUTING {behavior_name}.{current_action_name}.confirm\n\nCOMPLETE: {behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
                    response=f"COMPLETE: All behaviors finished",
                    status="success"
                )
            else:
                # Proceed to next behavior's first action
                next_behavior = behaviors_list[current_behavior_index + 1]
                next_behavior_name = next_behavior.name
                next_first_action = next_behavior.actions._actions[0]
                next_action_name = next_first_action.action_name
                
                full_behavior = f"{self.bot.bot_name}.{next_behavior_name}"
                full_action = f"{full_behavior}.{next_action_name}"
                
                # Update state to next behavior/action
                self.current_state['current_behavior'] = full_behavior
                self.current_state['current_action'] = full_action
                self.current_state['action_phase'] = 'not_started'
                self.current_state['completed_actions'] = []  # Reset for new behavior
                self._save_state(self.current_state)
                
                # Execute the next behavior's first action's instructions
                return self._execute_action_instructions(next_action_name)
        else:
            # Advance to next action within same behavior
            next_action = actions[current_index + 1]
            new_action_state = f"{self.current_state['current_behavior']}.{next_action.action_name}"
            
            self.current_state['current_action'] = new_action_state
            self.current_state['completed_actions'] = completed_actions
            self.current_state['action_phase'] = 'not_started'  # Reset for new action
            self._save_state(self.current_state)
            
            # Execute the next action's instructions
            return self._execute_action_instructions(next_action.action_name)
    
    def _handle_back_command(self) -> REPLCommandResponse:
        """Stub: Move back to previous action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action_name = self.current_state['current_action'].split('.')[-1]
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        completed_actions = self.current_state.get('completed_actions', [])
        
        if not completed_actions:
            # At first action of current behavior - try to move to previous behavior
            completed_behaviors = self.current_state.get('completed_behaviors', [])
            
            if not completed_behaviors:
                # No previous behaviors
                return REPLCommandResponse(
                    output=f"ERROR: Already at first action of first behavior",
                    response="ERROR: Already at first action",
                    status="error"
                )
            
            # Get previous behavior
            prev_behavior_name = completed_behaviors[-1]
            prev_behavior = self._get_behavior(prev_behavior_name)
            
            if not prev_behavior:
                return REPLCommandResponse(
                    output=f"ERROR: Previous behavior '{prev_behavior_name}' not found",
                    response="ERROR: Previous behavior not found",
                    status="error"
                )
            
            # Remove previous behavior from completed list
            completed_behaviors.pop()
            
            # Move to last action of previous behavior
            prev_actions = prev_behavior.actions._actions
            last_action = prev_actions[-1]
            last_action_name = last_action.action_name
            
            full_behavior = f"{self.bot.bot_name}.{prev_behavior_name}"
            full_action = f"{full_behavior}.{last_action_name}"
            
            # Set up completed_actions to include all but the last action of previous behavior
            new_completed_actions = []
            for i in range(len(prev_actions) - 1):
                action_state = f"{full_behavior}.{prev_actions[i].action_name}"
                new_completed_actions.append({
                    'action_state': action_state,
                    'timestamp': datetime.now().isoformat()
                })
            
            # Update state to previous behavior/action
            self.current_state['current_behavior'] = full_behavior
            self.current_state['current_action'] = full_action
            self.current_state['action_phase'] = 'not_started'
            self.current_state['completed_actions'] = new_completed_actions
            self.current_state['completed_behaviors'] = completed_behaviors
            self._save_state(self.current_state)
            
            # Execute the previous behavior's last action's instructions
            return self._execute_action_instructions(last_action_name)
        
        # Move back within same behavior
        # Remove last completed action and make it current
        last_completed = completed_actions.pop()
        new_action_state = last_completed['action_state']
        
        self.current_state['current_action'] = new_action_state
        self.current_state['action_phase'] = 'not_started'
        self.current_state['completed_actions'] = completed_actions
        self._save_state(self.current_state)
        
        new_action_name = new_action_state.split('.')[-1]
        
        # Execute the action's first operation (instructions)
        return self._execute_action_instructions(new_action_name)
    
    def _handle_next_command(self) -> REPLCommandResponse:
        """Move forward to next action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action_name = self.current_state['current_action'].split('.')[-1]
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        
        # Get current behavior
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return REPLCommandResponse(
                output=f"ERROR: Current behavior '{behavior_name}' not found",
                response=f"ERROR: behavior '{behavior_name}' not found",
                status="error"
            )
        
        # Find current action index
        actions = behavior.actions._actions
        current_index = -1
        for i, action in enumerate(actions):
            if action.action_name == current_action_name:
                current_index = i
                break
        
        if current_index == -1:
            return REPLCommandResponse(
                output=f"ERROR: Current action '{current_action_name}' not found in behavior",
                response="ERROR: Current action not found",
                status="error"
            )
        
        # Check if there's a next action in current behavior
        if current_index >= len(actions) - 1:
            # At last action of behavior - try to move to next behavior
            behaviors_list = [b for b in self.bot.behaviors]
            current_behavior_index = -1
            for i, b in enumerate(behaviors_list):
                if b.name == behavior_name:
                    current_behavior_index = i
                    break
            
            # Check if there's a next behavior
            if current_behavior_index >= len(behaviors_list) - 1:
                return REPLCommandResponse(
                    output="ERROR: Already at last action of last behavior",
                    response="ERROR: Already at last action",
                    status="error"
                )
            
            # Mark current action as complete
            completed_actions = self.current_state.get('completed_actions', [])
            completed_actions.append({
                'action_state': self.current_state['current_action'],
                'timestamp': datetime.now().isoformat()
            })
            
            # Mark current behavior as complete
            completed_behaviors = self.current_state.get('completed_behaviors', [])
            if behavior_name not in completed_behaviors:
                completed_behaviors.append(behavior_name)
            
            # Move to next behavior's first action
            next_behavior = behaviors_list[current_behavior_index + 1]
            next_behavior_name = next_behavior.name
            next_first_action = next_behavior.actions._actions[0]
            next_action_name = next_first_action.action_name
            
            full_behavior = f"{self.bot.bot_name}.{next_behavior_name}"
            full_action = f"{full_behavior}.{next_action_name}"
            
            # Update state to next behavior/action
            self.current_state['current_behavior'] = full_behavior
            self.current_state['current_action'] = full_action
            self.current_state['action_phase'] = 'not_started'
            self.current_state['completed_actions'] = []  # Reset for new behavior
            self.current_state['completed_behaviors'] = completed_behaviors
            self._save_state(self.current_state)
            
            # Execute the next behavior's first action's instructions
            return self._execute_action_instructions(next_action_name)
        
        # Move to next action within same behavior
        next_action = actions[current_index + 1]
        next_action_name = next_action.action_name
        full_action = f"{self.current_state['current_behavior']}.{next_action_name}"
        
        # Mark current action as complete
        completed_actions = self.current_state.get('completed_actions', [])
        completed_actions.append({
            'action_state': self.current_state['current_action'],
            'timestamp': datetime.now().isoformat()
        })
        
        # Navigate to next action and execute it
        self.current_state['current_action'] = full_action
        self.current_state['action_phase'] = 'not_started'
        self.current_state['completed_actions'] = completed_actions
        self._save_state(self.current_state)
        
        # Execute the next action's first operation (instructions)
        return self._execute_action_instructions(next_action_name)
    
    def _show_action_confirmation(self, action_name: str) -> REPLCommandResponse:
        """Show confirmation/review prompt for action."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action = self.current_state['current_action']
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        action_name_from_state = current_action.split('.')[-1]
        
        # Check if action is started
        action_state = self.current_state.get('action_state', 'not_started')
        if action_state != 'started':
            return REPLCommandResponse(
                output=f"ERROR: Action '{action_name_from_state}' has not been started yet. Use '{action_name_from_state} instructions' first.",
                response="ERROR: Action not started",
                status="error"
            )
        
        output_lines = [
            f"Action {behavior_name}.{action_name_from_state} is in progress",
            "",
            "Review your work, then:",
            "  confirm                              - Mark complete and advance to next action",
            "  back                                 - Return to previous action",
            f"  {action_name_from_state} instructions  - Re-execute for new instructions"
        ]
        
        return REPLCommandResponse(
            output="\n".join(output_lines),
            response="\n".join(output_lines),
            status="success",
            action=action_name_from_state
        )
    
    def _execute_action_instructions(self, action_name: str) -> REPLCommandResponse:
        """Execute action and get instructions (mock)."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action = self.current_state['current_action']
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        action_name = current_action.split('.')[-1]
        
        # Always execute and get instructions (can be re-run)
        action_phase = self.current_state.get('action_phase', 'not_started')
        
        if action_phase in ['instructions_given', 'submitted']:
            # Re-executing - provide fresh instructions
            output_lines = [
                f"EXECUTING {behavior_name}.{action_name}.instructions",
                "",
                "[INSTRUCTIONS]",
                "- Review context and requirements",
                "- Answer key questions",
                "- Provide necessary evidence",
                "",
                f"Next: Provide your work using 'submit' or '{action_name} submit'."
            ]
        else:
            # First execution - start the action
            self.current_state['action_phase'] = 'instructions_given'
            self.current_state['action_state'] = 'started'  # Keep for backward compat
            self.current_state['timestamp'] = datetime.now().isoformat()
            self._save_state(self.current_state)
            
            output_lines = [
                f"EXECUTING {behavior_name}.{action_name}.instructions",
                "",
                "[INSTRUCTIONS]",
                "- Review context and requirements",
                "- Answer key questions",
                "- Provide necessary evidence",
                "",
                f"Next: Provide your work using 'submit' or '{action_name} submit'."
            ]
        
        return REPLCommandResponse(
            output="\n".join(output_lines),
            response="\n".join(output_lines),
            status="success",
            action=action_name
        )
    
    def display_confirm_prompt(self) -> REPLStateDisplay:
        """Stub: Display confirmation prompt after action execution."""
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLStateDisplay(
                output="ERROR: No current action",
                state_loaded=False
            )
        
        current_action = self.current_state['current_action']
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        action_name = current_action.split('.')[-1]
        
        # Get next action
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return REPLStateDisplay(
                output="ERROR: behavior not found",
                state_loaded=False
            )
        
        actions = behavior.actions._actions
        current_index = -1
        for i, action in enumerate(actions):
            if action.action_name == action_name:
                current_index = i
                break
        
        next_action_name = "none"
        if current_index >= 0 and current_index < len(actions) - 1:
            next_action_name = actions[current_index + 1].action_name
        
        output_lines = [
            f"EXECUTED {behavior_name}.{action_name}",
            "Results:",
            "[Mock results - not executing real action]",
            f"Continue to next action ({next_action_name})? (y/n/review)"
        ]
        
        return REPLStateDisplay(
            output="\n".join(output_lines),
            state_loaded=True,
            current_behavior=self.current_state['current_behavior'],
            current_action=current_action
        )
    
    def _handle_exit_command(self) -> REPLCommandResponse:
        return REPLCommandResponse(
            output="Goodbye!",
            response="Goodbye!",
            status="success",
            repl_terminated=True
        )
    
    def _handle_advance_command(self) -> REPLCommandResponse:
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action to advance from",
                response="ERROR: No current action",
                status="error"
            )
        
        current_action_name = self.current_state['current_action'].split('.')[-1]
        behavior_name = self.current_state['current_behavior'].split('.')[-1]
        
        behavior = self._get_behavior(behavior_name)
        if not behavior:
            return REPLCommandResponse(
                output=f"ERROR: behavior '{behavior_name}' not found",
                response="ERROR: behavior not found",
                status="error"
            )
        
        actions = behavior.actions._actions
        current_index = -1
        for i, action in enumerate(actions):
            if action.action_name == current_action_name:
                current_index = i
                break
        
        if current_index == -1 or current_index >= len(actions) - 1:
            return REPLCommandResponse(
                output="No next action available",
                response="No next action",
                status="success"
            )
        
        next_action = actions[current_index + 1]
        full_action = f"{self.current_state['current_behavior']}.{next_action.action_name}"
        
        completed_actions = self.current_state.get('completed_actions', [])
        completed_actions.append({
            'action_state': self.current_state['current_action'],
            'timestamp': datetime.now().isoformat()
        })
        
        # Check if previous action was started but not completed
        action_state = self.current_state.get('action_state', 'not_started')
        if action_state == 'started':
            return REPLCommandResponse(
                output=f"ERROR: Current action '{current_action_name}' is in progress. Complete it with 'confirm' before advancing.",
                response="ERROR: Action in progress",
                status="error"
            )
        
        # Update state
        self.current_state['current_action'] = full_action
        self.current_state['completed_actions'] = completed_actions
        self.current_state['action_state'] = 'not_started'  # New action starts fresh
        self.current_state['action_phase'] = 'not_started'  # Reset phase
        self.current_state['timestamp'] = datetime.now().isoformat()
        self._save_state(self.current_state)
        
        output_lines = [
            f"OK advancing to {next_action.action_name}",
            f"CURRENT: {full_action}"
        ]
        
        return REPLCommandResponse(
            output="\n".join(output_lines),
            response=f"OK advancing to {next_action.action_name}",
            status="success",
            action=next_action.action_name
        )
    
    def _handle_loop_back_command(self) -> REPLCommandResponse:
        state_display = self.display_current_state()
        return REPLCommandResponse(
            output=state_display.output,
            response="Remaining in current action",
            status="success"
        )
    
    def _handle_workspace_command(self, args: str) -> REPLCommandResponse:
        workspace_path = args.strip()
        
        if not workspace_path:
            return REPLCommandResponse(
                output="ERROR: No workspace path specified",
                response="ERROR: No workspace path specified",
                status="error"
            )
        
        self._update_and_save_state(working_directory=workspace_path)
        
        return REPLCommandResponse(
            output=f"OK workspace={workspace_path}",
            response=f"OK workspace={workspace_path}",
            status="success"
        )
    
    def _handle_go_command(self) -> REPLCommandResponse:
        if not self.current_state or not self.current_state.get('current_action'):
            return REPLCommandResponse(
                output="ERROR: No current action to execute",
                response="ERROR: No current action",
                status="error"
            )
        
        action_name = self.current_state['current_action'].split('.')[-1]
        
        return REPLCommandResponse(
            output=f"[MOCK] Executing {action_name}...",
            response=f"[MOCK] Executing {action_name}...",
            status="success",
            action=action_name,
            context_passed_to_action={}
        )
    
    def _handle_scope_command(self, args: str) -> REPLCommandResponse:
        args = args.strip()
        
        if not args:
            return REPLCommandResponse(
                output="ERROR: No scope specified",
                response="ERROR: No scope specified",
                status="error"
            )
        
        try:
            scope = self._parse_scope(args)
        except Exception as e:
            return REPLCommandResponse(
                output=f"ERROR: Invalid scope format: {str(e)}",
                response=f"ERROR: Invalid scope format",
                status="error"
            )
        
        self._update_and_save_state(scope=scope)
        
        return REPLCommandResponse(
            output=f"OK scope stored",
            response=f"OK scope stored",
            status="success",
            scope_stored=True,
            scope=scope
        )
    
    def _parse_scope(self, args: str) -> Dict:
        if '=' in args:
            parts = args.split('=', 1)
            scope_type = parts[0].strip()
            scope_value = parts[1].strip()
            
            if scope_type == "files":
                return {'type': 'files', 'value': [scope_value]}
            elif scope_type == "story":
                return {'type': 'story', 'value': [scope_value]}
            else:
                return {'type': scope_type, 'value': [scope_value]}
        else:
            return {'type': 'story', 'value': [args]}
    
    def _handle_action_shortcut(self, action_name: str, subcommand: str) -> REPLCommandResponse:
        """Handle action shortcuts like 'clarify instructions', 'clarify submit', or 'clarify confirm'."""
        subcommand = subcommand.strip().lower()
        
        # If no subcommand, cycle through: instructions -> submit -> confirm
        if not subcommand:
            action_phase = self.current_state.get('action_phase', 'not_started')
            if action_phase == 'not_started':
                subcommand = "instructions"
            elif action_phase == 'instructions_given':
                subcommand = "submit"
            elif action_phase == 'submitted':
                subcommand = "confirm"
            else:
                subcommand = "instructions"
        
        # Handle subcommands
        if subcommand == "instructions" or subcommand == "run" or subcommand == "execute":
            # Navigate to action and execute instructions
            return self._handle_action_command(action_name)
        
        elif subcommand == "submit":
            # Navigate to action first
            if not self.current_state or not self.current_state.get('current_behavior'):
                return REPLCommandResponse(
                    output="ERROR: No current behavior set",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            
            behavior_name = self.current_state['current_behavior'].split('.')[-1]
            behavior = self._get_behavior(behavior_name)
            if not behavior:
                return REPLCommandResponse(
                    output=f"ERROR: Current behavior '{behavior_name}' not found",
                    response=f"ERROR: behavior '{behavior_name}' not found",
                    status="error"
                )
            
            action = self._find_action(behavior, action_name)
            if not action:
                available_actions = [a.action_name for a in behavior.actions._actions]
                actions_list = ", ".join(available_actions)
                return REPLCommandResponse(
                    output=f"ERROR: action '{action_name}' not found in behavior '{behavior_name}'\nAvailable actions: {actions_list}",
                    response=f"ERROR: action '{action_name}' not found",
                    status="error"
                )
            
            full_action = f"{self.current_state['current_behavior']}.{action_name}"
            self._navigate_to_action(behavior_name, action_name, full_action)
            
            # Execute submit
            return self._handle_submit_command()
        
        elif subcommand == "confirm":
            # Navigate to action first
            if not self.current_state or not self.current_state.get('current_behavior'):
                return REPLCommandResponse(
                    output="ERROR: No current behavior set",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            
            behavior_name = self.current_state['current_behavior'].split('.')[-1]
            behavior = self._get_behavior(behavior_name)
            if not behavior:
                return REPLCommandResponse(
                    output=f"ERROR: Current behavior '{behavior_name}' not found",
                    response=f"ERROR: behavior '{behavior_name}' not found",
                    status="error"
                )
            
            action = self._find_action(behavior, action_name)
            if not action:
                available_actions = [a.action_name for a in behavior.actions._actions]
                actions_list = ", ".join(available_actions)
                return REPLCommandResponse(
                    output=f"ERROR: action '{action_name}' not found in behavior '{behavior_name}'\nAvailable actions: {actions_list}",
                    response=f"ERROR: action '{action_name}' not found",
                    status="error"
                )
            
            full_action = f"{self.current_state['current_behavior']}.{action_name}"
            self._navigate_to_action(behavior_name, action_name, full_action)
            
            # Execute confirm
            return self._handle_confirm_command()
        
        else:
            return REPLCommandResponse(
                output=f"ERROR: Unknown subcommand '{subcommand}'. Use 'instructions', 'submit', or 'confirm'.\n  {action_name} instructions - Execute action\n  {action_name} submit       - Submit answers/evidence\n  {action_name} confirm      - Mark complete and advance",
                response=f"ERROR: Unknown subcommand '{subcommand}'",
                status="error"
            )
    
    def _handle_action_execution(self, action_name: str, args: str) -> REPLCommandResponse:
        if not self.current_state or not self.current_state.get('current_behavior'):
            return REPLCommandResponse(
                output="ERROR: No current behavior set. Please select a behavior first.",
                response="ERROR: No current behavior set",
                status="error"
            )
        
        return REPLCommandResponse(
            output=f"[MOCK] Executing {action_name}...",
            response=f"[MOCK] Executing {action_name}...",
            status="success",
            action=action_name,
            context_passed_to_action={}
        )

