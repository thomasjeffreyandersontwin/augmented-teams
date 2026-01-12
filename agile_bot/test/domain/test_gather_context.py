"""
Gather Context Tests

Tests for all stories in the 'Gather Context' sub-epic:
- Track Activity for Gather Context Action
- Proceed To Decide Planning
"""
import pytest
import os
from pathlib import Path
import json
from agile_bot.src.actions.clarify.clarify_action import ClarifyContextAction
from agile_bot.src.actions.strategy.strategy_action import StrategyAction
from agile_bot.src.behaviors.behavior import Behavior
from agile_bot.src.bot_path import BotPath
# NOTE: These functions are not used in this test file
# from agile_bot.bots.base_bot.test.test_execute_behavior_actions import (
#     verify_workflow_transition,
#     verify_workflow_saves_completed_action,
#     then_workflow_current_state_matches
# )
from agile_bot.test.domain.bot_test_helper import BotTestHelper




def given_environment_bootstrapped_with_guardrails(helper: BotTestHelper):
    """Given: Environment bootstrapped with guardrails."""
    bot_name = 'story_bot'
    behavior = 'shape'
    
    helper.create_behavior_json(behavior, actions=[{'name': 'clarify', 'order': 1}])
    helper.create_minimal_guardrails_files(behavior)
    
    questions = ['What is the scope?', 'Who are the users?']
    evidence = ['Requirements doc', 'User interviews']
    helper.create_guardrails_files(behavior, questions, evidence)
    return bot_name, behavior, questions, evidence




def given_environment_bootstrapped_with_malformed_guardrails(helper: BotTestHelper):
    """Given: Environment bootstrapped with malformed guardrails."""
    bot_name = 'story_bot'
    behavior = 'shape'
    
    helper.create_behavior_json(behavior, actions=[{"name": "clarify", "order": 1, "next_action": "strategy"}])
    helper.create_minimal_guardrails_files(behavior)
    helper.create_malformed_guardrails_file(behavior)
    
    from agile_bot.src.bot_path import BotPath
    from agile_bot.src.behaviors.behavior import Behavior
    bot_paths = BotPath(bot_directory=helper.bot_directory)
    behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
    action_obj = ClarifyContextAction(behavior=behavior_obj, action_config=None)
    return bot_name, behavior, action_obj


def given_environment_action_and_parameters_for_clarification(workspace_directory: Path, helper: BotTestHelper = None):
    """Given: Environment, action and parameters for clarification."""
    # Use BotTestHelper with production story_bot (no behavior.json creation needed)
    from pathlib import Path as P
    if helper is None:
        tmp_path = workspace_directory.parent if workspace_directory.name == 'workspace' else workspace_directory.parent
        helper = BotTestHelper(tmp_path)
    
    os.environ['BOT_DIRECTORY'] = str(helper.bot_directory)
    os.environ['WORKING_AREA'] = str(workspace_directory)
    
    helper.bot.behaviors.navigate_to('shape')
    behavior_obj = helper.bot.behaviors.current
    from agile_bot.src.actions.clarify.clarify_action import ClarifyContextAction
    action = ClarifyContextAction(behavior=behavior_obj, action_config=None)
    
    parameters = given_clarification_parameters(
        key_questions_answered={'user_types': 'Game Masters', 'first_action': 'Group tokens into mobs'},
        evidence_provided={'original_input': 'I want to turn minions into mobs', 'source_file': 'input.txt'},
        behavior='shape'
    )
    bot_paths = BotPath(workspace_path=workspace_directory, bot_directory=helper.bot_directory)
    return action, parameters, bot_paths


def given_environment_with_existing_clarification_and_action(helper: BotTestHelper):
    """Given: Environment with existing clarification and action."""
    os.environ['BOT_DIRECTORY'] = str(helper.bot_directory)
    os.environ['WORKING_AREA'] = str(helper.workspace)
    bot_paths = BotPath(workspace_path=helper.workspace, bot_directory=helper.bot_directory)
    clarification_file = given_clarification_json_file(
        helper.workspace, 'discovery',
        key_questions={'scope': 'Component level'},
        evidence={'doc': 'requirements.md'},
        bot_paths=bot_paths
    )
    
    helper.bot.behaviors.navigate_to('shape')
    behavior_obj = helper.bot.behaviors.current
    from agile_bot.src.actions.clarify.clarify_action import ClarifyContextAction
    action = ClarifyContextAction(behavior=behavior_obj, action_config=None)
    
    parameters = given_clarification_parameters(behavior='shape')
    return clarification_file, action, parameters, bot_paths


