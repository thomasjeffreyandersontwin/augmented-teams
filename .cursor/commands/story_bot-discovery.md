# story_bot-discovery - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action ${1:action}${2:+ }${2:params}

## Available Actions:

### clarify - Gather context
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action clarify
  # Optional: --key_questions_answered '{"q1": "answer"}' --evidence_provided '{"type": "content"}'

### strategy - Decide approach
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action strategy
  # Optional: --decisions_made '{"decision": "value"}' --assumptions_made '["assumption"]'

### build - Build knowledge graph
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action build
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"
  # Scope increment: --scope "{'type': 'increment', 'value': [1, 2]}"

### validate - Validate against rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action validate
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"
  # Scope files: --scope "{'type': 'files', 'value': ['path/to/file'], 'exclude': ['*.test.js']}"
  # Skip rules: --skiprule rule_name

### render - Generate output artifacts
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action render
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate with exclusions:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action validate --skiprule rule_to_skip

  # Work on multiple stories:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior discovery --action build --scope "{' type': 'story', 'value': ['Story 1', 'Story 2']}"