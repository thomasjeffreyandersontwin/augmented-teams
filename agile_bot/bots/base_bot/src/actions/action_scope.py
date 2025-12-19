from pathlib import Path
from typing import Dict, Any, List, Optional, Set
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths


class ActionScope:
    """
    Base class for action scopes (build, validate, etc.).
    
    Handles flexible scope configuration from CLI parameters:
    - story_names: List of specific story names to process
    - increment_priorities: List of increment priorities (e.g., [1, 2])
    - epic_names: List of epic names (e.g., ["Epic A", "Epic B"])
    - all: Boolean - if True, process all stories
    - scope: String - can be "all" or specific increment/epic name (convenience)
    
    Subclasses can extend to add action-specific scope parameters.
    """
    
    def __init__(self, parameters: Dict[str, Any], bot_paths: Optional[BotPaths] = None):
        self._parameters = parameters or {}
        self._bot_paths = bot_paths
        self._scope_config: Dict[str, Any] = {}
        self._build_scope()
    
    def _handle_scope_parameter(self, scope_value) -> None:
        """Handle the convenience 'scope' parameter."""
        if scope_value == 'all':
            self._scope_config['all'] = True
            return
        
        if 'increment_names' not in self._scope_config:
            self._scope_config['increment_names'] = []
        
        if isinstance(scope_value, str):
            self._scope_config['increment_names'].append(scope_value)
        elif isinstance(scope_value, list):
            self._scope_config['increment_names'].extend(scope_value)
    
    def _handle_standard_parameter(self, key: str, value) -> bool:
        """Handle standard scope parameters. Returns True if handled."""
        if key in ['story_names', 'increment_priorities', 'epic_names', 'increment_names']:
            self._scope_config[key] = [value] if not isinstance(value, list) else value
            return True
        if key == 'all' and value is True:
            self._scope_config['all'] = True
            return True
        return False
    
    def _build_scope(self):
        """Build scope configuration from parameters. Subclasses can override to add custom parameters."""
        if 'scope' in self._parameters:
            self._handle_scope_parameter(self._parameters['scope'])
        
        for key, value in self._parameters.items():
            if value is None or key == 'scope':
                continue
            if not self._handle_standard_parameter(key, value):
                self._handle_custom_parameter(key, value)
    
    def _handle_custom_parameter(self, key: str, value: Any):
        """Override in subclasses to handle action-specific parameters."""
        # Default: just store it
        self._scope_config[key] = value
    
    @property
    def scope(self) -> Dict[str, Any]:
        """Get scope configuration dictionary."""
        return self._scope_config
    
    def get_story_names(self, knowledge_graph: Dict[str, Any]) -> Optional[Set[str]]:
        """
        Extract story names from knowledge graph based on scope configuration.
        
        Returns:
            Set of story names in scope, or None if scope is 'all' or not specified.
        """
        scope_config = self._scope_config
        
        # If 'all' is True, return None (meaning process all)
        if scope_config.get('all') is True:
            return None
        
        story_names = set()
        
        # Collect from story_names
        if 'story_names' in scope_config:
            story_names_list = scope_config['story_names']
            if isinstance(story_names_list, list):
                story_names.update(story_names_list)
            elif isinstance(story_names_list, str):
                story_names.add(story_names_list)
        
        # Collect from increment_priorities
        if 'increment_priorities' in scope_config:
            self._collect_stories_from_items(
                scope_config['increment_priorities'],
                lambda priority: self._get_increment_story_names(knowledge_graph, priority),
                story_names
            )
        
        # Collect from increment_names
        if 'increment_names' in scope_config:
            self._collect_stories_from_items(
                scope_config['increment_names'],
                lambda name: self._get_increment_story_names_by_name(knowledge_graph, name),
                story_names
            )
        
        # Collect from epic_names
        if 'epic_names' in scope_config:
            self._collect_stories_from_items(
                scope_config['epic_names'],
                lambda name: self._get_epic_story_names(knowledge_graph, name),
                story_names
            )
        
        # If no scope specified at all, return None (meaning process all)
        if not scope_config:
            return None
        
        # If scope was explicitly provided, return the story_names set (even if empty)
        if 'story_names' in scope_config or 'increment_priorities' in scope_config or \
           'epic_names' in scope_config or 'increment_names' in scope_config:
            return story_names
        
        # Default: process all
        return None
    
    def _collect_stories_from_items(self, items: Any, get_stories_fn, story_names: Set[str]) -> None:
        """Helper to collect stories from a list or single item using a callback function.
        
        Args:
            items: Either a list of items or a single item
            get_stories_fn: Function that takes an item and returns a Set[str] of story names
            story_names: Set to update with collected story names
        """
        if isinstance(items, list):
            for item in items:
                stories = get_stories_fn(item)
                story_names.update(stories)
        else:
            stories = get_stories_fn(items)
            story_names.update(stories)
    
    def _extract_story_names(self, stories: list, story_names: Set[str]) -> None:
        """Extract story names from a list of stories.
        
        Extracted to eliminate duplication between _get_increment_story_names(),
        _get_increment_story_names_by_name(), and _extract_story_names_from_epic().
        """
        for story in stories:
            if isinstance(story, dict):
                story_names.add(story['name'])
            elif isinstance(story, str):
                story_names.add(story)
    
    def _get_increment_story_names(self, knowledge_graph: Dict[str, Any], priority: int) -> Set[str]:
        """Get story names from increment by priority."""
        story_names = set()
        increments = knowledge_graph.get('increments', [])
        
        for increment in increments:
            if increment.get('priority') == priority:
                self._extract_story_names(increment.get('stories', []), story_names)
        
        return story_names
    
    def _get_increment_story_names_by_name(self, knowledge_graph: Dict[str, Any], increment_name: str) -> Set[str]:
        """Get story names from increment by name."""
        story_names = set()
        increments = knowledge_graph.get('increments', [])
        
        for increment in increments:
            if increment.get('name') == increment_name:
                self._extract_story_names(increment.get('stories', []), story_names)
        
        return story_names
    
    def _get_epic_story_names(self, knowledge_graph: Dict[str, Any], epic_name: str) -> Set[str]:
        """Get all story names from an epic (recursively)."""
        story_names = set()
        epics = knowledge_graph.get('epics', [])
        
        for epic in epics:
            if epic.get('name') == epic_name:
                self._extract_story_names_from_epic(epic, story_names)
        
        return story_names
    
    def _extract_story_names_from_epic(self, epic_data: Dict[str, Any], story_names: Set[str]) -> None:
        """Recursively extract story names from epic and sub_epics."""
        # Extract from story_groups
        story_groups = epic_data.get('story_groups', [])
        for group in story_groups:
            self._extract_story_names(group.get('stories', []), story_names)
        
        # Recursively extract from sub_epics
        sub_epics = epic_data.get('sub_epics', [])
        for sub_epic in sub_epics:
            self._extract_story_names_from_epic(sub_epic, story_names)

