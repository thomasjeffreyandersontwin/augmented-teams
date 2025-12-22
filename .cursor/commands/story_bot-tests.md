# story_bot-tests - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action ${1:action}${2:+ }${2:params}

## Available Actions:

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules
  # Optional: --message <str>
  #   Optional parameter
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules --message "value"

### build - Build/update the knowledge graph by reading story markdown files and generating story-graph
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action build
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action build --scope '{"key": "value"}'

### render - Render output documents and artifacts from knowledge graph using templates and synchronizers
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action render
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action render --scope '{"key": "value"}'

### validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action validate
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all'|'files', 'value': <names|priorities|files>, 'exclude': <patterns>}
  # Optional: --background <flag>
  #   Optional parameter
  # Optional: --skip-cross-file <flag>
  #   Optional parameter
  # Optional: --all-files <flag>
  #   Optional parameter
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action validate --scope '{"key": "value"}' --background

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules
  # Optional: --message <str>
  #   Optional parameter
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action rules --message "value"

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate with exclusions:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action validate --skiprule rule_to_skip

  # Work on multiple stories:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action build --scope "{'type': 'story', 'value': ['Story 1', 'Story 2']}"