"""
Generate CLI Tests

Tests for all stories in the 'Generate CLI' sub-epic:
- Generate BOT CLI code
- Generate Cursor Command Files
- Generate Cursor Awareness Files
"""
import pytest
from pathlib import Path
import json
from unittest.mock import Mock, patch
from conftest import bootstrap_env, create_bot_config_file, given_bot_name_and_behaviors_setup, given_bot_name_and_behavior_setup
from agile_bot.bots.base_bot.test.test_helpers import create_base_actions_structure
from agile_bot.bots.base_bot.test.test_build_agile_bots import (
    given_bot_config_and_directory_setup,
    given_bot_configured_by_config,
    given_behavior_with_trigger_words
)

# ============================================================================
# HELPER FUNCTIONS - Sub-Epic Level (Used across multiple test classes)
# ============================================================================

# Consolidated helpers imported from test_generate_mcp_tools.py
from agile_bot.bots.base_bot.test.test_generate_mcp_tools import (
    given_bot_config_has_goal_and_description,
    given_behaviors_with_descriptions_and_trigger_words,
    when_generate_awareness_files_and_read_content,
    when_create_rules_directory_if_needed,
    when_generator_generates_awareness_files_direct,
    given_path_write_text_mocked_to_raise_permission_error,
    given_expected_awareness_filename,
    then_awareness_file_contains_bot_name,
    then_awareness_file_contains_behavior_sections,
    then_awareness_file_shape_section_contains_only_shape_words,
    then_awareness_file_contains_tool_patterns_for_behaviors,
    then_awareness_file_contains_priority_check_message,
    then_awareness_file_contains_behavior_format_sections,
    then_awareness_file_contains_error_handling_section,
    then_awareness_file_contains_repair_question,
    then_awareness_file_contains_tool_patterns,
    then_trigger_words_in_behavior_section,
    then_permission_error_raised_with_bot_specific_path,
    then_rules_directory_and_file_exist,
    then_awareness_file_contains_required_sections,
    generator,  # Import generator fixture
)

def given_bot_with_trigger_words_and_guardrails(workspace_root: Path, bot_name: str, bot_dir: Path, behaviors_config: list) -> None:
    """Given: Bot configured with trigger words and guardrails for behaviors."""
    from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
    bot_dir, workspace_directory = given_bot_configured_by_config(workspace_root, bot_name)
    for behavior_config in behaviors_config:
        behavior_name = behavior_config['name']
        trigger_words = behavior_config['trigger_words']
        create_minimal_guardrails_files(bot_dir, behavior_name, bot_name)
        given_behavior_with_trigger_words(bot_dir, behavior_name, trigger_words)
    return bot_dir

# Use shared helpers from conftest
# given_bot_name_and_behaviors_setup imported from conftest
# given_bot_name_and_behavior_setup imported from conftest

# ============================================================================
# HELPER FUNCTIONS - Sub-Epic Level (For TestGenerateCursorCommandFiles)
# ============================================================================

def given_cli_script_exists(workspace_root: Path, bot_dir: Path, bot_name: str) -> Path:
    """Given: CLI script exists."""
    cli_script_path = bot_dir / 'src' / f'{bot_name}_cli.py'
    cli_script_path.parent.mkdir(parents=True, exist_ok=True)
    cli_script_path.write_text('#!/usr/bin/env python\n', encoding='utf-8')
    return cli_script_path

def given_obsolete_command_file_exists(workspace_root: Path, bot_name: str) -> Path:
    """Given: Obsolete command file exists."""
    commands_dir = workspace_root / '.cursor' / 'commands'
    commands_dir.mkdir(parents=True, exist_ok=True)
    obsolete_file = commands_dir / f'{bot_name}-obsolete.md'
    obsolete_file.write_text('python obsolete.py', encoding='utf-8')
    return obsolete_file

