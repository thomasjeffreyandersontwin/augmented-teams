from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.workflow import WorkflowCommand


class DotNotationCommand(WorkflowCommand):
    """Handles dot notation commands like behavior.action or behavior.action.operation."""
    
    VALID_OPERATIONS = {"instructions", "submit", "confirm"}
    
    @property
    def name(self) -> str:
        return "dot_notation"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        dot_parts = args.split('.')
        
        if len(dot_parts) == 2:
            return self._handle_behavior_action(dot_parts[0], dot_parts[1])
        
        if len(dot_parts) == 3:
            return self._handle_behavior_action_operation(dot_parts[0], dot_parts[1], dot_parts[2])
        
        return REPLCommandResponse(
            output=f"ERROR: Invalid dot notation '{args}'",
            response="ERROR: Invalid dot notation",
            status="error"
        )
    
    def _handle_behavior_action(self, behavior_name: str, action_name: str) -> REPLCommandResponse:
        behavior = self.bot.behaviors.find_by_name(behavior_name)
        if not behavior:
            return self.error_behavior_not_found(behavior_name)
        
        action = behavior.actions.find_by_name(action_name)
        if not action:
            return REPLCommandResponse(
                output=f"ERROR: Action '{action_name}' not found in behavior '{behavior_name}'",
                response=f"ERROR: Action '{action_name}' not found",
                status="error"
            )
        
        self.navigate_to_behavior_action(behavior_name, action_name)
        return self.display_navigation()
    
    def _handle_behavior_action_operation(self, behavior_name: str, action_name: str, operation: str) -> REPLCommandResponse:
        behavior = self.bot.behaviors.find_by_name(behavior_name)
        if not behavior:
            return self.error_behavior_not_found(behavior_name)
        
        action = behavior.actions.find_by_name(action_name)
        if not action:
            return REPLCommandResponse(
                output=f"ERROR: Action '{action_name}' not found in behavior '{behavior_name}'",
                response=f"ERROR: Action '{action_name}' not found",
                status="error"
            )
        
        if operation not in self.VALID_OPERATIONS:
            return REPLCommandResponse(
                output=f"ERROR: Unknown operation '{operation}'. Use: instructions, submit, or confirm",
                response=f"ERROR: Unknown operation '{operation}'",
                status="error"
            )
        
        self.navigate_to_behavior_action(behavior_name, action_name)
        
        if operation == "instructions":
            return self.display_instructions()
        elif operation == "submit":
            return self.execute_submit()
        return self.execute_confirm()

