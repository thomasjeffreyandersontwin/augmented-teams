from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import json
from datetime import datetime
from .behaviors import Behaviors
from .behavior import Behavior
from .bot_paths import BotPaths
from ..utils import read_json_file
import logging
logger = logging.getLogger(__name__)
__all__ = ['Bot', 'BotResult', 'Behavior']

class BotResult:

    def __init__(self, status: str, behavior: str, action: str, data: Dict[str, Any]=None):
        self.status = status
        self.behavior = behavior
        self.action = action
        self.data = data or {}
        self.executed_instructions_from = f'{behavior}/{action}'

class Bot:

    def __init__(self, bot_name: str, bot_directory: Path, config_path: Path):
        self.name = bot_name
        self.bot_name = bot_name
        self.config_path = Path(config_path)
        self.bot_paths = BotPaths(bot_directory=bot_directory)
        bot_config_path = self.bot_paths.bot_directory / 'bot_config.json'
        if not bot_config_path.exists():
            raise FileNotFoundError(f'Bot config not found at {bot_config_path}')
        self._config = read_json_file(bot_config_path)
        self.behaviors = Behaviors(bot_name, self.bot_paths)
        self.behaviors._bot_instance = self
        for behavior in self.behaviors:
            behavior.bot = self

    @property
    def base_actions_path(self) -> Path:
        return self.bot_paths.bot_directory / 'base_actions'

    @property
    def description(self) -> str:
        return self._config.get('description', '')

    @property
    def goal(self) -> str:
        return self._config.get('goal', '')

    @property
    def instructions(self) -> List[str]:
        return self._config.get('instructions', [])

    @property
    def mcp(self) -> Dict[str, Any]:
        return self._config.get('mcp', {})

    @property
    def trigger_words(self) -> List[str]:
        return self._config.get('trigger_words', [])

    @property
    def working_area(self) -> Optional[str]:
        return self._config.get('WORKING_AREA')

    def help(self, topic: Optional[str] = None) -> Dict[str, Any]:
        """Display help information about the bot, behaviors, or actions.
        
        Args:
            topic: Optional topic for specific help (behavior name, action name, etc.)
        
        Returns:
            Dict with help information including behaviors, actions, and usage
        """
        from ..repl_cli.repl_help import REPLHelp
        
        # Create a minimal session-like object for REPLHelp
        class HelpContext:
            def __init__(self, bot):
                self.bot = bot
                self.current_behavior = bot.behaviors.current
                self.current_action = self.current_behavior.actions.current if self.current_behavior else None
                
            @property
            def has_current_behavior(self):
                return self.current_behavior is not None
            
            @property
            def has_current_action(self):
                return self.current_action is not None
            
            def _get_instructions_params_hint(self, action):
                """Return parameter hints for instructions - stub implementation."""
                return ""
            
            def _get_confirm_params_hint(self, action):
                """Return parameter hints for confirm - stub implementation."""
                return ""
        
        help_ctx = HelpContext(self)
        help_system = REPLHelp(self, help_ctx)
        
        # If no topic specified, return main help
        if not topic:
            return {
                'status': 'success',
                'help_text': help_system.main_help,
                'behaviors': self.behaviors.names,
                'current_behavior': self.behaviors.current.name if self.behaviors.current else None
            }
        
        # Check if topic is an action name for current behavior
        if self.behaviors.current:
            current_behavior = self.behaviors.current
            action_help = help_system.action_help(current_behavior.name, topic)
            if action_help:
                return {
                    'status': 'success',
                    'help_text': action_help.help_text,
                    'topic': topic,
                    'topic_type': 'action'
                }
        
        # Check if topic is a behavior name
        behavior_help = help_system.behavior_help(topic)
        if behavior_help:
            return {
                'status': 'success',
                'help_text': behavior_help.actions_list,
                'topic': topic,
                'topic_type': 'behavior'
            }
        
        # Topic not found
        return {
            'status': 'error',
            'message': f'Unknown help topic: {topic}'
        }
    
    def exit(self) -> Dict[str, Any]:
        """Exit the bot session gracefully.
        
        Returns:
            Dict with exit status and message
        """
        return {
            'status': 'exit',
            'message': 'Exiting bot session. Goodbye!'
        }
    
    def scope(self, scope_filter: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Dict with scope information or updated scope status
        """
        from ..actions.action_context import Scope, ScopeType
        import os
        
        if scope_filter is None:
            # Return current scope from persistent storage
            state_file = self.bot_paths.workspace_directory / 'behavior_action_state.json'
            if state_file.exists():
                try:
                    state_data = json.loads(state_file.read_text())
                    scope_dict = state_data.get('scope')
                    if scope_dict:
                        scope = Scope.from_dict(scope_dict)
                        return {
                            'status': 'success',
                            'message': 'Current scope',
                            'scope': scope.to_dict()
                        }
                except (json.JSONDecodeError, IOError):
                    pass
            return {
                'status': 'success',
                'message': 'No scope set',
                'scope': None
            }
        
        if scope_filter.lower() == 'all':
            # Clear scope from persistent storage
            Scope.clear_from_bot(self.bot_paths.workspace_directory)
            return {
                'status': 'success',
                'message': 'Scope filter cleared'
            }
        
        # Parse scope filter
        if scope_filter.startswith(('file:', 'files:')):
            value_part = scope_filter.split(':', 1)[1].strip()
            scope_values = [v.strip() for v in value_part.split(',') if v.strip()]
            scope_type = ScopeType.FILES
        else:
            scope_values = [v.strip() for v in scope_filter.split(',') if v.strip()]
            # Auto-detect if this looks like a file path
            looks_like_path = any(
                os.path.isabs(v) or '\\' in v or '/' in v 
                for v in scope_values
            )
            scope_type = ScopeType.FILES if looks_like_path else ScopeType.STORY
        
        scope = Scope(type=scope_type, value=scope_values)
        
        # Persist scope to storage
        scope.apply_to_bot(self.bot_paths.workspace_directory)
        
        return {
            'status': 'success',
            'message': f'Scope set to: {scope_filter}',
            'scope': scope.to_dict()
        }
    
    def path(self, directory: Optional[str] = None) -> Dict[str, Any]:
        """Set or view the working directory.
        
        Args:
            directory: Path to set as working directory, or None to view current path
        
        Returns:
            Dict with path information or updated path status
        """
        if directory is None:
            # Return current working directory
            current_path = self.bot_paths.workspace_directory
            return {
                'status': 'success',
                'path': str(current_path),
                'message': f'Current working directory: {current_path}'
            }
        
        # Set new working directory
        new_path = Path(directory)
        if not new_path.is_absolute():
            new_path = self.bot_paths.workspace_directory / new_path
        
        if not new_path.exists():
            return {
                'status': 'error',
                'message': f'Directory does not exist: {new_path}'
            }
        
        # Update the bot paths
        self.bot_paths._workspace_directory = new_path
        
        return {
            'status': 'success',
            'path': str(new_path),
            'message': f'Working directory set to: {new_path}'
        }

    def __getattr__(self, name: str):
        behavior = self.behaviors.find_by_name(name)
        if behavior:
            return behavior
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")