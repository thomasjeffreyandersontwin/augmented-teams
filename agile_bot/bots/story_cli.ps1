# Story Bot REPL CLI Launcher (Windows/PowerShell)
#
# Usage (for humans):
#   .\story_bot_cli.ps1
#
# This launches the interactive REPL session for story_bot
# Bot behaviors are loaded from story_bot directory
# Working directory defaults to workspace root
#
# AI AGENTS:
#   Commands must be PIPED via echo, NOT passed as arguments!
#   PowerShell uses semicolons (;) to chain commands, NOT && (that's bash/cmd)
#   
#   WHAT DOES NOT WORK:
#     [X] python repl_main.py instructions
#     [X] python repl_main.py --command instructions
#   
#   WHAT WORKS:
#     [OK] echo 'instructions' | python repl_main.py
#   
#   Step 1: Set environment and pipe command:
#     cd C:\dev\augmented-teams
#     $env:PYTHONPATH = "C:\dev\augmented-teams"
#     $env:BOT_DIRECTORY = "C:\dev\augmented-teams\agile_bot\bots\story_bot"
#     $env:WORKING_AREA = "<project_path>"  # e.g. demo\mob_minion
#     echo "instructions" | python agile_bot/bots/base_bot/src/repl_cli/repl_main.py
#   
#   Step 2: Read output, do work (create files, etc.)
#   Step 3: Pipe next command: echo "next" | python repl_main.py
#   Step 4: Repeat for each step in workflow
#   
#   REPL exits after each command - this is NORMAL in piped mode

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$WORKSPACE_ROOT = Split-Path -Parent (Split-Path -Parent $SCRIPT_DIR)

# Set environment variables
$env:PYTHONPATH = $WORKSPACE_ROOT
$env:BOT_DIRECTORY = Join-Path $WORKSPACE_ROOT "agile_bot\bots\story_bot"
# WORKING_AREA is read from bot_config.json by repl_main.py - don't set it here

# Launch REPL
$REPL_PATH = Join-Path $WORKSPACE_ROOT "agile_bot/bots/base_bot/src/repl_cli/repl_main.py"
python $REPL_PATH
