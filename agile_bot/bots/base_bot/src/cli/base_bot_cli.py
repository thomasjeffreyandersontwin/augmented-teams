#!/usr/bin/env python3

import sys
import argparse
import json
import logging
import re
import traceback
from pathlib import Path
from typing import Dict, Any, Tuple
from agile_bot.bots.base_bot.src.bot.bot import Bot, BotResult
from agile_bot.bots.base_bot.src.bot.workspace import get_base_actions_directory, get_bot_directory, get_python_workspace_root
from agile_bot.bots.base_bot.src.utils import read_json_file

logger = logging.getLogger(__name__)


class CliTerminalFormatter:
    """
    CLI-specific markdown formatter for chat-friendly output.
    Outputs markdown formatting that looks good in chat windows.
    """
    
    def format_directive(self, text: str) -> str:
        """Format CLI output directives (like 'PLEASE SHOW THIS OUTPUT TO THE USER')."""
        return f"## {text}"
    
    def format_header(self, text: str) -> str:
        """Format section headers."""
        return f"## {text}"
    
    def format_command(self, text: str) -> str:
        """Format command names (e.g., /story_bot-shape)."""
        return f"**{text}**"
    
    def format_label(self, text: str) -> str:
        """Format labels (e.g., 'Description:', 'Parameters:')."""
        return f"**{text}**"
    
    def format_parameter(self, text: str) -> str:
        """Format parameter placeholders (e.g., $1, $2)."""
        return f"`{text}`"
    
    def format_workflow_status_header(self, text: str) -> str:
        """Format workflow status section headers."""
        return f"## {text}"
    
    def format_workflow_directory(self, text: str) -> str:
        """Format directory paths in workflow status."""
        return f"**{text}**"
    
    def format_workflow_current_state(self, text: str) -> str:
        """Format current state information."""
        return f"**{text}**"
    
    def format_workflow_next_step(self, text: str) -> str:
        """Format next step instructions."""
        return f"**{text}**"
    
    def format_workflow_current_marker(self, text: str) -> str:
        """Format current action/behavior markers."""
        return f"**{text}**"
    
    def format_workflow_active_marker(self, text: str) -> str:
        """Format active behavior markers."""
        return f"**{text}**"
    
    def format_workflow_completed(self, text: str) -> str:
        """Format completed items."""
        return text  # Keep [x] for markdown checkboxes
    
    def format_workflow_pending(self, text: str) -> str:
        """Format pending items."""
        return text  # Keep [ ] for markdown checkboxes
    
    def format_error(self, text: str) -> str:
        """Format error messages."""
        return f"[ERROR] **{text}**"
    
    def format_warning(self, text: str) -> str:
        """Format warning messages."""
        return f"[WARNING] **{text}**"
    
    def format_success(self, text: str) -> str:
        """Format success messages."""
        return f"[OK] **{text}**"
    
    def format_info(self, text: str) -> str:
        """Format informational messages."""
        return f"[INFO] **{text}**"
    
    def format_separator(self, char: str = '=', length: int = 70) -> str:
        """Format separator lines."""
        return "---"
    
    def format_thin_separator(self) -> str:
        """Format a thin, less prominent separator line."""
        return "------"


