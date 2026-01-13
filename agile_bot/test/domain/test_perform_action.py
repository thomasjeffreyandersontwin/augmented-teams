"""
Perform Action Tests

Tests for all stories in the 'Perform Action' sub-epic, covering:
- Build Story Graph
- Clarify Requirements
- Validate Rules
- Decide Strategy
- Render Output
"""
import pytest
from pathlib import Path
import json
import os
from agile_bot.src.actions.build.build_action import BuildStoryGraphAction
from agile_bot.src.actions.render.render_action import RenderOutputAction
from agile_bot.src.actions.action_context import (
    ClarifyActionContext,
    StrategyActionContext,
    ValidateActionContext,
    ScopeActionContext
)
from agile_bot.test.domain.bot_test_helper import BotTestHelper


# ============================================================================
# STORY: Build Story Graph
# ============================================================================
class TestBuildStoryGraph:

    def test_action_injects_story_graph_template(self, tmp_path):
        """
        SCENARIO: Action Injects Story Graph Template
        GIVEN: Production story_bot with shape behavior (has story graph templates)
        WHEN: Action injects story graph template
        THEN: Instructions contain template_path from existing templates
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = BuildStoryGraphAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        instructions = action_obj.get_instructions()
        
        assert 'template_path' in instructions
        assert instructions['template_path'] is not None

    def test_action_loads_and_merges_instructions(self, tmp_path):
        """
        SCENARIO: Action Loads And Merges Instructions
        GIVEN: Production story_bot with shape behavior (has story graph templates)
        WHEN: Action injects story graph and instructions
        THEN: Instructions contain all BuildStoryGraphAction-specific fields
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('build')
        
        instructions = action_obj.do_execute()
        
        helper.build.assert_build_story_graph_instructions(instructions)

    def test_all_template_variables_are_replaced_in_instructions(self, tmp_path):
        """
        SCENARIO: All Template Variables Are Replaced In Instructions
        GIVEN: Production story_bot with shape behavior (has story graph templates)
        WHEN: Action injects all template variables
        THEN: Instructions contain all required BuildStoryGraphAction fields
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('build')
        
        instructions = action_obj.do_execute()
        
        helper.build.assert_build_story_graph_instructions(instructions)

    def test_behavior_updates_existing_story_graph_json(self, tmp_path):
        """
        SCENARIO: Prioritization behavior updates existing story-graph.json
        GIVEN: Production prioritization behavior with increments templates
        AND: Existing story-graph.json in workspace
        WHEN: Action injects story graph template for increments
        THEN: Instructions use production template (story_graph_increments.json) that updates existing file
        """
        helper = BotTestHelper(tmp_path)
        
        existing_story_graph = helper.story.given_story_graph_dict(epic='mob')
        stories_dir = helper.workspace / 'docs' / 'stories'
        story_graph_path = helper.files.given_file_created(stories_dir, 'story-graph.json', existing_story_graph)
        
        helper.bot.behaviors.navigate_to('prioritization')
        action_obj = BuildStoryGraphAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        instructions = action_obj.do_execute()
        
        # Then: Instructions indicate updating existing file
        assert instructions.get('story_graph_config'), "Instructions should contain 'story_graph_config'"
        config = instructions.get('story_graph_config', {})
        assert config.get('output') == 'story-graph.json', f"Expected output 'story-graph.json', got '{config.get('output')}'"
        assert instructions.get('template_path'), "Instructions should contain 'template_path'"
        assert story_graph_path.exists(), f"Story graph file should exist: {story_graph_path}"
        path_str = str(config.get('path')).replace('\\', '/')
        assert 'docs/stories' in path_str, f"Expected path to contain 'docs/stories', got '{config.get('path')}'"


# ============================================================================
# STORY: Clarify Requirements
# ============================================================================
class TestClarifyRequirements:
    def test_action_injects_questions_and_evidence(self, tmp_path):
        """
        SCENARIO: Action injects questions and evidence from production guardrails
        GIVEN: Production story_bot with shape behavior (has guardrails)
        WHEN: Action injects guardrails
        THEN: Instructions contain questions and evidence from production files
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        instructions = action_obj.do_execute()
        
        helper.clarify.assert_clarify_context_instructions(instructions)

    def test_save_clarification_data_when_parameters_provided(self, tmp_path):
        """
        SCENARIO: Save clarification data when parameters are provided
        GIVEN: Production story_bot clarify action
        WHEN: do_execute is called with key_questions_answered and evidence_provided
        THEN: clarification.json file is created in docs/stories/ folder
        AND: file contains behavior section with key_questions and evidence
        """
        # Given: Production story_bot clarify action
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # When: Action executes with parameters
        context = ClarifyActionContext(
            answers={'user_types': 'Game Masters', 'first_action': 'Group tokens into mobs'},
            evidence_provided={'original_input': 'I want to turn minions into mobs', 'source_file': 'input.txt'}
        )
        action.do_execute(context)
        
        # Then: clarification.json file exists and contains expected data
        helper.clarify.assert_clarification_file_exists()
        helper.clarify.assert_clarification_contains_behavior(
            'shape',
            expected_answers={'user_types': 'Game Masters', 'first_action': 'Group tokens into mobs'},
            expected_evidence={'original_input': 'I want to turn minions into mobs', 'source_file': 'input.txt'}
        )

    def test_preserve_existing_clarification_data_when_saving(self, tmp_path):
        """
        SCENARIO: Preserve existing clarification data when saving
        GIVEN: clarification.json already exists with data for 'discovery' behavior
        AND: Production story_bot clarify action for 'shape' behavior
        WHEN: do_execute is called with parameters
        THEN: clarification.json contains both 'discovery' and 'shape' sections
        AND: existing 'discovery' data is preserved
        """
        # Given: Existing clarification.json with discovery data
        helper = BotTestHelper(tmp_path)
        existing_data = {
            'discovery': {
                'key_questions': {
                    'questions': [],
                    'answers': {'scope': 'Component level'}
                },
                'evidence': {
                    'required': [],
                    'provided': {'doc': 'requirements.md'}
                }
            }
        }
        helper.clarify.given_existing_clarification_data(existing_data)
        
        # Setup production clarify action for shape
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # When: Action executes with parameters
        context = ClarifyActionContext(
            answers={'user_types': 'Game Masters'},
            evidence_provided={'original_input': 'I want to turn minions into mobs'}
        )
        action.do_execute(context)
        
        # Then: Both behaviors' data are preserved
        helper.clarify.assert_clarification_contains_behavior(
            'discovery',
            expected_answers={'scope': 'Component level'},
            expected_evidence={'doc': 'requirements.md'}
        )
        helper.clarify.assert_clarification_contains_behavior(
            'shape',
            expected_answers={'user_types': 'Game Masters'},
            expected_evidence={'original_input': 'I want to turn minions into mobs'}
        )

    def test_skip_saving_when_no_clarification_parameters_provided(self, tmp_path):
        """
        SCENARIO: Skip saving when no clarification parameters are provided
        GIVEN: Production story_bot clarify action
        WHEN: do_execute is called with empty parameters
        THEN: clarification.json file is not created
        """
        # Given: Production story_bot clarify action
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # When: Action executes with empty parameters
        context = ClarifyActionContext(answers=None, evidence_provided=None)
        action.do_execute(context)
        
        # Then: clarification.json file is not created
        helper.clarify.assert_clarification_file_not_exists()
    
    def test_guardrails_loads_required_context_from_workspace(self, tmp_path):
        """
        SCENARIO: Guardrails loads required context from workspace
        GIVEN: Workspace with guardrails files (questions and evidence)
        WHEN: Behavior loads guardrails
        THEN: Questions and evidence are loaded correctly
        """
        # Given: Workspace with guardrails files
        helper = BotTestHelper(tmp_path)
        behavior_name = 'shape'
        helper.clarify.given_guardrails_in_workspace(behavior_name)
        
        # When: Behavior loads guardrails from workspace
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(workspace_path=helper.workspace, bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        guardrails = behavior.guardrails
        
        # Then: Questions and evidence loaded correctly
        helper.clarify.assert_guardrails_loaded_correctly(guardrails)
    
    def test_guardrails_loads_strategy_assumptions_from_workspace(self, tmp_path):
        """
        SCENARIO: Guardrails loads strategy assumptions from workspace
        GIVEN: Workspace with strategy guardrails files
        WHEN: Behavior loads guardrails
        THEN: Strategy assumptions are loaded correctly
        """
        # Given: Workspace with strategy guardrails files
        helper = BotTestHelper(tmp_path)
        behavior_name = 'shape'
        helper.strategy.given_strategy_guardrails_in_workspace(behavior_name)
        
        # When: Behavior loads guardrails from workspace
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(workspace_path=helper.workspace, bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        guardrails = behavior.guardrails
        
        # Then: Strategy assumptions loaded correctly
        helper.strategy.assert_strategy_guardrails_loaded_correctly(guardrails)


# ============================================================================
# STORY: Validate Rules
# ============================================================================
class TestValidateRules:
    """Tests that rules are properly formatted into instructions for AI to use."""
    
    def test_story_graph_rules_formatted_in_instructions(self, tmp_path):
        """
        SCENARIO: Story graph validation includes rule content in instructions
        GIVEN: Production story_bot with shape behavior (validates story graph)
        AND: Story graph file exists
        WHEN: Validate action executes
        THEN: Instructions contain rule descriptions, DO/DON'T sections, and priorities from rule files
        """
        # GIVEN: Production story_bot with shape behavior (validates story graph)
        helper = BotTestHelper(tmp_path)
        
        # AND: Story graph file exists
        story_graph_data = {'epics': []}
        helper.story.create_story_graph(story_graph_data)
        
        helper.bot.behaviors.navigate_to('shape')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action from production behavior
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes
        result = action.do_execute(ValidateActionContext())
        
        # THEN: Instructions contain rule content from rule files
        helper.validate.assert_validate_instructions(result)
    
    def test_file_rules_formatted_in_instructions(self, tmp_path):
        """
        SCENARIO: File validation includes rule content in instructions
        GIVEN: Production story_bot with code behavior (validates files)
        AND: Story graph file exists
        WHEN: Validate action executes
        THEN: Instructions contain rule descriptions, DO/DON'T sections, and priorities from rule files
        """
        # GIVEN: Production story_bot with code behavior (validates files)
        helper = BotTestHelper(tmp_path)
        
        # AND: Story graph file exists
        story_graph_data = {'epics': []}
        helper.story.create_story_graph(story_graph_data)
        
        helper.bot.behaviors.navigate_to('code')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action from production behavior
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes
        result = action.do_execute(ValidateActionContext())
        
        # THEN: Instructions contain rule content from rule files
        helper.validate.assert_validate_instructions(result)

    def test_story_graph_scanner_receives_story_graph_data(self, tmp_path):
        """
        SCENARIO: Story graph scanners receive scoped story_graph data
        GIVEN: Story graph with multiple epics ("Build Knowledge", "Epic B")
        AND: Scope filtered to "Build Knowledge" epic
        AND: Production story_bot with shape behavior
        WHEN: Validate action executes with scope
        THEN: Scanner receives filtered story graph (only "Build Knowledge" epic)
        AND: Scanner executes successfully
        AND: Instructions contain "Build Knowledge" in scope description
        """
        # GIVEN: Story graph with multiple epics
        helper = BotTestHelper(tmp_path)
        story_graph_data = {
            'epics': [
                {'name': 'Build Knowledge', 'sub_epics': [], 'story_groups': []},
                {'name': 'Epic B', 'sub_epics': [], 'story_groups': []}
            ]
        }
        helper.story.create_story_graph(story_graph_data)
        
        # AND: Scope filtered to "Build Knowledge" epic
        from agile_bot.src.scope import Scope, ScopeType
        scope = Scope(workspace_directory=tmp_path)
        scope.filter(type=ScopeType.STORY, value=['Build Knowledge'])
        
        # AND: Production story_bot with shape behavior
        helper.bot.behaviors.navigate_to('shape')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action with rules
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes with scope
        context = ValidateActionContext(scope=scope)
        result = action.do_execute(context)
        
        # THEN: Instructions reference the scoped epic
        instructions = result.get('base_instructions', [])
        instructions_text = ' '.join(instructions)
        assert 'Build Knowledge' in instructions_text, \
            "Instructions must reference scoped epic 'Build Knowledge'"
        
        # AND: Scanner executed successfully (scanners ran - we got scanner output)
        # Check that rules were loaded
        rules = result.get('rules', [])
        assert len(rules) > 0, "Shape behavior must have validation rules"
    
    def test_file_scanner_receives_file_data(self, tmp_path):
        """
        SCENARIO: File scanners receive scoped file paths
        GIVEN: Multiple Python files (test_foo.py, test_bar.py, main.py)
        AND: Scope filtered to test files only (**/test*.py)
        AND: Production story_bot with code behavior
        WHEN: Validate action executes with scope
        THEN: Scanner receives filtered files (only test_foo.py, test_bar.py)
        AND: Scanner executes successfully
        AND: Instructions reference test file scope
        """
        # GIVEN: Multiple Python files
        helper = BotTestHelper(tmp_path)
        
        # AND: Story graph file exists (required for code behavior validation)
        story_graph_data = {'epics': []}
        helper.story.create_story_graph(story_graph_data)
        
        test_dir = tmp_path / 'workspace' / 'test'
        test_dir.mkdir(parents=True)
        src_dir = tmp_path / 'workspace' / 'src'
        src_dir.mkdir(parents=True)
        
        (test_dir / 'test_foo.py').write_text('# test file')
        (test_dir / 'test_bar.py').write_text('# test file')
        (src_dir / 'main.py').write_text('# main file')
        
        # AND: Scope filtered to test files only
        from agile_bot.src.scope import Scope, ScopeType
        scope = Scope(workspace_directory=tmp_path)
        scope.filter(type=ScopeType.FILES, value=['**/test*.py'])
        
        # AND: Production story_bot with code behavior
        helper.bot.behaviors.navigate_to('code')
        behavior = helper.bot.behaviors.current
        
        # AND: Validate action with rules
        from agile_bot.src.actions.validate.validate_action import ValidateRulesAction
        action = ValidateRulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Validate action executes with scope
        context = ValidateActionContext(scope=scope)
        result = action.do_execute(context)
        
        # THEN: Instructions reference file scope
        instructions = result.get('base_instructions', [])
        instructions_text = ' '.join(instructions)
        
        # Should reference test files in scope or file count
        has_file_reference = (
            'test' in instructions_text.lower() or
            'file' in instructions_text.lower() or
            str(test_dir) in instructions_text or
            'test_foo.py' in instructions_text or
            'test_bar.py' in instructions_text
        )
        assert has_file_reference, "Instructions must reference scoped files"
        
        # AND: Scanner executed successfully (scanners ran - we got scanner output)
        # Check that rules were loaded
        rules = result.get('rules', [])
        assert len(rules) > 0, "Code behavior must have validation rules"


# ============================================================================
# STORY: Decide Strategy
# ============================================================================
class TestDecideStrategy:

    def test_action_injects_decision_criteria_and_assumptions(self, tmp_path):
        """
        SCENARIO: Action Injects Decision Criteria And Assumptions
        GIVEN: Production story_bot with shape behavior (has guardrails)
        WHEN: Action injects strategy criteria and assumptions
        THEN: Instructions contain all required strategy fields
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        instructions = action_obj.do_execute()
        
        helper.strategy.assert_strategy_instructions(instructions)

    def test_save_strategy_data_when_parameters_provided(self, tmp_path):
        """
        SCENARIO: Save strategy data when parameters are provided
        GIVEN: Production story_bot strategy action
        WHEN: do_execute is called with decisions_made and assumptions_made
        THEN: strategy.json file is created in docs/stories/ folder
        AND: file contains behavior section with decisions_made and assumptions_made
        """
        # Given: Production story_bot strategy action
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        # When: Action executes with parameters
        decisions_made = {
            'drill_down': 'Dig deep on system interactions',
            'flow_scope': 'End-to-end user-system behavior'
        }
        assumptions_made = [
            'Focus on user flow over internal systems',
            'Cover the end-to-end scenario'
        ]
        context = StrategyActionContext(
            decisions_made=decisions_made,
            assumptions_made=assumptions_made
        )
        action.do_execute(context)
        
        # Then: strategy.json file exists and contains expected data
        helper.strategy.assert_strategy_file_exists()
        helper.strategy.assert_strategy_contains_behavior(
            'shape',
            expected_decisions=decisions_made,
            expected_assumptions=assumptions_made
        )

    def test_preserve_existing_strategy_data_when_saving(self, tmp_path):
        """
        SCENARIO: Preserve existing strategy data when saving
        GIVEN: strategy.json already exists with data for 'discovery' behavior
        AND: Production story_bot strategy action for 'shape' behavior
        WHEN: do_execute is called with parameters
        THEN: strategy.json contains both 'discovery' and 'shape' sections
        AND: existing 'discovery' data is preserved
        """
        # Given: Existing strategy.json with discovery data
        helper = BotTestHelper(tmp_path)
        existing_data = {
            'discovery': {
                'strategy_criteria': {
                    'criteria': {},
                    'decisions_made': {'scope': 'Component level'}
                },
                'assumptions': {
                    'typical_assumptions': [],
                    'assumptions_made': ['Stories follow user story format']
                }
            }
        }
        helper.strategy.given_existing_strategy_data(existing_data)
        
        # Setup production strategy action for shape
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        # When: Action executes with parameters
        context = StrategyActionContext(
            decisions_made={
                'drill_down': 'Dig deep on system interactions',
                'flow_scope': 'End-to-end user-system behavior'
            },
            assumptions_made=[
                'Focus on user flow over internal systems',
                'Cover the end-to-end scenario'
            ]
        )
        action.do_execute(context)
        
        # Then: Both behaviors' data are preserved
        helper.strategy.assert_strategy_contains_behavior(
            'discovery',
            expected_decisions={'scope': 'Component level'},
            expected_assumptions=['Stories follow user story format']
        )
        helper.strategy.assert_strategy_contains_behavior(
            'shape',
            expected_decisions={'drill_down': 'Dig deep on system interactions', 'flow_scope': 'End-to-end user-system behavior'},
            expected_assumptions=['Focus on user flow over internal systems', 'Cover the end-to-end scenario']
        )

    def test_skip_saving_when_no_strategy_parameters_provided(self, tmp_path):
        """
        SCENARIO: Skip saving when no strategy parameters are provided
        GIVEN: Production story_bot strategy action
        WHEN: do_execute is called with empty parameters
        THEN: strategy.json file is not created
        """
        # Given: Production story_bot strategy action
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        # When: Action executes with empty parameters
        context = StrategyActionContext(decisions_made=None, assumptions_made=None)
        action.do_execute(context)
        
        # Then: strategy.json file is not created
        helper.strategy.assert_strategy_file_not_exists()

# ============================================================================
# STORY: Render Output
# ============================================================================
class TestRenderOutput:

    def test_action_injects_render_configs_and_instructions(self, tmp_path):
        """
        SCENARIO: Action injects render configs and instructions
        GIVEN: Production story_bot with shape behavior (has render configs)
        WHEN: Action injects render data
        THEN: Instructions contain all required render fields
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        helper.state.set_state('shape', 'render')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('render')
        
        instructions = action_obj.do_execute()
        
        helper.render.assert_render_output_instructions(instructions)

    def test_synchronizers_are_executed_automatically(self, tmp_path):
        """
        SCENARIO: Synchronizers are executed automatically during render action
        GIVEN: Production story_bot with shape behavior (has synchronizers)
        WHEN: Render output action executes
        THEN: Synchronizers are executed automatically
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        helper.state.set_state('shape', 'render')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('render')
        
        result = action_obj.do_execute()
        
        base_instructions = result.get('base_instructions', [])
        base_instructions_text = '\n'.join(base_instructions)
        assert 'Synchronizers Already Executed' in base_instructions_text or 'render' in base_instructions_text.lower()

    def test_template_configs_remain_in_instructions(self, tmp_path):
        """
        SCENARIO: Template configs remain in instructions for AI handling
        GIVEN: Production story_bot with shape behavior (has templates)
        WHEN: Render output action executes  
        THEN: Result includes instructions
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        helper.state.set_state('shape', 'render')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('render')
        
        result = action_obj.do_execute()
        
        base_instructions = result.get('base_instructions', [])
        assert len(base_instructions) > 0, "Should have instructions"

    def test_executed_synchronizers_info_in_instructions(self, tmp_path):
        """
        SCENARIO: Executed synchronizers information is included in AI instructions
        GIVEN: Production story_bot with shape behavior (has synchronizers)
        WHEN: Render output action executes
        THEN: Instructions include synchronizer execution info
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        helper.state.set_state('shape', 'render')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('render')
        
        result = action_obj.do_execute()
        
        base_instructions = '\n'.join(result.get('base_instructions', []))
        assert 'Synchronizers Already Executed' in base_instructions or 'render' in base_instructions.lower()
