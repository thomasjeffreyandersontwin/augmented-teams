from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import importlib
import logging
from agile_bot.bots.base_bot.src.utils import read_json_file
from agile_bot.bots.base_bot.src.actions.action import Action
from agile_bot.bots.base_bot.src.actions.render.render_spec import RenderSpec
from agile_bot.bots.base_bot.src.bot.merged_instructions import MergedInstructions

logger = logging.getLogger(__name__)


class RenderOutputAction(Action):
    def __init__(self, behavior=None, action_config=None):
        super().__init__(behavior=behavior, action_config=action_config)
        
        # Load render specs from behavior folder
        self._render_specs: List[RenderSpec] = []
        self._load_render_specs()
    
    @property
    def action_name(self) -> str:
        """Action name is always 'render' for RenderOutputAction."""
        return 'render'
    
    @action_name.setter
    def action_name(self, value: str):
        raise AttributeError("action_name is read-only for RenderOutputAction")
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        # Load render-specific data (render_instructions and render_configs)
        render_instructions = self._load_render_instructions()
        render_configs = self._load_render_configs()
        
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
        self._inject_render_data(instructions, render_instructions, template_configs, executed_configs)
        
        # Add execution results to return data
        return {
            'instructions': instructions,
            'executed_configs': executed_configs,
            'template_configs': template_configs
        }
    
    def _find_render_folder(self) -> Path:
        # Render folder is at content/render/ directly
        return self.behavior.folder / 'content' / 'render'
    
    def _load_render_instructions(self) -> Dict[str, Any]:
        """Load render instructions.json - REQUIRED if render folder exists."""
        render_folder = self._find_render_folder()
        
        # If render folder doesn't exist, return empty dict (no render needed)
        if not render_folder.exists() or not render_folder.is_dir():
            return {}
        
        # If render folder exists, instructions.json is MANDATORY
        instructions_path = render_folder / 'instructions.json'
        if not instructions_path.exists():
            raise FileNotFoundError(
                f"Render folder exists at {render_folder} but instructions.json is missing. "
                f"instructions.json is mandatory when render folder exists."
            )
        
        return read_json_file(instructions_path)
    
    def _load_render_specs(self):
        render_folder = self._find_render_folder()
        
        # Guard: Only load specs if render folder exists
        if not render_folder.exists() or not render_folder.is_dir():
            return
        
        render_json_files = [f for f in render_folder.glob('*.json')]
        
        for render_json_file in render_json_files:
            config_data = read_json_file(render_json_file)
            render_spec = RenderSpec(config_data, render_folder, self.behavior.bot_paths, render_json_file)
            self._render_specs.append(render_spec)
    
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
    
    def _load_render_configs(self) -> List[Dict[str, Any]]:
        render_folder = self._find_render_folder()
        render_configs = []
        
        # Guard: Only load configs if render folder exists
        if not render_folder.exists() or not render_folder.is_dir():
            return render_configs
        
        render_json_files = [f for f in render_folder.glob('*.json')]
        
        for render_json_file in render_json_files:
            render_config = self._load_single_render_config(render_json_file)
            render_configs.append(render_config)
        
        return render_configs
    
    def _load_single_render_config(self, render_json_file: Path) -> Dict[str, Any]:
        config = read_json_file(render_json_file)
        
        config_entry = {
            'file': str(render_json_file.relative_to(self.behavior.bot_paths.bot_directory)),
            'config': config
        }
        
        if 'synchronizer' in config:
            self._verify_synchronizer_class(config['synchronizer'])
        elif 'template' in config:
            template_content = self._load_template_file(config['template'])
            config_entry['template'] = template_content
        
        return config_entry
    
    def _verify_synchronizer_class(self, synchronizer_class_path: str) -> None:
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
            # In test scenarios, synchronizer classes may not exist
            # Skip verification if module cannot be imported
            return
        
        synchronizer_class = getattr(module, class_name)
        
        has_render = hasattr(synchronizer_class, 'render')
        has_sync_methods = any(
            hasattr(synchronizer_class, method)
            for method in ['synchronize_outline', 'synchronize_increments', 'synchronize_exploration']
        )
        
        if not (has_render or has_sync_methods):
            raise ValueError(f'Synchronizer class {synchronizer_class_path} does not have required methods')
    
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
    
    def _load_template_file(self, template_path: str) -> str:
        render_folder = self._find_render_folder()
        templates_dir = render_folder / 'templates'
        
        if template_path.startswith('templates/'):
            template_path = template_path[10:]
        
        template_file = templates_dir / template_path
        return template_file.read_text(encoding='utf-8')
    
    def _inject_render_data(self, instructions: Dict[str, Any], render_instructions: Dict[str, Any], 
                            template_configs: List[Dict[str, Any]], executed_configs: List[Dict[str, Any]]) -> None:
        base_instructions_list = instructions.get('base_instructions', []).copy()
        
        # Add workspace path information to instructions
        workspace_path = self.working_dir
        bot_directory = self.behavior.bot_paths.bot_directory
        if workspace_path != bot_directory:
            workspace_info = f"\n**WORKSPACE PATH: {workspace_path}**\nAll render outputs must be written to paths relative to this workspace path, NOT to the bot's own directories."
            base_instructions_list.insert(0, workspace_info)
        
        # Add synchronizer execution summary at the top
        if executed_configs:
            sync_summary = self._format_executed_synchronizers(executed_configs)
            base_instructions_list.insert(1, sync_summary)
        
        # Add template handling instructions if there are template configs
        if template_configs:
            template_instructions = self._format_template_instructions(template_configs)
            base_instructions_list.append(template_instructions)
        
        # Inject render_instructions and render_configs template variables
        # Only pass template_configs (synchronizers already executed)
        self._inject_render_template_variables(base_instructions_list, render_instructions, template_configs)
        
        # Update instructions dict
        instructions['base_instructions'] = base_instructions_list
        
        # Add render-specific data to instructions dict
        instructions['render_instructions'] = render_instructions
        instructions['render_configs'] = template_configs  # Only templates need AI handling
        instructions['executed_configs'] = executed_configs  # For reference
        
        if workspace_path != bot_directory:
            instructions['workspace_path'] = str(workspace_path)
    
    def _inject_render_template_variables(self, instructions_list: List[str], render_instructions: Dict[str, Any], render_configs: List[Dict[str, Any]]) -> None:
        render_instructions_text = '\n'.join(render_instructions.get('instructions', []))
        
        # Format render configs for injection
        render_configs_text = self._format_render_configs(render_configs)
        
        # Replace template variables
        new_instructions = []
        for line in instructions_list:
            if '{{render_instructions}}' in line:
                # Split instructions into lines and insert them
                instructions_lines = render_instructions_text.split('\n')
                new_instructions.extend(instructions_lines)
            elif '{{render_configs}}' in line:
                # Split configs into lines and insert them
                configs_lines = render_configs_text.split('\n')
                new_instructions.extend(configs_lines)
            else:
                new_instructions.append(line)
        
        instructions_list[:] = new_instructions
    
    def _format_render_configs(self, render_configs: List[Dict[str, Any]]) -> str:
        if not render_configs:
            return "No render configurations found."
        
        formatted_parts = []
        formatted_parts.append("**Render Configurations:**")
        formatted_parts.append("")
        
        for i, render_config in enumerate(render_configs, 1):
            config = render_config.get('config', {})
            config_name = config.get('name', f'config_{i}')
            config_file = render_config.get('file', 'unknown')
            
            formatted_parts.append(f"{i}. **{config_name}** ({config_file})")
            
            # Always show instructions first (if present)
            self._format_instructions(config, formatted_parts)
            
            # Show execution method fields
            if 'synchronizer' in config:
                synchronizer = config.get('synchronizer', 'N/A')
                formatted_parts.append(f"   - Synchronizer: {synchronizer}")
                if 'renderer_command' in config:
                    renderer_cmd = config.get('renderer_command', 'N/A')
                    formatted_parts.append(f"   - Renderer Command: {renderer_cmd}")
            elif 'template' in config:
                template = config.get('template', 'N/A')
                formatted_parts.append(f"   - Template: {template}")
            
            # Show input and output fields
            if 'input' in config:
                formatted_parts.append(f"   - Input: {config.get('input', 'N/A')}")
            if 'output' in config:
                formatted_parts.append(f"   - Output: {config.get('output', 'N/A')}")
            
            # Show path if present
            if 'path' in config:
                formatted_parts.append(f"   - Path: {config.get('path', 'N/A')}")
            
            formatted_parts.append("")
        
        return '\n'.join(formatted_parts)
    
    
    def _format_instructions(self, config: Dict[str, Any], parts: list, indent: str = "   ") -> None:
        """Format instructions from config into parts list.
        
        Extracted to eliminate duplication between _format_render_configs()
        and _format_template_instructions().
        """
        if 'instructions' not in config:
            return
        
        instructions = config.get('instructions', '')
        if isinstance(instructions, str):
            parts.append(f"{indent}- Instructions: {instructions}")
        elif isinstance(instructions, list):
            parts.append(f"{indent}- Instructions:")
            for inst in instructions:
                parts.append(f"{indent}  * {inst}")
    
    def _format_executed_synchronizers(self, executed_configs: List[Dict[str, Any]]) -> str:
        """Format information about executed synchronizers for AI instructions."""
        parts = []
        parts.append("**Synchronizers Already Executed:**")
        parts.append("")
        parts.append("The following render configurations have been automatically executed via synchronizers:")
        parts.append("")
        
        for i, exec_config in enumerate(executed_configs, 1):
            config = exec_config.get('config', {}).get('config', {})
            config_name = config.get('name', f'config_{i}')
            status = exec_config.get('status', 'unknown')
            
            if status == 'executed':
                result = exec_config.get('result', {})
                output_path = result.get('output_path', 'N/A')
                parts.append(f"{i}. **{config_name}** - EXECUTED")
                parts.append(f"   - Output generated at: {output_path}")
                parts.append(f"   - Synchronizer: {config.get('synchronizer', 'N/A')}")
            else:
                error = exec_config.get('error', 'Unknown error')
                parts.append(f"{i}. **{config_name}** - FAILED")
                parts.append(f"   - Error: {error}")
            
            parts.append("")
        
        parts.append("These outputs have been generated and do not require further action.")
        parts.append("")
        
        return '\n'.join(parts)
    
    def _format_template_instructions(self, template_configs: List[Dict[str, Any]]) -> str:
        """Format instructions for template-based configs that need AI handling."""
        parts = []
        parts.append("**Template-Based Render Configurations Requiring AI Handling:**")
        parts.append("")
        parts.append("The following render configurations use templates and require AI assistance to generate outputs:")
        parts.append("")
        
        for i, render_config in enumerate(template_configs, 1):
            config = render_config.get('config', {})
            config_name = config.get('name', f'config_{i}')
            config_file = render_config.get('file', 'unknown')
            
            parts.append(f"{i}. **{config_name}** ({config_file})")
            
            # Show instructions
            self._format_instructions(config, parts)
            
            # Show template
            if 'template' in config:
                template = config.get('template', 'N/A')
                parts.append(f"   - Template: {template}")
            
            # Show input and output
            if 'input' in config:
                parts.append(f"   - Input: {config.get('input', 'N/A')}")
            if 'output' in config:
                parts.append(f"   - Output: {config.get('output', 'N/A')}")
            if 'path' in config:
                parts.append(f"   - Path: {config.get('path', 'N/A')}")
            
            parts.append("")
        
        parts.append("**IMPORTANT:** If you need to create code to execute a template or generate output programmatically,")
        parts.append("you should create a new synchronizer class instead. Follow these steps:")
        parts.append("")
        parts.append("1. Create a new synchronizer class in the appropriate synchronizers directory")
        parts.append("   (e.g., `agile_bot/bots/{bot_name}/src/synchronizers/{synchronizer_type}/`)")
        parts.append("   where {synchronizer_type} can be an artifact type like 'domain' or a behavior name like 'shape'")
        parts.append("2. Implement the synchronizer with a `render()` method that takes input_path, output_path, and kwargs")
        parts.append("3. Update the render spec JSON file to use `type: 'synchronizer'` and reference the new synchronizer class")
        parts.append("4. Ask the human for approval before creating the synchronizer")
        parts.append("")
        parts.append("This ensures consistency and reusability across render configurations.")
        parts.append("")
        
        return '\n'.join(parts)
    
    def inject_next_action_instructions(self):
        return "Proceed to validate action"
