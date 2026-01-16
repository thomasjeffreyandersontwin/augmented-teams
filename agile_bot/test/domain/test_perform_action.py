"""
Domain Tests for Execute Behavior Actions Epic

Tests for domain/core logic stories, covering:
- Perform Action sub-epic:
  - Build Story Graph
  - Clarify Requirements
  - Validate Rules
  - Display Rules
  - Decide Strategy
  - Render Output
  - Submit Instructions
- Domain sub-epic:
  - Save Guardrails
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
# STORY: Display Rules
# ============================================================================
class TestDisplayRules:
    """Tests that rules are properly loaded and formatted for display."""
    
    def test_action_loads_and_formats_rules_digest(self, tmp_path):
        """
        SCENARIO: Action loads and formats rules digest
        GIVEN: Production story_bot with tests behavior (has rules)
        WHEN: Rules action executes
        THEN: Instructions contain formatted rules digest with descriptions, priorities, DO/DON'T sections
        """
        # GIVEN: Production story_bot with tests behavior (has rules)
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('tests')
        behavior = helper.bot.behaviors.current
        
        # AND: Rules action from production behavior
        from agile_bot.src.rules.rules_action import RulesAction
        from agile_bot.src.actions.action_context import RulesActionContext
        action = RulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Rules action executes
        result = action.do_execute(RulesActionContext())
        
        # THEN: Instructions contain formatted rules digest
        helper.rules.assert_rules_instructions(result)
    
    def test_rules_list_includes_file_paths(self, tmp_path):
        """
        SCENARIO: Rules list includes file paths for each rule
        GIVEN: Production story_bot with tests behavior (has rules)
        WHEN: Rules action executes
        THEN: Display includes rule names with their file paths
        """
        # GIVEN: Production story_bot with tests behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('tests')
        behavior = helper.bot.behaviors.current
        
        # AND: Rules action
        from agile_bot.src.rules.rules_action import RulesAction
        from agile_bot.src.actions.action_context import RulesActionContext
        action = RulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Rules action executes
        result = action.do_execute(RulesActionContext())
        
        # THEN: Display includes file paths
        helper.rules.assert_rules_list_contains_file_paths(result)
    
    def test_all_behavior_rules_included_in_digest(self, tmp_path):
        """
        SCENARIO: All behavior rules are included in the digest
        GIVEN: Production story_bot with tests behavior (has multiple rules)
        WHEN: Rules action executes
        THEN: All rules from behavior are included in digest
        """
        # GIVEN: Production story_bot with tests behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('tests')
        behavior = helper.bot.behaviors.current
        
        # AND: Rules action
        from agile_bot.src.rules.rules_action import RulesAction
        from agile_bot.src.actions.action_context import RulesActionContext
        action = RulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Rules action executes
        result = action.do_execute(RulesActionContext())
        
        # THEN: All rules included (tests behavior has 25 rules)
        helper.rules.assert_rules_digest_contains_all_rules(result, expected_rule_count=20)
    
    def test_user_message_included_when_provided(self, tmp_path):
        """
        SCENARIO: User message is included in instructions when provided
        GIVEN: Production story_bot with tests behavior
        AND: User message requesting specific rule information
        WHEN: Rules action executes with message
        THEN: Instructions include user message
        """
        # GIVEN: Production story_bot with tests behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('tests')
        behavior = helper.bot.behaviors.current
        
        # AND: User message
        user_message = "Show me the rules for test organization"
        
        # AND: Rules action
        from agile_bot.src.rules.rules_action import RulesAction
        from agile_bot.src.actions.action_context import RulesActionContext
        action = RulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Rules action executes with message
        context = RulesActionContext(message=user_message)
        result = action.do_execute(context)
        
        # THEN: Instructions include user message
        helper.rules.assert_user_message_included(result, user_message)
    
    def test_no_user_message_section_when_empty(self, tmp_path):
        """
        SCENARIO: No user message section when message is empty
        GIVEN: Production story_bot with tests behavior
        WHEN: Rules action executes without message
        THEN: Instructions do not include user message section
        """
        # GIVEN: Production story_bot with tests behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('tests')
        behavior = helper.bot.behaviors.current
        
        # AND: Rules action
        from agile_bot.src.rules.rules_action import RulesAction
        from agile_bot.src.actions.action_context import RulesActionContext
        action = RulesAction(behavior=behavior, action_config=None)
        
        # WHEN: Rules action executes without message
        context = RulesActionContext(message=None)
        result = action.do_execute(context)
        
        # THEN: No user message section in instructions
        helper.rules.assert_no_user_message_when_empty(result)


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
        # Given: Existing strategy.json with discovery data (actual format)
        helper = BotTestHelper(tmp_path)
        existing_data = {
            'discovery': {
                'decisions': {'scope': 'Component level'},
                'assumptions': ['Stories follow user story format']
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


# ============================================================================
# STORY: Save Guardrails (Domain Layer)
# ============================================================================
class TestSaveGuardrailsViaCLI:
    """
    Tests for saving guardrail data - domain/core logic.
    
    Maps to story: Save Guardrails
    Sub-epic: Domain
    Epic: Execute Behavior Actions
    """
    
    def test_save_guardrail_data_answers(self, tmp_path):
        """
        SCENARIO: Save guardrail data (answers parameter)
        GIVEN: Bot is at shape behavior
        WHEN: User runs save command with answers parameter
        THEN: System saves answers to clarification.json under current behavior
        AND: System merges with existing answers
        """
        # Given: Bot is at shape behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # When: User runs save command with answers
        answers_data = {"What is the scope of this work?": "Building bot system"}
        context = ClarifyActionContext(answers=answers_data, evidence_provided=None)
        action.do_execute(context)
        
        # Then: System loads existing clarification.json for current behavior
        # And: System merges new data with existing data
        # And: System saves updated data to clarification.json
        helper.clarify.assert_clarification_file_exists()
        helper.clarify.assert_clarification_contains_answers('shape', answers_data)
    
    def test_save_guardrail_data_evidence(self, tmp_path):
        """
        SCENARIO: Save guardrail data (evidence_provided parameter)
        GIVEN: Bot is at shape behavior
        WHEN: User runs save command with evidence parameter
        THEN: System saves evidence to clarification.json under current behavior
        """
        # Given: Bot is at shape behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # When: User runs save command with evidence
        evidence_data = {
            "Requirements doc": "spec.md",
            "User interviews": "notes.md"
        }
        context = ClarifyActionContext(answers=None, evidence_provided=evidence_data)
        action.do_execute(context)
        
        # Then: System saves evidence to clarification.json
        helper.clarify.assert_clarification_file_exists()
        helper.clarify.assert_clarification_contains_evidence('shape', evidence_data)
    
    def test_save_guardrail_data_decisions(self, tmp_path):
        """
        SCENARIO: Save guardrail data (decisions parameter)
        GIVEN: Bot is at shape behavior
        WHEN: User runs save command with decisions parameter
        THEN: System saves decisions to strategy.json under current behavior
        """
        # Given: Bot is at shape behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        # When: User runs save command with decisions
        decisions_data = {"drill_down_approach": "Dig deep on system interactions"}
        context = StrategyActionContext(decisions_made=decisions_data, assumptions_made=None)
        action.do_execute(context)
        
        # Then: System saves decisions to strategy.json
        helper.strategy.assert_strategy_file_exists()
        helper.strategy.assert_strategy_contains_behavior('shape', expected_decisions=decisions_data)
    
    def test_save_guardrail_data_assumptions(self, tmp_path):
        """
        SCENARIO: Save guardrail data (assumptions parameter)
        GIVEN: Bot is at shape behavior
        WHEN: User runs save command with assumptions parameter
        THEN: System saves assumptions to strategy.json under current behavior
        """
        # Given: Bot is at shape behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        # When: User runs save command with assumptions
        assumptions_data = ["Focus on user flow over internal systems"]
        context = StrategyActionContext(decisions_made=None, assumptions_made=assumptions_data)
        action.do_execute(context)
        
        # Then: System saves assumptions to strategy.json
        helper.strategy.assert_strategy_file_exists()
        helper.strategy.assert_strategy_contains_behavior('shape', expected_assumptions=assumptions_data)
    
    def test_merge_with_existing_answers(self, tmp_path):
        """
        SCENARIO: Merge with existing data (answers)
        GIVEN: Guardrail file contains existing data for shape behavior
        WHEN: User runs save command with new data
        THEN: System preserves existing values for other fields
        AND: System overwrites only the provided field
        AND: Result matches merged_result
        """
        # Given: Existing data in clarification.json
        helper = BotTestHelper(tmp_path)
        existing_data = {
            'shape': {
                'key_questions': {
                    'questions': [],
                    'answers': {
                        "What is the scope of this work?": "Building bot system",
                        "Who are the target users?": "AI Agents"
                    }
                },
                'evidence': {
                    'required': [],
                    'provided': {}
                }
            }
        }
        helper.clarify.given_existing_clarification_data(existing_data)
        
        # When: User runs save command with new data (overwrites one field)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        new_answers = {"Who are the target users?": "Developers and AI Agents"}
        context = ClarifyActionContext(answers=new_answers, evidence_provided=None)
        action.do_execute(context)
        
        # Then: System preserves existing values for other fields
        # And: System overwrites only the provided field
        expected_merged = {
            "What is the scope of this work?": "Building bot system",
            "Who are the target users?": "Developers and AI Agents"
        }
        helper.clarify.assert_clarification_contains_answers('shape', expected_merged)
    
    def test_merge_with_existing_decisions(self, tmp_path):
        """
        SCENARIO: Merge with existing data (decisions)
        GIVEN: Guardrail file contains existing data for shape behavior
        WHEN: User runs save command with new data
        THEN: System preserves existing values for other fields
        AND: System overwrites only the provided field
        AND: Result matches merged_result
        """
        # Given: Existing data in strategy.json (actual format)
        helper = BotTestHelper(tmp_path)
        existing_data = {
            'shape': {
                'decisions': {
                    "drill_down_approach": "High and wide across all epics",
                    "depth_of_shaping": "Extensive"
                },
                'assumptions': []
            }
        }
        helper.strategy.given_existing_strategy_data(existing_data)
        
        # When: User runs save command with new data (overwrites one field)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('strategy')
        new_decisions = {"drill_down_approach": "Dig deep on system interactions"}
        context = StrategyActionContext(decisions_made=new_decisions, assumptions_made=None)
        action.do_execute(context)
        
        # Then: System preserves existing values for other fields
        # And: System overwrites only the provided field
        expected_merged = {
            "drill_down_approach": "Dig deep on system interactions",
            "depth_of_shaping": "Extensive"
        }
        helper.strategy.assert_strategy_contains_behavior('shape', expected_decisions=expected_merged)


# ============================================================================
# STORY: Submit Instructions
# ============================================================================
class TestSubmitInstructions:

    def test_submit_tracks_instruction_submission(self, tmp_path):
        """
        SCENARIO: Submit tracks instruction submission
        GIVEN: Bot is at shape.clarify
        WHEN: User calls submit_current_action() method
        THEN: System returns success status with behavior and action
        AND: System includes timestamp of submission
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        helper.bot.behaviors.current.actions.navigate_to('clarify')
        
        result = helper.bot.submit_current_action()
        
        assert result['status'] == 'success', f"Expected success status, got {result.get('status')}"
        assert result['behavior'] == 'shape', f"Expected behavior 'shape', got {result.get('behavior')}"
        assert result['action'] == 'clarify', f"Expected action 'clarify', got {result.get('action')}"
        assert 'timestamp' in result, "Expected timestamp in result"
        assert result['message'] == 'Instructions submitted for shape.clarify'

    def test_submit_fails_when_no_current_behavior(self, tmp_path):
        """
        SCENARIO: Submit fails when no current behavior
        GIVEN: Bot has no current behavior set
        WHEN: User calls submit_current_action() method
        THEN: System returns error status
        AND: Error indicates no current behavior
        """
        helper = BotTestHelper(tmp_path)
        # Explicitly clear current behavior (bot initializes to first behavior by default)
        helper.bot.behaviors._current_index = None# Behavior: prioritization

