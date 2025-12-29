#!/usr/bin/env python3
"""
Crc Bot CLI Entry Point

Command-line interface for crc_bot using BaseBotCli.

Usage:
    crc_bot [--behavior <name>] [--action <name>] [--options]
    crc_bot --help
    crc_bot --list
    crc_bot --behavior <name> --list
    crc_bot --close

Examples:
    crc_bot
    crc_bot --behavior exploration
    crc_bot --behavior exploration --action clarify
    crc_bot --behavior exploration --action clarify @increment.txt
"""
from pathlib import Path
import sys
import os
import json

python_workspace_root = Path(__file__).parent.parent.parent.parent.parent
if str(python_workspace_root) not in sys.path:
    sys.path.insert(0, str(python_workspace_root))


bot_directory = Path(__file__).parent.parent
os.environ['BOT_DIRECTORY'] = str(bot_directory)

if 'WORKING_AREA' not in os.environ and 'WORKING_DIR' not in os.environ:
    config_path = bot_directory / 'bot_config.json'
    if config_path.exists():
        bot_config = json.loads(config_path.read_text(encoding='utf-8'))
        if 'mcp' in bot_config and 'env' in bot_config['mcp']:
            mcp_env = bot_config['mcp']['env']
            if 'WORKING_AREA' in mcp_env:
                os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']
        elif 'WORKING_AREA' in bot_config:
            os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']


from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory
from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli



def main():
    """Main CLI entry point.

    Environment variables are bootstrapped before import:
    - BOT_DIRECTORY: Self-detected from script location
    - WORKING_AREA: Read from bot_config.json (or pre-set by user)
    
    All subsequent code reads from these environment variables.
    """
    bot_directory = get_bot_directory()
    workspace_directory = get_workspace_directory()

    bot_name = 'crc_bot'
    bot_config_path = bot_directory / 'bot_config.json'
    
    cli = BaseBotCli(
        bot_name=bot_name,
        bot_config_path=bot_config_path
    )
    
    cli.main()


if __name__ == '__main__':
    main()
