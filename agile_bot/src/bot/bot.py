from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
import json
from datetime import datetime
from ..behaviors import Behaviors, Behavior
from ..bot_path import BotPath
from ..scope import Scope
from ..help import Help
from ..navigation import NavigationResult
from ..exit_result import ExitResult
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
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:24','message':'Bot.__init__ entry','data':{'bot_name':bot_name,'bot_directory_param':str(bot_directory),'bot_directory_name':bot_directory.name if bot_directory else None},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.name = bot_name
        self.bot_name = bot_name
        self.config_path = Path(config_path)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:28','message':'Before BotPaths creation','data':{'bot_directory_to_pass':str(bot_directory)},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.bot_paths = BotPath(bot_directory=bot_directory)
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
        # Get allowed behaviors from bot_config.json
        allowed_behaviors = self._config.get('behaviors')
        self.behaviors = Behaviors(bot_name, self.bot_paths, allowed_behaviors=allowed_behaviors)
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:33','message':'After Behaviors creation','data':{'behavior_count':len(self.behaviors._behaviors) if self.behaviors else 0},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.behaviors._bot_instance = self
        for behavior in self.behaviors:
            behavior.bot = self
            # Ensure behavior.bot_name matches Bot's bot_name (not directory name)
            behavior.bot_name = self.bot_name
        
        # Create Scope instance with workspace context and load from state
        self._scope = Scope(self.bot_paths.workspace_directory, self.bot_paths)
        self._scope.load()
        
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:37','message':'Bot.__init__ exit','data':{},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion

    @property
    def base_actions_path(self) -> Path:
        return self.bot_paths.base_actions_directory

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
    
    @property
    def bot_directory(self) -> Path:
        """Return the bot directory path."""
        return self.bot_paths.bot_directory
    
    @property
    def workspace_directory(self) -> Path:
        """Return the workspace directory path."""
        return self.bot_paths.workspace_directory

    @property
    def progress_path(self) -> str:
        """Return current progress path (e.g., 'discovery.validate')."""
        if self.behaviors.current:
            behavior = self.behaviors.current
            if behavior.actions.current_action_name:
                return f"{behavior.name}.{behavior.actions.current_action_name}"
            else:
                return behavior.name
        return "idle"
    
    @property
    def stage_name(self) -> str:
        """Return current stage name (Idle/Ready/In Progress)."""
        if not self.behaviors.current:
            return "Idle"
        elif not self.behaviors.current.actions.current_action_name:
            return "Ready"
        else:
            return "In Progress"
    
    @property
    def commands(self) -> 'Help':
        """Return available commands as Help object."""
        return self.help()
    
    @property
    def current_behavior_name(self) -> str:
        """Return current behavior name."""
        return self.behaviors.current.name if self.behaviors.current else None
    
    @property
    def current_action_name(self) -> str:
        """Return current action name."""
        if self.behaviors.current and self.behaviors.current.actions.current_action_name:
            return self.behaviors.current.actions.current_action_name
        return None

    def help(self, topic: Optional[str] = None):
        """Display help information about the bot, behaviors, or actions.
        
        Args:
            topic: Optional topic for specific help (behavior name, action name, etc.)
        
        Returns:
            Help domain object with hierarchical help structure
        """
        from agile_bot.src.help.help import Help
        
        # Return new Help object that delegates to bot's behaviors/actions
        return Help(bot=self)
    
    def exit(self) -> Dict[str, Any]:
        """Exit the bot session gracefully.
        
        Returns:
            Dict with exit status and message
        """
        return {
            'status': 'exit',
            'message': 'Exiting bot session. Goodbye!'
        }
    
    def confirm(self, args: Optional[str] = None) -> Dict[str, Any]:
        """Confirm current action and advance workflow.
        
        Args:
            args: Optional arguments for confirmation
        
        Returns:
            Dict with confirmation result
        """
        if not self.behaviors.current:
            return {
                'status': 'error',
                'message': 'No current behavior to confirm'
            }
        
        behavior = self.behaviors.current
        if not behavior.actions.current:
            return {
                'status': 'error',
                'message': 'No current action to confirm'
            }
        
        action = behavior.actions.current
        
        try:
            # Call confirm on the action
            from ..actions.action_context import ActionContext
            context = action.context_class() if hasattr(action, 'context_class') else ActionContext()
            result = action.confirm(context)
            
            return {
                'status': 'success',
                'message': f'Confirmed {action.action_name}',
                'result': result
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error confirming: {str(e)}'
            }
    
    def current(self) -> Dict[str, Any]:
        """Get current action instructions.
        
        Returns:
            Dict with current action instructions
        """
        if not self.behaviors.current:
            return {
                'status': 'error',
                'message': 'No current behavior'
            }
        
        behavior = self.behaviors.current
        if not behavior.actions.current:
            return {
                'status': 'error',
                'message': 'No current action'
            }
        
        action = behavior.actions.current
        
        try:
            # Get instructions using get_instructions() method with default context
            from ..actions.action_context import ActionContext
            context = action.context_class() if hasattr(action, 'context_class') else ActionContext()
            instructions = action.get_instructions(context)
            
            # Return Instructions object directly for adapter serialization
            return instructions
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error getting instructions: {str(e)}'
            }
    
    def scope(self, scope_filter: Optional[str] = None):
        """Set or view the scope filter for the current workflow.
        
        AI AGENTS: This command requires COMPLETE folder paths. When you pass a directory path,
        you MUST include the ENTIRE folder structure from root or working area.
        
        Args:
            scope_filter: Complete folder path or story name to filter by, or None to view current scope
        
        Returns:
            Scope domain object
        """
        from ..scope.scope import ScopeType
        import os
        
        if scope_filter is None:
            # Return current scope instance
            return self._scope
        
        if scope_filter.lower() == 'all':
            # Clear scope
            self._scope.clear()
            self._scope.save()
            return self._scope
        
        if scope_filter.lower() == 'showall':
            # Show all - set to SHOW_ALL type
            self._scope.filter(ScopeType.SHOW_ALL, [])
            self._scope.save()
            return self._scope
        
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
            elif prefix in ('story', 'epic'):  # Both map to STORY (searches all levels)
                scope_type = ScopeType.STORY
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
        
        # Update scope filter
        self._scope.filter(scope_type, scope_values)
        self._scope.save()
        
        return self._scope
    
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
                self.behaviors.save_state()  # Persist state
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
                self.behaviors.save_state()  # Persist state
                return {
                    'status': 'success',
                    'message': f'Moved to {behavior.name}.{next_action}',
                    'behavior': behavior.name,
                    'action': next_action
                }
            else:
                # At last action of current behavior: advance to next behavior if any
                advance_result = self.behaviors.advance()
                return advance_result
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
                self.behaviors.save_state()  # Persist state
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

    def tree(self) -> str:
        """Display behavior hierarchy tree.
        
        Returns:
            String representation of all behaviors and their actions
        """
        lines = []
        behaviors_list = list(self.behaviors)
        
        for i, behavior in enumerate(behaviors_list):
            is_last_behavior = (i == len(behaviors_list) - 1)
            behavior_prefix = "└──" if is_last_behavior else "├──"
            is_current_behavior = (self.behaviors.current and behavior.name == self.behaviors.current.name)
            behavior_marker = "➤ " if is_current_behavior else ""
            lines.append(f"{behavior_prefix} {behavior_marker}{behavior.name}")
            
            # Show actions
            action_names = behavior.action_names
            for j, action in enumerate(action_names):
                is_last_action = (j == len(action_names) - 1)
                action_prefix = "    └──" if is_last_behavior else "│   └──" if is_last_action else "│   ├──"
                if not is_last_behavior and not is_last_action:
                    action_prefix = "│   ├──"
                is_current_action = (is_current_behavior and 
                                   behavior.actions.current_action_name == action)
                action_marker = "➤ " if is_current_action else ""
                lines.append(f"{action_prefix} {action_marker}{action}")
        
        return "\n".join(lines)
    
    def pos(self) -> Dict[str, Any]:
        """Get current position (behavior.action).
        
        Returns:
            Dict with current behavior and action
        """
        if not self.behaviors.current:
            return {
                'status': 'error',
                'message': 'No behavior is currently active'
            }
        
        behavior = self.behaviors.current
        action = behavior.actions.current_action_name
        
        if not action:
            return {
                'status': 'error',
                'message': f'No action is currently active in {behavior.name}'
            }
        
        return {
            'status': 'success',
            'behavior': behavior.name,
            'action': action,
            'position': f'{behavior.name}.{action}'
        }

    def __getattr__(self, name: str):
        behavior = self.behaviors.find_by_name(name)
        if behavior:
            return behavior
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")