# Interactive REPL Launcher for Story Bot (Windows/PowerShell)
#
# Usage:
#   .\repl.ps1
#
# This launches the interactive REPL session for story_bot
# Bot behaviors are loaded from story_bot directory
# Working directory defaults to workspace root

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$WORKSPACE_ROOT = (Resolve-Path "$SCRIPT_DIR\..\..\..").Path

# Set environment variables
$env:PYTHONPATH = $WORKSPACE_ROOT
$env:BOT_DIRECTORY = $SCRIPT_DIR  # This is story_bot - where behaviors are

# Launch REPL
python "$SCRIPT_DIR\..\base_bot\src\repl_cli\repl_main.py"

