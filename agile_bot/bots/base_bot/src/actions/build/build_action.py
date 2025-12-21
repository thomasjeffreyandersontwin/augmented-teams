from pathlib import Path
from typing import Dict, Any, Optional, Type
import logging
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.action_context import ActionContext, ScopeActionContext
from agile_bot.bots.base_bot.src.actions.build.knowledge import Knowledge
from agile_bot.bots.base_bot.src.actions.build.knowledge_graph_spec import KnowledgeGraphSpec
from agile_bot.bots.base_bot.src.actions.build.knowledge_graph_template import KnowledgeGraphTemplate
from agile_bot.bots.base_bot.src.actions.build.build_scope import BuildScope
from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
logger = logging.getLogger(__name__)

class BuildKnowledgeAction(Action):
    context_class: Type[ActionContext] = ScopeActionContext

    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        self._knowledge = Knowledge(self.behavior)

    @property
    def action_name(self) -> str:
        return 'build'

    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError('action_name is read-only for BuildKnowledgeAction')

    @property
    def knowledge(self) -> Optional[Knowledge]:
        self._knowledge = Knowledge(self.behavior)
        return self._knowledge

    @property
    def knowledge_graph_spec(self) -> Optional[KnowledgeGraphSpec]:
        return self.knowledge.knowledge_graph_spec

    @property
    def knowledge_graph_template(self) -> Optional[KnowledgeGraphTemplate]:
        return self.knowledge.knowledge_graph_template

    @property
    def rules(self):
        return ValidateRulesAction(behavior=self.behavior, action_config=None)

    def do_execute(self, context: ScopeActionContext) -> Dict[str, Any]:
        instructions = self.instructions.copy()
        instructions.update(self.knowledge.instructions)
        build_scope = BuildScope.from_context(context, self.behavior.bot_paths)
        instructions.set('scope', build_scope.scope)
        story_names = build_scope.get_story_names(self.knowledge_graph_spec.knowledge_graph.content)
        instructions.set('scope_story_names', list(story_names) if story_names else [])
        self._add_update_instructions(instructions)
        self.inject_rules(instructions)
        return {'instructions': instructions.to_dict()}

    def _add_update_instructions(self, instructions) -> None:
        file_exists = self.knowledge_graph_spec.knowledge_graph.path.exists()
        instructions.set('existing_file', {'path': str(self.knowledge_graph_spec.knowledge_graph.path), 'exists': file_exists})
        
        if file_exists:
            instructions.set('update_mode', True)
            instructions.set('update_instructions', {'mode': 'update_existing', 'message': f"**CRITICAL: Output file '{self.knowledge_graph_spec.knowledge_graph.path.name}' already exists. You MUST UPDATE this existing file by adding/modifying only the content needed for this behavior. DO NOT create a new file.**", 'existing_file_path': str(self.knowledge_graph_spec.knowledge_graph.path), 'preserve_existing': self._get_preserve_existing(self.knowledge_graph_spec.knowledge_graph), 'add_or_modify': self._determine_add_or_modify_content()})
        else:
            instructions.set('create_mode', True)
            instructions.set('create_instructions', {'mode': 'create_new', 'message': f"**CRITICAL: Output file '{self.knowledge_graph_spec.knowledge_graph.path.name}' does not exist. You MUST CREATE this file with the complete structure based on the provided template and rules.**", 'output_file_path': str(self.knowledge_graph_spec.knowledge_graph.path)})

    def _get_preserve_existing(self, story_graph) -> list:
        return [item for item in ['epics' if story_graph.has_epics else None, 'increments' if story_graph.has_increments else None, 'domain_concepts' if story_graph.has_domain_concepts else None] if item is not None]

    def _determine_add_or_modify_content(self) -> list:
        behavior_to_content = {'shape': [], 'prioritization': ['increments'], 'discovery': ['story refinements', 'increments', 'domain_concepts'], 'exploration': ['acceptance_criteria', 'domain_concepts'], 'scenarios': ['scenarios', 'domain_concepts'], 'tests': ['test_implementations', 'domain_concepts']}
        return behavior_to_content.get(self.behavior.name, [])

    def inject_rules(self, instructions) -> None:
        validate_action = self.rules
        rules_obj = validate_action.rules
        rules_text = rules_obj.formatted_rules()
        rules_data = validate_action.inject_behavior_specific_and_bot_rules()
        all_rules = rules_data.get('validation_rules', [])
        
        # Get existing base_instructions (these are the CUSTOM INSTRUCTIONS - keep them FIRST)
        existing_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        rules_section = []
        
        # Process each instruction, removing {{rules}} placeholder if present
        # Keep ALL other instructions as-is (they are the custom instructions)
        for line in existing_instructions:
            if isinstance(line, str) and '{{rules}}' in line:
                # Remove the placeholder line - we'll add rules at the very end
                pass  # Don't add this line
            else:
                # Keep all custom instructions
                new_instructions.append(line)
        
        # Prepare rules section to append at the END
        if rules_text != 'No validation rules found.':
            rules_lines = rules_text.split('\n')
            rules_section.extend(rules_lines)
        
        # CRITICAL: Append rules section at the VERY END (after ALL custom instructions)
        # This ensures: CUSTOM INSTRUCTIONS FIRST, RULES LAST
        if rules_section:
            new_instructions.append('')  # Blank line separator
            new_instructions.append('**VALIDATION RULES:**')  # Section header
            new_instructions.append('')  # Blank line
            new_instructions.extend(rules_section)
        
        # Replace base_instructions with: [custom instructions] + [rules at end]
        instructions._data['base_instructions'] = new_instructions
        instructions.set('rules', all_rules)