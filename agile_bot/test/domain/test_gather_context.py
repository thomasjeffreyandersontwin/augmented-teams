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
from agile_bot.src.actions.action_context import ClarifyActionContext
from agile_bot.src.bot_path import BotPath
from agile_bot.test.domain.bot_test_helper import BotTestHelper


class TestInjectGuardrailsAsPartOfClarifyRequirements:

    def test_action_injects_questions_and_evidence(self, tmp_path):
        """
        SCENARIO: Action injects questions and evidence from production guardrails
        GIVEN: Production story_bot with shape behavior (has guardrails)
        WHEN: Action injects guardrails
        THEN: Instructions contain questions and evidence from production files
        """
        # Given: Production story_bot with shape behavior
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action_obj = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # When: Action injects guardrails
        instructions = helper.behaviors.when_action_injects(action_obj, content='questions_and_evidence')
        
        # Then: Instructions contain all required clarify fields from production
        helper.clarify.assert_clarify_context_instructions(instructions)

class TestStoreClarificationData:

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
        bot_paths = BotPath(workspace_path=helper.workspace, bot_directory=helper.bot_directory)
        documentation_path = bot_paths.documentation_path
        clarification_file = helper.workspace / documentation_path / 'clarification.json'
        assert clarification_file.exists(), f"clarification.json should be created at {clarification_file}"
        
        clarification_data = json.loads(clarification_file.read_text(encoding='utf-8'))
        assert 'shape' in clarification_data
        assert clarification_data['shape']['key_questions']['answers']['user_types'] == 'Game Masters'
        assert clarification_data['shape']['evidence']['provided']['original_input'] == 'I want to turn minions into mobs'

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
        bot_paths = BotPath(workspace_path=helper.workspace, bot_directory=helper.bot_directory)
        documentation_path = bot_paths.documentation_path
        stories_folder = helper.workspace / documentation_path
        stories_folder.mkdir(parents=True, exist_ok=True)
        clarification_file = stories_folder / 'clarification.json'
        
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
        clarification_file.write_text(json.dumps(existing_data, indent=2), encoding='utf-8')
        
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
        clarification_data = json.loads(clarification_file.read_text(encoding='utf-8'))
        assert 'discovery' in clarification_data
        assert 'shape' in clarification_data
        assert clarification_data['discovery']['key_questions']['answers']['scope'] == 'Component level'
        assert clarification_data['shape']['key_questions']['answers']['user_types'] == 'Game Masters'

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
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        documentation_path = bot_paths.documentation_path
        clarification_file = helper.workspace / documentation_path / 'clarification.json'
        assert not clarification_file.exists(), f"clarification.json should not be created when no clarification data provided"


class TestLoadGuardrails:
    
    def test_guardrails_loads_required_context_guardrails(self, tmp_path):
        """
        SCENARIO: Guardrails loads required context guardrails
        GIVEN: Production story_bot behavior with guardrails directory
        WHEN: Guardrails instantiated with behavior_config
        THEN: Required context guardrails loaded
        """
        # Given: Production story_bot behavior (shape) with guardrails
        helper = BotTestHelper(tmp_path)
        behavior_name = 'shape'
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        
        # When: Guardrails instantiated from production behavior
        guardrails = behavior.guardrails
        
        # Then: Required context guardrails loaded from production files
        assert hasattr(guardrails, 'required_context')
        assert hasattr(guardrails, 'strategy')
        assert guardrails.required_context is not None
    
    def test_guardrails_loads_strategy_guardrails(self, tmp_path):
        """
        SCENARIO: Guardrails loads strategy guardrails
        GIVEN: Production story_bot behavior with strategy guardrails directory
        WHEN: Guardrails instantiated
        THEN: Strategy guardrails loaded
        """
        # Given: Production story_bot behavior (shape) with strategy guardrails
        helper = BotTestHelper(tmp_path)
        behavior_name = 'shape'
        from agile_bot.src.bot_path import BotPath
        from agile_bot.src.behaviors.behavior import Behavior
        bot_paths = BotPath(bot_directory=helper.bot_directory)
        behavior = Behavior(name=behavior_name, bot_paths=bot_paths)
        
        # When: Guardrails instantiated from production behavior
        guardrails = behavior.guardrails
        
        # Then: Strategy guardrails loaded from production files
        assert hasattr(guardrails, 'required_context')
        assert hasattr(guardrails, 'strategy')
        assert guardrails.strategy is not None
    
    def test_guardrails_properties_return_guardrails_objects(self, tmp_path):
        """
        SCENARIO: Guardrails properties return guardrails objects
        GIVEN: Production story_bot behavior with guardrails
        WHEN: Properties accessed (required_context, strategy)
        THEN: Returns RequiredContext object and Strategy object
        """
        # Given: Production story_bot behavior (shape) with guardrails
        helper = BotTestHelper(tmp_path)
        behavior_name = 'shape'
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
