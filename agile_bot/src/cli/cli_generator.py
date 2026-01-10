"""
CLI Generator for bots.

Generates shell scripts and PowerShell scripts that call the new CLI entry point.
"""
from pathlib import Path
from typing import Dict


class CliGenerator:
    """Generates CLI scripts (shell and PowerShell) for bots."""
    
    def __init__(self, workspace_root: Path, bot_location: str):
        """
        Initialize CLI generator.
        
        Args:
            workspace_root: Root directory of the workspace
            bot_location: Relative path to bot directory (e.g., 'agile_bot/bots/story_bot')
        """
        self.workspace_root = Path(workspace_root)
        self.bot_location = Path(bot_location)
        self.bot_name = self.bot_location.name
    
    def generate_cli_code(self) -> Dict[str, str]:
        """
        Generate all CLI scripts.
        
        Returns:
            Dictionary with paths to generated files:
            - 'cli_script': Path to shell script (.sh)
            - 'cli_powershell': Path to PowerShell script (.ps1)
            - 'cli_python': Path to Python CLI entry point (for compatibility, returns module path)
        """
        results = {}
        
        # Generate shell script
        shell_script_path = self._create_shell_script()
        results['cli_script'] = str(shell_script_path)
        
        # Generate PowerShell script
        powershell_script_path = self._create_powershell_script()
        results['cli_powershell'] = str(powershell_script_path)
        
        # For compatibility, return the module path (not a file path)
        results['cli_python'] = 'agile_bot.src.cli.cli_main'
        
        return results
    
    def _create_shell_script(self) -> Path:
        """Create shell script (.sh) for Unix/Linux/Mac."""
        script_name = 'story_cli.sh' if self.bot_name == 'story_bot' else f'{self.bot_name}_cli.sh'
        script_file = self.workspace_root / 'agile_bot' / script_name
        
        script_content = f"""#!/bin/bash
# {self.bot_name.replace('_', ' ').title()} CLI Launcher (Unix/Linux/Mac)
#
# Usage (for humans):
#   ./{script_name}
#
# This launches the interactive CLI session for {self.bot_name}
# Bot behaviors are loaded from {self.bot_location.name} directory
# Working directory defaults to workspace root
#
# AI AGENTS:
#   Commands must be PIPED via echo, NOT passed as arguments!
#   
#   WHAT DOES NOT WORK:
#     [X] python -m agile_bot.src.cli.cli_main instructions
#     [X] python -m agile_bot.src.cli.cli_main --command instructions
#   
#   WHAT WORKS:
#     [OK] echo 'instructions' | python -m agile_bot.src.cli.cli_main
#   
#   Step 1: Set environment and pipe command:
#     cd {self.workspace_root}
#     export PYTHONPATH="{self.workspace_root}"
#     export BOT_DIRECTORY="{self.workspace_root}/{self.bot_location}"
#     export WORKING_AREA="<project_path>"  # e.g. demo/mob_minion
#     echo "instructions" | python -m agile_bot.src.cli.cli_main
#   
#   Step 2: Read output, do work (create files, etc.)
#   Step 3: Pipe next command: echo "next" | python -m agile_bot.src.cli.cli_main
#   Step 4: Repeat for each step in workflow
#   
#   CLI exits after each command - this is NORMAL in piped mode

SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Set environment variables
export PYTHONPATH="$WORKSPACE_ROOT"
export BOT_DIRECTORY="$WORKSPACE_ROOT/{self.bot_location}"
# WORKING_AREA is read from bot_config.json by cli_main - don't set it here

# Launch CLI
python -m agile_bot.src.cli.cli_main
"""
        script_file.write_text(script_content, encoding='utf-8')
        script_file.chmod(0o755)  # Make executable
        
        return script_file
    
    def _create_powershell_script(self) -> Path:
        """Create PowerShell script (.ps1) for Windows."""
        script_name = 'story_cli.ps1' if self.bot_name == 'story_bot' else f'{self.bot_name}_cli.ps1'
        script_file = self.workspace_root / 'agile_bot' / script_name
        
        script_content = f"""# {self.bot_name.replace('_', ' ').title()} CLI Launcher (Windows/PowerShell)
#
# Usage (for humans):
#   .\\{script_name}
#
# This launches the interactive CLI session for {self.bot_name}
# Bot behaviors are loaded from {self.bot_location.name} directory
# Working directory defaults to workspace root
#
# AI AGENTS:
#   Commands must be PIPED via echo, NOT passed as arguments!
#   PowerShell uses semicolons (;) to chain commands, NOT && (that's bash/cmd)
#   
#   WHAT DOES NOT WORK:
#     [X] python -m agile_bot.src.cli.cli_main instructions
#     [X] python -m agile_bot.src.cli.cli_main --command instructions
#   
#   WHAT WORKS:
#     [OK] echo 'instructions' | python -m agile_bot.src.cli.cli_main
#   
#   Step 1: Set environment and pipe command:
#     cd {self.workspace_root}
#     $env:PYTHONPATH = "{self.workspace_root}"
#     $env:BOT_DIRECTORY = "{self.workspace_root}\\{self.bot_location}"
#     $env:WORKING_AREA = "<project_path>"  # e.g. demo\\mob_minion
#     echo "instructions" | python -m agile_bot.src.cli.cli_main
#   
#   Step 2: Read output, do work (create files, etc.)
#   Step 3: Pipe next command: echo "next" | python -m agile_bot.src.cli.cli_main
#   Step 4: Repeat for each step in workflow
#   
#   CLI exits after each command - this is NORMAL in piped mode

$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$WORKSPACE_ROOT = Split-Path -Parent $SCRIPT_DIR

# Set environment variables
$env:PYTHONPATH = $WORKSPACE_ROOT
$env:BOT_DIRECTORY = Join-Path $WORKSPACE_ROOT "{self.bot_location}"
# WORKING_AREA is read from bot_config.json by cli_main - don't set it here

# Launch CLI
python -m agile_bot.src.cli.cli_main
"""
        script_file.write_text(script_content, encoding='utf-8')
        
        return script_file
