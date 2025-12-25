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

    def _prepare_instructions(self, instructions, context: ValidateActionContext):
        """Prepare validation instructions with rules and validation data."""
        # Get rules with file paths for AI to read
        rules_text = self._format_rules_with_file_paths()
        
        # Get story graph schema path
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        
        # Get scope description
        scope_text = self._format_scope_description(context)
        
        # Build replacement data
        replacements = {
            'rules': rules_text if rules_text else 'No rules defined',
            'scanner_output': 'Scanner violations are shown above in the validation report.',
            'schema': f'**Schema:** Story graph at `{schema_path}`',
            'description': f'Validate **{self.behavior.name}** artifacts against rules. Scanner results shown above.',
            'scope': scope_text
        }
        
        # Replace placeholders in base instructions (both {{}} and {} formats)
        base_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        for line in base_instructions:
            if isinstance(line, str):
                # Replace {{placeholder}} format
                for key, value in replacements.items():
                    placeholder = '{{' + key + '}}'
                    if placeholder in line:
                        line = line.replace(placeholder, value)
                # Replace {placeholder} format
                for key, value in replacements.items():
                    placeholder = '{' + key + '}'
                    if placeholder in line:
                        line = line.replace(placeholder, value)
            new_instructions.append(line)
        
        instructions._data['base_instructions'] = new_instructions

    def _format_scope_description(self, context: ValidateActionContext) -> str:
        """Format scope description for validation instructions."""
        if context.scope:
            scope_dict = context.scope
            scope_type = scope_dict.get('type', 'all')
            scope_value = scope_dict.get('value', [])
            
            if scope_type == 'epic':
                return f"epic(s): {', '.join(scope_value)}"
            elif scope_type == 'story':
                return f"story/stories: {', '.join(scope_value)}"
            elif scope_type == 'files':
                return f"file(s): {', '.join(scope_value)}"
            else:
                return "all epics, sub-epics, stories, and domain concepts in the knowledge graph"
        else:
            return "all epics, sub-epics, stories, and domain concepts in the knowledge graph"

    def _format_rules_with_file_paths(self) -> str:
        """Format rules with file paths for AI to read and analyze."""
        rules_data = self.inject_behavior_specific_and_bot_rules()
        all_rules = rules_data.get('validation_rules', [])
        
        if not all_rules:
            return 'No validation rules found.'
        
        lines = []
        lines.append("**Rules to validate against (read each file for full DO/DON'T examples):**")
        lines.append("")
        
        for rule in all_rules:
            rule_file = rule.get('rule_file', 'unknown')
            rule_content = rule.get('rule_content', {})
            
            # Extract rule info
            name = rule_content.get('name', rule_file.split('/')[-1].replace('.json', '').replace('_', ' ').title())
            description = rule_content.get('description', 'No description')
            priority = rule_content.get('priority', 99)
            has_scanner = 'scanner' in rule_content or 'scanners' in rule_content
            
            # Format rule entry with file path
            scanner_status = '[Scanner]' if has_scanner else '[Manual Check]'
            lines.append(f"### Rule: {name} (Priority {priority}) {scanner_status}")
            lines.append(f"**File:** `{rule_file}`")
            lines.append(f"**Description:** {description}")
            
            # Add DO section
            do_section = rule_content.get('do', {})
            do_desc = do_section.get('description', '')
            if do_desc:
                lines.append(f"**DO:** {do_desc}")
            
            # Add DON'T section
            dont_section = rule_content.get('dont', {})
            dont_desc = dont_section.get('description', '')
            if dont_desc:
                lines.append(f"**DON'T:** {dont_desc}")
            
            lines.append("")
        
        lines.append("**IMPORTANT:** For rules marked [Manual Check], you MUST read the rule file and manually verify compliance since no scanner exists.")
        
        return '\n'.join(lines)
    
    def _do_submit(self, context: ValidateActionContext) -> Dict[str, Any]:
        """Run validation scanners and generate reports."""
        logger.info('=== Starting validation ===')
        logger.info(f'Behavior: {self.behavior.name}')
        logger.info(f'Context: scope={context.scope}, skip_cross_file={context.skip_cross_file}')
        
        result = self._executor.execute_synchronous(context)
        
        return {
            'status': 'submitted',
            'message': 'Validation completed',
            'validation_result': result
        }
    
    def do_execute(self, context: ValidateActionContext) -> Dict[str, Any]:
        """Legacy method for backwards compatibility."""
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