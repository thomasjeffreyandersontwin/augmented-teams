import os
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.actions.validate.file_discovery import FileDiscovery
from agile_bot.bots.base_bot.src.actions.validate.path_resolver import PathResolver

class ValidationScope:
    EXCLUDED_FILES = {'__init__.py'}

    def __init__(self, parameters: Dict[str, Any], bot_paths: Optional[BotPaths]=None, behavior_name: Optional[str]=None):
        self._parameters = parameters or {}
        self._bot_paths = bot_paths
        self._behavior_name = behavior_name
        self._scope_config: Dict[str, Any] = {}
        exclude_patterns = self._parameters.get('exclude', [])
        if isinstance(exclude_patterns, str):
            exclude_patterns = [exclude_patterns]
        self._file_discovery = FileDiscovery(bot_paths, behavior_name, exclude_patterns)
        self._path_resolver = PathResolver(bot_paths)
        self._build_scope()

    def _should_include_file(self, file_path: Path) -> bool:
        return self._file_discovery.should_include_file(file_path)

    def _expand_directory_to_files(self, dir_path: Path) -> List[Path]:
        return self._file_discovery.expand_directory_to_files(dir_path)

    def _behavior_to_directory(self) -> Optional[str]:
        if not self._behavior_name:
            return None
        if self._behavior_name == 'code':
            return 'src'
        return self._behavior_name

    def _build_scope(self):
        path_params = {'test', 'src'}
        for key, value in self._parameters.items():
            if value is None:
                continue
            if key in path_params:
                if not isinstance(value, list):
                    value = [value]
                self._scope_config[key] = [str(Path(p)).replace('\\', '/') for p in value]
            elif key == 'validate_all' and value is True:
                self._scope_config['all'] = True
            else:
                self._scope_config[key] = value

    @property
    def scope(self) -> Dict[str, Any]:
        return self._scope_config

    def files(self, key: str) -> List[Path]:
        files_list = self._auto_discover_if_needed(key, self._scope_config.get(key, []))
        resolved_paths = []
        for file_path_str in files_list:
            resolved_paths.extend(self._expand_path_if_needed(self._resolve_path(Path(file_path_str))))
        return resolved_paths

    def _auto_discover_if_needed(self, key, files_list):
        has_any_explicit_params = any((k in self._scope_config for k in ['src', 'test']))
        if not files_list and (not has_any_explicit_params) and self._bot_paths:
            discovered = self._auto_discover_files(key)
            if discovered:
                self._scope_config[key] = discovered
                return discovered
        return files_list

    def _resolve_path(self, file_path: Path) -> Path:
        return self._path_resolver.resolve_path(file_path)

    def _expand_path_if_needed(self, file_path: Path) -> List[Path]:
        return self._path_resolver.expand_path_if_needed(file_path, self._expand_directory_to_files)

    def all_files(self) -> Dict[str, List[Path]]:
        if self._behavior_name:
            return self._handle_behavior_specific_files({})
        return self._handle_general_file_discovery({})

    def _handle_behavior_specific_files(self, all_files_dict):
        behavior_dir = self._behavior_to_directory()
        if not behavior_dir:
            return all_files_dict
        file_key = self._get_file_key_for_behavior()
        has_explicit_files = file_key in self._scope_config or behavior_dir in self._scope_config
        has_any_explicit_params = any((k in self._scope_config for k in ['src', 'test']))
        if not has_explicit_files and (not has_any_explicit_params):
            files = self._discover_files_from_directory(behavior_dir)
            if files:
                all_files_dict[file_key] = files
        elif has_explicit_files or has_any_explicit_params:
            files = self._get_explicit_files_for_behavior(file_key, behavior_dir)
            if files:
                all_files_dict[file_key] = files
        return all_files_dict

    def _get_file_key_for_behavior(self):
        if self._behavior_name in ('tests', 'test'):
            return 'test'
        elif self._behavior_name == 'code':
            return 'src'
        else:
            return 'src'

    def _get_explicit_files_for_behavior(self, file_key, behavior_dir):
        if file_key in self._scope_config:
            return self.files(file_key)
        elif behavior_dir in self._scope_config:
            return self.files(behavior_dir)
        else:
            return []

    def _handle_general_file_discovery(self, all_files_dict):
        has_any_explicit_params = any((k in self._scope_config for k in ['src', 'test']))
        file_keys = {'test', 'src'}
        if not has_any_explicit_params:
            self._discover_all_file_keys(file_keys, all_files_dict)
        else:
            self._discover_explicit_file_keys(file_keys, all_files_dict)
        return all_files_dict

    def _discover_all_file_keys(self, file_keys, all_files_dict):
        for key in file_keys:
            files = self.files(key)
            if files:
                all_files_dict[key] = files

    def _discover_explicit_file_keys(self, file_keys, all_files_dict):
        for key in file_keys:
            if key in self._scope_config:
                files = self.files(key)
                if files:
                    all_files_dict[key] = files

    def _discover_files_from_directory(self, dir_name: str) -> List[Path]:
        return self._file_discovery.discover_files_from_directory(dir_name)

    def _auto_discover_files(self, key: str) -> List[str]:
        return self._file_discovery.auto_discover_files(key)