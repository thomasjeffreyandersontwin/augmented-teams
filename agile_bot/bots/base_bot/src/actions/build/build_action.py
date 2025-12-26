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

    def _prepare_instructions(self, instructions, context: ScopeActionContext):
        """Prepare build instructions with knowledge graph data, rules, and scope."""
        # Add knowledge instructions
        instructions.update(self.knowledge.instructions)
        
        # Handle scope
        build_scope = BuildScope.from_context(context, self.behavior.bot_paths)
        instructions.set('scope', build_scope.scope)
        story_names = build_scope.get_story_names(self.knowledge_graph_spec.knowledge_graph.content)
        instructions.set('scope_story_names', list(story_names) if story_names else [])
        
        # Add knowledge_graph_template and knowledge_graph_config for test compatibility
        if self.knowledge_graph_template:
            instructions.set('knowledge_graph_template', {
                'template_path': str(self.knowledge_graph_template.template_path) if self.knowledge_graph_template.template_path else None,
                'exists': self.knowledge_graph_template.exists
            })
        if self.knowledge_graph_spec.config_data:
            instructions.set('knowledge_graph_config', {
                'output': self.knowledge_graph_spec.output_filename,
                'path': self.knowledge_graph_spec.output_path,
                'template': self.knowledge_graph_spec.template_filename
            })
        
        # Add update/create instructions
        self._add_update_instructions(instructions)
        
        # Replace placeholders
        self._replace_schema_placeholders(instructions)
        
        # Inject rules
        self.inject_rules(instructions)
        
        # Replace content with file references
        self._replace_content_with_file_references(instructions)
    
    def _do_submit(self, context: ScopeActionContext) -> Dict[str, Any]:
        """Build actions don't have a submit step - AI does the work directly."""
        return {
            'status': 'submitted',
            'message': 'Build instructions provided to AI - knowledge graph will be built by AI'
        }
    
    def do_execute(self, context: ScopeActionContext) -> Dict[str, Any]:
        """Legacy method for backwards compatibility."""
        result = self.get_instructions(context)
        return result

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
    
    def _replace_schema_placeholders(self, instructions) -> None:
        """Replace {{schema}} and {{description}} placeholders in base_instructions with template references."""
        base_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        
        template = self.knowledge_graph_template
        description_lines_list = []
        
        if template and template.exists:
            template_path = template.template_path
            if template_path:
                # Create relative path reference: bot_name/behaviors/behavior_name/content/knowledge_graph/template_filename
                bot_dir = self.behavior.bot_paths.bot_directory
                try:
                    if template_path.is_absolute():
                        # Make it relative to bot directory, then prepend bot_name
                        try:
                            rel_path = template_path.relative_to(bot_dir)
                            template_reference = f"{self.behavior.bot_name}/{str(rel_path).replace('\\', '/')}"
                        except ValueError:
                            # If can't make relative, construct the expected path
                            template_reference = f"{self.behavior.bot_name}/behaviors/{self.behavior.name}/content/knowledge_graph/{template_path.name}"
                    else:
                        # Already relative, prepend bot_name
                        template_reference = f"{self.behavior.bot_name}/{str(template_path).replace('\\', '/')}"
                except Exception:
                    # Fallback to constructing the expected path
                    template_reference = f"{self.behavior.bot_name}/behaviors/{self.behavior.name}/content/knowledge_graph/{template_path.name if template_path else 'template.json'}"
            else:
                # No template path available
                template_reference = f"{self.behavior.bot_name}/behaviors/{self.behavior.name}/content/knowledge_graph/template.json"
            
            # Get output filename and path
            output_filename = self.knowledge_graph_spec.output_filename if self.knowledge_graph_spec else 'knowledge-graph.json'
            output_path = str(self.knowledge_graph_spec.knowledge_graph.path.parent) if self.knowledge_graph_spec else ''
            
            # Create description text for template file and output instructions
            description_lines_list = [
                f"Review the template file at `{template_reference}`. It shows the exact structure (fields, nesting, types) that your knowledge graph output must follow during this behavior. Read this file to understand the required schema.",
                "",
                f"Create `{output_filename}` if it does not exist. Place file at `{output_path}/`. Using the template for guidance.",
                "",
                f"If the file already exists then make SAFE edits only. Preserve existing structure and content. Add or modify only what is necessary. Do NOT overwrite indiscriminately unless explicitly asked. When adding nodes to the graph follow the template and do not add extra elements that you might see in other nodes, they will be added as a part of later behaviors."
            ]
        
        for line in base_instructions:
            if isinstance(line, str):
                if '{{schema}}' in line:
                    # Skip schema placeholder - not needed
                    pass
                elif '{{description}}' in line:
                    if description_lines_list:
                        # Add each description line as a separate instruction
                        new_instructions.extend(description_lines_list)
                    else:
                        # Remove the line if no description available
                        pass
                else:
                    new_instructions.append(line)
            else:
                new_instructions.append(line)
        
        instructions._data['base_instructions'] = new_instructions

    def inject_rules(self, instructions) -> None:
        validate_action = self.rules
        rules_obj = validate_action.rules
        rules_text = rules_obj.formatted_rules_digest()
        rules_data = validate_action.inject_behavior_specific_and_bot_rules()
        all_rules = rules_data.get('validation_rules', [])
        
        # Get existing base_instructions (these are the CUSTOM INSTRUCTIONS - keep them FIRST)
        existing_instructions = instructions.get('base_instructions', [])
        new_instructions = []
        rules_section = []
        
        # Get schema path for placeholder replacement
        schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        
        # Keep ALL other instructions, replacing placeholders as we go
        for line in existing_instructions:
            if isinstance(line, str):
                # Replace {{rules}} - skip it here, will add rules section at the end
                if '{{rules}}' in line:
                    continue
                # Replace {{schema}} placeholder
                if '{{schema}}' in line:
                    line = line.replace('{{schema}}', f'**Schema:** Story graph template at `{schema_path}`')
                # Replace {{description}} placeholder
                if '{{description}}' in line:
                    line = line.replace('{{description}}', f'**Task:** Build {self.behavior.name} knowledge graph from clarification and strategy data')
            # Keep all custom instructions
            new_instructions.append(line)
        
        # Prepare rules section to append at the END
        if rules_text != 'No validation rules found.':
            rules_lines = rules_text.split('\n')
            rules_section.extend(rules_lines)
        
        # Append rules section at the VERY END (after ALL custom instructions)
        if rules_section:
            # Strip trailing blank lines before adding rules
            while new_instructions and new_instructions[-1] == '':
                new_instructions.pop()
            new_instructions.append('')
            new_instructions.append('When building or adding to the story graph follow these rules,')
            new_instructions.extend(rules_section)
        
        # Replace base_instructions with: [custom instructions] + [rules at end]
        instructions._data['base_instructions'] = new_instructions
        instructions.set('rules', all_rules)

    def _replace_content_with_file_references(self, instructions) -> None:
        """Replace full content (templates, configs, rules) with file path references."""
        bot_dir = self.behavior.bot_paths.bot_directory
        
        # Convert template path to relative reference
        template_path = instructions.get('template_path')
        if template_path:
            try:
                template_path_obj = Path(template_path)
                if template_path_obj.is_absolute():
                    rel_path = template_path_obj.relative_to(bot_dir)
                    template_reference = f"{self.behavior.bot_name}/{str(rel_path).replace('\\', '/')}"
                else:
                    template_reference = f"{self.behavior.bot_name}/{str(template_path).replace('\\', '/')}"
            except Exception:
                template_reference = template_path
            instructions._data['template_path'] = template_reference
        
        # Convert config path to relative reference
        config_path = instructions.get('config_path')
        if config_path:
            try:
                config_path_obj = Path(config_path)
                if config_path_obj.is_absolute():
                    rel_path = config_path_obj.relative_to(bot_dir)
                    config_reference = f"{self.behavior.bot_name}/{str(rel_path).replace('\\', '/')}"
                else:
                    config_reference = f"{self.behavior.bot_name}/{str(config_path).replace('\\', '/')}"
            except Exception:
                config_reference = config_path
            instructions._data['config_path'] = config_reference
        
        # Replace full rules data with file path references
        if 'rules' in instructions._data and instructions._data['rules']:
            all_rules = instructions._data['rules']
            rule_files = []
            for rule in all_rules:
                if isinstance(rule, dict):
                    rule_file = rule.get('rule_file', '')
                    if rule_file:
                        rule_files.append(rule_file)
                elif isinstance(rule, str):
                    rule_files.append(rule)
            # Replace full rules with just file references
            instructions._data['rules'] = rule_files
            # Keep rules content as-is, no need to add file references
            # Rules are already formatted nicely from inject_rules method