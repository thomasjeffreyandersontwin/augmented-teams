from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.base import REPLCommand


class MetaCommand(REPLCommand):
    """Base for meta commands - provides access to help and status resources."""
    
    @property
    def help_resource(self):
        return self.session.help
    
    @property
    def status_resource(self):
        return self.session.status


class HelpCommand(MetaCommand):
    @property
    def name(self) -> str:
        return "help"
    
    @property
    def takes_args(self) -> bool:
        return True
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        args = args.strip()
        
        if not args:
            output = self.help_resource.main_help
        else:
            if not self.has_current_behavior:
                return self.error_no_current_behavior()
            action_help = self.help_resource.action_help(self.current_behavior_name, args)
            if not action_help:
                behavior_help = self.help_resource.behavior_help(self.current_behavior_name)
                if not behavior_help:
                    return self.error_behavior_not_found(self.current_behavior_name)
                output = f"ERROR: Action '{args}' not found"
            else:
                output = action_help.help_text
        
        return REPLCommandResponse(output=output, response=output, status="success")


class StatusCommand(MetaCommand):
    @property
    def name(self) -> str:
        return "status"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        state_display = self.session.display_current_state(full=True)
        return REPLCommandResponse(
            output=state_display.output,
            response=state_display.output,
            status="success"
        )


class ExitCommand(MetaCommand):
    @property
    def name(self) -> str:
        return "exit"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        return REPLCommandResponse(
            output="Goodbye!",
            response="Goodbye!",
            status="success",
            repl_terminated=True
        )


class CurrentCommand(MetaCommand):
    @property
    def name(self) -> str:
        return "current"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        
        phase = self.session.action_phase
        if phase in ('not_started', 'instructions_given'):
            return self._execute_instructions()
        elif phase == 'submitted':
            return self._execute_submit()
        return self._execute_instructions()
    
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


class LoopBackCommand(MetaCommand):
    @property
    def name(self) -> str:
        return "no"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        state_display = self.session.display_current_state()
        return REPLCommandResponse(
            output=state_display.output,
            response="Remaining in current action",
            status="success"
        )

