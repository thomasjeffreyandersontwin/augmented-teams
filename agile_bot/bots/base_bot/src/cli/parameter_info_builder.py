import re
from pathlib import Path
from typing import Optional

class ParameterInfoBuilder:
    """Builds parameter information for command help generation."""

    def __init__(self, bot_name: str, bot_directory: Path, description_extractor):
        self.bot_name = bot_name
        self.bot_directory = bot_directory
        self.description_extractor = description_extractor

    def build_param_info(self, cmd_name: str, params: list, cmd_content: str) -> tuple:
        """Build parameter placeholders and details from parameter numbers."""
        param_placeholders = []
        param_details = []
        for param_num in params:
            param_desc = self.infer_parameter_description(cmd_name, param_num, cmd_content)
            placeholder = self.extract_placeholder_name(cmd_name, param_desc, param_num)
            param_placeholders.append(f'<{placeholder}>')
            self.add_param_detail(param_num, cmd_name, placeholder, param_desc, param_details)
        return (param_placeholders, param_details)

    def add_param_detail(self, param_num: str, cmd_name: str, placeholder: str, param_desc: str, param_details: list):
        """Add parameter detail line to the details list."""
        handlers = {
            '1': lambda: self._add_param_1_detail(placeholder, param_details),
            '2': lambda: self.add_param_2_details(cmd_name, param_details),
            '3': lambda: self._add_param_3_detail(cmd_name, param_details),
            '4': lambda: self._add_param_4_detail(cmd_name, param_details),
        }
        handler = handlers.get(param_num)
        if not handler:
            self._add_default_param_detail(placeholder, param_desc, param_details)
            return
        handler()

    def _add_param_1_detail(self, placeholder: str, param_details: list):
        """Add detail for parameter 1 (action parameter)."""
        param_details.append(f'action:   {placeholder}')

    def _add_param_3_detail(self, cmd_name: str, param_details: list):
        """Add detail for parameter 3 (exclude patterns for code commands)."""
        if 'code' in cmd_name.lower():
            param_details.append('exclude:  File patterns to exclude (--exclude flag added automatically)')
        else:
            # This shouldn't normally happen, but handle gracefully
            param_details.append('param3:   Parameter 3')

    def _add_param_4_detail(self, cmd_name: str, param_details: list):
        """Add detail for parameter 4 (additional exclude patterns for code commands)."""
        if 'code' in cmd_name.lower():
            param_details.append('exclude:  Additional exclude patterns (continues from previous)')
        else:
            # This shouldn't normally happen, but handle gracefully
            param_details.append('param4:   Parameter 4')

    def _add_default_param_detail(self, placeholder: str, param_desc: str, param_details: list):
        """Add default parameter detail."""
        param_details.append(f'{placeholder}:   {param_desc}')

    def add_param_2_details(self, cmd_name: str, param_details: list):
        """Add details for parameter 2 (context parameter)."""
        if 'code' in cmd_name.lower():
            param_details.append("context:  Optional context or file path (e.g., 'src')")
            param_details.append('           Additional options:')
            param_details.append("           --exclude <patterns>  File patterns to exclude (e.g., '--exclude scanners folder')")
            param_details.append("           --skiprule <rules>    Rule names to skip (e.g., '--skiprule eliminate_duplication')")
        else:
            param_details.append('context:  Optional context or file path')

    def infer_parameter_description(self, cmd_name: str, param_num: str, cmd_content: str) -> str:
        """Infer parameter description from command name and parameter number."""
        if 'continue' in cmd_name or 'help' in cmd_name:
            return 'No parameters'
        if param_num == '1':
            return 'Action name (e.g., clarify, strategy, build, render, validate)'
        if param_num == '2':
            return 'Optional context or file path'
        if param_num == '3' and 'code' in cmd_name:
            return 'Optional: File patterns to exclude (e.g., scanners folder). The --exclude flag is added automatically.'
        if param_num == '4' and 'code' in cmd_name:
            return 'Additional exclude patterns (continues from $3)'
        return f'Parameter {param_num}'

    def extract_placeholder_name(self, cmd_name: str, param_desc: str, param_num: str) -> str:
        """Extract placeholder name for a parameter."""
        if param_num == '2':
            return 'context'
        if param_num != '1':
            return self.extract_word_from_description(param_desc, param_num)
        behavior_name = cmd_name.replace(f'{self.bot_name}-', '').replace('-', '_')
        if behavior_name in ['continue', 'help', ''] or cmd_name == self.bot_name:
            return 'action'
        action_names = self.description_extractor.get_action_names_from_behavior(behavior_name)
        return action_names if action_names else 'action'

    def extract_word_from_description(self, param_desc: str, param_num: str) -> str:
        """Extract a meaningful word from parameter description for placeholder."""
        skip_words = {'optional', 'action', 'name', 'or', 'file', 'path'}
        words = param_desc.lower().split()
        for word in words:
            if word not in skip_words and len(word) > 2:
                return word
        return f'param{param_num}'

