from pathlib import Path
from typing import Dict, Any, List, TYPE_CHECKING
if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.actions.render.render_spec import RenderSpec

class RenderInstructionFormatter:

    def inject_render_data(self, instructions: Dict[str, Any], render_instructions: Dict[str, Any], render_specs: List['RenderSpec']) -> None:
        base_instructions_list = instructions.get('base_instructions', []).copy()
        working_dir = self._inject_workspace_info(base_instructions_list, render_specs)
        executed_specs = [spec for spec in render_specs if spec.is_executed]
        template_specs = [spec for spec in render_specs if spec.requires_ai_handling and (not spec.is_executed)]
        self._add_spec_instructions(base_instructions_list, executed_specs, template_specs)
        self.inject_render_template_variables(base_instructions_list, render_instructions, template_specs)
        self._update_instructions_dict(instructions, base_instructions_list, render_instructions, template_specs, executed_specs, render_specs, working_dir)

    def _inject_workspace_info(self, base_instructions_list: List[str], render_specs: List['RenderSpec']) -> Path:
        if not render_specs:
            return None
        bot_paths = render_specs[0]._bot_paths
        working_dir = bot_paths.workspace_directory
        if working_dir != bot_paths.bot_directory:
            workspace_info = f"\n**WORKSPACE PATH: {working_dir}**\nAll render outputs must be written to paths relative to this workspace path, NOT to the bot's own directories."
            base_instructions_list.insert(0, workspace_info)
        return working_dir

    def _add_spec_instructions(self, base_instructions_list: List[str], executed_specs: List['RenderSpec'], template_specs: List['RenderSpec']) -> None:
        if executed_specs:
            base_instructions_list.insert(1, self.format_executed_synchronizers(executed_specs))
        if template_specs:
            base_instructions_list.append(self.format_template_instructions(template_specs))

    def _update_instructions_dict(self, instructions: Dict[str, Any], base_instructions_list: List[str], render_instructions: Dict[str, Any], template_specs: List['RenderSpec'], executed_specs: List['RenderSpec'], render_specs: List['RenderSpec'], working_dir: Path) -> None:
        instructions['base_instructions'] = base_instructions_list
        instructions['render_instructions'] = render_instructions
        instructions['render_configs'] = [spec.config_data for spec in template_specs]
        instructions['executed_configs'] = [spec.config_data for spec in executed_specs]
        if render_specs and working_dir and (working_dir != render_specs[0]._bot_paths.bot_directory):
            instructions['workspace_path'] = str(working_dir)

    def inject_render_template_variables(self, instructions_list: List[str], render_instructions: Dict[str, Any], render_specs: List['RenderSpec']) -> None:
        render_instructions_text = '\n'.join(render_instructions.get('instructions', []))
        render_configs_text = self.format_render_configs(render_specs)
        new_instructions = []
        for line in instructions_list:
            if '{{render_instructions}}' in line:
                instructions_lines = render_instructions_text.split('\n')
                new_instructions.extend(instructions_lines)
            elif '{{render_configs}}' in line:
                configs_lines = render_configs_text.split('\n')
                new_instructions.extend(configs_lines)
            else:
                new_instructions.append(line)
        instructions_list[:] = new_instructions

    def format_render_configs(self, render_specs: List['RenderSpec']) -> str:
        formatted_parts = ['**Render Configurations:**', '']
        for i, spec in enumerate(render_specs, 1):
            self._format_single_spec(spec, i, formatted_parts)
        return '\n'.join(formatted_parts)

    def _format_single_spec(self, spec: 'RenderSpec', index: int, formatted_parts: list):
        config_name = spec.name
        config_file = spec.config_data.get('file', 'unknown')
        formatted_parts.append(f'{index}. **{config_name}** ({config_file})')
        self.format_instructions(spec.config_data, formatted_parts)
        self._format_execution_method(spec, formatted_parts)
        self._format_config_fields(spec, formatted_parts)
        formatted_parts.append('')

    def _format_execution_method(self, spec: 'RenderSpec', formatted_parts: list):
        if spec.synchronizer:
            synchronizer = spec.synchronizer.synchronizer_class_path
            formatted_parts.append(f'   - Synchronizer: {synchronizer}')
            if 'renderer_command' in spec.config_data:
                renderer_cmd = spec.config_data.get('renderer_command', 'N/A')
                formatted_parts.append(f'   - Renderer Command: {renderer_cmd}')
        elif spec.template:
            template = spec.config_data.get('template', 'N/A')
            formatted_parts.append(f'   - Template: {template}')

    def _format_config_fields(self, spec: 'RenderSpec', formatted_parts: list):
        if spec.input:
            formatted_parts.append(f'   - Input: {spec.input}')
        if spec.output:
            formatted_parts.append(f'   - Output: {spec.output}')
        if 'path' in spec.config_data:
            formatted_parts.append(f"   - Path: {spec.config_data.get('path', 'N/A')}")

    def format_instructions(self, config: Dict[str, Any], parts: list, indent: str='   ') -> None:
        if 'instructions' not in config:
            return
        instructions = config.get('instructions', '')
        if isinstance(instructions, str):
            parts.append(f'{indent}- Instructions: {instructions}')
        elif isinstance(instructions, list):
            parts.append(f'{indent}- Instructions:')
            for inst in instructions:
                parts.append(f'{indent}  * {inst}')

    def format_executed_synchronizers(self, executed_specs: List['RenderSpec']) -> str:
        parts = ['**Synchronizers Already Executed:**', '', 'The following render configurations have been automatically executed via synchronizers:', '']
        for i, spec in enumerate(executed_specs, 1):
            self._format_executed_spec(spec, i, parts)
        parts.extend(['These outputs have been generated and do not require further action.', ''])
        return '\n'.join(parts)

    def _format_executed_spec(self, spec: 'RenderSpec', index: int, parts: list) -> None:
        if spec.execution_status == 'executed':
            result = spec.execution_result
            output_path = result.get('output_path', 'N/A') if result else 'N/A'
            parts.append(f'{index}. **{spec.name}** - EXECUTED')
            parts.append(f'   - Output generated at: {output_path}')
            if spec.synchronizer:
                parts.append(f'   - Synchronizer: {spec.synchronizer.synchronizer_class_path}')
        else:
            error = spec.execution_result.get('error', 'Unknown error') if spec.execution_result else 'Unknown error'
            parts.append(f'{index}. **{spec.name}** - FAILED')
            parts.append(f'   - Error: {error}')
        parts.append('')

    def format_template_instructions(self, template_specs: List['RenderSpec']) -> str:
        parts = ['**Template-Based Render Configurations Requiring AI Handling:**', '', 'The following render configurations use templates and require AI assistance to generate outputs:', '']
        self._format_template_specs_list(template_specs, parts)
        parts.extend(self._get_synchronizer_instructions())
        return '\n'.join(parts)

    def _format_template_specs_list(self, template_specs: List['RenderSpec'], parts: list):
        for i, spec in enumerate(template_specs, 1):
            config_name = spec.name
            config_file = spec.config_data.get('file', 'unknown')
            parts.append(f'{i}. **{config_name}** ({config_file})')
            self.format_instructions(spec.config_data, parts)
            if spec.template:
                template = spec.config_data.get('template', 'N/A')
                parts.append(f'   - Template: {template}')
            self._format_config_fields(spec, parts)
            parts.append('')

    def _get_synchronizer_instructions(self):
        return ['**IMPORTANT:** If you need to create code to execute a template or generate output programmatically,', 'you should create a new synchronizer class instead. Follow these steps:', '', '1. Create a new synchronizer class in the appropriate synchronizers directory', '   (e.g., `agile_bot/bots/{bot_name}/src/synchronizers/{synchronizer_type}/`)', "   where {synchronizer_type} can be an artifact type like 'domain' or a behavior name like 'shape'", '2. Implement the synchronizer with a `render()` method that takes input_path, output_path, and kwargs', "3. Update the render spec JSON file to use `type: 'synchronizer'` and reference the new synchronizer class", '4. Ask the human for approval before creating the synchronizer', '', 'This ensures consistency and reusability across render configurations.', '']