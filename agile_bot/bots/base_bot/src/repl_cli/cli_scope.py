"""CLI wrapper for Scope with display formatting."""
from pathlib import Path
from typing import Optional
from ..actions.action_context import Scope
from .cli_base import CLIBase
from .formatters.output_formatter import OutputFormatter
from ..actions.validate.file_link_builder import FileLinkBuilder
from ..bot.workspace import get_python_workspace_root
from ..utils import build_test_file_link, build_test_class_link, build_test_method_link
import json
import re


class CLIScope(CLIBase):
    """CLI wrapper for Scope that adds display formatting."""
    
    def __init__(self, scope: Scope, workspace_directory: Path, formatter: OutputFormatter):
        super().__init__(formatter)
        self._scope = scope
        self._workspace_directory = workspace_directory
    
    @classmethod
    def from_state_file(cls, workspace_directory: Path, formatter: OutputFormatter) -> Optional['CLIScope']:
        """Load scope from bot state file and wrap it."""
        try:
            state_file = workspace_directory / 'behavior_action_state.json'
            if not state_file.exists():
                return None
            
            state_data = json.loads(state_file.read_text())
            scope_dict = state_data.get('scope')
            if not scope_dict:
                return None
            
            scope = Scope.from_dict(scope_dict)
            return cls(scope, workspace_directory, formatter)
        except Exception:
            return None
    
    def to_formatted_display(self) -> str:
        """Render scope with CLI-specific formatting (warnings, separators, and AI instructions)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ScopeType
        lines = []
        
        scope_icon = self.formatter.scope_icon()
        file_icon = self.formatter.file_icon()
        
        # Scope section header
        lines.append(f"## {scope_icon} **Scope**")
        
        # Get plain scope display lines from domain object
        scope_lines = self._scope.to_display_lines(self._workspace_directory)
        
        # Extract filter value
        scope_value = None
        for line in scope_lines:
            if line.startswith("Scope Filter:"):
                scope_value = line.replace("Scope Filter:", "").strip()
                break
        
        # For file scopes, add wildcard if missing
        if self._scope.type == ScopeType.FILES and scope_value:
            # Add /* to the end if no wildcard present
            if not any(wildcard in scope_value for wildcard in ['*', '?', '[']):
                scope_value = scope_value.rstrip('/') + '/*'
        
        # Build story-graph.json path and link (only if files exist)
        story_graph_path = self._workspace_directory / 'docs' / 'stories' / 'story-graph.json'
        story_map_path = self._workspace_directory / 'docs' / 'stories' / 'story-map.drawio'
        links = ""
        
        # Get workspace root once if either file exists
        workspace_root = None
        if story_graph_path.exists() or story_map_path.exists():
            try:
                workspace_root = get_python_workspace_root()
            except (ValueError, AttributeError):
                pass
        
        # Graph link (to story-graph.json) - only if file exists
        if story_graph_path.exists() and workspace_root:
            try:
                rel_path = story_graph_path.relative_to(workspace_root)
                rel_path_str = str(rel_path).replace('\\', '/')
                links = f" | [Graph]({rel_path_str})"
            except (ValueError, AttributeError):
                pass
        
        # Map link (to story-map.drawio) - only if file exists
        if story_map_path.exists() and workspace_root:
            try:
                rel_path = story_map_path.relative_to(workspace_root)
                rel_path_str = str(rel_path).replace('\\', '/')
                links += f" | [map]({rel_path_str})"
            except (ValueError, AttributeError):
                pass
        
        lines.append(f"**Filter:** {scope_value}{links}")
        lines.append("")
        
        # Display scope items
        if self._scope.type == ScopeType.FILES:
            # Build hierarchical directory structure for files
            lines.append("```")
            tree_lines = self._build_file_tree(scope_lines)
            lines.extend(tree_lines)
            lines.append("```")
        else:
            # For story/other scopes, enhance with hyperlinks and display as markdown (not code block)
            enhanced_lines = self._enhance_story_lines_with_hyperlinks(scope_lines)
            for line in enhanced_lines:
                if line.startswith("Scope Filter:"):
                    continue
                lines.append(line)
        
        lines.append("")
        lines.append("")
        lines.append("- Work ONLY on this scope:")
        lines.append("- DO NOT work on all files or the entire story graph")
        lines.append("- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system")
        lines.append("")
        lines.append("To change scope (pick ONE - setting a new scope replaces the previous):")
        lines.append("```powershell")
        lines.append("scope all                            # Clear scope, work on entire project")
        lines.append("scope showAll                        # Show entire story graph (no filtering)")
        lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
        lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)')
        lines.append("```")
        
        return "\n".join(lines)
    
    def _build_file_tree(self, scope_lines: list) -> list:
        """Build a hierarchical directory tree from file paths."""
        from pathlib import Path
        
        # Extract file paths from scope lines
        file_paths = []
        for line in scope_lines:
            if line.startswith("Scope Filter:"):
                continue
            # Remove leading "  - " and parse as path
            path_str = line.strip().lstrip('- ').strip()
            if path_str and not path_str.endswith("(no files found)"):
                file_paths.append(Path(path_str))
        
        if not file_paths:
            return ["  (no files found)"]
        
        # Build tree structure
        tree = {}
        for file_path in file_paths:
            parts = file_path.parts
            current = tree
            for i, part in enumerate(parts):
                if part not in current:
                    current[part] = {}
                current = current[part]
        
        # Render tree
        return self._render_tree(tree, "")
    
    def _render_tree(self, tree: dict, prefix: str, is_last: bool = True) -> list:
        """Recursively render tree structure with proper indentation."""
        lines = []
        items = list(tree.items())
        
        for i, (name, subtree) in enumerate(items):
            is_last_item = (i == len(items) - 1)
            
            # Determine if this is a file or directory
            is_file = len(subtree) == 0
            
            # Build the line
            connector = "└── " if is_last_item else "├── "
            icon = self.formatter.file_icon() if is_file else "📁"
            lines.append(f"{prefix}{connector}{icon} {name}")
            
            # Recurse for directories
            if subtree:
                extension = "    " if is_last_item else "│   "
                lines.extend(self._render_tree(subtree, prefix + extension, is_last_item))
        
        return lines
    
    def _enhance_story_lines_with_hyperlinks(self, scope_lines: list) -> list:
        """Enhance story lines with hyperlinks to story files and format as tree structure."""
        enhanced_lines = []
        epic_name = None
        sub_epic_name = None
        
        # Pattern to match story/epic/sub-epic lines with optional test info
        # Format: "  🎯 Epic Name" or "    ⚙️ Sub Epic Name|TEST_FILE:file.py" or "      📝 Story Name|TEST_FILE:file.py|TEST_CLASS:ClassName"
        epic_pattern = re.compile(r'^(\s*)(🎯)\s+(.+?)(?:\|TEST_FILE:(.+))?$')
        sub_epic_pattern = re.compile(r'^(\s*)(⚙️)\s+(.+?)(?:\|TEST_FILE:(.+))?$')
        story_pattern = re.compile(r'^(\s*)(📝)\s+(.+?)(?:\|TEST_FILE:(.+?))?(?:\|TEST_CLASS:(.+))?$')
        
        # First pass: collect all items to determine tree structure, preserving indentation
        items = []
        for line in scope_lines:
            if line.startswith("Scope Filter:"):
                continue
            
            epic_match = epic_pattern.match(line)
            if epic_match:
                indent_level = len(epic_match.group(1)) // 2  # Each level is 2 spaces
                items.append(('epic', epic_match.group(3).strip(), indent_level, None, None))
                continue
            
            sub_epic_match = sub_epic_pattern.match(line)
            if sub_epic_match:
                indent_level = len(sub_epic_match.group(1)) // 2  # Each level is 2 spaces
                test_file = sub_epic_match.group(4) if sub_epic_match.lastindex >= 4 and sub_epic_match.group(4) else None
                items.append(('sub_epic', sub_epic_match.group(3).strip(), indent_level, None, test_file))
                continue
            
            story_match = story_pattern.match(line)
            if story_match:
                indent_level = len(story_match.group(1)) // 2  # Each level is 2 spaces
                test_file = story_match.group(4) if story_match.lastindex >= 4 and story_match.group(4) else None
                test_class = story_match.group(5) if story_match.lastindex >= 5 else None
                items.append(('story', story_match.group(3).strip(), indent_level, line, (test_file, test_class)))
                continue
        
        # Second pass: render with tree structure, respecting nesting levels
        epic_idx = -1
        sub_epic_indices = {}  # Track sub-epic indices by nesting level
        sub_epic_names = {}  # Track sub-epic names by nesting level
        sub_epic_test_files = {}  # Track sub-epic test_files by nesting level
        story_idx = -1
        
        for i, (item_type, item_name, indent_level, original_line, item_data) in enumerate(items):
            if item_type == 'epic':
                epic_name = item_name
                epic_idx = i
                sub_epic_indices = {}  # Reset sub-epic tracking for new epic
                sub_epic_names = {}  # Reset sub-epic names for new epic
                sub_epic_test_files = {}  # Reset sub-epic test_files for new epic
                story_idx = -1
                enhanced_lines.append(f"🎯 {epic_name}")
            
            elif item_type == 'sub_epic':
                # Track this sub-epic at its nesting level
                sub_epic_indices[indent_level] = i
                sub_epic_names[indent_level] = item_name
                # Track test_file from sub-epic (item_data is the test_file string)
                sub_epic_test_files[indent_level] = item_data
                story_idx = -1
                
                # Find siblings at the same nesting level
                has_siblings_at_level = any(
                    items[j][0] == 'sub_epic' and items[j][2] == indent_level 
                    for j in range(i + 1, len(items))
                )
                
                # Find children (stories or nested sub-epics) at deeper levels
                has_children = any(
                    (items[j][0] == 'story' or (items[j][0] == 'sub_epic' and items[j][2] > indent_level))
                    for j in range(i + 1, len(items))
                    if j < len(items) and items[j][2] > indent_level
                )
                
                # Build indentation prefix based on nesting level
                # Level 0 (directly under epic): 2 spaces + connector
                # Level 1 (nested sub-epic): 2 spaces + │   + connector
                # Level 2: 2 spaces + │   + │   + connector, etc.
                base_indent = "  " * indent_level
                
                # Build tree connector with vertical lines for parent levels
                connector_parts = []
                for level in range(indent_level):
                    # Check if there are siblings at this parent level after current position
                    has_siblings_at_parent = any(
                        items[k][0] == 'sub_epic' and items[k][2] == level
                        for k in range(i + 1, len(items))
                    )
                    # Check if there are items (stories or nested sub-epics) at this level or deeper
                    # that come after the current item
                    has_items_below = any(
                        items[k][2] > level
                        for k in range(i + 1, len(items))
                    )
                    # Show vertical line if there are siblings or items below at this parent level
                    if has_siblings_at_parent or has_items_below:
                        connector_parts.append("│   ")
                    else:
                        connector_parts.append("    ")
                
                prefix = "".join(connector_parts)
                
                # Determine connector for this level
                connector = "├── " if (has_siblings_at_level or has_children) else "└── "
                
                # Add test file link if available
                test_file = item_data
                test_link = ""
                if test_file:
                    test_link = self._build_test_file_link(test_file)
                
                enhanced_lines.append(f"{base_indent}{prefix}{connector}⚙️ {item_name}{test_link}")
            
            elif item_type == 'story':
                story_name = item_name
                
                # Find the parent sub-epic name at the appropriate nesting level
                parent_indent_level = indent_level - 1
                parent_sub_epic_name = sub_epic_names.get(parent_indent_level) if parent_indent_level >= 0 else None
                
                # Build story file path
                story_file_path = self._build_story_file_path(epic_name, parent_sub_epic_name, story_name)
                
                # Find the parent sub-epic index at the appropriate nesting level
                parent_sub_epic_idx = -1
                parent_indent_level = indent_level - 1
                if parent_indent_level >= 0:
                    parent_sub_epic_idx = sub_epic_indices.get(parent_indent_level, -1)
                
                # Check if this is the last story at this nesting level
                is_last_story = True
                for j in range(i + 1, len(items)):
                    if items[j][0] == 'story' and items[j][2] == indent_level:
                        is_last_story = False
                        break
                    elif items[j][2] <= indent_level and items[j][0] != 'story':
                        break
                
                # Build indentation prefix based on nesting level
                base_indent = "  " * indent_level
                
                # Build tree connector with vertical lines for parent levels
                connector_parts = []
                for level in range(indent_level):
                    # Check if there are siblings at this parent level after current position
                    has_siblings_at_parent = any(
                        items[k][0] == 'sub_epic' and items[k][2] == level
                        for k in range(i + 1, len(items))
                    )
                    # Check if there are items (stories or nested sub-epics) at this level or deeper
                    # that come after the current item
                    has_items_below = any(
                        items[k][2] > level
                        for k in range(i + 1, len(items))
                    )
                    # Show vertical line if there are siblings or items below at this parent level
                    if has_siblings_at_parent or has_items_below:
                        connector_parts.append("│   ")
                    else:
                        connector_parts.append("    ")
                
                prefix = "".join(connector_parts)
                
                # Determine connector for this level
                connector = prefix + ("└── " if is_last_story else "├── ")
                
                if story_file_path and story_file_path.exists():
                    # For files with emojis in path, use relative path from workspace root
                    # Cursor resolves markdown links relative to workspace root, not workspace_directory
                    try:
                        workspace_root = get_python_workspace_root()
                        rel_path = story_file_path.relative_to(workspace_root)
                        # Use relative path as markdown link - Cursor will resolve it correctly
                        rel_path_str = str(rel_path).replace('\\', '/')
                        enhanced_lines.append(f"{connector}[📝 {story_name}]({rel_path_str})")
                    except (ValueError, AttributeError):
                        # If relative path fails, try vscode://file URI as fallback
                        link_builder = FileLinkBuilder(self._workspace_directory)
                        file_uri = link_builder.get_file_uri(str(story_file_path))
                        enhanced_lines.append(f"{connector}[📝 {story_name}]({file_uri})")
                else:
                    # File doesn't exist, keep original formatting
                    enhanced_lines.append(f"{connector}📝 {story_name}")
                
                # Add test class link if available
                # Get test_class from story's item_data (stories should not have test_file)
                _, test_class = item_data if item_data else (None, None)
                
                # Get test_file ONLY from parent sub-epic (stories should not have test_file)
                test_file = None
                parent_indent_level = indent_level - 1
                if parent_indent_level >= 0:
                    test_file = sub_epic_test_files.get(parent_indent_level)
                
                if test_file and test_class:
                    test_class_link = self._build_test_class_link(test_file, test_class)
                    if test_class_link:
                        enhanced_lines[-1] = enhanced_lines[-1] + test_class_link
        
        return enhanced_lines
    
    def _build_story_file_path(self, epic_name: Optional[str], sub_epic_name: Optional[str], story_name: str) -> Optional[Path]:
        """Build the file path for a story based on epic/sub-epic/story names."""
        if not epic_name:
            return None
        
        # Build path: docs/stories/map/🎯 {epic_name}/⚙️ {sub_epic_name}/📝 {story_name}.md
        map_dir = self._workspace_directory / 'docs' / 'stories' / 'map'
        epic_folder = f"🎯 {epic_name}"
        
        if sub_epic_name and sub_epic_name != epic_name:
            sub_epic_folder = f"⚙️ {sub_epic_name}"
            story_file = map_dir / epic_folder / sub_epic_folder / f"📝 {story_name}.md"
        else:
            # If no sub-epic or sub-epic same as epic, check if epic folder has stories directly
            # Some structures might have stories directly under epic
            story_file = map_dir / epic_folder / f"📝 {story_name}.md"
            if not story_file.exists() and sub_epic_name:
                # Try with sub-epic folder even if it matches epic name
                sub_epic_folder = f"⚙️ {sub_epic_name}"
                story_file = map_dir / epic_folder / sub_epic_folder / f"📝 {story_name}.md"
        
        return story_file
    
    def _build_test_file_link(self, test_file: str) -> str:
        """Build link to test file."""
        return build_test_file_link(test_file, self._workspace_directory)
    
    def _build_test_class_link(self, test_file: str, test_class: str) -> str:
        """Build link to test class with line number."""
        return build_test_class_link(test_file, test_class, self._workspace_directory)
    
    @property
    def domain_scope(self) -> Scope:
        """Access the underlying domain Scope object."""
        return self._scope


