from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.base import REPLCommand


class StateCommand(REPLCommand):
    """Base for state commands - provides access to behavior/action lookup."""
    
    @property
    def behavior_names(self):
        return self.bot.behaviors.names if self.bot and self.bot.behaviors else []
    
    def find_behavior(self, behavior_name: str):
        return self.bot.behaviors.find_by_name(behavior_name)
    
    def find_action(self, behavior, action_name: str):
        return behavior.actions.find_by_name(action_name)
    
    def execute_instructions(self) -> REPLCommandResponse:
        output = "\n".join([
            f"EXECUTING {self.current_behavior_name}.{self.current_action_name}.instructions",
            "",
            "[INSTRUCTIONS]",
            "- Review context and requirements",
            "- Answer key questions",
            "- Provide necessary evidence",
            "",
            "Next: Provide your work using 'submit'."
        ])
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)


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
        
        self.bot.behaviors.navigate_to(behavior_name)
        first_action_name = behavior.actions.names[0]
        behavior.actions.navigate_to(first_action_name)
        return self.execute_instructions()


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
        return self.execute_instructions()


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
        return REPLCommandResponse(
            output=f"OK workspace={workspace_path}",
            response=f"OK workspace={workspace_path}",
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
        args = args.strip()
        if not args:
            return REPLCommandResponse(
                output="ERROR: No scope specified",
                response="ERROR: No scope specified",
                status="error"
            )
        return REPLCommandResponse(
            output="OK scope stored",
            response="OK scope stored",
            status="success",
            scope_stored=True
        )

