"""
Render Test Helper
Handles render action, templates, output generation + render-specific instruction assertions
"""
from .base_helper import BaseHelper


class RenderTestHelper(BaseHelper):
    """Helper for render action and output generation testing"""
    
    def assert_render_output_instructions(self, instructions):
        """Assert RenderOutputAction injected all required fields.
        
        Args:
            instructions: Instructions object from RenderOutputAction
        """
        # Check base instructions exist
        base_instructions = instructions.get('base_instructions', [])
        assert base_instructions, "base_instructions should be present"
        
        # Check RenderOutputAction-specific fields
        # Note: Some fields may be empty lists if no render configs exist
        assert instructions.get('render_instructions') is not None, "render_instructions should be set"
        assert instructions.get('render_configs') is not None, "render_configs should be set"
        assert instructions.get('executed_configs') is not None, "executed_configs should be set"
        assert instructions.get('executed_specs') is not None, "executed_specs should be set"
        assert instructions.get('template_specs') is not None, "template_specs should be set"
    
    def create_render_directory(self, directory_path, **params):
        """Create render output directory structure.
        
        Args:
            directory_path: Path to directory to create (relative to workspace or absolute)
            **params: Additional parameters (for future expansion)
        
        Returns:
            Path to created directory
        """
        from pathlib import Path
        
        # Handle relative vs absolute paths
        if isinstance(directory_path, str):
            directory_path = Path(directory_path)
        
        if not directory_path.is_absolute():
            directory_path = self.parent.workspace / directory_path
        
        directory_path.mkdir(parents=True, exist_ok=True)
        return directory_path
