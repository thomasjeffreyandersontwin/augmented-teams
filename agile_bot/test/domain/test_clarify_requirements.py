"""
Gather Context Tests

Tests for all stories in the 'Gather Context' sub-epic:
- Track Activity for Gather Context Action
- Proceed To Decide Planning
"""
import pytest
from agile_bot.src.actions.action_context import ClarifyActionContext
from agile_bot.test.domain.bot_test_helper import BotTestHelper


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
