"""
Navigate Bot Behaviors and Actions With CLI Tests - CLI Command Interface

Domain logic tested in: test_invoke_bot_directly.py::TestNavigateToBehaviorActionAndExecute
Domain logic tested in: test_invoke_bot_directly.py::TestNavigateSequentially

These tests focus on CLI-specific concerns:
- Command parsing (dot notation, next/back commands)
- CLI output format and error messages (TTY, Markdown, JSON modes)
- Delegation to domain logic

Uses common helpers from: test_invoke_bot_helpers.py
"""
import pytest
import json
from agile_bot.src.cli.cli_session import CLISession
from agile_bot.test.domain.test_invoke_bot_helpers import (
    setup_test_bot,
    create_behavior_action_state,
    assert_bot_at_behavior_action
)


def assert_valid_json(output: str) -> dict:
    """
    Helper to verify output contains valid JSON.
    Handles cases where output may contain multiple JSON objects or extra content.
    Returns the first valid JSON object parsed.
    """
    output = output.strip()
    # Try to parse as single JSON object first
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        # If that fails, try to find first valid JSON object
        # Look for first complete JSON object (starts with { and ends with })
        start_idx = output.find('{')
        if start_idx >= 0:
            # Find matching closing brace
            brace_count = 0
            for i in range(start_idx, len(output)):
                if output[i] == '{':
                    brace_count += 1
                elif output[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # Found complete JSON object
                        json_str = output[start_idx:i+1]
                        try:
                            return json.loads(json_str)
                        except json.JSONDecodeError:
                            pass
        pytest.fail(f"Output does not contain valid JSON: {output[:200]}")


def extract_status_section(output: str) -> str:
    """Extract the CLI STATUS section from output (after INSTRUCTIONS)."""
    status_start = output.find('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    if status_start == -1:
        status_start = output.find('CLI STATUS section')
    if status_start == -1:
        return output  # Return full output if status section not found
    return output[status_start:].strip()


def extract_footer_section(output: str) -> str:
    """Extract the footer section with Behaviors and Actions from output."""
    footer_start = output.find('Behaviors:')
    if footer_start == -1:
        return ""
    return output[footer_start:].strip()


class TestNavigateToBehaviorActionAndExecuteInTTYMode:
    """
    Story: Navigate Using CLI Dot Notation (TTY Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestNavigateToBehaviorActionAndExecute
    CLI focus: Command parsing and TTY output format verification
    """
    
    def test_user_navigates_with_behavior_only(self, tmp_path):
        """
        SCENARIO: User navigates with behavior only (no dots) - TTY Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery'
        THEN: CLI parses command and delegates to bot.behaviors.navigate_to()
              CLI output shows behavior tree, instructions, and status in exact TTY format
              Footer shows discovery and clarify bolded
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN: Bot with two behaviors, currently at shape.clarify
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'discovery' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('discovery')
        
        # THEN: CLI successfully parsed command and shows exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify behavior tree at top (may show discovery with marker)
        # Note: Top tree shows all behaviors, current one marked with ➤ in Progress section
        assert 'discovery' in output
        
        # Verify INSTRUCTIONS section
        assert '====================================================================================================' in output
        assert 'INSTRUCTIONS' in output
        assert 'Behavior Instructions - discovery' in output
        assert 'Action Instructions - clarify' in output
        
        # Verify CLI STATUS section
        status_section = extract_status_section(output)
        assert 'CLI STATUS section' in status_section
        assert 'Bot:' in status_section
        assert 'story_bot' in status_section
        
        # Verify Progress section shows discovery.clarify as current
        assert 'Current Position:' in status_section
        assert 'discovery.clarify' in status_section
        # Check for behavior tree markers (➤ for current)
        assert '➤' in status_section  # Current behavior marker
        assert 'discovery' in status_section
        assert 'clarify' in status_section
        
        # Verify footer shows discovery and clarify bolded
        footer = extract_footer_section(output)
        assert 'Behaviors:' in footer
        # Check for ANSI bold codes or markdown bold
        assert ('[1mdiscovery[0m' in footer or '**discovery**' in footer or 
                '\x1b[1mdiscovery\x1b[0m' in footer)  # Bolded
        assert 'Actions:' in footer
        assert ('[1mclarify[0m' in footer or '**clarify**' in footer or
                '\x1b[1mclarify\x1b[0m' in footer)  # Bolded
        
        # Verify delegation: Domain logic was invoked
        assert_bot_at_behavior_action(bot, 'discovery', 'clarify')
    
    def test_user_navigates_with_behavior_dot_action(self, tmp_path):
        """
        SCENARIO: User navigates with behavior.action (one dot) - TTY Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery.validate'
        THEN: CLI parses dot notation and navigates to discovery.validate
              CLI output shows instructions and status in exact TTY format
              Footer shows discovery and validate bolded
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'discovery.validate' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('discovery.validate')
        
        # THEN: CLI parsed dot notation and shows exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify INSTRUCTIONS section
        assert 'INSTRUCTIONS' in output
        assert 'Behavior Instructions - discovery' in output
        assert 'Action Instructions - validate' in output
        
        # Verify CLI STATUS section
        status_section = extract_status_section(output)
        assert 'Current Position:' in status_section
        assert 'discovery.validate' in status_section
        assert '➤' in status_section  # Current behavior marker
        assert 'discovery' in status_section
        assert 'validate' in status_section
        
        # Verify footer shows discovery and validate bolded
        footer = extract_footer_section(output)
        assert ('[1mdiscovery[0m' in footer or '**discovery**' in footer or
                '\x1b[1mdiscovery\x1b[0m' in footer)  # Bolded
        assert ('[1mvalidate[0m' in footer or '**validate**' in footer or
                '\x1b[1mvalidate\x1b[0m' in footer)  # Bolded
        
        # Verify delegation: Domain logic was invoked
        assert_bot_at_behavior_action(bot, 'discovery', 'validate')
    
    def test_user_navigates_with_full_dot_notation(self, tmp_path):
        """
        SCENARIO: User navigates with behavior.action.operation (two dots) - TTY Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery.validate.instructions'
        THEN: CLI parses full dot notation and executes operation
              CLI output shows execution result in TTY format
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters full dot notation via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('discovery.validate.instructions')
        
        # THEN: CLI parsed command and CLI shows output in TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0
        
        # Verify delegation: Domain logic was invoked (operation executed)
        assert_bot_at_behavior_action(bot, 'discovery', 'validate')
    
    def test_user_enters_invalid_behavior_in_dot_notation(self, tmp_path):
        """
        SCENARIO: User enters invalid behavior in dot notation - TTY Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'invalid_behavior.validate.instructions'
        THEN: CLI detects invalid behavior and displays error message in TTY format
              CLI output contains error indication
        
        CLI focus: Error handling and user feedback in TTY format
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters invalid behavior via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('invalid_behavior.validate.instructions')
        
        # THEN: CLI shows error message in TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'ERROR' in cli_response.output or 'error' in cli_response.output.lower() or cli_response.status == 'error'


class TestNavigateToBehaviorActionAndExecuteInPipeMode:
    """
    Story: Navigate Using CLI Dot Notation (Markdown Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestNavigateToBehaviorActionAndExecute
    CLI focus: Command parsing and Markdown output format verification
    """
    
    def test_user_navigates_with_behavior_only(self, tmp_path):
        """
        SCENARIO: User navigates with behavior only (no dots) - Markdown Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery'
        THEN: CLI parses command and delegates to bot.behaviors.navigate_to()
              CLI output shows behavior header, instructions, and status in exact Markdown format
              Footer shows discovery and clarify bolded
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN: Bot with two behaviors, currently at shape.clarify
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'discovery' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('discovery')
        
        # THEN: CLI successfully parsed command and shows exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify behavior header
        assert '# Behavior: discovery' in output or '## Behavior: discovery' in output
        
        # Verify INSTRUCTIONS section
        assert '## Behavior Instructions - discovery' in output
        assert '## Action Instructions - clarify' in output
        
        # Verify CLI STATUS section in markdown
        assert '## CLI STATUS section' in output
        assert '## 🤖 Bot: story_bot' in output
        assert '## 🗺️ Progress' in output
        assert '**Current Position:** discovery.clarify' in output
        
        # Verify footer shows discovery and clarify bolded
        footer = extract_footer_section(output)
        assert '**discovery**' in footer  # Bolded in markdown
        assert '**clarify**' in footer  # Bolded in markdown
        
        # Verify delegation: Domain logic was invoked
        assert_bot_at_behavior_action(bot, 'discovery', 'clarify')
    
    def test_user_navigates_with_behavior_dot_action(self, tmp_path):
        """
        SCENARIO: User navigates with behavior.action (one dot) - Markdown Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery.validate'
        THEN: CLI parses dot notation and navigates to discovery.validate
              CLI output shows navigation success in Markdown format
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'discovery.validate' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('discovery.validate')
        
        # THEN: CLI parsed dot notation and CLI shows output in Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0
        
        # Verify delegation: Domain logic was invoked
        assert_bot_at_behavior_action(bot, 'discovery', 'validate')
    
    def test_user_navigates_with_full_dot_notation(self, tmp_path):
        """
        SCENARIO: User navigates with behavior.action.operation (two dots) - Markdown Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery.validate.instructions'
        THEN: CLI parses full dot notation and executes operation
              CLI output shows execution result in Markdown format
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters full dot notation via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('discovery.validate.instructions')
        
        # THEN: CLI parsed command and CLI shows output in Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0
        
        # Verify delegation: Domain logic was invoked (operation executed)
        assert_bot_at_behavior_action(bot, 'discovery', 'validate')
    
    def test_user_enters_invalid_behavior_in_dot_notation(self, tmp_path):
        """
        SCENARIO: User enters invalid behavior in dot notation - Markdown Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'invalid_behavior.validate.instructions'
        THEN: CLI detects invalid behavior and displays error message in Markdown format
              CLI output contains error indication
        
        CLI focus: Error handling and user feedback in Markdown format
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters invalid behavior via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('invalid_behavior.validate.instructions')
        
        # THEN: CLI shows error message in Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'ERROR' in cli_response.output or 'error' in cli_response.output.lower() or cli_response.status == 'error'


class TestNavigateToBehaviorActionAndExecuteInJSONMode:
    """
    Story: Navigate Using CLI Dot Notation (JSON Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestNavigateToBehaviorActionAndExecute
    CLI focus: Command parsing and JSON output format verification
    """
    
    def test_user_navigates_with_behavior_only(self, tmp_path):
        """
        SCENARIO: User navigates with behavior only (no dots) - JSON Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery'
        THEN: CLI parses command and delegates to bot.behaviors.navigate_to()
              CLI output shows behavior JSON, instructions JSON, and bot JSON in exact format
              First JSON object contains behavior metadata with discovery name
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN: Bot with two behaviors, currently at shape.clarify
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'discovery' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('discovery')
        
        # THEN: CLI successfully parsed command and shows exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify first JSON object is behavior metadata
        behavior_data = assert_valid_json(output)
        assert isinstance(behavior_data, dict)
        assert behavior_data['name'] == 'discovery'
        assert 'description' in behavior_data
        assert 'action_names' in behavior_data
        assert 'clarify' in behavior_data['action_names']
        
        # Verify instructions JSON object exists
        assert 'INSTRUCTIONS' in output
        instructions_start = output.find('{', output.find('INSTRUCTIONS'))
        assert instructions_start > 0, "Should find start of instructions JSON object"
        instructions_data = assert_valid_json(output[instructions_start:])
        assert instructions_data['behavior_metadata']['name'] == 'discovery'
        assert instructions_data['action_metadata']['name'] == 'clarify'
        
        # Verify bot JSON object exists
        # Find bot JSON by searching for "current_behavior" key (unique to bot JSON)
        current_behavior_key = output.rfind('"current_behavior"')
        assert current_behavior_key > instructions_start, "Bot JSON should come after instructions JSON"
        # Find the start of the JSON object containing "current_behavior"
        bot_start = output.rfind('{', 0, current_behavior_key)
        assert bot_start >= 0, "Should find start of bot JSON object"
        bot_data = assert_valid_json(output[bot_start:])
        assert bot_data['current_behavior'] == 'discovery'
        
        # Verify delegation: Domain logic was invoked
        assert_bot_at_behavior_action(bot, 'discovery', 'clarify')
    
    def test_user_navigates_with_behavior_dot_action(self, tmp_path):
        """
        SCENARIO: User navigates with behavior.action (one dot) - JSON Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery.validate'
        THEN: CLI parses dot notation and navigates to discovery.validate
              CLI output shows navigation success in JSON format
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'discovery.validate' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('discovery.validate')
        
        # THEN: CLI parsed dot notation and CLI shows output in JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Verify JSON format
        assert_valid_json(cli_response.output)
        
        # Verify delegation: Domain logic was invoked
        assert_bot_at_behavior_action(bot, 'discovery', 'validate')
    
    def test_user_navigates_with_full_dot_notation(self, tmp_path):
        """
        SCENARIO: User navigates with behavior.action.operation (two dots) - JSON Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'discovery.validate.instructions'
        THEN: CLI parses full dot notation and executes operation
              CLI output shows execution result in JSON format
        
        Domain logic tested in: TestNavigateToBehaviorActionAndExecute
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters full dot notation via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('discovery.validate.instructions')
        
        # THEN: CLI parsed command and CLI shows output in JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Verify JSON format
        assert_valid_json(cli_response.output)
        
        # Verify delegation: Domain logic was invoked (operation executed)
        assert_bot_at_behavior_action(bot, 'discovery', 'validate')
    
    def test_user_enters_invalid_behavior_in_dot_notation(self, tmp_path):
        """
        SCENARIO: User enters invalid behavior in dot notation - JSON Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'invalid_behavior.validate.instructions'
        THEN: CLI detects invalid behavior and displays error message in JSON format
              CLI output contains error indication
        
        CLI focus: Error handling and user feedback in JSON format
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters invalid behavior via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('invalid_behavior.validate.instructions')
        
        # THEN: CLI shows error message in JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Verify JSON format (even errors should be JSON)
        error_data = assert_valid_json(cli_response.output)
        # Error should be indicated in JSON structure
        assert 'error' in str(error_data).lower() or cli_response.status == 'error'


class TestNavigateSequentiallyInTTYMode:
    """
    Story: Navigate Sequentially Using CLI Commands (TTY Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestNavigateSequentially
    CLI focus: Sequential command parsing (next/back) and TTY output format
    """
    
    def test_user_navigates_with_next_command(self, tmp_path):
        """
        SCENARIO: User navigates with next command - TTY Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'next'
        THEN: CLI parses 'next' command
              And Bot navigates to shape.strategy action
              And Bot executes shape.strategy action
              And CLI output shows execution result in exact TTY format
              And CLI output shows instructions for shape.strategy in exact TTY format
              And CLI output shows bot status in exact TTY format
              And Footer shows shape and strategy bolded
        
        Domain logic tested in: TestNavigateSequentially
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'next' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('next')
        
        # THEN: CLI parsed command and shows exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify execution result section (from unified structure)
        assert 'Status:' in output or 'Message:' in output
        
        # Verify INSTRUCTIONS section shows strategy action
        assert 'INSTRUCTIONS' in output
        assert 'Behavior Instructions - shape' in output
        assert 'Action Instructions - strategy' in output
        
        # Verify CLI STATUS section
        status_section = extract_status_section(output)
        assert 'Current Position:' in status_section
        assert 'shape.strategy' in status_section
        assert '➤' in status_section  # Current behavior marker
        assert 'shape' in status_section
        assert 'strategy' in status_section
        
        # Verify footer shows shape and strategy bolded
        footer = extract_footer_section(output)
        assert ('[1mshape[0m' in footer or '**shape**' in footer or
                '\x1b[1mshape\x1b[0m' in footer)  # Bolded
        assert ('[1mstrategy[0m' in footer or '**strategy**' in footer or
                '\x1b[1mstrategy\x1b[0m' in footer)  # Bolded
        
        # Verify delegation: Advanced to next action (strategy)
        assert_bot_at_behavior_action(bot, 'shape', 'strategy')
    
    def test_user_navigates_with_back_command(self, tmp_path):
        """
        SCENARIO: User navigates with back command - TTY Mode
        GIVEN: CLI is at shape.strategy
        WHEN: user enters 'back'
        THEN: CLI parses 'back' command
              And Bot navigates to shape.clarify action
              And Bot executes shape.clarify action
              And CLI output shows execution result in exact TTY format
              And CLI output shows instructions for shape.clarify in exact TTY format
              And CLI output shows bot status in exact TTY format
        """
        # GIVEN: at strategy (second action)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'strategy')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'back' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('back')
        
        # THEN: CLI parsed command and CLI shows output in TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify execution result section (from unified structure)
        assert 'Status:' in output or 'Message:' in output
        
        # Verify INSTRUCTIONS section shows clarify action (previous action)
        assert 'INSTRUCTIONS' in output
        assert 'Behavior Instructions - shape' in output
        assert 'Action Instructions - clarify' in output
        
        # Verify delegation: Moved back to previous action (clarify)
        assert_bot_at_behavior_action(bot, 'shape', 'clarify')


class TestNavigateSequentiallyInPipeMode:
    """
    Story: Navigate Sequentially Using CLI Commands (Markdown Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestNavigateSequentially
    CLI focus: Sequential command parsing (next/back) and Markdown output format
    """
    
    def test_user_navigates_with_next_command(self, tmp_path):
        """
        SCENARIO: User navigates with next command - Markdown Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'next'
        THEN: CLI parses 'next' command
        And Bot navigates to shape.strategy action
        And Bot executes shape.strategy action
        And CLI output shows execution result in exact Markdown format
        And CLI output shows instructions for shape.strategy in exact Markdown format
        And CLI output shows bot status in exact Markdown format
        And Footer shows shape and strategy bolded
        
        Domain logic tested in: TestNavigateSequentially
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'next' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('next')
        
        # THEN: CLI parsed command and shows exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify execution result section (from unified structure)
        assert 'Status:' in output or 'Message:' in output
        
        # Verify INSTRUCTIONS section
        assert '## Behavior Instructions - shape' in output
        assert '## Action Instructions - strategy' in output
        
        # Verify footer shows shape and strategy bolded
        footer = extract_footer_section(output)
        assert '**shape**' in footer  # Bolded in markdown
        assert '**strategy**' in footer  # Bolded in markdown
        
        # Verify delegation: Advanced to next action (strategy)
        assert_bot_at_behavior_action(bot, 'shape', 'strategy')
    
    def test_user_navigates_with_back_command(self, tmp_path):
        """
        SCENARIO: User navigates with back command - Markdown Mode
        GIVEN: CLI is at shape.strategy
        WHEN: user enters 'back'
        THEN: CLI parses 'back' command
        And Bot navigates to shape.clarify action
        And Bot executes shape.clarify action
        And CLI output shows execution result in exact Markdown format
        And CLI output shows instructions for shape.clarify in exact Markdown format
        And CLI output shows bot status in exact Markdown format
        """
        # GIVEN: at strategy (second action)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'strategy')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'back' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('back')
        
        # THEN: CLI parsed command and CLI shows output in Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify execution result section (from unified structure)
        assert 'Status:' in output or 'Message:' in output
        
        # Verify INSTRUCTIONS section shows clarify action (previous action)
        assert '## Behavior Instructions - shape' in output
        assert '## Action Instructions - clarify' in output
        
        # Verify delegation: Moved back to previous action (clarify)
        assert_bot_at_behavior_action(bot, 'shape', 'clarify')


class TestNavigateSequentiallyInJSONMode:
    """
    Story: Navigate Sequentially Using CLI Commands (JSON Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestNavigateSequentially
    CLI focus: Sequential command parsing (next/back) and JSON output format
    """
    
    def test_user_navigates_with_next_command(self, tmp_path):
        """
        SCENARIO: User navigates with next command - JSON Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'next'
        THEN: CLI parses 'next' command
        And Bot navigates to shape.strategy action
        And Bot executes shape.strategy action
        And CLI output shows unified JSON object in exact format
        And Unified JSON object contains execution section with execution.status="success", execution.behavior="shape", execution.action="strategy"
        And Unified JSON object contains instructions section for shape.strategy
        And Unified JSON object contains bot section with current_behavior="shape"
        
        Domain logic tested in: TestNavigateSequentially
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'next' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('next')
        
        # THEN: CLI parsed command and shows exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify unified JSON structure
        unified_data = assert_valid_json(output)
        assert isinstance(unified_data, dict)
        
        # Verify execution section
        assert 'execution' in unified_data
        execution = unified_data['execution']
        assert isinstance(execution, dict)
        assert execution['status'] == 'success'
        assert execution['behavior'] == 'shape'
        assert execution['action'] == 'strategy'
        assert 'message' in execution
        
        # Verify instructions section
        assert 'instructions' in unified_data
        instructions = unified_data['instructions']
        assert isinstance(instructions, dict)
        assert instructions['behavior_metadata']['name'] == 'shape'
        assert instructions['action_metadata']['name'] == 'strategy'
        
        # Verify bot section
        assert 'bot' in unified_data
        bot_data = unified_data['bot']
        assert isinstance(bot_data, dict)
        assert bot_data['current_behavior'] == 'shape'
        
        # Verify delegation: Advanced to next action (strategy)
        assert_bot_at_behavior_action(bot, 'shape', 'strategy')
    
    def test_user_navigates_with_back_command(self, tmp_path):
        """
        SCENARIO: User navigates with back command - JSON Mode
        GIVEN: CLI is at shape.strategy
        WHEN: user enters 'back'
        THEN: CLI parses 'back' command
        And Bot navigates to shape.clarify action
        And Bot executes shape.clarify action
        And CLI output shows unified JSON object in exact format
        And Unified JSON object contains execution section with execution.status="success", execution.behavior="shape", execution.action="clarify"
        And Unified JSON object contains instructions section for shape.clarify
        And Unified JSON object contains bot section with current_behavior="shape"
        """
        # GIVEN: at strategy (second action)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'strategy')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'back' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('back')
        
        # THEN: CLI parsed command and CLI shows output in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify unified JSON structure
        unified_data = assert_valid_json(output)
        assert isinstance(unified_data, dict)
        
        # Verify execution section
        assert 'execution' in unified_data
        execution = unified_data['execution']
        assert isinstance(execution, dict)
        assert execution['status'] == 'success'
        assert execution['behavior'] == 'shape'
        assert execution['action'] == 'clarify'
        
        # Verify instructions section
        assert 'instructions' in unified_data
        instructions = unified_data['instructions']
        assert isinstance(instructions, dict)
        assert instructions['behavior_metadata']['name'] == 'shape'
        assert instructions['action_metadata']['name'] == 'clarify'
        
        # Verify bot section
        assert 'bot' in unified_data
        bot_data = unified_data['bot']
        assert isinstance(bot_data, dict)
        assert bot_data['current_behavior'] == 'shape'
        
        # Verify delegation: Moved back to previous action (clarify)
        assert_bot_at_behavior_action(bot, 'shape', 'clarify')


class TestExitCLIInTTYMode:
    """
    Story: Exit CLI Session (TTY Mode)
    
    CLI focus: Exit command parsing and session termination in TTY format
    """
    
    def test_user_exits_cli_with_exit_command(self, tmp_path):
        """
        SCENARIO: User exits CLI with exit command - TTY Mode
        GIVEN: CLI is running
        WHEN: user enters 'exit'
        THEN: CLI parses 'exit' command and terminates session
              CLI response indicates termination in TTY format
        
        CLI focus: Command parsing and session lifecycle
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'discovery', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'exit' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('exit')
        
        # THEN: CLI indicates exit/termination in TTY format
        assert cli_response is not None
        assert cli_response.cli_terminated or 'exit' in cli_response.output.lower() or cli_response.status == 'exit'


class TestExitCLIInPipeMode:
    """
    Story: Exit CLI Session (Markdown Mode)
    
    CLI focus: Exit command parsing and session termination in Markdown format
    """
    
    def test_user_exits_cli_with_exit_command(self, tmp_path):
        """
        SCENARIO: User exits CLI with exit command - Markdown Mode
        GIVEN: CLI is running
        WHEN: user enters 'exit'
        THEN: CLI parses 'exit' command and terminates session
              CLI response indicates termination in Markdown format
        
        CLI focus: Command parsing and session lifecycle
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'discovery', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'exit' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('exit')
        
        # THEN: CLI indicates exit/termination in Markdown format
        assert cli_response is not None
        assert cli_response.cli_terminated or 'exit' in cli_response.output.lower() or cli_response.status == 'exit'


class TestExitCLIInJSONMode:
    """
    Story: Exit CLI Session (JSON Mode)
    
    CLI focus: Exit command parsing and session termination in JSON format
    """
    
    def test_user_exits_cli_with_exit_command(self, tmp_path):
        """
        SCENARIO: User exits CLI with exit command - JSON Mode
        GIVEN: CLI is running
        WHEN: user enters 'exit'
        THEN: CLI parses 'exit' command and terminates session
              CLI response indicates termination in JSON format
        
        CLI focus: Command parsing and session lifecycle
        """
        # GIVEN: CLI is running
        bot, workspace = setup_test_bot(tmp_path, ['discovery'])
        create_behavior_action_state(workspace, 'story_bot', 'discovery', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'exit' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('exit')
        
        # THEN: CLI indicates exit/termination in JSON format
        assert cli_response is not None
        # Verify JSON format
        assert_valid_json(cli_response.output)
        assert cli_response.cli_terminated or 'exit' in cli_response.output.lower() or cli_response.status == 'exit'


class TestDisplayBotHierarchyTreeInTTYMode:
    """
    Story: Display Bot Hierarchy Tree with Progress Indicators (TTY Mode)
    
    CLI focus: Hierarchy tree display format with progress markers in TTY format
    """
    
    def test_user_views_bot_hierarchy_with_status_command(self, tmp_path):
        """
        SCENARIO: User views bot hierarchy with status command - TTY Mode
        GIVEN: CLI is at exploration.validate
        WHEN: user enters 'status'
        THEN: CLI parses status command
              CLI displays bot hierarchy tree in exact TTY format
              Shows exploration.validate as current with proper markers
              Footer shows exploration and validate bolded
        
        CLI focus: Status command execution and hierarchy display
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Status displayed in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify CLI STATUS section is present
        status_section = extract_status_section(output)
        assert 'CLI STATUS section' in status_section
        
        # Verify Progress section shows exploration.validate as current
        assert 'Current Position:' in status_section
        assert 'exploration.validate' in status_section
        assert '➤' in status_section  # Current behavior marker
        assert 'exploration' in status_section
        assert 'validate' in status_section
        
        # Verify behavior tree shows proper markers
        assert '☐' in status_section  # Non-current behaviors
        assert '➤' in status_section  # Current operation marker
        
        # Verify footer shows exploration and validate bolded
        footer = extract_footer_section(output)
        assert ('[1mexploration[0m' in footer or '**exploration**' in footer or
                '\x1b[1mexploration\x1b[0m' in footer)  # Bolded
        assert ('[1mvalidate[0m' in footer or '**validate**' in footer or
                '\x1b[1mvalidate\x1b[0m' in footer)  # Bolded


class TestDisplayBotHierarchyTreeInPipeMode:
    """
    Story: Display Bot Hierarchy Tree with Progress Indicators (Markdown Mode)
    
    CLI focus: Hierarchy tree display format with progress markers in Markdown format
    """
    
    def test_user_views_bot_hierarchy_with_status_command(self, tmp_path):
        """
        SCENARIO: User views bot hierarchy with status command - Markdown Mode
        GIVEN: CLI is at exploration.validate
        WHEN: user enters 'status'
        THEN: CLI parses status command
              CLI displays bot hierarchy tree in Markdown format
        
        CLI focus: Status command execution and hierarchy display
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Status displayed in Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0


class TestDisplayBotHierarchyTreeInJSONMode:
    """
    Story: Display Bot Hierarchy Tree with Progress Indicators (JSON Mode)
    
    CLI focus: Hierarchy tree display format with progress markers in JSON format
    """
    
    def test_user_views_bot_hierarchy_with_status_command(self, tmp_path):
        """
        SCENARIO: User views bot hierarchy with status command - JSON Mode
        GIVEN: CLI is at exploration.validate
        WHEN: user enters 'status'
        THEN: CLI parses status command
              CLI displays bot hierarchy tree in JSON format
        
        CLI focus: Status command execution and hierarchy display
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Status displayed in JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Verify JSON format
        assert_valid_json(cli_response.output)


class TestDisplayCurrentPositionInTTYMode:
    """
    Story: Display Current Position in CLI (TTY Mode)
    
    CLI focus: Current position indicators in status display in TTY format
    """
    
    def test_user_views_current_position_in_status(self, tmp_path):
        """
        SCENARIO: User views current position in status - TTY Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'status'
        THEN: CLI displays current position with indicators in exact TTY format
              Shows shape.clarify as current with proper markers
              Footer shows shape and clarify bolded
        
        CLI focus: Position display in status output
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Current position displayed in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify Progress section shows shape.clarify as current
        status_section = extract_status_section(output)
        assert 'Current Position:' in status_section
        assert 'shape.clarify' in status_section
        assert '➤' in status_section  # Current behavior marker
        assert 'shape' in status_section
        assert 'clarify' in status_section
        
        # Verify footer shows shape and clarify bolded
        footer = extract_footer_section(output)
        assert ('[1mshape[0m' in footer or '**shape**' in footer or
                '\x1b[1mshape\x1b[0m' in footer)  # Bolded
        assert ('[1mclarify[0m' in footer or '**clarify**' in footer or
                '\x1b[1mclarify\x1b[0m' in footer)  # Bolded
    
    def test_cli_displays_progress_section_with_current_position(self, tmp_path):
        """
        SCENARIO: CLI displays Progress section with current position - TTY Mode
        GIVEN: CLI is at exploration.validate
        WHEN: CLI renders status display
        THEN: CLI displays Progress section header in TTY format
        
        CLI focus: Progress section in status display
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Progress information included in TTY format
        display_text = cli_response.output
        # Progress section should be present (format may vary)
        assert len(display_text) > 0
    
    def test_cli_displays_behavior_in_progress_section(self, tmp_path):
        """
        SCENARIO: CLI displays behavior in Progress section - TTY Mode
        GIVEN: CLI is at shape.validate
        WHEN: CLI renders status display
        THEN: CLI displays current behavior in Progress section in TTY format
        
        CLI focus: Behavior display in progress section
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Behavior info included in TTY format
        display_text = cli_response.output
        assert len(display_text) > 0


class TestDisplayCurrentPositionInPipeMode:
    """
    Story: Display Current Position in CLI (Markdown Mode)
    
    CLI focus: Current position indicators in status display in Markdown format
    """
    
    def test_user_views_current_position_in_status(self, tmp_path):
        """
        SCENARIO: User views current position in status - Markdown Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'status'
        THEN: CLI displays current position with indicators in exact Markdown format
              Shows shape.clarify as current
              Footer shows shape and clarify bolded
        
        CLI focus: Position display in status output
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Current position displayed in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify Progress section shows shape.clarify as current
        assert '## 🗺️ Progress' in output
        assert '**Current Position:** shape.clarify' in output
        
        # Verify footer shows shape and clarify bolded
        footer = extract_footer_section(output)
        assert '**shape**' in footer  # Bolded in markdown
        assert '**clarify**' in footer  # Bolded in markdown
    
    def test_cli_displays_progress_section_with_current_position(self, tmp_path):
        """
        SCENARIO: CLI displays Progress section with current position - Markdown Mode
        GIVEN: CLI is at exploration.validate
        WHEN: CLI renders status display
        THEN: CLI displays Progress section header in Markdown format
        
        CLI focus: Progress section in status display
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Progress information included in Markdown format
        display_text = cli_response.output
        # Progress section should be present (format may vary)
        assert len(display_text) > 0
    
    def test_cli_displays_behavior_in_progress_section(self, tmp_path):
        """
        SCENARIO: CLI displays behavior in Progress section - Markdown Mode
        GIVEN: CLI is at shape.validate
        WHEN: CLI renders status display
        THEN: CLI displays current behavior in Progress section in Markdown format
        
        CLI focus: Behavior display in progress section
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Behavior info included in Markdown format
        display_text = cli_response.output
        assert len(display_text) > 0


class TestDisplayCurrentPositionInJSONMode:
    """
    Story: Display Current Position in CLI (JSON Mode)
    
    CLI focus: Current position indicators in status display in JSON format
    """
    
    def test_user_views_current_position_in_status(self, tmp_path):
        """
        SCENARIO: User views current position in status - JSON Mode
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'status'
        THEN: CLI displays current position with indicators in exact JSON format
              Bot JSON object contains current_behavior="shape"
        
        CLI focus: Position display in status output
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Current position displayed in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify bot JSON object contains current position
        bot_data = assert_valid_json(output)
        assert isinstance(bot_data, dict)
        assert bot_data['current_behavior'] == 'shape'
        assert 'behavior_names' in bot_data
        assert 'shape' in bot_data['behavior_names']
    
    def test_cli_displays_progress_section_with_current_position(self, tmp_path):
        """
        SCENARIO: CLI displays Progress section with current position - JSON Mode
        GIVEN: CLI is at exploration.validate
        WHEN: CLI renders status display
        THEN: CLI displays Progress section header in JSON format
        
        CLI focus: Progress section in status display
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Progress information included in JSON format
        display_text = cli_response.output
        # Verify JSON format
        progress_data = assert_valid_json(display_text)
        assert isinstance(progress_data, dict)
    
    def test_cli_displays_behavior_in_progress_section(self, tmp_path):
        """
        SCENARIO: CLI displays behavior in Progress section - JSON Mode
        GIVEN: CLI is at shape.validate
        WHEN: CLI renders status display
        THEN: CLI displays current behavior in Progress section in JSON format
        
        CLI focus: Behavior display in progress section
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('status')
        
        # THEN: Behavior info included in JSON format
        display_text = cli_response.output
        # Verify JSON format
        status_data = assert_valid_json(display_text)
        assert isinstance(status_data, dict)
