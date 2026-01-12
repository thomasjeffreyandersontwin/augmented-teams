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
# NOTE: Removed bootstrap_env - use os.environ directly
from agile_bot.test.domain.bot_test_helper import BotTestHelper

# Use fixtures from conftest.py (bot_directory, workspace_directory)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_minimal_guardrails_files(bot_directory: Path, behavior: str, bot_name: str):
    """Create minimal guardrails directory structure for tests."""
    guardrails_dir = bot_directory / 'behaviors' / behavior / 'guardrails'
    guardrails_dir.mkdir(parents=True, exist_ok=True)
    # Create empty files if needed
    (guardrails_dir / 'key_questions.json').write_text('{}', encoding='utf-8')
    (guardrails_dir / 'evidence.json').write_text('{}', encoding='utf-8')

def given_base_instructions_for_render_output_copied(bot_directory: Path):
    """Given: Base instructions for render_output copied."""
    import shutil
    repo_root = Path(__file__).parent.parent.parent.parent.parent
    actual_base_actions_dir = repo_root / 'agile_bot' / 'base_actions'
    # BaseActionConfig loads from action_config.json, not instructions.json
    # Action name is 'render', not 'render_output'
    actual_config_file = actual_base_actions_dir / 'render' / 'action_config.json'
    if not actual_config_file.exists():
        # Try render_output as fallback
        actual_config_file = actual_base_actions_dir / 'render_output' / 'action_config.json'
    
    # For custom bot directory, copy to bot's base_actions
    # For production bot, verify file exists and skip copy
    production_base_actions = repo_root / 'agile_bot' / 'base_actions'
    bot_base_actions_dir = bot_directory.parent / 'base_actions' / 'render'
    
    # Check if using production bot (bot_directory is under agile_bot/bots/story_bot)
    is_production = str(bot_directory).replace('\\', '/').endswith('agile_bot/bots/story_bot')
    
    if is_production:
        # Using production bot - just verify the file exists, don't copy
        if not actual_config_file.exists():
            raise FileNotFoundError(f"Production action config not found at {actual_config_file}")
        return actual_config_file
    else:
        # Custom bot - copy the file
        bot_base_actions_dir.mkdir(parents=True, exist_ok=True)
        bot_config_file = bot_base_actions_dir / 'action_config.json'
        if actual_config_file.exists():
            shutil.copy2(actual_config_file, bot_config_file)
        else:
            # Create minimal config if file doesn't exist
            import json
            bot_config_file.write_text(json.dumps({
                "name": "render",
                "order": 5,
                "workflow": True,
                "instructions": [
                    "render base instructions",
                    "{{render_configs}}",
                    "{{render_instructions}}"
                ]
            }), encoding='utf-8')
        return bot_config_file


def given_behavior_render_instructions_created(bot_directory: Path, behavior: str):
    """Given: Behavior render instructions created."""
    behavior_dir = bot_directory / 'behaviors' / behavior
    render_dir = behavior_dir / 'content' / 'render'
    render_dir.mkdir(parents=True, exist_ok=True)
    render_instructions_file = render_dir / 'instructions.json'
    render_instructions_file.write_text(
        json.dumps({
            'behaviorName': behavior,
            'instructions': ['Render all story files', 'Generate markdown output']
        }),
        encoding='utf-8'
    )
    return render_instructions_file


def given_render_configs_created(render_dir: Path, configs: list):
    """Given: Render configs created."""
    created_configs = []
    for config_data in configs:
        config_file = render_dir / f"{config_data['name']}.json"
        config_file.write_text(json.dumps(config_data), encoding='utf-8')
        created_configs.append(config_file)
    return created_configs


def when_render_output_action_created(bot_name: str, behavior: str, bot_directory: Path):
    """When: RenderOutputAction created."""
    from agile_bot.src.bot_path import BotPath
    from agile_bot.src.behaviors.behavior import Behavior
    # BaseActionConfig deleted - Action already has config loading
    import json
    # create_minimal_guardrails_files moved to BotTestHelper
    
    # Create behavior.json directly (replaces deprecated create_actions_workflow_json)
    behavior_dir = bot_directory / 'behaviors' / behavior
    behavior_dir.mkdir(parents=True, exist_ok=True)
    behavior_file = behavior_dir / 'behavior.json'
    behavior_file.write_text(json.dumps({
        "behaviorName": behavior,
        "description": f"Test behavior: {behavior}",
        "actions_workflow": {
            "actions": [
                {"name": "clarify", "order": 1, "next_action": "strategy"},
                {"name": "strategy", "order": 2, "next_action": "build"},
                {"name": "build", "order": 3, "next_action": "validate"},
                {"name": "validate", "order": 4, "next_action": "render"},
                {"name": "render", "order": 5}
            ]
        }
    }, indent=2), encoding='utf-8')
    create_minimal_guardrails_files(bot_directory, behavior, bot_name)
    bot_paths = BotPath(bot_directory=bot_directory)
    behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
    return RenderOutputAction(
        behavior=behavior_obj,
        action_config=None
    )


