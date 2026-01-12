
"""
Decide Strategy Criteria Action Tests

Tests for all stories in the 'Decide Strategy Criteria Action' sub-epic:
- Inject Strategy Criteria Into Instructions
- Save Final Assumptions and Decisions
"""
import pytest
from pathlib import Path
import json
from agile_bot.src.actions.action_context import StrategyActionContext
from agile_bot.test.domain.bot_test_helper import BotTestHelper


# ============================================================================
# STORY: Inject Strategy Criteria Into Instructions
# ============================================================================

class TestInjectStrategyIntoInstructions:
    """Story: Inject Strategy Into Instructions - Tests strategy injection."""

    def test_action_injects_decision_criteria_and_assumptions(self, tmp_path):
        """
        SCENARIO: Action Injects Decision Criteria And Assumptions
        GIVEN: Production story_bot with shape behavior (has guardrails)
        WHEN: Action injects strategy criteria and assumptions
        THEN: Instructions contain all required strategy fields
        """
        # Given: Production story_bot with shape behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('strategy')
        
        # When: Action injects strategy criteria and assumptions
        instructions = helper.behaviors.when_action_injects(action_obj, content='strategy_criteria_and_assumptions')
        
        # Then: Instructions contain all required strategy fields
        helper.strategy.assert_strategy_instructions(instructions)


# ============================================================================
# STORY: Store Planning Data
# ============================================================================

class TestStoreStrategyData:
    """Story: Store Strategy Data - Tests that strategy data is saved to strategy.json."""

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
        strategy_file = helper.workspace / 'docs' / 'stories' / 'strategy.json'
        assert strategy_file.exists(), f"strategy.json should be created at {strategy_file}"
        
        strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
        assert 'shape' in strategy_data
        assert strategy_data['shape']['strategy_criteria']['decisions_made']['drill_down'] == 'Dig deep on system interactions'
        assert strategy_data['shape']['assumptions']['assumptions_made'] == assumptions_made

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
        stories_folder = helper.workspace / 'docs' / 'stories'
        stories_folder.mkdir(parents=True, exist_ok=True)
        strategy_file = stories_folder / 'strategy.json'
        
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
        strategy_file.write_text(json.dumps(existing_data, indent=2), encoding='utf-8')
        
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
        strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
        assert 'discovery' in strategy_data
        assert 'shape' in strategy_data
        assert strategy_data['discovery']['strategy_criteria']['decisions_made']['scope'] == 'Component level'
        assert strategy_data['shape']['strategy_criteria']['decisions_made']['drill_down'] == 'Dig deep on system interactions'

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
        strategy_file = helper.workspace / 'docs' / 'stories' / 'strategy.json'
        assert not strategy_file.exists(), f"strategy.json should not be created at {strategy_file} when no strategy data provided"
