from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.base import REPLCommand


class DotNotationCommand(REPLCommand):
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
        
        self.bot.behaviors.navigate_to(behavior_name)
        behavior.actions.navigate_to(action_name)
        return self._execute_instructions()
    
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
        
        self.bot.behaviors.navigate_to(behavior_name)
        behavior.actions.navigate_to(action_name)
        
        if operation == "instructions":
            return self._execute_instructions()
        elif operation == "submit":
            return self._execute_submit()
        return self._execute_confirm()
    
    def _execute_instructions(self) -> REPLCommandResponse:
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
    
    def _execute_submit(self) -> REPLCommandResponse:
        output = "\n".join([
            f"EXECUTING {self.current_behavior_name}.{self.current_action_name}.submit",
            "",
            "[ACKNOWLEDGMENT]",
            "- Answers received",
            "- Evidence recorded",
            "- Ready for confirmation",
            "",
            "Next: Type 'confirm' to mark complete and advance."
        ])
        return REPLCommandResponse(output=output, response=output, status="success", action=self.current_action_name)
    
    def _execute_confirm(self) -> REPLCommandResponse:
        behavior = self.current_behavior
        if not behavior:
            return self.error_no_current_behavior()
        
        behavior.actions.close_current()
        
        if behavior.actions.current:
            return self._execute_instructions()
        
        next_behavior = self.bot.behaviors.next()
        if next_behavior:
            self.bot.behaviors.close_current()
            if next_behavior.actions.names:
                next_behavior.actions.navigate_to(next_behavior.actions.names[0])
            return self._execute_instructions()
        
        return REPLCommandResponse(
            output=f"COMPLETE: {self.current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
            response="COMPLETE: All behaviors finished",
            status="success"
        )

