from pathlib import Path
from typing import Dict, Any, Optional
from agile_bot.bots.base_bot.src.state.activity_tracker import ActivityTracker
from agile_bot.bots.base_bot.src.state.workspace import (
    get_workspace_directory, 
    get_bot_directory,
    get_python_workspace_root
)


class BaseAction:
    
    def __init__(self, bot_name: str, behavior: str, bot_directory: Path, action_name: str):
        """Initialize BaseAction.
        
        Args:
            bot_name: Name of the bot
            behavior: Name of the behavior
            bot_directory: Directory where bot code lives
            action_name: Name of this action
            
        Note:
            workspace_directory is auto-detected from get_workspace_directory()
        """
        self.bot_name = bot_name
        self.behavior = behavior
        self.bot_directory = Path(bot_directory)
        self.action_name = action_name
    
    @property
    def workspace_directory(self) -> Path:
        """Get workspace directory (auto-detected from environment/agent.json)."""
        return get_workspace_directory()

    @property
    def tracker(self):
        """Get activity tracker (lazy initialization)."""
        if not hasattr(self, '_tracker'):
            self._tracker = ActivityTracker(self.workspace_directory, self.bot_name)
        return self._tracker

    @property
    def base_actions_dir(self) -> Path:
        """Get base actions directory.
        
        Returns path to base_bot's base_actions folder.
        """
        # Use centralized repository root
        repo_root = get_python_workspace_root()
        return repo_root / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
    

    @property
    def working_dir(self) -> Path:
        """Get workspace directory where content files are created."""
        return get_workspace_directory()
    
    @property
    def bot_dir(self) -> Path:
        """Get bot directory where bot code lives."""
        return self.bot_directory
    
    
    def track_activity_on_start(self):
        self.tracker.track_start(self.bot_name, self.behavior, self.action_name)
    
    def track_activity_on_completion(self, outputs: dict = None, duration: int = None):
        self.tracker.track_completion(self.bot_name, self.behavior, self.action_name, outputs, duration)
    
    def execute(self, parameters: Dict[str, Any] = None) -> Dict[str, Any]:
        """Template method that automatically tracks activity. Override do_execute() in subclasses."""
        # Track start
        self.track_activity_on_start()
        
        # Execute action logic (subclass implements this)
        result = self.do_execute(parameters or {})
        
        # Track completion
        self.track_activity_on_completion(outputs=result)
        
        return result
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Override this in subclasses to implement action logic."""
        raise NotImplementedError("Subclasses must implement do_execute()")
    
    def finalize_and_transition(self, next_action: Optional[str] = None):
        class TransitionResult:
            pass
        
        result = TransitionResult()
        result.next_action = next_action
        return result

