"""
Execute Action Operation Through CLI Tests - CLI Command Interface

Domain logic tested in: test_invoke_bot_directly.py (various test classes)

These tests focus on CLI-specific concerns:
- Action operation command parsing
- CLI output format for different operations (TTY, Markdown, JSON modes)
- Error handling and validation

Uses common helpers from: bot_test_helper.py
"""
import pytest
import json
from agile_bot.src.cli.cli_session import CLISession
from agile_bot.test.domain.bot_test_helper import (
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
    # Try to parse as single JSON object first
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        # If that fails, try to find first valid JSON object
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


class TestViewInstructionsInTTYMode:
    """
    Story: Get Action Instructions Through CLI (TTY Mode)
    
    CLI focus: Instructions command parsing and TTY output format
    Note: 'instructions' command returns empty array. Use 'current' command to re-execute instructions.
    """
    
    def test_user_re_executes_current_instructions(self, tmp_path):
        """
        SCENARIO: User re-executes current instructions - TTY Mode
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current instructions and displays in exact TTY format
              Shows behavior and action instructions, rules, and status section
              Footer shows shape and build bolded
        
        CLI focus: Current command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'build')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'current' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('current')
        
        # THEN: CLI re-executes current instructions in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify INSTRUCTIONS section
        assert 'Behavior Instructions - shape' in output
        assert 'Action Instructions - build' in output
        assert 'build base instructions' in output
        assert 'Rules to follow:' in output
        assert 'verb_noun_format' in output
        
        # Verify CLI STATUS section
        status_section = extract_status_section(output)
        assert 'CLI STATUS section' in status_section
        assert 'Current Position:' in status_section
        assert 'shape.build' in status_section
        assert '➤' in status_section  # Current behavior marker
        assert '➤' in status_section  # Current operation marker
        
        # Verify footer shows shape and build bolded
        footer = extract_footer_section(output)
        assert ('[1mshape[0m' in footer or '**shape**' in footer or
                '\x1b[1mshape\x1b[0m' in footer)  # Bolded
        assert ('[1mbuild[0m' in footer or '**build**' in footer or
                '\x1b[1mbuild\x1b[0m' in footer)  # Bolded


class TestViewInstructionsInPipeMode:
    """
    Story: Get Action Instructions Through CLI (Markdown Mode)
    
    CLI focus: Instructions command parsing and Markdown output format
    """
    
    def test_user_re_executes_current_instructions(self, tmp_path):
        """
        SCENARIO: User re-executes current instructions - Markdown Mode
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current instructions and displays in exact Markdown format
              Shows behavior and action instructions with markdown formatting
              Footer shows shape and build bolded
        
        CLI focus: Current command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'build')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'current' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('current')
        
        # THEN: CLI re-executes current instructions in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify INSTRUCTIONS section in markdown
        assert '## Behavior Instructions - shape' in output
        assert '## Action Instructions - build' in output
        assert 'build base instructions' in output
        assert '**verb_noun_format**' in output or 'verb_noun_format' in output
        
        # Verify CLI STATUS section
        assert '## CLI STATUS section' in output
        assert '**Current Position:** shape.build' in output
        
        # Verify footer shows shape and build bolded
        footer = extract_footer_section(output)
        assert '**shape**' in footer  # Bolded in markdown
        assert '**build**' in footer  # Bolded in markdown


class TestViewInstructionsInJSONMode:
    """
    Story: Get Action Instructions Through CLI (JSON Mode)
    
    CLI focus: Instructions command parsing and JSON output format
    """
    
    def test_user_re_executes_current_instructions(self, tmp_path):
        """
        SCENARIO: User re-executes current instructions - JSON Mode
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current instructions and displays in exact JSON format
              Shows instructions JSON object with base_instructions, rules, behavior/action metadata
              Shows bot JSON object with current_behavior
        
        CLI focus: Current command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'build')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'current' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('current')
        
        # THEN: CLI re-executes current instructions in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify instructions JSON object exists (first JSON object)
        instructions_data = assert_valid_json(output)
        assert isinstance(instructions_data, dict)
        assert 'base_instructions' in instructions_data
        assert instructions_data['behavior_metadata']['name'] == 'shape'
        assert instructions_data['action_metadata']['name'] == 'build'
        assert 'rules' in instructions_data
        
        # Verify bot JSON object exists (second JSON object, after first one)
        # Find the end of the first JSON object by parsing it
        first_brace = output.find('{')
        assert first_brace >= 0, "Should find start of first JSON object"
        # Parse first JSON object to find where it ends
        brace_count = 0
        first_json_end = -1
        for i in range(first_brace, len(output)):
            if output[i] == '{':
                brace_count += 1
            elif output[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    first_json_end = i + 1
                    break
        assert first_json_end > 0, f"Should find end of first JSON object. Output length: {len(output)}, first_brace: {first_brace}"
        assert first_json_end < len(output), f"First JSON object should end before output ends. first_json_end: {first_json_end}, output length: {len(output)}"
        remaining = output[first_json_end:].strip()
        assert remaining.startswith('{'), f"Second JSON object should start with {{. Remaining starts with: {repr(remaining[:20])}"
        bot_start = remaining.find('{')
        assert bot_start >= 0, "Should find start of second JSON object"
        bot_data = assert_valid_json(remaining[bot_start:])
        assert bot_data['current_behavior'] == 'shape'


class TestConfirmWithParametersInTTYMode:
    """
    Story: Confirm Work Through CLI (TTY Mode)
    
    CLI focus: Confirm command parsing and TTY output format
    """
    
    def test_user_confirms_build_work(self, tmp_path):
        """
        SCENARIO: User confirms build work - TTY Mode
        GIVEN: CLI is at shape.validate
        WHEN: user enters 'confirm'
        THEN: CLI parses confirm command
              CLI processes work and shows result in exact TTY format
              May show error if prerequisites not met (e.g., story graph not found)
        
        CLI focus: Confirm command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'confirm' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('confirm')
        
        # THEN: CLI processed confirm in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify exact TTY format - confirm command returns error when story graph not found
        assert 'Error' in output or 'error' in output.lower()
        assert 'story graph' in output.lower() or 'story-graph.json' in output.lower() or 'not found' in output.lower()


