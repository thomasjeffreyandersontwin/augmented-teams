from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field
from tinydb import TinyDB
from typing import Optional, Dict, Any
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths


@dataclass
class ActionState:
    """Identifies a specific action execution - groups bot_name, behavior, action."""
    bot_name: str
    behavior: str
    action: str
    outputs: Optional[Dict[str, Any]] = None
    duration: Optional[int] = None
    
    @property
    def state_key(self) -> str:
        """Get the action state key string."""
        return f'{self.bot_name}.{self.behavior}.{self.action}'


class ActivityTracker:
    def __init__(self, bot_paths: BotPaths, bot_name: str):
        self._bot_paths = bot_paths
        self.bot_name = bot_name
    
    @property
    def workspace_dir(self) -> Path:
        return self._bot_paths.workspace_directory

    @property
    def file(self) -> Path:
        return self._bot_paths.workspace_directory / 'activity_log.json'
    
    def track_start(self, state: ActionState):
        """Track the start of an action execution."""
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with TinyDB(self.file) as db:
            db.insert({
                'action_state': state.state_key,
                'status': 'started',
                'timestamp': datetime.now().isoformat()
            })
    
    def track_completion(self, state: ActionState):
        """Track the completion of an action execution."""
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with TinyDB(self.file) as db:
            entry = {
                'action_state': state.state_key,
                'status': 'completed',
                'timestamp': datetime.now().isoformat()
            }
            if state.outputs:
                entry['outputs'] = state.outputs
            if state.duration:
                entry['duration'] = state.duration
            db.insert(entry)
