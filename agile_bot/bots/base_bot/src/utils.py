"""
Base Bot Utilities

Common utility functions for bot operations.
"""
from pathlib import Path
import json
from typing import Dict, Any


def read_json_file(file_path: Path) -> Dict[str, Any]:
    """Read JSON file with UTF-8 encoding.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        Parsed JSON data as dictionary
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If JSON is malformed
    """
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return json.loads(file_path.read_text(encoding='utf-8'))


def update_memory(action: str, title: str = None, knowledge_to_store: str = None, existing_knowledge_id: str = None) -> Dict[str, Any]:
    """Stub for update_memory API - replaced by Cursor tool in production.
    
    This is a placeholder that gets patched in tests. In production, this would
    call the actual Cursor update_memory tool.
    
    Args:
        action: Action to perform ('create', 'update', 'delete')
        title: Title of the memory
        knowledge_to_store: Content to store
        existing_knowledge_id: ID of existing memory (for update/delete)
        
    Returns:
        Dictionary with status and id
    """
    # This is a stub - in production this calls Cursor's API
    # Tests will mock this function
    return {'status': 'created', 'id': 'stub-memory-id'}


def find_behavior_folder(workspace_root: Path, bot_name: str, behavior_name: str) -> Path:
    """Find behavior folder handling numbered prefixes.
    
    Behavior folders may have number prefixes (1_shape, 2_prioritization)
    but behavior names in config don't have numbers (shape, prioritization).
    
    Args:
        workspace_root: Root workspace directory
        bot_name: Name of the bot
        behavior_name: Behavior name without number prefix
        
    Returns:
        Path to behavior folder
        
    Raises:
        FileNotFoundError: If behavior folder not found
    """
    behaviors_dir = workspace_root / 'agile_bot' / 'bots' / bot_name / 'behaviors'
    
    # Try to find folder with or without number prefix
    for folder in behaviors_dir.glob(f'*{behavior_name}'):
        if folder.is_dir():
            return folder
    
    # Fall back to exact name
    behavior_folder = behaviors_dir / behavior_name
    if behavior_folder.exists():
        return behavior_folder
    
    raise FileNotFoundError(
        f'Behavior folder not found for {behavior_name} in {behaviors_dir}'
    )


