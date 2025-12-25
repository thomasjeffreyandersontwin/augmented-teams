from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import REPLCommand, InstructionDisplayCommand


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
        
        # Wrap with context header (includes Progress line)
        header = self.session.get_context_header_for_ai()
        full_output = f"{output}\n{header}"
        return REPLCommandResponse(output=full_output, response=output, status="success")


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


class CurrentCommand(InstructionDisplayCommand):
    @property
    def name(self) -> str:
        return "current"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        
        # Re-execute current operation based on progress state
        # Progress format is: behavior.action.operation
        progress = self.session.get_progress_line()
        
        # Extract operation from progress (last part after final dot)
        if '.' in progress and 'Progress: ' in progress:
            parts = progress.replace('Progress: ', '').split('.')
            if len(parts) >= 3:
                operation = parts[2]
                
                # Re-execute the current operation
                if operation == 'instructions':
                    # Import here to avoid circular dependency
                    from agile_bot.bots.base_bot.src.repl_cli.repl_commands.workflow import InstructionsCommand
                    cmd = InstructionsCommand(self.session)
                    return cmd.execute(args)
                elif operation == 'submit':
                    # Import here to avoid circular dependency
                    from agile_bot.bots.base_bot.src.repl_cli.repl_commands.workflow import SubmitCommand
                    cmd = SubmitCommand(self.session)
                    return cmd.execute(args)
                elif operation == 'confirm':
                    # Confirm doesn't make sense to re-execute
                    return REPLCommandResponse(
                        output="Cannot re-execute 'confirm'. Use 'next' or 'back' to navigate.",
                        response="Cannot re-execute confirm",
                        status="error"
                    )
        
        # Default: show instructions
        return self.display_instructions()


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