class BaseBotCli:
    def __init__(self, bot: Bot = None, bot_name: str = None, bot_config_path: Path = None):
        if bot:
            self.bot = bot
            self.bot_name = bot.name
            self.bot_directory = bot.bot_paths.bot_directory
        elif bot_name and bot_config_path:
            self.bot_name = bot_name
            self.bot_config_path = bot_config_path
            self.bot_directory = get_bot_directory()
            self.bot = self._create_bot_instance()
        else:
            raise ValueError("Must provide either bot instance or (bot_name and bot_config_path)")
        
        # Initialize CLI-specific formatter for output formatting
        self.formatter = CliTerminalFormatter()
    
    def _create_bot_instance(self) -> Bot:
        return Bot(
            bot_name=self.bot_name,
            bot_directory=self.bot_directory,
            config_path=self.bot_config_path
        )
    
    def run(self, behavior_name: str = None, action_name: str = None, **kwargs) -> Dict[str, Any]:
        try:
            result = self._route_to_action(behavior_name, action_name, kwargs)
            # _route_to_action already returns a formatted dict, so just return it
            return result
        except Exception as e:
            self._handle_error(e)
    
    def close_current_action(self) -> Dict[str, Any]:
        try:
            current_behavior = self._navigate_to_first_behavior_if_needed()
            current_behavior.actions.load_state()
            current_action = current_behavior.actions.current
            if current_action:
                current_behavior.actions.close_current()
            return self._execute_current_action(current_behavior)
        except Exception as e:
            self._handle_error(e)
    
    def _route_to_action(self, behavior_name: str, action_name: str, parameters: Dict[str, Any]):
        # Let exceptions propagate to run() which will handle them
        if action_name:
            return self._route_to_specific_action(behavior_name, action_name, parameters)
        if behavior_name:
            return self._route_to_behavior(behavior_name)
        return self._route_to_current_behavior_and_action()
    
    def _route_to_specific_action(self, behavior_name: str, action_name: str, parameters: Dict[str, Any]):
        # Let exceptions propagate to run() which will handle them
        behavior_obj = getattr(self.bot, behavior_name)
        action = behavior_obj.actions.find_by_name(action_name)
        if action is None:
            raise ValueError(f"Action '{action_name}' not found in behavior '{behavior_name}'")
        
        # Navigate to the action (saves workflow state)
        behavior_obj.actions.navigate_to(action_name)
        
        # Execute action directly
        result_data = action.execute(parameters or {})
        result = self._create_bot_result('completed', behavior_name, action_name, result_data)
        return self._format_result(result)
    
    def _route_to_behavior(self, behavior_name: str):
        # Let exceptions propagate to run() which will handle them
        behavior_obj = getattr(self.bot, behavior_name)
        return self._execute_current_action(behavior_obj)
    
    def _output_breadcrumbs(self, breadcrumbs: list, add_separator: bool = True):
        """Output breadcrumbs with UTF-8 encoding for emoji support.
        
        Extracted to eliminate duplication between help_behaviors_and_actions()
        and help_cursor_commands().
        """
        fmt = self._get_formatter()
        if add_separator:
            print(fmt.format_separator())
            print()
        sys.stdout.flush()  # Flush before buffer write to maintain order
        for line in breadcrumbs:
            # Skip AI directive lines
            if line.startswith("**CRITICAL: YOU MUST DISPLAY") or line.startswith("**YOU MUST DISPLAY"):
                continue
            # Write with UTF-8 encoding to preserve emojis for markdown rendering
            try:
                sys.stdout.buffer.write((line + "\n").encode('utf-8'))
                sys.stdout.buffer.flush()
            except Exception:
                # Fallback to regular print if buffer write fails
                print(line)
        sys.stdout.flush()
    
    def _navigate_to_first_behavior_if_needed(self):
        """Navigate to first behavior if no current behavior is set.
        
        Extracted to eliminate duplication between close_current_action() and 
        _route_to_current_behavior_and_action().
        """
        current_behavior = self.bot.behaviors.current
        if current_behavior is None:
            if self.bot.behaviors.first:
                self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
                current_behavior = self.bot.behaviors.current
            else:
                raise ValueError("No behaviors available")
        if current_behavior is None:
            raise ValueError("No current behavior")
        return current_behavior
    
    def _execute_current_action(self, behavior):
        """Execute current action for a behavior and return formatted result.
        
        Extracted to eliminate duplication between _route_to_behavior() and
        _route_to_current_behavior_and_action().
        """
        action = behavior.actions.forward_to_current()
        if action is None:
            raise ValueError(f"No current action found for behavior {behavior.name}")
        result_data = action.execute()
        result = self._create_bot_result('completed', behavior.name, action.action_name, result_data)
        return self._format_result(result)
    
    def _route_to_current_behavior_and_action(self):
        # Let exceptions propagate to run() which will handle them
        current_behavior = self._navigate_to_first_behavior_if_needed()
        return self._execute_current_action(current_behavior)
    
    def _create_bot_result(self, status: str, behavior: str, action: str, data: Dict[str, Any]) -> BotResult:
        """Create a BotResult object - wrapping happens at CLI/MCP level."""
        # Let exceptions propagate to calling method which will handle them
        return BotResult(status=status, behavior=behavior, action=action, data=data)
    
    def _format_result(self, result) -> Dict[str, Any]:
        # Let exceptions propagate to calling method which will handle them
        status = 'success' if result.status == 'completed' else result.status
        return {
            "status": status,
            "behavior": result.behavior,
            "action": result.action,
            "data": result.data
        }
    
    def list_behaviors(self):
        try:
            fmt = self.formatter
            print(fmt.format_header(f"Available behaviors for {self.bot_name}:"))
            for behavior in self.bot.behaviors:
                print(f"  {fmt.format_command(f'- {behavior.name}')}")
            sys.stdout.flush()
        except Exception as e:
            self._handle_error(e)
    
    def list_actions(self, behavior_name: str):
        try:
            fmt = self.formatter
            behavior_obj = getattr(self.bot, behavior_name)
            actions = self._get_behavior_actions(behavior_obj)
            
            print(fmt.format_header(f"Available actions for {behavior_name}:"))
            for action in actions:
                print(f"  {fmt.format_command(f'- {action}')}")
            sys.stdout.flush()
        except Exception as e:
            self._handle_error(e)
    
    def help_behaviors_and_actions(self):
        try:
            fmt = self.formatter
            print(f"\n{fmt.format_directive('**PLEASE SHOW THIS OUTPUT TO THE USER**')}\n")
            print(f"{fmt.format_header(f'Available Behaviors and Actions for {self.bot_name}:')}\n")
            print(fmt.format_separator())
            
            for behavior in self.bot.behaviors:
                behavior_name = behavior.name
                # Get behavior description
                behavior_description = self._get_behavior_description(f'{self.bot_name}-{behavior_name}')
                
                print(f"\n{fmt.format_command(f'Behavior: {behavior_name}')}")
                print(f"  {fmt.format_label('Description:')} {behavior_description}")
                
                # Get actions for this behavior
                try:
                    behavior_obj = getattr(self.bot, behavior_name)
                    actions = self._get_behavior_actions(behavior_obj)
                    
                    if actions:
                        print(f"  {fmt.format_label('Actions:')}")
                        for action in actions:
                            # Try to get action description from base_actions
                            action_description = self._get_action_description(action)
                            print(f"    {fmt.format_command(f'- {action}:')} {action_description}")
                    else:
                        print(f"  {fmt.format_label('Actions:')} {fmt.format_workflow_pending('None')}")
                except Exception as e:
                    print(f"  {fmt.format_label('Actions:')} {fmt.format_error(f'Error loading actions - {e}')}")
                    traceback.print_exc()
                    sys.stdout.flush()
            
            print(f"\n{fmt.format_separator()}")
            print(f"\n{fmt.format_label('Usage:')}")
            print(f"  {fmt.format_command(f'{self.bot_name} [--behavior <name>] [--action <name>] [--options]')}")
            print(f"  {fmt.format_command(f'{self.bot_name} --help')}          {fmt.format_label('# Show this help')}")
            print(f"  {fmt.format_command(f'{self.bot_name} --list')}          {fmt.format_label('# List behaviors/actions')}")
            print(f"  {fmt.format_command(f'{self.bot_name} --help-cursor')}   {fmt.format_label('# List cursor commands')}")
            print(f"  {fmt.format_command(f'{self.bot_name} --close')}         {fmt.format_label('# Close current action')}")
            
            # Add breadcrumbs at the end (from action.py - single source of truth)
            breadcrumbs = self._get_breadcrumbs_from_action()
            if breadcrumbs:
                print()  # Extra newline before separator
                self._output_breadcrumbs(breadcrumbs)
        except Exception as e:
            self._handle_error(e)
    
    def _extract_first_instruction(self, instructions: list) -> Optional[str]:
        """Extract first meaningful instruction line from a list."""
        if not isinstance(instructions, list):
            return None
        for line in instructions:
            if not line or line.startswith('**') or len(line.strip()) <= 10:
                continue
            desc = line.strip()
            return desc[:77] + '...' if len(desc) > 80 else desc
        return None
    
    def _get_action_description(self, action_name: str) -> str:
        base_actions_dir = get_base_actions_directory(bot_directory=get_bot_directory())
        
        action_prefixes = {
            'clarify': 'clarify',
            'strategy': 'strategy',
            'build': 'build',
            'render': 'render',
            'validate': 'validate'
        }
        
        action_folder = action_prefixes.get(action_name, action_name)
        config_path = base_actions_dir / action_folder / 'action_config.json'
        
        if not config_path.exists():
            return action_name.replace('_', ' ').title()
        
        try:
            config = json.loads(config_path.read_text(encoding='utf-8'))
            desc = self._extract_first_instruction(config.get('instructions', []))
            if desc:
                return desc
        except Exception as e:
            print(f"\n**ERROR in _get_action_description for {action_name}:**")
            traceback.print_exc()
            sys.stdout.flush()
        
        return action_name.replace('_', ' ').title()
    
    def _has_cli_output_directives(self, output: str) -> bool:

        directives = [
            "**PLEASE SHOW THIS OUTPUT TO THE USER**",
            "**YOU MUST DISPLAY THIS WORKFLOW STATUS TO THE USER:**",
            "**CRITICAL: YOU MUST DISPLAY",
            "**CRITICAL: YOU MUST DISPLAY THE ENTIRE OUTPUT"
        ]
        
        output_upper = output.upper()
        for directive in directives:
            if directive.upper() in output_upper:
                return True
        
        return False
    
    def _format_cli_output_for_display(self, output: str) -> Tuple[str, bool]:
        """
        Format CLI output for display, preserving verbatim format when directives are present.
        
        When CLI output contains directives like "**PLEASE SHOW THIS OUTPUT TO THE USER**"
        or "**YOU MUST DISPLAY THIS WORKFLOW STATUS TO THE USER:**", the output should
        be displayed exactly as-is without reformatting.
        
        Args:
            output: The raw CLI output string
            
        Returns:
            Tuple of (formatted_output, should_display_verbatim)
            - formatted_output: The output to display (unchanged when directives present)
            - should_display_verbatim: True if output contains directives and should be shown verbatim
        """
        if self._has_cli_output_directives(output):
            # Return output verbatim when directives are present
            return output, True
        
        # Otherwise, return output as-is (caller can format as needed)
        return output, False
    
    def _build_param_info(self, cmd_name: str, params: list, cmd_content: str) -> Tuple[list, list]:
        """Build parameter placeholders and details for a command."""
        param_placeholders = []
        param_details = []
        for param_num in params:
            param_desc = self._infer_parameter_description(cmd_name, param_num, cmd_content)
            placeholder = self._extract_placeholder_name(cmd_name, param_desc, param_num)
            param_placeholders.append(f"<{placeholder}>")
            
            if param_num == '1':
                param_details.append(f"action:   {placeholder}")
            elif param_num == '2':
                param_details.append("context:  Optional context or file path")
        return param_placeholders, param_details
    
    def _print_command_help(self, cmd_file: Path, fmt) -> None:
        """Print help for a single command file."""
        cmd_name = cmd_file.stem
        
        try:
            cmd_content = cmd_file.read_text(encoding='utf-8').strip()
            params = re.findall(r'\$\{(\d+):\}', cmd_content)
            description = self._get_behavior_description(cmd_name)
            param_placeholders, param_details = self._build_param_info(cmd_name, params, cmd_content)
            
            print(f"## {cmd_name}\n")
            print(f"{description}\n")
            print("```")
            syntax = f"/{cmd_name} {' '.join(param_placeholders)}" if param_placeholders else f"/{cmd_name}"
            print(syntax)
            if param_details:
                print()
                for detail in param_details:
                    print(detail)
            print("```\n")
        except Exception as e:
            print(f"## {cmd_name}\n")
            print(f"{fmt.format_error(f'Error reading command: {e}')}\n")
            traceback.print_exc()
            sys.stdout.flush()
    
    def help_cursor_commands(self):
        try:
            repo_root = get_python_workspace_root()
            commands_dir = repo_root / '.cursor' / 'commands'
            
            if not commands_dir.exists():
                print(self.formatter.format_warning(f"No cursor commands directory found at {commands_dir}"))
                return
            
            command_files = sorted(commands_dir.glob(f'{self.bot_name}*.md'))
            
            if not command_files:
                print(self.formatter.format_warning(f"No cursor commands found for {self.bot_name}"))
                return
            
            fmt = self.formatter
            sys.stdout.write("**CRITICAL: YOU MUST DISPLAY THE ENTIRE OUTPUT BELOW VERBATIM IN YOUR RESPONSE. DO NOT SKIP THIS. COPY AND PASTE IT DIRECTLY INTO YOUR MESSAGE.**\n")
            print(f"{fmt.format_header(f'Available Cursor Commands for {self.bot_name}:')}")
            print()
            print(fmt.format_separator())
            print()
            
            grouped_commands = self._group_commands(command_files)
            all_commands = [cmd for cmds in grouped_commands.values() for cmd in cmds]
            
            for cmd_file in all_commands:
                self._print_command_help(cmd_file, fmt)
            
            breadcrumbs = self._get_breadcrumbs_from_action()
            self._output_breadcrumbs(breadcrumbs)
        except Exception as e:
            self._handle_error(e)
    
    def _group_commands(self, command_files: list) -> dict:
        """
        Group commands into logical categories for better organization.
        
        Returns:
            Dictionary mapping group names to lists of command files
        """
        groups = {
            'Workflow Management': [],
            'Story Planning': [],
            'Implementation': [],
            'Other': []
        }
        
        for cmd_file in command_files:
            cmd_name = cmd_file.stem
            behavior_name = cmd_name.replace(f'{self.bot_name}-', '').replace('-', '_')
            
            # Workflow management commands
            if behavior_name in ['continue', 'help', ''] or cmd_name == self.bot_name:
                groups['Workflow Management'].append(cmd_file)
            # Story planning behaviors
            elif behavior_name in ['shape', 'prioritization', 'discovery', 'exploration', 'scenarios']:
                groups['Story Planning'].append(cmd_file)
            # Implementation behaviors
            elif behavior_name in ['tests', 'code']:
                groups['Implementation'].append(cmd_file)
            else:
                groups['Other'].append(cmd_file)
        
        # Remove empty groups
        return {k: v for k, v in groups.items() if v}
    
    def _get_behavior_description(self, cmd_name: str) -> str:
        # Handle main bot command (e.g., "story_bot" without behavior suffix)
        if cmd_name == self.bot_name:
            # Load command description from bot_config.json
            if hasattr(self, 'bot_config_path') and self.bot_config_path:
                try:
                    bot_config = read_json_file(self.bot_config_path)
                    # Check for "command description." (with period) or variations
                    cmd_desc = bot_config.get('command description.') or bot_config.get('command_description') or bot_config.get('commandDescription')
                    if cmd_desc:
                        return cmd_desc
                except Exception:
                    pass  # Fall through to default
        
        behavior_name = cmd_name.replace(f'{self.bot_name}-', '').replace('-', '_')
        
        if behavior_name in ['continue', 'help']:
            if behavior_name == 'continue':
                return 'Close current action and continue to next action in workflow'
            elif behavior_name == 'help':
                return 'List all available cursor commands and their parameters'
            else:
                return behavior_name.replace('_', ' ').title()
        
        behavior_file_path = (
            self.bot_directory / 'behaviors' / behavior_name / 'behavior.json'
        )
        
        if not behavior_file_path.exists():
            return behavior_name.replace('_', ' ').title()
        
        try:
            behavior_data = read_json_file(behavior_file_path)
            desc = self._extract_behavior_description_from_data(behavior_data)
            if desc:
                return desc
        except Exception as e:
            fmt = self.formatter
            print(f"\n{fmt.format_error(f'**ERROR in _get_behavior_description for {cmd_name}:**')}")
            traceback.print_exc()
            sys.stdout.flush()
        
        return behavior_name.replace('_', ' ').title()
    
    def _extract_behavior_description_from_data(self, behavior_data: dict) -> Optional[str]:
        """Extract description from behavior data, trying instructions first, then fallback fields."""
        instructions = behavior_data.get('instructions', [])
        if instructions:
            return '\n'.join(instructions) if isinstance(instructions, list) else str(instructions)
        
        description_parts = []
        if behavior_data.get('description'):
            description_parts.append(behavior_data['description'])
        if behavior_data.get('goal'):
            description_parts.append(behavior_data['goal'])
        if behavior_data.get('outputs') and len(description_parts) < 3:
            outputs = behavior_data['outputs']
            if isinstance(outputs, str):
                first_output = outputs.split(',')[0].strip()
                description_parts.append(f"Outputs: {first_output}")
        
        return ' | '.join(description_parts[:3]) if description_parts else None
    
    def _infer_parameter_description(self, cmd_name: str, param_num: str, cmd_content: str) -> str:
        if 'continue' in cmd_name or 'help' in cmd_name:
            return 'No parameters'
        
        # All behavior commands have the same parameter pattern:
        # $1 = optional action name, $2 = optional context/file path
        if param_num == '1':
            return 'Action name (e.g., clarify, strategy, build, render, validate)'
        elif param_num == '2':
            return 'Optional context or file path'
        
        return f'Parameter {param_num}'
    
    def _get_action_names_from_behavior(self, behavior_name: str) -> Optional[str]:
        """Get pipe-separated action names from behavior.json, or None if unavailable."""
        behavior_file_path = self.bot_directory / 'behaviors' / behavior_name / 'behavior.json'
        if not behavior_file_path.exists():
            return None
        
        try:
            behavior_data = read_json_file(behavior_file_path)
            actions = behavior_data.get('actions_workflow', {}).get('actions', [])
            action_names = [a.get('name', '') for a in actions if a.get('name')]
            return '|'.join(action_names) if action_names else None
        except Exception:
            return None
    
    def _extract_word_from_description(self, param_desc: str, param_num: str) -> str:
        """Extract a meaningful word from parameter description."""
        skip_words = {'optional', 'action', 'name', 'or', 'file', 'path'}
        words = param_desc.lower().split()
        for word in words:
            if word not in skip_words and len(word) > 2:
                return word
        return f'param{param_num}'
    
    def _extract_placeholder_name(self, cmd_name: str, param_desc: str, param_num: str) -> str:
        """Extract a short placeholder name from parameter description, dynamically getting actions for behavior."""
        if param_num == '2':
            return 'context'
        
        if param_num != '1':
            return self._extract_word_from_description(param_desc, param_num)
        
        behavior_name = cmd_name.replace(f'{self.bot_name}-', '').replace('-', '_')
        
        if behavior_name in ['continue', 'help', ''] or cmd_name == self.bot_name:
            return 'action'
        
        action_names = self._get_action_names_from_behavior(behavior_name)
        return action_names if action_names else 'action'
    
    def _get_behavior_actions(self, behavior_obj) -> list:
        excluded_attrs = {'forward_to_current_action', 'dir', 'current_project_file'}
        actions = []
        for attr_name in dir(behavior_obj):
            if self._is_action_method(behavior_obj, attr_name, excluded_attrs):
                actions.append(attr_name)
        return sorted(actions)
    
    def _is_action_method(self, behavior_obj, attr_name: str, excluded_attrs: set) -> bool:
        if attr_name.startswith('_'):
            return False
        if attr_name in excluded_attrs:
            return False
        return callable(getattr(behavior_obj, attr_name))
    
    @staticmethod
    def parse_arguments(description: str = "Bot CLI", custom_help_handler=None) -> Tuple[argparse.Namespace, Dict[str, str]]:
        parser = argparse.ArgumentParser(description=description, add_help=False)
        parser.add_argument('--behavior', nargs='?', help='Behavior name (optional)')
        parser.add_argument('--action', nargs='?', help='Action name (optional)')
        parser.add_argument('--user_message', nargs='?', help='User message from Cursor (optional)')
        parser.add_argument('--close', action='store_true', help='Close current action')
        parser.add_argument('--list', action='store_true', help='List available options')
        parser.add_argument('--help-cursor', action='store_true', help='List all cursor commands and parameters')
        parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
        parser.add_argument('--skiprule', nargs='*', help='Rule names to skip during validation (e.g., eliminate_duplication)')
        parser.add_argument('context', nargs='*', help='Additional context (file paths, parameters, etc.)')
        
        args, unknown = parser.parse_known_args()
        
        if args.action:
            action_might_be_file = BaseBotCli._looks_like_file_path(args.action)
            if action_might_be_file:
                unknown.append(args.action)
                args.action = None
        
        all_args = list(unknown) + (getattr(args, 'context', []) or [])
        params = BaseBotCli._parse_action_parameters(all_args)
        
        if args.user_message:
            params['user_message'] = args.user_message
        
        if args.skiprule:
            params['skiprule'] = args.skiprule
        
        return args, params
    
    @staticmethod
    def _looks_like_file_path(arg: str) -> bool:
        if not arg:
            return False
        arg_clean = arg.lstrip('@')
        return (
            '.' in arg_clean and (arg_clean.endswith(('.txt', '.md', '.json', '.yaml', '.yml', '.py', '.js', '.ts')) or
                                 '/' in arg_clean or '\\' in arg_clean) or
            arg_clean.startswith(('./', '../')) or
            '/' in arg_clean or '\\' in arg_clean
        )
    
    @staticmethod
    def _looks_like_directory_path(arg: str) -> bool:
        """Check if argument looks like a directory path (not a specific file)."""
        if not arg:
            return False
        arg_clean = arg.lstrip('@')
        # If it has path separators but no file extension, likely a directory
        has_separator = '/' in arg_clean or '\\' in arg_clean
        has_extension = '.' in arg_clean and any(arg_clean.endswith(ext) for ext in ('.txt', '.md', '.json', '.yaml', '.yml', '.py', '.js', '.ts', '.ps1', '.sh', '.bat'))
        return has_separator and not has_extension
    
    @staticmethod
    def _append_to_param(params: Dict, key: str, value: str) -> None:
        """Append value to params[key], handling str/list conversion."""
        if key not in params:
            params[key] = [value]
        elif isinstance(params[key], str):
            params[key] = [params[key], value]
        else:
            params[key].append(value)
    
    @staticmethod
    def _parse_key_value_arg(arg: str, params: Dict) -> None:
        """Parse an argument with '=' separator."""
        key, value = arg.split('=', 1)
        key = key.lstrip('--')
        
        if key in ['test', 'src'] and ',' in value:
            params[key] = [f.strip() for f in value.split(',')]
        else:
            params[key] = value
    
    @staticmethod
    def _parse_file_list_arg(unknown_args: list, start_idx: int, key: str, params: Dict) -> int:
        """Parse --test or --src followed by file paths. Returns new index."""
        file_list = []
        i = start_idx
        while i < len(unknown_args):
            next_arg = unknown_args[i]
            if not BaseBotCli._looks_like_file_path(next_arg) and not BaseBotCli._looks_like_directory_path(next_arg):
                break
            file_list.append(next_arg.lstrip('@'))
            i += 1
        
        if file_list:
            params[key] = file_list if len(file_list) > 1 else file_list[0]
        return i
    
    @staticmethod
    def _parse_file_path_arg(arg: str, params: Dict) -> None:
        """Parse a standalone file path argument."""
        file_path = arg.lstrip('@')
        
        if BaseBotCli._looks_like_directory_path(arg):
            BaseBotCli._append_to_param(params, 'src', file_path)
            return
        
        if file_path.endswith('.py'):
            file_name = Path(file_path).name
            is_test_file = file_name.startswith('test_') or file_name.endswith('_test.py')
            target_key = 'test' if is_test_file else 'src'
            BaseBotCli._append_to_param(params, target_key, file_path)
            return
        
        if 'increment_file' not in params:
            params['increment_file'] = file_path
        else:
            BaseBotCli._append_to_param(params, 'context_files', file_path)
    
    @staticmethod
    def _parse_context_arg(arg: str, params: Dict) -> None:
        """Parse a context argument (non-file, non-flag)."""
        if 'context' not in params:
            params['context'] = arg
        elif isinstance(params['context'], str):
            params['context'] = [params['context'], arg]
        else:
            params['context'].append(arg)
    
    @staticmethod
    def _parse_action_parameters(unknown_args: list) -> Dict[str, str]:
        params = {}
        i = 0
        
        while i < len(unknown_args):
            arg = unknown_args[i]
            if not arg:
                i += 1
                continue
            
            if '=' in arg:
                BaseBotCli._parse_key_value_arg(arg, params)
                i += 1
            elif arg in ['--test', '--src']:
                key = arg.lstrip('--')
                i = BaseBotCli._parse_file_list_arg(unknown_args, i + 1, key, params)
            elif arg.startswith('--'):
                i += 1
            elif BaseBotCli._looks_like_file_path(arg):
                BaseBotCli._parse_file_path_arg(arg, params)
                i += 1
            else:
                BaseBotCli._parse_context_arg(arg, params)
                i += 1
        
        return params
    
    def main(self):
        # Configure logging early so we can see what's happening
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.StreamHandler(sys.stdout)],
            force=True  # Override any existing configuration
        )
        logger.info("=== CLI Starting ===")
        logger.info(f"Bot: {self.bot_name}")
        try:
            args, params = BaseBotCli.parse_arguments(description=f"{self.bot_name} CLI")
        except Exception as e:
            # Handle exceptions in argument parsing
            self._handle_error(e)
            sys.exit(1)
        
        try:
            if args.help:
                self.help_behaviors_and_actions()
                return None
            elif args.help_cursor:
                self.help_cursor_commands()
                return None
            elif args.list:
                self._handle_list_command(args.behavior)
                return None
            else:
                result = self._execute_and_output(args, params)
                return result
        except (SystemExit, KeyboardInterrupt):
            # Re-raise system exits and keyboard interrupts
            raise
        except Exception as e:
            # Safety net: If exception reached here and wasn't handled by _handle_error,
            # print it now. _handle_error prints and re-raises, so if we're here, either:
            # 1. The exception was already printed by _handle_error (most common case)
            # 2. The exception bypassed _handle_error (shouldn't happen, but ensure we catch it)
            # To avoid duplicates, we check if this looks like an unhandled exception
            # by ensuring stdout was flushed and error was visible
            # Print error with clear markers so it's visible
            print("\n---", file=sys.stderr)
            print("**ERROR OCCURRED IN MAIN**", file=sys.stderr)
            print("---", file=sys.stderr)
            print(f"\n**Exception Type:** {type(e).__name__}", file=sys.stderr)
            print(f"**Exception Message:** {str(e)}", file=sys.stderr)
            print(f"\n**Full Traceback:**", file=sys.stderr)
            print("-" * 70, file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            print("-" * 70, file=sys.stderr)
            print("---\n", file=sys.stderr)
            # Also print to stdout in case stderr isn't captured
            print("\n---")
            print("**ERROR OCCURRED IN MAIN**")
            print("---")
            print(f"\n**Exception Type:** {type(e).__name__}")
            print(f"**Exception Message:** {str(e)}")
            print(f"\n**Full Traceback:**")
            print("-" * 70)
            traceback.print_exc()
            print("-" * 70)
            print("---\n")
            sys.stdout.flush()
            sys.stderr.flush()
            sys.exit(1)
    
    def _execute_and_output(self, args, params: Dict[str, str]):
        logger.info(f"Executing: behavior={args.behavior}, action={args.action}")
        logger.info(f"Parameters: {params}")
        if 'src' in params:
            logger.info(f"  src paths: {params['src']}")
        try:
            if args.close:
                logger.info("Closing current action...")
                result = self.close_current_action()
            else:
                action_name = args.action
                if action_name is None and args.behavior:
                    pass
                
                logger.info(f"Running action: {action_name} in behavior: {args.behavior}")
                result = self.run(
                    behavior_name=args.behavior,
                    action_name=action_name,
                    **params
                )
                logger.info("Action execution completed")
            
            # Extract and print instructions for AI to read and display
            # CRITICAL: Instructions must be printed so AI can see them
            data = result.get('data', {})
            instructions = data.get('instructions', {})
            
            # Handle both dict and direct list formats
            if isinstance(instructions, dict):
                base_instructions = instructions.get('base_instructions', [])
            elif isinstance(instructions, list):
                # If instructions is directly a list, treat it as base_instructions
                base_instructions = instructions
            else:
                base_instructions = []
            
            # Print ALL instructions directly - these are for the AI to read and display
            if isinstance(base_instructions, list) and len(base_instructions) > 0:
                for instruction in base_instructions:
                    # Handle Unicode encoding for Windows console (cp1252)
                    try:
                        print(instruction)
                    except UnicodeEncodeError:
                        # Replace Unicode characters that can't be encoded
                        safe_instruction = instruction.encode('ascii', errors='replace').decode('ascii')
                        print(safe_instruction)
                sys.stdout.flush()
            
            # Also print JSON result for programmatic access
            result_json = json.dumps(result, indent=2)
            print(result_json)
            sys.stdout.flush()
            
            return result
        except Exception as e:
            self._handle_error(e)
    
    def _handle_list_command(self, behavior_name: str = None):
        try:
            if behavior_name:
                self.list_actions(behavior_name)
            else:
                self.list_behaviors()
        except Exception as e:
            self._handle_error(e)
    
    def _handle_error(self, error: Exception):
        """Print exception to chat window (stdout) with full traceback."""
        print("\n" + "=" * 70)
        print("**ERROR OCCURRED**")
        print("=" * 70)
        print(f"\nException Type: {type(error).__name__}")
        print(f"Exception Message: {str(error)}")
        print("\nFull Traceback:")
        print("-" * 70)
        traceback.print_exc()
        print("-" * 70)
        print("=" * 70 + "\n")
        sys.stdout.flush()
        # Re-raise so main() can handle exit
        raise error
    
    def _get_breadcrumbs_from_action(self) -> list:
        """
        Get breadcrumbs from the current action's breadcrumb functionality.
        This is the ONLY way breadcrumbs are generated - always goes through BaseActions.
        
        Actions are responsible for generating the CONTENT (raw breadcrumb data).
        CLI is responsible for FORMATTING the content (colors, styling).
        
        Returns:
            List of breadcrumb strings, or empty list if unable to generate
        """
        if not self.bot:
            return []
        
        try:
            current_behavior = self.bot.behaviors.current
            if not current_behavior:
                # Try to navigate to first behavior if none is current
                if self.bot.behaviors.first:
                    self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
                    current_behavior = self.bot.behaviors.current
                if not current_behavior:
                    # No behavior available - return empty tree
                    return []
            
            # Load action state to ensure current action is set
            current_behavior.actions.load_state()
            current_action = current_behavior.actions.current
            
            if not current_action:
                # No current action - return empty tree
                return []
            
            # ALWAYS get breadcrumbs from the action instance (single source of truth)
            breadcrumbs = current_action.get_workflow_status_breadcrumbs()
            return breadcrumbs if breadcrumbs else []
            
        except Exception as e:
            # If anything fails, return empty tree (don't print errors, just fail silently)
            logger.debug(f"Failed to get breadcrumbs from action: {e}")
            return []
    

