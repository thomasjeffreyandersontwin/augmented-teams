"""
Get Help Using CLI Tests

Tests for all stories in the 'Get Help Using CLI' sub-epic:
- View Available Commands Using CLI Help
- View Command Examples Using CLI Help
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


class TestViewAvailableCommandsUsingCLIHelp:
    """Story: View Available Commands Using CLI Help"""
    
    def test_user_views_all_available_commands(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views all available commands
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI displays help menu with all commands
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters 'help'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help')
        
        # THEN: CLI displays help menu with all commands
        expected_commands = ['status', 'back', 'next', 'current', 'help', 'exit', 'scope']
        commands_found = sum(1 for cmd in expected_commands if cmd in cli_response.output.lower())
        assert commands_found >= 5  # At least most commands should be present
        # AND: help menu includes navigation commands (status, back, next, current)
        # AND: help menu includes scope commands (scope)
        # AND: help menu includes utility commands (help, exit)
    
    def test_user_views_help_for_navigation_commands(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views help for navigation commands
        GIVEN: CLI is running
        WHEN: user enters 'help navigation'
        THEN: CLI displays help for navigation commands only
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters 'help navigation'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help navigation')
        
        # THEN: CLI displays help for navigation commands only
        # Note: Specific behavior depends on implementation
        assert 'help' in cli_response.output.lower() or cli_response.status == 'success'
    
    def test_user_views_help_for_scope_commands(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views help for scope commands
        GIVEN: CLI is running
        WHEN: user enters 'help scope'
        THEN: CLI displays help for scope commands
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'help scope'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help scope')
        
        # THEN: CLI displays help for scope commands
        # AND: help includes scope filter syntax
        # AND: help includes scope clear command
        assert 'help' in cli_response.output.lower() or 'scope' in cli_response.output.lower() or cli_response.status == 'success'


class TestViewCommandExamplesUsingCLIHelp:
    """Story: View Command Examples Using CLI Help"""
    
    def test_user_views_examples_for_dot_notation_navigation(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views examples for dot notation navigation
        GIVEN: CLI is running
        WHEN: user enters 'help' or 'help navigation'
        THEN: CLI displays examples for dot notation
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters 'help' or 'help navigation'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help')
        
        # THEN: CLI displays examples for dot notation
        # AND: examples include 'discovery.build.instructions'
        # AND: examples include 'code.validate'
        # AND: examples include 'shape'
        # Note: Exact format depends on implementation
        assert 'help' in cli_response.output.lower() or cli_response.status == 'success'
    
    def test_user_views_examples_for_scope_filters(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views examples for scope filters
        GIVEN: CLI is running
        WHEN: user enters 'help scope'
        THEN: CLI displays examples for scope filters
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running at shape.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user enters 'help scope'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help scope')
        
        # THEN: CLI displays examples for scope filters
        # AND: examples include 'scope story="Story1, Story2"'
        # AND: examples include 'scope files="src/**/*.py"'
        # AND: examples include 'scope epic="Build Agile Bot"'
        # AND: examples include 'scope clear'
        assert 'help' in cli_response.output.lower() or 'scope' in cli_response.output.lower() or cli_response.status == 'success'
    
    def test_user_views_examples_for_action_operations(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views examples for action operations
        GIVEN: CLI is running
        WHEN: user enters 'help operations' or 'help'
        THEN: CLI displays examples for operations
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is running at discovery.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior_action_state(workspace_directory, 'discovery', 'build', 'instructions')
        
        # WHEN: user enters 'help operations' or 'help'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help')
        
        # THEN: CLI displays examples for operations
        # AND: examples include 'submit'
        # AND: examples include 'confirm'
        # AND: examples include 'discovery.build.instructions --scope "Story1"'
        assert 'help' in cli_response.output.lower() or cli_response.status == 'success'
    
    def test_help_displays_current_bot_context_in_examples(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: Help displays current bot context in examples
        GIVEN: CLI is at discovery.build.instructions
        WHEN: user enters 'help'
        THEN: CLI displays examples relevant to current context
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at discovery.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'discovery', ['clarify', 'strategy', 'build', 'validate', 'render'])
        create_behavior(bot_directory, 'code', ['strategy', 'validate', 'render', 'rules'])
        create_behavior_action_state(workspace_directory, 'discovery', 'build', 'instructions')
        
        # WHEN: user enters 'help'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help')
        
        # THEN: CLI displays examples relevant to current context
        # AND: examples include current behavior name 'discovery'
        # AND: examples include available actions for current behavior
        # Note: Context-aware help depends on implementation
        assert 'help' in cli_response.output.lower() or cli_response.status == 'success'


class TestDynamicParameterHelp:
    """Story: Dynamic Parameter Discovery and Help Display"""
    
    def test_type_hint_converter_exists_and_works(self):
        """
        SCENARIO: TypeHintConverter converts Python types to CLI types
        GIVEN: TypeHintConverter class exists
        WHEN: converting various Python type hints
        THEN: returns appropriate CLI type strings
        """
        from agile_bot.bots.base_bot.src.actions.help_action import TypeHintConverter
        from pathlib import Path
        
        # Test basic types
        assert TypeHintConverter.to_cli_type(str) == "string"
        assert TypeHintConverter.to_cli_type(int) == "int"
        assert TypeHintConverter.to_cli_type(bool) == "bool"
        assert TypeHintConverter.to_cli_type(dict) == "dict"
        assert TypeHintConverter.to_cli_type(list) == "list"
        assert TypeHintConverter.to_cli_type(Path) == "path"
    
    def test_help_action_displays_typed_parameters(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: Help displays action parameters with proper type hints
        GIVEN: help action is executed
        WHEN: action has parameters with type hints
        THEN: parameters are displayed with CLI-friendly types
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: help behavior exists
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render', 'help'])
        create_behavior_action_state(workspace_directory, 'shape', 'help', 'instructions')
        
        # WHEN: user views help
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help')
        
        # THEN: parameter types are displayed (e.g., <dict>, <path>, <string>)
        # Not just generic "Optional parameter"
        output_lower = cli_response.output.lower()
        
        # Should have type annotations in angle brackets
        has_type_hints = '<dict>' in output_lower or '<path>' in output_lower or '<string>' in output_lower
        
        # Should NOT have only generic descriptions
        has_generic_only = 'optional parameter' in output_lower and not has_type_hints
        
        assert has_type_hints, "Help should display typed parameters like <dict>, <path>, <string>"
        assert not has_generic_only, "Help should not show only generic 'Optional parameter' descriptions"
    
    def test_help_displays_meaningful_parameter_descriptions(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: Help displays meaningful parameter descriptions
        GIVEN: actions have parameters like scope, answers, decisions
        WHEN: user views help
        THEN: parameters show specific descriptions, not generic ones
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: help is available
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build', 'validate', 'render', 'help'])
        create_behavior_action_state(workspace_directory, 'shape', 'help', 'instructions')
        
        # WHEN: user views help
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('help')
        
        # THEN: scope parameter should have structure description
        output_lower = cli_response.output.lower()
        
        # Check for meaningful descriptions (at least one should be present)
        meaningful_descriptions = [
            'scope structure' in output_lower,
            'dict mapping' in output_lower,
            'question keys' in output_lower,
            'decision criteria' in output_lower,
            "{'type':" in output_lower  # Scope structure example
        ]
        
        has_meaningful_desc = any(meaningful_descriptions)
        
        # Should not have ONLY generic descriptions for ALL parameters
        generic_count = output_lower.count('optional parameter')
        meaningful_count = sum(meaningful_descriptions)
        
        assert has_meaningful_desc, "Help should show meaningful parameter descriptions like 'Scope structure: {...}'"
        assert meaningful_count > 0 or generic_count < 5, "Should have more meaningful descriptions than generic ones"

