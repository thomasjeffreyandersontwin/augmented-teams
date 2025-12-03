# Generate Bot MCP Server
# Usage: .\generate_bot.ps1 story_bot
# Usage: .\generate_bot.ps1 clean_code_bot

param(
    [Parameter(Mandatory=$true)]
    [string]$BotName
)

Write-Host "Generating MCP server for: $BotName" -ForegroundColor Cyan
Write-Host ""

$pythonScript = @"
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path.cwd()))

from agile_bot.bots.base_bot.src.mcp_server_generator import MCPServerGenerator

workspace_root = Path.cwd()

# Generate bot server
generator = MCPServerGenerator(
    workspace_root=workspace_root,
    bot_location=f'agile_bot/bots/$BotName'
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
print('Add this to C:\\Users\\thoma\\.cursor\\mcp.json:')
print('=' * 70)
print(json.dumps(artifacts['mcp_config'], indent=2))
print('=' * 70)
print()
print('Then restart Cursor to load the MCP server!')
"@

python -c $pythonScript

Write-Host ""
Write-Host "Done! Server generated for $BotName" -ForegroundColor Green

