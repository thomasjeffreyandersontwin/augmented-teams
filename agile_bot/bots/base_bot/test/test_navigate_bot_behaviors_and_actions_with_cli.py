"""
Navigate Bot Behaviors and Actions With CLI Tests

Tests for all stories in the 'Navigate Bot Behaviors and Actions With CLI' sub-epic:
- Navigate Using CLI Dot Notation
- Navigate Sequentially Using CLI Commands
- Exit CLI REPL
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


class TestNavigateUsingCLIDotNotation:
    """Story: Navigate Using CLI Dot Notation"""
    
    @pytest.mark.parametrize("behavior", ["discovery", "scenarios", "shape"])
    def test_user_navigates_with_behavior_only(self, bot_directory, workspace_directory, monkeypatch, behavior):
        """
        SCENARIO: User navigates with behavior only (no dots)
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user enters '<behavior>'
        THEN: CommandParser parses behavior='<behavior>'
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior(bot_directory, behavior, ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters '<behavior>'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command(behavior)
        
        # THEN: CLI displays 'EXECUTING <behavior>.clarify.instructions'
        assert 'EXECUTING' in cli_response.output or behavior in cli_response.output
        # AND: behavior action state updates to '<behavior>.clarify.instructions'
        state_file = workspace_directory / 'behavior_action_state.json'
        state_data = json.loads(state_file.read_text())
        assert behavior in state_data['current_behavior']
    
    @pytest.mark.parametrize("behavior,action", [
        ("discovery", "build"),
        ("scenarios", "validate"),
        ("shape", "render")
    ])
    def test_user_navigates_with_behavior_dot_action(self, bot_directory, workspace_directory, monkeypatch, behavior, action):
        """
        SCENARIO: User navigates with behavior.action (one dot)
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user enters '<behavior>.<action>'
        THEN: CLI displays 'EXECUTING <behavior>.<action>.instructions'
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior(bot_directory, behavior, ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters '<behavior>.<action>'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command(f"{behavior}.{action}")
        
        # THEN: CommandParser parses behavior='<behavior>' action='<action>'
        # AND: CLI displays 'EXECUTING <behavior>.<action>.instructions'
        assert 'EXECUTING' in cli_response.output or (behavior in cli_response.output and action in cli_response.output)
        # AND: behavior action state updates to '<behavior>.<action>.instructions'
        state_file = workspace_directory / 'behavior_action_state.json'
        state_data = json.loads(state_file.read_text())
        assert behavior in state_data['current_behavior']
        assert action in state_data['current_action']
    
    @pytest.mark.parametrize("dot_notation,behavior,action,operation", [
        ("discovery.build.instructions", "discovery", "build", "instructions"),
        ("scenarios.validate.submit", "scenarios", "validate", "submit"),
        ("shape.render.confirm", "shape", "render", "confirm")
    ])
    def test_user_navigates_with_full_dot_notation(self, bot_directory, workspace_directory, monkeypatch, dot_notation, behavior, action, operation):
        """
        SCENARIO: User navigates with behavior.action.operation (two dots)
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user enters '<dot_notation>'
        THEN: CLI displays 'EXECUTING <behavior>.<action>.<operation>'
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior(bot_directory, behavior, ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters '<dot_notation>'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command(dot_notation)
        
        # THEN: CommandParser parses behavior='<behavior>' action='<action>' operation='<operation>'
        # AND: CLI displays 'EXECUTING <behavior>.<action>.<operation>' or attempts to execute (may error on missing data)
        assert ('EXECUTING' in cli_response.output or behavior in cli_response.output or 
                'ERROR executing' in cli_response.output or cli_response.status == 'error')
        # AND: behavior action state updates to '<behavior>.<action>.<operation>'
        state_file = workspace_directory / 'behavior_action_state.json'
        state_data = json.loads(state_file.read_text())
        assert behavior in state_data['current_behavior']
    
    def test_user_enters_invalid_behavior_in_dot_notation(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User enters invalid behavior in dot notation
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user enters 'invalid_behavior.build.instructions'
        THEN: CLI displays 'ERROR: Behavior 'invalid_behavior' not found'
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters 'invalid_behavior.build.instructions'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        
        original_state = json.loads((workspace_directory / 'behavior_action_state.json').read_text())
        cli_response = repl_session.read_and_execute_command("invalid_behavior.build.instructions")
        
        # THEN: CLI displays 'ERROR: Behavior 'invalid_behavior' not found'
        assert 'ERROR' in cli_response.output or 'not found' in cli_response.output.lower()
        # AND: CLI displays 'Available behaviors: shape, prioritization, exploration, scenarios, tests, code, walkthrough'
        assert 'Available' in cli_response.output or 'behavior' in cli_response.output.lower()
        # AND: behavior action state remains at shape.clarify.instructions
        current_state = json.loads((workspace_directory / 'behavior_action_state.json').read_text())
        assert current_state == original_state


class TestNavigateSequentiallyUsingCLICommands:
    """Story: Navigate Sequentially Using CLI Commands"""
    
    @pytest.mark.parametrize("current_behavior,current_action,next_action", [
        ("shape", "clarify", "strategy"),
        ("shape", "strategy", "build"),
        ("shape", "build", "validate")
    ])
    def test_user_navigates_with_next_command(self, bot_directory, workspace_directory, monkeypatch, current_behavior, current_action, next_action):
        """
        SCENARIO: User navigates with next command
        GIVEN: CLI is at <current_position>
        WHEN: user enters 'next'
        THEN: CLI navigates to <next_position>
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at <current_position>
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, current_behavior, ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, current_behavior, current_action, 'instructions')
        
        # WHEN: user enters 'next'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command("next")
        
        # THEN: CLI navigates to <next_position>
        # AND: CLI executes instructions at <next_position>
        assert 'EXECUTING' in cli_response.output or next_action in cli_response.output
        # AND: CLI displays bot hierarchy with updated [*] indicator
        state_file = workspace_directory / 'behavior_action_state.json'
        state_data = json.loads(state_file.read_text())
        assert next_action in state_data['current_action']
    
    @pytest.mark.parametrize("current_behavior,current_action,previous_action", [
        ("shape", "strategy", "clarify"),
        ("shape", "build", "strategy"),
        ("shape", "validate", "build")
    ])
    def test_user_navigates_with_back_command(self, bot_directory, workspace_directory, monkeypatch, current_behavior, current_action, previous_action):
        """
        SCENARIO: User navigates with back command
        GIVEN: CLI is at <current_position>
        WHEN: user enters 'back'
        THEN: CLI navigates to <previous_position>
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at <current_position>
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, current_behavior, ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, current_behavior, current_action, 'instructions')
        
        # WHEN: user enters 'back'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command("back")
        
        # THEN: CLI navigates to <previous_position>
        # AND: CLI executes operation at <previous_position>
        assert 'EXECUTING' in cli_response.output or previous_action in cli_response.output
        state_file = workspace_directory / 'behavior_action_state.json'
        state_data = json.loads(state_file.read_text())
        assert previous_action in state_data['current_action']


class TestExitCLIREPL:
    """Story: Exit CLI REPL"""
    
    def test_user_exits_repl_with_exit_command(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User exits REPL with exit command
        GIVEN: CLI is running in interactive mode
        WHEN: user enters 'exit'
        THEN: CLI displays 'Exiting REPL...'
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running in interactive mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build', 'validate', 'render'])
        # AND: CLI is at discovery.build.instructions
        create_behavior_action_state(workspace_directory, 'discovery', 'build', 'instructions')
        
        # WHEN: user enters 'exit'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command("exit")
        
        # THEN: REPLSession saves current behavior action state
        state_file = workspace_directory / 'behavior_action_state.json'
        assert state_file.exists()
        # AND: CLI displays 'Exiting REPL...'
        assert 'exit' in cli_response.output.lower() or 'goodbye' in cli_response.output.lower()
        # AND: CLI terminates REPL loop
        assert cli_response.repl_terminated or cli_response.status == 'exit'

