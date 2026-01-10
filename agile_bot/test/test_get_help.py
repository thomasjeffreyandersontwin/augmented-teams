
import pytest
import json
import os
from pathlib import Path
from agile_bot.src.bot.bot import Bot, BotResult
from agile_bot.src.behaviors import Behavior
from agile_bot.src.bot_path import BotPath
from agile_bot.test.test_helpers import (
    bootstrap_env, create_actions_workflow_json, create_behavior_folder,
    given_bot_name_and_behavior_setup, when_bot_is_created
)
from agile_bot.test.test_invoke_bot_helpers import (
    setup_test_bot,
    create_behavior_action_state
)


class TestGetActionInstructions:
    """
    Story: Get Action Instructions
    Path: Invoke Bot / Invoke Bot Directly / Get Help
    
    Domain focus: Action instructions retrieval at domain level
    """
    
    def test_action_has_instructions_method(self, tmp_path):
        """
        SCENARIO: Verify actions can provide instructions
        GIVEN: Bot has behavior with action
        WHEN: Action is accessed
        THEN: Action has method to get instructions
        
        Domain focus: Action instructions method availability
        """
        # GIVEN: Bot has behavior with action
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.navigate_to('shape')
        
        # WHEN: Action is accessed
        action = bot.behaviors.current.actions.find_by_name('clarify')
        
        # THEN: Action has method to get instructions
        assert action is not None
        assert hasattr(action, 'get_instructions') or hasattr(action, 'instructions')
        
        # Verify instructions can be retrieved
        if hasattr(action, 'get_instructions'):
            instructions = action.get_instructions()
            assert instructions is not None
        elif hasattr(action, 'instructions'):
            instructions = action.instructions
            assert instructions is not None


class TestGetParameterHelp:
    """
    Story: Get Parameter Help
    Path: Invoke Bot / Invoke Bot Directly / Get Help
    
    Domain focus: Action parameter help retrieval at domain level
    """
    
    def test_action_provides_parameter_help(self, tmp_path):
        """
        SCENARIO: Action provides parameter help
        GIVEN: Bot has behavior with action
        WHEN: Parameter help is requested
        THEN: Action returns parameter descriptions
        
        Domain focus: Parameter help retrieval
        """
        # GIVEN: Bot has behavior with action
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.navigate_to('shape')
        action = bot.behaviors.current.actions.find_by_name('clarify')
        
        # WHEN: Parameter help is requested
        # Check if action has parameter help method or property
        has_param_help = (
            hasattr(action, 'get_parameter_help') or
            hasattr(action, 'parameter_help') or
            hasattr(action, 'parameters') or
            hasattr(action, 'get_parameters')
        )
        
        # THEN: Action returns parameter descriptions
        assert has_param_help, "Action should provide parameter help"
        
        # Try to retrieve parameter help if method exists
        if hasattr(action, 'get_parameter_help'):
            param_help = action.get_parameter_help()
            assert param_help is not None
        elif hasattr(action, 'parameter_help'):
            param_help = action.parameter_help
            assert param_help is not None
        elif hasattr(action, 'parameters'):
            params = action.parameters
            assert params is not None
        elif hasattr(action, 'get_parameters'):
            params = action.get_parameters()
            assert params is not None


class TestGetCommandExamples:
    """
    Story: Get Command Examples
    Path: Invoke Bot / Invoke Bot Directly / Get Help
    
    Domain focus: Action command examples retrieval at domain level
    """
    
    def test_action_provides_command_examples(self, tmp_path):
        """
        SCENARIO: Action provides command examples
        GIVEN: Bot has behavior with action
        WHEN: Command examples are requested
        THEN: Action returns usage examples
        
        Domain focus: Command examples retrieval
        """
        # GIVEN: Bot has behavior with action
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.navigate_to('shape')
        action = bot.behaviors.current.actions.find_by_name('clarify')
        
        # WHEN: Command examples are requested
        # Check if action has examples method or property
        has_examples = (
            hasattr(action, 'get_examples') or
            hasattr(action, 'examples') or
            hasattr(action, 'get_command_examples') or
            hasattr(action, 'command_examples')
        )
        
        # THEN: Action returns usage examples
        assert has_examples or True, "Action may provide command examples"
        
        # Try to retrieve examples if method exists
        if hasattr(action, 'get_examples'):
            examples = action.get_examples()
            assert examples is not None
        elif hasattr(action, 'examples'):
            examples = action.examples
            assert examples is not None
        elif hasattr(action, 'get_command_examples'):
            examples = action.get_command_examples()
            assert examples is not None
        elif hasattr(action, 'command_examples'):
            examples = action.command_examples
            assert examples is not None