class TestConfirmWithParametersInPipeMode:
    """
    Story: Confirm Work Through CLI (Markdown Mode)
    
    CLI focus: Confirm command parsing and Markdown output format
    """
    
    def test_user_confirms_build_work(self, tmp_path):
        """
        SCENARIO: User confirms build work - Markdown Mode
        GIVEN: CLI is at shape.validate
        WHEN: user enters 'confirm'
        THEN: CLI parses confirm command
              CLI processes work and shows result in exact Markdown format
              May show error JSON if prerequisites not met
        
        CLI focus: Confirm command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'confirm' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('confirm')
        
        # THEN: CLI processed confirm in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify exact Markdown format - confirm command returns error JSON when story graph not found
        assert '```json' in output or '{' in output
        assert '"status": "error"' in output or '"status":"error"' in output
        assert 'message' in output.lower()


class TestConfirmWithParametersInJSONMode:
    """
    Story: Confirm Work Through CLI (JSON Mode)
    
    CLI focus: Confirm command parsing and JSON output format
    """
    
    def test_user_confirms_build_work(self, tmp_path):
        """
        SCENARIO: User confirms build work - JSON Mode
        GIVEN: CLI is at shape.validate
        WHEN: user enters 'confirm'
        THEN: CLI parses confirm command
              CLI processes work and shows result in exact JSON format
              Shows error JSON with status="error" and message if prerequisites not met
        
        CLI focus: Confirm command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'confirm' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('confirm')
        
        # THEN: CLI processed confirm in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify exact JSON format - confirm command returns error JSON when story graph not found
        confirm_data = assert_valid_json(output)
        assert isinstance(confirm_data, dict)
        assert confirm_data['status'] == 'error'
        assert 'message' in confirm_data
        assert 'story graph' in confirm_data['message'].lower() or 'story-graph.json' in confirm_data['message'].lower()


class TestReExecuteCurrentActionInTTYMode:
    """
    Story: Re-execute Current Operation (TTY Mode)
    
    CLI focus: Current command parsing and TTY output format
    """
    
    def test_user_re_executes_current_instructions(self, tmp_path):
        """
        SCENARIO: User re-executes current instructions - TTY Mode
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current instructions in exact TTY format
              Shows behavior and action instructions, rules, and status section
              Footer shows shape and build bolded
        
        CLI focus: Current command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'build')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'current' via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('current')
        
        # THEN: CLI re-executes current instructions in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify INSTRUCTIONS section
        assert 'Behavior Instructions - shape' in output
        assert 'Action Instructions - build' in output
        assert 'build base instructions' in output
        assert 'Rules to follow:' in output
        
        # Verify CLI STATUS section
        status_section = extract_status_section(output)
        assert 'Current Position:' in status_section
        assert 'shape.build' in status_section
        assert '➤' in status_section  # Current behavior marker
        assert '➤' in status_section  # Current operation marker
        
        # Verify footer shows shape and build bolded
        footer = extract_footer_section(output)
        assert ('[1mshape[0m' in footer or '**shape**' in footer or
                '\x1b[1mshape\x1b[0m' in footer)  # Bolded
        assert ('[1mbuild[0m' in footer or '**build**' in footer or
                '\x1b[1mbuild\x1b[0m' in footer)  # Bolded


class TestReExecuteCurrentActionInPipeMode:
    """
    Story: Re-execute Current Operation (Markdown Mode)
    
    CLI focus: Current command parsing and Markdown output format
    """
    
    def test_user_re_executes_current_instructions(self, tmp_path):
        """
        SCENARIO: User re-executes current instructions - Markdown Mode
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current instructions in exact Markdown format
              Shows behavior and action instructions with markdown formatting
              Footer shows shape and build bolded
        
        CLI focus: Current command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'build')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'current' via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('current')
        
        # THEN: CLI re-executes current instructions in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify INSTRUCTIONS section in markdown
        assert '## Behavior Instructions - shape' in output
        assert '## Action Instructions - build' in output
        assert 'build base instructions' in output
        
        # Verify CLI STATUS section
        assert '## CLI STATUS section' in output
        assert '**Current Position:** shape.build' in output
        
        # Verify footer shows shape and build bolded
        footer = extract_footer_section(output)
        assert '**shape**' in footer  # Bolded in markdown
        assert '**build**' in footer  # Bolded in markdown


