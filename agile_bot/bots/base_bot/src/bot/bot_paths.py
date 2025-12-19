from pathlib import Path
import os
import logging
from typing import Dict, Any
from agile_bot.bots.base_bot.src.bot.workspace import get_workspace_directory, get_bot_directory, get_base_actions_directory, get_python_workspace_root
from agile_bot.bots.base_bot.src.utils import read_json_file

class BotPaths:

    def __init__(self, workspace_path: Path=None, bot_directory: Path=None):
        self._workspace_directory = Path(workspace_path) if workspace_path else get_workspace_directory()
        self._bot_directory = Path(bot_directory) if bot_directory else get_bot_directory()
        self._base_actions_directory = get_base_actions_directory()
        self._python_workspace_root = get_python_workspace_root()
        self._documentation_path = self._load_documentation_path()

    def _load_documentation_path(self) -> Path:
        bot_config_path = self._bot_directory / 'config' / 'bot_config.json'
        if bot_config_path.exists():
            try:
                config = read_json_file(bot_config_path)
                docs_path = config.get('docs_path', 'docs/stories')
                return Path(docs_path)
            except Exception as e:
                logging.getLogger(__name__).debug(f'Failed to load documentation path from {bot_config_path}: {e}')
                raise
        return Path('docs/stories')

    @property
    def workspace_directory(self) -> Path:
        return self._workspace_directory

    @property
    def bot_directory(self) -> Path:
        return self._bot_directory

    @property
    def base_actions_directory(self) -> Path:
        return self._base_actions_directory

    @property
    def python_workspace_root(self) -> Path:
        return self._python_workspace_root

    @property
    def documentation_path(self) -> Path:
        return self._documentation_path

    def find_repo_root(self) -> Path:
        return self.python_workspace_root

    def resolve_path_to_absolute(self, path_str: str) -> str:
        path = Path(path_str)
        if path.is_absolute():
            return str(path.resolve())
        absolute_path = path.resolve()
        return str(absolute_path)

    def is_path_like(self, value: str) -> bool:
        return '/' in value or '\\' in value or ('.' in value and any((value.endswith(ext) for ext in ('.py', '.md', '.json', '.txt', '.yaml', '.yml'))))

    def resolve_path_parameters(self, params: Dict[str, Any]) -> Dict[str, Any]:
        resolved = params.copy()
        self._resolve_list_param(resolved, 'src')
        self._resolve_list_param(resolved, 'test')
        self._resolve_exclude_param(resolved)
        self._resolve_list_param(resolved, 'context_files')
        if 'increment_file' in resolved and isinstance(resolved['increment_file'], str):
            resolved['increment_file'] = self.resolve_path_to_absolute(resolved['increment_file'])
        return resolved

    def _resolve_list_param(self, resolved: Dict[str, Any], key: str) -> None:
        if key not in resolved:
            return
        value = resolved[key]
        paths = [value] if isinstance(value, str) else value
        resolved[key] = [self.resolve_path_to_absolute(p) for p in paths]

    def _resolve_exclude_param(self, resolved: Dict[str, Any]) -> None:
        if 'exclude' not in resolved:
            return
        value = resolved['exclude']
        if isinstance(value, str):
            resolved['exclude'] = [self.resolve_path_to_absolute(value) if self.is_path_like(value) else value]
        elif isinstance(value, list):
            resolved['exclude'] = [self.resolve_path_to_absolute(p) if self.is_path_like(p) else p for p in value]