
"""
Decide Strategy Criteria Action Tests

Tests for all stories in the 'Decide Strategy Criteria Action' sub-epic:
- Inject Strategy Criteria Into Instructions
- Save Final Assumptions and Decisions
"""
import pytest
from pathlib import Path
from agile_bot.src.actions.strategy.strategy_action import StrategyAction
from agile_bot.test.domain.bot_test_helper import BotTestHelper


# ============================================================================
# STORY: Inject Strategy Criteria Into Instructions
# ============================================================================

class TestInjectStrategyIntoInstructions:
    """Story: Inject Strategy Into Instructions - Tests strategy injection."""

    def test_action_injects_decision_criteria_and_assumptions(self, tmp_path):
        """
        SCENARIO: Action Injects Decision Criteria And Assumptions
        """
        # Given: BotTestHelper provides production story_bot and workspace
        helper = BotTestHelper(tmp_path)
        behavior = 'shape'
        helper.create_minimal_guardrails_files(behavior)
        helper.bot.behaviors.navigate_to(behavior)
        action_obj = StrategyAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        # When: Action injects strategy criteria and assumptions
        instructions = helper.when_action_injects(action_obj, content='strategy_criteria_and_assumptions')
        
        # Then: Instructions contain all required strategy fields
        helper.assert_strategy_instructions(instructions)


# ============================================================================
# STORY: Store Planning Data
# ============================================================================

class TestStoreStrategyData:
    """Story: Store Strategy Data - Tests that strategy data is saved to strategy.json."""

    def test_save_strategy_data_when_parameters_provided(self, tmp_path):
        """
        SCENARIO: Save strategy data when parameters are provided
        GIVEN: strategy action is initialized
        AND: parameters contain decisions_made and assumptions_made
        WHEN: do_execute is called with these parameters
        THEN: strategy.json file is created in docs/stories/ folder
        AND: file contains behavior section with decisions_made and assumptions_made
        """
        # Given: BotTestHelper provides production story_bot and workspace
        helper = BotTestHelper(tmp_path)
        behavior = 'shape'
        helper.create_minimal_guardrails_files(behavior)
        helper.bot.behaviors.navigate_to(behavior)
        action = StrategyAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        # Create parameters with decisions and assumptions
        parameters = given_strategy_parameters(
            decisions_made={
                'drill_down': 'Dig deep on system interactions',
                'flow_scope': 'End-to-end user-system behavior'
            },
            assumptions_made=[
                'Focus on user flow over internal systems',
                'Cover the end-to-end scenario'
            ],
            behavior=behavior
        )
        
        # When: Action executes with parameters
        when_action_executes_with_strategy(action, parameters)
        
        # Then: strategy.json file exists
        strategy_file = then_strategy_file_exists(helper.workspace)
        
        # And: File contains behavior section with decisions_made and assumptions_made
        then_strategy_file_contains(
            strategy_file,
            behavior,
            expected_decisions_made={'drill_down': 'Dig deep on system interactions'},
            expected_assumptions_made=parameters['assumptions_made']
        )

    def test_preserve_existing_strategy_data_when_saving(self, tmp_path):
        """
        SCENARIO: Preserve existing strategy data when saving
        GIVEN: strategy.json already exists with data for 'discovery' behavior
        AND: strategy action is initialized for 'shape' behavior
        WHEN: do_execute is called with parameters
        THEN: strategy.json contains both 'discovery' and 'shape' sections
        AND: existing 'discovery' data is preserved
        """
        # Given: BotTestHelper provides production story_bot and workspace
        helper = BotTestHelper(tmp_path)
        
        # Create existing strategy.json with discovery data
        strategy_file = given_strategy_json_file(
            helper.workspace,
            'discovery',
            decisions_made={'scope': 'Component level'},
            assumptions_made=['Stories follow user story format']
        )
        
        # Setup shape behavior
        behavior = 'shape'
        helper.create_minimal_guardrails_files(behavior)
        helper.bot.behaviors.navigate_to(behavior)
        action = StrategyAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        # Create parameters for shape behavior
        parameters = given_strategy_parameters(behavior=behavior)
        
        # When: Action executes with parameters
        when_action_executes_with_strategy(action, parameters)
        
        # Then: Both behaviors' data are preserved
        strategy_data = then_strategy_file_preserves_existing_behaviors(strategy_file, ['discovery', 'shape'])
        assert strategy_data['discovery']['strategy_criteria']['decisions_made']['scope'] == 'Component level'
        assert strategy_data['shape']['strategy_criteria']['decisions_made']['drill_down'] == 'Dig deep on user workflows'

    def test_skip_saving_when_no_strategy_parameters_provided(self, tmp_path):
        """
        SCENARIO: Skip saving when no strategy parameters are provided
        GIVEN: strategy action is initialized
        AND: parameters do not contain decisions_made or assumptions_made
        WHEN: do_execute is called with empty or unrelated parameters
        THEN: strategy.json file is not created
        """
        # Given: BotTestHelper provides production story_bot and workspace
        helper = BotTestHelper(tmp_path)
        behavior = 'shape'
        helper.create_minimal_guardrails_files(behavior)
        helper.bot.behaviors.navigate_to(behavior)
        action = StrategyAction(behavior=helper.bot.behaviors.current, action_config=None)
        
        # Create empty parameters (no decisions or assumptions)
        parameters = {}
        
        # When: Action executes with empty parameters
        when_action_executes_with_strategy(action, parameters)
        
        # Then: strategy.json file is not created
        strategy_file = helper.workspace / 'docs' / 'stories' / 'strategy.json'
        assert not strategy_file.exists(), f"strategy.json should not be created at {strategy_file} when no strategy data provided"


