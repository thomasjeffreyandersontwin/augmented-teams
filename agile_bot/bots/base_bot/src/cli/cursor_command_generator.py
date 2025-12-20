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
        help_content = self._build_help_command_content(python_command)
        commands[f'{self.bot_name}-help'] = self._write_command_file(commands_dir / f'{self.bot_name}-help.md', help_content)
        # Base tools (not behavior-scoped)
        commands[f'{self.bot_name}-get_working_dir'] = self._write_command_file(
            commands_dir / f'{self.bot_name}-get_working_dir.md',
            f'{python_command} --action get_working_dir'
        )
        set_working_dir_syntax = (
            f"{python_command} --action set_working_dir "
            "${1:/path/to/workspace}${2:+ }${2:persist=true|false}"
        )
        commands[f'{self.bot_name}-set_working_dir'] = self._write_command_file(
            commands_dir / f'{self.bot_name}-set_working_dir.md',
            set_working_dir_syntax
        )
        return commands

    def _build_help_command_content(self, python_command: str) -> str:
        """Build help command content with display instructions."""
        lines = [
            f"{python_command} --help-cursor",
            "",
            "## Display Instructions",
            "",
            "After running the command above:",
            "1. Read the status.md file path shown in the output",
            "2. Display the file contents EXACTLY as written - do not reformat into tables or summarize",
            "3. Do NOT wrap the output in a code fence - render it as markdown directly",
            "4. Preserve all formatting, headers, and structure from the original file",
        ]
        return "\n".join(lines)

    def _generate_behavior_commands(self, commands_dir: Path, python_command: str, behaviors: list, commands: dict):
        for behavior_name in behaviors:
            behavior_command = self._build_behavior_command_with_actions(python_command, behavior_name)
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

    def _build_behavior_command_with_actions(self, python_command: str, behavior_name: str) -> str:
        """Build comprehensive command documentation with all actions and their parameters."""
        # Use raw strings and format separately to avoid escaping issues
        scope_epic = "{'type': 'epic', 'value': ['Epic Name']}"
        scope_story = "{'type': 'story', 'value': ['Story Name']}"
        scope_increment = "{'type': 'increment', 'value': [1, 2]}"
        scope_files = "{'type': 'files', 'value': ['path/to/file'], 'exclude': ['*.test.js']}"
        
        lines = [
            f"# {self.bot_name}-{behavior_name} - Available Actions",
            "",
            "## Quick Execute (with action prompt)",
            f"{python_command} --behavior {behavior_name} --action ${{1:action}}${{2:+ }}${{2:params}}",
            "",
            "## Available Actions:",
            "",
            "### clarify - Gather context",
            f"{python_command} --behavior {behavior_name} --action clarify",
            '  # Optional: --key_questions_answered \'{"q1": "answer"}\' --evidence_provided \'{"type": "content"}\'',
            "",
            "### strategy - Decide approach", 
            f"{python_command} --behavior {behavior_name} --action strategy",
            '  # Optional: --decisions_made \'{"decision": "value"}\' --assumptions_made \'["assumption"]\'',
            "",
            "### build - Build knowledge graph",
            f"{python_command} --behavior {behavior_name} --action build",
            "  # Scope all: (default)",
            f"  # Scope epic: --scope \"{scope_epic}\"",
            f"  # Scope story: --scope \"{scope_story}\"",
            f"  # Scope increment: --scope \"{scope_increment}\"",
            "",
            "### validate - Validate against rules",
            f"{python_command} --behavior {behavior_name} --action validate",
            "  # Scope all: (default)",
            f"  # Scope epic: --scope \"{scope_epic}\"",
            f"  # Scope story: --scope \"{scope_story}\"",
            f"  # Scope files: --scope \"{scope_files}\"",
            "  # Skip rules: --skiprule rule_name",
            "",
            "### render - Generate output artifacts",
            f"{python_command} --behavior {behavior_name} --action render",
            "  # Scope all: (default)",
            f"  # Scope epic: --scope \"{scope_epic}\"",
            f"  # Scope story: --scope \"{scope_story}\"",
            "",
            "## Common Patterns:",
            "  # Work on specific epic:",
            f"  {python_command} --behavior {behavior_name} --action build --scope \"{scope_epic}\"",
            "",
            "  # Validate with exclusions:",
            f"  {python_command} --behavior {behavior_name} --action validate --skiprule rule_to_skip",
            "",
            "  # Work on multiple stories:",
            f"  {python_command} --behavior {behavior_name} --action build --scope \"{{' type': 'story', 'value': ['Story 1', 'Story 2']}}\"",
        ]
        return "\n".join(lines)

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