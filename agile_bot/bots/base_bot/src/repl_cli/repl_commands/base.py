from abc import ABC, abstractmethod
from agile_bot.bots.base_bot.src.repl_cli.repl_results import REPLCommandResponse


class REPLCommand(ABC):
    def __init__(self, session):
        self.session = session
        self.bot = session.bot
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass
    
    @property
    def takes_args(self) -> bool:
        return False
    
    @abstractmethod
    def execute(self, args: str = "") -> REPLCommandResponse:
        pass
    
    @property
    def current_behavior(self):
        return self.session.current_behavior
    
    @property
    def current_action(self):
        return self.session.current_action
    
    @property
    def has_current_behavior(self) -> bool:
        return self.session.has_current_behavior
    
    @property
    def has_current_action(self) -> bool:
        return self.session.has_current_action
    
    @property
    def current_behavior_name(self):
        return self.session.current_behavior_name
    
    @property
    def current_action_name(self):
        return self.session.current_action_name
    
    def error_no_current_action(self, context: str = "") -> REPLCommandResponse:
        msg = f"ERROR: No current action{' to ' + context if context else ''}"
        return REPLCommandResponse(output=msg, response="ERROR: No current action", status="error")
    
    def error_no_current_behavior(self) -> REPLCommandResponse:
        return REPLCommandResponse(
            output="ERROR: No current behavior set. Please select a behavior first.",
            response="ERROR: No current behavior set",
            status="error"
        )
    
    def error_behavior_not_found(self, behavior_name: str) -> REPLCommandResponse:
        available = ", ".join(self.bot.behaviors.names)
        output = f"ERROR: Behavior '{behavior_name}' not found\nAvailable behaviors: {available}"
        return REPLCommandResponse(output=output, response=f"ERROR: Behavior '{behavior_name}' not found", status="error")
    
    def error_action_not_found(self, action_name: str) -> REPLCommandResponse:
        behavior = self.current_behavior
        available = ", ".join(behavior.actions.names) if behavior else ""
        output = f"ERROR: action '{action_name}' not found\nAvailable actions: {available}"
        return REPLCommandResponse(output=output, response=f"ERROR: action '{action_name}' not found", status="error")

