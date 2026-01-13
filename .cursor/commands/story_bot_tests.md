# story_bot_tests - Navigate to Tests Behavior

## Navigate to Behavior
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'tests' | python agile_bot/src/cli/cli_main.py

## Navigate to Specific Action
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'tests.${1|rules|build|validate|}' | python agile_bot/src/cli/cli_main.py

## Available Actions:

- rules - Load behavior-specific rules into AI context for guidance on writing compliant content
- build - Build knowledge graph for build
- validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance