# story_bot-code - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action ${1:action}${2:+ }${2:params}

## Available Actions:

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules
  # Optional: --message <str>
  #   Optional parameter
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules --message "value"

### strategy - Decide approach by presenting assumptions and decision criteria, then capturing decisions and assumptions
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action strategy
  # Optional: --decisions-made <dict>
  #   Optional parameter
  # Optional: --assumptions-made <list>
  #   Optional parameter
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action strategy --decisions-made '{"key": "value"}' --assumptions-made "value1" "value2"

### render - Render output documents and artifacts from knowledge graph using templates and synchronizers
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action render
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action render --scope '{"key": "value"}'

### validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate
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
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --scope '{"key": "value"}' --background

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules
  # Optional: --message <str>
  #   Optional parameter
  #
  # Full example:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action rules --message "value"

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate with exclusions:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action validate --skiprule rule_to_skip

  # Work on multiple stories:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior code --action build --scope "{'type': 'story', 'value': ['Story 1', 'Story 2']}"