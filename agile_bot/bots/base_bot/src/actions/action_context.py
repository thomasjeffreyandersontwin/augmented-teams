"""Typed action context classes for type-safe CLI parameter handling.

This module defines the ActionContext hierarchy - typed dataclasses that replace
Dict[str, Any] parameters. Each action declares which context class it uses,
enabling type-safe parameter passing from CLI to action.execute().

The CLI parser generator reads these context classes to generate argument parsers.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum


class ScopeType(Enum):
    """Valid scope types for filtering actions."""
    ALL = 'all'
    STORY = 'story'
    EPIC = 'epic'
    INCREMENT = 'increment'
    FILES = 'files'


@dataclass
class ScopeConfig:
    """Typed scope configuration for filtering what an action operates on.
    
    Replaces the untyped scope dict: {"type": "files", "value": [...], "exclude": [...]}
    """
    type: ScopeType = ScopeType.ALL
    value: List[str] = field(default_factory=list)
    exclude: List[str] = field(default_factory=list)
    skiprule: List[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ScopeConfig':
        """Create ScopeConfig from dictionary (for JSON parsing)."""
        if not data:
            return cls()
        
        scope_type_str = data.get('type', 'all')
        try:
            scope_type = ScopeType(scope_type_str)
        except ValueError:
            raise ValueError(f"Invalid scope type: '{scope_type_str}'. Valid types: {[t.value for t in ScopeType]}")
        
        return cls(
            type=scope_type,
            value=data.get('value', []) if isinstance(data.get('value'), list) else [data.get('value')] if data.get('value') else [],
            exclude=data.get('exclude', []) if isinstance(data.get('exclude'), list) else [data.get('exclude')] if data.get('exclude') else [],
            skiprule=data.get('skiprule', []) if isinstance(data.get('skiprule'), list) else [data.get('skiprule')] if data.get('skiprule') else [],
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            'type': self.type.value,
            'value': self.value,
            'exclude': self.exclude,
            'skiprule': self.skiprule,
        }


@dataclass
class ActionContext:
    """Base action context - empty by default.
    
    Actions that need no parameters use this directly.
    Other actions inherit from this and add their specific fields.
    """
    pass


@dataclass
class ScopeActionContext(ActionContext):
    """Context for actions that filter by scope (build, render).
    
    Provides the scope field for filtering stories, epics, increments, or files.
    """
    scope: Optional[ScopeConfig] = None


@dataclass
class ClarifyActionContext(ActionContext):
    """Context for clarify action.
    
    Contains answers to key questions and evidence provided during clarification.
    """
    key_questions_answered: Optional[Dict[str, Any]] = None
    evidence_provided: Optional[Dict[str, Any]] = None


@dataclass
class StrategyActionContext(ActionContext):
    """Context for strategy action.
    
    Contains decisions made and assumptions recorded during strategy planning.
    """
    decisions_made: Optional[Dict[str, Any]] = None
    assumptions_made: Optional[List[str]] = None


@dataclass
class ValidateActionContext(ScopeActionContext):
    """Context for validate action.
    
    Inherits scope from ScopeActionContext and adds validation-specific parameters.
    """
    background: Optional[bool] = None
    skip_cross_file: bool = False
    force_full: bool = False


# Type alias for context class type hints
ContextClass = type


