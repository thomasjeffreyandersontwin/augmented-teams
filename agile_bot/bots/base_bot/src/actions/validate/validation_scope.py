from pathlib import Path
from typing import Dict, Any, List, Optional
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths


class ValidationScope:
    def __init__(self, parameters: Dict[str, Any], bot_paths: Optional[BotPaths] = None, behavior_name: Optional[str] = None):
        self._parameters = parameters or {}
        self._bot_paths = bot_paths
        self._behavior_name = behavior_name
        self._scope_config: Dict[str, Any] = {}
        self._repo_root: Optional[Path] = None
        self._build_scope()
        if self._bot_paths:
            self._repo_root = self._find_repo_root()
    
    def _behavior_to_directory(self, behavior_name: Optional[str]) -> Optional[str]:
        """Map behavior name to directory name.
        
        - 'code' → 'src'
        - 'tests' → 'test'
        - Other behaviors → use behavior name as directory name
        """
        if not behavior_name:
            return None
        if behavior_name == 'code':
            return 'src'
        return behavior_name
    
    def _build_scope(self):
        path_params = {'test', 'src'}
        
        for key, value in self._parameters.items():
            if value is None:
                continue
            
            if key in path_params:
                if not isinstance(value, list):
                    value = [value]
                
                self._scope_config[key] = [
                    str(Path(p)).replace('\\', '/') for p in value
                ]
            elif key == 'validate_all' and value is True:
                self._scope_config['all'] = True
            else:
                self._scope_config[key] = value
    
    @property
    def scope(self) -> Dict[str, Any]:
        return self._scope_config
    
    def files(self, key: str) -> List[Path]:
        files_list = self._scope_config.get(key, [])
        
        # CRITICAL: Only auto-discover if NO explicit parameters were provided at all
        # Check if ANY path parameters (src, test) were explicitly provided
        has_any_explicit_params = any(
            key in self._scope_config 
            for key in ['src', 'test']
        )
        
        # Only auto-discover if no explicit files for this key AND no explicit params at all
        if not files_list and not has_any_explicit_params and self._bot_paths:
            files_list = self._auto_discover_files(key)
            if files_list:
                self._scope_config[key] = files_list
        
        resolved_paths = []
        for file_path_str in files_list:
            file_path = Path(file_path_str)
            
            # Resolve relative paths - ALWAYS use workspace_directory for explicit paths
            # This ensures paths like "agile_bot/bots/base_bot/src" resolve correctly
            # regardless of which bot is running the validation
            if not file_path.is_absolute():
                # Try repo_root first if available (most accurate)
                if self._repo_root:
                    candidate_path = self._repo_root / file_path
                    if candidate_path.exists():
                        file_path = candidate_path
                    elif self._bot_paths and self._bot_paths.workspace_directory:
                        # Fallback to workspace_directory (should be repo root)
                        file_path = self._bot_paths.workspace_directory / file_path
                elif self._bot_paths and self._bot_paths.workspace_directory:
                    file_path = self._bot_paths.workspace_directory / file_path
                else:
                    # Last resort: try current working directory
                    import os
                    file_path = Path(os.getcwd()) / file_path
            
            # If path is a directory, expand it to include all matching files
            # CRITICAL: Only scan files within this specific directory tree
            if file_path.exists() and file_path.is_dir():
                # Resolve to absolute path to ensure correct comparison
                abs_dir_path = file_path.resolve()
                # Normalize path separators for comparison (Windows vs Unix)
                abs_dir_str = str(abs_dir_path).replace('\\', '/')
                
                # Find all .py files recursively, but ONLY within this directory
                all_py_files = list(file_path.rglob('*.py'))
                # Filter to ensure files are actually within the directory (not parent directories)
                # Check that the file's absolute path starts with the directory's absolute path
                for f in all_py_files:
                    f_abs_str = str(f.resolve()).replace('\\', '/')
                    # Ensure the file path starts with the directory path + separator
                    # This prevents matching parent directories
                    if f_abs_str.startswith(abs_dir_str + '/') or f_abs_str == abs_dir_str:
                        resolved_paths.append(f)
            elif file_path.exists() and file_path.is_file():
                # It's a file, add it directly
                resolved_paths.append(file_path)
            else:
                # Path doesn't exist, but add it anyway (might be created later or error will be caught)
                resolved_paths.append(file_path)
        
        return resolved_paths
    
    def all_files(self) -> Dict[str, List[Path]]:
        all_files_dict = {}
        
        # If behavior name is provided, only discover files from that behavior's directory
        if self._behavior_name:
            behavior_dir = self._behavior_to_directory(self._behavior_name)
            if behavior_dir:
                # Map behavior name to scanner key
                # 'tests' or 'test' behavior → 'test' key
                # 'code' behavior → 'src' key
                # Other behaviors → 'src' key (scanners expect 'test' or 'src')
                if self._behavior_name in ('tests', 'test'):
                    file_key = 'test'
                elif self._behavior_name == 'code':
                    file_key = 'src'
                else:
                    # For other behavior directories, use 'src' key
                    file_key = 'src'
                
                # Check if explicit files were provided for this key or directory
                # Also check if ANY path parameters were provided (src, test)
                has_explicit_files = file_key in self._scope_config or behavior_dir in self._scope_config
                has_any_explicit_params = any(
                    key in self._scope_config 
                    for key in ['src', 'test']
                )
                
                # CRITICAL: Only auto-discover if NO explicit parameters were provided
                if not has_explicit_files and not has_any_explicit_params:
                    # Auto-discover files from behavior's directory (current bot only)
                    files = self._discover_files_from_directory(behavior_dir)
                    if files:
                        all_files_dict[file_key] = files
                elif has_explicit_files or has_any_explicit_params:
                    # Use explicitly provided files ONLY - no auto-discovery
                    if file_key in self._scope_config:
                        files = self.files(file_key)
                    elif behavior_dir in self._scope_config:
                        files = self.files(behavior_dir)
                    else:
                        # Explicit params provided but not for this key - return empty
                        files = []
                    if files:
                        all_files_dict[file_key] = files
            return all_files_dict
        
        # If no behavior name, discover both test and src files (backward compatibility)
        # But only if no explicit parameters were provided
        has_any_explicit_params = any(
            key in self._scope_config 
            for key in ['src', 'test']
        )
        
        if not has_any_explicit_params:
            # No explicit params - auto-discover from current bot's directories
            file_keys = {'test', 'src'}
            for key in file_keys:
                files = self.files(key)
                if files:
                    all_files_dict[key] = files
        else:
            # Explicit params provided - use ONLY those
            file_keys = {'test', 'src'}
            for key in file_keys:
                if key in self._scope_config:
                    files = self.files(key)
                    if files:
                        all_files_dict[key] = files
        
        return all_files_dict
    
    def _discover_files_from_directory(self, dir_name: str) -> List[Path]:
        """Discover files from a specific directory based on behavior.
        
        CRITICAL: Uses workspace_directory (the project being worked on), not bot_directory
        (the bot running the CLI). This ensures auto-discovery scans the correct project.
        
        For 'code' behavior, looks in workspace_directory/src (e.g., agile_bot/bots/base_bot/src)
        For 'tests' behavior, looks in workspace_directory/test (e.g., agile_bot/bots/base_bot/test)
        """
        if not self._bot_paths:
            return []
        
        # Use workspace_directory (the project being worked on), not bot_directory (the bot running CLI)
        # This ensures we scan the correct project's src folder, not the bot's src folder
        workspace_directory = self._bot_paths.workspace_directory
        search_dir = workspace_directory / dir_name
        
        if not search_dir.exists():
            return []
        
        discovered_files = []
        
        # Find all .py files recursively, but ONLY within this directory tree
        abs_dir_path = search_dir.resolve()
        abs_dir_str = str(abs_dir_path).replace('\\', '/')
        
        all_py_files = list(search_dir.rglob('*.py'))
        # Filter to ensure files are actually within the directory
        for f in all_py_files:
            f_abs_str = str(f.resolve()).replace('\\', '/')
            if f_abs_str.startswith(abs_dir_str + '/') or f_abs_str == abs_dir_str:
                discovered_files.append(f)
        
        return discovered_files
    
    def _find_repo_root(self) -> Optional[Path]:
        if not self._bot_paths:
            return None
        
        workspace_path = self._bot_paths.workspace_directory
        current = workspace_path.resolve()
        
        for i in range(10):
            if (current / '.git').exists() or (current / 'agile_bot').exists():
                return current
            if current.parent == current:
                break
            current = current.parent
        
        workspace_str = str(workspace_path.resolve())
        if 'demo' in workspace_str:
            parts = workspace_path.resolve().parts
            if 'demo' in parts:
                demo_idx = parts.index('demo')
                return Path(*parts[:demo_idx]) if demo_idx > 0 else workspace_path.resolve().parent
            else:
                return workspace_path.resolve().parent
        else:
            return workspace_path.resolve().parent
    
    def _auto_discover_files(self, key: str) -> List[str]:
        """Auto-discover files for a given key (test, src, or behavior name)."""
        if not self._bot_paths:
            return []
        
        # Map key to directory name
        # If behavior name exists, use behavior directory mapping
        # Otherwise, key is the directory name
        if self._behavior_name:
            behavior_dir = self._behavior_to_directory(self._behavior_name)
            dir_name = behavior_dir if behavior_dir else key
        else:
            dir_name = key
        
        workspace_directory = self._bot_paths.workspace_directory
        search_dir = workspace_directory / dir_name
        
        if not search_dir.exists():
            return []
        
        discovered_files = []
        
        # Find all .py files recursively
        discovered_files.extend(search_dir.rglob('*.py'))
        
        return [str(f) for f in discovered_files]
