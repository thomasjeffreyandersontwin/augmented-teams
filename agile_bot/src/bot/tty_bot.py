"""
TTY adapter for Bot domain object.
"""

from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseBotAdapter
from agile_bot.src.bot.bot import Bot

class TTYBot(BaseBotAdapter, TTYAdapter):
    """Serializes Bot domain object to TTY - exposes all Bot properties."""
    
    def __init__(self, bot: Bot):
        """
        Initialize TTY adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'tty')
        self.bot = bot
    
    # Expose ALL domain properties as FORMATTED display strings
    @property
    def name(self):
        """Returns formatted bot name header with registered bots."""
        lines = []
        # Show current bot and registered bots
        registered_bots = self.bot.bots
        if registered_bots:
            bot_list = ' | '.join(registered_bots)
            lines.append(f"{self.add_bold('🤖 Bot:')} {self.bot.name} | {self.add_bold('Registered:')} {bot_list}")
            lines.append(f"{self.add_bold('To change bots:')} bot <name>")
        else:
            lines.append(f"{self.add_bold('🤖 Bot:')} {self.bot.name}")
        return '\n'.join(lines)
    
    @property
    def bot_name(self):
        """Returns raw bot name."""
        return self.bot.bot_name
    
    @property
    def bot_directory(self):
        """Returns formatted bot directory path."""
        return f"{self.add_bold('Bot Path:')}\n{str(self.bot.bot_paths.bot_directory)}"
    
    @property
    def workspace_directory(self):
        """Returns formatted workspace directory path."""
        return f"{self.add_bold('Workspace Path:')}\n{str(self.bot.bot_paths.workspace_directory)}"
    
    @property
    def bot_paths(self):
        """Returns formatted bot paths display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        tty_bot_paths = AdapterFactory.create(self.bot.bot_paths, 'tty')
        return tty_bot_paths.serialize()
    
    @property
    def progress(self):
        """Returns formatted progress section with behaviors hierarchy."""
        lines = []
        lines.append(self.add_bold('🗺️ Progress'))
        lines.append(f"{self.add_bold('Current Position:')} {self.bot.progress_path}")
        lines.append("")
        
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        tty_behaviors = AdapterFactory.create(self.bot.behaviors, 'tty')
        lines.append(tty_behaviors.serialize())
        
        return '\n'.join(lines)
    
    @property
    def behaviors(self):
        """Returns formatted behaviors display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        tty_behaviors = AdapterFactory.create(self.bot.behaviors, 'tty')
        return tty_behaviors.serialize()
    
    @property
    def header(self):
        """Returns CLI STATUS section header with AI instructions."""
        lines = []
        lines.append("")
        lines.append(self.section_separator())
        # Center the text within the separator width (100 chars)
        text = "CLI STATUS section"
        separator_width = 100
        padding = (separator_width - len(text)) // 2
        centered_text = " " * padding + self.add_bold(text) + " " * padding
        lines.append(centered_text)
        lines.append("This section contains current scope filter (if set), current progress in workflow, and available commands")
        lines.append("Review the CLI STATUS section below to understand both current state and available commands.")
        lines.append("☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️")
        lines.append(self.section_separator())
        return '\n'.join(lines)
    
    @property
    def run_instructions(self):
        """Returns run instructions for executing behaviors/actions."""
        lines = []
        lines.append("Run:")
        lines.append("echo 'behavior.action' | python repl_main.py           # Defaults to 'instructions' operation")
        lines.append("echo 'behavior.action.operation' | python repl_main.py  # Runs operation")
        lines.append("")
        lines.append(self.add_bold("Args:"))
        lines.append('--scope "Epic, Sub Epic, Story"      # Filter by story names')
        lines.append('--scope "file:path/one,path/two"     # Filter by file paths')
        lines.append('--headless                             # Execute autonomously without user input')
        lines.append(self.subsection_separator())
        return '\n'.join(lines)
    
    @property
    def commands(self):
        """Returns available commands quick reference."""
        lines = []
        lines.append(self.add_bold('💻 Commands:'))
        lines.append(self.add_bold("status | back | current | next | path [dir] | scope [filter] | bot [name] | help | exit"))
        lines.append("")
        lines.append("// Run")
        lines.append("echo '[command]' | python repl_main.py")
        lines.append("// to invoke commands")
        lines.append("")
        lines.append(self.section_separator())
        return '\n'.join(lines)
    
    @property
    def behavior_action_summary(self):
        """Returns summary of all behaviors and actions."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        tty_behaviors = AdapterFactory.create(self.bot.behaviors, 'tty')
        
        lines = []
        lines.append(f"{self.add_bold('Behaviors:')} {tty_behaviors.names}")
        
        # Get actions from current behavior or first behavior
        behavior = self.bot.behaviors.current or next(iter(self.bot.behaviors), None)
        if behavior:
            tty_actions = AdapterFactory.create(behavior.actions, 'tty')
            lines.append(f"{self.add_bold('Actions:')} {tty_actions.names}")
        
        return '\n'.join(lines)
    
    def format_header(self) -> str:
        """Returns CLI STATUS section header with AI instructions."""
        return self.header
    
    def format_bot_info(self) -> str:
        """Returns bot name and paths."""
        lines = []
        lines.append(self.name)
        lines.append(self.bot_paths)
        
        if hasattr(self.bot, '_scope'):
            from agile_bot.src.cli.adapter_factory import AdapterFactory
            tty_scope = AdapterFactory.create(self.bot._scope, 'tty')
            lines.append(tty_scope.serialize())
        
        if self.bot.behaviors:
            lines.append(self.progress)
            lines.append(self.run_instructions)
        
        lines.append(self.commands)
        
        return '\n'.join(lines)
    
    def format_footer(self) -> str:
        """Returns behavior/action summary."""
        return self.behavior_action_summary
    
    def serialize(self) -> str:
        """Convert Bot to TTY string - uses base class serialization."""
        return super().serialize()
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
