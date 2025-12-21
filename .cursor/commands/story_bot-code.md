# story_bot-code - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action ${1:action}${2:+ }${2:params}

## Available Actions:

### clarify - Gather context
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action clarify
  # Optional: --key_questions_answered '{"q1": "answer"}' --evidence_provided '{"type": "content"}'

### strategy - Decide approach
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action strategy
  # Optional: --decisions_made '{"decision": "value"}' --assumptions_made '["assumption"]'

### build - Build knowledge graph
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action build
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"
  # Scope increment: --scope "{'type': 'increment', 'value': [1, 2]}"

### validate - Validate against rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"
  # Scope files: --scope "{'type': 'files', 'value': ['path/to/file'], 'exclude': ['*.test.js'], 'skiprule': ['rule_name']}"
  # Force full scan: --force-full
  # Skip cross-file scan: --skip-cross-file

  **NOTE:** For code behavior, validation runs in background.
  **AI MUST:** Poll status file every 10 seconds and report progress until complete.

### render - Generate output artifacts
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action render
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate specific files with exclusions and skip rules:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --scope "{'type': 'files', 'value': ['path/to/file.py'], 'exclude': ['test_*.py'], 'skiprule': ['eliminate_duplication']}"

  # Full validation scan (all files, all rules):
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --force-full

  # Quick validation (skip cross-file duplication check):
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --skip-cross-file

  # Work on multiple stories:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action build --scope "{'type': 'story', 'value': ['Story 1', 'Story 2']}"