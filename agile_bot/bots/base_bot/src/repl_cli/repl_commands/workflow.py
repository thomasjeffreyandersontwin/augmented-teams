from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.base import REPLCommand


class WorkflowCommand(REPLCommand):
    """Base for workflow commands - provides action phase/state properties."""
    
    @property
    def action_phase(self) -> str:
        return self.session.action_phase
    
    @property
    def is_submitted(self) -> bool:
        return self.action_phase == 'submitted'
    
    @property
    def is_instructions_given(self) -> bool:
        return self.action_phase == 'instructions_given'
    
    @property
    def is_not_started(self) -> bool:
        return self.action_phase == 'not_started'
    
    @property
    def can_submit(self) -> bool:
        return self.action_phase in ('not_started', 'instructions_given')
    
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


class InstructionsCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "instructions"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("get instructions for")
        return self.execute_instructions()


class SubmitCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "submit"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("submit for")
        
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


class ConfirmCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "confirm"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("confirm")
        
        behavior = self.current_behavior
        if not behavior:
            return self.error_no_current_behavior()
        
        behavior.actions.close_current()
        
        if behavior.actions.current:
            return self.execute_instructions()
        
        next_behavior = self.bot.behaviors.next()
        if next_behavior:
            self.bot.behaviors.close_current()
            if next_behavior.actions.names:
                next_behavior.actions.navigate_to(next_behavior.actions.names[0])
            return self.execute_instructions()
        
        return REPLCommandResponse(
            output=f"COMPLETE: {self.current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
            response="COMPLETE: All behaviors finished",
            status="success"
        )

