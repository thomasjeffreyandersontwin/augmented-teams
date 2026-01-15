"""
JSON adapter for Scope domain object.
"""

import json
from pathlib import Path
from agile_bot.src.cli.adapters import JSONAdapter
from agile_bot.src.scope.scope import Scope


class JSONScope(JSONAdapter):
    """Serializes Scope to JSON - exposes all Scope properties."""
    
    def __init__(self, scope: Scope):
        self.scope = scope
    
    # Expose ALL domain properties
    @property
    def type(self):
        return self.scope.type
    
    @property
    def value(self):
        return self.scope.value
    
    @property
    def exclude(self):
        return self.scope.exclude
    
    @property
    def skiprule(self):
        return self.scope.skiprule
    
    @property
    def story_graph_filter(self):
        return self.scope.story_graph_filter
    
    @property
    def file_filter(self):
        return self.scope.file_filter
    
    def to_dict(self) -> dict:
        """Convert Scope to dict with filtered content for panel display."""
        # Start with basic scope criteria
        result = {
            'type': self.scope.type.value,
            'filter': ', '.join(self.scope.value) if self.scope.value else '',
            'content': None,
            'graphLinks': []
        }
        
        # Add filtered content based on scope type
        if self.scope.type.value in ('story', 'showAll'):
            # Get filtered story graph
            story_graph = self.scope._get_story_graph_results()
            if story_graph:
                # Serialize story graph content (epics array)
                from agile_bot.src.story_graph.json_story_graph import JSONStoryGraph
                graph_adapter = JSONStoryGraph(story_graph)
                content = graph_adapter.to_dict().get('content', [])
                
                # Enrich content with test file links and document links
                # content is a dict with 'epics' key; keep the shape for the panel
                if content and 'epics' in content:
                    self._enrich_with_links(content['epics'], story_graph)
                    # keep as { 'epics': [...] } so scope_view can access content.epics
                    result['content'] = content
                else:
                    result['content'] = {'epics': []}
                
                # Add links to story map files if available
                if self.scope.bot_paths:
                    from pathlib import Path
                    docs_stories = self.scope.workspace_directory / 'docs' / 'stories'
                    story_map_file = docs_stories / 'story-map.md'
                    if story_map_file.exists():
                        result['graphLinks'].append({
                            'text': 'map',
                            'url': str(story_map_file)
                        })
        elif self.scope.type.value == 'files':
            # Get filtered file list
            files = self.scope._get_file_results()
            result['content'] = [{'path': str(f)} for f in files]
        
        return result
    
    def _enrich_with_links(self, epics: list, story_graph):
        """Enrich story graph epics with test file and document links."""
        if not self.scope.workspace_directory or not self.scope.bot_paths:
            return
        
        # Get the test directory from bot paths
        test_dir = self.scope.workspace_directory / self.scope.bot_paths.test_path
        # Get the docs/stories/map directory for document links
        docs_stories_map = self.scope.workspace_directory / 'docs' / 'stories' / 'map'
        
        for epic in epics:
            # Add document folder link for epic
            epic_folder = docs_stories_map / f"🎯 {epic['name']}"
            if epic_folder.exists() and epic_folder.is_dir():
                if 'links' not in epic:
                    epic['links'] = []
                epic['links'].append({
                    'text': 'docs',
                    'url': str(epic_folder),
                    'icon': 'document'
                })
            
            # Process sub-epics recursively
            if 'sub_epics' in epic:
                for sub_epic in epic['sub_epics']:
                    self._enrich_sub_epic_with_links(sub_epic, test_dir, docs_stories_map, epic['name'])
    
    def _enrich_sub_epic_with_links(self, sub_epic: dict, test_dir: Path, docs_stories_map: Path, epic_name: str, parent_path: str = None):
        """Recursively enrich sub-epic with test file and document links."""
        # Build the document path (epic/sub-epic hierarchy)
        if parent_path:
            sub_epic_doc_folder = Path(parent_path) / f"⚙️ {sub_epic['name']}"
        else:
            sub_epic_doc_folder = docs_stories_map / f"🎯 {epic_name}" / f"⚙️ {sub_epic['name']}"
        
        # Initialize links array
        if 'links' not in sub_epic:
            sub_epic['links'] = []
        
        # Add test file link if test_file is specified
        if 'test_file' in sub_epic and sub_epic['test_file']:
            test_file_path = test_dir / sub_epic['test_file']
            if test_file_path.exists():
                sub_epic['links'].append({
                    'text': 'test',
                    'url': str(test_file_path),
                    'icon': 'test_tube'
                })
        
        # Add document folder link if it exists (will be revealed in VS Code file explorer)
        if sub_epic_doc_folder.exists() and sub_epic_doc_folder.is_dir():
            sub_epic['links'].append({
                'text': 'docs',
                'url': str(sub_epic_doc_folder),
                'icon': 'document'
            })
        
        # Process nested sub-epics recursively
        if 'sub_epics' in sub_epic:
            for nested_sub_epic in sub_epic['sub_epics']:
                self._enrich_sub_epic_with_links(nested_sub_epic, test_dir, docs_stories_map, epic_name, str(sub_epic_doc_folder))
        
        # Process story groups and stories
        if 'story_groups' in sub_epic:
            for story_group in sub_epic['story_groups']:
                if 'stories' in story_group:
                    for story in story_group['stories']:
                        self._enrich_story_with_links(story, test_dir, sub_epic_doc_folder, sub_epic.get('test_file'))
    
    def _enrich_story_with_links(self, story: dict, test_dir: Path, parent_doc_folder: Path, parent_test_file: str):
        """Enrich story with test file links (with #test_class anchor) and document links."""
        # Initialize links array
        if 'links' not in story:
            story['links'] = []
        
        # Add story document file link
        story_doc_file = parent_doc_folder / f"📝 {story['name']}.md"
        if story_doc_file.exists():
            story['links'].append({
                'text': 'story',
                'url': str(story_doc_file),
                'icon': 'document'
            })
        
        # Add test file link with #test_class anchor if available
        test_file = story.get('test_file') or parent_test_file
        test_class = story.get('test_class')
        
        if test_file and test_class:
            test_file_path = test_dir / test_file
            if test_file_path.exists():
                # Add VS Code anchor for test class
                test_url = f"{test_file_path}#{test_class}"
                story['links'].append({
                    'text': 'test',
                    'url': test_url,
                    'icon': 'test_tube'
                })
        
        # Process scenarios
        if 'scenarios' in story:
            for scenario in story['scenarios']:
                self._enrich_scenario_with_links(scenario, test_dir, test_file, test_class)
    
    def _enrich_scenario_with_links(self, scenario: dict, test_dir: Path, story_test_file: str, story_test_class: str):
        """Enrich scenario with test file link (with #L<line_number> anchor for VS Code)."""
        test_method = scenario.get('test_method')
        
        if story_test_file and test_method:
            test_file_path = test_dir / story_test_file
            if test_file_path.exists():
                # Use find_test_method_line to get the actual line number
                from agile_bot.src.utils import find_test_method_line
                line_number = find_test_method_line(test_file_path, test_method)
                
                if line_number:
                    # Format: absolute_path#L<line_number> (VS Code line number format)
                    test_url = f"{test_file_path}#L{line_number}"
                    scenario['test_file'] = test_url
                else:
                    # Fallback: if we can't find line number, don't set test_file
                    # (panel will check for test_file existence before rendering icon)
                    pass
    
    def deserialize(self, data: str) -> dict:
        """Parse JSON string to dict."""
        return json.loads(data)
