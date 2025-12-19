from pathlib import Path
from typing import Dict, Any, List, Optional, Set
from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
from agile_bot.bots.base_bot.src.actions.scoping_parameter import ScopingParameter

class ActionScope:

    def __init__(self, parameters: Dict[str, Any], bot_paths: Optional[BotPaths]=None):
        self._parameters = parameters or {}
        self._bot_paths = bot_paths
        self._scope_config: Dict[str, Any] = {}
        self._build_scope()

    def _handle_scope_parameter(self, scope_value: Any) -> None:
        if not isinstance(scope_value, dict):
            return
        
        scope_type = scope_value.get('type')
        scope_val = scope_value.get('value')
        
        if scope_type == 'all':
            self._scope_config['all'] = True
        elif scope_type == 'story':
            self._scope_config['story_names'] = scope_val if isinstance(scope_val, list) else [scope_val]
        elif scope_type == 'epic':
            self._scope_config['epic_names'] = scope_val if isinstance(scope_val, list) else [scope_val]
        elif scope_type == 'increment':
            if scope_val and isinstance(scope_val, list) and len(scope_val) > 0:
                if isinstance(scope_val[0], int):
                    self._scope_config['increment_priorities'] = scope_val
                else:
                    self._scope_config['increment_names'] = scope_val
            elif isinstance(scope_val, int):
                self._scope_config['increment_priorities'] = [scope_val]
            elif isinstance(scope_val, str):
                self._scope_config['increment_names'] = [scope_val]

    def _build_scope(self):
        if 'scope' in self._parameters:
            self._handle_scope_parameter(self._parameters['scope'])
        for key, value in self._parameters.items():
            if value is None or key == 'scope':
                continue
            self._handle_custom_parameter(key, value)

    def _handle_custom_parameter(self, key: str, value: Any):
        self._scope_config[key] = value

    @property
    def scope(self) -> Dict[str, Any]:
        return self._scope_config

    def get_story_names(self, knowledge_graph: Dict[str, Any]) -> Optional[Set[str]]:
        if self._scope_config.get('all') is True or not self._scope_config:
            return None
        story_names = set()
        self._collect_from_story_names(self._scope_config, story_names)
        self._collect_from_increments(self._scope_config, knowledge_graph, story_names)
        self._collect_from_epics(self._scope_config, knowledge_graph, story_names)
        return story_names if story_names else None

    def _collect_from_story_names(self, scope_config, story_names):
        if 'story_names' in scope_config:
            story_names_list = scope_config['story_names']
            if isinstance(story_names_list, list):
                story_names.update(story_names_list)
            elif isinstance(story_names_list, str):
                story_names.add(story_names_list)

    def _collect_from_increments(self, scope_config, knowledge_graph, story_names):
        if 'increment_priorities' in scope_config:
            self._collect_stories_from_items(scope_config['increment_priorities'], lambda priority: self._get_increment_story_names(knowledge_graph, priority), story_names)
        if 'increment_names' in scope_config:
            self._collect_stories_from_items(scope_config['increment_names'], lambda name: self._get_increment_story_names_by_name(knowledge_graph, name), story_names)

    def _collect_from_epics(self, scope_config, knowledge_graph, story_names):
        if 'epic_names' in scope_config:
            self._collect_stories_from_items(scope_config['epic_names'], lambda name: self._get_epic_story_names(knowledge_graph, name), story_names)
        if 'story_names' in scope_config or 'increment_priorities' in scope_config or 'epic_names' in scope_config or ('increment_names' in scope_config):
            return story_names
        return None

    def _collect_stories_from_items(self, items: Any, get_stories_fn, story_names: Set[str]) -> None:
        if isinstance(items, list):
            for item in items:
                stories = get_stories_fn(item)
                story_names.update(stories)
        else:
            stories = get_stories_fn(items)
            story_names.update(stories)

    def _extract_story_names(self, stories: list, story_names: Set[str]) -> None:
        for story in stories:
            if isinstance(story, dict):
                story_names.add(story['name'])
            elif isinstance(story, str):
                story_names.add(story)

    def _get_increment_story_names(self, knowledge_graph: Dict[str, Any], priority: int) -> Set[str]:
        story_names = set()
        increments = knowledge_graph.get('increments', [])
        for increment in increments:
            if increment.get('priority') == priority:
                self._extract_story_names(increment.get('stories', []), story_names)
        return story_names

    def _get_increment_story_names_by_name(self, knowledge_graph: Dict[str, Any], increment_name: str) -> Set[str]:
        story_names = set()
        increments = knowledge_graph.get('increments', [])
        for increment in increments:
            if increment.get('name') == increment_name:
                self._extract_story_names(increment.get('stories', []), story_names)
        return story_names

    def _get_epic_story_names(self, knowledge_graph: Dict[str, Any], epic_name: str) -> Set[str]:
        story_names = set()
        epics = knowledge_graph.get('epics', [])
        for epic in epics:
            if epic.get('name') == epic_name:
                self._extract_story_names_from_epic(epic, story_names)
        return story_names

    def _extract_story_names_from_epic(self, epic_data: Dict[str, Any], story_names: Set[str]) -> None:
        story_groups = epic_data.get('story_groups', [])
        for group in story_groups:
            self._extract_story_names(group.get('stories', []), story_names)
        sub_epics = epic_data.get('sub_epics', [])
        for sub_epic in sub_epics:
            self._extract_story_names_from_epic(sub_epic, story_names)

    def filter_story_graph(self, story_graph: Dict[str, Any]) -> Dict[str, Any]:
        if 'scope' not in self._parameters:
            return story_graph
        scope_param = ScopingParameter(self._parameters['scope'])
        return scope_param.filter_story_graph(story_graph)