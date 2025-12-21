# story_bot-prioritization - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action ${1:action}${2:+ }${2:params}

## Available Actions:

### clarify - Gather context
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action clarify
  # Optional: --key_questions_answered '{"q1": "answer"}' --evidence_provided '{"type": "content"}'

### strategy - Decide approach
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action strategy
  # Optional: --decisions_made '{"decision": "value"}' --assumptions_made '["assumption"]'

### build - Build knowledge graph
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action build
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"
  # Scope increment: --scope "{'type': 'increment', 'value': [1, 2]}"

### validate - Validate against rules
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action validate
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"
  # Scope files: --scope "{'type': 'files', 'value': ['path/to/file'], 'exclude': ['*.test.js']}"
  # Skip rules: --skiprule rule_name

  **NOTE:** For code behavior, validation runs in background.
  **AI MUST:** Poll status file every 10 seconds and report progress until complete.

### render - Generate output artifacts
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action render
  # Scope all: (default)
  # Scope epic: --scope "{'type': 'epic', 'value': ['Epic Name']}"
  # Scope story: --scope "{'type': 'story', 'value': ['Story Name']}"

### rules - Inject rules into AI context
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action rules
  # Optional: --message "your request here"
  # Non-workflow action: Can be invoked anytime
  # Loads behavior rules and user message into AI context

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate with exclusions:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action validate --skiprule rule_to_skip

  # Work on multiple stories:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior prioritization --action build --scope "{' type': 'story', 'value': ['Story 1', 'Story 2']}"