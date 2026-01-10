#!/usr/bin/env python3
"""
Unified Generation Script for CRC Bot

Generates all CLI and MCP server code for crc_bot.
No parameters needed - auto-detects bot location from script path.

Usage:
    python generate.py
"""
from pathlib import Path
import sys
import os
import json

# Add workspace root to path
# generate.py is at agile_bot/bots/crc_bot/generate.py
# Workspace root is 3 levels up: crc_bot -> bots -> agile_bot -> workspace_root
script_dir = Path(__file__).parent.resolve()
python_workspace_root = script_dir.parent.parent.parent
if str(python_workspace_root) not in sys.path:
    sys.path.insert(0, str(python_workspace_root))

# Bootstrap environment variables (same pattern as crc_bot_cli.py)
bot_directory = script_dir
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

from agile_bot.src.cli.cli_generator import CliGenerator
from agile_bot.src.cli.cursor.cursor_command_visitor import CursorCommandGenerator
from agile_bot.bots.base_bot.src.mcp.mcp_server_generator import MCPServerGenerator


def main():
    """Generate all CLI and MCP code for crc_bot."""
    # Auto-detect bot location from script path
    bot_directory = script_dir
    workspace_root = python_workspace_root
    bot_location = bot_directory.relative_to(workspace_root)
    
    print("=" * 70)
    print("CRC Bot Code Generation")
    print("=" * 70)
    print(f"Workspace root: {workspace_root}")
    print(f"Bot directory: {bot_directory}")
    print(f"Bot location: {bot_location}")
    print()
    
    # Generate CLI code
    print("Generating CLI code...")
    print("-" * 70)
    cli_generator = CliGenerator(workspace_root=workspace_root, bot_location=str(bot_location))
    cli_results = cli_generator.generate_cli_code()
    
    print(f"  [OK] CLI Python: {cli_results['cli_python']}")
    print(f"  [OK] CLI Script: {cli_results['cli_script']}")
    print(f"  [OK] CLI PowerShell: {cli_results['cli_powershell']}")
    print()
    
    # Generate Cursor commands (optional - only for Cursor IDE)
    print("Generating Cursor commands...")
    print("-" * 70)
    try:
        from agile_bot.bots.base_bot.src.bot.bot import Bot
        bot = Bot(bot_name=cli_generator.bot_name, bot_directory=bot_directory, config_path=bot_directory / 'bot_config.json')
        cursor_visitor = CursorCommandGenerator(workspace_root, bot_location, bot, cli_generator.bot_name)
        cursor_commands = cursor_visitor.generate()
        registry_path = cursor_visitor.update_bot_registry(cli_results['cli_python'])
        
        print(f"  [OK] Cursor commands: {len(cursor_commands)} files")
        print(f"  [OK] Registry: {registry_path}")
    except Exception as e:
        print(f"  [SKIP] Cursor command generation skipped: {e}")
        print("         (This is normal in non-Cursor environments like VS Code)")
    print()
    
    # Generate MCP server code
    print("Generating MCP server code...")
    print("-" * 70)
    mcp_generator = MCPServerGenerator(bot_directory=bot_directory)
    mcp_results = mcp_generator.generate_server()
    
    print(f"  [OK] Bot config: {mcp_results['bot_config']}")
    print(f"  [OK] Server entry: {mcp_results['server_entry']}")
    print()
    
    # Generate awareness files
    print("Generating awareness files...")
    print("-" * 70)
    awareness_results = mcp_generator.generate_awareness_files()
    print(f"  [OK] Rules file: {awareness_results['rules_file']}")
    print()
    
    # Print MCP config for Cursor
    print("=" * 70)
    print("MCP Configuration for Cursor")
    print("=" * 70)
    print("Add this to your ~/.cursor/mcp.json (or C:\\Users\\<user>\\.cursor\\mcp.json on Windows):")
    print()
    print(json.dumps(mcp_results['mcp_config'], indent=2))
    print()
    print("=" * 70)
    print("Generation Complete!")
    print("=" * 70)
    print()
    print("Next steps:")
    print("  1. Add MCP config to ~/.cursor/mcp.json (see above)")
    print("  2. Restart Cursor to load the MCP server")
    print("  3. Use CLI commands via: crc_bot --help")


if __name__ == '__main__':
    main()

