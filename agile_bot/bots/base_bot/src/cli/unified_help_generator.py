from typing import List
from agile_bot.bots.base_bot.src.cli.help_renderer import HelpRenderer
from agile_bot.bots.base_bot.src.cli.description_extractor import DescriptionExtractor
from agile_bot.bots.base_bot.src.bot.workspace import get_base_actions_directory
from agile_bot.bots.base_bot.src.utils import read_json_file

class UnifiedHelpGenerator:
    
    def __init__(self, bot, bot_name: str, bot_directory, renderer: HelpRenderer, description_extractor: DescriptionExtractor):
        self.bot = bot
        self.bot_name = bot_name
        self.bot_directory = bot_directory
        self.renderer = renderer
        self.description_extractor = description_extractor
        self.action_order = ['clarify', 'strategy', 'build', 'validate', 'render']
    
    def generate_help(self) -> None:
        self.renderer.render_header(self.bot_name)
        behaviors_list = list(self.bot.behaviors)
        sorted_behaviors = self._sort_behaviors_for_display(behaviors_list)
        for behavior in sorted_behaviors:
            self._render_behavior(behavior)
        self._render_action_help_section()
    
    def _sort_behaviors_for_display(self, behaviors):
        behaviors_list = list(behaviors)
        behaviors_with_order = []
        for behavior in behaviors_list:
            order = self._get_behavior_order(behavior)
            behaviors_with_order.append((order, behavior))
        behaviors_with_order.sort(key=lambda x: x[0])
        return [behavior for _, behavior in behaviors_with_order]
    
    def _get_behavior_order(self, behavior) -> int:
        behavior_json_path = self.bot_directory / 'behaviors' / behavior.name / 'behavior.json'
        try:
            config = read_json_file(behavior_json_path)
            return config.get('order', 999)
        except (FileNotFoundError, KeyError):
            return 999
    
    def _render_behavior(self, behavior) -> None:
        from agile_bot.bots.base_bot.src.cli.help_context import BehaviorHelpContext
        behavior_name = behavior.name
        behavior_description = self.description_extractor.get_behavior_description(f'{self.bot_name}-{behavior_name}')
        actions = self._get_behavior_actions(behavior)
        additional_options = self._get_additional_options(behavior_name)
        context = BehaviorHelpContext(
            bot_name=self.bot_name,
            behavior_name=behavior_name,
            behavior_description=behavior_description,
            actions=actions,
            additional_options=additional_options
        )
        self.renderer.render_behavior_section(context)
    
    def _get_behavior_actions(self, behavior) -> List[str]:
        action_names_str = self.description_extractor.get_action_names_from_behavior(behavior.name)
        return action_names_str.split('|') if action_names_str else []
    
    def _get_additional_options(self, behavior_name: str) -> dict:
        if behavior_name == 'code':
            return {
                '--exclude <patterns>': "File patterns to exclude (e.g., '--exclude scanners folder')",
                '--skiprule <rules>': "Rule names to skip (e.g., '--skiprule eliminate_duplication')"
            }
        return None
    
    def _render_action_help_section(self) -> None:
        from agile_bot.bots.base_bot.src.cli.help_context import ActionHelpContext
        self.renderer.render_action_help_section_header()
        for action_name in self.action_order:
            action_description = self.description_extractor.get_action_description(action_name)
            if action_name == 'validate':
                action_description += '\n\n**NOTE:** For code behavior, validation runs in background. You MUST poll the status file every 10 seconds and report progress until complete.'
            parameters = self._get_action_parameters(action_name)
            parameter_descriptions = self._get_parameter_descriptions(action_name, parameters)
            context = ActionHelpContext(
                bot_name=self.bot_name,
                action_name=action_name,
                action_description=action_description,
                parameters=parameters,
                parameter_descriptions=parameter_descriptions
            )
            self.renderer.render_action_help(context)
    
    def _get_action_parameters(self, action_name: str) -> List[str]:
        parameter_map = {
            'clarify': ['--key_questions_answered <dict>', '--evidence_provided <dict>'],
            'strategy': ['--decisions_made <dict>', '--assumptions_made <list>'],
            'build': ['--scope <dict>'],
            'validate': ['--scope <dict>'],
            'render': ['--scope <dict>']
        }
        return parameter_map.get(action_name, [])
    
    def _get_parameter_descriptions(self, action_name: str, parameters: List[str]) -> dict:
        descriptions = {}
        for param in parameters:
            description = self._get_single_parameter_description(action_name, param)
            descriptions[param] = description
        return descriptions
    
    def _get_single_parameter_description(self, action_name: str, param: str) -> str:
        if 'key_questions_answered' in param:
            return "Dict mapping question keys to answer strings"
        if 'evidence_provided' in param:
            return "Dict mapping evidence types to evidence content"
        if 'decisions_made' in param:
            return "Dict mapping decision criteria keys to selected options/values"
        if 'assumptions_made' in param:
            return "List of assumption strings"
        if 'scope' in param:
            return self._get_scope_description(action_name)
        return "Optional parameter"
    
    def _get_scope_description(self, action_name: str) -> str:
        if action_name == 'validate':
            return "Scope structure:\n{'type': 'story'|'epic'|'increment'|'all'|'files', 'value': <names|priorities|files>, 'exclude': <patterns>}"
        return "Scope structure:\n{'type': 'story'|'epic'|'increment'|'all', 'value': <names|priorities>}"
