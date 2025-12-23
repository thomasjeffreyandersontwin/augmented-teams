"""
Run Interactive REPL Tests

Tests for all stories in the 'Run Interactive REPL' sub-epic:
- Launch REPL Loop
- Detect TTY Input
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
- Prompt For Basic Parameters
- Prompt For Story Scope Parameters
- Prompt For File Scope Parameters
- Display Confirm and Continue Prompt
- Enter Confirm Results
- Advance To Next Action
- Loop Back To Display State
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
BEHAVIOR_ACTION_BREADCRUMBS_DATA = [
    ("shape", "build", "clarify [OK] -> strategy [OK] -> build* -> validate -> render"),
    ("discovery", "clarify", "clarify* -> strategy -> build -> validate -> render"),
    ("scenarios", "validate", "clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render")
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
    
    # Use common helper to create actions workflow (this also creates behavior.json)
    create_actions_workflow_json(bot_directory, behavior_name, actions=actions, order=1)
    
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
    from agile_bot.bots.base_bot.test.conftest import bootstrap_env
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
    """Verify behavior action state hasn't changed, using common test helper for path."""
    state_file = get_behavior_action_state_path(workspace_directory)
    current_state = json.loads(state_file.read_text())
    assert current_state == original_state


def build_completed_action_list(behavior, completed_actions):
    return [
        {'action_state': f'story_bot.{behavior}.{ca}', 'timestamp': '2025-12-23T08:00:00.000000'}
        for ca in completed_actions
    ]


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
        then_cli_displays(cli_output, f"CURRENT: story_bot.{behavior}.{action}")
        then_cli_displays(cli_output, f"Working Directory: {working_dir}")
        then_cli_displays(cli_output, f"[{behavior}] {action_breadcrumbs}")


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


class TestDisplayFreshStart:
    def test_cli_displays_fresh_start_with_no_state_file(self, bot_directory, workspace_directory):
        given_no_behavior_action_state(workspace_directory)
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_exists(bot_directory, 'prioritization', COMMON_ACTIONS)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        cli_output = when_cli_launches_in_repl_mode(repl_session)
        
        then_cli_displays(cli_output, "FRESH")
        # No longer shows "No workspace configured" - workspace shown in header
        then_cli_displays(cli_output, "Commands:")
        # Workspace is set via environment variable, not a command
        then_cli_displays(cli_output, "help")
        then_cli_displays(cli_output, "<behavior>")
        then_cli_displays(cli_output, "<action>")
        then_cli_displays(cli_output, "confirm")
        then_cli_displays(cli_output, "exit")
    
    @pytest.mark.parametrize("selected_behavior", COMMON_BEHAVIORS)
    def test_user_selects_initial_behavior(self, bot_directory, workspace_directory, selected_behavior):
        given_no_behavior_action_state(workspace_directory)
        given_behavior_exists(bot_directory, selected_behavior, COMMON_ACTIONS)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"behavior {selected_behavior}")
        
        then_cli_responds(cli_response, f"OK behavior={selected_behavior}")
        then_cli_displays(cli_response, f"CURRENT: story_bot.{selected_behavior}.clarify")
        then_cli_displays(cli_response, f"[{selected_behavior}] clarify* -> strategy -> build -> validate -> render")
        then_behavior_action_state_is_set(workspace_directory, 'current_behavior', f'story_bot.{selected_behavior}')
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{selected_behavior}.clarify')
    
    def test_user_configures_workspace_in_fresh_session(self, bot_directory, workspace_directory):
        given_no_behavior_action_state(workspace_directory)
        workspace_path = "C:\\dev\\project"
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"workspace {workspace_path}")
        
        then_cli_responds(cli_response, f"OK workspace={workspace_path}")
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
        
        then_cli_displays(cli_output, f"CURRENT: story_bot.{behavior}.{action}")
        then_cli_displays(cli_output, f"Working Directory: {working_dir}")
        then_cli_displays(cli_output, "## Behavior/Action Progress")
        then_cli_displays(cli_output, f"{behavior}")
        
        for ca in completed_actions:
            then_cli_displays(cli_output, f"{ca}")
            then_cli_displays(cli_output, "[OK]")


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
        
        then_cli_displays(cli_output, "[shape]")
        then_cli_displays(cli_output, "clarify [OK]")
        then_cli_displays(cli_output, "strategy [OK]")
        then_cli_displays(cli_output, "build*")


class TestShowAvailableBehaviorsAndActions:
    
    def test_show_available_behaviors_and_actions(self, bot_directory, workspace_directory):
        given_behavior_exists(bot_directory, 'shape', COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, 'shape', 'build', 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "behavior shape")
        
        then_cli_responds(cli_response, "OK behavior=shape")
        then_cli_displays(cli_response, "CURRENT: story_bot.shape.clarify")


