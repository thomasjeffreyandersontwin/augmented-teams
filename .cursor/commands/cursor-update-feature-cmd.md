# @cursor-update-feature-from-env

Synchronize global Cursor assets from `.cursor/*` back into a specific feature’s `cursor/` folder.

## What it does
- Copies `.cursor/rules/*.mdc` → `features/<feature>/cursor/`
- Copies `.cursor/commands/*.md` → `features/<feature>/cursor/`
- Does not copy command functions by default (author command functions under the feature’s `cursor/` and use `@cursor-update-env` to push them to `commands/`)

## Usage
```bash
python commands/cursor-update-feature-from-env_cmd.py --feature <name>
```

## Notes
- `--feature` is required to avoid ambiguity
- Use when edits were made directly in `.cursor/*` and need to be localized
- Pairs with `@cursor-update-env` for forward sync