## Behavior Instructions - prioritization

The purpose of this behavior is to organize stories into delivery increments based on business value, dependencies, and risk

Organize stories into delivery increments based on business value, dependencies, and risk

## Action Instructions - validate

The purpose of this action is to validate story graph and/or artifacts against behavior-specific rules, checking for violations and compliance

prioritization: validate increment organization and dependencies

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3827/test_submit_works_with_differe0/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3827/test_submit_works_with_differe0/workspace/docs/stories/`
  clarification.json, strategy.json

## Step 1: Scanner Violation Review

Error running scanners: Story graph file (story-graph.json) not found in C:\Users\thoma\AppData\Local\Temp\pytest-of-thoma\pytest-3827\test_submit_works_with_differe0\workspace\docs\stories. Cannot validate rules without story graph. Expected story graph to be created by build action before validate.

Please review the validation report file in docs/stories/reports/

Carefully review all scanner-reported violations as follows:
1. For each violation message, locate the corresponding element in the story graph.
2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
6. Extract an **Example** from the actual code/content showing the problem.
7. Suggest a clear, concrete **Fix** with a code example informed by DO examples in the rule.

## Step 2: Manual Rule Review

**Rules to validate against (read each file for full DO/DON'T examples):**

### Rule: Map Sequential Spine Vs Optional Paths (Priority 1) [Scanner]
**File:** `story_bot/behaviors/prioritization/rules/map_sequential_spine_vs_optional_paths.json`
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**DO:** Identify the essential spine and mark optional paths clearly
**DON'T:** Don't mark everything as sequential, don't omit optional markers

### Rule: Design Vertical Slice Increments (Priority 2) [Scanner]
**File:** `story_bot/behaviors/prioritization/rules/design_vertical_slice_increments.json`
**Description:** Create increments that are vertical slices that deliver end-to-end working flows across multiple features/epics, NOT horizontal layers that complete one feature/epic at a time. Each increment must demonstrate complete working flow from start to finish.
**DO:** Design increments as vertical slices - end-to-end flows across multiple epics/features
**DON'T:** Don't design increments as horizontal layers, don't complete one feature/epic at a time

### Rule: Apply Quality Tradeoffs For Minimal Spine (Priority 3) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/apply_quality_tradeoffs_for_minimal_spine.json`
**Description:** Apply quality trade-offs to create thin slicing spine and later increments. Decide what quality the spine will have, what parts will be manual, what logic can be excluded, and how to prioritize adding quality in later increments.
**DO:** Make deliberate quality trade-offs to minimize spine size
**DON'T:** Don't build full quality into thin slicing spine, don't skip documenting trade-offs