def given_environment_action_and_empty_parameters(helper: BotTestHelper):
    """Given: Environment, action and empty parameters."""
    os.environ['BOT_DIRECTORY'] = str(helper.bot_directory)
    os.environ['WORKING_AREA'] = str(helper.workspace)
    
    helper.bot.behaviors.navigate_to('shape')
    behavior_obj = helper.bot.behaviors.current
    from agile_bot.src.actions.clarify.clarify_action import ClarifyContextAction
    action = ClarifyContextAction(behavior=behavior_obj, action_config=None)
    
    parameters = {'other_data': 'some value'}
    bot_paths = BotPath(bot_directory=helper.bot_directory)
    return action, parameters, bot_paths





def then_clarification_file_does_not_exist(workspace_directory: Path, bot_paths: BotPath = None):
    """Then step: clarification.json file does not exist."""
    if bot_paths is None:
        clarification_file = workspace_directory / 'docs' / 'stories' / 'clarification.json'
    else:
        documentation_path = bot_paths.documentation_path
        clarification_file = workspace_directory / documentation_path / 'clarification.json'
    assert not clarification_file.exists(), f"clarification.json should not be created at {clarification_file} when no clarification data provided"


class TestInjectGuardrailsAsPartOfClarifyRequirements:
    """Story: Inject Guardrails as Part of Clarify Requirements - Tests guardrail injection."""

    def test_action_injects_questions_and_evidence(self, tmp_path):
        helper = BotTestHelper(tmp_path, bot_directory=tmp_path / 'bot')
        bot_name, behavior, questions, evidence = given_environment_bootstrapped_with_guardrails(helper)
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
        action_obj = ClarifyContextAction(behavior=behavior_obj, action_config=None)
        instructions = helper.when_action_injects(action_obj, content='questions_and_evidence')
        
        # Verify all ClarifyContextAction fields are present
        helper.assert_clarify_context_instructions(instructions)
        
        # Verify specific guardrails content matches expectations
        helper.then_instructions_contain(instructions, 'guardrails', expected_questions=questions, expected_evidence=evidence)

class TestStoreClarificationData:
    """Story: Store Clarification Data - Tests that clarification data is saved to clarification.json."""

    def test_save_clarification_data_when_parameters_provided(self, tmp_path):
        helper = BotTestHelper(tmp_path)
        """
        SCENARIO: Save clarification data when parameters are provided
        GIVEN: clarify action is initialized
        AND: parameters contain key_questions_answered and evidence_provided
        WHEN: do_execute is called with these parameters
        THEN: clarification.json file is created in docs/stories/ folder
        AND: file contains behavior section with key_questions and evidence
        """
        action, parameters, bot_paths = given_environment_action_and_parameters_for_clarification(helper.workspace, helper)
        
        when_action_executes_with_clarification(action, parameters)
        
        clarification_file = then_clarification_file_exists(helper.workspace, bot_paths)
        then_clarification_file_contains(
            clarification_file,
            'shape',
            expected_key_questions={'user_types': 'Game Masters'},
            expected_evidence={'original_input': 'I want to turn minions into mobs'}
        )

    def test_preserve_existing_clarification_data_when_saving(self, tmp_path):
        helper = BotTestHelper(tmp_path)
        """
        SCENARIO: Preserve existing clarification data when saving
        GIVEN: clarification.json already exists with data for 'discovery' behavior
        AND: clarify action is initialized for 'shape' behavior
        WHEN: do_execute is called with parameters
        THEN: clarification.json contains both 'discovery' and 'shape' sections
        AND: existing 'discovery' data is preserved
        """
        clarification_file, action, parameters, bot_paths = given_environment_with_existing_clarification_and_action(helper)
        
        when_action_executes_with_clarification(action, parameters)
        
        then_clarification_file_contains(clarification_file, 'discovery')
        then_clarification_file_contains(clarification_file, 'shape')
        clarification_data = json.loads(clarification_file.read_text(encoding='utf-8'))
        assert clarification_data['discovery']['key_questions']['answers']['scope'] == 'Component level'
        assert clarification_data['shape']['key_questions']['answers']['user_types'] == 'Game Masters'

    def test_skip_saving_when_no_clarification_parameters_provided(self, tmp_path):
        helper = BotTestHelper(tmp_path)
        """
        SCENARIO: Skip saving when no clarification parameters are provided
        GIVEN: clarify action is initialized
        AND: parameters do not contain key_questions_answered or evidence_provided
        WHEN: do_execute is called with empty or unrelated parameters
        THEN: clarification.json file is not created
        """
        action, parameters, bot_paths = given_environment_action_and_empty_parameters(helper)
        
        when_action_executes_with_clarification(action, parameters)
        
        then_clarification_file_does_not_exist(helper.workspace, bot_paths)