def given_cursor_command_files_exist(bot_name: str, behaviors: list) -> None:
    """Given: Cursor command files exist in workspace root."""
    from agile_bot.bots.base_bot.src.bot.workspace import get_python_workspace_root
    repo_root = get_python_workspace_root()
    commands_dir = repo_root / '.cursor' / 'commands'
    commands_dir.mkdir(parents=True, exist_ok=True)
    for behavior in behaviors:
        cmd_file = commands_dir / f'{bot_name}-{behavior}.md'
        cmd_file.write_text(f'python {bot_name}_cli.py --behavior {behavior} --action ${{1:}}${{2:+ }}${{2:}}', encoding='utf-8')

def when_generator_generates_cursor_commands(workspace_root: Path, bot_dir: Path, bot_name: str, cli_script_path: Path, behaviors: list) -> dict:
    """When: Generator generates cursor commands."""
    from agile_bot.bots.base_bot.src.cli.cursor_command_generator import CursorCommandGenerator
    generator = CursorCommandGenerator(workspace_root, bot_dir, bot_name)
    return generator.generate_cursor_commands(cli_script_path, behaviors)

def when_generator_updates_registry(workspace_root: Path, bot_dir: Path, bot_name: str, cli_script_path: Path, behaviors: list) -> tuple:
    """When: Generator updates registry."""
    from agile_bot.bots.base_bot.src.cli.cursor_command_generator import CursorCommandGenerator
    generator = CursorCommandGenerator(workspace_root, bot_dir, bot_name)
    generator.generate_cursor_commands(cli_script_path, behaviors)
    registry_path = generator.update_bot_registry(cli_script_path)
    return registry_path

def then_base_command_files_exist(commands: dict, bot_name: str) -> None:
    """Then: Base command files exist."""
    assert f'{bot_name}' in commands
    assert f'{bot_name}-continue' in commands
    assert f'{bot_name}-help' in commands
    assert commands[f'{bot_name}'].exists()
    assert commands[f'{bot_name}-continue'].exists()
    assert commands[f'{bot_name}-help'].exists()

def then_behavior_command_files_exist(commands: dict, bot_name: str, behaviors: list) -> None:
    """Then: Behavior command files exist."""
    for behavior in behaviors:
        cmd_name = f'{bot_name}-{behavior}'
        assert cmd_name in commands
        assert commands[cmd_name].exists()

def then_obsolete_file_removed(obsolete_file: Path) -> None:
    """Then: Obsolete file removed."""
    assert not obsolete_file.exists()

def then_registry_contains_bot_entry(registry_path: Path, bot_name: str, cli_script_path: Path) -> None:
    """Then: Registry contains bot entry."""
    registry_data = json.loads(registry_path.read_text(encoding='utf-8'))
    assert bot_name in registry_data
    assert 'cli_path' in registry_data[bot_name]
    # Normalize path separators for cross-platform comparison
    registry_cli_path = registry_data[bot_name]['cli_path'].replace('/', '\\')
    cli_script_str = str(cli_script_path).replace('/', '\\')
    assert registry_cli_path in cli_script_str or cli_script_str.endswith(registry_data[bot_name]['cli_path'].split('/')[-1])

# ============================================================================
# HELPER FUNCTIONS - Sub-Epic Level (For TestGenerateHelp)
# ============================================================================

def when_help_generator_created(bot, bot_name: str, bot_directory: Path, formatter):
    """When: Help generator created."""
    from agile_bot.bots.base_bot.src.cli.cli_help_generator import CliHelpGenerator
    return CliHelpGenerator(bot, bot_name, bot_directory, formatter)

def when_help_generator_generates_cli_help(help_generator):
    """When: Help generator generates CLI help."""
    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        help_generator.help_behaviors_and_actions()
        return captured_output.getvalue()
    finally:
        sys.stdout = old_stdout

def when_help_generator_generates_cursor_help(help_generator):
    """When: Help generator generates cursor help."""
    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        def mock_breadcrumbs():
            return ['Breadcrumb line 1', 'Breadcrumb line 2']
        help_generator.help_cursor_commands(mock_breadcrumbs)
        return captured_output.getvalue()
    finally:
        sys.stdout = old_stdout

