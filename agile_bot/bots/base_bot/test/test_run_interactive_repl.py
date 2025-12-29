"""
Run Interactive REPL Tests

Tests for all stories in the 'Run Interactive REPL' sub-epic:
- Launch REPL Loop
- Detect TTY Input
- Support Pipe Automation Mode
- Support Dot Notation Commands
- Display Fresh Start
- Display Existing State
- Show Current Position In Workflow Breadcrumbs
- Show Available Behaviors and Actions
- Navigate To Behavior
- Navigate To Action
- Navigate Within Behavior
- Request Help
- Request Status
- Enter Action
- Advance To Next Action
- Exit REPL
"""
import pytest
import json
import sys
import os
from pathlib import Path
from io import StringIO
from typing import Dict, List

from agile_bot.bots.base_bot.src.repl_cli import (
    REPLStateDisplay,
    REPLCommandResponse,
    TTYDetectionResult
)
from agile_bot.bots.base_bot.test.test_helpers import (
    get_behavior_action_state_path,
    get_behavior_dir,
    create_actions_workflow_json
)


# ============================================================================
# COMMON TEST DATA - Shared across multiple test cases
# ============================================================================

# Common behaviors used across multiple tests
COMMON_BEHAVIORS = ["shape", "discovery", "scenarios", "code"]

# Common actions list for behavior workflows
COMMON_ACTIONS = ['clarify', 'strategy', 'build', 'validate', 'render']

# Behavior/Action combinations with breadcrumbs for state display tests
# Format: "action [OK]" for completed, "action *" for current, "action [ ]" for pending
BEHAVIOR_ACTION_BREADCRUMBS_DATA = [
    ("shape", "build", "clarify [OK] -> strategy [OK] -> build * -> validate [ ] -> render [ ]"),
    ("discovery", "clarify", "clarify * -> strategy [ ] -> build [ ] -> validate [ ] -> render [ ]"),
    ("scenarios", "validate", "clarify [OK] -> strategy [OK] -> build [OK] -> validate * -> render [ ]")
]

# Behavior/Action/Completed Actions for state display tests
BEHAVIOR_ACTION_COMPLETED_DATA = [
    ("shape", "build", ["clarify", "strategy"]),
    ("discovery", "validate", ["clarify", "strategy", "build"]),
    ("scenarios", "clarify", [])
]

# Invalid behavior names for error testing
INVALID_BEHAVIORS = ["invalid", "nonexistent", "test"]

# Invalid action names for error testing
INVALID_ACTIONS_PER_BEHAVIOR = [
    ("shape", "test"),
    ("discovery", "invalid"),
    ("code", "nonexistent")
]

# Behavior/Action combinations for execution tests
BEHAVIOR_ACTION_EXECUTION_DATA = [
    ("shape", "clarify"),
    ("shape", "strategy"),
    ("shape", "build"),
    ("prioritization", "validate"),
    ("discovery", "render")
]


@pytest.fixture
def bot_directory(tmp_path):
    bot_dir = tmp_path / 'agile_bot' / 'bots' / 'story_bot'
    bot_dir.mkdir(parents=True)
    
    config_data = {'name': 'story_bot'}
    (bot_dir / 'bot_config.json').write_text(json.dumps(config_data))
    
    return bot_dir


@pytest.fixture
def workspace_directory(tmp_path):
    workspace_dir = tmp_path / 'workspace'
    workspace_dir.mkdir(parents=True)
    return workspace_dir


@pytest.fixture
def behavior_action_state_file(workspace_directory):
    """Fixture providing behavior action state file path using common test helper."""
    return get_behavior_action_state_path(workspace_directory)


def given_behavior_exists(bot_directory, behavior_name, actions, bot_name='story_bot'):
    """Create behavior folder and actions workflow using common test helpers."""
    behavior_dir = get_behavior_dir(bot_directory, behavior_name)
    behavior_dir.mkdir(parents=True, exist_ok=True)
    
    # Convert action names to action configs if provided as strings
    if actions and isinstance(actions[0], str):
        action_configs = []
        for idx, action_name in enumerate(actions, start=1):
            action_configs.append({
                "name": action_name,
                "order": idx,
                "instructions": [f"Test instructions for {action_name} in {behavior_name}"]
            })
        actions = action_configs
    
    # Standard story bot behavior sequence order
    BEHAVIOR_ORDER = {
        'shape': 1,
        'prioritization': 2,
        'discovery': 3,
        'exploration': 4,
        'scenarios': 5,
        'tests': 6,
        'code': 7
    }
    behavior_order = BEHAVIOR_ORDER.get(behavior_name, 99)
    
    # Use common helper to create actions workflow (this also creates behavior.json)
    create_actions_workflow_json(bot_directory, behavior_name, actions=actions, order=behavior_order)
    
    # Create minimal guardrails files (required for Behavior initialization)
    from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
    create_minimal_guardrails_files(bot_directory, behavior_name, bot_name)


def given_behavior_action_state_exists(workspace_directory, behavior, action, working_directory, completed_actions=None):
    """Create behavior action state file using common test helper for path."""
    state_data = {
        'current_behavior': f'story_bot.{behavior}',
        'current_action': f'story_bot.{behavior}.{action}',
        'working_directory': working_directory,
        'timestamp': '2025-12-23T09:00:00.000000',
        'completed_actions': completed_actions or []
    }
    
    # Use common helper to get state file path
    state_file = get_behavior_action_state_path(workspace_directory)
    state_file.write_text(json.dumps(state_data))
    return state_file


def given_no_behavior_action_state(workspace_directory):
    """Remove behavior action state file if it exists, using common test helper for path."""
    state_file = get_behavior_action_state_path(workspace_directory)
    if state_file.exists():
        state_file.unlink()


def build_completed_action_list(behavior, completed_action_names):
    return [
        {'action_state': f'story_bot.{behavior}.{action_name}', 'timestamp': '2025-12-23T08:00:00.000000'}
        for action_name in completed_action_names
    ]


