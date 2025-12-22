from abc import ABC, abstractmethod
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class Visitor(ABC):
    
    @abstractmethod
    def visit_header(self, bot_name: str) -> None:
        pass
    
    @abstractmethod
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        pass
    
    @abstractmethod
    def visit_action(self, context: ActionHelpContext) -> None:
        pass
    
    @abstractmethod
    def visit_action_help_section_header(self) -> None:
        pass
    
    def visit_footer(self) -> None:
        pass
