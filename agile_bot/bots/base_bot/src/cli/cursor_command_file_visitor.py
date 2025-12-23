from pathlib import Path
from typing import Dict, Set, List, Optional
from agile_bot.bots.base_bot.src.generator.visitor import Visitor
from agile_bot.bots.base_bot.src.generator.help_context import BehaviorHelpContext, ActionHelpContext
from agile_bot.bots.base_bot.src.cli.cursor_command_renderer_visitor import CursorCommandRendererVisitor
from agile_bot.bots.base_bot.src.generator.orchestrator import Orchestrator
import json
from agile_bot.bots.base_bot.src.utils import read_json_file

class CursorCommandFileVisitor(Visitor):
    """Visitor that generates all Cursor command files for a bot."""
    
    def __init__(self, workspace_root: Path, cli_script_path: Path, bot=None):
        super().__init__(bot=bot)
        self.workspace_root = workspace_root
        self.cli_script_path = cli_script_path
        self.commands_dir: Optional[Path] = None
        self.python_command: Optional[str] = None
        self.commands: Dict[str, Path] = {}
        self.current_command_files: Set[Path] = set()
    
    def visit_header(self, bot_name: str) -> None:
        self.commands_dir = self._ensure_commands_directory()
        self.python_command = self._get_python_command()
        self.current_command_files = self._get_current_command_files()
        self._generate_base_commands()
    
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        behavior_command = self._build_behavior_command(context.behavior_name)
        self.commands[f'{self.bot_name}-{context.behavior_name}'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}-{context.behavior_name}.md',
            behavior_command
        )
        
        rules_command = self._build_rules_command(context.behavior_name)
        self.commands[f'{self.bot_name}-{context.behavior_name}-rules'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}-{context.behavior_name}-rules.md',
            rules_command
        )
    
    def visit_action(self, context: ActionHelpContext) -> None:
        pass
    
    def visit_action_help_section_header(self) -> None:
        pass
    
    def visit_footer(self) -> None:
        self._remove_obsolete_command_files()
    
    def _ensure_commands_directory(self) -> Path:
        commands_dir = self.workspace_root / '.cursor' / 'commands'
        commands_dir.mkdir(parents=True, exist_ok=True)
        return commands_dir
    
    def _get_python_command(self) -> str:
        rel_cli_script_path = self.cli_script_path.relative_to(self.workspace_root) if self.cli_script_path.is_absolute() else self.cli_script_path
        return f"python {str(rel_cli_script_path).replace('\\', '/')}"
    
    def _get_current_command_files(self) -> Set[Path]:
        try:
            bot_prefix = f'{self.bot_name}'
            existing_files = set()
            for file_path in self.commands_dir.glob(f'{bot_prefix}*.md'):
                existing_files.add(file_path)
            return existing_files
        except (FileNotFoundError, OSError):
            return set()
    
    def _generate_base_commands(self) -> None:
        self.commands[f'{self.bot_name}'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}.md',
            self.python_command
        )
        self.commands[f'{self.bot_name}-continue'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}-continue.md',
            f'{self.python_command} --close'
        )
        help_content = self._build_help_command_content()
        self.commands[f'{self.bot_name}-help'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}-help.md',
            help_content
        )
        self.commands[f'{self.bot_name}-get_working_dir'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}-get_working_dir.md',
            f'{self.python_command} --action get_working_dir'
        )
        set_working_dir_syntax = (
            f"{self.python_command} --action set_working_dir "
            "${1:/path/to/workspace}${2:+ }${2:persist=true|false}"
        )
        self.commands[f'{self.bot_name}-set_working_dir'] = self._write_command_file(
            self.commands_dir / f'{self.bot_name}-set_working_dir.md',
            set_working_dir_syntax
        )
    
    def _build_help_command_content(self) -> str:
        lines = [
            f"{self.python_command} --help-cursor",
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
    
    def _build_behavior_command(self, behavior_name: str) -> str:
        lines = self._build_command_header(behavior_name)
        behavior = self.bot.behaviors.find_by_name(behavior_name)
        if behavior:
            self._generate_action_help_for_behavior(behavior_name, lines)
        return "\n".join(lines)
    
    def _build_command_header(self, behavior_name: str) -> List[str]:
        return [
            f"# {self.bot_name}-{behavior_name} - Available Actions",
            "",
            "## Quick Execute (with action prompt)",
            f"{self.python_command} --behavior {behavior_name} --action ${{1:action}}${{2:+ }}${{2:params}}",
            "",
            "## Available Actions:",
            "",
        ]
    
    def _generate_action_help_for_behavior(self, behavior_name: str, lines: List[str]) -> None:
        command_visitor = CursorCommandRendererVisitor(
            self.python_command,
            behavior_name,
            lines,
            bot=self.bot
        )
        orchestrator = Orchestrator(command_visitor)
        orchestrator.visit_actions_for_behavior(behavior_name)
        self._visit_rules_action(command_visitor, behavior_name)
        command_visitor.visit_footer()
    
    def _visit_rules_action(self, visitor: CursorCommandRendererVisitor, behavior_name: str) -> None:
        from agile_bot.bots.base_bot.src.generator.help_context import ActionHelpContext
        if visitor.data_collector is None:
            return
        behavior = self.bot.behaviors.find_by_name(behavior_name)
        if behavior and behavior.actions.find_by_name('rules'):
            data_collector = visitor.data_collector
            action_description = data_collector.get_action_description('rules')
            parameters = data_collector.get_action_parameters('rules')
            parameter_descriptions = data_collector.get_parameter_descriptions('rules', parameters)
            context = ActionHelpContext(
                bot_name=self.bot_name,
                action_name='rules',
                action_description=action_description,
                parameters=parameters,
                parameter_descriptions=parameter_descriptions
            )
            visitor.visit_action(context)
    
    def _build_rules_command(self, behavior_name: str) -> str:
        examples = self._build_rules_examples(behavior_name)
        description = self._get_rules_description(behavior_name)
        header = self._build_rules_header(behavior_name, description)
        return "\n".join([header, "", "## Usage Examples", "", *examples])
    
    def _build_rules_examples(self, behavior_name: str) -> list:
        if behavior_name == 'code':
            return self._build_code_rules_examples(behavior_name)
        elif behavior_name == 'tests':
            return self._build_tests_rules_examples(behavior_name)
        else:
            return self._build_generic_rules_examples(behavior_name)
    
    def _build_code_rules_examples(self, behavior_name: str) -> list:
        return [
            f"# Write new production code following rules",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Help me write a new ValidationContext class that encapsulates validation parameters\"",
            "",
            f"# Refactor existing code to follow rules",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Refactor the _execute_scanner method to reduce parameters from 10 to 3\"",
            "",
            f"# Design API following rules",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Design a clean API for loading and filtering rules\"",
        ]
    
    def _build_tests_rules_examples(self, behavior_name: str) -> list:
        return [
            f"# Write new tests following rules",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Help me write tests for the new ValidationContext class\"",
            "",
            f"# Design test structure following rules",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"How should I structure tests for the rules validation workflow?\"",
            "",
            f"# Write parameterized tests",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Create parameterized tests for multiple rule validation scenarios\"",
        ]
    
    def _build_generic_rules_examples(self, behavior_name: str) -> list:
        return [
            f"# Get guidance on writing {behavior_name} content",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Help me write a new story following our rules\"",
            "",
            f"# Review work against rules",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"Does my scenario follow the rules?\"",
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
    
    def _build_rules_header(self, behavior_name: str, description: str) -> str:
        lines = [
            f"# {self.bot_name}-{behavior_name}-rules",
            "",
            description,
            "",
            "## Command",
            "",
            f"{self.python_command} --behavior {behavior_name} --action rules --message \"${{1:your question or request about {behavior_name} rules}}\"",
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
    
    def _remove_obsolete_command_files(self) -> None:
        current_file_paths = set(self.commands.values())
        for file_path in self.current_command_files:
            if file_path not in current_file_paths:
                file_path.unlink(missing_ok=True)
    
    def get_commands(self) -> Dict[str, Path]:
        return self.commands



