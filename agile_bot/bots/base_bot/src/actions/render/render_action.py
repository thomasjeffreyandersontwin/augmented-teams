from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import importlib
import logging
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.render.render_spec import RenderSpec
from agile_bot.bots.base_bot.src.actions.render.render_config_loader import RenderConfigLoader
from agile_bot.bots.base_bot.src.actions.render.render_instruction_formatter import RenderInstructionFormatter
from agile_bot.bots.base_bot.src.bot.merged_instructions import MergedInstructions

logger = logging.getLogger(__name__)


class RenderOutputAction(Action):
    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        
        # Initialize helper classes
        self._config_loader = RenderConfigLoader(self.behavior)
        self._instruction_formatter = RenderInstructionFormatter()
        
        # Load render specs from behavior folder
        self._render_specs: List[RenderSpec] = self._config_loader.load_render_specs()
    
    @property
    def action_name(self) -> str:
        """Action name is always 'render' for RenderOutputAction."""
        return 'render'
    
    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError("action_name is read-only for RenderOutputAction")
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        # Load render-specific data (render_instructions and render_configs)
        render_instructions = self._config_loader.load_render_instructions()
        render_configs = self._config_loader.load_render_configs()
        
        # Execute synchronizers automatically
        executed_configs = []
        template_configs = []
        
        for render_config in render_configs:
            config = render_config.get('config', {})
            
            if 'synchronizer' in config:
                # Execute synchronizer automatically
                try:
                    result = self._execute_synchronizer(render_config)
                    executed_configs.append({
                        'config': render_config,
                        'result': result,
                        'status': 'executed'
                    })
                    logger.info(f"Executed synchronizer for {config.get('name', 'unknown')}: {result.get('output_path', 'N/A')}")
                except Exception as e:
                    logger.error(f"Failed to execute synchronizer for {config.get('name', 'unknown')}: {e}")
                    executed_configs.append({
                        'config': render_config,
                        'error': str(e),
                        'status': 'failed'
                    })
            else:
                # Template-based config - include in instructions for AI to handle
                template_configs.append(render_config)
        
        # Use MergedInstructions to merge base and render instructions
        merged_instructions = MergedInstructions(
            base_instructions=self.instructions.get('base_instructions', []),
            render_instructions=render_instructions
        )
        instructions = merged_instructions.merge()
        
        # Inject render-specific data into instructions
        # Pass executed_configs so AI knows what was already done
        self._instruction_formatter.inject_render_data(
            instructions, 
            render_instructions, 
            template_configs, 
            executed_configs,
            self.working_dir,
            self.behavior.bot_paths.bot_directory
        )
        
        # Add execution results to return data
        return {
            'instructions': instructions,
            'executed_configs': executed_configs,
            'template_configs': template_configs
        }
    
    @property
    def render_specs(self) -> List[RenderSpec]:
        return self._render_specs
    
    @property
    def templates(self) -> List:
        templates = []
        for spec in self._render_specs:
            if spec.template:
                templates.append(spec.template)
        return templates
    
    @property
    def synchronizers(self) -> List:
        synchronizers = []
        for spec in self._render_specs:
            if spec.synchronizer:
                synchronizers.append(spec.synchronizer)
        return synchronizers
    
    def _execute_synchronizer(self, render_config: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a synchronizer from render config."""
        config = render_config.get('config', {})
        synchronizer_path = config.get('synchronizer')
        
        if not synchronizer_path:
            raise ValueError("No synchronizer specified in config")
        
        # Import synchronizer class dynamically
        synchronizer_class = self._import_synchronizer_class(synchronizer_path)
        
        # Instantiate synchronizer
        synchronizer_instance = synchronizer_class()
        
        # Resolve input and output paths
        workspace_dir = self.working_dir
        input_file = config.get('input', 'story-graph.json')
        output_file = config.get('output', 'output.md')
        config_path = config.get('path', 'docs/stories')
        
        # Resolve input path (relative to workspace)
        input_path = workspace_dir / config_path / input_file
        if not input_path.exists():
            # Try docs/stories as fallback
            input_path = workspace_dir / 'docs' / 'stories' / input_file
        
        # Resolve output path (relative to workspace)
        # Handle template variables in output filename
        output_file_resolved = output_file
        if '{solution_name_slug}' in output_file:
            # Try to get solution name from story-graph.json if it exists
            try:
                if input_path.exists():
                    story_graph_data = read_json_file(input_path)
                    solution_name = story_graph_data.get('solution_name', 'solution')
                    solution_name_slug = solution_name.lower().replace(' ', '-')
                    output_file_resolved = output_file.replace('{solution_name_slug}', solution_name_slug)
            except Exception:
                # If we can't resolve, use a default
                output_file_resolved = output_file.replace('{solution_name_slug}', 'solution')
        
        output_path = workspace_dir / config_path / output_file_resolved
        
        # Prepare kwargs from config
        kwargs = {}
        if 'renderer_command' in config:
            kwargs['renderer_command'] = config['renderer_command']
        if 'force_outline' in config:
            kwargs['force_outline'] = config['force_outline']
        
        # Add project_path for domain model synchronizers
        kwargs['project_path'] = str(workspace_dir)
        
        # Execute synchronizer
        result = synchronizer_instance.render(
            str(input_path),
            str(output_path),
            **kwargs
        )
        
        return result
    
    def _import_synchronizer_class(self, synchronizer_class_path: str):
        """Import synchronizer class dynamically."""
        module_path, class_name = synchronizer_class_path.rsplit('.', 1)
        
        possible_paths = [
            module_path,
            f'agile_bot.bots.{self.behavior.bot_name}.src.{module_path}',
            f'agile_bot.bots.{self.behavior.bot_name}.src.synchronizers.{module_path}',
        ]
        
        module = None
        for path in possible_paths:
            try:
                module = importlib.import_module(path)
                if hasattr(module, class_name):
                    break
                module = None
            except ImportError:
                continue
        
        if module is None:
            raise ImportError(f"Could not import synchronizer module: {synchronizer_class_path}")
        
        synchronizer_class = getattr(module, class_name)
        
        if not hasattr(synchronizer_class, 'render'):
            raise ValueError(f"Synchronizer class {synchronizer_class_path} does not have render method")
        
        return synchronizer_class
    
    def inject_next_action_instructions(self):
        return "Proceed to validate action"
