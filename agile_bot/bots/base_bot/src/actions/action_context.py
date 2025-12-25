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
    ALL = 'all'
    STORY = 'story'
    EPIC = 'epic'
    INCREMENT = 'increment'
    FILES = 'files'


@dataclass
class Scope:
    type: ScopeType = ScopeType.ALL
    value: List[str] = field(default_factory=list)
    exclude: List[str] = field(default_factory=list)
    skiprule: List[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
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
        return {
            'type': self.type.value,
            'value': self.value,
            'exclude': self.exclude,
            'skiprule': self.skiprule,
        }


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
    assumptions: Optional[List[str]] = None
    
    def __post_init__(self):
        # Allow dynamic attributes for decisions
        pass
    
    def get_decisions(self) -> Dict[str, Any]:
        """Get all decision attributes (exclude assumptions and internal attrs)."""
        excluded = {'assumptions'}
        return {k: v for k, v in self.__dict__.items() 
                if not k.startswith('_') and k not in excluded and v is not None}


@dataclass
class ValidateActionContext(ScopeActionContext):
    background: Optional[bool] = None
    skip_cross_file: bool = False
    all_files: bool = False
    force_full: bool = False  # Alias for all_files for backward compatibility
    
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