from agile_bot.src.actions.actions import Actions
from agile_bot.src.actions.action import Action
# NOTE: Guardrails not used in this test file
# from agile_bot.src.actions.guardrails import Guardrails




def given_environment_bootstrapped(helper: BotTestHelper):
    """Given: Environment bootstrapped."""
    # Helper already has bot_directory and workspace set up
    pass

class TestLoadGuardrails:
    """Story: Load Guardrails (Sub-epic: Gather Context)"""
    
    def test_guardrails_loads_required_context_guardrails(self, tmp_path):
        helper = BotTestHelper(tmp_path)
        """
        SCENARIO: Guardrails loads required context guardrails
        GIVEN: BehaviorConfig with guardrails directory
        WHEN: Guardrails instantiated with behavior_config
        THEN: Required context guardrails loaded
        """
        # Given: BehaviorConfig with guardrails directory
        given_environment_bootstrapped(helper)
        bot_name = 'story_bot'
        behavior_name = 'shape'
        helper.create_behavior_json(behavior_name, baseActionsPath="agile_bot/base_actions", 
                                   instructions=[f"Test instructions for {behavior_name}."])
        helper.create_minimal_guardrails_files(behavior_name)
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        
        # When: Guardrails instantiated
        guardrails = behavior.guardrails
        
        # Then: Required context guardrails loaded
        assert hasattr(guardrails, 'required_context')
        assert hasattr(guardrails, 'strategy')
        assert guardrails.required_context is not None
    
    def test_guardrails_loads_strategy_guardrails(self, tmp_path):
        helper = BotTestHelper(tmp_path)
        """
        SCENARIO: Guardrails loads strategy guardrails
        GIVEN: BehaviorConfig with strategy guardrails directory
        WHEN: Guardrails instantiated
        THEN: Strategy guardrails loaded
        """
        # Given: BehaviorConfig with strategy guardrails directory
        given_environment_bootstrapped(helper)
        bot_name = 'story_bot'
        behavior_name = 'shape'
        helper.create_behavior_json(behavior_name, baseActionsPath="agile_bot/base_actions", 
                                   instructions=[f"Test instructions for {behavior_name}."])
        helper.create_minimal_guardrails_files(behavior_name)
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        
        # When: Guardrails instantiated
        guardrails = behavior.guardrails
        
        # Then: Strategy guardrails loaded
        assert hasattr(guardrails, 'required_context')
        assert hasattr(guardrails, 'strategy')
        assert guardrails.strategy is not None
    
    def test_guardrails_properties_return_guardrails_objects(self, tmp_path):
        helper = BotTestHelper(tmp_path)
        """
        SCENARIO: Guardrails properties return guardrails objects
        GIVEN: Guardrails with loaded guardrails
        WHEN: Properties accessed (required_context, strategy)
        THEN: Returns RequiredContext object and Strategy object
        """
        # Given: Guardrails with loaded guardrails
        given_environment_bootstrapped(helper)
        bot_name = 'story_bot'
        behavior_name = 'shape'
        helper.create_behavior_json(behavior_name, baseActionsPath="agile_bot/base_actions", 
                                   instructions=[f"Test instructions for {behavior_name}."])
        helper.create_minimal_guardrails_files(behavior_name)
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        guardrails = behavior.guardrails
        
        # When: Properties accessed
        required_context = guardrails.required_context
        strategy = guardrails.strategy
        
        # Then: Returns guardrails objects
        assert required_context is not None
        assert strategy is not None
        
        # Then: Creates empty/default guardrails objects (doesn't raise error)
        assert hasattr(guardrails, 'required_context')
        assert hasattr(guardrails, 'strategy')


# ============================================================================
# CLARIFICATION HELPERS - Specific to gather context tests
# ============================================================================

