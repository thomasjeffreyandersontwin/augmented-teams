from pathlib import Path
from typing import Dict, Any

class MCPCodeGenerator:

    def __init__(self, bot_name: str, bot_directory: Path):
        self.bot_name = bot_name
        self.bot_directory = bot_directory

    def generate_server_entry_point(self) -> Path:
        src_dir = self.bot_directory / 'src'
        src_dir.mkdir(parents=True, exist_ok=True)
        server_file = src_dir / f'{self.bot_name}_mcp_server.py'
        server_code = f'''"""\n{self.bot_name.title().replace('_', ' ')} MCP Server Entry Point\n\nRunnable MCP server for {self.bot_name} using FastMCP and base generator.\n"""\nfrom pathlib import Path\nimport sys\nimport os\nimport json\n\npython_workspace_root = Path(__file__).parent.parent.parent.parent.parent\nif str(python_workspace_root) not in sys.path:\n    sys.path.insert(0, str(python_workspace_root))\n\n\nbot_directory = Path(__file__).parent.parent\nos.environ['BOT_DIRECTORY'] = str(bot_directory)\n\nif 'WORKING_AREA' not in os.environ:\n    config_path = bot_directory / 'bot_config.json'\n    if config_path.exists():\n        bot_config = json.loads(config_path.read_text(encoding='utf-8'))\n        if 'mcp' in bot_config and 'env' in bot_config['mcp']:\n            mcp_env = bot_config['mcp']['env']\n            if 'WORKING_AREA' in mcp_env:\n                os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']\n\n\nfrom agile_bot.bots.base_bot.src.bot.workspace import (\n    get_bot_directory,\n    get_workspace_directory\n)\nfrom agile_bot.bots.base_bot.src.mcp.mcp_server_generator import MCPServerGenerator\n\n\ndef main():\n    """Main entry point for {self.bot_name} MCP server.\n\n    Environment variables are bootstrapped before import:\n    - BOT_DIRECTORY: Self-detected from script location\n    - WORKING_AREA: Read from bot_config.json (or overridden by mcp.json env)\n    \n    All subsequent code reads from these environment variables.\n    """\n    bot_directory = get_bot_directory()\n    workspace_directory = get_workspace_directory()\n    \n    generator = MCPServerGenerator(\n        bot_directory=bot_directory\n    )\n\n    mcp_server = generator.create_server_instance()\n    generator.register_all_tools(mcp_server)\n\n    mcp_server.run()\n\n\nif __name__ == '__main__':\n    main()\n'''
        server_file.write_text(server_code)
        return server_file