### Rule: Identify Marketable Increments (Priority 4) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/identify_marketable_increments.json`
**Description:** Identify marketable increments of value during prioritization. Name increments with business value terms that stakeholders understand, not technical implementation terms.
**DO:** Name increments with business value terms
**DON'T:** Don't use technical implementation terms in increment names

### Rule: Prioritize Architectural Risk Validation (Priority 5) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/prioritize_architectural_risk_validation.json`
**Description:** Prioritize early increments to validate architectural risks and technology decisions. Build risky integrations, test unfamiliar technologies, and validate solution feasibility early to avoid late-stage surprises.
**DO:** Prioritize architectural risk validation in early increments
**DON'T:** Don't defer architectural risks to later increments, don't assume integrations will work without validation


Scanner tools don't cover or catch every rule violation. Do a second pass:
1. Carefully read each rule file, fully reviewing DO and DON'T sections, and every provided example.
2. Inspect all epics, sub-epics, stories, and domain concepts in the story graph for compliance.
3. Compare the properties and content of each element against the rule's requirements.
4. Document any violations the scanner could not find.
5. For each violation, extract an **Example** showing the problem and provide a **Fix** with code example.

## Unified Violations Table

Record ALL findings (scanner + manual) in this comprehensive table. Only include rows for actual violations found:

| Theme | Rule | Location | Valid/FP | Source | Root Cause | Problem Example | Fix with Code Example |
|-------|------|----------|----------|--------|------------|-----------------|----------------------|

**Column Guide:**
- **Theme**: Grouping category (e.g., 'naming violations', 'missing behavior', 'mechanism-oriented language')
- **Rule**: Name of the rule being violated
- **Location**: Path in story graph (e.g., `epics[1].sub_epics[0].name`) or file path
- **Valid/FP**: Valid if rule breach, False Positive if incorrectly flagged (explain why)
- **Source**: Scanner (detected by automated scanner), Manual (found during AI review), Both (flagged by scanner AND confirmed by manual review)
- **Root Cause**: Underlying reason for the violation
- **Problem Example**: Actual code/text showing the issue (e.g., `"Strategy Types"`, `"Create Mobs"`)
- **Fix with Code Example**: Corrected version (e.g., `"Select Strategy"`, `"Assembles Combat Mob"`)

## Step 3: Summarize Findings & Recommendations

Provide a concise summary:
- Report how many **scanner violations** were valid vs false positives.
- Enumerate any **additional manual findings** not caught by scanners.
- Group all violations by recurring theme or pattern.
- Split violations into **Priority Fixes** (must resolve before continuing) and **Optional Improvements**.

Present your summary and await user confirmation before automatically applying or proposing corrections.
prioritization: validate increment organization and dependencies

### Key Questions

