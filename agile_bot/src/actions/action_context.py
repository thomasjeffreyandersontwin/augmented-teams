"""Typed action context classes for type-safe CLI parameter handling.

This module defines the ActionContext hierarchy - typed dataclasses that replace
Dict[str, Any] parameters. Each action declares which context class it uses,
enabling type-safe parameter passing from CLI to action.execute().

The CLI parser generator reads these context classes to generate argument parsers.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from pathlib import Path
from enum import Enum

# Import scope domain classes from scope package
from ..scope import Scope, ScopeType, StoryGraphFilter, FileFilter




@dataclass
class ActionContext:
    pass


@dataclass
class ScopeActionContext(ActionContext):
    scope: Optional[Scope] = None


@dataclass
class ClarifyActionContext(ActionContext):
    answers: Optional[Dict[str, Any]] = None
    evidence_provided: Optional[Dict[str, Any]] = None
    context: Optional[str] = None


@dataclass
class StrategyActionContext(ActionContext):
    decisions_made: Optional[Dict[str, Any]] = None
    assumptions: Optional[List[str]] = None
    assumptions_made: Optional[List[str]] = None
    
    def __post_init__(self):
        """Normalize strategy context fields and keep backward compatibility."""
        # Default collections to empty to simplify downstream checks
        if self.decisions_made is None:
            object.__setattr__(self, 'decisions_made', {})
        if self.assumptions_made is None:
            object.__setattr__(self, 'assumptions_made', self.assumptions or [])
        # Keep legacy alias in sync
        if self.assumptions is None:
            object.__setattr__(self, 'assumptions', self.assumptions_made)
    
    def get_decisions(self) -> Dict[str, Any]:
        """Get all decision attributes (exclude assumption fields and internals)."""
        excluded = {'assumptions', 'assumptions_made', 'decisions_made'}
        decisions = dict(self.decisions_made or {})
        for key, value in self.__dict__.items():
            if key.startswith('_') or key in excluded or value is None:
                continue
            decisions[key] = value
        return decisions
    
    @property
    def assumptions_list(self) -> Optional[List[str]]:
        """Alias to keep existing code using context.assumptions working."""
        return self.assumptions or self.assumptions_made
    
    @assumptions_list.setter
    def assumptions_list(self, value: Optional[List[str]]):
        object.__setattr__(self, 'assumptions_made', value)
        object.__setattr__(self, 'assumptions', value)


@dataclass
class ValidateActionContext(ScopeActionContext):
    background: Optional[bool] = None
    skip_cross_file: bool = False
    all_files: bool = False
    force_full: bool = False  # Alias for all_files for backward compatibility
    max_cross_file_comparisons: int = 20  # Maximum number of files to compare against in cross-file duplication scan
    
    def __post_init__(self):
        # Sync force_full and all_files - they mean the same thing
        if self.force_full:
            object.__setattr__(self, 'all_files', True)
        elif self.all_files:
            object.__setattr__(self, 'force_full', True)


@dataclass
class RulesActionContext(ActionContext):
    message: Optional[str] = None


# Type alias for context class type hints
ContextClass = type