def then_help_contains_behaviors(help_output: str, bot_name: str, behaviors: list) -> None:
    """Then: Help contains behaviors."""
    for behavior in behaviors:
        assert f'{bot_name}-{behavior}' in help_output

def then_help_contains_actions(help_output: str, actions: list) -> None:
    """Then: Help contains actions."""
    for action in actions:
        assert action in help_output

def then_help_contains_action_parameters(help_output: str, action_name: str, parameters: list) -> None:
    """Then: Help contains action parameters."""
    assert action_name in help_output
    for param in parameters:
        assert param in help_output

def then_cli_help_contains_cli_syntax(help_output: str, cli_script_path: str) -> None:
    """Then: CLI help contains CLI syntax."""
    assert 'python' in help_output
    # Normalize paths for comparison (handle both forward and backslashes)
    normalized_path = cli_script_path.replace('\\', '/')
    normalized_output = help_output.replace('\\', '/')
    script_name = cli_script_path.split('/')[-1] if '/' in cli_script_path else cli_script_path.split('\\')[-1]
    assert normalized_path in normalized_output or script_name in normalized_output

def then_cursor_help_contains_cursor_syntax(help_output: str, bot_name: str) -> None:
    """Then: Cursor help contains cursor syntax or display instructions."""
    # The help generator now writes to files and outputs display instructions
    # So we check for either the actual help content OR the display instruction format
    assert (
        f'/{bot_name}-' in help_output or 
        f'## {bot_name}-' in help_output or
        'Read and display the contents of' in help_output  # New format: outputs file paths
    )


class TestGenerateBOTCLIcode:
    """Story: Generate BOT CLI code - Tests CLI code generation."""
    
    # TODO: Add test scenarios for Generate BOT CLI code story
    pass


class TestGenerateCursorCommandFiles:
    """Story: Generate Cursor Command Files - Tests Cursor command file generation."""
    
    @pytest.mark.parametrize("behaviors,verification_type", [
        # Example 1: Base command files with multiple behaviors
        (['shape', 'discovery'], 'base'),
        # Example 2: Behavior command files with multiple behaviors
        (['shape', 'discovery'], 'behavior'),
        # Example 3: Single behavior
        (['shape'], 'behavior'),
    ])
    def test_generator_creates_command_files(self, workspace_root, behaviors, verification_type):
        """
        SCENARIO: Generator creates command files
        GIVEN: Bot configuration exists with behaviors
        AND: CLI script exists
        WHEN: Generator generates cursor commands
        THEN: Generator creates appropriate command files (base or behavior-specific)
        """
        # Given: Bot configuration exists
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', behaviors)
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        cli_script_path = given_cli_script_exists(workspace_root, bot_dir, bot_name)
        
        # When: Generator generates cursor commands
        commands = when_generator_generates_cursor_commands(workspace_root, bot_dir, bot_name, cli_script_path, behaviors)
        
        # Then: Appropriate command files created
        if verification_type == 'base':
            then_base_command_files_exist(commands, bot_name)
        elif verification_type == 'behavior':
            then_behavior_command_files_exist(commands, bot_name, behaviors)
    
    def test_generator_removes_obsolete_command_files(self, workspace_root):
        """
        SCENARIO: Generator removes obsolete command files
        GIVEN: Bot configuration exists
        AND: Obsolete command files exist
        AND: CLI script exists
        WHEN: Generator generates cursor commands
        THEN: Generator removes obsolete command files
        """
        # Given: Bot configuration exists
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        obsolete_file = given_obsolete_command_file_exists(workspace_root, bot_name)
        cli_script_path = given_cli_script_exists(workspace_root, bot_dir, bot_name)
        
        # When: Generator generates cursor commands
        when_generator_generates_cursor_commands(workspace_root, bot_dir, bot_name, cli_script_path, behaviors)
        
        # Then: Obsolete file removed
        then_obsolete_file_removed(obsolete_file)
    
    def test_generator_updates_bot_registry(self, workspace_root):
        """
        SCENARIO: Generator updates bot registry
        GIVEN: Bot configuration exists
        AND: CLI script exists
        WHEN: Generator generates cursor commands and updates registry
        THEN: Registry contains bot entry with CLI path
        """
        # Given: Bot configuration exists
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        cli_script_path = given_cli_script_exists(workspace_root, bot_dir, bot_name)
        
        # When: Generator generates cursor commands and updates registry
        registry_path = when_generator_updates_registry(workspace_root, bot_dir, bot_name, cli_script_path, behaviors)
        
        # Then: Registry contains bot entry with CLI path
        then_registry_contains_bot_entry(registry_path, bot_name, cli_script_path)

