# Crc Bot CLI Wrapper (PowerShell)

    $SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

    if (-not $env:WORKING_DIR) {
        $env:WORKING_DIR = (Resolve-Path "$SCRIPT_DIR\..\..\..").Path
    }

    python "$SCRIPT_DIR\src\crc_bot_cli.py" $args
    