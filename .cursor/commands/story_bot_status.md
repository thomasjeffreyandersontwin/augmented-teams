# story_bot_status - Display Current Bot Status

Display current position in workflow, active scope, and available commands.

## Show Status
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'status' | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py