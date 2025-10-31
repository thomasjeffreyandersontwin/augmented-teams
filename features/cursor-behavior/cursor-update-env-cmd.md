# @cursor-update-env

Synchronize localized Cursor assets from `features/<feature>/cursor/` into `.cursor/*` and `commands/`.

## What it does
- Scans all `features/*/cursor/` folders (or a single `--feature`)
- Copies rule docs `*.mdc` → `.cursor/rules/`
- Copies command docs `*.md` → `.cursor/commands/`
- Copies command functions `*.py` → `commands/`
- Skips overwriting identical files; prints what changed

## Usage
```bash
python commands/cursor-update-env_cmd.py [--feature <name>]
```

## Notes
- Source of truth is per-feature `cursor/` folders
- Pairs with `@cursor-update-feature-from-env` for reverse sync
