from pathlib import Path
from typing import Dict, Any, Optional
from agile_bot.bots.base_bot.src.utils import read_json_file


class KnowledgeGraphTemplate:
    def __init__(self, kg_dir: Path, template_filename: Optional[str]):
        self._kg_dir = kg_dir
        self._template_filename = template_filename
        self._template_content: Dict[str, Any] = {}
        self._template_path: Optional[Path] = None
        self._load_template()
    
    def _load_template(self):
        if not self._template_filename:
            # No template filename specified - template is optional
            return
        
        template_path = self._kg_dir / self._template_filename
        
        # If template file doesn't exist, that's okay - template is optional
        if not template_path.exists():
            # Template file not found - this is acceptable for behaviors that don't need templates
            return
        
        self._template_content = read_json_file(template_path)
        self._template_path = template_path
    
    @property
    def schema(self) -> Dict[str, Any]:
        return self._template_content
    
    @property
    def template_content(self) -> Dict[str, Any]:
        return self._template_content
    
    @property
    def template_path(self) -> Optional[Path]:
        return self._template_path
    
    @property
    def exists(self) -> bool:
        """Check if template file actually exists."""
        return self._template_path is not None and self._template_path.exists()