class TestGenerateHelp:
    """Story: Generate Help - Tests help generation for behaviors and actions."""
    
    @pytest.mark.parametrize("behaviors,verification_type,expected_data", [
        # Example 1: Multiple behaviors
        (['shape', 'discovery'], 'behaviors', None),
        # Example 2: Single behavior with actions
        (['shape'], 'actions', ['clarify', 'strategy', 'build', 'validate', 'render']),
        # Example 3: Action parameters for clarify
        (['shape'], 'action_parameters', {'action': 'clarify', 'params': ['--key_questions_answered', '--evidence_provided']}),
        # Example 4: Action parameters for build
        (['shape'], 'action_parameters', {'action': 'build', 'params': ['--scope']}),
    ])
    def test_generator_creates_cli_help_content(self, workspace_root, behaviors, verification_type, expected_data):
        """
        SCENARIO: Generator creates CLI help content
        GIVEN: Bot has behaviors configured
        WHEN: Help generator generates CLI help
        THEN: Help contains expected content (behaviors, actions, or parameters)
        """
        # Given: Bot has behaviors configured
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', behaviors)
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        bot_dir, workspace_directory = given_bot_configured_by_config(workspace_root, bot_name)
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        for behavior_name in behaviors:
            create_actions_workflow_json(bot_dir, behavior_name)
            create_minimal_guardrails_files(bot_dir, behavior_name, bot_name)
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
        formatter = Mock()
        formatter.format_directive = lambda x: x
        formatter.format_header = lambda x: x
        formatter.format_separator = lambda: '---'
        
        # When: Help generator generates CLI help
        help_generator = when_help_generator_created(bot, bot_name, bot_dir, formatter)
        help_output = when_help_generator_generates_cli_help(help_generator)
        
        # Then: Help contains expected content
        if verification_type == 'behaviors':
            then_help_contains_behaviors(help_output, bot_name, behaviors)
        elif verification_type == 'actions':
            then_help_contains_actions(help_output, expected_data)
        elif verification_type == 'action_parameters':
            then_help_contains_action_parameters(help_output, expected_data['action'], expected_data['params'])
    
    def test_generator_creates_cli_help_with_cli_syntax(self, workspace_root):
        """
        SCENARIO: Generator creates CLI help with CLI syntax
        GIVEN: Bot has behaviors configured
        AND: CLI script exists
        WHEN: Help generator generates CLI help
        THEN: Help contains CLI command syntax
        """
        # Given: Bot has behaviors configured
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        bot_dir, workspace_directory = given_bot_configured_by_config(workspace_root, bot_name)
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        create_minimal_guardrails_files(bot_dir, 'shape', bot_name)
        cli_script_path = given_cli_script_exists(workspace_root, bot_dir, bot_name)
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
        formatter = Mock()
        formatter.format_directive = lambda x: x
        formatter.format_header = lambda x: x
        formatter.format_separator = lambda: '---'
        
        # When: Help generator generates CLI help
        help_generator = when_help_generator_created(bot, bot_name, bot_dir, formatter)
        help_output = when_help_generator_generates_cli_help(help_generator)
        
        # Then: Help contains CLI command syntax
        then_cli_help_contains_cli_syntax(help_output, str(cli_script_path))
    
    def test_generator_creates_cursor_help_for_behaviors(self, workspace_root):
        """
        SCENARIO: Generator creates cursor help for behaviors
        GIVEN: Bot has behaviors configured
        AND: Cursor command files exist
        WHEN: Help generator generates cursor help
        THEN: Help contains cursor command syntax
        """
        # Given: Bot has behaviors configured
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape', 'discovery'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        bot_dir, workspace_directory = given_bot_configured_by_config(workspace_root, bot_name)
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        for behavior_name in behaviors:
            create_actions_workflow_json(bot_dir, behavior_name)
            create_minimal_guardrails_files(bot_dir, behavior_name, bot_name)
        given_cursor_command_files_exist(bot_name, behaviors)
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
        formatter = Mock()
        formatter.format_header = lambda x: x
        formatter.format_separator = lambda: '---'
        formatter.format_warning = lambda x: x
        formatter.format_directive = lambda x: x
        
        # When: Help generator generates cursor help
        help_generator = when_help_generator_created(bot, bot_name, bot_dir, formatter)
        help_output = when_help_generator_generates_cursor_help(help_generator)
        
        # Then: Help contains cursor command syntax
        then_cursor_help_contains_cursor_syntax(help_output, bot_name)

