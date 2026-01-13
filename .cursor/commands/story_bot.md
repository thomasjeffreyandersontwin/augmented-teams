# story_bot - REPL Status and Navigation

## Status
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'status' | python agile_bot/src/cli/cli_main.py

## Help
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'help' | python agile_bot/src/cli/cli_main.py

## Navigation
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'next' | python agile_bot/src/cli/cli_main.py
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'back' | python agile_bot/src/cli/cli_main.py

## Scope
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'scope all' | python agile_bot/src/cli/cli_main.py
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'scope "${1:story_name}"' | python agile_bot/src/cli/cli_main.py

## Path
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'path ${1:project_path}' | python agile_bot/src/cli/cli_main.py

## Exit
$env:BOT_DIRECTORY = 'C:\dev\augmented-teams\agile_bot\bots\story_bot'; $env:PYTHONPATH = 'C:\dev\augmented-teams'; echo 'exit' | python agile_bot/src/cli/cli_main.py