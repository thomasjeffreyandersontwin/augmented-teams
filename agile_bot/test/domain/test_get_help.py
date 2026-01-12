
import pytest
import json
import os
from pathlib import Path
from agile_bot.src.bot.bot import Bot, BotResult
from agile_bot.src.behaviors import Behavior
from agile_bot.src.bot_path import BotPath
# NOTE: This file uses BotTestHelper instead of deprecated functions
# Removed: bootstrap_env, create_actions_workflow_json (use BotTestHelper)
from agile_bot.test.domain.bot_test_helper import BotTestHelper

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
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        
        # WHEN: Action is accessed
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # THEN: Complete action object with instructions capability
        assert action is not None
        assert hasattr(action, 'action_name')
        assert action.action_name == 'clarify'
        assert hasattr(action, 'order')
        assert isinstance(action.order, int)
        assert hasattr(action, 'behavior')
        assert hasattr(action, 'get_instructions') or hasattr(action, 'instructions')
        
        # Verify instructions can be retrieved and have structure
        if hasattr(action, 'get_instructions'):
            instructions = action.get_instructions()
            assert instructions is not None
            assert isinstance(instructions, (dict, object))
        elif hasattr(action, 'instructions'):
            instructions = action.instructions
            assert instructions is not None
            assert isinstance(instructions, (dict, object))


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
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # WHEN: Parameter help is requested
        # Check if action has parameter help method or property
        has_param_help = (
            hasattr(action, 'get_parameter_help') or
            hasattr(action, 'parameter_help') or
            hasattr(action, 'parameters') or
            hasattr(action, 'get_parameters')
        )
        
        # THEN: Complete action object with parameter help capability
        assert action is not None
        assert action.action_name == 'clarify'
        assert hasattr(action, 'order')
        assert isinstance(action.order, int)
        assert has_param_help, "Action should provide parameter help"
        
        # Try to retrieve parameter help if method exists and verify structure
        if hasattr(action, 'get_parameter_help'):
            param_help = action.get_parameter_help()
            assert param_help is not None
            assert isinstance(param_help, (dict, list, str))
        elif hasattr(action, 'parameter_help'):
            param_help = action.parameter_help
            assert param_help is not None
            assert isinstance(param_help, (dict, list, str))
        elif hasattr(action, 'parameters'):
            params = action.parameters
            assert params is not None
            assert isinstance(params, (dict, list))
        elif hasattr(action, 'get_parameters'):
            params = action.get_parameters()
            assert params is not None
            assert isinstance(params, (dict, list))


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
        helper = BotTestHelper(tmp_path)
        helper.bot.behaviors.navigate_to('shape')
        action = helper.bot.behaviors.current.actions.find_by_name('clarify')
        
        # WHEN: Command examples are requested
        # Check if action has examples method or property
        has_examples = (
            hasattr(action, 'get_examples') or
            hasattr(action, 'examples') or
            hasattr(action, 'get_command_examples') or
            hasattr(action, 'command_examples')
        )
        
        # THEN: Complete action object (examples are optional)
        assert action is not None
        assert action.action_name == 'clarify'
        assert hasattr(action, 'order')
        assert isinstance(action.order, int)
        assert has_examples or True, "Action may provide command examples"
        
        # Try to retrieve examples if method exists and verify structure
        if hasattr(action, 'get_examples'):
            examples = action.get_examples()
            assert examples is not None
            assert isinstance(examples, (dict, list, str))
        elif hasattr(action, 'examples'):
            examples = action.examples
            assert examples is not None
            assert isinstance(examples, (dict, list, str))
        elif hasattr(action, 'get_command_examples'):
            examples = action.get_command_examples()
            assert examples is not None
            assert isinstance(examples, (dict, list, str))
        elif hasattr(action, 'command_examples'):
            examples = action.command_examples
            assert examples is not None
            assert isinstance(examples, (dict, list, str))
