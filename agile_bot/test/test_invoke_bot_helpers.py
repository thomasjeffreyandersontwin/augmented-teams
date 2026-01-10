"""
Common Test Helpers for Invoke Bot Tests

Provides reusable helpers for bot setup and assertions.
Self-contained for the new test area (agile_bot/test/).
"""
import json
from pathlib import Path

from agile_bot.src.bot.bot import Bot
from agile_bot.test.test_helpers import (
    create_actions_workflow_json,
    create_base_actions_structure,
    bootstrap_env,
    create_bot_config_file
)
from agile_bot.test.test_execute_behavior_actions import (
    create_minimal_guardrails_files
)


def setup_test_bot(tmp_path, behaviors: list[str]) -> tuple[Bot, Path]:
    """
    Setup test bot with behaviors for Invoke Bot tests.
    
    Uses the actual story_bot directory instead of creating a temp bot.
    Only creates a temp workspace directory for state files.
    
    Args:
        tmp_path: pytest tmp_path fixture (used only for workspace)
        behaviors: List of behavior names to use (e.g., ['shape', 'discovery'])
    
    Returns:
        tuple: (Bot instance, workspace_directory Path)
        
    Example:
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        bot.behaviors.navigate_to('shape')
    """
    from pathlib import Path
    
    # Get the actual story_bot directory
    repo_root = Path(__file__).parent.parent.parent
    bot_dir = repo_root / 'agile_bot' / 'bots' / 'story_bot'
    
    # Create temp workspace directory for state files
    workspace_dir = tmp_path / 'workspace'
    workspace_dir.mkdir(parents=True, exist_ok=True)

    # Bootstrap environment with actual bot_dir and temp workspace
    bootstrap_env(bot_dir, workspace_dir)
    
    # Load the actual bot
    config_path = bot_dir / 'bot_config.json'
    if not config_path.exists():
        config_path = bot_dir / 'config' / 'bot_config.json'
    
    bot = Bot(
        bot_name='story_bot',
        bot_directory=bot_dir,
        config_path=config_path
    )
    return bot, workspace_dir


def create_behavior_action_state(workspace_dir: Path, bot_name: str, 
                                  behavior: str, action: str,
                                  operation: str = 'instructions') -> Path:
    """
    Create behavior_action_state.json file with specified state.
    
    Args:
        workspace_dir: Workspace directory path
        bot_name: Bot name (e.g., 'story_bot')
        behavior: Behavior name (e.g., 'shape')
        action: Action name (e.g., 'clarify')
        operation: Operation name (default: 'instructions')
        
    Returns:
        Path: state_file path
        
    Example:
        state_file = create_behavior_action_state(
            workspace, 'story_bot', 'shape', 'clarify', 'instructions'
        )
    """
    state_data = {
        'current_behavior': f'{bot_name}.{behavior}',
        'current_action': f'{bot_name}.{behavior}.{action}',
        'operation': operation,
        'working_directory': str(workspace_dir),
        'timestamp': '2025-12-26T10:00:00.000000'
    }
    
    state_file = workspace_dir / 'behavior_action_state.json'
    state_file.write_text(json.dumps(state_data), encoding='utf-8')
    return state_file


def read_behavior_action_state(workspace_dir: Path) -> dict:
    """
    Read and parse behavior_action_state.json.
    
    Returns:
        dict: Parsed state data
        
    Example:
        state = read_behavior_action_state(workspace)
        assert state['current_behavior'] == 'story_bot.shape'
    """
    state_file = workspace_dir / 'behavior_action_state.json'
    assert state_file.exists(), "State file should exist"
    return json.loads(state_file.read_text(encoding='utf-8'))


def assert_bot_at_behavior_action(bot: Bot, behavior_name: str, 
                                   action_name: str):
    """
    Assert bot is at specified behavior and action.
    
    Example:
        assert_bot_at_behavior_action(bot, 'shape', 'clarify')
    """
    assert bot.behaviors.current.name == behavior_name
    assert bot.behaviors.current.actions.current_action_name == action_name


def assert_state_file_shows_behavior_action(workspace_dir: Path, 
                                              bot_name: str,
                                              behavior: str, 
                                              action: str):
    """
    Assert state file shows expected behavior and action.
    
    Example:
        assert_state_file_shows_behavior_action(
            workspace, 'story_bot', 'shape', 'clarify'
        )
    """
    state = read_behavior_action_state(workspace_dir)
    assert state['current_behavior'] == f'{bot_name}.{behavior}'
    assert state['current_action'].startswith(f'{bot_name}.{behavior}.{action}')


def assert_action_in_completed_list(workspace_dir: Path, bot_name: str,
                                      behavior: str, action: str):
    """
    Assert action appears in completed_actions list in state file.
    
    Example:
        assert_action_in_completed_list(workspace, 'story_bot', 'shape', 'clarify')
    """
    state = read_behavior_action_state(workspace_dir)
    completed = [a.get('action_state') for a in state.get('completed_actions', [])]
    assert f'{bot_name}.{behavior}.{action}' in completed


def assert_scope_is_set(bot: Bot, scope_type: str, scope_value: list):
    """
    Assert bot scope is set with specified type and value.
    
    Example:
        assert_scope_is_set(bot, 'story', ['Epic Name'])
    """
    assert bot.scope.type == scope_type
    assert bot.scope.value == scope_value
    assert bot.scope.is_active()


def assert_scope_is_cleared(bot: Bot):
    """
    Assert bot scope is cleared (not active).
    
    Example:
        assert_scope_is_cleared(bot)
    """
    assert not bot.scope.is_active()
    assert bot.scope.type is None


def read_activity_log(workspace_dir: Path) -> list:
    """
    Read and parse activity_log.json.
    
    Returns:
        list: Parsed activity log entries
        
    Example:
        activity_log = read_activity_log(workspace)
        assert len(activity_log) > 0
    """
    activity_log_file = workspace_dir / 'activity_log.json'
    if not activity_log_file.exists():
        return []
    return json.loads(activity_log_file.read_text(encoding='utf-8'))


def assert_activity_logged(workspace_dir: Path, action_state: str, 
                            event_type: str):
    """
    Assert action is logged in activity log with specified event type.
    
    Args:
        workspace_dir: Workspace directory path
        action_state: Action state (e.g., 'story_bot.shape.clarify')
        event_type: Event type (e.g., 'start', 'complete')
        
    Example:
        assert_activity_logged(workspace, 'story_bot.shape.clarify', 'start')
    """
    activity_log = read_activity_log(workspace_dir)
    matching_entries = [
        entry for entry in activity_log
        if entry.get('action_state') == action_state 
        and entry.get('event') == event_type
    ]
    assert len(matching_entries) > 0, \
        f"No {event_type} event found for {action_state} in activity log"
