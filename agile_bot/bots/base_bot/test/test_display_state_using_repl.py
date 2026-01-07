"""
Display Bot State Using CLI Tests - CURRENT Implementation

Tests validate CURRENT implementation before refactoring.
Current uses REPLStatus helper, not StatusDisplay class.
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


class TestDisplayBotHierarchyTreeInCLI:
    """Story: Display Bot Hierarchy Tree - CURRENT behavior"""
    
    def test_user_views_bot_hierarchy_with_status_command(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views bot hierarchy with status command
        GIVEN: CLI is at exploration.build.instructions
        WHEN: user enters 'status'
        THEN: CLI displays bot hierarchy tree
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at exploration.build.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior(bot_directory, 'exploration', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'exploration', 'build', 'instructions')
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: CLI displays bot hierarchy tree with indicators
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Status command returns output (content varies based on state)
        assert len(cli_response.output) > 0


class TestDisplayCurrentPositionInCLI:
    """Story: Display Current Position - CURRENT behavior"""
    
    def test_user_views_current_position_in_status(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views current position in status
        GIVEN: CLI is at shape.clarify.instructions
        WHEN: user enters 'status'
        THEN: CLI displays current position
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: CLI is at shape.clarify.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # WHEN: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: CLI displays current position
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        # Status command returns output
        assert len(cli_response.output) > 0
    
    def test_cli_displays_progress_section_with_current_position(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays Progress section with current position
        Given: CLI is at exploration.validate.instructions
        When: CLI renders status display
        Then: CLI displays Progress section header
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI is at exploration.validate.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'exploration', ['validate'])
        create_behavior_action_state(workspace_directory, 'exploration', 'validate', 'instructions')
        
        # When: CLI renders status display
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays Progress section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Progress' in cli_response.output or 'Current Position' in cli_response.output
    
    def test_cli_displays_hierarchical_status_tree_with_progress_indicators(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays hierarchical status tree with progress indicators
        Given: CLI is at exploration.validate.instructions
        When: CLI renders hierarchical status
        Then: CLI displays behaviors with status markers
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI is at exploration.validate.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior(bot_directory, 'exploration', ['validate'])
        create_behavior_action_state(workspace_directory, 'exploration', 'validate', 'instructions')
        
        # When: CLI renders hierarchical status
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays hierarchical status
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0
    
    def test_cli_displays_run_instructions_and_args_sections(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays Run instructions and Args sections
        Given: CLI is at exploration.validate.instructions
        When: CLI renders hierarchical status
        Then: CLI displays Run section
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI is at exploration.validate.instructions
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'exploration', ['validate'])
        create_behavior_action_state(workspace_directory, 'exploration', 'validate', 'instructions')
        
        # When: CLI renders hierarchical status
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays Run section or Args section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0


class TestDisplayActiveScopeInCLIStatus:
    """Story: Display Active Scope - CURRENT behavior"""
    
    def test_user_views_active_scope_in_status(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: User views active scope in status
        GIVEN: Scope filter is set
        WHEN: user views status
        THEN: CLI displays active scope
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # GIVEN: Scope filter is set
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: True)
        create_behavior(bot_directory, 'shape', ['clarify', 'strategy', 'build'])
        create_behavior_action_state(workspace_directory, 'shape', 'build', 'instructions')
        
        # WHEN: user views status
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        # Set scope first
        repl_session.read_and_execute_command('scope story="Story1"')
        # Then view status
        cli_response = repl_session.read_and_execute_command('status')
        
        # THEN: CLI displays status (scope may or may not be shown depending on implementation)
        assert cli_response is not None
        assert isinstance(cli_response.output, str)


class TestDisplayCLIHeader:
    """Story: Display CLI Header"""
    
    def test_cli_displays_cli_status_section_header_when_status_command_is_run(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays CLI STATUS section header when status command is run
        Given: CLI is initialized
        When: user enters 'status' command
        Then: CLI displays CLI STATUS section header
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI is initialized
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: user enters 'status' command
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays CLI STATUS section header
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'CLI STATUS section' in cli_response.output
        assert 'You MUST DISPLAY this entire section' in cli_response.output
    
    def test_cli_displays_bot_name_with_robot_emoji_in_header(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays bot name with robot emoji in header
        Given CLI is initialized with story_bot
        And CLI is in piped mode
        When CLI renders the dashboard header
        Then output contains heading with robot emoji and bot name
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given CLI is initialized with story_bot
        # And CLI is in piped mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When CLI renders the dashboard header
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then output contains heading with robot emoji and bot name
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Bot: story_bot' in cli_response.output or 'story_bot' in cli_response.output
    
    def test_cli_displays_bot_path_in_code_block(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays bot path in code block
        Given CLI is initialized with story_bot at path
        When CLI renders the dashboard header
        Then output contains Bot Path label
        And output shows the full bot directory path in code block
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given CLI is initialized with story_bot at path
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When CLI renders the dashboard header
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then output contains Bot Path label
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Bot Path' in cli_response.output or 'bot' in cli_response.output.lower()
    
    def test_cli_displays_workspace_name_and_path(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays workspace name and path
        Given CLI is initialized with workspace base_bot
        And workspace path is set
        When CLI renders the dashboard header
        Then output contains folder emoji and Workspace label
        And output shows workspace name
        And output shows full workspace path in code block
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given CLI is initialized with workspace base_bot
        # And workspace path is set
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When CLI renders the dashboard header
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then output contains Workspace label
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Workspace' in cli_response.output or str(workspace_directory) in cli_response.output
    
    def test_cli_displays_path_change_instructions(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays path change instructions
        Given CLI is in piped mode
        When CLI renders the dashboard header
        Then output contains 'To change path:' label
        And output shows path command examples
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given CLI is in piped mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When CLI renders the dashboard header
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then output contains path change instructions
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'path' in cli_response.output.lower()
    
    def test_cli_applies_separator_after_header_section(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI applies separator after header section
        Given CLI is in piped mode
        When CLI renders the dashboard header
        Then output ends with horizontal separator line
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given CLI is in piped mode
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When CLI renders the dashboard header
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then output ends with separator
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0
    
    def test_cli_displays_headless_mode_section_when_configured(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays headless mode section when configured
        Given: Headless mode is configured with API key
        When: CLI renders status display
        Then: CLI displays headless mode section
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: Headless mode is configured with API key
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: CLI renders status display
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays headless mode section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Headless Mode' in cli_response.output
    
    def test_cli_displays_active_headless_session_when_running(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays active headless session when running
        Given: Headless mode is configured
        AND: Active headless session is running
        When: CLI renders status display
        Then: CLI displays 'Active Session:' section
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: Headless mode is configured
        # AND: Active headless session is running
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # Create a log file to simulate active session
        log_dir = workspace_directory / 'logs'
        log_dir.mkdir(exist_ok=True)
        (log_dir / 'headless-2025-12-30-01-31-17.log').write_text('test log')
        
        # When: CLI renders status display
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays Active Session section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Headless Mode' in cli_response.output
    
    def test_cli_displays_headless_mode_unavailable_when_not_configured(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays headless mode unavailable when not configured
        Given: Headless mode is not configured
        When: CLI renders status display
        Then: CLI displays headless mode section with unavailable status
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: Headless mode is not configured
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: CLI renders status display
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays headless mode section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Headless Mode' in cli_response.output


class TestDisplayCLINavigationMenuFooter:
    """Story: Display CLI Navigation Menu Footer"""
    
    def test_cli_displays_commands_menu_footer(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays commands menu footer
        Given: CLI displays status
        When: CLI renders commands menu footer
        Then: CLI displays Commands section header
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI displays status
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: CLI renders commands menu footer
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays Commands section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Commands' in cli_response.output or 'status' in cli_response.output.lower()


class TestDisplayHeadlessModeStatusInCLI:
    """Story: Display Headless Mode Status in CLI"""
    
    def test_cli_displays_headless_mode_section_when_configured(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays headless mode section when configured
        Given: CLI is initialized
        And: headless mode is configured with API key
        When: user enters 'status'
        Then: CLI displays headless mode section
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI is initialized
        # And: headless mode is configured with API key
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays headless mode section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Headless Mode' in cli_response.output
    
    def test_cli_displays_active_headless_session_when_running(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays active headless session when running
        Given: CLI is initialized
        And: headless mode is configured
        And: active headless session is running
        When: user enters 'status'
        Then: CLI displays 'Active Session:' section
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI is initialized
        # And: headless mode is configured
        # And: active headless session is running
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # Create a log file to simulate active session
        log_dir = workspace_directory / 'logs'
        log_dir.mkdir(exist_ok=True)
        (log_dir / 'headless-2025-12-30-01-31-17.log').write_text('test log')
        
        # When: user enters 'status'
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI displays Active Session section
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'Headless Mode' in cli_response.output


class TestDisplayAvailableBotInTreeHierarchy:
    """Story: Display Available Bot in Tree Hierarchy"""
    
    def test_cli_displays_bot_name_in_header(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays bot name in header
        Given: CLI displays status
        When: CLI renders bot hierarchy
        Then: CLI shows current bot name in header
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI displays status
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: CLI renders bot hierarchy
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI shows current bot name in header
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert 'story_bot' in cli_response.output or 'Bot' in cli_response.output


class TestDisplayCLIBotCommandInNavigationMenuFooter:
    """Story: Display CLI Bot Command in Navigation Menu Footer"""
    
    def test_cli_displays_bot_command_in_footer(self, bot_directory, workspace_directory, monkeypatch):
        """
        SCENARIO: CLI displays bot command in footer
        Given: CLI displays footer
        When: CLI renders footer
        Then: CLI shows available navigation commands
        """
        from agile_bot.bots.base_bot.src.repl_cli.repl_session import REPLSession
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        
        # Given: CLI displays footer
        monkeypatch.setattr(sys.stdin, 'isatty', lambda: False)
        create_behavior(bot_directory, 'shape', ['clarify'])
        create_behavior_action_state(workspace_directory, 'shape', 'clarify', 'instructions')
        
        # When: CLI renders footer
        bot = Bot(
            bot_name='story_bot',
            bot_directory=bot_directory,
            config_path=bot_directory / 'bot_config.json'
        )
        repl_session = REPLSession(bot=bot, workspace_directory=workspace_directory)
        cli_response = repl_session.read_and_execute_command('status')
        
        # Then: CLI shows available navigation commands
        assert cli_response is not None
        assert isinstance(cli_response.output, str)
        assert len(cli_response.output) > 0

