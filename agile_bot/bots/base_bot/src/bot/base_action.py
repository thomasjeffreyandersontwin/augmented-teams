from pathlib import Path
from typing import Dict, Any, Optional
from agile_bot.bots.base_bot.src.state.activity_tracker import ActivityTracker
from agile_bot.bots.base_bot.src.state.workspace import get_workspace_directory


class BaseAction:
    
    def __init__(self, bot_name: str, behavior: str, botspace_root: Path, action_name: str):
        self.bot_name = bot_name
        self.behavior = behavior
        self.botspace_root = Path(botspace_root)
        self.action_name = action_name

        self.tracker = ActivityTracker(self.working_dir, bot_name)

    @property
    def base_actions_dir(self) -> Path:
        """Instance convenience property for the base actions directory.

        Computes the path relative to `self.botspace_root`, matching other
        directory properties (non-static).
        """
        return Path(self.botspace_root) / 'agile_bot' / 'bots' / 'base_bot' / 'base_actions'
    

    @property
    def working_dir(self) -> Path:
        """Read-only working directory derived from the workspace helper."""
        return get_workspace_directory()
    
    @property
    def bot_dir(self) -> Path:
        """Get action's bot directory path (read-only)."""
        return self.botspace_root / 'agile_bot' / 'bots' / self.bot_name
    
    
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

