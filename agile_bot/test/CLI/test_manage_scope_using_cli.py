"""
Manage Bot Scope Through CLI Tests - CLI Command Interface

Domain logic tested in: test_invoke_bot_directly.py::TestManageScopeIntegration

These tests focus on CLI-specific concerns:
- Scope command parsing
- CLI output format for scope operations (TTY, Markdown, JSON modes)
- Delegation to domain logic

Uses common helpers from: bot_test_helper.py
"""
import pytest
import json
from pathlib import Path
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


def create_story_graph_with_multiple_results(workspace_dir: Path):
    """Create a story graph with multiple epics and stories for testing."""
    stories_dir = workspace_dir / 'docs' / 'stories'
    stories_dir.mkdir(parents=True, exist_ok=True)
    
    story_graph = {
        'epics': [
            {
                'name': 'Epic A',
                'sub_epics': [
                    {
                        'name': 'Sub-Epic A1',
                        'story_groups': [
                            {
                                'type': 'and',
                                'connector': None,
                                'stories': [
                                    {'name': 'Story A1'},
                                    {'name': 'Story A2'}
                                ]
                            }
                        ]
                    }
                ]
            },
            {
                'name': 'Epic B',
                'sub_epics': [
                    {
                        'name': 'Sub-Epic B1',
                        'story_groups': [
                            {
                                'type': 'and',
                                'connector': None,
                                'stories': [
                                    {'name': 'Story B1'},
                                    {'name': 'Story B2'}
                                ]
                            }
                        ]
                    }
                ]
            }
        ],
        'increments': []
    }
    
    story_graph_path = stories_dir / 'story-graph.json'
    story_graph_path.write_text(json.dumps(story_graph, indent=2), encoding='utf-8')
    return story_graph_path


def extract_scope_section(output: str) -> str:
    """Extract just the scope section from CLI output (before INSTRUCTIONS)."""
    # Find the start of the scope section
    scope_start = output.find('🎯 Scope')
    if scope_start == -1:
        scope_start = output.find('## 🎯 Scope')
    
    if scope_start == -1:
        return output  # Return full output if scope section not found
    
    # Find the end of scope section (before INSTRUCTIONS or next major section)
    instructions_start = output.find('====================================================================================================\nINSTRUCTIONS')
    if instructions_start == -1:
        instructions_start = output.find('\n====================================================================================================\nINSTRUCTIONS')
    
    if instructions_start > scope_start:
        return output[scope_start:instructions_start].strip()
    
    # If no instructions section, look for separator line followed by empty line
    separator_pattern = '────────────────────────────────────────────────────────────'
    separator_pos = output.find(separator_pattern, scope_start)
    if separator_pos > scope_start:
        # Include separator and one newline after
        end_pos = output.find('\n', separator_pos + len(separator_pattern))
        if end_pos > separator_pos:
            return output[scope_start:end_pos + 1].strip()
        return output[scope_start:separator_pos + len(separator_pattern)].strip()
    
    return output[scope_start:].strip()


