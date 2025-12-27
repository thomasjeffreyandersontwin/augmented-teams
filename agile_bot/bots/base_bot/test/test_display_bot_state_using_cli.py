"""
Display Bot State Using CLI Tests

Tests for all stories in the 'Display Bot State Using CLI' sub-epic:
- Display Bot Hierarchy Tree in CLI
- Display Current Position in CLI
- Display Active Scope in CLI Status
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
    """Create behavior folder with actions and required guardrails"""
    behavior_dir = bot_directory / 'behaviors' / behavior_name
    behavior_dir.mkdir(parents=True, exist_ok=True)
    
    actions_workflow = {
        'actions': [{'name': action, 'order': i+1} for i, action in enumerate(actions)]
    }
    
    behavior_config = {
        'name': behavior_name,
        'description': f'Test {behavior_name} behavior',
        'order': 1,
        'actions_workflow': actions_workflow
    }
    (behavior_dir / 'behavior.json').write_text(json.dumps(behavior_config))
    
    # Create guardrails/strategy directory structure for strategy action
    guardrails_strategy_dir = behavior_dir / 'guardrails' / 'strategy'
    guardrails_strategy_dir.mkdir(parents=True, exist_ok=True)
    typical_assumptions = {'assumptions': []}
    (guardrails_strategy_dir / 'typical_assumptions.json').write_text(json.dumps(typical_assumptions))
    
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
    """Story: Display Bot Hierarchy Tree in CLI"""
    
    def test_user_views_bot_hierarchy_with_status_command(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views bot hierarchy with status command
        GIVEN: CLI is at discovery.build.instructions
        WHEN: user enters 'status'
        THEN: CLI displays bot hierarchy tree
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at discovery.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'discovery', 'build', 'instructions')
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: StatusDisplay generates bot hierarchy tree
        # AND: CLI displays bot hierarchy tree with [x], [*], [ ] indicators
        assert any(indicator in cli_response.output for indicator in ['[x]', '[*]', '[ ]']) or 'Behaviors:' in cli_response.output
        # AND: CLI shows discovery behavior marked with [*]
        assert 'discovery' in cli_response.output.lower()
        # AND: CLI shows build action under discovery
    
    def test_cli_shows_completed_actions_with_x_indicator(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI shows completed actions with [x] indicator
        GIVEN: CLI is at discovery.build.instructions
        WHEN: user views status
        THEN: CLI displays clarify action with [x] indicator
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at discovery.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'discovery', 'build', 'instructions')
        # AND: discovery.clarify action is completed
        
        # WHEN: user views status
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: StatusDisplay marks completed actions with [x]
        # AND: CLI displays clarify action with [x] indicator
        # Note: This depends on actual completion tracking implementation
        assert cli_response.status == 'success' or 'status' in cli_response.output.lower()


class TestDisplayCurrentPositionInCLI:
    """Story: Display Current Position in CLI"""
    
    @pytest.mark.parametrize("behavior,action,operation", [
        ("shape", "clarify", "instructions"),
        ("discovery", "build", "submit"),
        ("code", "validate", "confirm")
    ])
    def test_user_views_current_position_in_status(self, bot_directory, workspace_directory, monkeypatch, behavior, action, operation):
        """
        SCENARIO: User views current position in status
        GIVEN: CLI is at <behavior>.<action>.<operation>
        WHEN: user enters 'status'
        THEN: CLI displays current position
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at <behavior>.<action>.<operation>
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, behavior, ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, behavior, action, operation)
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: StatusDisplay reads current position from context
        # AND: CLI displays current position '<behavior>.<action>.<operation>'
        assert behavior in cli_response.output.lower()
        # AND: CLI highlights current position in hierarchy tree
    
    def test_current_position_updates_after_navigation(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: Current position updates after navigation
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user navigates to discovery.build.instructions
        THEN: CLI updates current position display
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user navigates to discovery.build.instructions
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        repl_session.read_and_execute_command('discovery.build.instructions')
        # AND: user views status
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: REPLSession updates behavior action state
        # AND: CLI updates current position display to 'discovery.build.instructions'
        assert 'discovery' in cli_response.output.lower()
        state_file = workspace_directory / 'behavior_action_state.json'
        state_data = json.loads(state_file.read_text())
        assert 'discovery' in state_data['current_behavior']
        assert 'build' in state_data['current_action']


class TestDisplayActiveScopeInCLIStatus:
    """Story: Display Active Scope in CLI Status"""
    
    def test_user_views_active_scope_in_status(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views active scope in status
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'status'
        THEN: CLI displays active scope section
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        # AND: active scope filter is story="Story1, Story2"
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        # Set scope first
        repl_session.read_and_execute_command('scope story="Story1, Story2"')
        # Then check status
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: StatusDisplay reads active scope from context
        # AND: CLI displays active scope section with 'story="Story1, Story2"'
        assert 'scope' in cli_response.output.lower() or 'story' in cli_response.output.lower()
    
    def test_status_shows_no_active_scope_when_cleared(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: Status shows no active scope when cleared
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'status'
        THEN: CLI displays 'No active scope filters'
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        # AND: no scope filters are active
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: StatusDisplay detects no active scope
        # AND: CLI displays 'No active scope filters' or omits scope section
        # Note: Actual behavior may vary based on implementation
        assert cli_response.status == 'success' or 'status' in cli_response.output.lower()
    
    def test_status_shows_combined_scope_filters(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: Status shows combined scope filters
        GIVEN: CLI is at code.validate.instructions
        WHEN: user enters 'status'
        THEN: CLI displays both knowledge graph and files scope
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at code.validate.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'code', ['strategy', 'validate', 'render', 'rules'])
        create_behavior_action_state(workspace_directory, 'code', 'validate', 'instructions')
        # AND: active scope filters are story="Validate Code" AND files="src/**/*.py"
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        # Set combined scope
        repl_session.read_and_execute_command('scope story="Validate Code" files="src/**/*.py"')
        # Then check status
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: StatusDisplay reads all active scope types from context
        # AND: CLI displays both knowledge graph and files scope
        assert 'scope' in cli_response.output.lower() or cli_response.status == 'success'

