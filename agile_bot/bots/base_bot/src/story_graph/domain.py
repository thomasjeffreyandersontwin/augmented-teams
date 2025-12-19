"""
Domain Objects

Domain objects for story graphs - not part of the node hierarchy.
"""

from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class Collaborator:
    """Represents a collaborating domain concept."""
    name: str
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def from_str(cls, name: str) -> 'Collaborator':
        """Create from string (presentation boundary)."""
        return cls(name=name)


@dataclass
class Responsibility:
    """Represents a responsibility with its collaborators."""
    name: str
    collaborators: List[Collaborator]
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Responsibility':
        """Create from JSON dict (presentation boundary)."""
        return cls(
            name=data.get('name', ''),
            collaborators=[
                Collaborator.from_str(c) 
                for c in data.get('collaborators', [])
            ]
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dict (for serialization)."""
        return {
            'name': self.name,
            'collaborators': [c.name for c in self.collaborators]
        }


@dataclass
class DomainConcept:
    """Represents a domain concept with its responsibilities."""
    name: str
    responsibilities: List[Responsibility]
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DomainConcept':
        """Create from JSON dict (presentation boundary)."""
        return cls(
            name=data.get('name', ''),
            responsibilities=[
                Responsibility.from_dict(r)
                for r in data.get('responsibilities', [])
            ]
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dict (for serialization)."""
        return {
            'name': self.name,
            'responsibilities': [r.to_dict() for r in self.responsibilities]
        }


@dataclass
class StoryUser:
    """Represents a user in the story context."""
    name: str
    
    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def from_str(cls, user_name: str) -> 'StoryUser':
        """Create from string (presentation boundary)."""
        return cls(name=user_name)
    
    @classmethod
    def from_list(cls, user_names: List[str]) -> List['StoryUser']:
        """Create list from string list (presentation boundary)."""
        return [cls.from_str(name) for name in user_names]
    
    def to_str(self) -> str:
        """Convert to string (for serialization)."""
        return self.name

