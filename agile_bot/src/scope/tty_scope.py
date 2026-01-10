"""
TTY adapter for Scope domain object.
"""

from pathlib import Path
from agile_bot.src.cli.adapters import TTYAdapter
from agile_bot.src.scope.scope import Scope


class TTYScope(TTYAdapter):
    """Serializes Scope to TTY - delegates to result adapters (StoryGraph or file list)."""
    
    def __init__(self, scope: Scope):
        """Initialize TTYScope.
        
        Args:
            scope: Scope domain object (already has workspace_directory)
        """
        self.scope = scope
    
    def serialize(self) -> str:
        """Convert Scope to TTY string - delegates to result domain adapters."""
        lines = []
        
        lines.append(self.add_bold("🎯 Scope"))
        
        # Display scope filter
        if self.scope.type.value == 'all':
            filter_display = "all (entire project)"
        else:
            filter_display = ', '.join(self.scope.value) if isinstance(self.scope.value, list) else str(self.scope.value) if self.scope.value else "all"
        
        lines.append(f"🎯 {self.add_bold('Current Scope:')} {filter_display}")
        lines.append("")
        
        # Get results from Scope and delegate to appropriate adapter
        results = self.scope.results
        
        if results is not None:
            # Check type and delegate
            from agile_bot.src.story_graph.story_graph import StoryGraph
            
            if isinstance(results, StoryGraph):
                # Delegate to TTYStoryGraph adapter
                from agile_bot.src.cli.adapter_factory import AdapterFactory
                storyGrapgAdapter = AdapterFactory.create(results, 'tty')
                lines.append(storyGrapgAdapter.serialize())
            elif isinstance(results, list):
                # File list - format as tree
                if results:
                    for file_path in sorted(results):
                        try:
                            rel_path = file_path.relative_to(self.scope.workspace_directory)
                            lines.append(f"  - {rel_path}")
                        except ValueError:
                            lines.append(f"  - {file_path}")
                else:
                    lines.append("  (no files found)")
        else:
            lines.append("  (no scope set)")
        
        lines.append("To change scope (pick ONE - setting a new scope replaces the previous):")
        lines.append("scope all                            # Clear scope, work on entire project")
        lines.append('scope "Story Name"                   # Filter by story (replaces any file scope)')
        lines.append('scope "file:C:/path/to/**/*.py"      # Filter by files (replaces any story scope)')
        lines.append(self.subsection_separator())
        
        return '\n'.join(lines)
    
    def parse_command_text(self, text: str) -> tuple[str, str]:
        """Parse command text."""
        parts = text.split(maxsplit=1)
        verb = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        return verb, args
