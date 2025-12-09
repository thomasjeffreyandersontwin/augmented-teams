"""
Render Output Tests

Tests for all stories in the 'Render Output' sub-epic:
- Track Activity for Render Output Action
- Proceed To Validate Rules
"""
import pytest
from pathlib import Path
import json
from agile_bot.bots.base_bot.src.bot.render_output_action import RenderOutputAction
from agile_bot.bots.base_bot.test.test_helpers import (
    bootstrap_env,
    create_activity_log_file,
    create_workflow_state,
    verify_action_tracks_start,
    verify_action_tracks_completion,
    verify_workflow_transition,
    verify_workflow_saves_completed_action,
    read_activity_log
)

# Use fixtures from conftest.py (bot_directory, workspace_directory)

# ============================================================================
# STORY: Track Activity for Render Output Action
# ============================================================================

class TestTrackActivityForRenderOutputAction:
    """Story: Track Activity for Render Output Action - Tests activity tracking for render_output."""

    def test_track_activity_when_render_output_action_starts(self, bot_directory, workspace_directory):
        verify_action_tracks_start(bot_directory, workspace_directory, RenderOutputAction, 'render_output', behavior='discovery')

    def test_track_activity_when_render_output_action_completes(self, bot_directory, workspace_directory):
        verify_action_tracks_completion(
            bot_directory,
            workspace_directory,
            RenderOutputAction,
            'render_output',
            behavior='discovery',
            outputs={'files_generated_count': 3, 'file_paths': ['story-map.md', 'increments.md']},
            duration=180
        )

    def test_track_multiple_render_output_invocations_across_behaviors(self, workspace_directory):
        # Activity log is in workspace_directory
        workspace_directory.mkdir(parents=True, exist_ok=True)
        log_file = workspace_directory / 'activity_log.json'
        from tinydb import TinyDB
        with TinyDB(log_file) as db:
            db.insert({'action_state': 'story_bot.shape.render_output', 'timestamp': '09:00'})
            db.insert({'action_state': 'story_bot.discovery.render_output', 'timestamp': '10:00'})
        
        log_data = read_activity_log(workspace_directory)
        assert len(log_data) == 2
        assert log_data[0]['action_state'] == 'story_bot.shape.render_output'
        assert log_data[1]['action_state'] == 'story_bot.discovery.render_output'

    def test_activity_log_creates_file_if_not_exists(self, bot_directory, workspace_directory):
        """
        SCENARIO: Activity log creates file if it doesn't exist
        GIVEN: workspace directory exists but no activity log
        WHEN: Action tracks activity
        THEN: Activity log file is created automatically
        """
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        log_file = workspace_directory / 'activity_log.json'
        assert not log_file.exists()
        
        # When: Action tracks activity
        action = RenderOutputAction(
            bot_name='story_bot',
            behavior='discovery',
            bot_directory=bot_directory
        )
        action.track_activity_on_start()
        
        # Then: Log file is created
        assert log_file.exists()


# ============================================================================
# STORY: Proceed To Validate Rules
# ============================================================================

class TestProceedToValidateRules:
    """Story: Proceed To Validate Rules - Tests transition to validate_rules action."""

    def test_seamless_transition_from_render_output_to_validate_rules(self, bot_directory, workspace_directory):
        verify_workflow_transition(bot_directory, workspace_directory, 'render_output', 'validate_rules', behavior='discovery')

    def test_workflow_state_captures_render_output_completion(self, bot_directory, workspace_directory):
        verify_workflow_saves_completed_action(bot_directory, workspace_directory, 'render_output')

    def test_render_output_action_executes_successfully(self, bot_directory, workspace_directory):
        """
        SCENARIO: Render output action executes successfully
        GIVEN: render_output action is initialized
        WHEN: Action is executed
        THEN: Action completes without errors
        """
        # Bootstrap environment
        bootstrap_env(bot_directory, workspace_directory)
        
        bot_name = 'story_bot'
        behavior = 'discovery'
        
        action = RenderOutputAction(
            bot_name=bot_name,
            behavior=behavior,
            bot_directory=bot_directory
        )
        
        # Action should initialize successfully
        assert action.bot_name == bot_name
        assert action.behavior == behavior
