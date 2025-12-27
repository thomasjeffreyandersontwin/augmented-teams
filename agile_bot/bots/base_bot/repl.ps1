# Interactive REPL Launcher for Base Bot (Windows/PowerShell)
#
# Usage:
#   .\repl.ps1
#
# This launches the interactive REPL session

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$WORKSPACE_ROOT = (Resolve-Path "$SCRIPT_DIR\..\..\..").Path

# Set environment variables
$env:PYTHONPATH = $WORKSPACE_ROOT
$env:BOT_DIRECTORY = $SCRIPT_DIR

# Launch REPL
python "$SCRIPT_DIR\src\repl_cli\repl_main.py"