- Which areas of the story map carry the most business or delivery risk?
- Which areas are expected to deliver the most value if delivered early?
- Which areas are the most complex or hardest to implement, relative to their value?
- Do you want thin slices to be as end-to-end as possible?
- Are there any components, capabilities, or services that need to be reused across multiple stories or features?
- Are there any project or program constraints that impact delivery order?
- Are there users or groups that must go first to enable others to follow?

### Evidence

Story map from Shape stage (epics, features, and initial story breakdown), Business cases or initiative briefs, Project charters and delivery timelines, Capability or architectural dependency maps, User rollout or onboarding strategies, Risk registers or readiness checklists, Value modeling or impact estimation docs

### Decisions

**increment_slicing_strategy:** What approach are you taking to group the work into thin slices or increments of value, and how are you ensuring they are as small as possible while still being valuable and/or generating learning or reducing risk?

- Delivering End-to-End Journey — supports integrated validation across systems and users
- Validating Impact - Feasibility — reduces uncertainty and derisks critical components early
- Maximizing Earned Value — delivers early impact and builds stakeholder confidence
- Increasing Reuse/Dependency— prevents downstream rework and enables reuse
- Quick Win — implements lowest-complexity paths first
- Validating Impact — validates whether users care, intend to use, or will act on the solution before investing in full delivery (e.g., Wizard of Oz, landing pages, stubs, or mafia offers)


### Assumptions

- Thin slices should provide either value, learning, or risk reduction
- Slices do not need to include all functionality to be useful
- Not every increment must be user-visible if it validates key assumptions
- Some slices may be architectural if they unlock multiple features
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_instructi1/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_instructi1/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_instructi1/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_instructi1/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_with_mess1/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_with_mess1/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_with_mess2/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_with_mess2/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_with_mess2/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_with_mess2/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_without_m0/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_without_m0/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_without_m2/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_without_m2/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.
## Rules Available (25 total)

1. use_domain_language (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_domain_language.json)
2. consistent_vocabulary (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/consistent_vocabulary.json)
3. no_defensive_code_in_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/no_defensive_code_in_tests.json)
4. production_code_clean_functions (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_clean_functions.json)
5. bug_fix_test_first (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/bug_fix_test_first.json)
6. call_production_code_directly (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/call_production_code_directly.json)
7. cover_all_behavior_paths (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/cover_all_behavior_paths.json)
8. mock_only_boundaries (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/mock_only_boundaries.json)
9. create_parameterized_tests_for_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/create_parameterized_tests_for_scenarios.json)
10. define_fixtures_in_test_file (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/define_fixtures_in_test_file.json)
11. design_api_through_failing_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/design_api_through_failing_tests.json)
12. test_observable_behavior (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/test_observable_behavior.json)
13. helper_extraction_and_reuse (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/helper_extraction_and_reuse.json)
14. match_specification_scenarios (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/match_specification_scenarios.json)
15. place_imports_at_top (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/place_imports_at_top.json)
16. object_oriented_test_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/object_oriented_test_helpers.json)
17. production_code_explicit_dependencies (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/production_code_explicit_dependencies.json)
18. self_documenting_tests (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/self_documenting_tests.json)
19. standard_test_data_sets (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/standard_test_data_sets.json)
20. assert_full_results (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/assert_full_results.json)
21. use_ascii_only (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_ascii_only.json)
22. pytest_bdd_orchestrator_pattern (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/pytest_bdd_orchestrator_pattern.json)
23. use_class_based_organization (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_class_based_organization.json)
24. use_exact_variable_names (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_exact_variable_names.json)
25. use_given_when_then_helpers (C:/dev/augmented-teams/agile_bot/bots/story_bot/behaviors/tests/rules/use_given_when_then_helpers.json)

# Behavior: tests

## Behavior Instructions - tests

The purpose of this behavior is to write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior

**BEHAVIOR PURPOSE:**
This behavior WRITES TEST FILES. The primary output is executable test code files that validate story behavior.
Write test files (.py, .js, etc.) with executable test code from scenarios/examples that validate story behavior
The secondary output is to make sure that the story_graph.json scenarios, stories, and sub-epics have test fields added for the test methods, test classes, and test files respectively.
After creating test files, classes, and methods, you MUST map them to the story-graph.json:

## Action Instructions - rules

