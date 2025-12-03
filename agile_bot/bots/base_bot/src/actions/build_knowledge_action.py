"""
Build Knowledge Action

Handles build_knowledge action including:
- Injecting knowledge graph templates
"""
from pathlib import Path
import json
from typing import Dict, Any
from agile_bot.bots.base_bot.src.utils import find_behavior_folder

# Note: All file reads in this module use UTF-8 encoding for Windows compatibility


class BuildKnowledgeAction:
    """Build Knowledge action implementation."""
    
    def __init__(self, bot_name: str, behavior: str, workspace_root: Path):
        """Initialize Build Knowledge action.
        
        Args:
            bot_name: Name of the bot
            behavior: Behavior name
            workspace_root: Root workspace directory
        """
        self.bot_name = bot_name
        self.behavior = behavior
        self.workspace_root = Path(workspace_root)
    
    def inject_knowledge_graph_template(self) -> Dict[str, Any]:
        """Inject knowledge graph template path into instructions.
        
        Returns:
            Instructions with template path
            
        Raises:
            FileNotFoundError: If template not found
        """
        # Find behavior folder (handles numbered prefixes)
        behavior_folder = find_behavior_folder(
            self.workspace_root,
            self.bot_name,
            self.behavior
        )
        kg_dir = behavior_folder / 'content' / 'knowledge_graph'
        
        if not kg_dir.exists():
            raise FileNotFoundError(
                f'Knowledge graph template not found at {kg_dir}'
            )
        
        # Find any JSON template in the directory
        templates = list(kg_dir.glob('*.json'))
        if not templates:
            raise FileNotFoundError(
                f'Knowledge graph template not found in {kg_dir}'
            )
        
        template_path = templates[0]
        
        return {
            'knowledge_graph_template': str(template_path)
        }



