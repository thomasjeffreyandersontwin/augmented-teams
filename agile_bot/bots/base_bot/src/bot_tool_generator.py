"""
Bot Tool Generator

Generates bot tool that routes to current behavior and current action.
"""
from pathlib import Path
from typing import Dict, Any


class BotTool:
    """Bot tool that routes to current behavior and current action."""
    
    def __init__(self, bot_name: str, config_path: Path, workspace_root: Path):
        self.bot_name = bot_name
        self.config_path = config_path
        self.workspace_root = workspace_root
        self.name = f'{bot_name}_tool'
    
    def invoke(self, parameters: Dict[str, Any] = None):
        """Invoke bot tool - forwards to current behavior and current action."""
        from agile_bot.bots.base_bot.src.bot import Bot
        
        bot = Bot(
            bot_name=self.bot_name,
            workspace_root=self.workspace_root,
            config_path=self.config_path
        )
        return bot.forward_to_current_behavior_and_current_action()


class BotToolGenerator:
    """Generator for bot tools."""
    
    def __init__(self, bot_name: str, config_path: Path, workspace_root: Path):
        self.bot_name = bot_name
        self.config_path = config_path
        self.workspace_root = workspace_root
    
    def create_bot_tool(self) -> BotTool:
        """Create bot tool instance."""
        return BotTool(
            bot_name=self.bot_name,
            config_path=self.config_path,
            workspace_root=self.workspace_root
        )