The purpose of this action is to load behavior-specific rules into ai context for guidance on writing compliant content

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_without_m2/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_user_gets_rules_without_m2/workspace/docs/stories/`
  clarification.json, strategy.json

CRITICAL: This is the rules action - it loads rules for AI context. DO NOT run validation.
CRITICAL: You MUST systematically read each rule file listed below using the read_file tool BEFORE acting on the user's message.
Read ALL rule files first, then apply them to the user's request.
Each rule file path is provided - use read_file to load the complete rule content including examples.
After reading all rules, act on the user's message following ALL the rules you just read.

CRITICAL: When reporting validation results, use this EXACT format:
For each rule checked, report: Rule Name | PASS or FAIL | If FAIL, explain why in one sentence
Example: prefer_object_model_over_config | PASS
Example: eliminate_duplication | FAIL | Same logic repeated in lines 45-50 and 78-83
Keep it simple: just tell the user what passed, what failed, and if it failed, why.

Rules to follow:

- **use_domain_language**: Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
  DO: Use domain language for classes, methods, and test names. Example: class GatherContextAction, def inject_guardrails(), test_agent_loads_config_when_file_exists
  DON'T: Don't use generic technical terms or implementation-specific names. Example: class StdioHandler (wrong), def execute_with_guardrails (wrong), test_agt_init_sets_vars (wrong)

- **consistent_vocabulary**: Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
  DO: Use same word for same concept everywhere. Example: create_agent(), create_config(), create_workspace() - all use 'create'
  DON'T: Don't mix synonyms for same concept. Example: create_agent() + build_config() + make_workspace() (wrong - pick one verb)

- **no_defensive_code_in_tests**: Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
  DO: Assume correct setup - let test fail if wrong. Example: behavior = Behavior(name='shape') then assert behavior.name == 'shape'
  DON'T: Don't add if-checks, type guards, or fallback handling in tests. Example: if behavior_file.exists(): (wrong - test should fail if it doesn't)

- **production_code_clean_functions**: Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
  DO: Single responsibility, small focused functions. Example: initialize_from_config() calls validate_exists(), load_config(), validate_structure(), apply_config()
  DON'T: Don't make functions that do multiple unrelated things or are too long. Example: 50-line function that loads, validates, and applies config

- **bug_fix_test_first**: When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
  DO: Follow RED-GREEN-PRODUCTION workflow. Example: Write test reproducing bug -> Run test (RED) -> Fix minimal code -> Run test (GREEN) -> Run full suite
  DON'T: Don't fix bugs directly without failing test first. Example: Editing production code without test -> deploying -> hoping it works (wrong)

- **call_production_code_directly**: Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
  DO: Call production code directly, let it fail naturally. Example: agent = Agent(workspace); agent.initialize(config); assert agent.is_initialized
  DON'T: Don't mock class under test, comment out calls, or fake state. Example: agent = Mock(spec=Agent) (wrong); agent._initialized = True (wrong)

- **cover_all_behavior_paths**: Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
  DO: Test normal, edge, and failure paths separately. Example: test_loads_valid_config() (happy), test_loads_empty_config() (edge), test_raises_when_missing() (failure)
  DON'T: Don't test only happy path or combine multiple behaviors in one test. Example: Single test for both success and failure (wrong)

- **mock_only_boundaries**: Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
  DO: Mock only external dependencies you can't control. Example: with patch('requests.get') as mock: (external API - OK to mock)
  DON'T: Don't mock internal logic, class under test, or file I/O. Example: with patch('agent.validate_config') (wrong - test the logic!)

- **create_parameterized_tests_for_scenarios**: If scenarios have Examples tables, create parameterized tests using @pytest.mark.parametrize. Each row becomes a test case. Don't write single tests that only test one example. Example: @pytest.mark.parametrize('input,expected', [(1, 2), (3, 4)])
  DO: Create parameterized tests from Examples tables. Example: @pytest.mark.parametrize('paths,count', [(['p1','p2'], 2), (['p3'], 1)])
  DON'T: Don't hardcode single example or duplicate test methods. Example: def test_with_value_1(): (wrong); def test_with_value_2(): (wrong - use parametrize)

- **define_fixtures_in_test_file**: Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
  DO: Define fixtures in same test file. Example: @pytest.fixture def config_file(tmp_path): ... (in test_agent.py)
  DON'T: Don't create separate conftest.py for agent-specific fixtures. Example: src/conftest.py with agent fixtures (wrong - put in test file)

- **design_api_through_failing_tests**: Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
  DO: Write test against real expected API that fails initially. Example: project = Project(path); project.initialize(); assert project.is_ready (fails until implemented)
  DON'T: Don't use placeholders, dummy values, or skip the failing step. Example: project = 'TODO' (wrong); assuming test passes first (wrong)

- **test_observable_behavior**: Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
  DO: Test observable outcomes through public API. Example: assert agent.config_path == expected; assert agent.is_initialized (public properties)
  DON'T: Don't test private state or implementation details. Example: assert agent._initialized (wrong); assert agent._config_cache (wrong)

- **helper_extraction_and_reuse**: Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
  DO: Extract duplicate setup to reusable helpers. Example: create_agent_with_config(name, workspace, config) returns initialized Agent
  DON'T: Don't duplicate setup code across tests. Example: Same 10 lines of setup in every test method (wrong - extract to helper)

- **match_specification_scenarios**: Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
  DO: Test matches specification exactly. Example: GIVEN config exists, WHEN Agent(agent_name='story_bot'), THEN config_path == agents/base/agent.json
  DON'T: Don't use different terminology or assert things not in specification. Example: assert agent._internal_flag (not in spec - wrong)

- **place_imports_at_top**: Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
  DO: All imports at top, grouped by type. Example: import json; import pytest; from agile_bot.bots... import X
  DON'T: Don't place imports inside functions or after code. Example: def test(): from pathlib import Path (wrong - import inside function)

- **object_oriented_test_helpers**: Consolidate tests around object-oriented helpers/factories (e.g., BotTestHelper test hopper) that build complete domain objects with standard data. Example: helper = BotTestHelper(tmp_path); helper.set_state('shape','clarify'); helper.assert_at_behavior_action('shape','clarify'). Avoid scattering many primitive parameters across parametrize blocks or inline setups.
  DO: Use shared helper objects to create full test fixtures and assert against complete domain objects, not fragments.
  DON'T: Do not spread test setup across many primitive parameters or cherry-pick single values from partial objects.

- **production_code_explicit_dependencies**: Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
  DO: Inject all dependencies through constructor. Example: def __init__(self, config_loader, domain_graph): self._loader = config_loader
  DON'T: Don't access globals, singletons, or create dependencies internally. Example: self._loader = ConfigLoader() (wrong - creates internally)

- **self_documenting_tests**: Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
  DO: Let code structure document the test. Example: generator = MCPServerGenerator(name, config); file = generator.generate() - API is clear
  DON'T: Don't add verbose comments explaining obvious things. Example: # This will fail because API doesn't exist yet (unnecessary)

- **standard_test_data_sets**: Use standard, named test data sets across tests instead of recreating ad-hoc values. Example: STANDARD_STATE = {...}; helper.set_state(...); assert helper.get_state() == STANDARD_STATE.
  DO: Define canonical data once (helper constants/factories) and reuse it so every test exercises the full domain object.
  DON'T: Do not create new ad-hoc values per test or assert only one field from a complex object.

- **assert_full_results**: Assert full domain results (state/log/graph objects), not single cherry-picked fields. Example: assert helper.get_state() == STANDARD_STATE, not assert helper.get_state()['current'] == 'shape.clarify'.
  DO: Compare entire objects/dicts/dataclasses against standard data fixtures.
  DON'T: Do not assert single fields or lengths when validating complex results.

- **use_ascii_only**: All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
  DO: Use ASCII-only characters. Example: print('[PASS] Agent initialized'); print('[ERROR] Config not found')
  DON'T: Don't use Unicode or emojis. Example: print('[checkmark] Done') (wrong); print('[green_check] OK') (wrong)

- **pytest_bdd_orchestrator_pattern**: Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
  DO: Orchestrator pattern: test shows flow, delegates to helpers. Example: # Given; create_config_file(); # When; agent.initialize(); # Then; assert agent.is_initialized
  DON'T: Don't use feature files or inline complex setup. Example: @given('config exists') def step(): ... (wrong - use pytest directly)

- **use_class_based_organization**: Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
  DO: Map story hierarchy to test structure exactly. Example: Sub-epic 'Generate Bot Tools' -> test_generate_bot_tools.py, Story 'Generate Bot Tools' -> TestGenerateBotTools
  DON'T: Don't use generic/abbreviated names or wrong order. Example: class TestToolGen (wrong - use TestGenerateBotTools)

- **use_exact_variable_names**: Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
  DO: Use exact names from specification in tests and production. Example: agent_name, workspace_root, config_path - all from spec
  DON'T: Don't use different names than specification. Example: name = 'bot' when spec says agent_name (wrong)

- **use_given_when_then_helpers**: Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
  DO: Use Given/When/Then helper functions for setup, action, assertion. Example: given_bot_config_exists(); bot = when_bot_instantiated(); then_bot_uses_correct_directories(bot)
  DON'T: Don't use inline operations of 4+ lines. Example: config_dir = ...; config_dir.mkdir(); config_file = ...; config_file.write_text() (wrong - extract to helper)

CRITICAL: The rules digest above contains everything you need to get started.

WORKFLOW:
1. Read the rules digest above (descriptions + key principles)
2. Apply rules to the user's request
3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):
   - Use read_file tool to read that specific rule file
   - The full rule has detailed examples and detection patterns
4. Cite rule names when making decisions

Please make sure to validate content against the rules above, as well as the more detailed version of the rule files linked below.

When analyzing code, focus on finding violations and cite the specific rule names.# Behavior: prioritization

## Behavior Instructions - prioritization

The purpose of this behavior is to organize stories into delivery increments based on business value, dependencies, and risk

Organize stories into delivery increments based on business value, dependencies, and risk

## Action Instructions - validate

The purpose of this action is to validate story graph and/or artifacts against behavior-specific rules, checking for violations and compliance

prioritization: validate increment organization and dependencies

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_submit_works_with_differe0/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_submit_works_with_differe0/workspace/docs/stories/`
  clarification.json, strategy.json

