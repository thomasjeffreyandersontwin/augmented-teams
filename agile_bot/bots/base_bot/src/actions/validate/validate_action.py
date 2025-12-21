from typing import Dict, Any, List, Type
import logging
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext, ValidateActionContext
from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
from agile_bot.bots.base_bot.src.actions.validate.validation_executor import ValidationExecutor
from agile_bot.bots.base_bot.src.utils import read_json_file

logger = logging.getLogger(__name__)

class ScannerExecutionError(Exception):

    def __init__(self, rule_file: str, scanner_path: str, original_error: Exception):
        self.rule_file = rule_file
        self.scanner_path = scanner_path
        self.original_error = original_error
        message = f"Scanner execution failed for rule '{rule_file}' (scanner: {scanner_path}): {original_error}"
        super().__init__(message)

class ValidateRulesAction(Action):
    context_class: Type[ActionContext] = ValidateActionContext

    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        self._rules = Rules(behavior=self.behavior, bot_paths=self.behavior.bot_paths)
        self._executor = ValidationExecutor(self.behavior, self._rules)

    @property
    def action_name(self) -> str:
        return 'validate'

    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError('action_name is read-only for ValidateRulesAction')

    @property
    def rules(self) -> Rules:
        return self._rules

    def do_execute(self, context: ValidateActionContext) -> Dict[str, Any]:
        logger.info('=== Starting validation ===')
        logger.info(f'Behavior: {self.behavior.name}')
        logger.info(f'Context: scope={context.scope}, skip_cross_file={context.skip_cross_file}')
        return self._executor.execute_synchronous(context)

    def inject_common_bot_rules(self) -> Dict[str, Any]:
        base_bot_rules_dir = self.bot_dir.parent / 'base_bot' / 'rules'
        common_rules = []
        for rule_file in base_bot_rules_dir.glob('*.json'):
            rule_data = read_json_file(rule_file)
            common_rules.append({'rule_file': f'agile_bot/bots/base_bot/rules/{rule_file.name}', 'rule_content': rule_data})
        return {'validation_rules': common_rules}

    def inject_behavior_specific_and_bot_rules(self) -> Dict[str, Any]:
        all_rules = []
        bot_dir = self.behavior.bot_paths.bot_directory
        bot_rules_dir = bot_dir / 'rules'
        for rule_file in bot_rules_dir.glob('*.json'):
            rule_data = read_json_file(rule_file)
            all_rules.append({'rule_file': f'{bot_dir.name}/rules/{rule_file.name}', 'rule_content': rule_data})
        behavior_rules_dir = bot_dir / 'behaviors' / self.behavior.name / 'rules'
        for rule_file in behavior_rules_dir.glob('*.json'):
            rule_data = read_json_file(rule_file)
            all_rules.append({'rule_file': f'{bot_dir.name}/behaviors/{self.behavior.name}/rules/{rule_file.name}', 'rule_content': rule_data})
        common_rules_data = self.inject_common_bot_rules()
        all_rules.extend(common_rules_data.get('validation_rules', []))
        return {'validation_rules': all_rules}

    def get_action_instructions(self) -> List[str]:
        action_instructions = []
        base_actions_path = self.base_actions_dir
        config_path = base_actions_path / 'validate' / 'action_config.json'
        config = read_json_file(config_path)
        action_instructions = config.get('instructions', [])
        return action_instructions

    def inject_next_action_instructions(self):
        return ''

    def finalize_and_transition(self, next_action: str=None):

        class ActionResult:

            def __init__(self, next_action):
                self.next_action = next_action
        return ActionResult(next_action=next_action)