from pathlib import Path
from typing import Dict, Any, List
from agile_bot.bots.base_bot.src.cli.mcp_code_visitor import MCPCodeVisitor
from agile_bot.bots.base_bot.src.cli.action_data_collector import ActionDataCollector
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.cli.base_bot_cli import CliTerminalFormatter
from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.generator.orchestrator import Orchestrator, GeneratorConfig

class MCPCodeGenerator:

    def __init__(self, bot_name: str, bot_directory: Path):
        self.bot_name = bot_name
        self.bot_directory = bot_directory

    def generate_server_entry_point(self, behaviors: List[str], bot: Bot) -> Path:
        workspace_root = self.bot_directory.parent.parent.parent.parent.parent
        formatter = CliTerminalFormatter()
        description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, formatter)
        data_collector = ActionDataCollector(bot, self.bot_name, self.bot_directory, description_extractor)
        
        mcp_visitor = MCPCodeVisitor(workspace_root, self.bot_directory, self.bot_name, behaviors, data_collector)
        
        config = GeneratorConfig(
            bot=bot,
            bot_name=self.bot_name,
            visitor=mcp_visitor,
            data_collector=data_collector
        )
        generator = Orchestrator(config)
        generator.generate()
        
        return mcp_visitor.create_server_file()







