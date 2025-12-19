"""
Story Graph Nodes

Node hierarchy for story graphs with proper inheritance.
All nodes except Epic have sequential_order.
"""

from abc import ABC, abstractmethod
from typing import List, Iterator, Optional, Dict, Any, Union, TYPE_CHECKING
from dataclasses import dataclass, field
from pathlib import Path
import json

if TYPE_CHECKING:
    from .domain import DomainConcept, StoryUser
else:
    from .domain import DomainConcept, StoryUser


@dataclass
class StoryNode(ABC):
    """
    Base class for all story graph nodes.
    
    All nodes share:
    - name: The node's name (required)
    - children: List of child nodes (implemented by subclasses)
    - sequential_order: Optional ordering (None for Epic, set for others)
    - Iteration capability over children
    """
    
    name: str
    sequential_order: Optional[float] = None  # None for Epic, set for others
    
    def __post_init__(self):
        """Initialize node after dataclass creation."""
        self._children: List['StoryNode'] = []
    
    @property
    @abstractmethod
    def children(self) -> List['StoryNode']:
        """Get child nodes. Must be implemented by subclasses."""
        pass
    
    def __iter__(self) -> Iterator['StoryNode']:
        """Iterate over children for easy traversal."""
        return iter(self.children)
    
    def __repr__(self) -> str:
        order = f", order={self.sequential_order}" if self.sequential_order is not None else ""
        return f"{self.__class__.__name__}(name='{self.name}'{order})"


@dataclass
class Epic(StoryNode):
    """
    Represents an epic in the story graph.
    
    Epics do NOT have sequential_order (remains None).
    Children can be SubEpic or StoryGroup.
    """
    
    domain_concepts: Optional[List[DomainConcept]] = None
    
    def __post_init__(self):
        """Ensure Epic never has sequential_order."""
        super().__post_init__()
        if self.sequential_order is not None:
            self.sequential_order = None
        if self.domain_concepts is None:
            self.domain_concepts = []
        self._children: List['StoryNode'] = []
    
    @property
    def children(self) -> List['StoryNode']:
        """Epic children are SubEpics and StoryGroups."""
        return self._children
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Epic':
        """Construct Epic and all children from JSON dict."""
        # Build domain concepts
        domain_concepts = [
            DomainConcept.from_dict(dc) 
            for dc in data.get('domain_concepts', [])
        ]
        
        epic = cls(
            name=data.get('name', ''),
            domain_concepts=domain_concepts
        )
        
        # Build children recursively
        for sub_epic_data in data.get('sub_epics', []):
            sub_epic = SubEpic.from_dict(sub_epic_data, parent=epic)
            epic._children.append(sub_epic)
        
        for story_group_data in data.get('story_groups', []):
            story_group = StoryGroup.from_dict(story_group_data, parent=epic)
            epic._children.append(story_group)
        
        return epic


@dataclass
class SubEpic(StoryNode):
    """
    Represents a sub-epic (feature) in the story graph.
    
    SubEpics HAVE sequential_order (required).
    Children can be nested SubEpics or StoryGroups.
    """
    
    sequential_order: float  # Required for SubEpic (override base Optional)
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("SubEpic requires sequential_order")
        self._children: List['StoryNode'] = []
    
    @property
    def children(self) -> List['StoryNode']:
        """SubEpic children are nested SubEpics and StoryGroups."""
        return self._children
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], parent: Optional[StoryNode] = None) -> 'SubEpic':
        """Construct SubEpic and all children from JSON dict."""
        sequential_order = data.get('sequential_order')
        if sequential_order is None:
            raise ValueError("SubEpic requires sequential_order")
        
        sub_epic = cls(
            name=data.get('name', ''),
            sequential_order=float(sequential_order),
            _parent=parent
        )
        
        # Build children recursively
        for nested_sub_epic_data in data.get('sub_epics', []):
            nested_sub_epic = SubEpic.from_dict(nested_sub_epic_data, parent=sub_epic)
            sub_epic._children.append(nested_sub_epic)
        
        for story_group_data in data.get('story_groups', []):
            story_group = StoryGroup.from_dict(story_group_data, parent=sub_epic)
            sub_epic._children.append(story_group)
        
        return sub_epic


