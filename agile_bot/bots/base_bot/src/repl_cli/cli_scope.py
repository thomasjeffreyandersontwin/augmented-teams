"""CLI wrapper for Scope with display formatting."""
from pathlib import Path
from typing import Optional
from agile_bot.bots.base_bot.src.actions.action_context import Scope
import json


class CLIScope:
    """CLI wrapper for Scope that adds display formatting."""
    
    def __init__(self, scope: Scope, workspace_directory: Path):
        self._scope = scope
        self._workspace_directory = workspace_directory
    
    @classmethod
    def from_state_file(cls, workspace_directory: Path) -> Optional['CLIScope']:
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
            return cls(scope, workspace_directory)
        except Exception:
            return None
    
    def to_formatted_display(self) -> str:
        """Render scope with CLI-specific formatting (warnings, separators)."""
        lines = []
        
        lines.append("-" * 60)
        lines.append("⚠️  SCOPE FILTER ACTIVE - Work ONLY on the following scope:")
        lines.append("-" * 60)
        
        # Get plain scope display lines from domain object
        scope_lines = self._scope.to_display_lines(self._workspace_directory)
        lines.extend(scope_lines)
        
        lines.append("")
        lines.append("⚠️  DO NOT work on all files or the entire story graph")
        lines.append("⚠️  Focus EXCLUSIVELY on the items listed above")
        lines.append("-" * 60)
        lines.append("")
        
        return "\n".join(lines)
    
    @property
    def domain_scope(self) -> Scope:
        """Access the underlying domain Scope object."""
        return self._scope

