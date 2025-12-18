from pathlib import Path
from typing import Dict, Any, Optional, TYPE_CHECKING
from agile_bot.bots.base_bot.src.utils import read_json_file

if TYPE_CHECKING:
    from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
    from agile_bot.bots.base_bot.src.actions.validate.story_graph import StoryGraph
    from agile_bot.bots.base_bot.src.actions.build.knowledge_graph_template import KnowledgeGraphTemplate


class KnowledgeGraphSpec:
    def __init__(self, kg_dir: Path, bot_paths: 'BotPaths'):
        self._kg_dir = kg_dir
        self._bot_paths = bot_paths
        self._config_data: Dict[str, Any] = {}
        self._config_path: Optional[Path] = None
        self._template: Optional['KnowledgeGraphTemplate'] = None
        self._knowledge_graph: Optional['StoryGraph'] = None
        self._load_config()
    
    def _load_config(self):
        # If knowledge_graph folder doesn't exist, use defaults and load story graph from project
        if not self._kg_dir.exists():
            # Default config: use story-graph.json from project's docs/stories folder
            self._config_data = {
                'path': 'docs/stories',
                'output': 'story-graph.json',
                'template': None  # No template needed - just load existing story graph
            }
            self._config_path = None
            return
        
        config_files = list(self._kg_dir.glob('*.json'))
        if not config_files:
            # If folder exists but no config files, use defaults
            self._config_data = {
                'path': 'docs/stories',
                'output': 'story-graph.json',
                'template': None
            }
            self._config_path = None
            return
        
        config_path = config_files[0]
        self._config_data = read_json_file(config_path)
        self._config_path = config_path
    
    @property
    def knowledge_graph(self) -> 'StoryGraph':
        if self._knowledge_graph is None:
            from agile_bot.bots.base_bot.src.actions.validate.story_graph import StoryGraph
            working_dir = self._bot_paths.workspace_directory
            # Pass self (KnowledgeGraphSpec) so StoryGraph can read config internally
            self._knowledge_graph = StoryGraph(
                self._bot_paths,
                working_dir,
                require_file=False,
                knowledge_graph_spec=self
            )
        return self._knowledge_graph
    
    @property
    def output_path(self) -> str:
        """Deprecated: Use knowledge_graph property instead."""
        return self._config_data.get('path', 'docs/stories')
    
    @property
    def output_filename(self) -> str:
        """Deprecated: Use knowledge_graph property instead."""
        return self._config_data.get('output', 'story-graph.json')
    
    @property
    def template_filename(self) -> Optional[str]:
        template_filename = self._config_data.get('template')
        if not template_filename:
            # If no template specified, return None (will be handled by template property)
            return None
        return template_filename
    
    @property
    def template(self) -> Optional['KnowledgeGraphTemplate']:
        if self._template is None:
            template_filename = self.template_filename
            if not template_filename:
                # No template - return None (behavior doesn't need knowledge graph template)
                return None
            from agile_bot.bots.base_bot.src.actions.build.knowledge_graph_template import KnowledgeGraphTemplate
            self._template = KnowledgeGraphTemplate(
                self._kg_dir,
                template_filename
            )
        return self._template
    
    @property
    def config_data(self) -> Dict[str, Any]:
        return self._config_data
    
    @property
    def config_path(self) -> Optional[Path]:
        return self._config_path