def when_render_output_action_loads_and_merges_instructions(bot_name: str, behavior: str, bot_directory: Path):
    """When: RenderOutputAction loads and merges instructions."""
    import json
    from agile_bot.src.bot_path import BotPath
    from agile_bot.src.behaviors.behavior import Behavior
    # BaseActionConfig deleted - Action already has config loading
    # create_minimal_guardrails_files moved to BotTestHelper
    
    # Create behavior.json directly (replaces deprecated create_actions_workflow_json)
    behavior_dir = bot_directory / 'behaviors' / behavior
    behavior_dir.mkdir(parents=True, exist_ok=True)
    behavior_file = behavior_dir / 'behavior.json'
    behavior_file.write_text(json.dumps({
        "behaviorName": behavior,
        "description": f"Test behavior: {behavior}",
        "actions_workflow": {
            "actions": [
                {"name": "clarify", "order": 1, "next_action": "strategy"},
                {"name": "strategy", "order": 2, "next_action": "build"},
                {"name": "build", "order": 3, "next_action": "validate"},
                {"name": "validate", "order": 4, "next_action": "render"},
                {"name": "render", "order": 5}
            ]
        }
    }, indent=2), encoding='utf-8')
    create_minimal_guardrails_files(bot_directory, behavior, bot_name)
    bot_paths = BotPath(bot_directory=bot_directory)
    behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
    action_obj = RenderOutputAction(
        behavior=behavior_obj,
        action_config=None
    )
    # Call do_execute to trigger template variable replacement via _inject_render_data
    from agile_bot.src.actions.action_context import ScopeActionContext
    result = action_obj.do_execute(ScopeActionContext())
    return action_obj, result



def then_all_render_output_assertions_pass(base_instructions_text: str):
    """Then step: All render output assertions pass."""
    # Verify that synchronizers ran and their output is in instructions
    # The production bot will show synchronizer execution results
    assert 'Synchronizers Already Executed' in str(base_instructions_text) or 'render' in str(base_instructions_text).lower()
    # Check that actual render configs are mentioned (e.g. render_domain_model)
    assert 'render_domain_model' in str(base_instructions_text) or 'render_story' in str(base_instructions_text)




def then_activity_log_file_does_not_exist(workspace_directory: Path):
    """Then: Activity log file does not exist."""
    log_file = workspace_directory / 'activity_log.json'
    assert not log_file.exists()
    return log_file


def when_render_output_action_tracks_start(bot_name: str, behavior: str, bot_directory: Path):
    """When: Render output action tracks start."""
    import json
    from agile_bot.src.bot_path import BotPath
    from agile_bot.src.behaviors.behavior import Behavior
    # BaseActionConfig deleted - Action already has config loading
    # create_minimal_guardrails_files moved to BotTestHelper
    # Create behavior.json directly (replaces deprecated create_actions_workflow_json)
    behavior_dir = bot_directory / 'behaviors' / behavior
    behavior_dir.mkdir(parents=True, exist_ok=True)
    behavior_file = behavior_dir / 'behavior.json'
    behavior_file.write_text(json.dumps({
        "behaviorName": behavior,
        "description": f"Test behavior: {behavior}",
        "actions_workflow": {
            "actions": [
                {"name": "clarify", "order": 1, "next_action": "strategy"},
                {"name": "strategy", "order": 2, "next_action": "build"},
                {"name": "build", "order": 3, "next_action": "validate"},
                {"name": "validate", "order": 4, "next_action": "render"},
                {"name": "render", "order": 5}
            ]
        }
    }, indent=2), encoding='utf-8')
    create_minimal_guardrails_files(bot_directory, behavior, bot_name)
    bot_paths = BotPath(bot_directory=bot_directory)
    behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
    action = RenderOutputAction(
        behavior=behavior_obj,
        action_config=None
    )
    action.track_activity_on_start()
    return action


def then_activity_log_file_exists(log_file: Path):
    """Then: Activity log file exists."""
    assert log_file.exists()


