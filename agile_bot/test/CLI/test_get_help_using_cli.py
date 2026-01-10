"""
Get Help Using CLI Tests - CLI Command Interface

CLI focus: Help command parsing and output formatting (TTY, Markdown, JSON modes)

These tests focus on CLI-specific concerns:
- 'help' command parsing
- Help output format and content
- Examples display

Uses common helpers from: test_invoke_bot_helpers.py
"""
import pytest
import json
from agile_bot.src.cli.cli_session import CLISession
from agile_bot.test.test_invoke_bot_helpers import (
    setup_test_bot,
    create_behavior_action_state
)


def assert_valid_json(output: str) -> dict:
    """
    Helper to verify output contains valid JSON.
    Handles cases where output may contain multiple JSON objects or extra content.
    Returns the first valid JSON object parsed.
    """
    output = output.strip()
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        start_idx = output.find('{')
        if start_idx >= 0:
            brace_count = 0
            for i in range(start_idx, len(output)):
                if output[i] == '{':
                    brace_count += 1
                elif output[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        json_str = output[start_idx:i+1]
                        try:
                            return json.loads(json_str)
                        except json.JSONDecodeError:
                            pass
        pytest.fail(f"Output does not contain valid JSON: {output[:200]}")


class TestDisplayActionHelpUsingCLIInTTYMode:
    """
    Story: View Available Commands (Help) (TTY Mode)
    
    CLI focus: Help command parsing and TTY output format
    """
    
    def test_user_views_all_available_commands(self, tmp_path):
        """
        SCENARIO: User views all available commands - TTY Mode
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI parses 'help' command
              CLI displays help menu in exact TTY format
              Shows Core Commands, Available Components, Examples, Other Commands, Scope Command Details
        
        CLI focus: Help output exact format verification
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'help' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('help')
        
        # THEN: CLI displays help menu in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify exact format with hard-coded expectations
        # Core Commands section
        assert 'Core Commands:' in output
        assert 'echo \'[behavior.][action.]operation\' | python repl_main.py' in output
        assert 'echo \'[behavior][.action]\' | python repl_main.py' in output
        
        # Available Components section
        assert 'Available Components:' in output
        assert 'behaviors' in output
        assert 'shape' in output or 'discovery' in output  # At least one behavior listed
        assert 'actions:' in output
        assert 'clarify' in output
        assert 'build' in output
        assert 'validate' in output
        assert 'operations:' in output
        assert 'instructions' in output
        assert 'confirm' in output
        
        # Examples section
        assert 'Examples:' in output
        assert 'echo \'.\' | python repl_main.py' in output
        assert 'echo \'shape\' | python repl_main.py' in output
        assert 'echo \'shape.build\' | python repl_main.py' in output
        
        # Other Commands section
        assert 'Other Commands:' in output
        assert 'echo \'status\' | python repl_main.py' in output
        assert 'echo \'next\' | python repl_main.py' in output
        assert 'echo \'scope [filter]\' | python repl_main.py' in output
        assert 'echo \'help\' | python repl_main.py' in output
        assert 'echo \'exit\' | python repl_main.py' in output
        
        # Scope Command Details section
        assert 'Scope Command Details:' in output
        assert 'IMPORTANT:' in output
        assert 'Usage (pick ONE' in output or 'Usage:' in output
        assert 'echo \'scope all\' | python repl_main.py' in output
        assert 'echo \'scope "Story Name"\' | python repl_main.py' in output
        assert 'echo \'scope "file:' in output

    def test_user_views_examples_in_help(self, tmp_path):
        """
        SCENARIO: User views examples in help - TTY Mode
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI displays help with examples in exact TTY format
              Shows specific command examples with descriptions
        
        CLI focus: Help examples format verification
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'help' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('help')
        
        # THEN: CLI displays help with examples in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify examples section format
        assert 'Examples:' in output
        # Verify example format: command -> description
        assert '->' in output or '-> Execute' in output or '-> Jump' in output
        # Verify specific examples
        assert 'echo \'.\' | python repl_main.py' in output
        assert 'echo \'shape.build\' | python repl_main.py' in output


class TestDisplayActionHelpUsingCLIInPipeMode:
    """
    Story: View Available Commands (Help) (Markdown Mode)
    
    CLI focus: Help command parsing and Markdown output format
    """
    
    def test_user_views_all_available_commands(self, tmp_path):
        """
        SCENARIO: User views all available commands - Markdown Mode
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI parses 'help' command
              CLI displays help menu in exact Markdown format
        
        CLI focus: Help output format verification
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'help' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('help')
        
        # THEN: CLI displays help menu in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify exact Markdown format with hard-coded expectations
        # Core Commands section
        assert '## Core Commands' in output
        assert 'echo \'[behavior.][action.]operation\' | python repl_main.py' in output
        
        # Available Components section
        assert 'Available Components:' in output
        assert 'behaviors' in output
        assert 'actions:' in output
        assert 'clarify' in output
        assert 'build' in output
        
        # Examples section
        assert 'Examples:' in output
        assert 'echo \'.\' | python repl_main.py' in output
        
        # Other Commands section
        assert 'Other Commands:' in output
        assert 'echo \'status\' | python repl_main.py' in output
        assert 'echo \'help\' | python repl_main.py' in output

    def test_user_views_examples_in_help(self, tmp_path):
        """
        SCENARIO: User views examples in help - Markdown Mode
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI displays help with examples in exact Markdown format
        
        CLI focus: Help output format verification
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'help' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('help')
        
        # THEN: CLI displays help with examples in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify examples section format
        assert 'Examples:' in output
        assert 'echo \'.\' | python repl_main.py' in output
        assert 'echo \'shape.build\' | python repl_main.py' in output


class TestDisplayActionHelpUsingCLIInJSONMode:
    """
    Story: View Available Commands (Help) (JSON Mode)
    
    CLI focus: Help command parsing and JSON output format
    """
    
    def test_user_views_all_available_commands(self, tmp_path):
        """
        SCENARIO: User views all available commands - JSON Mode
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI parses 'help' command
              CLI displays help menu in exact JSON format
        
        CLI focus: Help output format verification
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'help' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('help')
        
        # THEN: CLI displays help menu in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify JSON format
        help_data = assert_valid_json(output)
        assert isinstance(help_data, dict)
        # Verify help JSON structure
        assert 'main_help' in help_data or 'commands' in help_data or 'examples' in help_data

    def test_user_views_examples_in_help(self, tmp_path):
        """
        SCENARIO: User views examples in help - JSON Mode
        GIVEN: CLI is running
        WHEN: user enters 'help'
        THEN: CLI displays help with examples in exact JSON format
        
        CLI focus: Help output format verification
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'help' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('help')
        
        # THEN: CLI displays help with examples in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify JSON format
        help_data = assert_valid_json(output)
        assert isinstance(help_data, dict)
        # Verify examples are in JSON structure
        assert 'examples' in help_data or 'command_examples' in help_data or 'main_help' in help_data
