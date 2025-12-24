import json
from pathlib import Path
from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import InstructionDisplayCommand


class WorkflowCommand(InstructionDisplayCommand):
    """Base for workflow commands - provides action phase/state properties and workflow operations."""
    
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
    
    def execute_submit(self) -> REPLCommandResponse:
        """Execute the current action's submit() method. SINGLE SOURCE OF TRUTH."""
        action = self.current_action
        if not action:
            return REPLCommandResponse(
                output="ERROR: No current action",
                response="ERROR: No current action",
                status="error"
            )
        
        try:
            # Call the real action.submit() method
            context = action.context_class()
            result = action.submit(context)
            
            # Format output
            status = result.get('status', 'unknown')
            message = result.get('message', 'Work submitted')
            
            output = "\n".join([
                f"EXECUTING {self.current_behavior_name}.{self.current_action_name}.submit",
                "",
                f"[{status.upper()}]",
                f"- {message}",
                "",
                "Type 'confirm' to complete this action and advance to next."
            ])
            
            return REPLCommandResponse(
                output=output,
                response=output,
                status="success",
                action=self.current_action_name
            )
        except Exception as e:
            error_msg = f"ERROR executing {self.current_action_name}.submit(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=self.current_action_name
            )
    
    def execute_confirm(self) -> REPLCommandResponse:
        """Execute the current action's confirm() method and advance. SINGLE SOURCE OF TRUTH."""
        action = self.current_action
        behavior = self.current_behavior
        if not behavior or not action:
            return self.error_no_current_behavior()
        
        current_behavior_name = behavior.name
        current_action_name = action.action_name
        
        try:
            # Call the real action.confirm() method
            context = action.context_class()
            result = action.confirm(context)
            
            # Check if at last action BEFORE closing
            is_last_action = behavior.actions.next() is None
            
            # Mark current action as complete and advance
            behavior.actions.close_current()
            
            # If not at last action, advance to next action and show navigation
            if not is_last_action:
                return self.display_navigation()
            
            # At last action - behavior is complete
            # Mark behavior as complete in state file
            self._mark_behavior_complete(current_behavior_name)
            
            # Check for next behavior BEFORE close_current since it advances the index
            next_behavior = self.bot.behaviors.next()
            
            if next_behavior:
                # Advance to next behavior
                self.bot.behaviors.close_current()
                # Navigate to next behavior's first action
                if next_behavior.actions.names:
                    self.navigate_to_behavior_action(next_behavior.name, next_behavior.actions.names[0])
                    return self.display_navigation()
            
            # No more behaviors - all complete
            return REPLCommandResponse(
                output=f"COMPLETE: {current_behavior_name} behavior finished\n\nALL BEHAVIORS COMPLETE!",
                response="COMPLETE: All behaviors finished",
                status="success"
            )
        except Exception as e:
            error_msg = f"ERROR executing {current_action_name}.confirm(): {str(e)}"
            return REPLCommandResponse(
                output=error_msg,
                response=error_msg,
                status="error",
                action=current_action_name
            )
    
    def _mark_behavior_complete(self, behavior_name: str) -> None:
        """Add behavior to completed_behaviors in state file."""
        state_file = self.session.workspace_directory / 'behavior_action_state.json'
        if not state_file.exists():
            return
        try:
            state_data = json.loads(state_file.read_text())
            completed = state_data.get('completed_behaviors', [])
            if behavior_name not in completed:
                completed.append(behavior_name)
            state_data['completed_behaviors'] = completed
            state_file.write_text(json.dumps(state_data, indent=2))
        except (json.JSONDecodeError, IOError):
            pass


class InstructionsCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "instructions"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("get instructions for")
        # Just display instructions - no state change
        return self.display_instructions()


class SubmitCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "submit"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("submit for")
        return self.execute_submit()


class ConfirmCommand(WorkflowCommand):
    @property
    def name(self) -> str:
        return "confirm"
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action("confirm")
        return self.execute_confirm()

