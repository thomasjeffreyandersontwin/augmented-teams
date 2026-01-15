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
    # Class-level registry for bot switching
    _active_bot_instance: Optional['Bot'] = None
    _active_bot_name: Optional[str] = None

    def __init__(self, bot_name: str, bot_directory: Path, config_path: Path):
        # #region agent log
        import json; from pathlib import Path as P; log_path = P(r'c:\dev\augmented-teams\.cursor\debug.log'); log_path.parent.mkdir(parents=True, exist_ok=True); log_file = open(log_path, 'a', encoding='utf-8'); log_file.write(json.dumps({'location':'bot.py:24','message':'Bot.__init__ entry','data':{'bot_name':bot_name,'bot_directory_param':str(bot_directory),'bot_directory_name':bot_directory.name if bot_directory else None},'timestamp':__import__('time').time()*1000,'sessionId':'debug-session','hypothesisId':'H1'})+'\n'); log_file.close()
        # #endregion
        self.name = bot_name
        self.bot_name = bot_name
        self.config_path = Path(config_path)
        
        # Register this bot as the active one
        Bot._active_bot_instance = self
        Bot._active_bot_name = bot_name
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
    
    @property
    def bots(self) -> List[str]:
        """Return list of all registered bot names.
        
        Discovers bots by scanning the parent bots directory for subdirectories
        containing bot_config.json files.
        
        Returns:
            List of bot names (directory names) that have valid bot_config.json
        """
        registered_bots = []
        
        # Get the parent bots directory (bot_directory.parent)
        bots_parent_dir = self.bot_paths.bot_directory.parent
        
        # Scan for bot directories
        if bots_parent_dir.exists() and bots_parent_dir.is_dir():
            for bot_dir in bots_parent_dir.iterdir():
                if bot_dir.is_dir():
                    bot_config = bot_dir / 'bot_config.json'
                    if bot_config.exists():
                        registered_bots.append(bot_dir.name)
        
        return sorted(registered_bots)
    
    @property
    def active_bot(self) -> 'Bot':
        """Return the currently active bot instance.
        
        Returns:
            The active Bot instance from the class-level registry
        """
        return Bot._active_bot_instance if Bot._active_bot_instance else self
    
    @active_bot.setter
    def active_bot(self, bot_name: str):
        """Switch to a different registered bot.
        
        Creates a new Bot instance for the specified bot and updates the
        class-level registry so all subsequent calls return the new instance.
        
        Args:
            bot_name: Name of the bot to switch to
        
        Raises:
            ValueError: If bot_name is not registered or invalid
        """
        # Validate bot exists
        registered_bots = self.bots
        
        if bot_name not in registered_bots:
            raise ValueError(
                f"Bot '{bot_name}' not found. Available bots: {', '.join(registered_bots)}"
            )
        
        # If switching to current bot, no action needed
        if bot_name == Bot._active_bot_name:
            return
        
        # Create new Bot instance for the target bot
        bots_parent_dir = self.bot_paths.bot_directory.parent
        new_bot_dir = bots_parent_dir / bot_name
        new_config_path = new_bot_dir / 'bot_config.json'
        
        if not new_config_path.exists():
            raise FileNotFoundError(f"Bot config not found at {new_config_path}")
        
        # Create new Bot instance (this will auto-register via __init__)
        Bot(
            bot_name=bot_name,
            bot_directory=new_bot_dir,
            config_path=new_config_path
        )

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
            Dict with status, message, and scope data when setting scope, or Scope object when viewing
        """
        from ..scope.scope import ScopeType
        import os
        
        if scope_filter is None:
            # Return current scope instance for property access
            return self._scope
        
        # Track if this is a clear operation
        is_clear = False
        
        # Strip "set" or "clear" keywords from CLI commands
        scope_filter_lower = scope_filter.lower().strip()
        if scope_filter_lower.startswith('set '):
            scope_filter = scope_filter[4:].strip()  # Remove "set " prefix
            scope_filter_lower = scope_filter.lower().strip()  # Recalculate after removing "set"
        
        # Strip surrounding quotes (single or double) from the filter value
        scope_filter = scope_filter.strip()
        if (scope_filter.startswith('"') and scope_filter.endswith('"')) or \
           (scope_filter.startswith("'") and scope_filter.endswith("'")):
            scope_filter = scope_filter[1:-1]
            scope_filter_lower = scope_filter.lower().strip()  # Recalculate after stripping quotes
        
        if scope_filter_lower == 'clear':
            # Clear scope
            is_clear = True
            self._scope.clear()
            self._scope.save()
            from ..scope.scope_command_result import ScopeCommandResult
            return ScopeCommandResult(
                status='success',
                message='Scope cleared',
                scope=self._scope
            )
        
        if scope_filter.lower() == 'all':
            # Clear scope
            self._scope.clear()
            self._scope.save()
            from ..scope.scope_command_result import ScopeCommandResult
            return ScopeCommandResult(
                status='success',
                message='Scope cleared (set to all)',
                scope=self._scope
            )
        
        if scope_filter.lower() == 'showall':
            # Show all - set to SHOW_ALL type
            self._scope.filter(ScopeType.SHOW_ALL, [])
            self._scope.save()
            from ..scope.scope_command_result import ScopeCommandResult
            return ScopeCommandResult(
                status='success',
                message='Scope set to show all',
                scope=self._scope
            )
        
        # Parse scope filter
        # Handle multiple formats:
        # 1. "story=TestStory" or "story:TestStory" (delimited)
        # 2. "story TestStory" (space-separated)
        # 3. "TestStory" (auto-detect)
        
        if '=' in scope_filter or ':' in scope_filter:
            # Format: story=TestStory or story:TestStory
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
                # Use the original prefix for the message
                prefix = 'story' if prefix == 'story' else 'epic'
            elif prefix == 'increment':
                scope_type = ScopeType.INCREMENT
            else:
                # Unknown prefix, treat as story
                scope_type = ScopeType.STORY
                prefix = 'story'
        elif ' ' in scope_filter:
            # Format: story TestStory (space-separated)
            parts = scope_filter.split(None, 1)  # Split on first whitespace
            potential_prefix = parts[0].lower()
            
            # Check if first word is a valid scope type
            if potential_prefix in ('story', 'epic', 'increment', 'file', 'files'):
                prefix = potential_prefix
                value_part = parts[1] if len(parts) > 1 else ''
                scope_values = [v.strip() for v in value_part.split(',') if v.strip()]
                
                # Map prefix to scope type
                if prefix in ('file', 'files'):
                    scope_type = ScopeType.FILES
                elif prefix in ('story', 'epic'):
                    scope_type = ScopeType.STORY
                elif prefix == 'increment':
                    scope_type = ScopeType.INCREMENT
                else:
                    scope_type = ScopeType.STORY
            else:
                # Not a recognized prefix, treat whole thing as value
                scope_values = [v.strip() for v in scope_filter.split(',') if v.strip()]
                # Auto-detect based on value
                looks_like_path = any(
                    os.path.isabs(v) or '\\' in v or '/' in v 
                    for v in scope_values
                )
                if looks_like_path:
                    scope_type = ScopeType.FILES
                    prefix = 'files'
                else:
                    scope_type = ScopeType.STORY
                    prefix = 'story'
        else:
            # No delimiter or space - auto-detect based on value
            scope_values = [v.strip() for v in scope_filter.split(',') if v.strip()]
            # Auto-detect if this looks like a file path
            looks_like_path = any(
                os.path.isabs(v) or '\\' in v or '/' in v 
                for v in scope_values
            )
            if looks_like_path:
                scope_type = ScopeType.FILES
                prefix = 'files'
            else:
                scope_type = ScopeType.STORY
                prefix = 'story'
        
        # Update scope filter
        self._scope.filter(scope_type, scope_values)
        self._scope.save()
        
        # Return a ScopeCommandResult object that will be serialized properly
        from ..scope.scope_command_result import ScopeCommandResult
        return ScopeCommandResult(
            status='success',
            message=f'Scope set to {prefix}: {", ".join(scope_values)}',
            scope=self._scope
        )
    
    def workspace(self, directory: Optional[str] = None) -> Dict[str, Any]:
        """Alias for path command - set or view the working directory.
        
        Args:
            directory: Path to set as working directory, or None to view current path
        
        Returns:
            Dict with path information or updated path status
        """
        return self.path(directory)
    
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
        
        # Update the bot paths (with persistence)
        self.bot_paths.update_workspace_directory(new_path, persist=True)
        
        # Reload scope for new workspace
        self._scope = Scope(self.bot_paths.workspace_directory, self.bot_paths)
        self._scope.load()
        
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
    
    def execute(self, behavior_name: str, action_name: Optional[str] = None, params: Optional[Dict[str, Any]] = None) -> Any:
        """Execute a specific behavior.action and return instructions.
        
        Navigates to behavior/action and calls get_instructions() with optional parameters.
        
        Args:
            behavior_name: Name of the behavior to execute
            action_name: Name of the action to execute (optional, uses current action if None)
            params: Optional parameters to pass to action context (guardrails, answers, decisions, etc.)
        
        Returns:
            Instructions object from action.get_instructions()
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
        
        # Get current action
        action = behavior.actions.current
        if not action:
            return {
                'status': 'error',
                'message': f'No current action in {behavior_name}'
            }
        
        # Save state after navigation
        self.behaviors.save_state()
        
        try:
            # Get instructions using get_instructions() method with context
            from ..actions.action_context import ActionContext
            context = action.context_class() if hasattr(action, 'context_class') else ActionContext()
            
            # If params provided, populate context attributes
            if params:
                for key, value in params.items():
                    # Always set the attribute (even if it doesn't exist yet)
                    # This allows passing both old names (decisions) and new names (decisions_made)
                    setattr(context, key, value)
            
            # Get instructions (will save guardrails if provided in context)
            instructions = action.get_instructions(context)
            
            # Return Instructions object directly for adapter serialization
            return instructions
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error executing {behavior_name}.{action.action_name}: {str(e)}'
            }
    
    def save(self, answers: Optional[Dict[str, str]] = None,
             evidence_provided: Optional[Dict[str, str]] = None,
             decisions: Optional[Dict[str, str]] = None,
             assumptions: Optional[List[str]] = None) -> Dict[str, Any]:
        """Save guardrail data (answers, evidence, decisions, assumptions) for current behavior.
        
        Args:
            answers: Question-answer pairs for clarification
            evidence_provided: Evidence key-value pairs for clarification
            decisions: Criteria-decision pairs for strategy
            assumptions: List of assumption strings for strategy
        
        Returns:
            Status dict with success/error message
        """
        from ..actions.clarify.requirements_clarifications import RequirementsClarifications
        from ..actions.clarify.required_context import RequiredContext
        from ..actions.strategy.strategy_decision import StrategyDecision
        from ..actions.strategy.strategy import Strategy
        
        current_behavior = self.behaviors.current
        if not current_behavior:
            return {
                'status': 'error',
                'message': 'No current behavior set'
            }
        
        try:
            saved_items = []
            
            if answers or evidence_provided:
                required_context = RequiredContext(current_behavior.folder)
                clarifications = RequirementsClarifications(
                    behavior_name=current_behavior.name,
                    bot_paths=current_behavior.bot_paths,
                    required_context=required_context,
                    key_questions_answered=answers or {},
                    evidence_provided=evidence_provided or {},
                    context=None
                )
                clarifications.save()
                if answers:
                    saved_items.append('answers')
                if evidence_provided:
                    saved_items.append('evidence')
            
            if decisions or assumptions:
                strategy = Strategy(current_behavior.folder)
                strategy_decision = StrategyDecision(
                    behavior_name=current_behavior.name,
                    bot_paths=current_behavior.bot_paths,
                    strategy=strategy,
                    decisions_made=decisions or {},
                    assumptions_made=assumptions or []
                )
                strategy_decision.save()
                if decisions:
                    saved_items.append('decisions')
                if assumptions:
                    saved_items.append('assumptions')
            
            if not saved_items:
                return {
                    'status': 'error',
                    'message': 'No data provided to save'
                }
            
            return {
                'status': 'success',
                'message': f"Saved {', '.join(saved_items)} for {current_behavior.name}",
                'behavior': current_behavior.name,
                'saved': saved_items
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error saving: {str(e)}'
            }
    
    def submit(self) -> Dict[str, Any]:
        """Submit current action instructions to AI agent.
        
        Gets the current action's instructions (including display_content with all 
        behavior instructions, action instructions, base instructions, and guardrails),
        copies them to clipboard, and opens Cursor chat.
        
        Returns:
            Status dict with success message, current context, and instructions content
        """
        current_behavior = self.behaviors.current
        if not current_behavior:
            return {
                'status': 'error',
                'message': 'No current behavior set'
            }
        
        current_action_name = current_behavior.actions.current_action_name
        if not current_action_name:
            return {
                'status': 'error',
                'message': 'No current action set'
            }
        
        try:
            # Get the current action object
            action = current_behavior.actions.find_by_name(current_action_name)
            if not action:
                return {
                    'status': 'error',
                    'message': f'Action {current_action_name} not found'
                }
            
            # Get instructions with display_content built
            instructions = action.get_instructions()
            display_content = instructions.display_content
            
            if not display_content:
                return {
                    'status': 'error',
                    'message': 'No instructions available to submit'
                }
            
            # Convert display_content to string
            if isinstance(display_content, list):
                content_str = '\n'.join(display_content)
            else:
                content_str = str(display_content)
            
            # Copy to clipboard and automate Cursor chat using keyboard shortcuts
            clipboard_status = 'failed'
            cursor_status = 'not_attempted'
            
            try:
                import pyperclip
                import pyautogui
                import time
                
                # Copy to clipboard
                pyperclip.copy(content_str)
                clipboard_status = 'success'
                time.sleep(0.2)
                
                # Ctrl+L to open chat
                pyautogui.hotkey('ctrl', 'l')
                time.sleep(0.3)
                
                # Ctrl+V to paste
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.2)
                
                cursor_status = 'opened'
                
            except ImportError as e:
                clipboard_status = 'failed'
                cursor_status = f'failed: pyautogui/pyperclip not installed - {str(e)}'
            except Exception as e:
                cursor_status = f'failed: {str(e)}'
            
            return {
                'status': 'success',
                'message': f'Instructions submitted for {current_behavior.name}.{current_action_name}',
                'behavior': current_behavior.name,
                'action': current_action_name,
                'timestamp': datetime.now().isoformat(),
                'clipboard_status': clipboard_status,
                'cursor_status': cursor_status,
                'instructions_length': len(content_str),
                'instructions': content_str  # Include for JSON mode
            }
            
        except Exception as e:
            logger.error(f'Error in submit: {str(e)}', exc_info=True)
            return {
                'status': 'error',
                'message': f'Error submitting instructions: {str(e)}'
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