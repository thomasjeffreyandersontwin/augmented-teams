"""
Story Bot MCP Server Entry Point

Runnable MCP server for story_bot using FastMCP and base generator.
"""
from pathlib import Path
import sys
import os
import json

# Setup Python import path for package imports
# This file is at: agile_bot/bots/story_bot/src/story_bot_mcp_server.py
python_workspace_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(python_workspace_root))

# ============================================================================
# BOOTSTRAP: Set environment variables before importing other modules
# ============================================================================

# 1. Self-detect bot directory from this script's location
bot_directory = Path(__file__).parent.parent  # src/ -> story_bot/
os.environ['BOT_DIRECTORY'] = str(bot_directory)

# 2. Read agent.json and set workspace directory (if not already set by mcp.json)
if 'WORKING_AREA' not in os.environ:
    agent_json_path = bot_directory / 'agent.json'
    if agent_json_path.exists():
        agent_config = json.loads(agent_json_path.read_text(encoding='utf-8'))
        if 'WORKING_AREA' in agent_config:
            os.environ['WORKING_AREA'] = agent_config['WORKING_AREA']

# ============================================================================
# Now import - everything will read from environment variables
# ============================================================================

from agile_bot.bots.base_bot.src.state.workspace import (
    get_bot_directory,
    get_workspace_directory
)
from agile_bot.bots.base_bot.src.mcp.mcp_server_generator import MCPServerGenerator


def main():
    """Main entry point for story_bot MCP server.

    Environment variables are bootstrapped before import:
    - BOT_DIRECTORY: Self-detected from script location
    - WORKING_AREA: Read from agent.json (or overridden by mcp.json env)
    
    All subsequent code reads from these environment variables.
    """
    # Get directories (these now just read from env vars we set above)
    bot_directory = get_bot_directory()
    workspace_directory = get_workspace_directory()
    
    # Create MCP server
    generator = MCPServerGenerator(
        bot_directory=bot_directory
    )

    mcp_server = generator.create_server_instance()
    generator.register_all_behavior_action_tools(mcp_server)

    mcp_server.run()


if __name__ == '__main__':
    main()
