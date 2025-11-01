# Behavior Index Feature

The **Behavior Index** feature maintains an up-to-date index of all AI behaviors across features, providing visibility into what behaviors exist, where they live, and which ones are active.

## Implementation

The behavior index is implemented according to `behavior-index-rule.mdc`:

### Rule Compliance

**Always:**
- ✅ Detects additions, updates, or deletions in `features/*/code-agent-behaviors/`
- ✅ Records feature name, file type, path, and modification timestamp
- ✅ Updates both local (`features/<feature>/code-agent-behavior-index.json`) and global (`.cursor/behavior-index.json`) indexes
- ✅ Logs the number of behaviors detected and updated
- ✅ The Cursor environment **must constantly refer to the behavior index during chat** to discover available commands, rules, functions, and MCP configs

**Never:**
- ✅ Manually edit index files
- ✅ Include draft or experimental behaviors in the index

### Index Structure

The index has two sections:

1. **`deployed`** - Behaviors organized by deployment location (e.g., `.cursor/rules/`, `.cursor/commands/`, `commands/`)
2. **`features`** - Behaviors organized by feature name

Each entry includes:
- `feature` - Feature name
- `file` - File name
- `type` - File extension (.mdc, .md, .py, .json)
- `path` - Full file path
- `modified` - Modification timestamp
- `purpose` - One-liner description extracted from the file

### Purpose Extraction

The index automatically extracts one-liner purposes from behavior files by:
1. Looking for `**Purpose:**` headers in markdown files
2. Extracting Python docstrings
3. Using the first meaningful line of the file

After generating the index, review `.cursor/behavior-index.json` and manually update any nonsensical purposes with clear, concise descriptions.

### Syncing Purposes

After updating purposes in the global index, run:
```bash
python features/code-agent-behavior/code-agent-behaviors/code-agent-behavior-index-cmd.py sync-purposes
```

This copies updated purposes from the global index to all local index files.

### File Structure

```
features/<feature>/
  ├── code-agent-behaviors/
  │   ├── <behavior-name>-rule.mdc
  │   ├── <behavior-name>-cmd.md
  │   └── <behavior-name>-cmd.py
  └── code-agent-behavior-index.json  ← Local index
```

### Usage

```bash
# Index all features
python behavior-index-cmd.py

# Index specific feature
python behavior-index-cmd.py <feature-name>

# Sync purposes from global to local indexes
python behavior-index-cmd.py sync-purposes
```

### Output

The script provides detailed reporting:
- ✅ **Indexed**: Number of behaviors indexed
- 📁 **Features**: Number of features processed
- ⏭️ **Skipped**: Files skipped due to draft/experimental markers

### Cursor Environment Integration

**Critical Requirement:** The Cursor environment **must constantly refer to `.cursor/behavior-index.json` during chat** to discover and use available commands, rules, functions, and MCP configs. This ensures:

* The AI assistant has complete visibility into all available behaviors across all features
* Commands, rules, and functions are discoverable without manual lookup
* The index serves as the single source of truth for what behaviors are available
* Real-time awareness of new behaviors as they're added or updated

### Auto-Triggers

The index runs automatically on workspace open via VS Code task `"Behavior Index on Startup"`.

## Related Files

- `behavior-index-rule.mdc` - The rule definition
- `behavior-index-cmd.md` - Command documentation
- `behavior-index-cmd.py` - Implementation
