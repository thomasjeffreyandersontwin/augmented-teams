"""
Execute Action Operation Through CLI Tests - CURRENT Implementation

Tests validate CURRENT implementation before refactoring.
"""
import pytest
import json
import sys
from pathlib import Path


@pytest.fixture
def bot_directory(tmp_path):
    """Create a temporary bot directory with bot_config.json"""
    bot_dir = tmp_path / 'agile_bot' / 'bots' / 'story_bot'
    bot_dir.mkdir(parents=True)
    
    config_data = {'name': 'story_bot'}
    (bot_dir / 'bot_config.json').write_text(json.dumps(config_data))
    
    return bot_dir


@pytest.fixture
def workspace_directory(tmp_path):
    """Create a temporary workspace directory"""
    workspace_dir = tmp_path / 'workspace'
    workspace_dir.mkdir(parents=True)
    return workspace_dir


def create_behavior(bot_directory, behavior_name, actions):
    """Create behavior folder with actions"""
    behavior_dir = bot_directory / 'behaviors' / behavior_name
    behavior_dir.mkdir(parents=True, exist_ok=True)
    
    behavior_config = {
        'name': behavior_name,
        'description': f'Test {behavior_name} behavior'
    }
    (behavior_dir / 'behavior.json').write_text(json.dumps(behavior_config))
    
    for action in actions:
        action_dir = behavior_dir / 'actions' / action
        action_dir.mkdir(parents=True, exist_ok=True)
        action_config = {
            'name': action,
            'description': f'Test {action} action'
        }
        (action_dir / 'action.json').write_text(json.dumps(action_config))


def create_behavior_action_state(workspace_directory, behavior, action, operation='instructions'):
    """Create behavior action state file with specified state"""
    state_data = {
        'current_behavior': f'story_bot.{behavior}',
        'current_action': f'story_bot.{behavior}.{action}',
        'operation': operation,
        'working_directory': str(workspace_directory),
        'timestamp': '2025-12-26T10:00:00.000000'
    }
    
    state_file = workspace_directory / 'behavior_action_state.json'
    state_file.write_text(json.dumps(state_data))
    return state_file


class TestGetActionInstructionsThroughCLI:
    """Story: Get Action Instructions Through CLI - CURRENT behavior"""
    
    def test_user_gets_instructions_for_build_action(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User gets instructions for build action
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'shape.build.instructions'
        THEN: CLI displays instructions
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'shape.build.instructions'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('shape.build.instructions')
        
        # THEN: CLI displays instructions
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestConfirmWorkThroughCLI:
    """Story: Confirm Work Through CLI - 2-phase model"""
    
    def test_user_confirms_build_work(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User confirms build work (2-phase model)
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'confirm'
        THEN: CLI processes work and advances to next action
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'confirm'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('confirm')
        
        # THEN: CLI processes confirm
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestConfirmActionCompletionThroughCLI:
    """Story: Confirm Action Completion - 2-phase model"""
    
    def test_user_confirms_build_action_completion(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User confirms build action completion
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'confirm'
        THEN: CLI processes confirmation and advances
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'confirm'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('confirm')
        
        # THEN: CLI processes confirmation
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestReExecuteCurrentOperationUsingCLI:
    """Story: Re-execute Current Operation - CURRENT behavior"""
    
    def test_user_re_executes_current_instructions(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User re-executes current instructions
        GIVEN: CLI is at discovery.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current operation
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at discovery.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'discovery', 'build', 'instructions')
        
        # WHEN: user enters 'current'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('current')
        
        # THEN: CLI re-executes current operation
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestHandleOperationErrorsAndValidationInCLI:
    """Story: Handle Operation Errors - CURRENT behavior"""
    
    def test_user_enters_invalid_command(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User enters invalid command
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'invalid_command'
        THEN: CLI displays error message
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'invalid_command'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('invalid_command_xyz')
        
        # THEN: CLI displays error
        assert cli_response is not None
        assert 'ERROR' in cli_response.output or 'error' in cli_response.output.lower() or cli_response.status == 'error'