@dataclass
class StoryGroup(StoryNode):
    """
    Represents a group of stories with connection logic.
    
    StoryGroups HAVE sequential_order (required).
    Children are Stories.
    """
    
    sequential_order: float  # Required for StoryGroup
    group_type: str = "and"  # "and" (horizontal) or "or" (vertical)
    connector: Optional[str] = None  # "and", "or", "opt", or None
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("StoryGroup requires sequential_order")
        self._children: List['StoryNode'] = []
    
    @property
    def children(self) -> List['StoryNode']:
        """StoryGroup children are Stories."""
        return self._children
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], parent: Optional[StoryNode] = None) -> 'StoryGroup':
        """Construct StoryGroup and all children from JSON dict."""
        # StoryGroup might not have explicit sequential_order in JSON
        # Use a default if missing (will be ordered by position in list)
        sequential_order = data.get('sequential_order', 1.0)
        
        story_group = cls(
            name=data.get('name', ''),  # StoryGroups might not have names
            sequential_order=float(sequential_order),
            group_type=data.get('type', 'and'),
            connector=data.get('connector'),
            _parent=parent
        )
        
        # Build children (stories)
        for story_data in data.get('stories', []):
            story = Story.from_dict(story_data, parent=story_group)
            story_group._children.append(story)
        
        return story_group


@dataclass
class Story(StoryNode):
    """
    Represents a story with scenarios, scenario outlines, and acceptance criteria as child nodes.
    
    Stories HAVE sequential_order (required).
    """
    
    sequential_order: float  # Required for Story
    connector: Optional[str] = None
    story_type: str = "user"  # "user", "system", or "technical"
    users: Optional[List[StoryUser]] = None
    test_file: Optional[str] = None
    test_class: Optional[str] = None
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("Story requires sequential_order")
        if self.users is None:
            self.users = []
        self._children: List['StoryNode'] = []
    
    @property
    def children(self) -> List['StoryNode']:
        """Story children are Scenario, ScenarioOutline, and AcceptanceCriteria nodes."""
        return self._children
    
    @property
    def scenarios(self) -> List['Scenario']:
        """Get scenario child nodes."""
        return [child for child in self._children if isinstance(child, Scenario)]
    
    @property
    def scenario_outlines(self) -> List['ScenarioOutline']:
        """Get scenario outline child nodes."""
        return [child for child in self._children if isinstance(child, ScenarioOutline)]
    
    @property
    def acceptance_criteria(self) -> List['AcceptanceCriteria']:
        """Get acceptance criteria child nodes."""
        return [child for child in self._children if isinstance(child, AcceptanceCriteria)]
    
    @property
    def default_test_class(self) -> str:
        """Generate default test class name from story name."""
        if not self.name:
            return ""
        words = self.name.split()
        class_name = "".join(word.capitalize() for word in words)
        return f"Test{class_name}"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], parent: Optional[StoryNode] = None) -> 'Story':
        """Construct Story and all children from JSON dict."""
        sequential_order = data.get('sequential_order')
        if sequential_order is None:
            raise ValueError("Story requires sequential_order")
        
        # Build users
        users = [
            StoryUser.from_str(u)
            for u in data.get('users', [])
        ]
        
        story = cls(
            name=data.get('name', ''),
            sequential_order=float(sequential_order),
            connector=data.get('connector'),
            story_type=data.get('story_type', 'user'),
            users=users,
            test_file=data.get('test_file'),
            test_class=data.get('test_class'),
            _parent=parent
        )
        
        # Build acceptance criteria as child nodes
        acceptance_criteria_data = data.get('acceptance_criteria', [])
        for idx, ac_data in enumerate(acceptance_criteria_data):
            ac = AcceptanceCriteria.from_dict(ac_data, index=idx, parent=story)
            story._children.append(ac)
        
        # Build scenarios as child nodes
        scenarios_data = data.get('scenarios', [])
        for idx, scenario_data in enumerate(scenarios_data):
            scenario = Scenario.from_dict(scenario_data, index=idx, parent=story)
            story._children.append(scenario)
        
        # Build scenario outlines as child nodes
        scenario_outlines_data = data.get('scenario_outlines', [])
        for idx, scenario_outline_data in enumerate(scenario_outlines_data):
            scenario_outline = ScenarioOutline.from_dict(scenario_outline_data, index=idx, parent=story)
            story._children.append(scenario_outline)
        
        return story


