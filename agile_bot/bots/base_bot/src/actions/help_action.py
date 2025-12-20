import sys
import re
from pathlib import Path
from typing import Dict, Any
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.bot.workspace import get_python_workspace_root, get_base_actions_directory


class HelpAction(Action):
    """Action that displays help information for cursor commands and actions."""
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        instructions = self.instructions.copy()
        
        # Add help content to display
        self._add_help_content_to_display(instructions)
        
        # Status breadcrumbs are already in display_content from base instructions property
        return {'instructions': instructions.to_dict()}
    
    def _add_help_content_to_display(self, instructions):
        """Add cursor commands and action help to display content."""
        # #region agent log
        import json as _json; open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a').write(_json.dumps({"location": "help_action.py:_add_help_content_to_display", "message": "Starting help generation", "data": {}, "hypothesisId": "fix-verify", "timestamp": __import__('time').time()}) + '\n')
        # #endregion
        
        # Add header
        instructions.add_display(f"## Available Cursor Commands for {self.behavior.bot_name}:")
        instructions.add_display('')
        instructions.add_display('---')
        instructions.add_display('')
        
        # Add command help
        command_files = self._get_cursor_command_files()
        if command_files:
            self._add_all_command_help(command_files, instructions)
        
        # Add action help
        instructions.add_display('---')
        instructions.add_display('')
        instructions.add_display('## Action Help')
        instructions.add_display('')
        self._add_action_help(instructions)
        
        instructions.add_display('---')
        instructions.add_display('')
    
    def _get_cursor_command_files(self):
        """Get list of cursor command files for this bot."""
        repo_root = get_python_workspace_root()
        commands_dir = repo_root / '.cursor' / 'commands'
        if not commands_dir.exists():
            return []
        command_files = list(commands_dir.glob(f'{self.behavior.bot_name}*.md'))
        return command_files
    
    def _add_all_command_help(self, command_files, instructions):
        """Add help for all cursor commands, sorted by behavior order."""
        # Sort commands by behavior order
        sorted_commands = self._sort_commands_by_behavior_order(command_files)
        for cmd_file in sorted_commands:
            self._add_command_help(cmd_file, instructions)
    
    def _sort_commands_by_behavior_order(self, command_files):
        """Sort command files by behavior order from behavior.json files."""
        from agile_bot.bots.base_bot.src.utils import read_json_file
        bot_name = self.behavior.bot_name
        bot_directory = self.behavior.bot_paths.bot_directory
        
        def get_command_order(cmd_file: Path) -> tuple:
            cmd_name = cmd_file.stem
            behavior_name = cmd_name.replace(f'{bot_name}-', '').replace('-', '_')
            
            # Special commands come first
            if behavior_name in ['', 'continue', 'help', 'get_working_dir', 'set_working_dir'] or cmd_name == bot_name:
                return (0, cmd_name)
            
            # Get order from behavior.json
            behavior_json_path = bot_directory / 'behaviors' / behavior_name / 'behavior.json'
            order = 999
            if behavior_json_path.exists():
                try:
                    config = read_json_file(behavior_json_path)
                    order = config.get('order', 999)
                except Exception:
                    pass
            return (1, order, cmd_name)
        
        sorted_files = sorted(command_files, key=get_command_order)
        # #region agent log
        import json as _json; open(r'c:\dev\augmented-teams\.cursor\debug.log', 'a').write(_json.dumps({"location": "help_action.py:_sort_commands_by_behavior_order", "message": "Sorted commands", "data": {"sorted_commands": [f.stem for f in sorted_files]}, "hypothesisId": "fix-verify", "timestamp": __import__('time').time()}) + '\n')
        # #endregion
        return sorted_files
    
    def _add_command_help(self, cmd_file: Path, instructions):
        """Add help for a single cursor command."""
        cmd_name = cmd_file.stem
        try:
            cmd_content = cmd_file.read_text(encoding='utf-8').strip()
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
        """Get description for a command from behavior object."""
        # Extract behavior name from command name
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
        
        # Extract behavior name
        behavior_name = cmd_name.replace(f'{bot_name}-', '')
        
        # Try to get description from behavior object
        try:
            behavior = self.behavior.bot.behaviors.find_by_name(behavior_name)
            if behavior:
                # Get description from behavior object, not config
                description = getattr(behavior, 'description', None)
                if description:
                    return description
        except Exception:
            pass
        
        return f'{behavior_name} behavior'
    
    def _add_action_help(self, instructions):
        """Add help for base actions in proper workflow order with parameters."""
        base_actions_dir = get_base_actions_directory()
        
        # Define action order and parameters
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
                ('--scope <dict>', "Scope: {'type': 'story'|'epic'|'increment'|'all'|'files', 'value': <names|priorities|files>, 'exclude': <patterns>}")
            ],
            'render': [
                ('--scope <dict>', "Scope: {'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}")
            ]
        }
        
        # Iterate through actions in proper order
        for action_name in action_order:
            action_dir = base_actions_dir / action_name
            if not action_dir.exists() or not action_dir.is_dir():
                continue
            
            action_config_file = action_dir / 'action_config.json'
            if not action_config_file.exists():
                continue
            
            try:
                from agile_bot.bots.base_bot.src.utils import read_json_file
                action_config = read_json_file(action_config_file)
                description = action_config.get('description', f'{action_name} action')
                
                instructions.add_display(f'### {action_name}')
                instructions.add_display('')
                instructions.add_display(description)
                instructions.add_display('')
                instructions.add_display('```')
                instructions.add_display(f'/{self.behavior.bot_name}-<behavior> {action_name} [parameters]')
                
                # Add parameter details
                params = action_parameters.get(action_name, [])
                if params:
                    instructions.add_display('')
                    for param_name, param_desc in params:
                        instructions.add_display(f'{param_name}:   {param_desc}')
                
                instructions.add_display('```')
                instructions.add_display('')
            except Exception as e:
                # Skip actions that can't be loaded
                continue

