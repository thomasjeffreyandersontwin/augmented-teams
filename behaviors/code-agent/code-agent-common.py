"""Common utilities for code-agent runners.

This module provides shared functions used across all code-agent runners
to dynamically discover behavior directories without hardcoded paths.
"""

from pathlib import Path
import json
from typing import List, Dict, Optional


def find_deployed_behaviors(root: Optional[Path] = None) -> List[Path]:
    """
    Dynamically find all directories containing behavior.json with deployed=true.
    
    Args:
        root: Root directory to search from. Defaults to 'behaviors' in current directory.
        
    Returns:
        List of Path objects pointing to directories with deployed behaviors.
        
    Example:
        >>> dirs = find_deployed_behaviors()
        >>> for dir in dirs:
        ...     print(f"Watching: {dir}")
    """
    if root is None:
        root = Path("behaviors")
    
    if not root.exists():
        return []
    
    deployed_dirs = []
    
    for behavior_json in root.glob("**/behavior.json"):
        try:
            with open(behavior_json, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if config.get("deployed") == True:
                    # Return the parent directory of behavior.json
                    deployed_dirs.append(behavior_json.parent)
        except Exception:
            # Skip files that can't be read or parsed
            pass
    
    return deployed_dirs


def find_all_behavior_jsons(root: Optional[Path] = None) -> List[Dict[str, any]]:
    """
    Find all behavior.json files and return their configurations.
    
    Args:
        root: Root directory to search from. Defaults to 'behaviors' in current directory.
        
    Returns:
        List of dicts containing 'path' (Path to behavior.json parent dir) and 'config' (parsed JSON).
        
    Example:
        >>> behaviors = find_all_behavior_jsons()
        >>> for behavior in behaviors:
        ...     if behavior['config'].get('deployed'):
        ...         print(f"Deployed: {behavior['path']}")
    """
    if root is None:
        root = Path("behaviors")
    
    if not root.exists():
        return []
    
    behaviors = []
    
    for behavior_json in root.glob("**/behavior.json"):
        try:
            with open(behavior_json, 'r', encoding='utf-8') as f:
                config = json.load(f)
                behaviors.append({
                    'path': behavior_json.parent,
                    'config': config,
                    'json_path': behavior_json
                })
        except Exception:
            # Skip files that can't be read or parsed
            pass
    
    return behaviors


def get_behavior_feature_name(behavior_dir: Path) -> Optional[str]:
    """
    Extract feature name from a behavior directory.
    
    Args:
        behavior_dir: Path to behavior directory (containing behavior.json).
        
    Returns:
        Feature name string, or None if not found.
        
    Example:
        >>> name = get_behavior_feature_name(Path("behaviors/bdd"))
        >>> print(name)  # "bdd"
    """
    try:
        behavior_json = behavior_dir / "behavior.json"
        if behavior_json.exists():
            with open(behavior_json, 'r', encoding='utf-8') as f:
                config = json.load(f)
                return config.get("feature", behavior_dir.name)
    except Exception:
        pass
    
    # Fallback to directory name
    return behavior_dir.name
