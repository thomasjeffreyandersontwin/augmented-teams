# crc_bot-walkthrough - Available Actions

## Quick Execute (with action prompt)
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action ${1:action}${2:+ }${2:params}

## Available Actions:

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action rules
  # Optional: --message <value>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action rules --message "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action rules --message="value"

### clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action clarify
  # Optional: --answers <value>
  #   Dict mapping question keys to answer strings
  # Optional: --evidence-provided <value>
  #   Optional parameter
  # Optional: --context <value>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action clarify --answers "value" --evidence-provided "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action clarify --answers="value" --evidence-provided="value"

### strategy - decide approach by capturing assumptions and decision criteria
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action strategy
  # Optional: --assumptions <value>
  #   List of assumption strings
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action strategy --assumptions "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action strategy --assumptions="value"

### build - {{description}}
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action build
  # Optional: --scope <value>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action build --scope "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action build --scope="value"

### validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action validate
  # Optional: --scope <value>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all'|'files', 'value': <names|priorities|files>, 'exclude': <patterns>}
  # Optional: --background <value>
  #   Optional parameter
  # Optional: --skip-cross-file <bool>
  #   Optional parameter
  # Optional: --all-files <bool>
  #   Optional parameter
  # Optional: --force-full <bool>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action validate --scope "value" --background "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action validate --scope="value" --background="value"

### render - Render output documents and artifacts from knowledge graph using templates and synchronizers
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action render
  # Optional: --scope <value>
  #   Scope structure:
  #   {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action render --scope "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action render --scope="value"

### rules - Load behavior-specific rules into AI context for guidance on writing compliant content
python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action rules
  # Optional: --message <value>
  #   Optional parameter
  #
  # Full example (bash/sh):
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action rules --message "value"
  #
  # PowerShell: Use = syntax for parameters with values:
  # python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action rules --message="value"

## Common Patterns:
  # Work on specific epic:
  python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action build --scope "{'type': 'epic', 'value': ['Epic Name']}"

  # Validate with exclusions:
  python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action validate --skiprule rule_to_skip

  # Work on multiple stories:
  python agile_bot/bots/crc_bot/src/crc_bot_cli.py --behavior walkthrough --action build --scope "{'type': 'story', 'value': ['Story 1', 'Story 2']}"