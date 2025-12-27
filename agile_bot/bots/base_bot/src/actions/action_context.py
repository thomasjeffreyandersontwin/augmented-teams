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


class ScopeType(Enum):
    ALL = 'all'
    STORY = 'story'
    EPIC = 'epic'
    INCREMENT = 'increment'
    FILES = 'files'


@dataclass
class KnowledgeGraphFilter:
    """Filters content by knowledge graph nodes (stories, epics, increments).
    
    Used for filtering operations to specific parts of the story graph.
    """
    stories: List[str] = field(default_factory=list)
    epics: List[str] = field(default_factory=list)
    increments: List[int] = field(default_factory=list)
    
    def matches_story(self, story_name: str) -> bool:
        """Check if story matches filter."""
        if not self.stories:
            return True
        return story_name in self.stories
    
    def matches_epic(self, epic_name: str) -> bool:
        """Check if epic matches filter."""
        if not self.epics:
            return True
        return epic_name in self.epics
    
    def filter_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter knowledge graph to only nodes matching this filter."""
        # For now, return full graph if no filters specified
        if not self.stories and not self.epics and not self.increments:
            return knowledge_graph
        # TODO: Implement actual filtering logic in Phase 3
        return knowledge_graph


@dataclass
class FileFilter:
    """Filters files by path patterns.
    
    Supports glob patterns for include/exclude.
    """
    include_patterns: List[str] = field(default_factory=list)
    exclude_patterns: List[str] = field(default_factory=list)
    
    def matches_file(self, file_path: Path) -> bool:
        """Check if file matches the filter."""
        if not self.include_patterns:
            return True
        # TODO: Implement glob pattern matching in Phase 3
        file_str = str(file_path)
        for pattern in self.include_patterns:
            if pattern in file_str:
                return True
        return False
    
    def filter_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list to only files matching this filter."""
        if not self.include_patterns and not self.exclude_patterns:
            return file_list
        # TODO: Implement actual filtering logic in Phase 3
        return file_list


@dataclass
class Scope:
    """Scope for filtering bot operations to specific content.
    
    Uses KnowledgeGraphFilter for story/epic/increment scoping
    and FileFilter for file-based scoping. Maintains backward compatibility
    with type/value/exclude API.
    """
    type: ScopeType = ScopeType.ALL
    value: List[str] = field(default_factory=list)
    exclude: List[str] = field(default_factory=list)
    skiprule: List[str] = field(default_factory=list)
    
    # New filter objects
    _knowledge_graph_filter: Optional[KnowledgeGraphFilter] = field(default=None, repr=False)
    _file_filter: Optional[FileFilter] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Initialize filter objects from type/value/exclude."""
        # Create knowledge graph filter for story/epic/increment types
        if self.type in (ScopeType.STORY, ScopeType.EPIC, ScopeType.INCREMENT):
            if self.type == ScopeType.STORY:
                self._knowledge_graph_filter = KnowledgeGraphFilter(stories=self.value)
            elif self.type == ScopeType.EPIC:
                self._knowledge_graph_filter = KnowledgeGraphFilter(epics=self.value)
            elif self.type == ScopeType.INCREMENT:
                # Convert string values to integers
                increments = [int(v) if isinstance(v, str) and v.isdigit() else v for v in self.value]
                self._knowledge_graph_filter = KnowledgeGraphFilter(increments=increments)
        
        # Create file filter for files type
        if self.type == ScopeType.FILES:
            self._file_filter = FileFilter(
                include_patterns=self.value,
                exclude_patterns=self.exclude
            )
    
    @property
    def knowledge_graph_filter(self) -> Optional[KnowledgeGraphFilter]:
        """Get knowledge graph filter (lazy init if needed)."""
        return self._knowledge_graph_filter
    
    @property
    def file_filter(self) -> Optional[FileFilter]:
        """Get file filter (lazy init if needed)."""
        return self._file_filter
    
    def filters_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
        """Filter knowledge graph using knowledge graph filter."""
        if self._knowledge_graph_filter:
            return self._knowledge_graph_filter.filter_knowledge_graph(knowledge_graph)
        return knowledge_graph
    
    def filters_files(self, file_list: List[Path]) -> List[Path]:
        """Filter file list using file filter."""
        if self._file_filter:
            return self._file_filter.filter_files(file_list)
        return file_list
    
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





