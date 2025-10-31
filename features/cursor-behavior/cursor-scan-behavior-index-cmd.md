# @cursor-scan-behavior-index

Scan the codebase and automatically update `cursor-behavior-index.mdc` with current inventory.

## What it does
- Scans all `features/*/cursor/` directories for rules, commands, and command functions
- Scans `.cursor/rules/`, `.cursor/commands/`, and `commands/` for deployed items
- Identifies orphaned items (deployed but not in any feature source)
- Updates the Current Inventory, Deployment Inventory, and Orphaned Behaviors sections in the index

## Usage
```bash
python features/cursor-behavior/cursor-scan-behavior-index_cmd.py
```

Or if synced to commands:
```bash
python commands/cursor-scan-behavior-index_cmd.py
```

## Execution Model
- **Type:** Code-backed command
- **Function:** `features/cursor-behavior/cursor-scan-behavior-index_cmd.py`

## When to use
- After adding/removing rules, commands, or command functions in features
- When the index file is out of sync with actual files
- As part of maintenance workflow before committing changes

## Notes
- Automatically formats sections according to index conventions
- Preserves other sections (MCP Servers, etc.) untouched
- Shows scan summary with counts per feature

