"""
Story Bot MCP Server Entry Point

Runnable MCP server for story_bot using FastMCP and base generator.
"""
from pathlib import Path
import sys
import os
import json
from datetime import datetime
import logging

# Setup Python import path for package imports
python_workspace_root = Path(__file__).parent.parent.parent.parent.parent
if str(python_workspace_root) not in sys.path:
    sys.path.insert(0, str(python_workspace_root))

# ============================================================================
# BOOTSTRAP: Set environment variables before importing other modules
# ============================================================================

# 1. Self-detect bot directory from this script's location
bot_directory = Path(__file__).parent.parent  # src/ -> story_bot/
os.environ['BOT_DIRECTORY'] = str(bot_directory)

# 2. Read bot_config.json and set workspace directory (if not already set by mcp.json env)
if 'WORKING_AREA' not in os.environ:
    config_path = bot_directory / 'bot_config.json'
    if config_path.exists():
        bot_config = json.loads(config_path.read_text(encoding='utf-8'))
        # Check mcp.env.WORKING_AREA (standard location)
        if 'mcp' in bot_config and 'env' in bot_config['mcp']:
            mcp_env = bot_config['mcp']['env']
            if 'WORKING_AREA' in mcp_env:
                os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']

# ============================================================================
# Now import - everything will read from environment variables
# ============================================================================

from agile_bot.bots.base_bot.src.bot.workspace import (
    get_bot_directory,
    get_workspace_directory,
    get_python_workspace_root
)
from agile_bot.bots.base_bot.src.bot.bot import Bot, BotResult
from agile_bot.bots.base_bot.src.mcp.server_restart import restart_mcp_server
from fastmcp import FastMCP
import logging

logger = logging.getLogger(__name__)

def main():
    """Main entry point for story_bot MCP server.

    Environment variables are bootstrapped before import:
    - BOT_DIRECTORY: Self-detected from script location
    - WORKING_AREA: Read from bot_config.json (or overridden by mcp.json env)
    
    All subsequent code reads from these environment variables.
    
    Note: This file is generated with static tool registrations.
    Tools are registered at generation time, not dynamically at runtime.
    """
    bot_directory = get_bot_directory()
    workspace_directory = get_workspace_directory()
    
    bot = Bot(bot_name='story_bot', bot_directory=bot_directory, config_path=bot_directory / 'bot_config.json')
    
    server_name = 'story_bot'
    mcp_server = FastMCP(server_name)
    
    # Tools are statically registered in the generated code below
    # This section is replaced during code generation with actual tool registrations
    
    mcp_server.run()


if __name__ == '__main__':
    main()