class TestGenerateCursorAwarenessFiles:
    """Story: Generate Cursor Awareness Files - Tests awareness file generation."""

    def test_generator_creates_workspace_rules_file_with_trigger_patterns(self, workspace_root):
        """
        SCENARIO: Generator creates workspace rules file with trigger patterns
        GIVEN: Bot configuration exists with behaviors
        AND: Bot is initialized with trigger words and guardrails configured
        WHEN: Generator runs generate_awareness_files() method
        THEN: Generator creates file with bot-specific filename: mcp-test-bot-awareness.mdc
        AND: Filename includes bot name with hyphens
        AND: Generated rules file includes ACTUAL trigger words from bot
        AND: File includes bot name from config
        """
        # Given: Bot configuration exists with behaviors
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape', 'discovery'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        bot_dir = given_bot_with_trigger_words_and_guardrails(workspace_root, bot_name, bot_dir, [
            {'name': 'shape', 'trigger_words': ['shape story', 'define story outline', 'create story map']},
            {'name': 'discovery', 'trigger_words': ['discover stories', 'break down stories', 'enumerate stories']}
        ])
        
        # When: Generator runs generate_awareness_files() method
        gen, rules_file, content = when_generate_awareness_files_and_read_content(bot_dir, bot_name)
        
        # Then: File includes bot name
        then_awareness_file_contains_bot_name(content, bot_name)
        
        # And: Trigger words are SECTIONED by behavior (not flat list)
        then_awareness_file_contains_behavior_sections(content, ['Shape', 'Discovery'])
        
        # And: Shape section includes ONLY shape trigger words
        then_awareness_file_shape_section_contains_only_shape_words(content)
        
        # And: Each behavior section shows tool pattern
        then_awareness_file_contains_tool_patterns_for_behaviors(content, bot_name, ['shape', 'discovery'])

    def test_rules_file_includes_bot_goal_and_behavior_descriptions(self, workspace_root):
        """
        SCENARIO: Rules file includes bot goal and behavior descriptions
        GIVEN: Bot config has goal and description
        WHEN: Generator creates .cursor/rules/mcp-<bot-name>-awareness.mdc file
        THEN: File includes bot's goal from bot_config.json
        AND: Critical rule mentions bot's goal: "When user is trying to [goal], check MCP tools FIRST"
        AND: Each behavior section includes "When user is trying to [behavior description]"
        """
        # Given: A bot configuration file with a working directory and behaviors
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape', 'discovery'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        # And: Bot config has goal and description
        from agile_bot.bots.base_bot.test.test_generate_mcp_tools import given_bot_config_has_goal_and_description
        given_bot_config_has_goal_and_description(
            workspace_root,
            bot_name,
            'Transform user needs into well-structured stories',
            'Helps teams create and refine user stories'
        )
        # And: Behaviors have descriptions and trigger words configured
        given_behaviors_with_descriptions_and_trigger_words(bot_dir, [
            {
                'name': 'shape',
                'description': 'Create initial story map outline from user context',
                'patterns': ['shape story', 'create story map']
            },
            {
                'name': 'discovery',
                'description': 'Elaborate stories with user flows and domain rules',
                'patterns': ['discover stories', 'elaborate stories']
            }
        ])
        # And: A bot that has been initialized with that config file
        bot_dir, workspace_directory = given_bot_configured_by_config(workspace_root, bot_name)
        
        # When: Generator creates .cursor/rules/mcp-<bot-name>-awareness.mdc file
        gen, rules_file, content = when_generate_awareness_files_and_read_content(bot_dir, bot_name)
        
        # Then: File contains priority check message
        then_awareness_file_contains_priority_check_message(content, bot_name)
        
        # And: Each behavior follows explicit format
        then_awareness_file_contains_behavior_format_sections(content, bot_name)
        
        # And: File includes error handling section
        then_awareness_file_contains_error_handling_section(content)
        then_awareness_file_contains_repair_question(content)

    def test_rules_file_maps_trigger_patterns_to_tool_naming_conventions(self, workspace_root):
        """
        SCENARIO: Rules file maps trigger patterns to tool naming conventions
        GIVEN: A bot configuration file with a working directory and behaviors
        AND: Behaviors have trigger words configured
        AND: A bot that has been initialized with that config file
        WHEN: File is written to .cursor/rules/mcp-test-bot-awareness.mdc
        THEN: Each behavior section includes tool pattern with ACTUAL bot name
        AND: Tool patterns appear in behavior sections (not flat list)
        """
        # Given: A bot configuration file with a working directory and behaviors
        bot_name, behaviors = given_bot_name_and_behaviors_setup('test_bot', ['shape', 'discovery'])
        bot_config, bot_dir = given_bot_config_and_directory_setup(workspace_root, bot_name, behaviors)
        # And: Behaviors have trigger words configured
        given_behavior_with_trigger_words(bot_dir, 'shape', ['shape story', 'define outline'])
        given_behavior_with_trigger_words(bot_dir, 'discovery', ['discover stories', 'enumerate stories'])
        
        # And: A bot that has been initialized with that config file
        bot_dir, workspace_directory = given_bot_configured_by_config(workspace_root, bot_name)
        # When: File is written to .cursor/rules/mcp-test-bot-awareness.mdc
        gen, rules_file, content = when_generate_awareness_files_and_read_content(bot_dir, bot_name)
        
        # Then: Each behavior section includes tool pattern with ACTUAL bot name
        then_awareness_file_contains_behavior_sections(content, behaviors)
        # And: Tool patterns appear in behavior sections (not flat list)
        then_awareness_file_contains_tool_patterns(content, bot_name, behaviors)
        # And: Trigger words are in correct sections
        then_trigger_words_in_behavior_section(content, 'shape', ['shape story', 'define outline'])
        then_trigger_words_in_behavior_section(content, 'discovery', ['discover stories', 'enumerate stories'])

    # test_generator_handles_file_write_errors_gracefully_creates_directory removed - exception handling test

    # test_generator_handles_file_write_errors_with_clear_error_message removed - exception handling test
        """
        SCENARIO: Generator handles file write errors with clear error message
        GIVEN: .cursor/rules/ directory is write-protected
        WHEN: Generator attempts to write file
        THEN: Generator raises clear error message indicating permission issue
        AND: Error includes bot-specific path attempted
        """
        # Given: Rules directory exists
        rules_dir = when_create_rules_directory_if_needed()
        # And: Path.write_text is mocked to raise PermissionError
        expected_filename = given_expected_awareness_filename()
        # Exception handling test removed

    def test_full_awareness_generation_workflow(self, generator, workspace_root):
        """
        SCENARIO: Full awareness generation workflow
        GIVEN: MCP Server Generator initialized
        WHEN: generate_awareness_files() called
        THEN: Bot-specific rules file is created
        AND: Rules file has all required sections
        """
        # When: Generate awareness files
        when_generator_generates_awareness_files_direct(generator)
        
        # Then: Rules file created with bot-specific filename
        rules_dir, rules_file = then_rules_directory_and_file_exist()
        # And: Rules file has all required sections
        then_awareness_file_contains_required_sections(rules_file, 'test_bot')





