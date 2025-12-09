from pathlib import Path
import os


def get_python_workspace_root() -> Path:
    """Return the repository root used for Python imports.

    This value is derived relative to this file's location and mirrors the
    previous behavior where callers used Path(__file__).parent.parent.parent...
    Use this for import-path resolution only (keeping import behavior stable).
    """
    return Path(__file__).parent.parent.parent.parent.parent


def get_bot_directory() -> Path:
    """Get bot directory from BOT_DIRECTORY environment variable.
    
    Entry points (MCP server, CLI) must bootstrap this environment variable
    before importing other modules. They should self-detect from their script
    location and set the env var.
    
    Returns:
        Path to bot directory (e.g., C:/dev/augmented-teams/agile_bot/bots/story_bot)
    
    Raises:
        RuntimeError: If BOT_DIRECTORY environment variable is not set
    """
    bot_dir = os.environ.get('BOT_DIRECTORY')
    if not bot_dir:
        raise RuntimeError(
            "BOT_DIRECTORY environment variable is not set. "
            "Entry points must bootstrap this before importing other modules."
        )
    return Path(bot_dir)


def get_workspace_directory() -> Path:
    """Get workspace directory from WORKING_AREA environment variable.

    Entry points (MCP server, CLI) must bootstrap this environment variable
    before importing other modules. They should read from agent.json and set
    the env var.

    The workspace directory is where content files are created (workflow_state.json,
    activity_log.json, docs/, etc.). This is different from the bot directory.

    Returns:
        Path to workspace directory where content files should be created
        
    Raises:
        RuntimeError: If WORKING_AREA environment variable is not set
    """
    workspace = os.environ.get('WORKING_AREA') or os.environ.get('WORKING_DIR')
    if not workspace:
        raise RuntimeError(
            "WORKING_AREA environment variable is not set. "
            "Entry points must bootstrap this before importing other modules."
        )
    return Path(workspace)


def get_behavior_folder(bot_name: str, behavior: str) -> Path:
    """Return the path to a behavior folder for a given bot.

    Args:
        bot_name: Name of the bot (e.g., 'story_bot')
        behavior: Name of the behavior (e.g., '1_shape', 'shape')

    Returns:
        Path to behavior folder in bot directory

    Example: 
        get_behavior_folder('story_bot', '1_shape') ->
        C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/1_shape
    """
    bot_directory = get_bot_directory()
    return bot_directory / 'behaviors' / behavior