class TestRequestHelp:
    
    @pytest.mark.parametrize("behavior,actions,action,parameters", [
        ("shape", ["clarify", "strategy", "build", "validate", "render"], "build", ["--scope <dict>"]),
        ("discovery", ["clarify", "strategy", "build", "validate", "render"], "validate", ["--scope <dict>", "--background <flag>"]),
        ("scenarios", ["clarify", "strategy", "build", "validate", "render"], "clarify", ["--key-questions-answered <dict>", "--evidence-provided <dict>"])
    ])
    def test_user_asks_for_help_for_current_behavior(self, bot_directory, workspace_directory, behavior, actions, action, parameters):
        given_behavior_exists(bot_directory, behavior, actions)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "help")
        
        # Help without args now shows all behaviors (not just current behavior's actions)
        then_cli_displays(cli_response, "Available Behaviors:")
        # Check that the current behavior is listed
        then_cli_displays(cli_response, behavior)
    
    @pytest.mark.parametrize("behavior,action,description,parameters,parameter_syntax", [
        ("shape", "build", "Build knowledge graph for build", ["--scope <dict>"], "--scope '{\"type\": \"epic\", \"value\": [\"Epic Name\"]}'"),
        ("discovery", "validate", "Validate knowledge graph against rules", ["--scope <dict>", "--background <flag>"], "--scope '{\"type\": \"all\"}' --background"),
        ("scenarios", "clarify", "Gather context by asking questions", ["--key-questions-answered <dict>"], "--key-questions-answered '{\"q1\": \"answer\"}'")
    ])
    def test_user_asks_for_detailed_help_for_specific_action(self, bot_directory, workspace_directory, behavior, action, description, parameters, parameter_syntax):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"help {action}")
        
        then_cli_displays(cli_response, f"## {action}")
        then_cli_displays(cli_response, "Full command:")
        then_cli_displays(cli_response, f"action {action}")
        then_cli_displays(cli_response, "Parameters:")
        then_cli_displays(cli_response, "Examples:")


class TestRequestStatus:
    
    @pytest.mark.parametrize("behavior,action,working_dir,completed_actions,breadcrumbs", [
        ("shape", "build", "C:\\dev\\my-project", ["clarify", "strategy"], "[shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render"),
        ("prioritization", "clarify", "C:\\dev\\my-project", [], "[prioritization] clarify* -> strategy -> build -> validate -> render"),
        ("discovery", "validate", "C:\\dev\\another-proj", ["clarify", "strategy", "build"], "[discovery] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render")
    ])
    def test_user_views_status_display(self, bot_directory, workspace_directory, behavior, action, working_dir, completed_actions, breadcrumbs):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, working_dir, completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, "status")
        
        then_cli_displays(cli_response, f"CURRENT: story_bot.{behavior}.{action}")
        then_cli_displays(cli_response, f"Working Directory: {working_dir}")
        then_cli_displays(cli_response, breadcrumbs)


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
        
        then_cli_responds(cli_response, f"OK behavior={target_behavior}")
        then_cli_displays(cli_response, f"CURRENT: story_bot.{target_behavior}.clarify")
        then_cli_displays(cli_response, f"[{target_behavior}] clarify* -> strategy -> build -> validate -> render")
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
        
        then_cli_responds(cli_response, f"OK action={target_action}")
        then_cli_displays(cli_response, f"CURRENT: story_bot.{current_behavior}.{target_action}")
        then_cli_displays(cli_response, f"{target_action}*")
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
        
        then_cli_responds(cli_response, f"ERROR: action '{invalid_action}' not found in behavior '{current_behavior}'")
        then_cli_displays(cli_response, "Available actions: clarify, strategy, build, validate, render")
        then_behavior_action_state_remains_unchanged(workspace_directory, original_state)


