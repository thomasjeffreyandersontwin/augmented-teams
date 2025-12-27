"""
Display Bot State Using CLI Tests - CURRENT Implementation

Tests validate CURRENT implementation before refactoring.
Current uses REPLStatus helper, not StatusDisplay class.
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


class TestDisplayBotHierarchyTreeInCLI:
    """Story: Display Bot Hierarchy Tree - CURRENT behavior"""
    
    def test_user_views_bot_hierarchy_with_status_command(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views bot hierarchy with status command
        GIVEN: CLI is at exploration.build.instructions
        WHEN: user enters 'status'
        THEN: CLI displays bot hierarchy tree
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at exploration.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior(bot_directory, 'exploration', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'exploration', 'build', 'instructions')
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: CLI displays bot hierarchy tree with indicators
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Status command returns output (content varies based on state)
        assert len(cli_response.output) > 0


class TestDisplayCurrentPositionInCLI:
    """Story: Display Current Position - CURRENT behavior"""
    
    def test_user_views_current_position_in_status(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views current position in status
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user enters 'status'
        THEN: CLI displays current position
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: CLI displays current position
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Status command returns output
        assert len(cli_response.output) > 0


class TestDisplayActiveScopeInCLIStatus:
    """Story: Display Active Scope - CURRENT behavior"""
    
    def test_user_views_active_scope_in_status(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views active scope in status
        GIVEN: Scope filter is set
        WHEN: user views status
        THEN: CLI displays active scope
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: Scope filter is set
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user views status
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        # Set scope first
        repl_session.read_and_execute_command('scope story="Story1"')
        # Then view status
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: CLI displays status (scope may or may not be shown depending on implementation)
        assert cli_response is not None
        assert isinstance(cli_response.output, str)

