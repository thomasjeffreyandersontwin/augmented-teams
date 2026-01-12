# Crc Bot CLI Wrapper (PowerShell)

    $SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

    if (-not $env:WORKING_AREA) {
        $env:WORKING_AREA = (Resolve-Path "$SCRIPT_DIR\..\..\..").Path
    }

    python "$SCRIPT_DIR\src\crc_bot_cli.py" $args
    