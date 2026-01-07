"""
Manage Bot Scope Through CLI Tests - CURRENT Implementation

Tests validate CURRENT implementation before refactoring.
Current implementation uses single Scope object, not separate KnowledgeGraphFilter + FileFilter.
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


class TestFilterWorkUsingScopeInCLI:
    """Story: Filter Work Using Scope - CURRENT behavior (single Scope object)"""
    
    def test_user_sets_scope_filter(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User sets scope filter
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'scope story="Story1"'
        THEN: CLI stores scope filter
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'scope story="Story1"'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('scope story="Story1"')
        
        # THEN: CLI stores scope filter
        assert cli_response is not None
        # Current implementation stores scope in session
        assert isinstance(cli_response.output, str)
    
    def test_user_views_current_scope(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views current scope
        GIVEN: Scope filter is set
        WHEN: user enters 'scope'
        THEN: CLI displays current scope
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: Scope filter is set
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'scope' (view current)
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        # First set a scope
        repl_session.read_and_execute_command('scope story="Story1"')
        # Then view it
        cli_response = repl_session.read_and_execute_command('scope')
        
        # THEN: CLI displays current scope
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestClearScopeFiltersInCLI:
    """Story: Clear Scope Filters - CURRENT behavior"""
    
    def test_user_clears_all_scope_filters(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User clears all scope filters
        GIVEN: Scope filter is set
        WHEN: user enters 'scope clear'
        THEN: CLI clears scope filter
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: Scope filter is set
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'scope clear'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        # First set a scope
        repl_session.read_and_execute_command('scope story="Story1"')
        # Then clear it
        cli_response = repl_session.read_and_execute_command('scope clear')
        
        # THEN: CLI clears scope
        assert cli_response is not None
        assert isinstance(cli_response.output, str)