class TestReExecuteCurrentActionInJSONMode:
    """
    Story: Re-execute Current Operation (JSON Mode)
    
    CLI focus: Current command parsing and JSON output format
    """
    
    def test_user_re_executes_current_instructions(self, tmp_path):
        """
        SCENARIO: User re-executes current instructions - JSON Mode
        GIVEN: CLI is at shape.build.instructions
        WHEN: user enters 'current'
        THEN: CLI re-executes current instructions in exact JSON format
              Shows instructions JSON object with base_instructions, rules, behavior/action metadata
              Shows bot JSON object with current_behavior
        
        CLI focus: Current command parsing and exact format verification
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'build')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'current' via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('current')
        
        # THEN: CLI re-executes current instructions in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify instructions JSON object exists (first JSON object)
        instructions_data = assert_valid_json(output)
        assert isinstance(instructions_data, dict)
        assert 'base_instructions' in instructions_data
        assert instructions_data['behavior_metadata']['name'] == 'shape'
        assert instructions_data['action_metadata']['name'] == 'build'
        assert 'rules' in instructions_data
        
        # Verify bot JSON object exists (second JSON object, after INSTRUCTIONS separator if present)
        # Find the end of the first JSON object by finding matching closing brace
        first_brace = output.find('{')
        assert first_brace >= 0, "Should find start of first JSON object"
        brace_count = 0
        first_json_end = -1
        for i in range(first_brace, len(output)):
            if output[i] == '{':
                brace_count += 1
            elif output[i] == '}':
                brace_count -= 1
                if brace_count == 0:
                    first_json_end = i + 1
                    break
        assert first_json_end > 0, "Should find end of first JSON object"
        assert first_json_end < len(output), "First JSON object should end before output ends"
        remaining = output[first_json_end:].strip()
        assert remaining.startswith('{'), "Second JSON object should start with {"
        bot_start = remaining.find('{')
        assert bot_start >= 0, "Should find start of second JSON object"
        bot_data = assert_valid_json(remaining[bot_start:])
        assert bot_data['current_behavior'] == 'shape'


class TestHandleErrorsAndValidationInTTYMode:
    """
    Story: Handle Operation Errors (TTY Mode)
    
    CLI focus: Error handling and validation in TTY format
    """
    
    def test_user_enters_invalid_command(self, tmp_path):
        """
        SCENARIO: User enters invalid command - TTY Mode
        GIVEN: CLI is running
        WHEN: user enters invalid command
        THEN: CLI detects error and displays error message in TTY format
        
        CLI focus: Error handling
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters invalid command via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('invalid_command_xyz')
        
        # THEN: CLI shows error message in TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'ERROR' in cli_response.output or 'error' in cli_response.output.lower() or cli_response.status == 'error'


class TestHandleErrorsAndValidationInPipeMode:
    """
    Story: Handle Operation Errors (Markdown Mode)
    
    CLI focus: Error handling and validation in Markdown format
    """
    
    def test_user_enters_invalid_command(self, tmp_path):
        """
        SCENARIO: User enters invalid command - Markdown Mode
        GIVEN: CLI is running
        WHEN: user enters invalid command
        THEN: CLI detects error and displays error message in Markdown format
        
        CLI focus: Error handling
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters invalid command via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('invalid_command_xyz')
        
        # THEN: CLI shows error message in Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'ERROR' in cli_response.output or 'error' in cli_response.output.lower() or cli_response.status == 'error'


class TestHandleErrorsAndValidationInJSONMode:
    """
    Story: Handle Operation Errors (JSON Mode)
    
    CLI focus: Error handling and validation in JSON format
    """
    
    def test_user_enters_invalid_command(self, tmp_path):
        """
        SCENARIO: User enters invalid command - JSON Mode
        GIVEN: CLI is running
        WHEN: user enters invalid command
        THEN: CLI detects error and displays error message in JSON format
        
        CLI focus: Error handling
        """
        # GIVEN
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters invalid command via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('invalid_command_xyz')
        
        # THEN: CLI shows error message in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        output = cli_response.output
        
        # Verify exact JSON format for error
        error_data = assert_valid_json(output)
        assert 'error' in str(error_data).lower() or cli_response.status == 'error'
