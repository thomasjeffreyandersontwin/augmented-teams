# story_bot-scenarios - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action ${1:action}${2:+ }${2:params}

## Available Actions:

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action rules
  # Optional: --message <str>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action rules --message "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action rules --message="value"

### clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action clarify
  # Optional: --key-questions-answered <dict>
  #   Optional parameter
  # Optional: --evidence-provided <dict>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action clarify --key-questions-answered '{"key": "value"}' --evidence-provided '{"key": "value"}'
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action clarify --key-questions-answered="{`"key`": `"value`"}" --evidence-provided="{`"key`": `"value`"}"

### strategy - Decide approach by presenting assumptions and decision criteria, then capturing decisions and assumptions
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action strategy
  # Optional: --decisions-made <dict>
  #   Optional parameter
  # Optional: --assumptions-made <list>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action strategy --decisions-made '{"key": "value"}' --assumptions-made "value1" "value2"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action strategy --decisions-made="{`"key`": `"value`"}" --assumptions-made="value1" "value2"

### build - Build knowledge graph for build
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action build
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action build --scope '{"key": "value"}'
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action build --scope="{`"key`": `"value`"}"

### validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action validate
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all'|'files', 'value': <names|priorities|files>, 'exclude': <patterns>}
  # Optional: --background <flag>
  #   Optional parameter
  # Optional: --skip-cross-file <flag>
  #   Optional parameter
  # Optional: --all-files <flag>
  #   Optional parameter
  # Optional: --force-full <flag>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action validate --scope '{"key": "value"}' --background
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action validate --scope="{`"key`": `"value`"}" --background

### render - Render output documents and artifacts from knowledge graph using templates and synchronizers
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action render
  # Optional: --scope <dict>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action render --scope '{"key": "value"}'
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action render --scope="{`"key`": `"value`"}"

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action rules
  # Optional: --message <str>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action rules --message "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action rules --message="value"

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate with exclusions:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action validate --skiprule rule_to_skip

  # Work on multiple stories:
  python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior scenarios --action build --scope "{'type': 'story', 'value': ['Story 1', 'Story 2']}"