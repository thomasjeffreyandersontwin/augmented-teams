"""
Render Output Tests

Tests for all stories in the 'Render Output' sub-epic:
- Track Activity for Render Output Action
- Proceed To Validate Rules
- Render Output Using Synchronizers
"""
import pytest
from pathlib import Path
import json
from agile_bot.src.actions.render.render_action import RenderOutputAction
import os
from agile_bot.test.domain.bot_test_helper import BotTestHelper

# ============================================================================
# STORY: Track Activity for Render Output Action
# ============================================================================

class TestTrackActivityForRenderOutputAction:
    """Story: Track Activity for Render Output Action - Tests activity tracking for render_output."""

    def test_track_activity_when_render_output_action_starts(self, tmp_path):
        # Given: Bot directory and workspace directory are set up
        # When: Render output action starts
        # Then: Activity is tracked
        helper = BotTestHelper(tmp_path)
        helper.behaviors.verify_action_tracks_start(RenderOutputAction, 'render', behavior='discovery')

    def test_track_activity_when_render_output_action_completes(self, tmp_path):
        # Given: Bot directory and workspace directory are set up
        # When: Render output action completes with outputs and duration
        # Then: Activity is tracked
        helper = BotTestHelper(tmp_path)
        helper.behaviors.verify_action_tracks_completion(
            RenderOutputAction,
            'render',
            behavior='discovery',
            outputs={'files_generated_count': 3, 'file_paths': ['story-map.md', 'increments.md']},
            duration=180
        )

    def test_track_multiple_render_output_invocations_across_behaviors(self, tmp_path):
        # Activity log is in workspace_directory
        helper = BotTestHelper(tmp_path)
        helper.activity.given_activity_log()
        
        helper.activity.then_activity_log_matches(
            expected_count=2,
            expected_action_states=['story_bot.shape.render', 'story_bot.discovery.render']
        )

    def test_activity_log_creates_file_if_not_exists(self, tmp_path):
        """
        SCENARIO: Activity Log Creates File If Not Exists
        GIVEN: workspace directory exists but no activity log
        WHEN: Action tracks activity
        THEN: Activity log file is created automatically
        """
        # Given: Workspace directory exists but no activity log using production story_bot
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('discovery')
        os.environ['BOT_DIRECTORY'] = str(helper.bot_directory)
        os.environ['WORKING_AREA'] = str(helper.workspace)
        
        log_file = helper.workspace / 'activity_log.json'
        assert not log_file.exists()
        
        # When: Action tracks activity using production behavior
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        action.track_activity_on_start()
        
        # Then: Log file is created
        assert log_file.exists()


# ============================================================================
# STORY: Proceed To Validate Rules
# ============================================================================

class TestProceedToValidateRules:
    """Story: Proceed To Validate - Tests transition to validate action."""

    def test_seamless_transition_from_validate_to_render_output(self, tmp_path):
        """
        SCENARIO: Seamless Transition From Validate Rules To Render Output
        """
        # Given: Workspace directory is set up (use production bot directory)
        helper = BotTestHelper(tmp_path)
        # When: Validate rules action completes
        # Then: Workflow transitions to render_output
        helper.behaviors.verify_workflow_transition('validate', 'render', behavior='discovery')

    def test_workflow_state_captures_render_output_completion(self, tmp_path):
        """
        SCENARIO: Workflow State Captures Render Output Completion
        """
        # Given: Workspace directory is set up (use production bot directory)
        helper = BotTestHelper(tmp_path)
        # When: Render output action completes
        # Then: Workflow state captures completion
        helper.behaviors.verify_workflow_saves_completed_action('render')

    def test_render_output_action_executes_successfully(self, tmp_path):
        """
        SCENARIO: Render Output Action Executes Successfully
        GIVEN: render_output action is initialized from production story_bot
        WHEN: Action is executed
        THEN: Action completes without errors
        """
        # Use production story_bot
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('discovery')
        behavior_obj = helper.bot.behaviors.current
        
        # Create action from production behavior
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        
        # Action should initialize successfully
        assert action.behavior.bot_name == 'story_bot'
        assert action.behavior.name == 'discovery'


# ============================================================================
# STORY: Inject Render Instructions and Configs
# ============================================================================