# ============================================================================
# STRATEGY HELPERS - Specific to strategy action tests
# ============================================================================

def given_strategy_parameters(decisions_made=None, assumptions_made=None, behavior='shape'):
    """Given: Strategy parameters with decisions and assumptions.
    
    Args:
        decisions_made: Dict of decisions made (default: {'drill_down': 'Dig deep on system interactions', 'flow_scope': 'End-to-end user-system behavior'})
        assumptions_made: List of assumptions made (default: ['Focus on user flow over internal systems', 'Cover the end-to-end scenario'])
        behavior: Behavior name (default: 'shape')
    
    Returns:
        Dict with 'decisions_made' and 'assumptions_made' keys
    """
    if decisions_made is None:
        if behavior == 'shape':
            decisions_made = {
                'drill_down': 'Dig deep on system interactions',
                'flow_scope': 'End-to-end user-system behavior'
            }
        elif behavior == 'discovery':
            decisions_made = {'scope': 'Component level'}
        else:
            decisions_made = {}
    
    if assumptions_made is None:
        if behavior == 'shape':
            assumptions_made = [
                'Focus on user flow over internal systems',
                'Cover the end-to-end scenario'
            ]
        elif behavior == 'discovery':
            assumptions_made = ['Stories follow user story format']
        else:
            assumptions_made = []
    
    return {
        'decisions_made': decisions_made,
        'assumptions_made': assumptions_made
    }


def given_strategy_json_file(workspace_directory: Path, behavior: str, decisions_made: dict = None, assumptions_made: list = None):
    """Given: strategy.json file exists with data for behavior.
    
    Args:
        workspace_directory: Workspace directory path
        behavior: Behavior name
        decisions_made: Dict of decisions made (default: empty dict)
        assumptions_made: List of assumptions made (default: empty list)
    
    Returns:
        Path to strategy.json file
    """
    import json
    
    stories_folder = workspace_directory / 'docs' / 'stories'
    stories_folder.mkdir(parents=True, exist_ok=True)
    strategy_file = stories_folder / 'strategy.json'
    
    if decisions_made is None:
        decisions_made = {}
    if assumptions_made is None:
        assumptions_made = []
    
    existing_data = {
        behavior: {
            'strategy_criteria': {
                'criteria': {},
                'decisions_made': decisions_made
            },
            'assumptions': {
                'typical_assumptions': [],
                'assumptions_made': assumptions_made
            }
        }
    }
    strategy_file.write_text(json.dumps(existing_data, indent=2), encoding='utf-8')
    return strategy_file


def when_action_executes_with_strategy(action, parameters: dict):
    """When: Action executes with strategy parameters.
    
    Args:
        action: StrategyAction instance
        parameters: Dict with 'decisions_made' and 'assumptions_made' keys
    
    Returns:
        Result from action.do_execute()
    """
    from agile_bot.src.actions.action_context import StrategyActionContext
    
    context = StrategyActionContext(
        decisions_made=parameters.get('decisions_made'),
        assumptions_made=parameters.get('assumptions_made')
    )
    return action.do_execute(context)


def then_strategy_file_exists(workspace_directory: Path):
    """Then: strategy.json file exists.
    
    Args:
        workspace_directory: Workspace directory path
    
    Returns:
        Path to strategy.json file
    """
    strategy_file = workspace_directory / 'docs' / 'stories' / 'strategy.json'
    assert strategy_file.exists(), f"strategy.json should be created at {strategy_file}"
    return strategy_file


def then_strategy_file_contains(strategy_file: Path, behavior: str, expected_decisions_made: dict = None, expected_assumptions_made: list = None):
    """Then: strategy.json contains behavior data.
    
    Args:
        strategy_file: Path to strategy.json file
        behavior: Behavior name to check
        expected_decisions_made: Expected decisions_made dict
        expected_assumptions_made: Expected assumptions_made list
    
    Returns:
        Full strategy data dict
    """
    import json
    
    strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
    assert behavior in strategy_data
    
    if expected_decisions_made:
        assert 'strategy_criteria' in strategy_data[behavior]
        assert 'decisions_made' in strategy_data[behavior]['strategy_criteria']
        for key, value in expected_decisions_made.items():
            assert strategy_data[behavior]['strategy_criteria']['decisions_made'][key] == value
    
    if expected_assumptions_made:
        assert 'assumptions' in strategy_data[behavior]
        assert 'assumptions_made' in strategy_data[behavior]['assumptions']
        assert strategy_data[behavior]['assumptions']['assumptions_made'] == expected_assumptions_made
    
    return strategy_data


def then_strategy_file_preserves_existing_behaviors(strategy_file: Path, existing_behaviors: list):
    """Then: strategy.json preserves existing behavior data.
    
    Args:
        strategy_file: Path to strategy.json file
        existing_behaviors: List of behavior names that should be preserved
    
    Returns:
        Full strategy data dict
    """
    import json
    
    strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
    for behavior in existing_behaviors:
        assert behavior in strategy_data, f"Existing {behavior} data should be preserved"
    return strategy_data
