# Code Agent Behavior v1.0

**A self-managing AI behavior system for IDE agents.**

## What is Code Agent Behavior?

Code Agent Behavior adds a bit ot organization to Cursor's AI customization capability by letting you define, manage, and deploy descrete AI behaviors in your IDE. It keeps AI behaviuors modular, versioned, and portable.

Instead of scattered prompts and rules, you get a structured system where you house related rules, commands, configuration for tools, and code automations all in one place, and then deploy them to where cursor needs them to be in order to use them.

## Key Features

**Behavior Structure** - Validate, fix, and create AI behaviors following structure and naming conventions.

**Behavior Sync** - Auto-deploy behaviors from source to `.cursor/` with file watchers and smart routing.

**Behavior Index** - Maintain a searchable JSON catalog of all behaviors with purposes and deployment locations.
**Behavior Consistency** - Use AI to detect semantic overlaps, contradictions, and inconsistencies across behaviors.

**Behavior Suggest** - Detect repetitive tasks and suggest creating new behaviors to capture patterns.

## Installation

1. **Extract the release** to your project:
   ```bash
   unzip code-agent-behavior-v1.0.zip -d your-project/
   cd your-project
   ```

2. **Copy sync files** to bootstrap the system:
   ```bash
   cp features/code-agent-behavior/code-agent-behavior-sync-cmd.py commands/
   cp features/code-agent-behavior/code-agent-behavior-sync-cmd.md .cursor/commands/
   cp features/code-agent-behavior/code-agent-behavior-sync-rule.mdc .cursor/rules/
   ```

3. **Run sync** to deploy everything:
   ```
   
   \code-agent-behavior-sync
   ```

That's it! Sync deploys all behaviors, starts watchers, and indexes everything automatically.

## Available Commands

Follow this lifecycle when creating and managing behaviors:

### 1. Create New Behavior or Feature
`\code-agent-behavior-structure create <feature> <behavior-name>`

Scaffolds a new behavior with rule, command, and implementation files.
> *Example:* Create "tdd-test-scaffolding" behavior. AI generates empty test methods from requirements, enforcing test-first discipline.

### 2. Validate
`\code-agent-behavior-structure validate [<feature>]`

Checks naming conventions and required sections are present.
> *Example:* Ensures TDD behaviors specify *when* tests must run before code, not just that they should.

### 3. Sync
`\code-agent-behavior-sync [<feature>]`

Deploys behaviors to `.cursor/` where AI reads them. Auto-starts watchers.
> *Example:* TDD rules now active in every chat. AI blocks production code until tests exist and fail.

### 4. Update Index
`\code-agent-behavior-index [<feature>]`

Rebuilds global catalog so AI knows what behaviors exist.
> *Example:* AI discovers your TDD behaviors and references them when proposing implementation approaches.

### 5. Check Consistency (Ongoing)
`\code-agent-behavior-consistency [<feature>]`

Detects conflicts and overlaps across behaviors.
> *Example:* Flags conflict between "strict-tdd: tests always first" and "spike-solutions: explore code before tests."

### 6. Suggest New Behaviors
`\code-agent-behavior-suggest`

AI detects repetitive guidance and offers to formalize it as a behavior.
> *Example:* After repeatedly saying "extract test helpers to conftest.py," AI suggests creating a "tdd-test-organization" behavior.

**Other Commands:**
- `\code-agent-behavior-structure fix` - Auto-repair structure issues

## File Structure

```
features/code-agent-behavior/              # The behavior management system
  ├── code-agent-behavior.json            # Marker file (deployed: true)
  ├── code-agent-behavior-index.json      # Local behavior catalog
  ├── code-agent-behavior-outline.md      # Feature overview
  ├── *-rule.mdc                          # Behavior rules (when/then)
  ├── *-cmd.md                            # Command documentation
  ├── *-cmd.py                            # Python implementations
  ├── *-tasks.json                        # VS Code tasks
  └── docs/                                # Feature documentation

features/tdd/                              # Your custom behavior feature
  ├── code-agent-behavior.json            # Marker file (deployed: true) - marks this for deployment
  ├── tdd-index.json
  ├── tdd-outline.md
  ├── tdd-red-green-refactor-rule.mdc
  ├── tdd-test-scaffolding-cmd.md
  ├── tdd-test-scaffolding-cmd.py
  └── tdd-tasks.json
```

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

## Commands

### Structure Commands
```bash
# Validate all behaviors
python commands/code-agent-behavior-structure-cmd.py validate

# Fix structure issues
python commands/code-agent-behavior-structure-cmd.py fix

# Create new behavior
python commands/code-agent-behavior-structure-cmd.py create <feature> <behavior-name>
```

### Sync Commands
```bash
# Sync all behaviors
python commands/code-agent-behavior-sync-cmd.py

# Sync specific feature
python commands/code-agent-behavior-sync-cmd.py <feature-name>

# Watch mode (auto-sync on changes)
python commands/code-agent-behavior-sync-cmd.py watch
```

```

**Version:** 1.0  
**Released:** November 1, 2025  
**License:** [Your License]