@dataclass
class Scenario(StoryNode):
    """
    Represents a BDD scenario.
    
    Has Step nodes as children. Has sequential_order since it's not an Epic.
    """
    
    sequential_order: float  # Required (not Epic)
    type: str = ""
    background: List[str] = field(default_factory=list)
    test_method: Optional[str] = None
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("Scenario requires sequential_order")
        self._children: List['StoryNode'] = []
    
    @property
    def children(self) -> List['StoryNode']:
        """Scenario children are Step nodes."""
        return self._children
    
    @property
    def steps(self) -> List['Step']:
        """Get step child nodes."""
        return [child for child in self._children if isinstance(child, Step)]
    
    @property
    def default_test_method(self) -> str:
        """Generate default test method name from scenario name."""
        if not self.name:
            return ""
        words = self.name.split()
        method_name = "_".join(word.lower() for word in words)
        return f"test_{method_name}"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], index: int = 0, parent: Optional[StoryNode] = None) -> 'Scenario':
        """Construct Scenario and all children from JSON dict."""
        # Use index as sequential_order if not explicitly set
        sequential_order = float(data.get('sequential_order', index + 1))
        
        scenario = cls(
            name=data.get('name', ''),
            sequential_order=sequential_order,
            type=data.get('type', ''),
            background=data.get('background', []),
            test_method=data.get('test_method'),
            _parent=parent
        )
        
        # Build steps as child nodes
        steps_value = data.get('steps', '')
        if isinstance(steps_value, str):
            # Parse newline-separated steps
            step_strings = [s.strip() for s in steps_value.split('\n') if s.strip()]
        elif isinstance(steps_value, list):
            step_strings = steps_value
        else:
            step_strings = []
        
        for step_idx, step_text in enumerate(step_strings):
            step = Step(
                name=step_text,
                text=step_text,
                sequential_order=float(step_idx + 1),
                _parent=scenario
            )
            scenario._children.append(step)
        
        return scenario


@dataclass
class ScenarioOutline(StoryNode):
    """
    Represents a BDD scenario outline with examples.
    
    Has Step nodes as children. Has sequential_order since it's not an Epic.
    """
    
    sequential_order: float  # Required (not Epic)
    type: str = ""
    background: List[str] = field(default_factory=list)
    examples: Dict[str, Any] = field(default_factory=dict)
    test_method: Optional[str] = None
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("ScenarioOutline requires sequential_order")
        self._children: List['StoryNode'] = []
    
    @property
    def children(self) -> List['StoryNode']:
        """ScenarioOutline children are Step nodes."""
        return self._children
    
    @property
    def steps(self) -> List['Step']:
        """Get step child nodes."""
        return [child for child in self._children if isinstance(child, Step)]
    
    @property
    def examples_columns(self) -> List[str]:
        """Get example column names."""
        return self.examples.get('columns', [])
    
    @property
    def examples_rows(self) -> List[List[str]]:
        """Get example data rows."""
        return self.examples.get('rows', [])
    
    @property
    def default_test_method(self) -> str:
        """Generate default test method name from scenario outline name."""
        if not self.name:
            return ""
        words = self.name.split()
        method_name = "_".join(word.lower() for word in words)
        return f"test_{method_name}"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], index: int = 0, parent: Optional[StoryNode] = None) -> 'ScenarioOutline':
        """Construct ScenarioOutline and all children from JSON dict."""
        # Use index as sequential_order if not explicitly set
        sequential_order = float(data.get('sequential_order', index + 1))
        
        scenario_outline = cls(
            name=data.get('name', ''),
            sequential_order=sequential_order,
            type=data.get('type', ''),
            background=data.get('background', []),
            examples=data.get('examples', {}),
            test_method=data.get('test_method'),
            _parent=parent
        )
        
        # Build steps as child nodes
        steps_value = data.get('steps', '')
        if isinstance(steps_value, str):
            # Parse newline-separated steps
            step_strings = [s.strip() for s in steps_value.split('\n') if s.strip()]
        elif isinstance(steps_value, list):
            step_strings = steps_value
        else:
            step_strings = []
        
        for step_idx, step_text in enumerate(step_strings):
            step = Step(
                name=step_text,
                text=step_text,
                sequential_order=float(step_idx + 1),
                _parent=scenario_outline
            )
            scenario_outline._children.append(step)
        
        return scenario_outline


