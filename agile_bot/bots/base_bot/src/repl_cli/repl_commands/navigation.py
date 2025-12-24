from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.base import REPLCommand


class NavigationCommand(REPLCommand):
    """Base for navigation commands - provides navigation-specific state."""
    
    @property
    def next_action(self):
        behavior = self.current_behavior
        return behavior.actions.next() if behavior else None
    
    @property
    def next_behavior(self):
        return self.bot.behaviors.next()
    
    @property
    def has_more_actions(self) -> bool:
        return self.next_action is not None
    
    @property
    def has_more_behaviors(self) -> bool:
        return self.next_behavior is not None


class NextCommand(NavigationCommand):
    @property
    def name(self) -> str:
        return "next"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        
        behavior = self.current_behavior
        if not behavior:
            return self.error_no_current_behavior()
        
        if self.has_more_actions:
            behavior.actions.navigate_to(self.next_action.action_name)
            return self._execute_instructions()
        
        if self.has_more_behaviors:
            next_beh = self.next_behavior
            self.bot.behaviors.navigate_to(next_beh.name)
            if next_beh.actions.names:
                next_beh.actions.navigate_to(next_beh.actions.names[0])
            return self._execute_instructions()
        
        return REPLCommandResponse(
            output="ERROR: Already at last action of last behavior",
            response="ERROR: Already at last action",
            status="error"
        )
    
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


class BackCommand(NavigationCommand):
    @property
    def name(self) -> str:
        return "back"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        
        return REPLCommandResponse(
            output="Back navigation not yet implemented via domain",
            response="Back navigation pending",
            status="error"
        )


class GoCommand(NavigationCommand):
    @property
    def name(self) -> str:
        return "go"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("execute")
        
        output = f"[MOCK] Executing {self.current_action_name}..."
        return REPLCommandResponse(
            output=output, response=output, status="success",
            action=self.current_action_name, context_passed_to_action={}
        )

