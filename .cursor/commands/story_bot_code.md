# story_bot_code - Navigate to Code Behavior

## Navigate to Behavior
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'code' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py

## Navigate to Specific Action
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'code.${1|rules|build|validate|}' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py

## Available Actions:

- rules - Load behavior-specific rules into AI context for guidance on writing compliant content
- build - Build knowledge graph for build
- validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance