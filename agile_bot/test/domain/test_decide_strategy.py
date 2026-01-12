
"""
Decide Strategy Criteria Action Tests

Tests for all stories in the 'Decide Strategy Criteria Action' sub-epic:
- Inject Strategy Criteria Into Instructions
- Save Final Assumptions and Decisions
"""
import pytest
from agile_bot.src.actions.action_context import StrategyActionContext
from agile_bot.test.domain.bot_test_helper import BotTestHelper


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