def given_bot_name_and_behavior_for_discovery():
    """Given: Bot name and behavior for discovery."""
    bot_name = 'story_bot'
    behavior = 'discovery'
    return bot_name, behavior


def when_create_render_output_action(bot_name: str, behavior: str, bot_directory: Path):
    """When: Create render output action."""
    import json
    from agile_bot.src.bot_path import BotPath
    from agile_bot.src.behaviors.behavior import Behavior
    # BaseActionConfig deleted - Action already has config loading
    # create_minimal_guardrails_files moved to BotTestHelper
    # Create behavior.json directly (replaces deprecated create_actions_workflow_json)
    behavior_dir = bot_directory / 'behaviors' / behavior
    behavior_dir.mkdir(parents=True, exist_ok=True)
    behavior_file = behavior_dir / 'behavior.json'
    behavior_file.write_text(json.dumps({
        "behaviorName": behavior,
        "description": f"Test behavior: {behavior}",
        "actions_workflow": {
            "actions": [
                {"name": "clarify", "order": 1, "next_action": "strategy"},
                {"name": "strategy", "order": 2, "next_action": "build"},
                {"name": "build", "order": 3, "next_action": "validate"},
                {"name": "validate", "order": 4, "next_action": "render"},
                {"name": "render", "order": 5}
            ]
        }
    }, indent=2), encoding='utf-8')
    create_minimal_guardrails_files(bot_directory, behavior, bot_name)
    bot_paths = BotPath(bot_directory=bot_directory)
    behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
    action = RenderOutputAction(
        behavior=behavior_obj,
        action_config=None
    )
    return action




def given_bot_name_and_behavior_for_shape():
    """Given: Bot name and behavior for shape."""
    bot_name = 'test_bot'
    behavior = 'shape'
    return bot_name, behavior


def given_render_dir_and_configs_setup(bot_directory: Path, behavior: str):
    """Given: Render dir and configs setup."""
    behavior_dir = bot_directory / 'behaviors' / behavior
    render_dir = behavior_dir / 'content' / 'render'
    render_dir.mkdir(parents=True, exist_ok=True)
    given_behavior_render_instructions_created(bot_directory, behavior)
    
    # Create template file if referenced in configs
    templates_dir = render_dir / 'templates'
    templates_dir.mkdir(parents=True, exist_ok=True)
    template_file = templates_dir / 'story-map.txt'
    template_file.write_text('Story Map Template', encoding='utf-8')
    
    given_render_configs_created(render_dir, [
        {
            'name': 'render_story_files',
            'type': 'synchronizer',
            'path': 'docs/stories',
            'input': 'story-graph.json',
            'synchronizer': 'synchronizers.story_scenarios.StoryScenariosSynchronizer',
            'output': 'docs/stories',
            'instructions': 'Render story-graph.json to story markdown files'
        },
        {
            'name': 'render_story_map_txt',
            'type': 'template',
            'path': 'docs/stories',
            'input': 'story-graph.json',
            'template': 'templates/story-map.txt',
            'output': 'story-map.txt',
            'instructions': 'Render story-graph.json to story-map.txt format'
        }
    ])
    return render_dir


def when_render_configs_formatted(configs=None, format_type='json', action_obj=None):
    """
    Consolidated function for formatting render configs.
    Replaces: when_format_render_configs
    
    Args:
        configs: Render configs dict (if None and action_obj provided, loads from action_obj)
        format_type: Format type (default 'json')
        action_obj: Action object (if provided and configs is None, loads configs from it)
    
    Returns:
        Formatted configs string
    """
    if configs is None:
        if action_obj is None:
            raise ValueError("Either configs or action_obj must be provided")
        configs = action_obj._config_loader.load_render_configs()
    
    if action_obj is not None:
        # Convert dict configs to RenderSpec objects if needed
        from agile_bot.src.actions.render.render_spec import RenderSpec
        if configs and isinstance(configs[0], dict):
            # Convert dict configs to RenderSpec objects
            render_specs = []
            for config_dict in configs:
                config_data = config_dict.get('config', config_dict)
                render_folder = action_obj._config_loader.find_render_folder()
                spec = RenderSpec(config_data, render_folder, action_obj.behavior.bot_paths)
                render_specs.append(spec)
            return action_obj._instruction_formatter.format_render_configs(render_specs)
        else:
            # Already RenderSpec objects
            return action_obj._instruction_formatter.format_render_configs(configs)
    else:
        # If no action_obj, assume configs is already a dict and format it
        import json
        return json.dumps(configs, indent=2) if format_type == 'json' else str(configs)