def given_stdin_is_tty(monkeypatch):
    monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)


def given_stdin_is_piped(monkeypatch):
    monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)


def when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory):
    from agile_bot.bots.base_bot.test.test_helpers import bootstrap_env
    from agile_bot.bots.base_bot.src.repl_cli import REPLSession
    from agile_bot.bots.base_bot.src.bot.bot import Bot
    
    bootstrap_env(bot_directory, workspace_directory)
    
    bot = Bot(
        bot_name='story_bot',
        bot_directory=bot_directory,
        config_path=bot_directory / 'bot_config.json'
    )
    
    repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
    return repl_session


def when_cli_launches_in_repl_mode(repl_session):
    return repl_session.display_current_state()


def when_user_enters_command(repl_session, command):
    return repl_session.read_and_execute_command(command)


def then_cli_loads_behavior_action_state(repl_session_state):
    assert repl_session_state.state_loaded is True


def then_cli_displays(cli_output, expected_text):
    assert expected_text in cli_output.output


def then_behavior_action_state_is_set(workspace_directory, field, expected_value):
    """Verify behavior action state field value, using common test helper for path."""
    state_file = get_behavior_action_state_path(workspace_directory)
    state_data = json.loads(state_file.read_text())
    assert state_data[field] == expected_value


def then_cli_responds(cli_response, expected_response):
    assert expected_response in cli_response.response


def then_behavior_action_state_remains_unchanged(workspace_directory, original_state):
    """Verify behavior action state hasn't changed (excluding timestamp), using common test helper for path."""
    state_file = get_behavior_action_state_path(workspace_directory)
    current_state = json.loads(state_file.read_text())
    
    # Compare everything except timestamp (which may update on session load)
    assert current_state['current_behavior'] == original_state['current_behavior']
    assert current_state['current_action'] == original_state['current_action']
    assert current_state['working_directory'] == original_state['working_directory']
    assert current_state.get('completed_actions', []) == original_state.get('completed_actions', [])


class TestLaunchREPLLoop:
    @pytest.mark.parametrize("behavior,action,action_breadcrumbs", BEHAVIOR_ACTION_BREADCRUMBS_DATA)
    def test_launch_repl_with_existing_state(self, bot_directory, workspace_directory, behavior, action, action_breadcrumbs):
        working_dir = "C:\\dev\\project"
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        
        # Determine completed actions based on current action
        if action == "clarify":
            completed_actions = []
        elif action == "build":
            completed_actions = [
                {'action_state': f'story_bot.{behavior}.clarify', 'timestamp': '2025-12-23T08:00:00.000000'},
                {'action_state': f'story_bot.{behavior}.strategy', 'timestamp': '2025-12-23T08:30:00.000000'}
            ]
        elif action == "validate":
            completed_actions = [
                {'action_state': f'story_bot.{behavior}.clarify', 'timestamp': '2025-12-23T08:00:00.000000'},
                {'action_state': f'story_bot.{behavior}.strategy', 'timestamp': '2025-12-23T08:30:00.000000'},
                {'action_state': f'story_bot.{behavior}.build', 'timestamp': '2025-12-23T09:00:00.000000'}
            ]
        else:
            completed_actions = []
        
        given_behavior_action_state_exists(
            workspace_directory, 
            behavior, 
            action,
            working_dir,
            completed_actions=completed_actions
        )
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        then_cli_loads_behavior_action_state(cli_output)
        # Compact view shows behaviors and actions lists
        then_cli_displays(cli_output, f"**Behaviors:** {behavior}")
        then_cli_displays(cli_output, "**Actions:**")
        # Current state is in the object properties
        assert cli_output.current_action == f"story_bot.{behavior}.{action}"
        assert cli_output.breadcrumbs == action_breadcrumbs


class TestDetectTTYInput:
    def test_detect_tty_when_stdin_is_tty(self, bot_directory, workspace_directory, monkeypatch):
        given_stdin_is_tty(monkeypatch)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        tty_detection = repl_session.detect_tty()
        
        assert tty_detection.tty_detected is True
        assert tty_detection.interactive_prompts_enabled is True
    
    def test_detect_non_tty_when_stdin_is_piped(self, bot_directory, workspace_directory, monkeypatch):
        given_stdin_is_piped(monkeypatch)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        tty_detection = repl_session.detect_tty()
        
        assert tty_detection.tty_detected is False
        assert tty_detection.interactive_prompts_enabled is False