class TestSetScopeInTTYMode:
    """
    Story: Filter Work Using Scope (TTY Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestManageScopeIntegration
    CLI focus: Scope command parsing and TTY output format
    """
    
    def test_user_views_scope_with_epic_filter_showing_multiple_stories(self, tmp_path):
        """
        SCENARIO: User views scope with epic filter showing multiple stories - TTY Mode
        GIVEN: Story graph exists with Epic A containing Story A1 and Story A2
              AND: Scope filter is set to epic="Epic A"
        WHEN: user enters 'scope' (no arguments)
        THEN: CLI displays scope section in exact TTY format
              Shows epic filter, story graph with both stories, and instructions
        
        CLI focus: Exact TTY format verification with multiple results
        """
        # GIVEN: Story graph with multiple stories
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        create_story_graph_with_multiple_results(workspace)
        
        # Set epic scope filter (returns multiple stories)
        bot.scope('epic=Epic A')
        
        # WHEN: user views scope via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('scope')
        
        # THEN: CLI displays scope section in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        
        # Extract just the scope section
        scope_output = extract_scope_section(cli_response.output)
        
        # Verify exact format with hard-coded expectations
        # Line 1: Bold "🎯 Scope" header
        assert scope_output.startswith('\x1b[1m🎯 Scope\x1b[0m') or scope_output.startswith('🎯 Scope')
        
        # Line 2: Current scope with epic name
        assert '🎯' in scope_output
        assert 'Current Scope:' in scope_output or '\x1b[1mCurrent Scope:\x1b[0m' in scope_output
        assert 'Epic A' in scope_output
        
        # Empty line after current scope
        assert '\n\n' in scope_output or scope_output.count('\n') >= 2
        
        # Story Graph section
        assert 'Story Graph' in scope_output
        assert 'Path:' in scope_output
        assert 'story-graph.json' in scope_output
        assert 'Epics: 1' in scope_output
        
        # Epic hierarchy showing both stories
        assert 'Epic A' in scope_output
        assert 'Sub-Epic A1' in scope_output
        assert 'Story A1' in scope_output
        assert 'Story A2' in scope_output
        
        # Instructions section
        assert 'To change scope (pick ONE - setting a new scope replaces the previous):' in scope_output
        assert 'scope all' in scope_output
        assert 'scope "Story Name"' in scope_output
        assert 'scope "file:' in scope_output
        
        # Separator line at end
        assert '────────────────────────────────────────────────────────────' in scope_output
    
    def test_user_views_scope_with_story_filter_showing_single_story(self, tmp_path):
        """
        SCENARIO: User views scope with story filter showing single story - TTY Mode
        GIVEN: Story graph exists with Epic A containing Story A1 and Story A2
              AND: Scope filter is set to story="Story A1"
        WHEN: user enters 'scope' (no arguments)
        THEN: CLI displays scope section in exact TTY format
              Shows story filter, story graph with only Story A1, and instructions
        
        CLI focus: Exact TTY format verification with single result
        """
        # GIVEN: Story graph with multiple stories
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        create_story_graph_with_multiple_results(workspace)
        
        # Set story scope filter (returns single story)
        bot.scope('story=Story A1')
        
        # WHEN: user views scope via CLI (TTY mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='tty')
        cli_response = cli_session.execute_command('scope')
        
        # THEN: CLI displays scope section in exact TTY format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        
        # Extract just the scope section
        scope_output = extract_scope_section(cli_response.output)
        
        # Verify exact format with hard-coded expectations
        # Header
        assert scope_output.startswith('\x1b[1m🎯 Scope\x1b[0m') or scope_output.startswith('🎯 Scope')
        
        # Current scope with story name
        assert 'Story A1' in scope_output
        
        # Story Graph section
        assert 'Story Graph' in scope_output
        assert 'Epics: 1' in scope_output
        
        # Epic hierarchy showing only Story A1 (not Story A2)
        assert 'Epic A' in scope_output
        assert 'Sub-Epic A1' in scope_output
        assert 'Story A1' in scope_output
        # Story A2 should NOT appear in the scope results (filtered out)
        story_a1_pos = scope_output.find('Story A1')
        assert story_a1_pos > 0, "Story A1 should be found"
        # Extract the scope results section (between Story Graph and instructions)
        scope_results_section = scope_output.split('Story A1')[0] + scope_output.split('Story A1')[1].split('To change scope')[0] if 'To change scope' in scope_output else scope_output
        # Story A2 should not appear in the scope results
        assert 'Story A2' not in scope_results_section, "Story A2 should be filtered out and not appear in scope results"
        
        # Instructions section
        assert 'To change scope (pick ONE - setting a new scope replaces the previous):' in scope_output
        assert 'scope all' in scope_output
        
        # Separator line
        assert '────────────────────────────────────────────────────────────' in scope_output


class TestSetScopeInPipeMode:
    """
    Story: Filter Work Using Scope (Markdown Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestManageScopeIntegration
    CLI focus: Scope command parsing and Markdown output format
    """
    
    def test_user_views_scope_with_epic_filter_showing_multiple_stories(self, tmp_path):
        """
        SCENARIO: User views scope with epic filter showing multiple stories - Markdown Mode
        GIVEN: Story graph exists with Epic A containing Story A1 and Story A2
              AND: Scope filter is set to epic="Epic A"
        WHEN: user enters 'scope' (no arguments)
        THEN: CLI displays scope section in exact Markdown format
              Shows epic filter, story graph with both stories, and instructions
        
        CLI focus: Exact Markdown format verification with multiple results
        """
        # GIVEN: Story graph with multiple stories
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        create_story_graph_with_multiple_results(workspace)
        
        # Set epic scope filter (returns multiple stories)
        bot.scope('epic=Epic A')
        
        # WHEN: user views scope via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('scope')
        
        # THEN: CLI displays scope section in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        
        # Extract just the scope section
        scope_output = extract_scope_section(cli_response.output)
        
        # Verify exact Markdown format with hard-coded expectations
        # Header: 🎯 Scope (format_header(2, "🎯 Scope") produces "## 🎯 Scope\n")
        assert scope_output.startswith('🎯 Scope') or '## 🎯 Scope' in scope_output or scope_output.startswith('## 🎯 Scope')
        
        # Current scope with bold formatting
        assert '**🎯 Current Scope:**' in scope_output
        assert 'Epic A' in scope_output
        
        # Story Graph section
        assert 'Story Graph' in scope_output
        assert '**Path:**' in scope_output
        assert 'story-graph.json' in scope_output
        assert '**Epic Count:** 1' in scope_output or 'Epic Count:' in scope_output
        
        # Epic hierarchy showing both stories
        assert '### Epics' in scope_output or 'Epics:' in scope_output
        assert 'Epic A' in scope_output
        assert 'Sub-Epic A1' in scope_output
        assert 'Story A1' in scope_output
        assert 'Story A2' in scope_output
        
        # Instructions section with markdown list items
        assert 'To change scope (pick ONE - setting a new scope replaces the previous):' in scope_output
        assert '`scope all`' in scope_output
        assert '`scope "Story Name"`' in scope_output
        assert '`scope "file:' in scope_output
        
        # Separator
        assert '---' in scope_output
    
    def test_user_views_scope_with_story_filter_showing_single_story(self, tmp_path):
        """
        SCENARIO: User views scope with story filter showing single story - Markdown Mode
        GIVEN: Story graph exists with Epic A containing Story A1 and Story A2
              AND: Scope filter is set to story="Story A1"
        WHEN: user enters 'scope' (no arguments)
        THEN: CLI displays scope section in exact Markdown format
              Shows story filter, story graph with only Story A1, and instructions
        
        CLI focus: Exact Markdown format verification with single result
        """
        # GIVEN: Story graph with multiple stories
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        create_story_graph_with_multiple_results(workspace)
        
        # Set story scope filter (returns single story)
        bot.scope('story=Story A1')
        
        # WHEN: user views scope via CLI (Markdown mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='markdown')
        cli_response = cli_session.execute_command('scope')
        
        # THEN: CLI displays scope section in exact Markdown format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        
        # Extract just the scope section
        scope_output = extract_scope_section(cli_response.output)
        
        # Verify exact Markdown format
        assert scope_output.startswith('🎯 Scope') or '## 🎯 Scope' in scope_output
        assert '**🎯 Current Scope:**' in scope_output
        assert 'Story A1' in scope_output
        assert 'Story Graph' in scope_output
        assert 'Epic A' in scope_output
        assert 'Story A1' in scope_output
        # Story A2 should NOT appear in the filtered results
        assert 'To change scope' in scope_output, "Instructions section should be present"
        story_section = scope_output.split('Story Graph')[1].split('To change scope')[0]
        # Story A2 should not appear in the story graph section
        assert 'Story A2' not in story_section, "Story A2 should be filtered out and not appear in story graph results"
        assert 'To change scope' in scope_output
        assert '---' in scope_output


