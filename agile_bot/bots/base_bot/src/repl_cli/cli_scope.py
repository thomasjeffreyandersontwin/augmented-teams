"""CLI wrapper for Scope with display formatting."""
from pathlib import Path
from typing import Optional
from agile_bot.bots.base_bot.src.actions.action_context import Scope
from agile_bot.bots.base_bot.src.repl_cli.cli_base import CLIBase
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter
import json


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
        
        lines.append(f"**Filter:** {scope_value}")
        lines.append("")
        
        # Display scope items
        if self._scope.type == ScopeType.FILES:
            # Build hierarchical directory structure for files
            lines.append("```")
            tree_lines = self._build_file_tree(scope_lines)
            lines.extend(tree_lines)
            lines.append("```")
        else:
            # For story/other scopes, use existing display
            lines.append("```")
            for line in scope_lines:
                if line.startswith("Scope Filter:"):
                    continue
                lines.append(line)
            lines.append("```")
        
        lines.append("")
        lines.append("")
        lines.append("- Work ONLY on this scope:")
        lines.append("- DO NOT work on all files or the entire story graph")
        lines.append("- Focus EXCLUSIVELY on the items listed above - do not work on the entire story graph or file system")
        lines.append("")
        lines.append("To change scope (pick ONE - setting a new scope replaces the previous):")
        lines.append("```powershell")
        lines.append("scope all                            # Clear scope, work on entire project")
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
    
    @property
    def domain_scope(self) -> Scope:
        """Access the underlying domain Scope object."""
        return self._scope


