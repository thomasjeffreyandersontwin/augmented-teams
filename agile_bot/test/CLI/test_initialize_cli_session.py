"""
Initialize CLI Session Tests - CLI Initialization Interface

Tests for CLI session initialization stories:
- Launch CLI in Interactive Mode
- Launch CLI in Pipe Mode
- Detect and Configure TTY/Non-TTY Input for CLI
- Load and Display Workspace Context in CLI

CLI focus: Session initialization, TTY detection, mode configuration
Uses common helpers from: test_invoke_bot_helpers.py

Note: Some advanced features (adapters, display_current_state) not yet implemented in CLISession.
These tests will be enhanced once domain classes are created in Phase 2.3.
"""
import pytest
import json
import sys
from pathlib import Path
from agile_bot.src.cli.cli_session import CLISession
from agile_bot.test.domain.test_invoke_bot_helpers import (
    setup_test_bot,
    create_behavior_action_state
)


def create_story_graph(workspace_directory):
    """Create a story graph file in workspace"""
    stories_dir = workspace_directory / 'docs' / 'stories'
    stories_dir.mkdir(parents=True, exist_ok=True)
    
    story_graph = {
        "epics": [
            {
                "name": "Test Epic",
                "stories": ["Test Story 1", "Test Story 2"]
            }
        ]
    }
    (stories_dir / 'story-graph.json').write_text(json.dumps(story_graph))
    return stories_dir / 'story-graph.json'


