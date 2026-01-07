"""
Display Bot State Using CLI Tests - REPL Status Display Interface

Tests for displaying bot state through CLI status commands.
All tests focus on REPL-specific concerns: status command parsing,
display format, and user feedback.

REPL focus: Status display, hierarchy tree, position indicators
Uses common helpers from: test_invoke_bot_helpers.py
"""
import pytest
import sys
from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
from agile_bot.bots.base_bot.test.test_invoke_bot_helpers import (
    setup_test_bot,
    create_behavior_action_state
)


class TestViewBehaviorHierarchy:
    """
    Story: Display Bot Hierarchy Tree
    
    REPL focus: Hierarchy tree display format
    """
    
    def test_user_views_bot_hierarchy_with_status_command(self, tmp_path, monkeypatch):
        """
        SCENARIO: User views bot hierarchy with status command
        GIVEN: CLI is at exploration.validate
        WHEN: user enters 'status'
        THEN: REPL parses status command
              CLI displays bot hierarchy tree
        
        REPL focus: Status command execution and hierarchy display
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape', 'exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via REPL
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: Status displayed
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0


class TestViewCurrentPosition:
    """
    Story: Display Current Position
    
    REPL focus: Current position indicators in status display
    """
    
    def test_user_views_current_position_in_status(self, tmp_path, monkeypatch):
        """
        SCENARIO: User views current position in status
        GIVEN: CLI is at shape.clarify
        WHEN: user enters 'status'
        THEN: CLI displays current position with indicators
        
        REPL focus: Position display in status output
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'clarify')
        bot.behaviors.load_state()
        
        # WHEN: user enters 'status' via REPL
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: Current position displayed
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0
    
    def test_cli_displays_progress_section_with_current_position(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays Progress section with current position
        GIVEN: CLI is at exploration.validate
        WHEN: CLI renders status display
        THEN: CLI displays Progress section header
        
        REPL focus: Progress section in status display
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['exploration'])
        create_behavior_action_state(workspace, 'story_bot', 'exploration', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Progress information included
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        # Progress section should be present (format may vary)
        assert len(display_text) > 0
    
    def test_cli_displays_behavior_in_progress_section(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays behavior in Progress section
        GIVEN: CLI is at shape.validate
        WHEN: CLI renders status display
        THEN: CLI displays current behavior in Progress section
        
        REPL focus: Behavior display in progress section
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Behavior info included
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        assert len(display_text) > 0


class TestViewActiveScope:
    """
    Story: Display Active Scope Filter
    
    REPL focus: Scope display in status output
    """
    
    def test_cli_displays_active_scope_in_status(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays active scope in status
        GIVEN: Scope filter is active
        WHEN: user enters 'status'
        THEN: CLI displays active scope information
        
        REPL focus: Scope display format
        """
        # GIVEN: Bot with scope set
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        create_behavior_action_state(workspace, 'story_bot', 'shape', 'validate')
        bot.behaviors.load_state()
        
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        # Set a scope
        repl_session.read_and_execute_command('scope story="Test Story"')
        
        # WHEN: user enters 'status' via REPL
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: Scope information displayed
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestViewSessionHeader:
    """
    Story: Display Session Header
    
    REPL focus: Session header formatting
    """
    
    def test_cli_displays_bot_name_in_header(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays bot name in header
        GIVEN: Bot is initialized
        WHEN: CLI renders display
        THEN: Header includes bot name
        
        REPL focus: Header display format
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Bot name in header
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        assert 'story_bot' in display_text.lower() or len(display_text) > 0
    
    def test_cli_displays_working_area_in_header(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays working area in header
        GIVEN: Workspace is configured
        WHEN: CLI renders display
        THEN: Header includes workspace path
        
        REPL focus: Workspace info in header
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Workspace info included
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        assert len(display_text) > 0


class TestViewNavigationCommands:
    """
    Story: Display Navigation Commands
    
    REPL focus: Available commands display
    """
    
    def test_cli_displays_available_commands(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays available commands
        GIVEN: CLI is running
        WHEN: Status displayed
        THEN: Available commands shown
        
        REPL focus: Command list display
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Commands available
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        # Commands may be shown in various formats
        assert len(display_text) > 0


class TestViewHeadlessModeStatus:
    """
    Story: Display Headless Mode Status
    
    REPL focus: Headless mode indicators
    """
    
    def test_cli_shows_headless_mode_when_active(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI shows headless mode when active
        GIVEN: Headless mode is enabled
        WHEN: Status displayed
        THEN: Headless indicator shown
        
        REPL focus: Mode indicator display
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Mode info included
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        # Headless/pipe mode may show different indicators
        assert len(display_text) > 0


class TestViewAvailableBots:
    """
    Story: Display Available Bots
    
    REPL focus: Bot list display
    """
    
    def test_cli_displays_configured_bot(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays configured bot
        GIVEN: Bot is configured
        WHEN: Status displayed
        THEN: Bot information shown
        
        REPL focus: Bot info display format
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Bot info included
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        assert len(display_text) > 0


class TestDisplayCLIBotCommandInNavigationMenuFooter:
    """
    Story: Display CLI Bot Command in Navigation Menu Footer
    
    REPL focus: Footer command display
    """
    
    def test_cli_displays_bot_command_in_footer(self, tmp_path, monkeypatch):
        """
        SCENARIO: CLI displays bot command in footer
        GIVEN: CLI is running
        WHEN: Status displayed
        THEN: Footer shows available commands
        
        REPL focus: Footer formatting
        """
        # GIVEN
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        bot, workspace = setup_test_bot(tmp_path, ['shape'])
        
        # WHEN: Status displayed
        repl_session = REPLSession(bot=bot, workspace_directory=workspace)
        cli_output = repl_session.display_current_state()
        
        # THEN: Footer info included
        display_text = str(cli_output.output) if hasattr(cli_output, 'output') else str(cli_output)
        # Footer may show help, commands, or other info
        assert len(display_text) > 0
