# Code Agent Behavior v1.1

**A self-managing AI behavior system for IDE agents.**

## What's New in v1.1

### Simplified Directory Structure
- **Flattened behavior files** - Moved all behavior files from nested `code-agent-behaviors/` subdirectory directly into `features/code-agent-behavior/`
- **Cleaner organization** - Eliminated unnecessary nesting for easier navigation and maintenance
- **No breaking changes** - All functionality remains the same, just simpler paths

### File Structure Changes
```
features/code-agent-behavior/
  ├── code-agent-behavior.json
  ├── code-agent-index.json
  ├── code-agent-consistency-rule.mdc    # Previously in code-agent-behaviors/
  ├── code-agent-consistency-cmd.md      # Previously in code-agent-behaviors/
  ├── code-agent-consistency-cmd.py      # Previously in code-agent-behaviors/
  ├── code-agent-index-rule.mdc          # Previously in code-agent-behaviors/
  ├── code-agent-index-cmd.md            # Previously in code-agent-behaviors/
  ├── code-agent-index-cmd.py            # Previously in code-agent-behaviors/
  ├── code-agent-structure-rule.mdc      # Previously in code-agent-behaviors/
  ├── code-agent-structure-cmd.py        # Previously in code-agent-behaviors/
  ├── code-agent-structure-*-cmd.md      # Previously in code-agent-behaviors/
  ├── code-agent-suggest-rule.mdc        # Previously in code-agent-behaviors/
  ├── code-agent-suggest-cmd.md          # Previously in code-agent-behaviors/
  ├── code-agent-sync-rule.mdc           # Previously in code-agent-behaviors/
  ├── code-agent-sync-cmd.md             # Previously in code-agent-behaviors/
  ├── code-agent-sync-cmd.py             # Previously in code-agent-behaviors/
  ├── code-agent-tasks.json              # Previously in code-agent-behaviors/
  └── docs/
```

### Migration from v1.0

If you're upgrading from v1.0:

1. **Extract the new release**:
   ```bash
   unzip code-agent-v1.1.zip -d your-project/
   ```

2. **Run sync** to update deployment:
   ```
   \code-agent-sync
   ```

That's it! The sync command will handle deploying from the new flattened structure.

## Key Features

**Behavior Structure** - Validate, fix, and create AI behaviors following structure and naming conventions.

**Behavior Sync** - Auto-deploy behaviors from source to `.cursor/` with file watchers and smart routing.

**Behavior Index** - Maintain a searchable JSON catalog of all behaviors with purposes and deployment locations.

**Behavior Consistency** - Use AI to detect semantic overlaps, contradictions, and inconsistencies across behaviors.

**Behavior Suggest** - Detect repetitive tasks and suggest creating new behaviors to capture patterns.

## Installation (New Users)

1. **Extract the release** to your project:
   ```bash
   unzip code-agent-v1.1.zip -d your-project/
   cd your-project
   ```

2. **Copy sync files** to bootstrap the system:
   ```bash
   cp features/code-agent-behavior/code-agent-sync-cmd.py commands/
   cp features/code-agent-behavior/code-agent-sync-cmd.md .cursor/commands/
   cp features/code-agent-behavior/code-agent-sync-rule.mdc .cursor/rules/
   ```

3. **Run sync** to deploy everything:
   ```
   \code-agent-sync
   ```

That's it! Sync deploys all behaviors, starts watchers, and indexes everything automatically.

## Available Commands

Follow this lifecycle when creating and managing behaviors:

### 1. Create New Behavior or Feature
`\code-agent-structure create <feature> <behavior-name>`

Scaffolds a new behavior with rule, command, and implementation files.

### 2. Validate
`\code-agent-structure validate [<feature>]`

Checks naming conventions and required sections are present.

### 3. Sync
`\code-agent-sync [<feature>]`

Deploys behaviors to `.cursor/` where AI reads them. Auto-starts watchers.

### 4. Update Index
`\code-agent-index [<feature>]`

Rebuilds global catalog so AI knows what behaviors exist.

### 5. Check Consistency (Ongoing)
`\code-agent-consistency [<feature>]`

Detects conflicts and overlaps across behaviors.

### 6. Suggest New Behaviors
`\code-agent-suggest`

AI detects repetitive guidance and offers to formalize it as a behavior.

**Other Commands:**
- `\code-agent-structure fix` - Auto-repair structure issues

## How It Works

1. **Mark feature for deployment** with `code-agent-behavior.json` containing `{"deployed": true}`
2. **Define behaviors** in the feature folder (rules, commands, Python, tasks)
3. **Sync deploys** them to `.cursor/` and `commands/` for the AI to read
4. **Index tracks** all behaviors across marked features
5. **Watchers auto-sync** when you make changes
6. **AI uses** the deployed behaviors during chat

## Requirements

- Python 3.12+
- Cursor IDE
- Optional: OpenAI API key (for consistency checking)

**Version:** 1.1  
**Released:** November 2, 2025  
**License:** [Your License]