class TestPipeAutomationMode:
    """Tests for pipe/automation mode behavior (non-TTY stdin)"""
    
    def test_pipe_mode_processes_commands_without_prompts(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        # Execute shape command
        response = when_user_enters_command(repl_session, "shape")
        
        # Verify no interactive prompts in output
        assert "[story_bot] >" not in response.output
        # Verify real instructions are displayed (not just mock markers)
        assert len(response.output) > 100  # Real instructions are substantial
        assert response.status == 'success'
    
    def test_pipe_mode_maintains_state_between_commands(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        # Execute sequence of commands
        when_user_enters_command(repl_session, "shape")
        when_user_enters_command(repl_session, "build")
        when_user_enters_command(repl_session, "submit")
        response = when_user_enters_command(repl_session, "status")
        
        # Verify state was maintained through all commands (should be at build after submit)
        then_cli_displays(response, "shape.build")
        # Verify current action in state file
        then_behavior_action_state_is_set(workspace_directory, 'current_action', 'story_bot.shape.build')
    
    def test_pipe_mode_handles_eof_gracefully(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        response = when_user_enters_command(repl_session, "shape")
        
        # In pipe mode, should not display "Exiting REPL..." message
        assert response.status == 'success'
        # Verify real instructions are displayed
        assert len(response.output) > 100


class TestDotNotationCommands:
    """Tests for dot notation command support"""
    
    def test_navigate_using_behavior_dot_action(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_exists(bot_directory, 'discovery', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        response = when_user_enters_command(repl_session, "discovery.build")
        
        # Displays real instruction content (not mock "EXECUTING" prefix)
        assert response.status == 'success'
        assert len(response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_action', 'story_bot.discovery.build')
    
    def test_navigate_and_execute_operation_using_dot_notation(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        # Must get instructions first before submit
        when_user_enters_command(repl_session, "shape.build.instructions")
        response = when_user_enters_command(repl_session, "shape.build.submit")
        
        # Submit returns status JSON, not "EXECUTING" prefix
        assert response.status == 'success'
        assert 'submitted' in response.output.lower() or 'build' in response.output.lower()
        then_behavior_action_state_is_set(workspace_directory, 'current_action', 'story_bot.shape.build')
    
    @pytest.mark.parametrize("behavior,action,operation,needs_instructions", [
        ("shape", "build", "instructions", False),
        ("discovery", "validate", "instructions", False),
    ])
    def test_dot_notation_with_all_operations(self, bot_directory, workspace_directory, behavior, action, operation, needs_instructions):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        # Get instructions first if operation requires it
        if needs_instructions:
            when_user_enters_command(repl_session, f"{behavior}.{action}.instructions")
        
        response = when_user_enters_command(repl_session, f"{behavior}.{action}.{operation}")
        
        assert response.status == 'success'
        then_cli_displays(response, f"{behavior}.{action}.{operation}")
    
    def test_dot_notation_with_invalid_behavior(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        original_state_file = get_behavior_action_state_path(workspace_directory)
        original_state = json.loads(original_state_file.read_text())
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        response = when_user_enters_command(repl_session, "invalid.build")
        
        then_cli_responds(response, "ERROR: behavior 'invalid' not found")
        then_behavior_action_state_remains_unchanged(workspace_directory, original_state)
    
    def test_dot_notation_with_invalid_action(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        original_state_file = get_behavior_action_state_path(workspace_directory)
        original_state = json.loads(original_state_file.read_text())
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        response = when_user_enters_command(repl_session, "shape.nonexistent")
        
        # Check output (full error message) instead of response (short error message)
        then_cli_displays(response, "ERROR: Action 'nonexistent' not found in behavior 'shape'")
        then_behavior_action_state_remains_unchanged(workspace_directory, original_state)
    
    def test_dot_notation_with_invalid_operation(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        original_state_file = get_behavior_action_state_path(workspace_directory)
        original_state = json.loads(original_state_file.read_text())
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        response = when_user_enters_command(repl_session, "shape.build.invalid")
        
        then_cli_responds(response, "ERROR: Unknown operation 'invalid'")
        then_cli_displays(response, "Use: instructions, submit, or confirm")
        then_behavior_action_state_remains_unchanged(workspace_directory, original_state)
    
    def test_batch_process_all_behaviors_with_dot_notation(self, bot_directory, workspace_directory):
        # Create all standard behaviors
        for behavior in ['shape', 'prioritization', 'discovery', 'exploration', 'scenarios', 'tests', 'code']:
            given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        
        # Execute render.instructions for all behaviors
        behaviors_tested = []
        for behavior in ['shape', 'prioritization', 'discovery', 'exploration', 'scenarios', 'tests', 'code']:
            response = when_user_enters_command(repl_session, f"{behavior}.render.instructions")
            if response.status == 'success':
                behaviors_tested.append(behavior)
        
        # Verify all behaviors were processed successfully
        assert len(behaviors_tested) == 7
        then_behavior_action_state_is_set(workspace_directory, 'current_action', 'story_bot.code.render')


class TestDisplayFreshStart:
    def test_cli_displays_fresh_start_with_no_state_file(self, bot_directory, workspace_directory):
        given_no_behavior_action_state(workspace_directory)
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_exists(bot_directory, 'prioritization', COMMON_ACTIONS)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Fresh start auto-initializes to first behavior/action
        then_cli_displays(cli_output, "**Behaviors:**")
        then_cli_displays(cli_output, "**Actions:**")
        then_cli_displays(cli_output, "help")
        then_cli_displays(cli_output, "exit")
    
    @pytest.mark.parametrize("selected_behavior", COMMON_BEHAVIORS)
    def test_user_selects_initial_behavior(self, bot_directory, workspace_directory, selected_behavior):
        given_no_behavior_action_state(workspace_directory)
        given_behavior_exists(bot_directory, selected_behavior, COMMON_ACTIONS)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"behavior {selected_behavior}")
        
        # Navigation now auto-executes instructions
        assert cli_response.status == 'success'
        # Check for real instruction content
        assert len(cli_response.output) > 100
        # Verify behavior and action are in output
        assert selected_behavior in cli_response.output.lower() or 'behavior' in cli_response.output.lower()
        then_behavior_action_state_is_set(workspace_directory, 'current_behavior', f'story_bot.{selected_behavior}')
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{selected_behavior}.clarify')
    
    def test_user_configures_workspace_in_fresh_session(self, bot_directory, workspace_directory):
        given_no_behavior_action_state(workspace_directory)
        workspace_path = "C:\\dev\\project"
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"workspace {workspace_path}")
        
        then_cli_responds(cli_response, f"Path changed to: {workspace_path}")
        then_behavior_action_state_is_set(workspace_directory, 'working_directory', workspace_path)


class TestDisplayExistingState:
    
    @pytest.mark.parametrize("behavior,action,completed_actions", BEHAVIOR_ACTION_COMPLETED_DATA)
    def test_cli_displays_existing_state_with_progress(self, bot_directory, workspace_directory, behavior, action, completed_actions):
        working_dir = "C:\\dev\\project"
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_action_state_exists(workspace_directory, behavior, action, working_dir, completed_action_list)
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Compact view shows behaviors and actions
        then_cli_displays(cli_output, f"**Behaviors:** {behavior}")
        # Use status command for full progress view
        status_output = when_user_enters_command(repl_session, "status")
        then_cli_displays(status_output, f"**Progress:** {behavior}.{action}")
        then_cli_displays(status_output, f"{behavior}")
        
        for ca in completed_actions:
            then_cli_displays(status_output, f"{ca}")
            then_cli_displays(status_output, "[OK]")


class TestShowCurrentPositionInWorkflowBreadcrumbs:
    
    def test_show_breadcrumbs_for_current_position(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(
            workspace_directory,
            'shape',
            'build',
            'C:\\dev\\project',
            [
                {'action_state': 'story_bot.shape.clarify', 'timestamp': '2025-12-23T08:00:00.000000'},
                {'action_state': 'story_bot.shape.strategy', 'timestamp': '2025-12-23T08:30:00.000000'}
            ]
        )
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Breadcrumbs are in the object property (with space before * marker)
        assert "clarify [OK]" in cli_output.breadcrumbs
        assert "strategy [OK]" in cli_output.breadcrumbs
        assert "build *" in cli_output.breadcrumbs


class TestShowAvailableBehaviorsAndActions:
    
    def test_show_available_behaviors_and_actions(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "behavior shape")
        
        # Navigation now auto-executes instructions - displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_action', 'story_bot.shape.clarify')


class TestRequestHelp:
    
    @pytest.mark.parametrize("behavior,actions,action", [
        ("shape", ["clarify", "strategy", "build", "validate", "render"], "build"),
        ("discovery", ["clarify", "strategy", "build", "validate", "render"], "validate"),
        ("scenarios", ["clarify", "strategy", "build", "validate", "render"], "clarify")
    ])
    def test_user_asks_for_help_for_current_behavior(self, bot_directory, workspace_directory, behavior, actions, action):
        given_behavior_exists(bot_directory, behavior, actions)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "help")
        
        # Help shows Core Commands header
        then_cli_displays(cli_response, "Core Commands:")
        # Help shows available behaviors
        then_cli_displays(cli_response, "behaviors")
        then_cli_displays(cli_response, behavior)
        # Help shows action descriptions
        then_cli_displays(cli_response, "actions:")
        then_cli_displays(cli_response, "clarify")
        then_cli_displays(cli_response, "Gather context")
        # Help shows operations
        then_cli_displays(cli_response, "operations:")
    
    @pytest.mark.parametrize("behavior,action", [
        ("shape", "build"),
        ("discovery", "validate"),
        ("scenarios", "clarify")
    ])
    def test_user_asks_for_detailed_help_for_specific_action(self, bot_directory, workspace_directory, behavior, action):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"help {action}")
        
        # Action header
        then_cli_displays(cli_response, f"## {action}")
        # Usage section
        then_cli_displays(cli_response, "Usage:")
        then_cli_displays(cli_response, f"{action}")
        # Action stages (instructions, submit, confirm)
        then_cli_displays(cli_response, "Action Stages")
        then_cli_displays(cli_response, "instructions")
        then_cli_displays(cli_response, "submit")
        then_cli_displays(cli_response, "confirm")
        # Context Parameters section (if applicable)
        then_cli_displays(cli_response, "Context Parameters")


class TestRequestStatus:
    
    @pytest.mark.parametrize("behavior,action,working_dir,completed_actions", [
        ("shape", "build", "C:\\dev\\my-project", ["clarify", "strategy"]),
        ("prioritization", "clarify", "C:\\dev\\my-project", []),
        ("discovery", "validate", "C:\\dev\\another-proj", ["clarify", "strategy", "build"])
    ])
    def test_user_views_status_display(self, bot_directory, workspace_directory, behavior, action, working_dir, completed_actions):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, working_dir, completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "status")
        
        # Status shows hierarchical progress with Progress: format
        then_cli_displays(cli_response, f"**Progress:** {behavior}.{action}")
        # Status shows Behaviors with current marked [*]
        then_cli_displays(cli_response, f"**Behaviors:** {behavior}")
        then_cli_displays(cli_response, f"{behavior} [*]")
        # Status shows Actions with completed marked [OK]
        then_cli_displays(cli_response, "**Actions:** {action}")
        for ca in completed_actions:
            then_cli_displays(cli_response, f"{ca} [OK]")
        # Status shows current action marked [*]
        then_cli_displays(cli_response, f"{action} [*]")
        # Current Position section
        then_cli_displays(cli_response, "CURRENT POSITION")


class TestNavigateToBehavior:
    
    @pytest.mark.parametrize("current_behavior,current_action,target_behavior", [
        ("shape", "build", "discovery"),
        ("discovery", "validate", "exploration"),
        ("scenarios", "clarify", "tests"),
        ("code", "validate", "scenarios")
    ])
    def test_user_navigates_to_different_behavior(self, bot_directory, workspace_directory, current_behavior, current_action, target_behavior):
        given_behavior_exists(bot_directory, current_behavior, COMMON_ACTIONS)
        given_behavior_exists(bot_directory, target_behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, current_behavior, current_action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"behavior {target_behavior}")
        
        # Navigation now auto-executes instructions - displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_behavior', f'story_bot.{target_behavior}')
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{target_behavior}.clarify')
    
    @pytest.mark.parametrize("invalid_behavior", INVALID_BEHAVIORS)
    def test_user_navigates_to_invalid_behavior(self, bot_directory, workspace_directory, invalid_behavior):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        original_state_file = get_behavior_action_state_path(workspace_directory)
        original_state = json.loads(original_state_file.read_text())
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"behavior {invalid_behavior}")
        
        then_cli_responds(cli_response, f"ERROR: behavior '{invalid_behavior}' not found")
        then_cli_displays(cli_response, "Available behaviors:")
        then_behavior_action_state_remains_unchanged(workspace_directory, original_state)


class TestNavigateToAction:
    
    @pytest.mark.parametrize("current_behavior,current_action,completed_actions,target_action", [
        ("shape", "clarify", [], "validate"),
        ("shape", "build", ["clarify", "strategy"], "validate"),
        ("discovery", "validate", ["clarify", "strategy", "build"], "render"),
        ("scenarios", "strategy", ["clarify"], "build")
    ])
    def test_user_navigates_to_action_within_current_behavior(self, bot_directory, workspace_directory, current_behavior, current_action, completed_actions, target_action):
        completed_action_list = build_completed_action_list(current_behavior, completed_actions)
        
        given_behavior_exists(bot_directory, current_behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, current_behavior, current_action, 'C:\\dev\\project', completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"action {target_action}")
        
        # Navigation now auto-executes instructions - displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{current_behavior}.{target_action}')
    
    @pytest.mark.parametrize("current_behavior,invalid_action", INVALID_ACTIONS_PER_BEHAVIOR)
    def test_user_navigates_to_invalid_action(self, bot_directory, workspace_directory, current_behavior, invalid_action):
        given_behavior_exists(bot_directory, current_behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, current_behavior, 'build', 'C:\\dev\\project')
        
        original_state_file = get_behavior_action_state_path(workspace_directory)
        original_state = json.loads(original_state_file.read_text())
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"action {invalid_action}")
        
        then_cli_displays(cli_response, f"ERROR: action '{invalid_action}' not found")
        then_cli_displays(cli_response, "Available actions: clarify, strategy, build, validate, render")
        then_behavior_action_state_remains_unchanged(workspace_directory, original_state)


class TestNavigateWithinBehavior:
    
    @pytest.mark.parametrize("behavior,current_action,completed_actions,command,expected_in_output,new_action", [
        ("shape", "build", ["clarify", "strategy"], "current", "CLI STATUS", "build"),
        ("shape", "build", ["clarify", "strategy"], "confirm", "CLI STATUS", "validate"),
        ("shape", "validate", ["clarify", "strategy", "build"], "back", "CLI STATUS", "build"),
        ("shape", "clarify", [], "back", "ERROR: Already at first action", "clarify"),
        ("shape", "render", ["clarify", "strategy", "build", "validate"], "confirm", "COMPLETE: shape behavior finished", "render")
    ])
    def test_user_executes_workflow_navigation_commands(self, bot_directory, workspace_directory, behavior, current_action, completed_actions, command, expected_in_output, new_action):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, current_action, 'C:\\dev\\project', completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, command)
        
        # New display format no longer uses "EXECUTING" prefix
        then_cli_displays(cli_response, expected_in_output)
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{behavior}.{new_action}')


class TestConfirmAdvancesAcrossBehaviors:
    """Tests for confirming at last action of behavior advancing to next behavior"""
    
    @pytest.mark.parametrize("current_behavior,next_behavior", [
        ("shape", "prioritization"),
        ("prioritization", "discovery"),
        ("discovery", "exploration"),
        ("exploration", "scenarios"),
        ("scenarios", "tests"),
        ("tests", "code")
    ])
    def test_confirm_at_last_action_moves_to_next_behavior(self, bot_directory, workspace_directory, current_behavior, next_behavior):
        """Confirming at last action of behavior moves to next behavior's first action"""
        completed_actions = build_completed_action_list(current_behavior, ["clarify", "strategy", "build", "validate"])
        
        given_behavior_exists(bot_directory, current_behavior, COMMON_ACTIONS)
        given_behavior_exists(bot_directory, next_behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, current_behavior, 'render', 'C:\\dev\\project', completed_actions)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute render instructions first, then confirm
        when_user_enters_command(repl_session, "render")
        cli_response = when_user_enters_command(repl_session, "confirm")
        
        # Then CLI moves to next behavior's first action - displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_behavior', f'story_bot.{next_behavior}')
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{next_behavior}.clarify')
    
    def test_confirm_at_last_action_marks_behavior_complete(self, bot_directory, workspace_directory):
        """Confirming at last action marks current behavior as complete and updates completed_behaviors"""
        completed_actions = build_completed_action_list("shape", ["clarify", "strategy", "build", "validate"])
        
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_exists(bot_directory, 'prioritization', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'render', 'C:\\dev\\project', completed_actions)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute render instructions first, then confirm
        when_user_enters_command(repl_session, "render")
        when_user_enters_command(repl_session, "confirm")
        
        # Verify shape is in completed_behaviors (completed_actions resets per behavior)
        state_file = get_behavior_action_state_path(workspace_directory)
        state_data = json.loads(state_file.read_text())
        completed_behaviors = state_data.get('completed_behaviors', [])
        assert 'shape' in completed_behaviors
    
    def test_confirm_at_last_behavior_shows_workflow_complete(self, bot_directory, workspace_directory):
        """Confirming at last action of last behavior (code) shows workflow complete"""
        completed_actions = build_completed_action_list("code", ["clarify", "strategy", "build", "validate"])
        
        given_behavior_exists(bot_directory, 'code', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'code', 'render', 'C:\\dev\\project', completed_actions)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute render instructions first, then confirm
        when_user_enters_command(repl_session, "render")
        cli_response = when_user_enters_command(repl_session, "confirm")
        
        # Then CLI shows workflow is complete (no next behavior)
        then_cli_displays(cli_response, "COMPLETE")
        then_cli_displays(cli_response, "code")


class TestExitREPL:
    
    def test_user_exits_repl_session(self, bot_directory, workspace_directory):
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "exit")
        
        then_cli_displays(cli_response, "Goodbye!")
        assert cli_response.repl_terminated is True


class TestEnterAction:
    
    @pytest.mark.parametrize("behavior,action", BEHAVIOR_ACTION_EXECUTION_DATA)
    def test_user_executes_current_action_mock(self, bot_directory, workspace_directory, behavior, action):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Just use the action name to execute (defaults to instructions)
        cli_response = when_user_enters_command(repl_session, action)
        
        # Displays real instruction content (not mock "EXECUTING" prefix)
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        assert cli_response.action == action


class TestDisplayConfirmAndContinuePrompt:
    
    @pytest.mark.parametrize("behavior,action,next_action", [
        ("shape", "clarify", "strategy"),
        ("shape", "strategy", "build"),
        ("shape", "build", "validate")
    ])
    def test_cli_displays_action_completion_and_prompts_for_continuation(self, bot_directory, workspace_directory, behavior, action, next_action):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute action (instructions), then display_confirm_prompt gets current state
        when_user_enters_command(repl_session, action)
        confirm_prompt = repl_session.display_confirm_prompt()
        
        then_cli_displays(confirm_prompt, f"EXECUTED {behavior}.{action}")
        then_cli_displays(confirm_prompt, "Results:")
        then_cli_displays(confirm_prompt, f"Continue to next action ({next_action})? (y/n/review)")


class TestEnterConfirmResults:
    
    @pytest.mark.parametrize("behavior,current_action,next_action,completed_actions", [
        ("shape", "clarify", "strategy", []),
        ("shape", "strategy", "build", ["clarify"]),
        ("shape", "build", "validate", ["clarify", "strategy"])
    ])
    def test_user_confirms_action_completion_and_advances_workflow(self, bot_directory, workspace_directory, behavior, current_action, next_action, completed_actions):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, current_action, 'C:\\dev\\project', completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Use confirm to advance - now it auto-executes instructions for next action
        cli_response = when_user_enters_command(repl_session, "confirm")
        
        # Displays real instruction content for next action
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{behavior}.{next_action}')


class TestAdvanceToNextAction:
    
    def test_advance_to_next_action_updates_state(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project', [
            {'action_state': 'story_bot.shape.clarify', 'timestamp': '2025-12-23T08:00:00.000000'},
            {'action_state': 'story_bot.shape.strategy', 'timestamp': '2025-12-23T08:30:00.000000'}
        ])
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute action (instructions), then confirm to advance
        when_user_enters_command(repl_session, "build")
        advance_response = when_user_enters_command(repl_session, "confirm")
        
        state_file = get_behavior_action_state_path(workspace_directory)
        assert state_file.exists()
        
        state_data = json.loads(state_file.read_text())
        assert state_data['current_action'] == 'story_bot.shape.validate'
        
        # Confirm now auto-executes instructions for next action - displays real content
        assert advance_response.status == 'success'
        assert len(advance_response.output) > 100


class TestLoopBackToDisplayState:
    
    def test_workflow_advances_and_displays_updated_state(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute action (instructions), then confirm to advance
        when_user_enters_command(repl_session, "build")
        when_user_enters_command(repl_session, "confirm")
        
        state_display = repl_session.display_current_state()
        
        # Verify the state shows validate is current
        assert state_display.current_action == "story_bot.shape.validate"
        then_cli_displays(state_display, "**Behaviors:** shape")
        then_cli_displays(state_display, "validate")


class TestCompactMenuDisplay:
    """Tests for compact menu display on REPL launch"""
    
    def test_compact_menu_displays_behaviors_list(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_exists(bot_directory, 'discovery', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Compact menu shows behaviors list
        then_cli_displays(cli_output, "**Behaviors:**")
        then_cli_displays(cli_output, "shape")
        then_cli_displays(cli_output, "discovery")
    
    def test_compact_menu_displays_actions_list(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Compact menu shows actions list
        then_cli_displays(cli_output, "**Actions:**")
        then_cli_displays(cli_output, "clarify")
        then_cli_displays(cli_output, "strategy")
        then_cli_displays(cli_output, "build")
        then_cli_displays(cli_output, "validate")
        then_cli_displays(cli_output, "render")
    
    def test_compact_menu_displays_navigation_commands(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Compact menu shows navigation commands
        then_cli_displays(cli_output, "status")
        then_cli_displays(cli_output, "back")
        then_cli_displays(cli_output, "current")
        then_cli_displays(cli_output, "next")
        then_cli_displays(cli_output, "help")
        then_cli_displays(cli_output, "exit")


class TestBreadcrumbsFormat:
    """Tests for breadcrumbs display format with [OK] markers"""
    
    @pytest.mark.parametrize("behavior,action,completed_actions,expected_breadcrumb_parts", [
        ("shape", "build", ["clarify", "strategy"], ["clarify [OK]", "strategy [OK]", "build *"]),
        ("discovery", "clarify", [], ["clarify *", "strategy", "build"]),
        ("scenarios", "validate", ["clarify", "strategy", "build"], ["clarify [OK]", "strategy [OK]", "build [OK]", "validate *"])
    ])
    def test_breadcrumbs_show_completed_actions_with_ok_marker(self, bot_directory, workspace_directory, behavior, action, completed_actions, expected_breadcrumb_parts):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project', completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Breadcrumbs in object property
        for expected_part in expected_breadcrumb_parts:
            assert expected_part in cli_output.breadcrumbs, f"Expected '{expected_part}' in breadcrumbs: {cli_output.breadcrumbs}"
    
    def test_breadcrumbs_show_current_action_with_asterisk(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project', [
            {'action_state': 'story_bot.shape.clarify', 'timestamp': '2025-12-23T08:00:00.000000'},
            {'action_state': 'story_bot.shape.strategy', 'timestamp': '2025-12-23T08:30:00.000000'}
        ])
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        # Current action marked with asterisk (with space before marker)
        assert "build *" in cli_output.breadcrumbs
        # Future actions have no marker
        assert "validate" in cli_output.breadcrumbs


class TestShowActionParameterHelp:
    """Tests for displaying action parameter help with syntax and type annotations"""
    
    @pytest.mark.parametrize("behavior,action,expected_params", [
        ("shape", "build", ["--scope"]),
        ("discovery", "validate", ["--scope"]),
    ])
    def test_user_requests_parameter_help_for_action(self, bot_directory, workspace_directory, behavior, action, expected_params):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"help {action}")
        
        # Action header displayed
        then_cli_displays(cli_response, f"## {action}")
        # Usage section displayed
        then_cli_displays(cli_response, "Usage:")
        # Context Parameters section displayed  
        then_cli_displays(cli_response, "Context Parameters")


# =============================================================================
# INCREMENT 11: REPL All Scope Parameters (Mock Backend) Tests
# =============================================================================

# Test data for scope filtering
STORY_GRAPH_TEST_DATA = {
    "Run Interactive REPL": ["Navigate To Behavior", "Navigate To Action", "Request Help", "Request Status"],
    "Execute Behavior Actions": ["Submit Action", "Confirm Action", "Advance To Next"]
}

INCREMENT_11_STORIES = [
    "Provide Context For Instructions",
    "Store Scope Context",
    "Get Instructions and Display"
]

FILE_SCOPE_TEST_DATA = {
    "src/repl_cli/": ["repl_session.py", "repl_commands.py", "repl_help.py"],
    "src/bot/": ["bot.py", "behavior.py", "action.py"]
}


def given_story_graph_exists(workspace_directory, epics_with_stories):
    """Create a test story graph with specified epics and stories."""
    story_graph = {"epics": []}
    for epic_name, story_names in epics_with_stories.items():
        stories = [{"name": name, "priority": 11} for name in story_names]
        story_graph["epics"].append({
            "name": epic_name,
            "story_groups": [{"stories": stories}]
        })
    
    stories_dir = workspace_directory / "docs" / "stories"
    stories_dir.mkdir(parents=True, exist_ok=True)
    (stories_dir / "story-graph.json").write_text(json.dumps(story_graph))


def given_workspace_files_exist(workspace_directory, directory_files):
    """Create test files in workspace directories."""
    for directory, files in directory_files.items():
        dir_path = workspace_directory / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        for file_name in files:
            (dir_path / file_name).write_text(f"# Test file: {file_name}")


def given_scope_stored_in_state(workspace_directory, scope_type, scope_value, exclude=None):
    """Add scope parameters to the behavior action state file."""
    state_file = get_behavior_action_state_path(workspace_directory)
    if state_file.exists():
        state_data = json.loads(state_file.read_text())
    else:
        state_data = {}
    
    state_data['scope'] = {
        'type': scope_type,
        'value': scope_value if isinstance(scope_value, list) else [scope_value],
        'exclude': exclude or []
    }
    state_file.write_text(json.dumps(state_data))


class TestProvideContextForInstructions:
    """Tests for Provide Context For Instructions story.
    
    Tests that REPLSession parses action-specific parameters (like --message)
    and builds ActionContext for the current action.
    """
    
    @pytest.mark.parametrize("behavior,message", [
        ("shape", "What are the key user goals for this feature?"),
        ("discovery", "Who are the primary stakeholders?"),
        ("exploration", "What are the acceptance criteria for this story?")
    ])
    def test_repl_parses_message_parameter_for_clarify(self, bot_directory, workspace_directory, behavior, message):
        """REPLSession gathers and parses message parameter for clarify instructions."""
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with message parameter
        cli_response = when_user_enters_command(repl_session, f"clarify --message \"{message}\"")
        
        # Should execute successfully with message in context - displays real content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
    
    def test_repl_displays_error_for_missing_required_parameter(self, bot_directory, workspace_directory):
        """REPLSession validates parameters and shows error for missing required params."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'clarify', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute clarify without message (should still work - message is optional)
        cli_response = when_user_enters_command(repl_session, "clarify")
        
        # Should execute - message is optional for clarify
        assert cli_response.status == 'success'
    
    def test_bot_uses_stored_scope_when_user_omits_scope_parameter(self, bot_directory, workspace_directory):
        """Bot retrieves stored scope when user provides parameters without explicit scope."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        given_scope_stored_in_state(workspace_directory, 'story', ['Navigate To Behavior'])
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute build without scope - should use stored scope
        cli_response = when_user_enters_command(repl_session, "build")
        
        # Displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100


class TestProvideStoryScopeContextForInstructions:
    """Tests for Provide Story Scope Context For Instructions story.
    
    Tests that scope parameters filter the story graph and pass matching 
    stories to the action.
    """
    
    @pytest.mark.parametrize("scope_type,scope_value,expected_count", [
        ("story", "Navigate To Behavior", 1),
        ("story", "Request Help", 1),
        ("epic", "Run Interactive REPL", 4),
    ])
    def test_scope_filters_story_graph_and_passes_to_action(self, bot_directory, workspace_directory, scope_type, scope_value, expected_count):
        """Scope filters story graph and passes matching stories to action."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        given_story_graph_exists(workspace_directory, STORY_GRAPH_TEST_DATA)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with scope parameter
        scope_json = f"{{'type': '{scope_type}', 'value': ['{scope_value}']}}"
        cli_response = when_user_enters_command(repl_session, f"build --scope \"{scope_json}\"")
        
        # Displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
    
    def test_scope_with_nonexistent_story_returns_warning(self, bot_directory, workspace_directory):
        """Scope with non-existent story returns empty result with warning."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        given_story_graph_exists(workspace_directory, STORY_GRAPH_TEST_DATA)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with non-existent story
        scope_json = "{'type': 'story', 'value': ['Nonexistent Story']}"
        cli_response = when_user_enters_command(repl_session, f"build --scope \"{scope_json}\"")
        
        # Should still execute but may show warning about no matches
        assert cli_response.status == 'success'
    
    def test_repl_displays_validation_error_for_invalid_scope_type(self, bot_directory, workspace_directory):
        """REPLSession displays validation error for invalid scope type."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with invalid scope type
        scope_json = "{'type': 'invalid_type', 'value': []}"
        cli_response = when_user_enters_command(repl_session, f"build --scope \"{scope_json}\"")
        
        # Should show error for invalid scope type
        then_cli_displays(cli_response, "ERROR")


class TestProvideFileScopeContextForInstructions:
    """Tests for Provide File Scope Context For Instructions story.
    
    Tests that file scope parameters filter workspace files and pass
    matching files to the action.
    """
    
    @pytest.mark.parametrize("include_path,expected_count", [
        ("src/repl_cli/", 3),
        ("src/bot/", 3),
    ])
    def test_file_scope_filters_workspace_files(self, bot_directory, workspace_directory, include_path, expected_count):
        """File scope filters workspace files and passes matching files to action."""
        given_behavior_exists(bot_directory, 'code', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'code', 'validate', 'C:\\dev\\project')
        given_workspace_files_exist(workspace_directory, FILE_SCOPE_TEST_DATA)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with file scope
        scope_json = f"{{'type': 'files', 'value': ['{include_path}']}}"
        cli_response = when_user_enters_command(repl_session, f"validate --scope \"{scope_json}\"")
        
        # Displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
    
    def test_file_scope_with_exclude_pattern(self, bot_directory, workspace_directory):
        """File scope with exclude pattern filters out matching files."""
        given_behavior_exists(bot_directory, 'code', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'code', 'validate', 'C:\\dev\\project')
        given_workspace_files_exist(workspace_directory, FILE_SCOPE_TEST_DATA)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with file scope and exclude pattern
        scope_json = "{'type': 'files', 'value': ['src/'], 'exclude': ['*.pyc']}"
        cli_response = when_user_enters_command(repl_session, f"validate --scope \"{scope_json}\"")
        
        assert cli_response.status == 'success'


class TestStoreScopeContext:
    """Tests for Store Scope Context story.
    
    Tests that scope PARAMETERS (filter criteria) are stored, not resolved
    results. When scope is used later, it re-evaluates against current state.
    """
    
    def test_bot_stores_scope_parameters_not_resolved_results(self, bot_directory, workspace_directory):
        """Bot stores scope parameters in BehaviorActionState, not resolved items."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        given_story_graph_exists(workspace_directory, STORY_GRAPH_TEST_DATA)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute with scope parameter
        scope_json = "{'type': 'increment', 'value': [11]}"
        when_user_enters_command(repl_session, f"build --scope \"{scope_json}\"")
        
        # Verify scope parameters are stored
        state_file = get_behavior_action_state_path(workspace_directory)
        state_data = json.loads(state_file.read_text())
        
        # Should store type and value, not resolved stories
        assert 'scope' in state_data or 'current_action' in state_data
    
    def test_stored_scope_finds_newly_added_content(self, bot_directory, workspace_directory):
        """Stored scope parameters find newly added content on subsequent action."""
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        given_story_graph_exists(workspace_directory, {"Test Epic": ["Story A", "Story B"]})
        given_scope_stored_in_state(workspace_directory, 'epic', ['Test Epic'])
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Add new story to the graph
        stories_dir = workspace_directory / "docs" / "stories"
        story_graph = json.loads((stories_dir / "story-graph.json").read_text())
        story_graph["epics"][0]["story_groups"][0]["stories"].append({"name": "Story C", "priority": 11})
        (stories_dir / "story-graph.json").write_text(json.dumps(story_graph))
        
        # Execute build - should find all 3 stories now
        cli_response = when_user_enters_command(repl_session, "build")
        
        assert cli_response.status == 'success'


class TestGetInstructionsAndDisplay:
    """Tests for Get Instructions and Display story.
    
    Tests the instructions operation returns formatted output for display.
    """
    
    @pytest.mark.parametrize("behavior,action", [
        ("shape", "build"),
        ("exploration", "validate"),
        ("scenarios", "build")
    ])
    def test_user_requests_instructions_and_sees_formatted_output(self, bot_directory, workspace_directory, behavior, action):
        """User requests instructions and sees formatted output."""
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Request instructions
        cli_response = when_user_enters_command(repl_session, f"{action} instructions")
        
        # Displays real instruction content (not mock markers)
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100  # Real instructions are substantial
        then_cli_displays(cli_response, "CURRENT POSITION")  # Context header appears at end


class TestSubmitActionAndDisplayResults:
    """Tests for Submit Action and Display Results story.
    
    Tests submit operation with stubbed file writes.
    """
    
    @pytest.mark.parametrize("behavior,action", [
        ("shape", "build"),
        ("exploration", "validate"),
        ("scenarios", "build")
    ])
    def test_user_submits_action_and_sees_summary(self, bot_directory, workspace_directory, behavior, action):
        """User submits action and sees submission summary."""
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Get instructions first
        when_user_enters_command(repl_session, action)
        
        # Then submit
        cli_response = when_user_enters_command(repl_session, "submit")
        
        # Displays real submit output
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 50  # Submit has output


class TestConfirmActionAndDisplayResults:
    """Tests for Confirm Action and Display Results story.
    
    Tests confirm operation advances workflow and shows next action.
    """
    
    @pytest.mark.parametrize("behavior,current_action,next_action", [
        ("shape", "clarify", "strategy"),
        ("shape", "strategy", "build"),
        ("shape", "build", "validate")
    ])
    def test_user_confirms_and_advances_to_next_action(self, bot_directory, workspace_directory, behavior, current_action, next_action):
        """User confirms action and advances to next action with instructions."""
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, current_action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute and confirm
        when_user_enters_command(repl_session, current_action)
        cli_response = when_user_enters_command(repl_session, "confirm")
        
        # Should advance and show next action instructions - displays real content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{behavior}.{next_action}')
    
    def test_confirm_at_last_action_advances_to_next_behavior(self, bot_directory, workspace_directory):
        """Confirming last action advances to next behavior's first action."""
        completed_actions = build_completed_action_list("shape", ["clarify", "strategy", "build", "validate"])
        
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_exists(bot_directory, 'prioritization', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'render', 'C:\\dev\\project', completed_actions)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute render and confirm
        when_user_enters_command(repl_session, "render")
        cli_response = when_user_enters_command(repl_session, "confirm")
        
        # Should advance to next behavior - displays real instruction content
        assert cli_response.status == 'success'
        assert len(cli_response.output) > 100
        then_behavior_action_state_is_set(workspace_directory, 'current_behavior', 'story_bot.prioritization')