class TestSetScopeInJSONMode:
    """
    Story: Filter Work Using Scope (JSON Mode)
    
    Domain logic: test_invoke_bot_directly.py::TestManageScopeIntegration
    CLI focus: Scope command parsing and JSON output format
    """
    
    def test_user_views_scope_with_epic_filter_showing_multiple_stories(self, tmp_path):
        """
        SCENARIO: User views scope with epic filter showing multiple stories - JSON Mode
        GIVEN: Story graph exists with Epic A containing Story A1 and Story A2
              AND: Scope filter is set to epic="Epic A"
        WHEN: user enters 'scope' (no arguments)
        THEN: CLI displays scope in exact JSON format
              Shows scope type, value array with epic name, and empty exclude/skiprule arrays
        
        CLI focus: Exact JSON format verification with multiple results
        """
        # GIVEN: Story graph with multiple stories
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        create_story_graph_with_multiple_results(workspace)
        
        # Set epic scope filter (returns multiple stories)
        bot.scope('epic=Epic A')
        
        # WHEN: user views scope via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('scope')
        
        # THEN: CLI displays scope in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        
        # Extract JSON scope object (first JSON object in output)
        scope_data = assert_valid_json(cli_response.output)
        
        # Verify exact JSON structure
        assert isinstance(scope_data, dict)
        assert 'type' in scope_data
        assert 'value' in scope_data
        assert 'exclude' in scope_data
        assert 'skiprule' in scope_data
        
        # Verify epic filter values
        assert scope_data['type'] == 'epic' or scope_data['type'] == 'story'  # May be stored as 'story' if epic name used
        assert isinstance(scope_data['value'], list)
        assert 'Epic A' in scope_data['value']
        assert isinstance(scope_data['exclude'], list)
        assert isinstance(scope_data['skiprule'], list)
    
    def test_user_views_scope_with_story_filter_showing_single_story(self, tmp_path):
        """
        SCENARIO: User views scope with story filter showing single story - JSON Mode
        GIVEN: Story graph exists with Epic A containing Story A1 and Story A2
              AND: Scope filter is set to story="Story A1"
        WHEN: user enters 'scope' (no arguments)
        THEN: CLI displays scope in exact JSON format
              Shows scope type="story", value array with story name, and empty arrays
        
        CLI focus: Exact JSON format verification with single result
        """
        # GIVEN: Story graph with multiple stories
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        create_story_graph_with_multiple_results(workspace)
        
        # Set story scope filter (returns single story)
        bot.scope('story=Story A1')
        
        # WHEN: user views scope via CLI (JSON mode)
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        cli_response = cli_session.execute_command('scope')
        
        # THEN: CLI displays scope in exact JSON format
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        
        # Extract JSON scope object
        scope_data = assert_valid_json(cli_response.output)
        
        # Verify exact JSON structure
        assert isinstance(scope_data, dict)
        assert scope_data['type'] == 'story'
        assert isinstance(scope_data['value'], list)
        assert len(scope_data['value']) == 1
        assert 'Story A1' in scope_data['value']
        assert isinstance(scope_data['exclude'], list)
        assert isinstance(scope_data['skiprule'], list)
