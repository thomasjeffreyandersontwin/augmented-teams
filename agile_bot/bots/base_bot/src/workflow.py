"""
Workflow

Manages behavior workflow execution.
"""
from pathlib import Path
import json


class Workflow:
    """Workflow manager for behavior execution."""
    
    def __init__(self, workspace_root: Path):
        self.workspace_root = Path(workspace_root)
    
    def is_terminal_action(self, action_name: str) -> bool:
        """Check if action is terminal (last) action."""
        return action_name == 'validate_rules'
    
    def is_behavior_complete(self, behavior: str, state_file: Path) -> bool:
        """Check if behavior workflow is complete."""
        if not state_file.exists():
            return False
        
        state = json.loads(state_file.read_text(encoding='utf-8'))
        completed = state.get('completed_actions', [])
        
        # Check if validate_rules is in completed actions for this behavior
        return any(
            f'.{behavior}.validate_rules' in action['action_state']
            for action in completed
        )

