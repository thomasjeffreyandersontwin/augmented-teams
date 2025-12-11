# Story Bot CLI Wrapper (PowerShell)

# Get script directory
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

# Set WORKING_DIR environment variable rather than forcing a "workspace_root".
# Tools/invokers should set WORKING_DIR explicitly. If not set, default to
# repository root derived from the script location (development fallback).
$env:WORKING_DIR = $env:WORKING_DIR -or (Resolve-Path "$SCRIPT_DIR\..\..\..").Path

# Run Python CLI script with all arguments passed through
python "$SCRIPT_DIR\src\story_bot_cli.py" $args
