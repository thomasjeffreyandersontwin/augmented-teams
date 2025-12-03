#!/bin/bash
# Generate Bot MCP Server
# Usage: ./generate_bot.sh story_bot
# Usage: ./generate_bot.sh clean_code_bot

if [ -z "$1" ]; then
    echo "Usage: ./generate_bot.sh <bot_name>"
    echo "Example: ./generate_bot.sh story_bot"
    exit 1
fi

BOT_NAME=$1

echo "Generating MCP server for: $BOT_NAME"
echo ""

python << EOF
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path.cwd()))

from agile_bot.bots.base_bot.src.mcp_server_generator import MCPServerGenerator

workspace_root = Path.cwd()

# Generate bot server
generator = MCPServerGenerator(
    workspace_root=workspace_root,
    bot_location=f'agile_bot/bots/$BOT_NAME'
)

print('Discovering behaviors...')
behaviors = generator.discover_behaviors_from_folders()
print(f'Found {len(behaviors)} behaviors: {behaviors}')
print()

print('Generating server artifacts...')
artifacts = generator.generate_server()

print()
print('Generated files:')
print(f'  Bot config: {artifacts["bot_config"]}')
print(f'  Server entry: {artifacts["server_entry"]}')
print()

print('=' * 70)
print('Add this to ~/.cursor/mcp.json:')
print('=' * 70)
print(json.dumps(artifacts['mcp_config'], indent=2))
print('=' * 70)
print()
print('Then restart Cursor to load the MCP server!')
EOF

echo ""
echo "Done! Server generated for $BOT_NAME"

