"""
Bot Test Helper

Provides BotTestHelper class for bot setup and testing.

All domain-specific methods are now in sub-helpers:
- state: State management
- behaviors: Behavior and action management
- guardrails: Guardrails setup
- clarify: Clarify action
- strategy: Strategy action
- build: Build action and knowledge graph
- validate: Validate action, scanners, and rules
- render: Render action
- activity: Activity logging and tracking
- story: Story graph and story map
- scope: Scope and filtering
- instructions: Generic instruction methods
- files: File and directory management
"""
import json
import os
from pathlib import Path

from agile_bot.src.bot.bot import Bot
from agile_bot.test.domain.helpers import (
    StateTestHelper,
    BehaviorTestHelper,
    GuardrailsTestHelper,
    ClarifyTestHelper,
    StrategyTestHelper,
    BuildTestHelper,
    ValidateTestHelper,
    RenderTestHelper,
    ActivityTestHelper,
    StoryTestHelper,
    ScopeTestHelper,
    InstructionsTestHelper,
    FileTestHelper
)
class BotTestHelper:
    """
    Test helper that provides production story_bot and workspace.
    
    All domain-specific methods are accessible through sub-helpers:
    - helper.state.set_state()
    - helper.behaviors.navigate_to()
    - helper.story.create_story_graph()
    - etc.
    """
    
    def __init__(self, tmp_path: Path, workspace_directory: Path = None, bot_directory: Path = None):
        """Initialize with production story_bot and temp workspace.
        
        Args:
            tmp_path: Temporary directory path (pytest fixture)
            workspace_directory: Optional workspace directory (defaults to tmp_path / 'workspace')
            bot_directory: Optional custom bot directory (defaults to production story_bot)
        """
        # Use custom bot directory if provided, otherwise use production story_bot
        if bot_directory is not None:
            self.bot_directory = bot_directory
            self.bot_directory.mkdir(parents=True, exist_ok=True)
        else:
            # Get the actual story_bot directory (always the same)
            repo_root = Path(__file__).parent.parent.parent.parent
            self.bot_directory = repo_root / 'agile_bot' / 'bots' / 'story_bot'
        
        # Create temp workspace directory for state files (default to tmp_path / 'workspace')
        self.workspace = workspace_directory if workspace_directory is not None else tmp_path / 'workspace'
        self.workspace.mkdir(parents=True, exist_ok=True)

        # Bootstrap environment (set environment variables directly)
        os.environ['BOT_DIRECTORY'] = str(self.bot_directory)
        os.environ['WORKING_AREA'] = str(self.workspace)
        
        # Load the actual bot (always story_bot with all behaviors)
        # For custom bot_directory, create config in root; for production, check root then config/
        if bot_directory is not None:
            config_path = self.bot_directory / 'bot_config.json'
            # If custom bot_directory and no config exists, create minimal bot_config.json
            if not config_path.exists():
                import json
                config_data = {
                    'botName': 'story_bot',
                    'behaviors': []
                }
                config_path.write_text(json.dumps(config_data, indent=2), encoding='utf-8')
        else:
            config_path = self.bot_directory / 'bot_config.json'
            if not config_path.exists():
                config_path = self.bot_directory / 'config' / 'bot_config.json'
        
        # DON'T update bot_config.json - production bot already has all behaviors
        # and we shouldn't modify production files from tests
        
        self.bot = Bot(
            bot_name='story_bot',
            bot_directory=self.bot_directory,
            config_path=config_path
        )
        
        # Initialize sub-helpers
        self.state = StateTestHelper(parent=self)
        self.behaviors = BehaviorTestHelper(parent=self)
        self.guardrails = GuardrailsTestHelper(parent=self)
        self.clarify = ClarifyTestHelper(parent=self)
        self.strategy = StrategyTestHelper(parent=self)
        self.build = BuildTestHelper(parent=self)
        self.validate = ValidateTestHelper(parent=self)
        self.render = RenderTestHelper(parent=self)
        self.activity = ActivityTestHelper(parent=self)
        self.story = StoryTestHelper(parent=self)
        self.scope = ScopeTestHelper(parent=self)
        self.instructions = InstructionsTestHelper(parent=self)
        self.files = FileTestHelper(parent=self)
    
    def setup_custom_bot_directory(self, bot_directory: Path = None, workspace_directory: Path = None):
        """Set up a custom bot directory for testing (instead of production story_bot).
        
        Args:
            bot_directory: Custom bot directory to use (defaults to tmp_path / 'bot' if use_custom_bot was True)
            workspace_directory: Optional workspace directory (defaults to self.workspace)
        """
        if bot_directory:
            self.bot_directory = bot_directory
        elif not hasattr(self, 'bot_directory') or self.bot_directory is None:
            # If use_custom_bot was True, bot_directory should already be set
            # Otherwise, create default custom bot directory
            from pathlib import Path as P
            # Try to infer tmp_path from workspace
            tmp_path = self.workspace.parent if self.workspace.name == 'workspace' else self.workspace
            self.bot_directory = tmp_path / 'bot'
        
        self.bot_directory.mkdir(parents=True, exist_ok=True)
        
        if workspace_directory:
            self.workspace = workspace_directory
            self.workspace.mkdir(parents=True, exist_ok=True)
        
        # Bootstrap environment (set environment variables directly)
        os.environ['BOT_DIRECTORY'] = str(self.bot_directory)
        os.environ['WORKING_AREA'] = str(self.workspace)
        
        # Create bot if it doesn't exist yet
        if self.bot is None:
            config_path = self.bot_directory / 'bot_config.json'
            if not config_path.exists():
                config_path = self.bot_directory / 'config' / 'bot_config.json'
            
            if config_path.exists():
                self.bot = Bot(
                    bot_name='story_bot',
                    bot_directory=self.bot_directory,
                    config_path=config_path
                )