class TestNavigateWithinBehavior:
    
    @pytest.mark.parametrize("behavior,current_action,completed_actions,command,response_message,new_action,new_completed_actions,breadcrumbs", [
        ("shape", "build", ["clarify", "strategy"], "current", "CURRENT: story_bot.shape.build\nReady to run", "build", ["clarify", "strategy"], "[shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render"),
        ("shape", "build", ["clarify", "strategy"], "confirm", "OK advancing to validate", "validate", ["clarify", "strategy", "build"], "[shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render"),
        ("shape", "validate", ["clarify", "strategy", "build"], "back", "Moving back to previous action", "build", ["clarify", "strategy"], "[shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render"),
        ("shape", "clarify", [], "back", "ERROR: Already at first action", "clarify", [], "[shape] clarify* -> strategy -> build -> validate -> render"),
        ("shape", "render", ["clarify", "strategy", "build", "validate"], "confirm", "COMPLETE: shape behavior finished", "render", ["clarify", "strategy", "build", "validate", "render"], "[shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate [OK] -> render [OK]")
    ])
    def test_user_executes_workflow_navigation_commands(self, bot_directory, workspace_directory, behavior, current_action, completed_actions, command, response_message, new_action, new_completed_actions, breadcrumbs):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, current_action, 'C:\\dev\\project', completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, command)
        
        then_cli_responds(cli_response, response_message)
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{behavior}.{new_action}')
        then_cli_displays(cli_response, breadcrumbs)


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
        
        then_cli_displays(cli_response, f"EXECUTING {behavior}.{action}...")
        then_cli_displays(cli_response, "[mock response - not executing real action]")
        assert cli_response.status == 'success'
        assert cli_response.action == action


@pytest.mark.skip(reason="Parameter validation not yet implemented in stub")
class TestPromptForBasicParameters:
    
    @pytest.mark.parametrize("behavior,action,required_params,param_input,acknowledgment", [
        ("shape", "clarify", ["key_questions_answered", "evidence_provided"], 
         "clarify.key_questions.q1=\"What is scope?\" clarify.evidence.e1=\"Requirements\"", 
         "OK received 1 key question, 1 evidence"),
        ("shape", "strategy", ["decisions_made", "assumptions_made"], 
         "strategy.decisions.d1=\"Use REST API\" strategy.assumptions=\"Single user\"", 
         "OK received 1 decision, 1 assumption")
    ])
    def test_cli_prompts_for_missing_action_parameters(self, bot_directory, workspace_directory, behavior, action, required_params, param_input, acknowledgment):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Use action name to execute (defaults to instructions)
        result_run = when_user_enters_command(repl_session, action)
        
        then_cli_displays(result_run, f"MISSING PARAMETERS for {behavior}.{action}")
        for param in required_params:
            then_cli_displays(result_run, param)
        then_cli_displays(result_run, "Please provide parameters:")
        
        result_confirm = when_user_enters_command(repl_session, param_input)
        then_cli_responds(result_confirm, acknowledgment)


@pytest.mark.skip(reason="Scope parameter validation not yet implemented in stub")
class TestPromptForStoryScopeParameters:
    
    @pytest.mark.parametrize("behavior,action,invalid_scope,available_epics,available_increments,epics_list,increments_list", [
        ("shape", "build", "scope=\"wrong format\"", ["Manage Mobs", "Execute Mob Actions", "Configure Game"], [1, 2, 3], "Manage Mobs, Execute Mob Actions, Configure Game", "1, 2, 3"),
        ("shape", "validate", "scope.type=epic", ["Manage Mobs", "Execute Mob Actions", "Configure Game"], [1, 2, 3], "Manage Mobs, Execute Mob Actions, Configure Game", "1, 2, 3"),
        ("shape", "render", "scope.value=\"Manage Mobs\"", ["Manage Mobs", "Execute Mob Actions"], [1, 2], "Manage Mobs, Execute Mob Actions", "1, 2")
    ])
    def test_cli_handles_invalid_story_scope_and_provides_helpful_prompt(self, bot_directory, workspace_directory, behavior, action, invalid_scope, available_epics, available_increments, epics_list, increments_list):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"run {invalid_scope}")
        
        then_cli_displays(cli_response, "ERROR: Invalid scope syntax")
        then_cli_displays(cli_response, "Expected format:")
        then_cli_displays(cli_response, "scope.type=epic|story|increment|all scope.value=\"Name\"")
        then_cli_displays(cli_response, "Available in current story graph:")
        then_cli_displays(cli_response, f"Epics: {epics_list}")
        then_cli_displays(cli_response, f"Increments: {increments_list}")
        then_cli_displays(cli_response, "Examples:")
        then_cli_displays(cli_response, "scope.type=epic scope.value=\"Manage Mobs\"")