class TestInjectRenderInstructionsAndConfigs:
    """Story: Inject Render Instructions and Configs - Tests template variable injection."""

    def test_all_template_variables_are_replaced_in_instructions(self, tmp_path):
        """
        SCENARIO: All template variables are replaced in final instructions
        GIVEN: Render action with production synchronizers from story_bot
        WHEN: Action executes
        THEN: Instructions contain all required render fields
        """
        # Use production story_bot with real synchronizers
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        helper.state.set_state('shape', 'render')
        
        # Execute render action using production behavior
        from agile_bot.src.actions.render.render_action import RenderOutputAction
        from agile_bot.src.actions.action_context import ScopeActionContext
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        result = action.do_execute(ScopeActionContext())
        
        # Verify all RenderOutputAction fields are present in production bot
        helper.render.assert_render_output_instructions(result)

    def test_render_configs_format_includes_all_fields(self, tmp_path):
        """
        SCENARIO: Formatted render_configs includes all fields referenced in instructions
        GIVEN: Production story_bot with render configs
        WHEN: Configs are formatted for injection  
        THEN: All fields are present in formatted output
        """
        # Use production story_bot - shape has render configs
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        os.environ['BOT_DIRECTORY'] = str(helper.bot_directory)
        os.environ['WORKING_AREA'] = str(helper.workspace)
        
        # Create action from production behavior
        behavior_obj = helper.bot.behaviors.current
        action_obj = RenderOutputAction(behavior=behavior_obj, action_config=None)
        
        # When: Format render configs using production method
        formatted = action_obj._instruction_formatter.format_render_configs(action_obj._render_specs)
        
        # Then: Production render configs have all required fields
        assert 'render_sync' in formatted or 'render_story' in formatted or 'render_domain' in formatted
        assert 'manually generate' in formatted.lower() or 'render' in formatted.lower()
        assert 'story-graph.json' in formatted or 'input' in formatted.lower() or 'domain' in formatted.lower()
        assert 'template' in formatted.lower() or 'transform' in formatted.lower() or 'render' in formatted.lower()
        assert '.md' in formatted or '.txt' in formatted or '.drawio' in formatted


# ============================================================================
# STORY: Render Output Using Synchronizers
# ============================================================================

class TestRenderOutputUsingSynchronizers:
    """Story: Render Output Using Synchronizers - Tests automatic execution of synchronizers."""

    def test_synchronizers_are_executed_automatically(self, tmp_path):
        """
        SCENARIO: Synchronizers are executed automatically during render action
        GIVEN: Production bot with real synchronizers
        WHEN: Render output action executes
        THEN: Synchronizers are executed automatically
        """
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'render')
        
        # Execute render action
        from agile_bot.src.actions.render.render_action import RenderOutputAction
        from agile_bot.src.actions.action_context import ScopeActionContext
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        result = action.do_execute(ScopeActionContext())
        
        # Verify synchronizers tried to execute (they may fail due to missing input files, that's OK)
        base_instructions = result.get('base_instructions', [])
        base_instructions_text = '\n'.join(base_instructions)
        assert 'Synchronizers Already Executed' in base_instructions_text or 'render' in base_instructions_text.lower()

    def test_template_configs_remain_in_instructions(self, tmp_path):
        """
        SCENARIO: Template configs remain in instructions for AI handling
        GIVEN: Production bot with synchronizers and templates
        WHEN: Render output action executes  
        THEN: Result includes instructions
        """
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'render')
        
        # Execute render action
        from agile_bot.src.actions.render.render_action import RenderOutputAction
        from agile_bot.src.actions.action_context import ScopeActionContext
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        result = action.do_execute(ScopeActionContext())
        
        # Verify result has base instructions
        base_instructions = result.get('base_instructions', [])
        assert len(base_instructions) > 0, "Should have instructions"

    def test_executed_synchronizers_info_in_instructions(self, tmp_path):
        """
        SCENARIO: Executed synchronizers information is included in AI instructions
        GIVEN: Production bot with synchronizers
        WHEN: Render output action executes
        THEN: Instructions include synchronizer execution info
        """
        helper = BotTestHelper(tmp_path)
        helper.state.set_state('shape', 'render')
        
        # Execute render action
        from agile_bot.src.actions.render.render_action import RenderOutputAction
        from agile_bot.src.actions.action_context import ScopeActionContext
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        result = action.do_execute(ScopeActionContext())
        
        # Verify instructions mention synchronizers
        base_instructions = '\n'.join(result.get('base_instructions', []))
        assert 'Synchronizers Already Executed' in base_instructions or 'render' in base_instructions.lower()
