"""Render instruction formatter for RenderOutputAction."""

from pathlib import Path
from typing import Dict, Any, List


class RenderInstructionFormatter:
    """Handles formatting and injecting render data into AI instructions."""
    
    def inject_render_data(self, instructions: Dict[str, Any], render_instructions: Dict[str, Any], 
                          template_configs: List[Dict[str, Any]], executed_configs: List[Dict[str, Any]],
                          working_dir: Path, bot_directory: Path) -> None:
        """Inject render-specific data into instructions dict."""
        base_instructions_list = instructions.get('base_instructions', []).copy()
        
        # Add workspace path information to instructions
        if working_dir != bot_directory:
            workspace_info = f"\n**WORKSPACE PATH: {working_dir}**\nAll render outputs must be written to paths relative to this workspace path, NOT to the bot's own directories."
            base_instructions_list.insert(0, workspace_info)
        
        # Add synchronizer execution summary at the top
        if executed_configs:
            sync_summary = self.format_executed_synchronizers(executed_configs)
            base_instructions_list.insert(1, sync_summary)
        
        # Add template handling instructions if there are template configs
        if template_configs:
            template_instructions = self.format_template_instructions(template_configs)
            base_instructions_list.append(template_instructions)
        
        # Inject render_instructions and render_configs template variables
        # Only pass template_configs (synchronizers already executed)
        self.inject_render_template_variables(base_instructions_list, render_instructions, template_configs)
        
        # Update instructions dict
        instructions['base_instructions'] = base_instructions_list
        
        # Add render-specific data to instructions dict
        instructions['render_instructions'] = render_instructions
        instructions['render_configs'] = template_configs  # Only templates need AI handling
        instructions['executed_configs'] = executed_configs  # For reference
        
        if working_dir != bot_directory:
            instructions['workspace_path'] = str(working_dir)
    
    def inject_render_template_variables(self, instructions_list: List[str], render_instructions: Dict[str, Any], render_configs: List[Dict[str, Any]]) -> None:
        """Inject render template variables into instructions list."""
        render_instructions_text = '\n'.join(render_instructions.get('instructions', []))
        
        # Format render configs for injection
        render_configs_text = self.format_render_configs(render_configs)
        
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
    
    def format_render_configs(self, render_configs: List[Dict[str, Any]]) -> str:
        """Format render configs for display in instructions."""
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
            self.format_instructions(config, formatted_parts)
            
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
    
    def format_instructions(self, config: Dict[str, Any], parts: list, indent: str = "   ") -> None:
        """Format instructions from config into parts list.
        
        Extracted to eliminate duplication between format_render_configs()
        and format_template_instructions().
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
    
    def format_executed_synchronizers(self, executed_configs: List[Dict[str, Any]]) -> str:
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
    
    def format_template_instructions(self, template_configs: List[Dict[str, Any]]) -> str:
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
            self.format_instructions(config, parts)
            
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

