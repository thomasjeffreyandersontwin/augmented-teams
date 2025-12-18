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
    
    def _build_scope(self):
        """Build scope configuration from parameters. Subclasses can override to add custom parameters."""
        # Handle convenience 'scope' parameter - convert to appropriate scope type
        if 'scope' in self._parameters:
            scope_value = self._parameters['scope']
            if scope_value == 'all':
                self._scope_config['all'] = True
            else:
                # Assume it's an increment name or epic name
                # Try to determine which - could be either, so we'll set both for flexibility
                # The story graph resolver will handle matching
                if 'increment_names' not in self._scope_config:
                    self._scope_config['increment_names'] = []
                if isinstance(scope_value, str):
                    self._scope_config['increment_names'].append(scope_value)
                elif isinstance(scope_value, list):
                    self._scope_config['increment_names'].extend(scope_value)
        
        # Handle explicit scope parameters
        for key, value in self._parameters.items():
            if value is None:
                continue
            
            if key == 'scope':
                # Already handled above
                continue
            elif key in ['story_names', 'increment_priorities', 'epic_names', 'increment_names']:
                # Standard story graph scope parameters
                if not isinstance(value, list):
                    value = [value]
                self._scope_config[key] = value
            elif key == 'all' and value is True:
                self._scope_config['all'] = True
            else:
                # Allow subclasses to handle custom parameters
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
            priorities = scope_config['increment_priorities']
            if isinstance(priorities, list):
                for priority in priorities:
                    increment_stories = self._get_increment_story_names(knowledge_graph, priority)
                    story_names.update(increment_stories)
            else:
                increment_stories = self._get_increment_story_names(knowledge_graph, priorities)
                story_names.update(increment_stories)
        
        # Collect from increment_names
        if 'increment_names' in scope_config:
            increment_names = scope_config['increment_names']
            if isinstance(increment_names, list):
                for increment_name in increment_names:
                    increment_stories = self._get_increment_story_names_by_name(knowledge_graph, increment_name)
                    story_names.update(increment_stories)
            elif isinstance(increment_names, str):
                increment_stories = self._get_increment_story_names_by_name(knowledge_graph, increment_names)
                story_names.update(increment_stories)
        
        # Collect from epic_names
        if 'epic_names' in scope_config:
            epic_names_list = scope_config['epic_names']
            if isinstance(epic_names_list, list):
                for epic_name in epic_names_list:
                    epic_stories = self._get_epic_story_names(knowledge_graph, epic_name)
                    story_names.update(epic_stories)
            elif isinstance(epic_names_list, str):
                epic_stories = self._get_epic_story_names(knowledge_graph, epic_names_list)
                story_names.update(epic_stories)
        
        # If no scope specified at all, return None (meaning process all)
        if not scope_config:
            return None
        
        # If scope was explicitly provided, return the story_names set (even if empty)
        if 'story_names' in scope_config or 'increment_priorities' in scope_config or \
           'epic_names' in scope_config or 'increment_names' in scope_config:
            return story_names
        
        # Default: process all
        return None
    
    def _get_increment_story_names(self, knowledge_graph: Dict[str, Any], priority: int) -> Set[str]:
        """Get story names from increment by priority."""
        story_names = set()
        increments = knowledge_graph.get('increments', [])
        
        for increment in increments:
            if increment.get('priority') == priority:
                stories = increment.get('stories', [])
                for story in stories:
                    if isinstance(story, dict):
                        story_names.add(story['name'])
                    elif isinstance(story, str):
                        story_names.add(story)
        
        return story_names
    
    def _get_increment_story_names_by_name(self, knowledge_graph: Dict[str, Any], increment_name: str) -> Set[str]:
        """Get story names from increment by name."""
        story_names = set()
        increments = knowledge_graph.get('increments', [])
        
        for increment in increments:
            if increment.get('name') == increment_name:
                stories = increment.get('stories', [])
                for story in stories:
                    if isinstance(story, dict):
                        story_names.add(story['name'])
                    elif isinstance(story, str):
                        story_names.add(story)
        
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
            stories = group.get('stories', [])
            for story in stories:
                if isinstance(story, dict):
                    story_names.add(story['name'])
                elif isinstance(story, str):
                    story_names.add(story)
        
        # Recursively extract from sub_epics
        sub_epics = epic_data.get('sub_epics', [])
        for sub_epic in sub_epics:
            self._extract_story_names_from_epic(sub_epic, story_names)

