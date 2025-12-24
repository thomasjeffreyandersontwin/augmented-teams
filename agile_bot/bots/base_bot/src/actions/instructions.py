from pathlib import Path
from typing import Any, List, Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths


class Instructions:
    
    def __init__(self, base_instructions: List[str] = None, bot_paths: 'BotPaths' = None):
        self._data = {}
        self._data['base_instructions'] = list(base_instructions) if base_instructions else []
        self._display_content: List[str] = []
        self._bot_paths = bot_paths
    
    def add(self, *lines: str) -> 'Instructions':
        for line in lines:
            self._data['base_instructions'].append(line)
        return self
    
    def add_display(self, *lines: str) -> 'Instructions':
        for line in lines:
            self._display_content.append(line)
        return self
    
    @property
    def display_content(self) -> List[str]:
        return list(self._display_content)
    
    @property
    def context_sources_text(self) -> List[str]:
        """Generate standard 'Where to find context' section with actual paths."""
        if not self._bot_paths:
            # Return placeholder version if bot_paths not available
            return [
                "**Where to find context:**",
                "- Context will be passed in this message (including context sources attached/dropped into the message)",
                "- Additional context in `{project_area}/docs/context/` (original input files, prompts, source material)",
                "- Generated files in `{project_area}/docs/stories/` (clarification.json, planning.json)",
                "- Conversation history and existing project files"
            ]
        
        workspace = str(self._bot_paths.workspace_directory)
        return [
            "**Where to find context:**",
            "- Context will be passed in this message (including context sources attached/dropped into the message)",
            f"- Additional context in `{workspace}/docs/context/` (original input files, prompts, source material)",
            f"- Generated files in `{workspace}/docs/stories/` (clarification.json, planning.json)",
            "- Conversation history and existing project files"
        ]
    
    def write_display_to_file(self, filename: str = 'status.md') -> Path:
        if not self._display_content:
            return None
        
        if not self._bot_paths:
            raise ValueError("bot_paths not set. Pass bot_paths to Instructions constructor.")
        
        # Write to .cursor/display/ directory under workspace
        display_dir = self._bot_paths.workspace_directory / '.cursor' / 'display'
        display_dir.mkdir(parents=True, exist_ok=True)
        
        display_file = display_dir / filename
        content = '\n'.join(self._display_content)
        display_file.write_text(content, encoding='utf-8')
        
        return display_file
    
    def set(self, key: str, value: Any) -> 'Instructions':
        if key == 'base_instructions':
            raise ValueError("Use add() method to add to base_instructions")
        self._data[key] = value
        return self
    
    def update(self, data: Dict[str, Any]) -> 'Instructions':
        for key, value in data.items():
            if key == 'base_instructions':
                # Extend, don't replace
                if isinstance(value, list):
                    self._data['base_instructions'].extend(value)
            else:
                self._data[key] = value
        return self
    
    def to_dict(self) -> Dict[str, Any]:
        result = dict(self._data)
        result['display_content'] = list(self._display_content)
        return result
    
    def copy(self) -> 'Instructions':
        new_inst = Instructions(bot_paths=self._bot_paths)
        new_inst._data = dict(self._data)
        new_inst._data['base_instructions'] = list(self._data['base_instructions'])
        new_inst._display_content = list(self._display_content)
        return new_inst
    
    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)
    
    def __getitem__(self, key: str) -> Any:
        return self._data[key]
    
    def __setitem__(self, key: str, value: Any):
        if key == 'base_instructions':
            raise ValueError("Use add() method to add to base_instructions")
        self._data[key] = value
    
    def __contains__(self, key: str) -> bool:
        return key in self._data
    
    def __repr__(self) -> str:
        return f"Instructions({self._data})"

