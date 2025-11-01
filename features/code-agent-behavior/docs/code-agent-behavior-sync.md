# Behavior Sync Feature

The **Behavior Sync** feature keeps feature-local AI behaviors in sync with the global `.cursor/` environment so the IDE agent always sees the latest rules, commands, and tools.

## Implementation

The behavior sync is implemented according to `behavior-sync-rule.mdc`:

### Rule Compliance

**Always:**
- ✅ Preserves file structure (`rules`, `commands`, `functions`, `mcp`)
- ✅ Merges MCP configs (`*-mcp.json`) if they already exist
- ✅ Merges `tasks.json` files from `features/*/.vscode/tasks.json` into root `.vscode/tasks.json`
- ✅ Overwrites only if the source is newer
- ✅ Logs synced and merged files
- ✅ Skips files marked as "draft" or "experimental"

**Never:**
- ✅ Never edits `.cursor/` directly (it's generated)
- ✅ Never syncs behaviors marked as "draft" or "experimental"

### File Structure & Routing

**All files** in `features/<feature-name>/code-agent-behaviors/` are synced to their destination:

```
features/<feature-name>/code-agent-behaviors/
  ├── <rule-name>.mdc          → .cursor/rules/
  ├── <command-name>.md         → .cursor/commands/
  ├── <function-name>.py        → commands/ (root level, NOT .cursor/commands/)
  └── <tool-name>-mcp.json      → .cursor/mcp/ (merged if exists)
```

**Routing Rules:**
- `.mdc` files → `.cursor/rules/`
- `.md` files → `.cursor/commands/`
- `.py` files → `commands/` (project root, not inside `.cursor/`)
- `.json` files → `.cursor/mcp/` (merged for MCP configs)

**Special Handling:**
- `features/*/.vscode/tasks.json` → Merged into root `.vscode/tasks.json` (tasks combined, duplicate labels avoided)

### Usage

```bash
# Sync all features
python behavior-sync-cmd.py

# Sync specific feature
python behavior-sync-cmd.py <feature-name>

# Watch mode (auto-sync on file changes)
python behavior-sync-cmd.py watch
```

### Watch Mode

Watch mode automatically syncs behaviors when files change:
- Monitors all `features/*/code-agent-behaviors/` directories
- Triggers sync when `.mdc`, `.md`, `.py`, or `.json` files change
- Debounces rapid changes (waits 2 seconds after last change)
- Skips draft/experimental files (same logic as manual sync)

Start watching:
```bash
python behavior-sync-cmd.py watch
```

Stop watching: Press `Ctrl+C`

### Output

The script provides detailed reporting:
- ✅ **Synced**: Files copied to `.cursor/`
- 🔄 **Merged**: MCP configs and tasks.json merged (preserves existing + adds new)
- ⏭️ **Skipped**: Files skipped due to:
  - Draft/experimental markers
  - Source not newer than destination
  - Merge/copy errors

### Auto-Triggers

The sync runs automatically:
- **On workspace open** via VS Code task `"Behavior Sync on Startup"`
- **On file changes** via watch mode (start manually or use `"Behavior Sync Watch Mode"` task)

### Post-Sync Actions

After syncing, run `\behavior-index` to update the behavior index with the synced changes.

## Related Files

- `behavior-sync-rule.mdc` - The rule definition
- `behavior-sync-cmd.md` - Command documentation
- `behavior-sync-cmd.py` - Implementation