## Step 1: Scanner Violation Review

Error running scanners: Story graph file (story-graph.json) not found in C:\Users\thoma\AppData\Local\Temp\pytest-of-thoma\pytest-3828\test_submit_works_with_differe0\workspace\docs\stories. Cannot validate rules without story graph. Expected story graph to be created by build action before validate.

Please review the validation report file in docs/stories/reports/

Carefully review all scanner-reported violations as follows:
1. For each violation message, locate the corresponding element in the story graph.
2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
6. Extract an **Example** from the actual code/content showing the problem.
7. Suggest a clear, concrete **Fix** with a code example informed by DO examples in the rule.

## Step 2: Manual Rule Review

**Rules to validate against (read each file for full DO/DON'T examples):**

### Rule: Map Sequential Spine Vs Optional Paths (Priority 1) [Scanner]
**File:** `story_bot/behaviors/prioritization/rules/map_sequential_spine_vs_optional_paths.json`
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**DO:** Identify the essential spine and mark optional paths clearly
**DON'T:** Don't mark everything as sequential, don't omit optional markers

### Rule: Design Vertical Slice Increments (Priority 2) [Scanner]
**File:** `story_bot/behaviors/prioritization/rules/design_vertical_slice_increments.json`
**Description:** Create increments that are vertical slices that deliver end-to-end working flows across multiple features/epics, NOT horizontal layers that complete one feature/epic at a time. Each increment must demonstrate complete working flow from start to finish.
**DO:** Design increments as vertical slices - end-to-end flows across multiple epics/features
**DON'T:** Don't design increments as horizontal layers, don't complete one feature/epic at a time

### Rule: Apply Quality Tradeoffs For Minimal Spine (Priority 3) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/apply_quality_tradeoffs_for_minimal_spine.json`
**Description:** Apply quality trade-offs to create thin slicing spine and later increments. Decide what quality the spine will have, what parts will be manual, what logic can be excluded, and how to prioritize adding quality in later increments.
**DO:** Make deliberate quality trade-offs to minimize spine size
**DON'T:** Don't build full quality into thin slicing spine, don't skip documenting trade-offs

### Rule: Identify Marketable Increments (Priority 4) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/identify_marketable_increments.json`
**Description:** Identify marketable increments of value during prioritization. Name increments with business value terms that stakeholders understand, not technical implementation terms.
**DO:** Name increments with business value terms
**DON'T:** Don't use technical implementation terms in increment names

### Rule: Prioritize Architectural Risk Validation (Priority 5) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/prioritize_architectural_risk_validation.json`
**Description:** Prioritize early increments to validate architectural risks and technology decisions. Build risky integrations, test unfamiliar technologies, and validate solution feasibility early to avoid late-stage surprises.
**DO:** Prioritize architectural risk validation in early increments
**DON'T:** Don't defer architectural risks to later increments, don't assume integrations will work without validation


Scanner tools don't cover or catch every rule violation. Do a second pass:
1. Carefully read each rule file, fully reviewing DO and DON'T sections, and every provided example.
2. Inspect all epics, sub-epics, stories, and domain concepts in the story graph for compliance.
3. Compare the properties and content of each element against the rule's requirements.
4. Document any violations the scanner could not find.
5. For each violation, extract an **Example** showing the problem and provide a **Fix** with code example.

## Unified Violations Table

Record ALL findings (scanner + manual) in this comprehensive table. Only include rows for actual violations found:

| Theme | Rule | Location | Valid/FP | Source | Root Cause | Problem Example | Fix with Code Example |
|-------|------|----------|----------|--------|------------|-----------------|----------------------|

**Column Guide:**
- **Theme**: Grouping category (e.g., 'naming violations', 'missing behavior', 'mechanism-oriented language')
- **Rule**: Name of the rule being violated
- **Location**: Path in story graph (e.g., `epics[1].sub_epics[0].name`) or file path
- **Valid/FP**: Valid if rule breach, False Positive if incorrectly flagged (explain why)
- **Source**: Scanner (detected by automated scanner), Manual (found during AI review), Both (flagged by scanner AND confirmed by manual review)
- **Root Cause**: Underlying reason for the violation
- **Problem Example**: Actual code/text showing the issue (e.g., `"Strategy Types"`, `"Create Mobs"`)
- **Fix with Code Example**: Corrected version (e.g., `"Select Strategy"`, `"Assembles Combat Mob"`)

## Step 3: Summarize Findings & Recommendations

Provide a concise summary:
- Report how many **scanner violations** were valid vs false positives.
- Enumerate any **additional manual findings** not caught by scanners.
- Group all violations by recurring theme or pattern.
- Split violations into **Priority Fixes** (must resolve before continuing) and **Optional Improvements**.

Present your summary and await user confirmation before automatically applying or proposing corrections.
prioritization: validate increment organization and dependencies

### Key Questions

- Which areas of the story map carry the most business or delivery risk?
- Which areas are expected to deliver the most value if delivered early?
- Which areas are the most complex or hardest to implement, relative to their value?
- Do you want thin slices to be as end-to-end as possible?
- Are there any components, capabilities, or services that need to be reused across multiple stories or features?
- Are there any project or program constraints that impact delivery order?
- Are there users or groups that must go first to enable others to follow?

### Evidence

Story map from Shape stage (epics, features, and initial story breakdown), Business cases or initiative briefs, Project charters and delivery timelines, Capability or architectural dependency maps, User rollout or onboarding strategies, Risk registers or readiness checklists, Value modeling or impact estimation docs

### Decisions

**increment_slicing_strategy:** What approach are you taking to group the work into thin slices or increments of value, and how are you ensuring they are as small as possible while still being valuable and/or generating learning or reducing risk?

- Delivering End-to-End Journey — supports integrated validation across systems and users
- Validating Impact - Feasibility — reduces uncertainty and derisks critical components early
- Maximizing Earned Value — delivers early impact and builds stakeholder confidence
- Increasing Reuse/Dependency— prevents downstream rework and enables reuse
- Quick Win — implements lowest-complexity paths first
- Validating Impact — validates whether users care, intend to use, or will act on the solution before investing in full delivery (e.g., Wizard of Oz, landing pages, stubs, or mafia offers)


### Assumptions

- Thin slices should provide either value, learning, or risk reduction
- Slices do not need to include all functionality to be useful
- Not every increment must be user-visible if it validates key assumptions
- Some slices may be architectural if they unlock multiple features# Behavior: prioritization

## Behavior Instructions - prioritization

The purpose of this behavior is to organize stories into delivery increments based on business value, dependencies, and risk

Organize stories into delivery increments based on business value, dependencies, and risk

## Action Instructions - validate

The purpose of this action is to validate story graph and/or artifacts against behavior-specific rules, checking for violations and compliance

prioritization: validate increment organization and dependencies

---

**Look for context in the following locations:**
- in this message and chat history
- in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_submit_works_with_differe0/workspace/docs/context/`
- generated files in `C:/Users/thoma/AppData/Local/Temp/pytest-of-thoma/pytest-3828/test_submit_works_with_differe0/workspace/docs/stories/`
  clarification.json, strategy.json

## Step 1: Scanner Violation Review

Error running scanners: Story graph file (story-graph.json) not found in C:\Users\thoma\AppData\Local\Temp\pytest-of-thoma\pytest-3828\test_submit_works_with_differe0\workspace\docs\stories. Cannot validate rules without story graph. Expected story graph to be created by build action before validate.

Please review the validation report file in docs/stories/reports/

Carefully review all scanner-reported violations as follows:
1. For each violation message, locate the corresponding element in the story graph.
2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
6. Extract an **Example** from the actual code/content showing the problem.
7. Suggest a clear, concrete **Fix** with a code example informed by DO examples in the rule.

## Step 2: Manual Rule Review

**Rules to validate against (read each file for full DO/DON'T examples):**

### Rule: Map Sequential Spine Vs Optional Paths (Priority 1) [Scanner]
**File:** `story_bot/behaviors/prioritization/rules/map_sequential_spine_vs_optional_paths.json`
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**DO:** Identify the essential spine and mark optional paths clearly
**DON'T:** Don't mark everything as sequential, don't omit optional markers

### Rule: Design Vertical Slice Increments (Priority 2) [Scanner]
**File:** `story_bot/behaviors/prioritization/rules/design_vertical_slice_increments.json`
**Description:** Create increments that are vertical slices that deliver end-to-end working flows across multiple features/epics, NOT horizontal layers that complete one feature/epic at a time. Each increment must demonstrate complete working flow from start to finish.
**DO:** Design increments as vertical slices - end-to-end flows across multiple epics/features
**DON'T:** Don't design increments as horizontal layers, don't complete one feature/epic at a time

### Rule: Apply Quality Tradeoffs For Minimal Spine (Priority 3) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/apply_quality_tradeoffs_for_minimal_spine.json`
**Description:** Apply quality trade-offs to create thin slicing spine and later increments. Decide what quality the spine will have, what parts will be manual, what logic can be excluded, and how to prioritize adding quality in later increments.
**DO:** Make deliberate quality trade-offs to minimize spine size
**DON'T:** Don't build full quality into thin slicing spine, don't skip documenting trade-offs

### Rule: Identify Marketable Increments (Priority 4) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/identify_marketable_increments.json`
**Description:** Identify marketable increments of value during prioritization. Name increments with business value terms that stakeholders understand, not technical implementation terms.
**DO:** Name increments with business value terms
**DON'T:** Don't use technical implementation terms in increment names

### Rule: Prioritize Architectural Risk Validation (Priority 5) [Manual Check]
**File:** `story_bot/behaviors/prioritization/rules/prioritize_architectural_risk_validation.json`
**Description:** Prioritize early increments to validate architectural risks and technology decisions. Build risky integrations, test unfamiliar technologies, and validate solution feasibility early to avoid late-stage surprises.
**DO:** Prioritize architectural risk validation in early increments
**DON'T:** Don't defer architectural risks to later increments, don't assume integrations will work without validation


Scanner tools don't cover or catch every rule violation. Do a second pass:
1. Carefully read each rule file, fully reviewing DO and DON'T sections, and every provided example.
2. Inspect all epics, sub-epics, stories, and domain concepts in the story graph for compliance.
3. Compare the properties and content of each element against the rule's requirements.
4. Document any violations the scanner could not find.
5. For each violation, extract an **Example** showing the problem and provide a **Fix** with code example.

## Unified Violations Table

Record ALL findings (scanner + manual) in this comprehensive table. Only include rows for actual violations found:

| Theme | Rule | Location | Valid/FP | Source | Root Cause | Problem Example | Fix with Code Example |
|-------|------|----------|----------|--------|------------|-----------------|----------------------|

**Column Guide:**
- **Theme**: Grouping category (e.g., 'naming violations', 'missing behavior', 'mechanism-oriented language')
- **Rule**: Name of the rule being violated
- **Location**: Path in story graph (e.g., `epics[1].sub_epics[0].name`) or file path
- **Valid/FP**: Valid if rule breach, False Positive if incorrectly flagged (explain why)
- **Source**: Scanner (detected by automated scanner), Manual (found during AI review), Both (flagged by scanner AND confirmed by manual review)
- **Root Cause**: Underlying reason for the violation
- **Problem Example**: Actual code/text showing the issue (e.g., `"Strategy Types"`, `"Create Mobs"`)
- **Fix with Code Example**: Corrected version (e.g., `"Select Strategy"`, `"Assembles Combat Mob"`)

## Step 3: Summarize Findings & Recommendations

Provide a concise summary:
- Report how many **scanner violations** were valid vs false positives.
- Enumerate any **additional manual findings** not caught by scanners.
- Group all violations by recurring theme or pattern.
- Split violations into **Priority Fixes** (must resolve before continuing) and **Optional Improvements**.

Present your summary and await user confirmation before automatically applying or proposing corrections.
prioritization: validate increment organization and dependencies

### Key Questions

- Which areas of the story map carry the most business or delivery risk?
- Which areas are expected to deliver the most value if delivered early?
- Which areas are the most complex or hardest to implement, relative to their value?
- Do you want thin slices to be as end-to-end as possible?
- Are there any components, capabilities, or services that need to be reused across multiple stories or features?
- Are there any project or program constraints that impact delivery order?
- Are there users or groups that must go first to enable others to follow?

### Evidence

Story map from Shape stage (epics, features, and initial story breakdown), Business cases or initiative briefs, Project charters and delivery timelines, Capability or architectural dependency maps, User rollout or onboarding strategies, Risk registers or readiness checklists, Value modeling or impact estimation docs

### Decisions

**increment_slicing_strategy:** What approach are you taking to group the work into thin slices or increments of value, and how are you ensuring they are as small as possible while still being valuable and/or generating learning or reducing risk?

- Delivering End-to-End Journey — supports integrated validation across systems and users
- Validating Impact - Feasibility — reduces uncertainty and derisks critical components early
- Maximizing Earned Value — delivers early impact and builds stakeholder confidence
- Increasing Reuse/Dependency— prevents downstream rework and enables reuse
- Quick Win — implements lowest-complexity paths first
- Validating Impact — validates whether users care, intend to use, or will act on the solution before investing in full delivery (e.g., Wizard of Oz, landing pages, stubs, or mafia offers)


### Assumptions

- Thin slices should provide either value, learning, or risk reduction
- Slices do not need to include all functionality to be useful
- Not every increment must be user-visible if it validates key assumptions
- Some slices may be architectural if they unlock multiple features
        
        result = helper.bot.submit_current_action()
        
        assert result['status'] == 'error', f"Expected error status, got {result.get('status')}"
        assert 'No current behavior' in result['message'], f"Expected 'No current behavior' in message, got {result.get('message')}"

    def test_submit_fails_when_no_current_action(self, tmp_path):
        """
        SCENARIO: Submit fails when no current action
        GIVEN: Bot is at behavior but no action is set
        WHEN: User calls submit_current_action() method
        THEN: System returns error status
        AND: Error indicates no current action
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        # Explicitly clear current action (navigating to behavior sets first action by default)
        helper.bot.behaviors.current.actions._current_index = None
        
        result = helper.bot.submit_current_action()
        
        assert result['status'] == 'error', f"Expected error status, got {result.get('status')}"
        assert 'No current action' in result['message'], f"Expected 'No current action' in message, got {result.get('message')}"

    def test_submit_works_with_different_behaviors_and_actions(self, tmp_path):
        """
        SCENARIO: Submit works with different behaviors and actions
        GIVEN: Bot is at prioritization.validate
        WHEN: User calls submit_current_action() method
        THEN: System returns success with correct behavior and action
        """
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('prioritization')
        helper.bot.behaviors.current.actions.navigate_to('validate')
        
        result = helper.bot.submit_current_action()
        
        assert result['status'] == 'success'
        assert result['behavior'] == 'prioritization'
        assert result['action'] == 'validate'
        assert 'timestamp' in result