@pytest.mark.skip(reason="File scope parameter validation not yet implemented in stub")
class TestPromptForFileScopeParameters:
    
    @pytest.mark.parametrize("behavior,action,invalid_scope,workspace_folders,default_folder,available_epics,folder_list,epics_list", [
        ("code", "validate", "scope=wrongformat", ["src/", "tests/", "docs/", "agile_bot/"], "src/", ["Manage Mobs", "Execute Actions"], "src/, tests/, docs/, agile_bot/", "Manage Mobs, Execute Actions"),
        ("tests", "build", "scope.type=files", ["src/", "tests/", "docs/"], "tests/", ["Manage Mobs"], "src/, tests/, docs/", "Manage Mobs"),
        ("code", "render", "scope.value=src/", ["src/", "tests/", "agile_bot/"], "src/", ["Manage Mobs", "Configure Game"], "src/, tests/, agile_bot/", "Manage Mobs, Configure Game")
    ])
    def test_cli_handles_invalid_file_story_scope_in_dual_scope_behaviors(self, bot_directory, workspace_directory, behavior, action, invalid_scope, workspace_folders, default_folder, available_epics, folder_list, epics_list):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        cli_response = when_user_enters_command(repl_session, f"run {invalid_scope}")
        
        then_cli_displays(cli_response, "ERROR: Invalid scope syntax")
        then_cli_displays(cli_response, f"For '{behavior}' behavior, scope can be:")
        then_cli_displays(cli_response, "File scope: scope.type=files scope.value=<path> scope.exclude=<pattern>")
        then_cli_displays(cli_response, "Story scope: scope.type=epic|story|increment|all scope.value=\"Name\"")
        then_cli_displays(cli_response, "File scope options:")
        then_cli_displays(cli_response, f"Default for '{behavior}': {default_folder}")
        then_cli_displays(cli_response, f"Available folders: {folder_list}")
        then_cli_displays(cli_response, "Story scope options:")
        then_cli_displays(cli_response, f"Available epics: {epics_list}")


class TestDisplayConfirmAndContinuePrompt:
    
    @pytest.mark.parametrize("behavior,action,results_summary,results_display,next_action", [
        ("shape", "clarify", {"questions_answered": 7, "evidence_types": 3}, "- Answered 7 key questions\n- Provided 3 evidence types", "strategy"),
        ("shape", "strategy", {"decisions_made": 5, "assumptions": 2}, "- Made 5 decisions\n- Listed 2 assumptions", "build"),
        ("shape", "build", {"items_added": 12, "mode": "create"}, "- Added 12 items\n- Mode: create", "validate")
    ])
    def test_cli_displays_action_completion_and_prompts_for_continuation(self, bot_directory, workspace_directory, behavior, action, results_summary, results_display, next_action):
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, action, 'C:\\dev\\project')
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Execute action (instructions), then display_confirm_prompt gets current state
        when_user_enters_command(repl_session, action)
        confirm_prompt = repl_session.display_confirm_prompt()
        
        then_cli_displays(confirm_prompt, f"EXECUTED {behavior}.{action}")
        then_cli_displays(confirm_prompt, "Results:")
        # Stub shows mock results - not checking specific content
        then_cli_displays(confirm_prompt, f"Continue to next action ({next_action})? (y/n/review)")


class TestEnterConfirmResults:
    
    @pytest.mark.parametrize("behavior,current_action,next_action,completed_actions,new_completed_actions,breadcrumbs", [
        ("shape", "clarify", "strategy", [], ["clarify"], "[shape] clarify [OK] -> strategy* -> build -> validate -> render"),
        ("shape", "strategy", "build", ["clarify"], ["clarify", "strategy"], "[shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render"),
        ("shape", "build", "validate", ["clarify", "strategy"], ["clarify", "strategy", "build"], "[shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render")
    ])
    def test_user_confirms_action_completion_and_advances_workflow(self, bot_directory, workspace_directory, behavior, current_action, next_action, completed_actions, new_completed_actions, breadcrumbs):
        completed_action_list = build_completed_action_list(behavior, completed_actions)
        
        given_behavior_exists(bot_directory, behavior, COMMON_ACTIONS)
        given_behavior_action_state_exists(workspace_directory, behavior, current_action, 'C:\\dev\\project', completed_action_list)
        
        repl_session = when_user_runs_command_with_stdio_flag(bot_directory, workspace_directory)
        when_cli_launches_in_repl_mode(repl_session)
        
        # Use confirm to advance
        cli_response = when_user_enters_command(repl_session, "confirm")
        
        then_cli_displays(cli_response, f"OK advancing to {next_action}")
        then_behavior_action_state_is_set(workspace_directory, 'current_action', f'story_bot.{behavior}.{next_action}')
        then_cli_displays(cli_response, f"CURRENT: story_bot.{behavior}.{next_action}")
        then_cli_displays(cli_response, breadcrumbs)


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
        
        then_cli_displays(advance_response, "CURRENT: story_bot.shape.validate")


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
        
        then_cli_displays(state_display, "CURRENT: story_bot.shape.validate")
        then_cli_displays(state_display, "[shape]")
        then_cli_displays(state_display, "validate*")

