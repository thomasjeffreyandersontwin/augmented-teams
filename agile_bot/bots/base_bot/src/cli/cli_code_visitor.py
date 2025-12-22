import stat
from pathlib import Path
from typing import Dict, Any
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.generator.help_context import BehaviorHelpContext, ActionHelpContext
from agile_bot.bots.base_bot.src.bot.bot import Bot

class CliCodeVisitor(Visitor):
    
    def __init__(self, workspace_root: Path, bot_location: Path, bot):
        super().__init__(bot=bot)
        self.workspace_root = workspace_root
        self.bot_location = bot_location
    
    def visit_header(self, bot_name: str) -> None:
        pass
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        pass
    
    def visit_action(self, context: ActionHelpContext) -> None:
        pass
    
    def visit_action_help_section_header(self) -> None:
        pass
    
    def visit_footer(self) -> None:
        self._create_python_cli_script()
        self._create_shell_script()
        self._create_powershell_script()
    
    def _create_python_cli_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        src_dir = bot_dir / 'src'
        src_dir.mkdir(parents=True, exist_ok=True)
        cli_file = src_dir / f'{self.bot.bot_name}_cli.py'
        cli_code = self._build_python_cli_code()
        return self._write_executable_file(cli_file, cli_code, executable=True)
    
    def _build_python_cli_code(self) -> str:
        docstring = self._build_cli_docstring()
        imports = self._build_cli_imports()
        bootstrap = self._build_cli_bootstrap()
        main_function = self._build_cli_main_function()
        return f'''#!/usr/bin/env python3
{docstring}
{imports}

{bootstrap}

{main_function}
'''
    
    def _build_cli_docstring(self) -> str:
        bot_title = self.bot.bot_name.title().replace('_', ' ')
        return f'''"""
{bot_title} CLI Entry Point

Command-line interface for {self.bot.bot_name} using BaseBotCli.

Usage:
    {self.bot.bot_name} [--behavior <name>] [--action <name>] [--options]
    {self.bot.bot_name} --help
    {self.bot.bot_name} --list
    {self.bot.bot_name} --behavior <name> --list
    {self.bot.bot_name} --close

Examples:
    {self.bot.bot_name}
    {self.bot.bot_name} --behavior exploration
    {self.bot.bot_name} --behavior exploration --action clarify
    {self.bot.bot_name} --behavior exploration --action clarify @increment.txt
"""'''
    
    def _build_cli_imports(self) -> str:
        return '''from pathlib import Path
import sys
import os
import json

python_workspace_root = Path(__file__).parent.parent.parent.parent.parent
if str(python_workspace_root) not in sys.path:
    sys.path.insert(0, str(python_workspace_root))


bot_directory = Path(__file__).parent.parent
os.environ['BOT_DIRECTORY'] = str(bot_directory)

if 'WORKING_AREA' not in os.environ and 'WORKING_DIR' not in os.environ:
    config_path = bot_directory / 'bot_config.json'
    if config_path.exists():
        bot_config = json.loads(config_path.read_text(encoding='utf-8'))
        if 'mcp' in bot_config and 'env' in bot_config['mcp']:
            mcp_env = bot_config['mcp']['env']
            if 'WORKING_AREA' in mcp_env:
                os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']
        elif 'WORKING_AREA' in bot_config:
            os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']


from agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory
from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli'''
    
    def _build_cli_bootstrap(self) -> str:
        return ''
    
    def _build_cli_main_function(self) -> str:
        return f'''def main():
    """Main CLI entry point.

    Environment variables are bootstrapped before import:
    - BOT_DIRECTORY: Self-detected from script location
    - WORKING_AREA: Read from bot_config.json (or pre-set by user)
    
    All subsequent code reads from these environment variables.
    """
    bot_directory = get_bot_directory()
    workspace_directory = get_workspace_directory()

    bot_name = '{self.bot.bot_name}'
    bot_config_path = bot_directory / 'bot_config.json'
    
    cli = BaseBotCli(
        bot_name=bot_name,
        bot_config_path=bot_config_path
    )
    
    cli.main()


if __name__ == '__main__':
    main()'''

    def _create_shell_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        script_file = bot_dir / f'{self.bot.bot_name}_cli'
        script_content = f'#!/bin/bash\n\n    SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"\n\n    export WORKING_DIR="${{WORKING_DIR:-$(cd "$SCRIPT_DIR/../../.." && pwd)}}"\n\n    python3 "$SCRIPT_DIR/src/{self.bot.bot_name}_cli.py" "$@"\n    '
        return self._write_executable_file(script_file, script_content, executable=True, group_and_other=True)
    
    def _write_executable_file(self, file_path: Path, content: str, executable: bool = False, group_and_other: bool = False) -> Path:
        file_path.write_text(content, encoding='utf-8')
        if executable:
            mode = stat.S_IEXEC
            if group_and_other:
                mode |= stat.S_IXGRP | stat.S_IXOTH
            file_path.chmod(file_path.stat().st_mode | mode)
        return file_path

    def _create_powershell_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        script_file = bot_dir / f'{self.bot.bot_name}_cli.ps1'
        script_content = f"""# {self.bot.bot_name.title().replace('_', ' ')} CLI Wrapper (PowerShell)

    $SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path

    if (-not $env:WORKING_DIR) {{
        $env:WORKING_DIR = (Resolve-Path "$SCRIPT_DIR\\..\\..\\..").Path
    }}

    python "$SCRIPT_DIR\\src\\{self.bot.bot_name}_cli.py" $args
    """
        script_file.write_text(script_content, encoding='utf-8')
        return script_file
