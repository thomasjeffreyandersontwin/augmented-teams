from pathlib import Path
from typing import Dict, Set, Optional, List
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.bot.bot import Bot
from agile_bot.bots.base_bot.src.generator.orchestrator import Orchestrator, GeneratorConfig
from agile_bot.bots.base_bot.src.cli.action_data_collector import ActionDataCollector
from agile_bot.bots.base_bot.src.cli.command_renderer import CursorCommandVisitor
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.cli.base_bot_cli import CliTerminalFormatter
import json

class CursorCommandGenerator:

    def __init__(self, workspace_root: Path, bot_location: Path, bot_name: str):
        self.workspace_root = workspace_root
        self.bot_location = bot_location
        self.bot_name = bot_name
        self._bot: Optional[Bot] = None
        self._data_collector: Optional[ActionDataCollector] = None
    
    def _get_bot(self) -> Bot:
        if self._bot is None:
            bot_directory = self.workspace_root / self.bot_location
            config_path = bot_directory / 'bot_config.json'
            self._bot = Bot(bot_name=self.bot_name, bot_directory=bot_directory, config_path=config_path)
        return self._bot
    
    def _get_data_collector(self) -> ActionDataCollector:
        if self._data_collector is None:
            bot = self._get_bot()
            formatter = CliTerminalFormatter()
            description_extractor = DescriptionExtractor(self.bot_name, self.bot_location, formatter)
            self._data_collector = ActionDataCollector(
                bot=bot,
                bot_name=self.bot_name,
                bot_directory=self.bot_location,
                description_extractor=description_extractor
            )
        return self._data_collector

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
            
            rules_command = self._build_rules_command(python_command, behavior_name)
            commands[f'{self.bot_name}-{behavior_name}-rules'] = self._write_command_file(commands_dir / f'{self.bot_name}-{behavior_name}-rules.md', rules_command)

    def _get_current_command_files(self, commands_dir: Path) -> Set[Path]:
        try:
            bot_prefix = f'{self.bot_name}'
            existing_files = set()
            for file_path in commands_dir.glob(f'{bot_prefix}*.md'):
                existing_files.add(file_path)
            return existing_files
        except (FileNotFoundError, OSError):
            return set()

    def _remove_obsolete_command_files(self, commands_dir: Path, existing_files: Set[Path], current_commands: Dict[str, Path]):
        current_file_paths = set(current_commands.values())
        for file_path in existing_files:
            if file_path not in current_file_paths:
                file_path.unlink(missing_ok=True)

    def _build_behavior_command_with_actions(self, python_command: str, behavior_name: str) -> str:
        lines: List[str] = [
            f"# {self.bot_name}-{behavior_name} - Available Actions",
            "",
            "## Quick Execute (with action prompt)",
            f"{python_command} --behavior {behavior_name} --action ${{1:action}}${{2:+ }}${{2:params}}",
            "",
            "## Available Actions:",
            "",
        ]
        
        # Use visitor pattern to generate action help
        bot = self._get_bot()
        behavior = bot.behaviors.find_by_name(behavior_name)
        if behavior:
            data_collector = self._get_data_collector()
            command_visitor = CursorCommandVisitor(python_command, self.bot_name, behavior_name, lines)
            
            # Visit all actions
            action_names = data_collector.action_order + ['rules']
            for action_name in action_names:
                action = behavior.actions.find_by_name(action_name)
                if action:
                    from agile_bot.bots.base_bot.src.cli.help_context import ActionHelpContext
                    action_description = data_collector.get_action_description(action_name)
                    parameters = data_collector.get_action_parameters(action_name)
                    parameter_descriptions = data_collector.get_parameter_descriptions(action_name, parameters)
                    context = ActionHelpContext(
                        bot_name=self.bot_name,
                        action_name=action_name,
                        action_description=action_description,
                        parameters=parameters,
                        parameter_descriptions=parameter_descriptions
                    )
                    command_visitor.visit_action(context)
            
            # Add footer with common patterns
            command_visitor.visit_footer()
        
        return "\n".join(lines)
    

    def _build_rules_command(self, python_command: str, behavior_name: str) -> str:
        examples = self._build_rules_examples(python_command, behavior_name)
        description = self._get_rules_description(behavior_name)
        header = self._build_rules_header(behavior_name, description, python_command)
        return "\n".join([header, "", "## Usage Examples", "", *examples])
    
    def _build_rules_examples(self, python_command: str, behavior_name: str) -> list:
        if behavior_name == 'code':
            return self._build_code_rules_examples(python_command, behavior_name)
        elif behavior_name == 'tests':
            return self._build_tests_rules_examples(python_command, behavior_name)
        else:
            return self._build_generic_rules_examples(python_command, behavior_name)
    
    def _build_code_rules_examples(self, python_command: str, behavior_name: str) -> list:
        return [
            f"# Write new production code following rules",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Help me write a new ValidationContext class that encapsulates validation parameters\"",
            "",
            f"# Refactor existing code to follow rules",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Refactor the _execute_scanner method to reduce parameters from 10 to 3\"",
            "",
            f"# Design API following rules",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Design a clean API for loading and filtering rules\"",
        ]
    
    def _build_tests_rules_examples(self, python_command: str, behavior_name: str) -> list:
        return [
            f"# Write new tests following rules",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Help me write tests for the new ValidationContext class\"",
            "",
            f"# Design test structure following rules",
            f"{python_command} --behavior {behavior_name} --action rules --message \"How should I structure tests for the rules validation workflow?\"",
            "",
            f"# Write parameterized tests",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Create parameterized tests for multiple rule validation scenarios\"",
        ]
    
    def _build_generic_rules_examples(self, python_command: str, behavior_name: str) -> list:
        return [
            f"# Get guidance on writing {behavior_name} content",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Help me write a new story following our rules\"",
            "",
            f"# Review work against rules",
            f"{python_command} --behavior {behavior_name} --action rules --message \"Does my scenario follow the rules?\"",
        ]
    
    def _get_rules_description(self, behavior_name: str) -> str:
        descriptions = {
            'code': 'Load code behavior rules into AI context for guidance on writing clean, maintainable production code',
            'tests': 'Load tests behavior rules into AI context for guidance on writing effective, well-structured tests',
            'scenarios': 'Load scenarios behavior rules into AI context for guidance on writing clear, testable scenarios',
            'exploration': 'Load exploration behavior rules into AI context for guidance on defining acceptance criteria',
            'discovery': 'Load discovery behavior rules into AI context for guidance on story decomposition and flow',
            'shape': 'Load shape behavior rules into AI context for guidance on story mapping and domain modeling',
            'prioritization': 'Load prioritization behavior rules into AI context for guidance on organizing delivery increments'
        }
        return descriptions.get(behavior_name, f"Load {behavior_name} behavior rules into AI context for guidance on writing new content.")
    
    def _build_rules_header(self, behavior_name: str, description: str, python_command: str) -> str:
        lines = [
            f"# {self.bot_name}-{behavior_name}-rules",
            "",
            description,
            "",
            "## Command",
            "",
            f"{python_command} --behavior {behavior_name} --action rules --message \"${{1:your question or request about {behavior_name} rules}}\"",
            "",
            "## What This Does",
            "",
            f"- Loads all {behavior_name} behavior rules",
            "- Displays numbered list of all rules in status.md",
            "- Provides your message to AI with full rules context",
            "- AI must read each rule file and apply them to your request",
            "- AI helps you write new content following the rules",
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
        try:
            trigger_data = read_json_file(trigger_file)
            return trigger_data.get('patterns', [])
        except (json.JSONDecodeError, FileNotFoundError):
            return []