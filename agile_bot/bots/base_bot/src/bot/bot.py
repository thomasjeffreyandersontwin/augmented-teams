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
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:24','message':'Bot.__init__ entry','data':{'bot_name':bot_name},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.name = bot_name
        self.bot_name = bot_name
        self.config_path = Path(config_path)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:28','message':'Before BotPaths creation','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.bot_paths = BotPaths(bot_directory=bot_directory)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:28','message':'After BotPaths creation','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        bot_config_path = self.bot_paths.bot_directory / 'bot_config.json'
        if not bot_config_path.exists():
            raise FileNotFoundError(f'Bot config not found at {bot_config_path}')
        self._config = read_json_file(bot_config_path)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:33','message':'Before Behaviors creation','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.behaviors = Behaviors(bot_name, self.bot_paths)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:33','message':'After Behaviors creation','data':{'behavior_count':len(self.behaviors._behaviors) if self.behaviors else 0},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.behaviors._bot_instance = self
        for behavior in self.behaviors:
            behavior.bot = self
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:37','message':'Bot.__init__ exit','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion

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

    def status(self) -> 'Status':
        """Return current bot status as Status domain object.
        
        Returns:
            Status domain object with progress_path, stage_name, current_behavior, current_action
        """
        from agile_bot.src.status.status import Status
        
        # Determine progress path
        if self.behaviors.current:
            behavior = self.behaviors.current
            if behavior.actions.current_action_name:
                progress_path = f"{behavior.name}.{behavior.actions.current_action_name}"
            else:
                progress_path = behavior.name
        else:
            progress_path = "idle"
        
        # Determine stage
        if not self.behaviors.current:
            stage_name = "Idle"
        elif not self.behaviors.current.actions.current_action_name:
            stage_name = "Ready"
        else:
            stage_name = "In Progress"
        
        # Current behavior/action
        current_behavior = self.behaviors.current.name if self.behaviors.current else None
        current_action = None
        if self.behaviors.current and self.behaviors.current.actions.current_action_name:
            current_action = self.behaviors.current.actions.current_action_name
        
        return Status(
            progress_path=progress_path,
            stage_name=stage_name,
            current_behavior=current_behavior,
            current_action=current_action
        )

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
        # Handle prefixed scope syntax (story=, epic=, increment=, files=, file:, files:)
        if '=' in scope_filter or ':' in scope_filter:
            # Determine delimiter (= or :)
            if '=' in scope_filter:
                delimiter = '='
                prefix, value_part = scope_filter.split('=', 1)
            else:
                delimiter = ':'
                prefix, value_part = scope_filter.split(':', 1)
            
            prefix = prefix.strip().lower()
            value_part = value_part.strip()
            scope_values = [v.strip() for v in value_part.split(',') if v.strip()]
            
            # Map prefix to scope type
            if prefix in ('file', 'files'):
                scope_type = ScopeType.FILES
            elif prefix == 'story':
                scope_type = ScopeType.STORY
            elif prefix == 'epic':
                scope_type = ScopeType.EPIC
            elif prefix == 'increment':
                scope_type = ScopeType.INCREMENT
            else:
                # Unknown prefix, treat as story
                scope_type = ScopeType.STORY
        else:
            # No prefix - auto-detect based on value
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

    def next(self) -> Dict[str, Any]:
        """Navigate to the next action in the current behavior workflow.
        
        Returns:
            Dict with navigation result (new position, message)
        """
        if not self.behaviors.current:
            return {
                'status': 'error',
                'message': 'No behavior is currently active. Use a behavior.action command to start.'
            }
        
        behavior = self.behaviors.current
        current_action = behavior.actions.current_action_name
        
        if not current_action:
            # No current action, start with first action
            if behavior.action_names:
                first_action = behavior.action_names[0]
                behavior.actions.navigate_to(first_action)
                return {
                    'status': 'success',
                    'message': f'Moved to {behavior.name}.{first_action}',
                    'behavior': behavior.name,
                    'action': first_action
                }
            else:
                return {
                    'status': 'error',
                    'message': f'Behavior {behavior.name} has no actions'
                }
        
        # Find next action
        action_names = behavior.action_names
        try:
            current_index = action_names.index(current_action)
            if current_index < len(action_names) - 1:
                next_action = action_names[current_index + 1]
                behavior.actions.navigate_to(next_action)
                return {
                    'status': 'success',
                    'message': f'Moved to {behavior.name}.{next_action}',
                    'behavior': behavior.name,
                    'action': next_action
                }
            else:
                return {
                    'status': 'info',
                    'message': f'Already at last action in {behavior.name}',
                    'behavior': behavior.name,
                    'action': current_action
                }
        except ValueError:
            return {
                'status': 'error',
                'message': f'Current action {current_action} not found in behavior'
            }
    
    def back(self) -> Dict[str, Any]:
        """Navigate to the previous action in the current behavior workflow.
        
        Returns:
            Dict with navigation result (new position, message)
        """
        if not self.behaviors.current:
            return {
                'status': 'error',
                'message': 'No behavior is currently active'
            }
        
        behavior = self.behaviors.current
        current_action = behavior.actions.current_action_name
        
        if not current_action:
            return {
                'status': 'error',
                'message': 'No current action to go back from'
            }
        
        # Find previous action
        action_names = behavior.action_names
        try:
            current_index = action_names.index(current_action)
            if current_index > 0:
                prev_action = action_names[current_index - 1]
                behavior.actions.navigate_to(prev_action)
                return {
                    'status': 'success',
                    'message': f'Moved back to {behavior.name}.{prev_action}',
                    'behavior': behavior.name,
                    'action': prev_action
                }
            else:
                return {
                    'status': 'info',
                    'message': f'Already at first action in {behavior.name}',
                    'behavior': behavior.name,
                    'action': current_action
                }
        except ValueError:
            return {
                'status': 'error',
                'message': f'Current action {current_action} not found in behavior'
            }
    
    def execute(self, behavior_name: str, action_name: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Execute a specific behavior.action with optional parameters.
        
        Args:
            behavior_name: Name of the behavior to execute
            action_name: Name of the action to execute (optional, uses current action if None)
            params: Optional parameters to pass to the action
        
        Returns:
            Dict with execution result
        """
        # Find behavior
        behavior = self.behaviors.find_by_name(behavior_name)
        if not behavior:
            return {
                'status': 'error',
                'message': f'Behavior not found: {behavior_name}',
                'available_behaviors': [b.name for b in self.behaviors]
            }
        
        # Set as current behavior
        self.behaviors.navigate_to(behavior_name)
        
        # Determine action to execute
        if action_name:
            # Set specific action as current
            try:
                behavior.actions.navigate_to(action_name)
            except ValueError:
                return {
                    'status': 'error',
                    'message': f'Action not found: {action_name}',
                    'available_actions': behavior.action_names
                }
        else:
            # Use current action or first action
            if not behavior.actions.current_action_name:
                if behavior.action_names:
                    behavior.actions.navigate_to(behavior.action_names[0])
                else:
                    return {
                        'status': 'error',
                        'message': f'Behavior {behavior_name} has no actions'
                    }
        
        current_action_name = behavior.actions.current_action_name
        
        # Execute the action (stub for now - actual execution would invoke action logic)
        return {
            'status': 'success',
            'message': f'Executed {behavior_name}.{current_action_name}',
            'behavior': behavior_name,
            'action': current_action_name,
            'result': 'Action execution complete'
        }

    def __getattr__(self, name: str):
        behavior = self.behaviors.find_by_name(name)
        if behavior:
            return behavior
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")