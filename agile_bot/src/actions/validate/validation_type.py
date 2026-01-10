from enum import Enum


class ValidationType(Enum):
    """Type of content a behavior validates by default."""
    STORY_GRAPH = 'story_graph'
    FILES = 'files'
    BOTH = 'both'
