# @cursor-create-command

Scaffold a new command under a feature `cursor/` folder, with docs and optional code function.

## What it does
- Creates: `features/<feature>/cursor/<name>-cmd.md`
- Optionally creates: `features/<feature>/cursor/<name>_cmd.py` (omit when `--ai-only`)
- Optionally appends a stub section referencing MCP tools (if provided)

## Usage
```bash
python commands/cursor-create-command.py --name <name> --feature <feature> [--ai-only] [--description "text"]
```

## Parameters
- `--name` (required): command name (kebab-case recommended)
- `--feature` (required): owning feature
- `--ai-only` (flag): create doc only (no code function)
- `--description` (optional): short purpose shown at top of doc

## Follow-ups
- Sync to environment: `python commands/cursor-update-env.py --feature <feature>`
- Update index: `python commands/cursor-update-commands-index.py`