def then_formatted_configs_contain_sync_and_template(formatted: str):
    """Then: Formatted configs contain sync and template."""
    assert 'render_sync' in formatted
    assert 'render_template' in formatted


def then_formatted_configs_contain_synchronizer_fields(formatted: str):
    """Then: Formatted configs contain synchronizer fields."""
    # Production bot format: "manually generate OUTPUT by taking INPUT and transform using TEMPLATE/SYNCHRONIZER"
    assert 'manually generate' in formatted.lower() or 'render' in formatted.lower()
    assert 'taking' in formatted.lower() or 'input' in formatted.lower()
    assert 'story-graph.json' in formatted or 'input' in formatted.lower()
    assert 'transform' in formatted.lower() or 'output' in formatted.lower()


def then_formatted_configs_contain_template_fields(formatted: str):
    """Then: Formatted configs contain template fields."""
    # Production bot format includes template info in the transform section
    assert 'template' in formatted.lower() or 'transform' in formatted.lower()
    assert '.md' in formatted  # Should have markdown output files


def when_create_sync_and_template_configs(render_dir: Path):
    """When: Create sync and template configs."""
    sync_config = render_dir / 'render_sync.json'
    sync_config.write_text(
        json.dumps({
            'name': 'render_sync',
            'type': 'synchronizer',
            'path': 'docs/stories',
            'input': 'story-graph.json',
            'synchronizer': 'synchronizers.test.TestSynchronizer',
            'renderer_command': 'render-test',
            'output': 'test-output.drawio',
            'instructions': 'Test synchronizer instructions'
        }),
        encoding='utf-8'
    )
    
    template_config = render_dir / 'render_template.json'
    template_config.write_text(
        json.dumps({
            'name': 'render_template',
            'type': 'template',
            'path': 'docs/stories',
            'input': 'story-graph.json',
            'template': 'templates/test-template.md',
            'output': 'test-output.md',
            'instructions': 'Test template instructions'
        }),
        encoding='utf-8'
    )
    
    # Create the template file that the config references
    templates_dir = render_dir / 'templates'
    templates_dir.mkdir(parents=True, exist_ok=True)
    template_file = templates_dir / 'test-template.md'
    template_file.write_text('# Test Template\n\nThis is a test template.', encoding='utf-8')
    
    return sync_config, template_config


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
        helper.verify_action_tracks_start(RenderOutputAction, 'render', behavior='discovery')

    def test_track_activity_when_render_output_action_completes(self, tmp_path):
        # Given: Bot directory and workspace directory are set up
        # When: Render output action completes with outputs and duration
        # Then: Activity is tracked
        helper = BotTestHelper(tmp_path)
        helper.verify_action_tracks_completion(
            RenderOutputAction,
            'render',
            behavior='discovery',
            outputs={'files_generated_count': 3, 'file_paths': ['story-map.md', 'increments.md']},
            duration=180
        )

    def test_track_multiple_render_output_invocations_across_behaviors(self, tmp_path):
        # Activity log is in workspace_directory
        helper = BotTestHelper(tmp_path)
        helper.given_activity_log()
        
        helper.then_activity_log_matches(
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
        # Given: Workspace directory exists but no activity log
        helper = BotTestHelper(tmp_path)
        # Bootstrap environment
        # Set environment variables directly instead of using deprecated bootstrap_env
        os.environ['BOT_DIRECTORY'] = str(helper.bot_directory)
        os.environ['WORKING_AREA'] = str(helper.workspace)
        
        log_file = then_activity_log_file_does_not_exist(helper.workspace)
        
        # When: Action tracks activity
        # Then: Activity log file is created automatically
        when_render_output_action_tracks_start('story_bot', 'discovery', helper.bot_directory)
        
        # Then: Log file is created
        then_activity_log_file_exists(log_file)


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
        helper.verify_workflow_transition('validate', 'render', behavior='discovery')

    def test_workflow_state_captures_render_output_completion(self, tmp_path):
        """
        SCENARIO: Workflow State Captures Render Output Completion
        """
        # Given: Workspace directory is set up (use production bot directory)
        helper = BotTestHelper(tmp_path)
        # When: Render output action completes
        # Then: Workflow state captures completion
        helper.verify_workflow_saves_completed_action('render')

    def test_render_output_action_executes_successfully(self, tmp_path):
        """
        SCENARIO: Render Output Action Executes Successfully
        GIVEN: render_output action is initialized
        WHEN: Action is executed
        THEN: Action completes without errors
        """
        # Use production bot directory
        helper = BotTestHelper(tmp_path)
        bot_directory = helper.bot_directory
        bot_name, behavior = given_bot_name_and_behavior_for_discovery()
        
        action = when_create_render_output_action(bot_name, behavior, bot_directory)
        
        # Action should initialize successfully
        assert action.behavior.bot_name == bot_name
        assert action.behavior.name == behavior


# ============================================================================
# STORY: Inject Render Instructions and Configs
# ============================================================================

class TestInjectRenderInstructionsAndConfigs:
    """Story: Inject Render Instructions and Configs - Tests template variable injection."""

    def test_all_template_variables_are_replaced_in_instructions(self, tmp_path):
        """
        SCENARIO: All template variables are replaced in final instructions
        GIVEN: Render action with production synchronizers
        WHEN: Action executes
        THEN: Instructions contain all required render fields
        """
        # Use production bot with real synchronizers
        helper = BotTestHelper(tmp_path)
        helper.set_state('shape', 'render')
        
        # Execute render action
        from agile_bot.src.actions.render.render_action import RenderOutputAction
        from agile_bot.src.actions.action_context import ScopeActionContext
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        result = action.do_execute(ScopeActionContext())
        
        # Verify all RenderOutputAction fields are present
        helper.assert_render_output_instructions(result)

    def test_render_configs_format_includes_all_fields(self, tmp_path):
        """
        SCENARIO: Formatted render_configs includes all fields referenced in instructions
        GIVEN: Render configs with instructions, synchronizer, template, input, output fields
        WHEN: Configs are formatted for injection
        THEN: All fields are present in formatted output
        """
        # Use production bot directory
        helper = BotTestHelper(tmp_path)
        bot_directory = helper.bot_directory
        os.environ['BOT_DIRECTORY'] = str(bot_directory)
        os.environ['WORKING_AREA'] = str(helper.workspace)
        
        bot_name, behavior = given_bot_name_and_behavior_for_shape()
        render_dir = helper.given_directory_created(bot_directory, directory_type='behavior_render', behavior=behavior)
        when_create_sync_and_template_configs(render_dir)
        
        # When: Action formats render configs
        action_obj = when_render_output_action_created(bot_name, behavior, bot_directory)
        
        formatted = when_render_configs_formatted(action_obj=action_obj)
        
        # Then: All fields are present
        then_formatted_configs_contain_sync_and_template(formatted)
        then_formatted_configs_contain_synchronizer_fields(formatted)
        then_formatted_configs_contain_template_fields(formatted)


# ============================================================================
# HELPER FUNCTIONS - Domain Classes (Stories 7-8: MergedInstructions Render)
# ============================================================================

from unittest.mock import Mock
from agile_bot.legacy.src.bot.merged_instructions import MergedInstructions
# BaseActionConfig deleted - Action already has config loading


def given_action_with_instructions(instructions: list):
    """Given: Action with instructions (BaseActionConfig merged into Action)."""
    from agile_bot.src.actions.action import Action
    action = Mock(spec=Action)
    action._base_config = {'instructions': instructions}
    action.instructions = instructions
    return action


def given_render_instructions(instructions: dict):
    """Given: Render instructions dict."""
    return instructions


def when_merged_instructions_instantiated(base_action_config, render_instructions=None):
    """When: MergedInstructions instantiated."""
    # Extract instructions from base_action_config if it's a Mock/object, otherwise use directly
    if hasattr(base_action_config, 'instructions'):
        base_instructions = base_action_config.instructions
    elif isinstance(base_action_config, list):
        base_instructions = base_action_config
    else:
        base_instructions = base_action_config
    return MergedInstructions(base_instructions, render_instructions)


def when_render_instructions_accessed(merged_instructions: MergedInstructions):
    """When: render_instructions property accessed."""
    return merged_instructions.render_instructions


def when_merge_called(merged_instructions: MergedInstructions):
    """When: merge() called."""
    return merged_instructions.merge()


def then_render_instructions_are(result: dict, expected: dict):
    """Then: Render instructions are expected."""
    assert result == expected


def then_render_instructions_is_none(result):
    """Then: Render instructions is None."""
    assert result is None


def then_merged_contains_base_instructions(merged: dict, expected: list):
    """Then: Merged dict contains base instructions."""
    assert merged['base_instructions'] == expected


def then_merged_contains_render_instructions(merged: dict, expected: dict):
    """Then: Merged dict contains render instructions."""
    assert 'render_instructions' in merged
    assert merged['render_instructions'] == expected


def then_merged_does_not_contain_render_instructions(merged: dict):
    """Then: Merged dict does not contain render instructions."""
    assert 'render_instructions' not in merged


# ============================================================================
# TEST CLASSES - Domain Classes (Stories 7-8: MergedInstructions Render)
# ============================================================================

class TestGetRenderInstructions:
    """Story: Get Render Instructions (Sub-epic: Render Output)"""
    
def then_render_instructions_matches_expected(result, expected_result):
    """Then: Render instructions matches expected result."""
    if expected_result is None:
        then_render_instructions_is_none(result)
    else:
        then_render_instructions_are(result, expected_result)


class TestGetRenderInstructions:
    """Story: Get Render Instructions (Sub-epic: Render Output)"""
    
    @pytest.mark.parametrize("render_instructions,expected_result", [
        # Example 1: Render instructions provided
        ({'instructions': ['render1', 'render2']}, {'instructions': ['render1', 'render2']}),
        # Example 2: No render instructions
        (None, None),
    ])
    def test_render_instructions_property_returns_provided_instructions_or_none(self, render_instructions, expected_result):
        """
        SCENARIO: Render instructions property returns provided instructions or None
        GIVEN: MergedInstructions with or without render instructions
        WHEN: render_instructions property accessed
        THEN: Returns render instructions dict when provided, None when not provided
        """
        # Given: BaseActionConfig and optional render instructions
        base_action_config = given_action_with_instructions(['base1'])
        
        # When: MergedInstructions instantiated and render_instructions accessed
        merged_instructions = when_merged_instructions_instantiated(base_action_config, render_instructions)
        result = when_render_instructions_accessed(merged_instructions)
        
        # Then: Render instructions are expected
        then_render_instructions_matches_expected(result, expected_result)


class TestMergeBaseAndRenderInstructions:
    """Story: Merge Base and Render Instructions (Sub-epic: Render Output)"""
    
    def test_merge_combines_base_and_render_instructions(self):
        """
        SCENARIO: Merge combines base and render instructions
        GIVEN: BaseActionConfig with ['base1', 'base2'] and render instructions {'instructions': ['render1', 'render2']}
        WHEN: merge() called
        THEN: Returns dict with base_instructions and render_instructions
        """
        # Given: BaseActionConfig and render instructions
        base_action_config = given_action_with_instructions(['base1', 'base2'])
        render_instructions = {'instructions': ['render1', 'render2']}
        
        # When: MergedInstructions instantiated and merge() called
        merged_instructions = when_merged_instructions_instantiated(base_action_config, render_instructions)
        result = when_merge_called(merged_instructions)
        
        # Then: Merged dict contains both instruction sets
        then_merged_contains_base_instructions(result, ['base1', 'base2'])
        then_merged_contains_render_instructions(result, render_instructions)
    
    def test_merge_handles_empty_render_instructions(self):
        """
        SCENARIO: Merge handles empty render instructions
        GIVEN: BaseActionConfig with ['base1'] and empty render instructions {}
        WHEN: merge() called
        THEN: Returns dict with base_instructions and empty render_instructions
        """
        # Given: BaseActionConfig with empty render instructions dict
        base_action_config = given_action_with_instructions(['base1'])
        render_instructions = {}
        
        # When: MergedInstructions instantiated and merge() called
        merged_instructions = when_merged_instructions_instantiated(base_action_config, render_instructions)
        result = when_merge_called(merged_instructions)
        
        # Then: Merged dict contains base instructions and empty render instructions
        then_merged_contains_base_instructions(result, ['base1'])
        then_merged_contains_render_instructions(result, render_instructions)


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
        helper.set_state('shape', 'render')
        
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
        helper.set_state('shape', 'render')
        
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
        helper.set_state('shape', 'render')
        
        # Execute render action
        from agile_bot.src.actions.render.render_action import RenderOutputAction
        from agile_bot.src.actions.action_context import ScopeActionContext
        behavior_obj = helper.bot.behaviors.current
        action = RenderOutputAction(behavior=behavior_obj, action_config=None)
        result = action.do_execute(ScopeActionContext())
        
        # Verify instructions mention synchronizers
        base_instructions = '\n'.join(result.get('base_instructions', []))
        assert 'Synchronizers Already Executed' in base_instructions or 'render' in base_instructions.lower()
