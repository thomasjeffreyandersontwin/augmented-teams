"""
Markdown adapter for StoryGraph domain object.
"""

from agile_bot.src.cli.adapters import MarkdownAdapter
from agile_bot.src.story_graph.story_graph import StoryGraph

class MarkdownStoryGraph(MarkdownAdapter):
    """Serializes StoryGraph to Markdown."""
    
    def __init__(self, story_graph: StoryGraph):
        self.story_graph = story_graph
    
    def serialize(self) -> str:
        """Convert StoryGraph to Markdown string."""
        lines = []
        
        lines.append(self.format_header(2, "Story Graph"))
        lines.append("")
        
        lines.append(f"**Path:** `{self.story_graph.path}`")
        lines.append("")
        lines.append(f"**Epic Count:** {self.story_graph.epic_count}")
        lines.append("")
        
        features = []
        if self.story_graph.has_increments:
            features.append("Increments")
        if self.story_graph.has_domain_concepts:
            features.append("Domain Concepts")
        
        if features:
            lines.append(f"**Features:** {', '.join(features)}")
            lines.append("")
        
        # Show epic hierarchy
        content = self.story_graph.content
        if content and 'epics' in content:
            lines.append(self.format_header(3, "Epics"))
            lines.append("")
            
            for epic in content['epics']:
                epic_name = epic.get('name', 'Unknown')
                lines.append(f"- 🎯  **{epic_name}**")
                
                # Recursively show sub-epics and their stories
                for sub_epic in epic.get('sub_epics', []):
                    self._render_sub_epic(sub_epic, lines, indent_level=1)
                
                lines.append("")
        
        return ''.join(lines)
    
    def _render_sub_epic(self, sub_epic: dict, lines: list, indent_level: int):
        """Recursively render a sub-epic and its nested sub-epics and stories.
        
        Args:
            sub_epic: Sub-epic dictionary from story graph
            lines: List to append output lines to
            indent_level: Current indentation level (0 = epic, 1 = first sub-epic, etc.)
        """
        sub_epic_name = sub_epic.get('name', 'Unknown')
        indent = "  " * (indent_level + 1)  # +1 because epic is already indented
        lines.append(f"{indent}- ⚙️  {sub_epic_name}")
        
        # Show stories from story groups
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                story_name = story.get('name', 'Unknown')
                story_indent = "  " * (indent_level + 2)
                lines.append(f"{story_indent}- 📝  {story_name}")
        
        # Show individual stories directly under sub-epic
        for story in sub_epic.get('stories', []):
            story_name = story.get('name', 'Unknown')
            story_indent = "  " * (indent_level + 2)
            lines.append(f"{story_indent}- 📝  {story_name}")
        
        # Recursively handle nested sub-epics
        for nested_sub_epic in sub_epic.get('sub_epics', []):
            self._render_sub_epic(nested_sub_epic, lines, indent_level + 1)
    
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
