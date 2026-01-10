from pathlib import Path
import os
from ..utils import read_json_file

def get_python_workspace_root() -> Path:
    """
    Get the root of the Python workspace (repository root).
    workspace.py is at: agile_bot/src/bot/workspace.py
    Go up: bot -> src -> agile_bot -> workspace_root
    """
    return Path(__file__).parent.parent.parent.parent

def get_bot_directory() -> Path:
    bot_dir = os.environ.get('BOT_DIRECTORY')
    if not bot_dir:
        raise RuntimeError('BOT_DIRECTORY environment variable is not set. Entry points must bootstrap this before importing other modules.')
    return Path(bot_dir.strip())

def get_workspace_directory() -> Path:
    workspace = os.environ.get('WORKING_AREA') or os.environ.get('WORKING_DIR')
    if not workspace:
        raise RuntimeError('WORKING_AREA environment variable is not set. Entry points must bootstrap this before importing other modules.')
    return Path(workspace.strip())

def get_base_actions_directory(bot_directory: Path=None) -> Path:
    """
    Get base actions directory.
    
    Args:
        bot_directory: Optional bot directory path. If None, uses BOT_DIRECTORY env var.
    
    Returns:
        Path to base_actions directory (from bot_config.json or default to agile_bot/base_actions)
    """
    from ..utils import read_json_file
    
    if bot_directory is None:
        bot_directory = get_bot_directory()
    
    # Try to read from bot_config.json
    config_paths = [
        bot_directory / 'bot_config.json',
        bot_directory / 'config' / 'bot_config.json'
    ]
    
    python_workspace_root = get_python_workspace_root()
    
    for config_path in config_paths:
        if config_path.exists():
            try:
                config = read_json_file(config_path)
                base_actions_path = config.get('baseActionsPath')
                if base_actions_path:
                    # If relative path, resolve from workspace root
                    path = Path(base_actions_path)
                    if not path.is_absolute():
                        path = python_workspace_root / base_actions_path
                    return path
            except Exception:
                pass  # Fall through to default
    
    # Default: base_actions at workspace root level
    return python_workspace_root / 'agile_bot' / 'base_actions'

def get_behavior_folder(bot_name: str, behavior: str) -> Path:
    bot_directory = get_bot_directory()
    return bot_directory / 'behaviors' / behavior