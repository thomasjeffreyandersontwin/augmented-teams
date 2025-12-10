from pathlib import Path
from typing import Dict, Any
import json
from agile_bot.bots.base_bot.src.bot.base_action import BaseAction
from agile_bot.bots.base_bot.src.bot.behavior_folder_finder import find_nested_subfolder, find_behavior_subfolder

# Note: All file reads in this module use UTF-8 encoding for Windows compatibility


class BuildKnowledgeAction(BaseAction):
    
    def __init__(self, bot_name: str, behavior: str, bot_directory: Path):
        super().__init__(bot_name, behavior, bot_directory, 'build_knowledge')
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute build_knowledge action logic."""
        instructions = self.inject_knowledge_graph_template()
        
        # Add explicit update instructions if existing file was found
        if instructions.get('existing_file') and instructions.get('update_mode'):
            existing_file = instructions['existing_file']
            config = instructions['knowledge_graph_config']
            output_path = config.get('path', 'docs/stories')
            output_filename = config.get('output', 'story-graph.json')
            
            instructions['update_instructions'] = {
                'mode': 'update_existing',
                'message': f"**CRITICAL: Output file '{output_filename}' already exists at '{output_path}/{output_filename}'. You MUST UPDATE this existing file by adding/modifying only the content needed for this behavior. DO NOT create a new file.**",
                'existing_file_path': existing_file['path'],
                'preserve_existing': [
                    'epics' if existing_file.get('has_epics') else None,
                    'domain_concepts' if existing_file.get('has_domain_concepts') else None,
                ],
                'add_or_modify': self._determine_add_or_modify_content()
            }
            # Remove None values
            instructions['update_instructions']['preserve_existing'] = [
                item for item in instructions['update_instructions']['preserve_existing'] if item is not None
            ]

        # Inject validation rules proactively
        validation_rules = self.inject_validation_rules()
        if validation_rules:
            instructions['validation_rules'] = validation_rules
            instructions['token_estimate'] = self._estimate_tokens(instructions)
        
        return {'instructions': instructions}
    
    def _determine_add_or_modify_content(self) -> list:
        """
        Determine what content should be added or modified based on the current behavior.
        
        Returns:
            List of content types to add/modify
        """
        behavior_to_content = {
            'prioritization': ['increments'],
            'discovery': ['story refinements', 'increments', 'domain_concepts'],
            'exploration': ['acceptance_criteria', 'domain_concepts'],
            'scenarios': ['scenarios', 'domain_concepts'],
            'tests': ['test_implementations', 'domain_concepts'],
        }
        
        return behavior_to_content.get(self.behavior, ['knowledge_graph'])
    
    def inject_knowledge_graph_template(self) -> Dict[str, Any]:
        # Find behavior folder (handles numbered prefixes)
        from agile_bot.bots.base_bot.src.bot.bot import Behavior
        behavior_folder = Behavior.find_behavior_folder(
            self.bot_directory,
            self.bot_name,
            self.behavior
        )
        
        # Find content/knowledge_graph folder (handles numbered prefixes)
        kg_dir = find_nested_subfolder(behavior_folder, 'content', 'knowledge_graph')
        
        if not kg_dir:
            raise FileNotFoundError(
                f'Knowledge graph folder not found under {behavior_folder}'
            )
        
        # Find config files (e.g., build_story_graph_outline.json)
        config_files = list(kg_dir.glob('*.json'))
        if not config_files:
            raise FileNotFoundError(
                f'Knowledge graph config not found in {kg_dir}'
            )
        
        # Load the first config file to get template reference
        config_path = config_files[0]
        with open(config_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
        
        # Get the template filename from config
        template_filename = config_data.get('template')
        if not template_filename:
            raise ValueError(
                f'No template specified in {config_path}'
            )
        
        # Load the actual template file
        template_path = kg_dir / template_filename
        if not template_path.exists():
            raise FileNotFoundError(
                f'Template file not found: {template_path}'
            )
        
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = json.load(f)
        
        # Check if output file exists and add update instructions
        output_path = config_data.get('path', 'docs/stories')
        output_filename = config_data.get('output', 'story-graph.json')
        existing_file_info = self._check_existing_output_file(output_path, output_filename)
        
        result = {
            'knowledge_graph_template': template_content,
            'knowledge_graph_config': config_data,
            'template_path': str(template_path),
            'config_path': str(config_path)
        }
        
        # Add existing file information if file exists
        if existing_file_info:
            result['existing_file'] = existing_file_info
            result['update_mode'] = True
        
        return result
    
    def _check_existing_output_file(self, output_path: str, output_filename: str) -> Dict[str, Any]:
        """
        Check if the output file already exists and return information about it.
        
        Args:
            output_path: Relative path from project root (e.g., 'docs/stories')
            output_filename: Output filename (e.g., 'story-graph.json')
            
        Returns:
            Dict with existing file info if file exists, None otherwise
        """
        import os
        working_area = os.environ.get('WORKING_AREA')
        if not working_area:
            return None
        
        project_root = Path(working_area)
        output_file_path = project_root / output_path / output_filename
        
        if output_file_path.exists():
            try:
                with open(output_file_path, 'r', encoding='utf-8') as f:
                    existing_content = json.load(f)
                
                return {
                    'path': str(output_file_path),
                    'exists': True,
                    'has_epics': 'epics' in existing_content,
                    'has_increments': 'increments' in existing_content,
                    'has_domain_concepts': any(
                        'domain_concepts' in epic for epic in existing_content.get('epics', [])
                    ),
                    'structure_summary': {
                        'epic_count': len(existing_content.get('epics', [])),
                        'has_increments': 'increments' in existing_content
                    }
                }
            except (json.JSONDecodeError, IOError):
                # File exists but can't be read - return basic info
                return {
                    'path': str(output_file_path),
                    'exists': True,
                    'readable': False
                }
        
        return None

    def inject_validation_rules(self) -> Dict[str, Any]:
        """
        Load validation rules by delegating to ValidateRulesAction to avoid code duplication.
        Rules are injected into the LLM prompt so it can follow them during generation.
        """
        from agile_bot.bots.base_bot.src.bot.validate_rules_action import ValidateRulesAction
        
        # Create ValidateRulesAction instance to reuse its rule-loading logic
        validate_action = ValidateRulesAction(
            bot_name=self.bot_name,
            behavior=self.behavior,
            bot_directory=self.bot_directory
        )
        
        # Use existing method to load both common and behavior-specific rules
        rules_data = validate_action.inject_behavior_specific_and_bot_rules()
        
        # Return the validation_rules portion
        return rules_data.get('validation_rules', [])
    
    def _estimate_tokens(self, instructions: Dict[str, Any]) -> int:
        """
        Estimate token count for the full instructions payload.
        Uses rough approximation: word count * 1.3
        """
        total_chars = len(json.dumps(instructions, indent=2))
        # Approximate: 1 token ~= 4 characters for JSON
        estimated_tokens = total_chars // 4
        return estimated_tokens