@dataclass
class AcceptanceCriteria(StoryNode):
    """
    Represents an acceptance criterion in the story graph.
    
    Leaf node (no children) but still part of the hierarchy.
    Has sequential_order since it's not an Epic.
    """
    
    sequential_order: float  # Required (not Epic)
    text: str  # The criterion text/description
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("AcceptanceCriteria requires sequential_order")
    
    @property
    def children(self) -> List['StoryNode']:
        """AcceptanceCriteria are leaf nodes - no children."""
        return []
    
    @classmethod
    def from_dict(cls, data: Union[str, Dict[str, Any]], index: int = 0, parent: Optional[StoryNode] = None) -> 'AcceptanceCriteria':
        """Construct AcceptanceCriteria from JSON dict or string."""
        if isinstance(data, str):
            # Simple string format - use index as order
            text = data
            sequential_order = float(index + 1)
        else:
            # Dict format with explicit sequential_order
            text = data.get('description', data.get('text', ''))
            sequential_order = float(data.get('sequential_order', index + 1))
        
        return cls(
            name=text,  # Use text as name for hierarchy consistency
            text=text,
            sequential_order=sequential_order,
            _parent=parent
        )


@dataclass
class Step(StoryNode):
    """
    Represents a step in a scenario or scenario outline.
    
    Leaf node (no children) at the bottom of the hierarchy.
    Has sequential_order since it's not an Epic.
    """
    
    sequential_order: float  # Required (not Epic)
    text: str  # The step text
    _parent: Optional[StoryNode] = field(default=None, repr=False)
    
    def __post_init__(self):
        """Ensure sequential_order is set."""
        super().__post_init__()
        if self.sequential_order is None:
            raise ValueError("Step requires sequential_order")
    
    @property
    def children(self) -> List['StoryNode']:
        """Steps are leaf nodes - no children."""
        return []


class StoryMap:
    """
    Top-level story map that constructs itself from story graph JSON.
    """
    
    def __init__(self, story_graph: Dict[str, Any]):
        """Construct the entire object model from story graph JSON."""
        self.story_graph = story_graph
        self._epics: List[Epic] = []
        
        # Build all epics, which build their children recursively
        for epic_data in story_graph.get('epics', []):
            self._epics.append(Epic.from_dict(epic_data))
    
    @classmethod
    def from_bot(cls, bot: Any) -> 'StoryMap':
        """Create StoryMap from bot object (finds story-graph.json)."""
        # Handle different bot object types
        if hasattr(bot, 'bot_paths') and hasattr(bot.bot_paths, 'bot_directory'):
            bot_directory = Path(bot.bot_paths.bot_directory)
        elif hasattr(bot, 'bot_directory'):
            bot_directory = Path(bot.bot_directory)
        elif isinstance(bot, (str, Path)):
            bot_directory = Path(bot)
        else:
            raise TypeError(f"Expected bot with bot_paths.bot_directory, bot_directory attribute, or Path/str, got {type(bot)}")
        
        story_graph_path = bot_directory / 'docs' / 'stories' / 'story-graph.json'
        
        if not story_graph_path.exists():
            raise FileNotFoundError(f"Story graph not found at {story_graph_path}")
        
        with open(story_graph_path, 'r', encoding='utf-8') as f:
            story_graph = json.load(f)
        
        return cls(story_graph)
    
    @property
    def epics(self) -> List[Epic]:
        """Get all epics."""
        return self._epics
    
    def walk(self, node: StoryNode) -> Iterator[StoryNode]:
        """Walk the tree starting from a node."""
        yield node
        for child in node.children:
            yield from self.walk(child)

