### Command: `behavior-sync-cmd.md`

**Purpose:** Keep AI behaviors up to date across all features.

**Usage:**
* `\behavior-sync` — sync all behaviors
* `\behavior-sync <feature>` — sync a specific feature
* `python features/cursor-behavior/cursor/behavior-sync-cmd.py watch` — watch for file changes and auto-sync

**File Routing Rules:**
1. **All files** in `features/*/cursor/` folders are synced
2. Files are routed to correct locations based on extension:
   * `.mdc` files → `.cursor/rules/`
   * `.md` files → `.cursor/commands/`
   * `.py` files → `commands/` (root level, NOT `.cursor/commands/`)
   * `.json` files → `.cursor/mcp/` (merged if MCP configs exist)
3. **Special handling:**
   * `features/*/.vscode/tasks.json` → Merged into root `.vscode/tasks.json` (tasks combined, duplicate labels avoided)

**Steps:**
1. Scan `features/*/cursor/` folders
2. Route files to correct destination based on extension
3. Merge MCP configs (`*-mcp.json`) if they already exist
4. Overwrite only if source is newer
5. Skip files marked as "draft" or "experimental"
6. Report results
7. **After syncing, run `\behavior-index` to update the behavior index with the synced changes**

**Rule Association:**
* Follow rules in `features/*/cursor/rules/` folders when syncing
* Rules are associated with their respective features and should be maintained accordingly




**Rule:**
* `\behavior-sync-rule` — [description of rule this command follows]

**Implementation:**
* `behavior_sync()` — [description of code function]

**AI Usage:**
* [When to use AI assistance - e.g., for complex reasoning, content generation, etc.]

**Code Usage:**
* [When to use code execution - e.g., for file operations, data processing, etc.]