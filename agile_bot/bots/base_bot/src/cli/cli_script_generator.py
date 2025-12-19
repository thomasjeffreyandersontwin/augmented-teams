import stat
from pathlib import Path
from typing import Dict, Any

class CliScriptGenerator:

    def __init__(self, workspace_root: Path, bot_location: Path, bot_name: str):
        self.workspace_root = workspace_root
        self.bot_location = bot_location
        self.bot_name = bot_name

    def generate_python_cli_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        src_dir = bot_dir / 'src'
        src_dir.mkdir(parents=True, exist_ok=True)
        cli_file = src_dir / f'{self.bot_name}_cli.py'
        cli_code = f'''#!/usr/bin/env python3\n"""\n{self.bot_name.title().replace('_', ' ')} CLI Entry Point\n\nCommand-line interface for {self.bot_name} using BaseBotCli.\n\nUsage:\n    {self.bot_name} [--behavior <name>] [--action <name>] [--options]\n    {self.bot_name} --help\n    {self.bot_name} --list\n    {self.bot_name} --behavior <name> --list\n    {self.bot_name} --close\n\nExamples:\n    {self.bot_name}\n    {self.bot_name} --behavior exploration\n    {self.bot_name} --behavior exploration --action clarify\n    {self.bot_name} --behavior exploration --action clarify --increment_file=increment.txt\n"""\nfrom pathlib import Path\nimport sys\nimport os\nimport json\n\npython_workspace_root = Path(__file__).parent.parent.parent.parent.parent\nif str(python_workspace_root) not in sys.path:\n    sys.path.insert(0, str(python_workspace_root))\n\n\nbot_directory = Path(__file__).parent.parent\nos.environ['BOT_DIRECTORY'] = str(bot_directory)\n\nif 'WORKING_AREA' not in os.environ and 'WORKING_DIR' not in os.environ:\n    config_path = bot_directory / 'bot_config.json'\n    if config_path.exists():\n        bot_config = json.loads(config_path.read_text(encoding='utf-8'))\n        if 'mcp' in bot_config and 'env' in bot_config['mcp']:\n            mcp_env = bot_config['mcp']['env']\n            if 'WORKING_AREA' in mcp_env:\n                os.environ['WORKING_AREA'] = mcp_env['WORKING_AREA']\n        elif 'WORKING_AREA' in bot_config:\n            os.environ['WORKING_AREA'] = bot_config['WORKING_AREA']\n\n\nfrom agile_bot.bots.base_bot.src.bot.workspace import get_bot_directory, get_workspace_directory\nfrom agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli\n\n\ndef main():\n    """Main CLI entry point.\n\n    Environment variables are bootstrapped before import:\n    - BOT_DIRECTORY: Self-detected from script location\n    - WORKING_AREA: Read from bot_config.json (or pre-set by user)\n    \n    All subsequent code reads from these environment variables.\n    """\n    bot_directory = get_bot_directory()\n    workspace_directory = get_workspace_directory()\n\n    bot_name = \'{self.bot_name}'\n    bot_config_path = bot_directory / 'bot_config.json'\n    \n    cli = BaseBotCli(\n        bot_name=bot_name,\n        bot_config_path=bot_config_path\n    )\n    \n    cli.main()\n\n\nif __name__ == '__main__':\n    main()\n'''
        cli_file.write_text(cli_code, encoding='utf-8')
        cli_file.chmod(cli_file.stat().st_mode | stat.S_IEXEC)
        return cli_file

    def generate_shell_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        script_file = bot_dir / f'{self.bot_name}_cli'
        script_content = f'#!/bin/bash\n\n    SCRIPT_DIR="$(cd "$(dirname "${{BASH_SOURCE[0]}}")" && pwd)"\n\n    export WORKING_DIR="${{WORKING_DIR:-$(cd "$SCRIPT_DIR/../../.." && pwd)}}"\n\n    python3 "$SCRIPT_DIR/src/{self.bot_name}_cli.py" "$@"\n    '
        script_file.write_text(script_content, encoding='utf-8')
        script_file.chmod(script_file.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        return script_file

    def generate_powershell_script(self) -> Path:
        bot_dir = self.workspace_root / self.bot_location
        script_file = bot_dir / f'{self.bot_name}_cli.ps1'
        script_content = f"""# {self.bot_name.title().replace('_', ' ')} CLI Wrapper (PowerShell)\n\n    $SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path\n\n    if (-not $env:WORKING_DIR) {{\n        $env:WORKING_DIR = (Resolve-Path "$SCRIPT_DIR\\..\\..\\..").Path\n    }}\n\n    python "$SCRIPT_DIR\\src\\{self.bot_name}_cli.py" $args\n    """
        script_file.write_text(script_content, encoding='utf-8')
        return script_file
