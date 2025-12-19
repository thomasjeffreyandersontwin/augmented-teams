from pathlib import Path
from typing import Dict, Set
from agile_bot.bots.base_bot.src.utils import read_json_file
import json

class CursorCommandGenerator:

    def __init__(self, workspace_root: Path, bot_location: Path, bot_name: str):
        self.workspace_root = workspace_root
        self.bot_location = bot_location
        self.bot_name = bot_name

    def generate_cursor_commands(self, cli_script_path: Path, behaviors: list) -> Dict[str, Path]:
        commands_dir = self._ensure_commands_directory()
        python_command = self._get_python_command(cli_script_path)
        current_command_files = self._get_current_command_files(commands_dir)
        commands = self._generate_base_commands(commands_dir, python_command)
        self._generate_behavior_commands(commands_dir, python_command, behaviors, commands)
        self._remove_obsolete_command_files(commands_dir, current_command_files, commands)
        return commands

    def _ensure_commands_directory(self) -> Path:
        commands_dir = self.workspace_root / '.cursor' / 'commands'
        commands_dir.mkdir(parents=True, exist_ok=True)
        return commands_dir

    def _get_python_command(self, cli_script_path: Path) -> str:
        rel_cli_script_path = cli_script_path.relative_to(self.workspace_root) if cli_script_path.is_absolute() else self.bot_location / 'src' / cli_script_path.name
        return f"python {str(rel_cli_script_path).replace('\\', '/')}"

    def _generate_base_commands(self, commands_dir: Path, python_command: str) -> Dict[str, Path]:
        commands = {}
        commands[f'{self.bot_name}'] = self._write_command_file(commands_dir / f'{self.bot_name}.md', python_command)
        commands[f'{self.bot_name}-continue'] = self._write_command_file(commands_dir / f'{self.bot_name}-continue.md', f'{python_command} --close')
        commands[f'{self.bot_name}-help'] = self._write_command_file(commands_dir / f'{self.bot_name}-help.md', f'{python_command} --help-cursor')
        return commands

    def _generate_behavior_commands(self, commands_dir: Path, python_command: str, behaviors: list, commands: dict):
        for behavior_name in behaviors:
            behavior_command = f'{python_command} --behavior {behavior_name} --action ${{1:}}${{2:+ }}${{2:}}'
            commands[f'{self.bot_name}-{behavior_name}'] = self._write_command_file(commands_dir / f'{self.bot_name}-{behavior_name}.md', behavior_command)

    def _get_current_command_files(self, commands_dir: Path) -> Set[Path]:
        if not commands_dir.exists():
            return set()
        bot_prefix = f'{self.bot_name}'
        existing_files = set()
        for file_path in commands_dir.glob(f'{bot_prefix}*.md'):
            existing_files.add(file_path)
        return existing_files

    def _remove_obsolete_command_files(self, commands_dir: Path, existing_files: Set[Path], current_commands: Dict[str, Path]):
        current_file_paths = set(current_commands.values())
        for file_path in existing_files:
            if file_path not in current_file_paths:
                file_path.unlink(missing_ok=True)

    def _write_command_file(self, file_path: Path, command: str) -> Path:
        file_path.write_text(command, encoding='utf-8')
        return file_path

    def update_bot_registry(self, cli_script_path: Path) -> Path:
        registry_path = self._get_registry_path()
        registry = self._load_registry(registry_path)
        rel_cli_path = self._get_relative_cli_path(cli_script_path)
        registry[self.bot_name] = {'trigger_patterns': self._load_bot_trigger_patterns(), 'cli_path': rel_cli_path}
        registry_path.write_text(json.dumps(registry, indent=2, sort_keys=True), encoding='utf-8')
        return registry_path

    def _get_registry_path(self) -> Path:
        registry_path = self.workspace_root / 'agile_bot' / 'bots' / 'registry.json'
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        return registry_path

    def _load_registry(self, registry_path: Path) -> dict:
        if registry_path.exists():
            try:
                return read_json_file(registry_path)
            except (json.JSONDecodeError, FileNotFoundError):
                return {}
        return {}

    def _get_relative_cli_path(self, cli_script_path: Path) -> str:
        if cli_script_path.is_absolute():
            return str(cli_script_path.relative_to(self.workspace_root)).replace('\\', '/')
        return str(self.bot_location / 'src' / cli_script_path.name).replace('\\', '/')

    def _load_bot_trigger_patterns(self) -> list:
        trigger_file = self.workspace_root / self.bot_location / 'trigger_words.json'
        if not trigger_file.exists():
            return []
        try:
            trigger_data = read_json_file(trigger_file)
            return trigger_data.get('patterns', [])
        except (json.JSONDecodeError, FileNotFoundError):
            return []