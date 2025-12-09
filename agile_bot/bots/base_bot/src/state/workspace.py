from pathlib import Path
from typing import Optional
import os


def get_python_workspace_root() -> Path:
    """Return the repository root used for Python imports.

    This value is derived relative to this file's location and mirrors the
    previous behavior where callers used Path(__file__).parent.parent.parent...
    Use this for import-path resolution only (keeping import behavior stable).
    """
    return Path(__file__).parent.parent.parent.parent.parent


def get_workspace_directory(workspace: Optional[Path] = None) -> Path:
    """Return the workspace directory used for file I/O.

    Return the workspace directory used for file I/O.

    Behavior:
    - If the environment variable `WORKING_AREA` (preferred) or `WORKING_DIR`
      is set, that value is returned (this makes the environment the single
      authoritative source for directing outputs).
    - Otherwise, if `workspace` is provided, it is returned.
    - If neither is available a RuntimeError is raised.
    """
    # Prefer an explicit environment-controlled working area so callers
    # can direct all outputs to a single folder regardless of invocation.
    env_working = os.environ.get('WORKING_AREA') or os.environ.get('WORKING_DIR')
    if env_working:
        return Path(env_working)

    raise RuntimeError(
        "WORKING_AREA (or WORKING_DIR) environment variable must be set to determine the workspace directory."
    )


def get_behavior_folder(bot_name: str, behavior: str, workspace: Path) -> Path:
    """Return the path to a behavior folder for a given bot.

    Example: get_behavior_folder('story_bot', '1_shape', workspace) ->
      <workspace>/agile_bot/bots/story_bot/behaviors/1_shape

    The `workspace` parameter is required and must be a `Path` pointing to
    the workspace directory used for file I/O.
    """
    workspace = get_workspace_directory(workspace)

    return workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior
