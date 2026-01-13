# story_bot_discovery - Navigate to Discovery Behavior

## Navigate to Behavior
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'discovery' | python agile_bot/src/cli/cli_main.py

## Navigate to Specific Action
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'discovery.${1|rules|clarify|strategy|build|validate|render|}' | python agile_bot/src/cli/cli_main.py

## Available Actions:

- rules - Load behavior-specific rules into AI context for guidance on writing compliant content
- clarify - Gather context by asking required questions and collecting evidence in order to increase understanding
- strategy - decide approach by capturing assumptions and decision criteria
- build - Build knowledge graph for build
- validate - Validate knowledge graph and/or artifacts against behavior-specific rules, checking for violations and compliance
- render - Render output documents and artifacts from knowledge graph using templates and synchronizers