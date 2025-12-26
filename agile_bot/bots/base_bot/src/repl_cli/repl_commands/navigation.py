from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse
from agile_bot.bots.base_bot.src.repl_cli.repl_commands.repl_command import InstructionDisplayCommand


class NavigationCommand(InstructionDisplayCommand):
    @property
    def next_action(self):
        behavior = self.current_behavior
        return behavior.actions.next() if behavior else None
    
    @property
    def previous_action(self):
        behavior = self.current_behavior
        return behavior.actions.previous() if behavior else None
    
    @property
    def next_behavior(self):
        return self.bot.behaviors.next()
    
    @property
    def previous_behavior(self):
        return self.bot.behaviors.previous()
    
    @property
    def has_more_actions(self) -> bool:
        return self.next_action is not None
    
    @property
    def has_previous_actions(self) -> bool:
        return self.previous_action is not None
    
    @property
    def has_more_behaviors(self) -> bool:
        return self.next_behavior is not None
    
    @property
    def has_previous_behaviors(self) -> bool:
        return self.previous_behavior is not None


class NextCommand(NavigationCommand):
    @property
    def name(self) -> str:
        return "next"
    
    def _validate_navigation_state(self) -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        behavior = self.current_behavior
        if not behavior:
            return self.error_no_current_behavior()
        return None
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        error = self._validate_navigation_state()
        if error:
            return error
        
        behavior = self.current_behavior
        
        # Cache next_action to avoid calling it multiple times (side effects)
        next_act = self.next_action
        if next_act:
            behavior.actions.navigate_to(next_act.action_name)
            return self.display_navigation()
        
        # At last action - try next behavior
        next_beh = self.next_behavior
        if next_beh:
            if next_beh.actions.names:
                self.navigate_to_behavior_action(next_beh.name, next_beh.actions.names[0])
            return self.display_navigation()
        
        return REPLCommandResponse(
            output="ERROR: Already at last action of last behavior",
            response="ERROR: Already at last action",
            status="error"
        )


class BackCommand(NavigationCommand):
    @property
    def name(self) -> str:
        return "back"
    
    def _validate_navigation_state(self) -> REPLCommandResponse:
        if not self.has_current_action:
            return self.error_no_current_action()
        behavior = self.current_behavior
        if not behavior:
            return self.error_no_current_behavior()
        return None
    
    def execute(self, args: str = "") -> REPLCommandResponse:
        error = self._validate_navigation_state()
        if error:
            return error
        
        behavior = self.current_behavior
        
        # Cache previous_action to avoid calling it multiple times (side effects)
        prev_act = self.previous_action
        if prev_act:
            behavior.actions.navigate_to(prev_act.action_name)
            return self.display_navigation()
        
        # At first action - try to go to previous behavior's last action
        prev_beh = self.previous_behavior
        if prev_beh:
            # Navigate to last action of previous behavior
            if prev_beh.actions.names:
                last_action_name = prev_beh.actions.names[-1]
                self.navigate_to_behavior_action(prev_beh.name, last_action_name)
            return self.display_navigation()
        
        return REPLCommandResponse(
            output="ERROR: Already at first action of first behavior",
            response="ERROR: Already at first action",
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

