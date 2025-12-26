import json
from pathlib import Path
from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import InstructionDisplayCommand


def update_state_file_with_workspace(workspace_directory: Path, workspace_path: str) -> None:
    state_file = workspace_directory / 'behavior_action_state.json'
    if state_file.exists():
        state_data = json.loads(state_file.read_text())
    else:
        state_data = {}
    state_data['working_directory'] = workspace_path
    state_file.parent.mkdir(parents=True, exist_ok=True)
    state_file.write_text(json.dumps(state_data, indent=2))


class StateCommand(InstructionDisplayCommand):
    @property
    def behavior_names(self):
        return self.bot.behaviors.names if self.bot and self.bot.behaviors else []
    
    def find_behavior(self, behavior_name: str):
        return self.bot.behaviors.find_by_name(behavior_name)
    
    def find_action(self, behavior, action_name: str):
        return behavior.actions.find_by_name(action_name)


class BehaviorCommand(StateCommand):
    @property
    def name(self) -> str:
        return "behavior"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        behavior_name = args.strip()
        if not behavior_name:
            return REPLCommandResponse(
                output="ERROR: No behavior specified",
                response="ERROR: No behavior specified",
                status="error"
            )
        
        behavior = self.find_behavior(behavior_name)
        if not behavior:
            return self.error_behavior_not_found(behavior_name)
        
        if not behavior.actions.names:
            return REPLCommandResponse(
                output=f"ERROR: behavior '{behavior_name}' has no actions",
                response=f"ERROR: behavior '{behavior_name}' has no actions",
                status="error"
            )
        
        first_action_name = behavior.actions.names[0]
        self.navigate_to_behavior_action(behavior_name, first_action_name)
        return self.display_navigation()


class ActionCommand(StateCommand):
    @property
    def name(self) -> str:
        return "action"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        action_name = args.strip()
        if not action_name:
            return REPLCommandResponse(
                output="ERROR: No action specified",
                response="ERROR: No action specified",
                status="error"
            )
        
        if not self.has_current_behavior:
            return self.error_no_current_behavior()
        
        behavior = self.current_behavior
        action = self.find_action(behavior, action_name)
        if not action:
            return self.error_action_not_found(action_name)
        
        behavior.actions.navigate_to(action_name)
        return self.display_navigation()


class WorkspaceCommand(StateCommand):
    @property
    def name(self) -> str:
        return "workspace"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        workspace_path = args.strip()
        if not workspace_path:
            return REPLCommandResponse(
                output="ERROR: No workspace path specified",
                response="ERROR: No workspace path specified",
                status="error"
            )
        
        update_state_file_with_workspace(self.session.workspace_directory, workspace_path)
        
        return REPLCommandResponse(
            output=f"OK workspace={workspace_path}",
            response=f"OK workspace={workspace_path}",
            status="success"
        )


class PathCommand(StateCommand):
    @property
    def name(self) -> str:
        return "path"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        workspace_path = args.strip()
        if not workspace_path:
            # If no args, show current path
            current_path = self.session.workspace_directory
            return REPLCommandResponse(
                output=f"Current path: {current_path}",
                response=f"Current path: {current_path}",
                status="success"
            )
        
        update_state_file_with_workspace(self.session.workspace_directory, workspace_path)
        
        return REPLCommandResponse(
            output=f"OK path={workspace_path}",
            response=f"OK path={workspace_path}",
            status="success"
        )


class ScopeCommand(StateCommand):
    @property
    def name(self) -> str:
        return "scope"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
        
        args = args.strip()
        if not args:
            # Show current scope if no args (same display as banner)
            scope_lines = self.session._get_scope_display_lines()
            if scope_lines:
                output = "\n".join(scope_lines)
                return REPLCommandResponse(
                    output=output,
                    response=output,
                    status="success"
                )
            else:
                return REPLCommandResponse(
                    output="No scope set",
                    response="No scope set",
                    status="success"
                )
        
        # Handle "all" - clears the scope filter
        if args.lower() == 'all':
            self.session.clear_scope()
            return REPLCommandResponse(
                output="Scope filter cleared",
                response="Scope filter cleared",
                status="success"
            )
        
        if args.startswith(('file:', 'files:')):
            prefix = args.split(':', 1)[0].strip().lower()
            value_part = args.split(':', 1)[1].strip()
            scope_values_raw = [v.strip() for v in value_part.split(',') if v.strip()]
            scope_type = ScopeType.FILES
            scope_value = scope_values_raw
        else:
            scope_type = ScopeType.STORY
            scope_values_raw = [v.strip() for v in args.split(',') if v.strip()]
            scope_value = scope_values_raw
        
        scope = Scope(type=scope_type, value=scope_value)
        self.session.store_scope_parameters(scope)
        
        # Get the scope display lines (same as banner)
        scope_lines = self.session._get_scope_display_lines()
        output = "\n".join(scope_lines)
        
        return REPLCommandResponse(
            output=output,
            response=output,
            status="success",
            scope_stored=True
        )

