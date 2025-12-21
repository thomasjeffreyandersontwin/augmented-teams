import sys
import re
import logging
from pathlib import Path
from typing import Dict, Any, Type
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext
from agile_bot.bots.base_bot.src.bot.workspace import get_python_workspace_root, get_base_actions_directory

logger = logging.getLogger(__name__)

class HelpAction(Action):
    context_class: Type[ActionContext] = ActionContext  # Help action needs no parameters
    
    def do_execute(self, context: ActionContext) -> Dict[str, Any]:
        instructions = self.instructions.copy()
        self._add_help_content_to_display(instructions)
        return {'instructions': instructions.to_dict()}
    
    def _add_help_content_to_display(self, instructions):
        instructions.add_display(f"## Available Cursor Commands for {self.behavior.bot_name}:")
        instructions.add_display('')
        instructions.add_display('---')
        instructions.add_display('')
        command_files = self._get_cursor_command_files()
        if command_files:
            self._add_all_command_help(command_files, instructions)
        instructions.add_display('---')
        instructions.add_display('')
        instructions.add_display('## Action Help')
        instructions.add_display('')
        self._add_action_help(instructions)
        instructions.add_display('---')
        instructions.add_display('')
    
    def _get_cursor_command_files(self):
        repo_root = get_python_workspace_root()
        commands_dir = repo_root / '.cursor' / 'commands'
        if not commands_dir.exists():
            return []
        return list(commands_dir.glob(f'{self.behavior.bot_name}*.md'))
    
    def _add_all_command_help(self, command_files, instructions):
        sorted_commands = self._sort_commands_by_behavior_order(command_files)
        for cmd_file in sorted_commands:
            self._add_command_help(cmd_file, instructions)
    
    def _sort_commands_by_behavior_order(self, command_files):
        from agile_bot.bots.base_bot.src.utils import read_json_file
        bot_name = self.behavior.bot_name
        bot_directory = self.behavior.bot_paths.bot_directory
        
        def get_command_order(cmd_file: Path) -> tuple:
            cmd_name = cmd_file.stem
            behavior_name = cmd_name.replace(f'{bot_name}-', '').replace('-', '_')
            if behavior_name in ['', 'continue', 'help', 'get_working_dir', 'set_working_dir'] or cmd_name == bot_name:
                return (0, cmd_name)
            order = self._get_behavior_order(bot_directory, behavior_name)
            return (1, order, cmd_name)
        return sorted(command_files, key=get_command_order)
    
    def _get_behavior_order(self, bot_directory: Path, behavior_name: str) -> int:
        from agile_bot.bots.base_bot.src.utils import read_json_file
        behavior_json_path = bot_directory / 'behaviors' / behavior_name / 'behavior.json'
        if not behavior_json_path.exists():
            return 999
        try:
            config = read_json_file(behavior_json_path)
            return config.get('order', 999)
        except Exception:
            logger.debug(f'Failed to read behavior order for {behavior_name}')
            return 999
    
    def _add_command_help(self, cmd_file: Path, instructions):
        cmd_name = cmd_file.stem
        try:
            description = self._get_command_description(cmd_name)
            instructions.add_display(f'## {cmd_name}')
            instructions.add_display('')
            instructions.add_display(description)
            instructions.add_display('')
            instructions.add_display('```')
            instructions.add_display(f'/{cmd_name}')
            instructions.add_display('```')
            instructions.add_display('')
        except Exception as e:
            instructions.add_display(f'## {cmd_name}')
            instructions.add_display('')
            instructions.add_display(f'[ERROR] Error reading command: {e}')
            instructions.add_display('')
    
    def _get_command_description(self, cmd_name: str) -> str:
        bot_name = self.behavior.bot_name
        if cmd_name == bot_name:
            return f"Execute the current action and current behavior in the {bot_name} workflow."
        if cmd_name == f'{bot_name}-continue':
            return "Close current action and continue to next action in workflow"
        if cmd_name == f'{bot_name}-help':
            return "List all available cursor commands and their parameters"
        if cmd_name == f'{bot_name}-get_working_dir':
            return "Get Working Dir"
        if cmd_name == f'{bot_name}-set_working_dir':
            return "Set Working Dir"
        behavior_name = cmd_name.replace(f'{bot_name}-', '')
        return self._get_behavior_description(behavior_name)
    
    def _get_behavior_description(self, behavior_name: str) -> str:
        try:
            behavior = self.behavior.bot.behaviors.find_by_name(behavior_name)
            if behavior:
                description = getattr(behavior, 'description', None)
                if description:
                    return description
        except Exception:
            logger.debug(f'Failed to get description for behavior {behavior_name}')
        return f'{behavior_name} behavior'
    
    def _add_action_help(self, instructions):
        base_actions_dir = get_base_actions_directory()
        action_order = ['clarify', 'strategy', 'build', 'validate', 'render']
        action_parameters = {
            'clarify': [
                ('--key_questions_answered <dict>', 'Dict mapping question keys to answer strings'),
                ('--evidence_provided <dict>', 'Dict mapping evidence types to evidence content')
            ],
            'strategy': [
                ('--decisions_made <dict>', 'Dict mapping decision criteria keys to selected options/values'),
                ('--assumptions_made <list>', 'List of assumption strings')
            ],
            'build': [
                ('--scope <dict>', "Scope: {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}")
            ],
            'validate': [
                ('--scope <dict>', "Scope: {'type': 'story'|'epic'|'increment'|'all'|'files', 'value': <names|priorities|files>, 'exclude': <patterns>, 'skiprule': <rule_names>}"),
                ('--force-full', 'Force full scan of all files, ignoring timestamps (flag: presence = full scan)'),
                ('--skip-cross-file', 'Skip cross-file duplicate checking (flag: presence = skip cross-file scan)')
            ],
            'render': [
                ('--scope <dict>', "Scope: {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}")
            ]
        }
        for action_name in action_order:
            self._add_single_action_help(instructions, base_actions_dir, action_name, action_parameters)
    
    def _add_single_action_help(self, instructions, base_actions_dir: Path, action_name: str, action_parameters: dict):
        action_dir = base_actions_dir / action_name
        if not action_dir.exists() or not action_dir.is_dir():
            return
        action_config_file = action_dir / 'action_config.json'
        if not action_config_file.exists():
            return
        try:
            from agile_bot.bots.base_bot.src.utils import read_json_file
            action_config = read_json_file(action_config_file)
            description = action_config.get('description', f'{action_name} action')
            instructions.add_display(f'### {action_name}')
            instructions.add_display('')
            instructions.add_display(description)
            instructions.add_display('')
            if action_name == 'validate':
                instructions.add_display('**NOTE:** For code behavior, validation runs in background. You MUST poll the status file every 10 seconds and report progress until complete.')
                instructions.add_display('')
            instructions.add_display('```')
            instructions.add_display(f'/{self.behavior.bot_name}-<behavior> {action_name} [parameters]')
            params = action_parameters.get(action_name, [])
            if params:
                instructions.add_display('')
                for param_name, param_desc in params:
                    instructions.add_display(f'{param_name}:   {param_desc}')
            instructions.add_display('```')
            instructions.add_display('')
        except Exception:
            logger.debug(f'Failed to load action config for {action_name}')
