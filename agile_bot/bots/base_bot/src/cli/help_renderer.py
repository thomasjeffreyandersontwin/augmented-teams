from abc import ABC, abstractmethod
from typing import List, Dict, Any
from pathlib import Path
from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext, ActionHelpContext

class HelpRenderer(ABC):
    """Abstract base class for rendering help output."""
    
    @abstractmethod
    def render_header(self, bot_name: str) -> None:
        """Render help header."""
        pass
    
    @abstractmethod
    def render_behavior_section(self, context: BehaviorHelpContext) -> None:
        """Render behavior section with actions."""
        pass
    
    @abstractmethod
    def render_action_help_section_header(self) -> None:
        """Render action help section header."""
        pass
    
    @abstractmethod
    def render_action_help(self, context: ActionHelpContext) -> None:
        """Render action help with parameters."""
        pass
    
    @abstractmethod
    def render_separator(self) -> None:
        """Render separator."""
        pass
    
    def _render_parameter_description(self, param: str, param_desc: str) -> None:
        """Render a single parameter description (shared helper)."""
        if '\n' in param_desc:
            lines = param_desc.split('\n')
            print(f'{param}:   {lines[0]}')
            for line in lines[1:]:
                print(f'    {line}')
        else:
            print(f'{param}:   {param_desc}')
    
    def _render_action_list_and_context(self, action_list: str) -> None:
        """Render action list and context line (shared helper)."""
        print(f'action:   {action_list}')
        print('context:  Optional context or file path')
    
    def _render_additional_options(self, additional_options: Dict[str, str]) -> None:
        """Render additional options if present (shared helper)."""
        if additional_options:
            print('           Additional options:')
            for option, description in additional_options.items():
                print(f"           {option}  {description}")