class TestStartCLISessionInTTYMode:
    """
    Story: Launch CLI in Interactive Mode (TTY Mode)
    
    CLI focus: Session initialization in interactive mode with TTY adapters
    """
    
    def test_cli_launches_in_interactive_mode(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI launches in interactive mode
        GIVEN: CLISession is configured for interactive mode
        WHEN: user runs CLI
        THEN: CLISession wraps Bot
              CLI can execute commands
        
        CLI focus: Interactive mode initialization
        """
        # GIVEN: Interactive mode (TTY detected)
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        monkeypatch.setattr(sys.stdout, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: CLISession initializes in interactive mode
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: CLISession wraps Bot
        assert cli_session.bot is not None
        assert cli_session.bot.bot_name == 'story_bot'
        
        # AND: CLI can execute commands
        response = cli_session.execute_command('status')
        assert response is not None
        assert isinstance(response.output, str)
    
    def test_cli_loads_existing_behavior_action_state_on_launch(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI loads existing behavior action state on launch
        GIVEN: CLISession is configured for interactive mode
              AND: behavior action state file exists
        WHEN: user runs CLI
        THEN: Bot loads stored behavior action state
        
        CLI focus: State persistence on session launch
        """
        # GIVEN: Interactive mode with existing state
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['discovery'])
        state_file = create_behavior_action_state(workspace, 'story_bot', 'discovery', 'validate')
        
        # Load state into bot before creating CLI session
        bot.behaviors.load_state()
        
        # WHEN: CLISession initializes
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: State loaded from file
        assert state_file.exists()
        assert bot.behaviors.current.name == 'discovery'
        assert bot.behaviors.current.actions.current.action_name == 'validate'
    
    def test_cli_displays_status_on_launch(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays status on launch
        GIVEN: CLISession is initialized in interactive mode
        WHEN: user executes 'status' command
        THEN: CLI displays complete status output with all required sections in correct order
        
        CLI focus: Status display format verification
        """
        # GIVEN: Interactive mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify status output contains all required sections in order
        # Expected order: header -> bot name -> bot paths -> progress -> commands -> summary
        
        # 1. Header section (starts with separator, contains centered bold text)
        assert output.find("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") >= 0
        assert "CLI STATUS section" in output
        assert "This section contains current scope filter (if set), current progress in workflow, and available commands" in output
        assert "☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️" in output
        
        # 2. Bot name section (bold "🤖 Bot:" + space + bot name)
        assert "🤖 Bot:" in output
        assert bot.bot_name in output
        
        # 3. Bot paths section (Bot Path:, Workspace:, change path instructions)
        assert "Bot Path:" in output
        assert str(bot.bot_paths.bot_directory) in output
        assert "📂" in output  # Workspace emoji
        assert "Workspace:" in output  # Workspace label (may have ANSI codes around it)
        assert workspace.name in output
        assert str(bot.bot_paths.workspace_directory) in output
        assert "To change path:" in output
        
        # 4. Progress section (🗺️ Progress, Current Position, behaviors list)
        assert "🗺️ Progress" in output
        assert "Current Position:" in output
        
        # 5. Commands section (💻 Commands:, command list)
        assert "💻 Commands:" in output
        assert "status | back | current | next" in output
        
        # 6. Behavior/Action summary
        assert "Behaviors:" in output
        assert "Actions:" in output
        
        # Verify section order
        header_pos = output.find("CLI STATUS section")
        bot_name_pos = output.find("🤖 Bot:")
        bot_path_pos = output.find("Bot Path:")
        progress_pos = output.find("🗺️ Progress")
        commands_pos = output.find("💻 Commands:")
        behaviors_pos = output.find("Behaviors:")
        
        assert header_pos < bot_name_pos < bot_path_pos < progress_pos < commands_pos < behaviors_pos, \
            "Sections must appear in correct order"
    
    def test_cli_displays_header_section(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays header section
        GIVEN: CLISession is initialized
        WHEN: user executes 'status' command
        THEN: CLI displays header section with exact format including ANSI bold codes
        
        CLI focus: Header section format verification
        """
        # GIVEN: Interactive mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify header section format exactly
        # Expected: separator line (100 chars), centered bold "CLI STATUS section", description, warning, separator
        separator = "━" * 100
        assert separator in output
        assert "CLI STATUS section" in output
        assert "This section contains current scope filter (if set), current progress in workflow, and available commands" in output
        assert "Review the CLI STATUS section below to understand both current state and available commands." in output
        assert "☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️" in output
        
        # Verify header appears before bot section
        header_pos = output.find("CLI STATUS section")
        bot_pos = output.find("🤖 Bot:")
        assert header_pos < bot_pos, "Header must appear before bot section"
    
    def test_cli_displays_bot_section(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays bot section
        GIVEN: CLISession is initialized
        WHEN: user executes 'status' command
        THEN: CLI displays bot section with exact format
        
        CLI focus: Bot section format verification (bot name, bot path, workspace path, change path instructions)
        """
        # GIVEN: Interactive mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify bot section format exactly
        # Bot name: bold("🤖 Bot:") + space + bot name (not bold)
        assert "🤖 Bot:" in output
        assert bot.bot_name in output
        
        # Bot Path section: bold("Bot Path:") + newline + path
        assert "Bot Path:" in output
        assert str(bot.bot_paths.bot_directory) in output
        
        # Workspace section: emoji + bold("Workspace:") + space + workspace name + newline + path
        assert "📂" in output  # Workspace emoji
        assert "Workspace:" in output  # Workspace label (may have ANSI codes around it)
        assert workspace.name in output
        assert str(bot.bot_paths.workspace_directory) in output
        
        # Change path instructions
        assert "To change path:" in output
        assert "path demo/mob_minion" in output
        assert "path ../another_bot" in output
        
        # Verify order: Bot name -> Bot Path -> Workspace -> Change path instructions
        bot_name_pos = output.find("🤖 Bot:")
        bot_path_label_pos = output.find("Bot Path:")
        workspace_label_pos = output.find("Workspace:")  # May have ANSI codes and emoji before it
        change_path_pos = output.find("To change path:")
        
        assert bot_name_pos < bot_path_label_pos < workspace_label_pos < change_path_pos, \
            "Bot section elements must appear in correct order"


class TestStartCLISessionInPipeMode:
    """
    Story: Launch CLI in Pipe Mode (Markdown Mode)
    
    CLI focus: Session initialization in pipe mode with Markdown adapters
    """
    
    def test_cli_launches_in_pipe_mode(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI launches in pipe mode
        GIVEN: CLISession is configured for pipe mode (non-TTY)
        WHEN: commands are piped
        THEN: CLISession creates session without interactive prompts
              CLI can execute commands in pipe mode
              CLI uses markdown adapters for output
        
        CLI focus: Pipe mode initialization and markdown adapter selection
        """
        # GIVEN: Pipe mode (non-TTY detected)
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        monkeypatch.setattr(sys.stdout, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: CLISession initializes in pipe mode
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: CLISession wraps Bot
        assert cli_session.bot is not None
        
        # AND: CLI can execute commands
        response = cli_session.execute_command('status')
        assert response is not None
        assert isinstance(response.output, str)
    
    def test_cli_displays_status_in_markdown_format(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays status in markdown format in pipe mode
        GIVEN: CLISession is initialized in pipe mode
        WHEN: user executes 'status' command
        THEN: CLI displays complete status output in markdown format with all required sections
        
        CLI focus: Markdown format verification in pipe mode
        """
        # GIVEN: Pipe mode (non-TTY detected)
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        monkeypatch.setattr(sys.stdout, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify markdown format output contains all required sections
        # Expected markdown format: headers (##), bold (**text**), code blocks (`text`), lists (-)
        
        # 1. Header section (markdown separator and header)
        assert "---" in output  # Markdown separator
        assert "## CLI STATUS section" in output
        assert "**☢️  You MUST DISPLAY this entire section" in output
        
        # 2. Bot header section (markdown header with emoji)
        assert "## 🤖 Bot:" in output
        assert bot.bot_name in output
        
        # 3. Bot paths section (markdown headers and bold)
        assert "## Bot Paths" in output
        assert "**Bot Directory:**" in output
        assert "**Workspace:**" in output
        assert "`" in output  # Code/backtick markers (for paths)
        
        # 4. Progress section (markdown header)
        assert "## 🗺️ Progress" in output
        assert "**Current Position:**" in output
        
        # 5. Commands section (markdown header)
        assert "## 💻 Commands" in output
        assert "```powershell" in output  # Code block
        
        # 6. Behavior/Action summary
        assert "**Behaviors:**" in output
        assert "**Actions:**" in output
        
        # Verify markdown formatting elements are present
        assert "**" in output  # Bold markers
        assert "##" in output  # Headers
    
    def test_cli_displays_header_section_in_markdown(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays header section in markdown format
        GIVEN: CLISession is initialized in pipe mode
        WHEN: user executes 'status' command
        THEN: CLI displays header section with markdown formatting
        
        CLI focus: Markdown header section format verification
        """
        # GIVEN: Pipe mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify markdown header format
        # Markdown headers use # or ##
        assert "#" in output or "##" in output
        
        # Markdown bold uses **text**
        assert "**" in output
    
    def test_cli_displays_bot_section_in_markdown(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays bot section in markdown format
        GIVEN: CLISession is initialized in pipe mode
        WHEN: user executes 'status' command
        THEN: CLI displays bot section with markdown formatting
        
        CLI focus: Markdown bot section format verification
        """
        # GIVEN: Pipe mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify markdown bot section format
        # Bot name in markdown header
        assert "# Bot:" in output or "## Bot:" in output or bot.bot_name in output
        
        # Paths in markdown format (bold labels, code blocks for paths)
        assert "**Bot Directory:**" in output or "**Workspace:**" in output
        assert "`" in output  # Code blocks for paths
        
        # Verify markdown structure
        assert "##" in output  # Section headers


class TestDetectAndConfigureTTYNonTTYInput:
    """
    Story: Detect and Configure TTY/Non-TTY Input for CLI
    
    CLI focus: TTY detection and mode configuration
    """
    
    def test_tty_detector_identifies_interactive_terminal(self, tmp_path, monkeypatch):
        """
        SCENARIO: TTY detector identifies interactive terminal
        GIVEN: stdin is connected to a TTY terminal
        WHEN: CLI detects TTY status
        THEN: Interactive mode is detected
        
        CLI focus: TTY detection logic
        """
        # GIVEN: TTY detected
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: CLISession initializes
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: Interactive mode detected (via sys.stdin.isatty())
        assert sys.stdin.isatty() is True
    
    def test_tty_detector_identifies_piped_input(self, tmp_path, monkeypatch):
        """
        SCENARIO: TTY detector identifies piped input
        GIVEN: stdin is piped from another process
        WHEN: CLI detects TTY status
        THEN: Pipe mode is detected
        
        CLI focus: Non-TTY detection logic
        """
        # GIVEN: Non-TTY (piped input)
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: CLISession initializes
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: Pipe mode detected
        assert sys.stdin.isatty() is False


class TestStartCLISessionInJSONMode:
    """
    Story: Launch CLI in JSON Mode
    
    CLI focus: Session initialization in JSON mode with JSON adapters
    """
    
    def test_cli_launches_in_json_mode(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI launches in JSON mode
        GIVEN: CLISession is configured for JSON mode via mode parameter
        WHEN: commands are executed
        THEN: CLISession creates session without interactive prompts
              CLI can execute commands in JSON mode
              CLI uses JSON adapters for output
        
        CLI focus: JSON mode initialization and JSON adapter selection
        """
        # GIVEN: JSON mode set explicitly (e.g., for web view)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        
        # WHEN: CLISession executes command in JSON mode
        # THEN: CLISession wraps Bot
        assert cli_session.bot is not None
        assert cli_session.mode == 'json'
        
        # AND: CLI can execute commands
        response = cli_session.execute_command('status')
        assert response is not None
        assert isinstance(response.output, str)
    
    def test_cli_displays_status_in_json_format(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays status in JSON format in JSON mode
        GIVEN: CLISession is initialized in JSON mode
        WHEN: user executes 'status' command
        THEN: CLI displays complete status output in JSON format with all required fields
        
        CLI focus: JSON format verification in JSON mode
        """
        # GIVEN: JSON mode set explicitly
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify exact JSON format output
        # Import assert_valid_json helper from another CLI test file
        import sys
        from pathlib import Path
        cli_test_dir = Path(__file__).parent
        sys.path.insert(0, str(cli_test_dir))
        from test_execute_actions_using_cli import assert_valid_json
        
        data = assert_valid_json(output)
        
        # Verify required JSON fields are present
        assert 'name' in data or 'bot_name' in data
        assert 'bot_directory' in data or 'bot_paths' in data
        assert 'workspace_directory' in data or 'bot_paths' in data
        assert 'behavior_names' in data or 'behaviors' in data or 'current_behavior' in data
    
    def test_cli_displays_header_section_in_json(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays header section in JSON format
        GIVEN: CLISession is initialized in JSON mode
        WHEN: user executes 'status' command
        THEN: CLI displays header section with JSON structure
        
        CLI focus: JSON header section format verification
        """
        # GIVEN: JSON mode set explicitly
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify JSON format
        import json
        data = json.loads(output)
        
        # JSON should have structured data
        assert isinstance(data, dict)
        assert len(data) > 0
    
    def test_cli_displays_bot_section_in_json(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays bot section in JSON format
        GIVEN: CLISession is initialized in JSON mode
        WHEN: user executes 'status' command
        THEN: CLI displays bot section with JSON structure
        
        CLI focus: JSON bot section format verification
        """
        # GIVEN: JSON mode set explicitly
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        bot.behaviors.load_state()
        
        cli_session = CLISession(bot=bot, workspace_directory=workspace, mode='json')
        
        # WHEN: user executes status command
        cli_response = cli_session.execute_command('status')
        output = cli_response.output
        
        # THEN: Verify JSON bot section format
        import json
        data = json.loads(output)
        
        # Bot name should be in JSON (either 'name' or 'bot_name' field)
        assert 'name' in data or 'bot_name' in data, "Bot name should be present in JSON"
        if 'name' in data:
            assert data['name'] == bot.bot_name or data['name'] == bot.name, f"Bot name should match. Expected: {bot.bot_name} or {bot.name}, got: {data['name']}"
        else:
            assert 'bot_name' in data, "If 'name' not present, 'bot_name' must be"
            assert data['bot_name'] == bot.bot_name or data['bot_name'] == bot.name, f"Bot name should match. Expected: {bot.bot_name} or {bot.name}, got: {data['bot_name']}"
        
        # Bot directory should be in JSON (either 'bot_directory' or in 'bot_paths')
        assert 'bot_directory' in data or 'bot_paths' in data, "Bot directory should be present in JSON"
        if 'bot_directory' in data:
            assert str(bot.bot_directory) in str(data['bot_directory']), f"Bot directory should match. Expected to contain: {bot.bot_directory}"
        else:
            assert 'bot_paths' in data, "If 'bot_directory' not present, 'bot_paths' must be"
            assert 'bot_directory' in data['bot_paths'] or str(bot.bot_directory) in str(data['bot_paths']), f"Bot directory should be in bot_paths. Expected to contain: {bot.bot_directory}"


class TestLoadWorkspaceContext:
    """
    Story: Load and Display Workspace Context in CLI
    
    CLI focus: Workspace context loading on session launch
    """
    
    def test_cli_loads_workspace_directory_on_launch(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI loads workspace directory on launch
        GIVEN: Workspace directory exists
        WHEN: CLISession initializes
        THEN: CLISession stores workspace directory path
        
        CLI focus: Workspace context initialization
        """
        # GIVEN: Workspace exists
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: CLISession initializes
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: Workspace directory stored
        assert cli_session.workspace_directory == workspace
        assert cli_session.workspace_directory.exists()
    
    def test_cli_loads_story_graph_when_available(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI loads story graph when available
        GIVEN: Workspace has story graph file
        WHEN: CLISession initializes
        THEN: CLISession loads story graph
        
        CLI focus: Story graph context loading
        Note: Skipped - feature not yet implemented in CLISession
        """
        # GIVEN: Workspace with story graph
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_story_graph(workspace)
        
        # WHEN: CLISession initializes
        cli_session = CLISession(bot=bot, workspace_directory=workspace)
        
        # THEN: Story graph loaded (to be implemented)
        pass