def given_clarification_parameters(key_questions_answered=None, evidence_provided=None, behavior='shape'):
    """Given: Clarification parameters with questions and evidence.
    
    Args:
        key_questions_answered: Dict of answered questions (default: {'user_types': 'Game Masters'})
        evidence_provided: Dict of provided evidence (default: {'original_input': 'I want to turn minions into mobs'})
        behavior: Behavior name (default: 'shape')
    
    Returns:
        Dict with 'key_questions_answered' and 'evidence_provided' keys
    """
    if key_questions_answered is None:
        if behavior == 'shape':
            key_questions_answered = {'user_types': 'Game Masters'}
        elif behavior == 'discovery':
            key_questions_answered = {'scope': 'Component level'}
        else:
            key_questions_answered = {}
    
    if evidence_provided is None:
        if behavior == 'shape':
            evidence_provided = {'original_input': 'I want to turn minions into mobs', 'source_file': 'input.txt'}
        elif behavior == 'discovery':
            evidence_provided = {'doc': 'requirements.md'}
        else:
            evidence_provided = {}
    
    return {
        'key_questions_answered': key_questions_answered,
        'evidence_provided': evidence_provided
    }


def given_clarification_json_file(workspace_directory: Path, behavior: str, key_questions: dict = None, evidence: dict = None, bot_paths=None):
    """Given: clarification.json file exists with data for behavior.
    
    Args:
        workspace_directory: Workspace directory path
        behavior: Behavior name
        key_questions: Dict of key questions answers (default: empty dict)
        evidence: Dict of evidence provided (default: empty dict)
        bot_paths: BotPath instance (if None, uses default docs/stories path)
    
    Returns:
        Path to clarification.json file
    """
    if bot_paths is None:
        stories_folder = workspace_directory / 'docs' / 'stories'
    else:
        documentation_path = bot_paths.documentation_path
        stories_folder = workspace_directory / documentation_path
    
    stories_folder.mkdir(parents=True, exist_ok=True)
    clarification_file = stories_folder / 'clarification.json'
    
    if key_questions is None:
        key_questions = {}
    if evidence is None:
        evidence = {}
    
    # New structure: key_questions has 'questions' and 'answers', evidence has 'required' and 'provided'
    existing_data = {
        behavior: {
            'key_questions': {
                'questions': [],
                'answers': key_questions
            },
            'evidence': {
                'required': [],
                'provided': evidence
            }
        }
    }
    clarification_file.write_text(json.dumps(existing_data, indent=2), encoding='utf-8')
    return clarification_file


def when_action_executes_with_clarification(action, parameters: dict):
    """When: Action executes with clarification parameters.
    
    Args:
        action: ClarifyContextAction instance
        parameters: Dict with 'key_questions_answered' and 'evidence_provided' keys
    
    Returns:
        Result from action.do_execute()
    """
    from agile_bot.src.actions.action_context import ClarifyActionContext
    
    context = ClarifyActionContext(
        answers=parameters.get('key_questions_answered'),
        evidence_provided=parameters.get('evidence_provided')
    )
    return action.do_execute(context)


def then_clarification_file_exists(workspace_directory: Path, bot_paths=None):
    """Then: clarification.json file exists.
    
    Args:
        workspace_directory: Workspace directory path
        bot_paths: BotPath instance (if None, uses default docs/stories path)
    
    Returns:
        Path to clarification.json file
    """
    if bot_paths is None:
        clarification_file = workspace_directory / 'docs' / 'stories' / 'clarification.json'
    else:
        documentation_path = bot_paths.documentation_path
        clarification_file = workspace_directory / documentation_path / 'clarification.json'
    
    assert clarification_file.exists(), f"clarification.json should be created at {clarification_file}"
    return clarification_file


def then_clarification_file_contains(clarification_file: Path, behavior: str, expected_key_questions: dict = None, expected_evidence: dict = None):
    """Then: clarification.json contains behavior data.
    
    Args:
        clarification_file: Path to clarification.json file
        behavior: Behavior name to check
        expected_key_questions: Expected key questions answers dict
        expected_evidence: Expected evidence provided dict
    
    Returns:
        Full clarification data dict
    """
    clarification_data = json.loads(clarification_file.read_text(encoding='utf-8'))
    assert behavior in clarification_data
    
    if expected_key_questions:
        assert 'key_questions' in clarification_data[behavior]
        assert 'answers' in clarification_data[behavior]['key_questions']
        for key, value in expected_key_questions.items():
            assert clarification_data[behavior]['key_questions']['answers'][key] == value
    
    if expected_evidence:
        assert 'evidence' in clarification_data[behavior]
        assert 'provided' in clarification_data[behavior]['evidence']
        for key, value in expected_evidence.items():
            assert clarification_data[behavior]['evidence']['provided'][key] == value
    
    return clarification_data
