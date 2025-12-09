from pathlib import Path
from datetime import datetime
from tinydb import TinyDB
from agile_bot.bots.base_bot.src.state.workspace import get_workspace_directory


class ActivityTracker:
    
    def __init__(self, workspace_root: Path, bot_name: str):
        # Always resolve the authoritative workspace via the workspace helper.
        # Ignore any workspace_root passed in to centralize environment access.
        self.workspace_root = Path(get_workspace_directory())
        self.bot_name = bot_name
        # Don't create directory in __init__, create it when actually writing
    
    @property
    def workspace_directory(self) -> Path:
        """Return the authoritative workspace directory (from workspace helper)."""
        return get_workspace_directory()

    @property
    def file(self) -> Path:
        """Get activity log file path."""
        # Activity logs live at the workspace root per environment-only policy.
        return self.workspace_directory / 'activity_log.json'
    
    def track_start(self, bot_name: str, behavior: str, action: str):
        # Ensure directory exists before writing
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with TinyDB(self.file) as db:
            db.insert({
                'action_state': f'{bot_name}.{behavior}.{action}',
                'status': 'started',
                'timestamp': datetime.now().isoformat()
            })
    
    def track_completion(self, bot_name: str, behavior: str, action: str, outputs: dict = None, duration: int = None):
        # Ensure directory exists before writing
        self.file.parent.mkdir(parents=True, exist_ok=True)
        with TinyDB(self.file) as db:
            entry = {
                'action_state': f'{bot_name}.{behavior}.{action}',
                'status': 'completed',
                'timestamp': datetime.now().isoformat()
            }
            if outputs:
                entry['outputs'] = outputs
            if duration:
                entry['duration'] = duration
            db.insert(entry)

