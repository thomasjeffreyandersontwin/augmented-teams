"""
Markdown adapter for Bot domain object.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.cli.base_hierarchical_adapter import BaseBotAdapter
from agile_bot.src.bot.bot import Bot

class MarkdownBot(BaseBotAdapter, MarkdownAdapter):
    """Serializes Bot domain object to Markdown - matches TTYBot structure."""
    
    def __init__(self, bot: Bot):
        """
        Initialize Markdown adapter for Bot.
        
        Args:
            bot: Bot domain object to serialize
        """
        BaseBotAdapter.__init__(self, bot, 'markdown')
        self.bot = bot
    
    
    @property
    def name(self):
        """Returns formatted bot name header."""
        return MarkdownAdapter.format_header(self, 2, f"🤖 Bot: {self.bot.name}").strip()
    
    @property
    def bot_paths(self):
        """Returns formatted bot paths display."""
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        markdown_bot_paths = AdapterFactory.create(self.bot.bot_paths, 'markdown')
        return markdown_bot_paths.serialize()
    
    @property
    def progress(self):
        """Returns formatted progress section with behaviors hierarchy."""
        lines = []
        lines.append(MarkdownAdapter.format_header(self, 2, "🗺️ Progress"))
        lines.append("")
        lines.append(f"**Current Position:** {self.bot.progress_path}")
        lines.append("")
        
        from agile_bot.src.cli.adapter_factory import AdapterFactory
        markdown_behaviors = AdapterFactory.create(self.bot.behaviors, 'markdown')
        lines.append(markdown_behaviors.serialize())
        
        return '\n'.join(lines)
    
    @property
    def commands(self):
        """Returns available commands quick reference."""
        lines = []
        lines.append(MarkdownAdapter.format_header(self, 2, "💻 Commands"))
        lines.append("")
        lines.append("**status | back | current | next | path [dir] | scope [filter] | headless \"msg\" | help | exit**")
        lines.append("")
        lines.append("```powershell")
        lines.append("echo '[command]' | python -m agile_bot.src.cli.cli_main")
        lines.append("```")
        lines.append("")
        lines.append("---")
        return '\n'.join(lines)
    
    @property
    def behavior_action_summary(self):
        """Returns summary of all behaviors and actions."""
        lines = []
        
        # Get behavior names
        behavior_names = []
        for behavior in self.bot.behaviors:
            name = behavior.name
            if name == (self.bot.behaviors.current.name if self.bot.behaviors.current else None):
                behavior_names.append(f"**{name}**")
            else:
                behavior_names.append(name)
        
        lines.append(f"**Behaviors:** {' | '.join(behavior_names)}")
        
        # Get actions from current behavior
        behavior = self.bot.behaviors.current or next(iter(self.bot.behaviors), None)
        if behavior:
            action_names = []
            all_actions = list(behavior.actions) + list(behavior.actions._non_workflow_actions)
            current_action_name = behavior.actions.current.action_name if behavior.actions.current else None
            for action in all_actions:
                name = action.action_name
                if name == current_action_name:
                    action_names.append(f"**{name}**")
                else:
                    action_names.append(name)
            lines.append(f"**Actions:** {' | '.join(action_names)}")
        
        return '\n'.join(lines)
    
    def format_header(self) -> str:
        """Returns CLI STATUS section header with AI instructions in markdown."""
        lines = []
        lines.append("")
        lines.append("---")
        header_text = MarkdownAdapter.format_header(self, 2, "CLI STATUS section")
        lines.append(header_text)
        lines.append("")
        lines.append("This section contains current scope filter (if set), current progress in workflow, and available commands")
        lines.append("")
        lines.append("Review the CLI STATUS section below to understand both current state and available commands.")
        lines.append("")
        lines.append("**☢️  You MUST DISPLAY this entire section in your response to the user exactly as you see it. ☢️**")
        lines.append("")
        lines.append("---")
        return '\n'.join(lines)
        
    def format_bot_info(self) -> str:
        """Returns bot name and paths."""
        lines = []
        lines.append(self.name)
        lines.append("")
        lines.append(self.bot_paths)
        
        if hasattr(self.bot, '_scope') and self.bot._scope and hasattr(self.bot._scope, 'type'):
            from agile_bot.src.cli.adapter_factory import AdapterFactory
            try:
                markdown_scope = AdapterFactory.create(self.bot._scope, 'markdown')
                lines.append(markdown_scope.serialize())
                lines.append("")
            except (AttributeError, TypeError):
                pass
        
        if self.bot.behaviors:
            lines.append(self.progress)
            lines.append("")
        
        lines.append(self.commands)
        lines.append("")
        
        return '\n'.join(lines)
    
    def format_footer(self) -> str:
        """Returns behavior/action summary."""
        return self.behavior_action_summary
    
    def serialize(self) -> str:
        """Convert Bot to Markdown string - uses base class serialization."""
        result = super().serialize()
        return result + "\n" if result else result
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
