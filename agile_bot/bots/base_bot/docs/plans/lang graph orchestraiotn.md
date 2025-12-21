# BaseBot → LangGraph Integration Plan

## Objective

Integrate **LangGraph** into **BaseBot** as a hidden orchestration layer.  
LangGraph becomes the execution engine that drives behavior workflows, with **StoryBot** (and future bots) providing declarative configuration.

---

## Current Architecture

### BaseBot (Engine) — All Python Code

```
agile_bot/bots/base_bot/
├── src/
│   ├── bot/                       # Bot framework
│   │   ├── bot.py                 # Bot class - loads config, manages behaviors
│   │   ├── behavior.py            # Behavior class - loads behavior.json
│   │   ├── behaviors.py           # Behaviors collection
│   │   ├── bot_paths.py           # BotPaths - path resolution
│   │   ├── workspace.py           # Workspace utilities
│   │   ├── trigger_words.py       # Trigger word matching
│   │   └── reminders.py           # Next action/behavior reminders
│   │
│   ├── actions/                   # Action implementations
│   │   ├── action.py              # Base Action class
│   │   ├── actions.py             # Actions collection (workflow management)
│   │   ├── action_factory.py      # Dynamic action instantiation
│   │   ├── action_state_manager.py # behavior_action_state.json management
│   │   ├── activity_tracker.py    # activity_log.json (TinyDB)
│   │   ├── instructions.py        # Instructions builder
│   │   ├── workflow_status_builder.py # Status breadcrumbs
│   │   │
│   │   ├── build/                 # BuildKnowledgeAction
│   │   ├── clarify/               # ClarifyContextAction
│   │   ├── render/                # RenderOutputAction
│   │   ├── strategy/              # StrategyAction
│   │   └── validate/              # ValidateRulesAction
│   │
│   ├── cli/                       # CLI framework
│   │   ├── base_bot_cli.py        # BaseBotCli main class
│   │   ├── cli_executor.py        # Command execution
│   │   ├── cli_command_router.py  # Route to behavior/action
│   │   └── cli_parameter_parser.py # Argument parsing
│   │
│   └── story_graph/               # Story graph utilities
│
└── base_actions/                  # Base action JSON configs
    ├── build/action_config.json
    ├── clarify/action_config.json
    ├── render/action_config.json
    ├── strategy/action_config.json
    └── validate/action_config.json
```

### StoryBot (Declarative Configuration) — No Python Code

```
agile_bot/bots/story_bot/
├── bot_config.json                # Bot-level: behaviors list, instructions, MCP config
│
└── behaviors/                     # Per-behavior declarations
    ├── shape/
    │   ├── behavior.json          # Workflow: actions_workflow, trigger_words
    │   ├── content/               # Templates, knowledge graph specs
    │   │   ├── knowledge_graph/   # Build templates
    │   │   ├── render/            # Render configs
    │   │   └── synchronize/       # Sync configs
    │   ├── guardrails/            # Context injection
    │   │   ├── required_context/  # evidence.json, key_questions.json
    │   │   ├── planning/          # assumptions, decision_criteria
    │   │   └── strategy/          # strategy configs
    │   └── rules/                 # Validation rules (*.json)
    │
    ├── discovery/
    ├── exploration/
    ├── prioritization/
    ├── scenarios/
    ├── tests/
    └── code/
```

### Key Relationships

| Component | Location | Responsibility |
|-----------|----------|----------------|
| **Bot** | `base_bot/src/bot/bot.py` | Loads bot_config.json, creates Behaviors |
| **Behaviors** | `base_bot/src/bot/behaviors.py` | Collection of Behavior instances |
| **Behavior** | `base_bot/src/bot/behavior.py` | Loads behavior.json, creates Actions |
| **Actions** | `base_bot/src/actions/actions.py` | Manages workflow, state, navigation |
| **ActionFactory** | `base_bot/src/actions/action_factory.py` | Dynamically loads action classes |
| **Action** | `base_bot/src/actions/action.py` | Base class: execute() → do_execute() |

---

## Existing State Management

### Current State Files

| File | Location | Purpose | Managed By |
|------|----------|---------|------------|
| `behavior_action_state.json` | `<workspace>/` | Current behavior/action, completed actions | `ActionStateManager` |
| `activity_log.json` | `<workspace>/` | Action start/complete timestamps (TinyDB) | `ActivityTracker` |
| `story-graph.json` | `<workspace>/docs/stories/` | Main knowledge graph | Actions |
| `context/` | `<workspace>/docs/stories/context/` | Session context files | `ContextDataInjector` |
| `guardrails/` | Per-behavior | Clarification, strategy data | `Guardrails` class |

### behavior_action_state.json Structure

```json
{
  "current_behavior": "story_bot.discovery",
  "current_action": "story_bot.discovery.build",
  "completed_actions": [
    {
      "action_state": "story_bot.discovery.clarify",
      "timestamp": "2025-12-20T10:30:00"
    },
    {
      "action_state": "story_bot.discovery.strategy",
      "timestamp": "2025-12-20T10:45:00"
    }
  ],
  "timestamp": "2025-12-20T11:00:00"
}
```

### activity_log.json Structure (TinyDB)

```json
{
  "_default": {
    "1": {"action_state": "story_bot.discovery.clarify", "status": "started", "timestamp": "..."},
    "2": {"action_state": "story_bot.discovery.clarify", "status": "completed", "timestamp": "...", "outputs": {...}}
  }
}
```

---

## Current Execution Flow

```
1. CLI: story_bot_cli --behavior discovery --action build

2. BaseBotCli.main()
   → CliCommandRouter.route(args)
   → CliExecutor.execute_and_output(args, params)

3. Bot.__init__(bot_name, bot_directory, config_path)
   → Loads bot_config.json
   → Creates Behaviors collection
   → Each Behavior loads behavior.json

4. Behavior.actions → Actions.__init__(behavior)
   → Reads actions_workflow from behavior.json
   → ActionFactory.create_action_instance() for each action
   → ActionStateManager.load_state() → sets current action

5. Actions.navigate_to("build")
   → Sets _current_index
   → ActionStateManager.save_state()

6. Action.execute(parameters)
   → ActivityTracker.track_start()
   → do_execute(parameters) → Returns instructions dict
   → ActivityTracker.track_completion()

7. CliExecutor._output_result(result)
   → Prints JSON + base_instructions for AI to execute
```

---

## LangGraph Integration Point

### Where LangGraph Fits

LangGraph replaces the manual workflow orchestration in `Actions` class.  
Instead of `Actions.navigate_to()` → `Action.execute()` → `Actions.close_current()`,  
LangGraph orchestrates the flow with automatic checkpointing.

```
Current:  Actions.navigate_to() → Action.execute() → Actions.close_current()
                    ↓                    ↓                    ↓
          ActionStateManager    ActivityTracker      ActionStateManager

With LangGraph:
          LangGraph.execute(graph)
                    ↓
          Node 1: clarify → checkpoint
                    ↓
          Node 2: strategy → checkpoint
                    ↓
          Node 3: build → checkpoint
                    ↓
          Node 4: validate → checkpoint
```

### What Changes

| Current | With LangGraph |
|---------|----------------|
| `Actions` manages workflow order | LangGraph graph defines order |
| `ActionStateManager` tracks current/completed | LangGraph checkpoints replace this |
| `ActivityTracker` logs start/complete | Preserved, called from nodes |
| `Actions.close_current()` advances workflow | LangGraph auto-advances on node completion |

### What Stays the Same

| Component | Status |
|-----------|--------|
| `Action.execute()` / `do_execute()` | Unchanged — becomes node body |
| `Behavior` loading from behavior.json | Unchanged — feeds graph builder |
| `Bot` and `Behaviors` | Unchanged |
| `story-graph.json` and all state files | Unchanged — adapter wraps them |
| CLI interface | Unchanged — hidden orchestration |

---

## Implementation Plan

### New Directory Structure

```
agile_bot/bots/base_bot/src/
├── orchestration/                  # NEW: LangGraph integration
│   ├── __init__.py
│   ├── state_adapter.py            # Wraps existing state files
│   ├── graph_builder.py            # Builds graph from behavior.json
│   ├── runner.py                   # LangGraph execution + checkpointing
│   └── action_nodes.py             # Wraps Action classes as graph nodes
│
├── bot/                            # Existing (unchanged)
├── actions/                        # Existing (unchanged)
└── cli/                            # Existing (unchanged)
```

### Step 1: BaseBotStateAdapter

Wraps existing state files into a single LangGraph-compatible state object.

```python
# base_bot/src/orchestration/state_adapter.py

from pathlib import Path
from typing import Dict, Any, Optional
import json
from tinydb import TinyDB

class BaseBotStateAdapter:
    """Wraps BaseBot's existing state files for LangGraph orchestration."""
    
    def __init__(self, bot_paths):
        self.bot_paths = bot_paths
        self.workspace = bot_paths.workspace_directory
        self._state = None
    
    @property
    def state(self) -> Dict[str, Any]:
        if self._state is None:
            self._state = self._load_state()
        return self._state
    
    def _load_state(self) -> Dict[str, Any]:
        return {
            # From behavior_action_state.json
            "workflow_state": self._load_workflow_state(),
            
            # From story-graph.json
            "story_graph": self._load_story_graph(),
            
            # From activity_log.json
            "activity_log": self._load_activity_log(),
            
            # Context files
            "context": self._collect_context(),
            
            # Runtime mode
            "mode": "interactive",  # or "autonomous"
        }
    
    def _load_workflow_state(self) -> Optional[Dict]:
        path = self.workspace / "behavior_action_state.json"
        if path.exists():
            return json.loads(path.read_text(encoding='utf-8'))
        return None
    
    def _load_story_graph(self) -> Optional[Dict]:
        path = self.workspace / "docs/stories/story-graph.json"
        if path.exists():
            return json.loads(path.read_text(encoding='utf-8'))
        return None
    
    def _load_activity_log(self) -> list:
        path = self.workspace / "activity_log.json"
        if path.exists():
            with TinyDB(path) as db:
                return db.all()
        return []
    
    def _collect_context(self) -> Dict[str, Any]:
        context_dir = self.workspace / "docs/stories/context"
        return {
            "path": str(context_dir),
            "files": [str(f) for f in context_dir.glob("*")] if context_dir.exists() else []
        }
    
    def to_dict(self) -> Dict[str, Any]:
        return self.state
    
    def update_workflow_state(self, current_action: str, completed: list):
        """Update workflow state after action completion."""
        self._state["workflow_state"] = {
            "current_action": current_action,
            "completed_actions": completed
        }
    
    def persist(self):
        """Write modified state back to files."""
        # Workflow state is handled by LangGraph checkpoints
        # Story graph persisted by actions themselves
        pass
```

### Step 2: BehaviorGraphBuilder

Reads `behavior.json` and builds a LangGraph from `actions_workflow`.

```python
# base_bot/src/orchestration/graph_builder.py

from typing import Dict, Any, List, Callable
from langgraph.graph import StateGraph

class BehaviorGraphBuilder:
    """Builds LangGraph from behavior.json actions_workflow."""
    
    def __init__(self, behavior):
        self.behavior = behavior
        self.behavior_config = behavior._config
        self.actions_workflow = self.behavior_config.get("actions_workflow", {})
    
    def build_graph(self, node_executors: Dict[str, Callable]) -> StateGraph:
        """Build StateGraph from actions_workflow.
        
        Args:
            node_executors: Map action names to executor functions
                           {"clarify": run_clarify, "build": run_build, ...}
        
        Returns:
            Configured StateGraph ready to compile
        """
        # Define state schema
        from typing import TypedDict, Annotated
        from operator import add
        
        class WorkflowState(TypedDict):
            story_graph: dict
            workflow_state: dict
            current_action: str
            completed_actions: Annotated[list, add]
            instructions: dict
        
        graph = StateGraph(WorkflowState)
        
        # Get sorted actions from workflow
        actions = self.actions_workflow.get("actions", [])
        sorted_actions = sorted(actions, key=lambda a: a.get("order", 0))
        
        # Add nodes
        for action_config in sorted_actions:
            action_name = action_config["name"]
            if action_name in node_executors:
                graph.add_node(action_name, node_executors[action_name])
        
        # Add edges based on next_action
        for i, action_config in enumerate(sorted_actions):
            action_name = action_config["name"]
            next_action = action_config.get("next_action")
            
            if next_action and next_action in node_executors:
                graph.add_edge(action_name, next_action)
            elif i == len(sorted_actions) - 1:
                # Last action goes to END
                from langgraph.graph import END
                graph.add_edge(action_name, END)
        
        # Set entry point
        if sorted_actions:
            from langgraph.graph import START
            graph.add_edge(START, sorted_actions[0]["name"])
        
        return graph
    
    def get_action_order(self) -> List[str]:
        """Return action names in workflow order."""
        actions = self.actions_workflow.get("actions", [])
        sorted_actions = sorted(actions, key=lambda a: a.get("order", 0))
        return [a["name"] for a in sorted_actions]
```

### Step 3: Action Node Wrappers

Wraps existing Action classes as LangGraph node functions.

```python
# base_bot/src/orchestration/action_nodes.py

from typing import Dict, Any, Callable
from agile_bot.bots.base_bot.src.actions.action_factory import ActionFactory

def create_node_executors(behavior) -> Dict[str, Callable]:
    """Create LangGraph node executors from existing Action classes.
    
    Each node executor:
    1. Gets the Action instance from ActionFactory
    2. Calls action.execute(parameters)
    3. Updates state with results
    4. Returns updated state for next node
    """
    factory = ActionFactory(behavior)
    
    def make_node_executor(action_name: str, action_config: dict):
        def node_executor(state: Dict[str, Any]) -> Dict[str, Any]:
            # Create action instance
            action = factory.create_action_instance(
                action_name=action_name,
                action_config=action_config
            )
            
            # Execute action (this calls track_start, do_execute, track_completion)
            parameters = state.get("parameters", {})
            result = action.execute(parameters)
            
            # Update state
            return {
                "current_action": action_name,
                "completed_actions": [action_name],
                "instructions": result.get("instructions", {})
            }
        
        return node_executor
    
    # Build executors for all actions in workflow
    actions_workflow = behavior._config.get("actions_workflow", {})
    actions = actions_workflow.get("actions", [])
    
    executors = {}
    for action_config in actions:
        action_name = action_config["name"]
        executors[action_name] = make_node_executor(action_name, action_config)
    
    return executors
```

### Step 4: LangGraphRunner

Hidden orchestration layer with checkpointing.

```python
# base_bot/src/orchestration/runner.py

from pathlib import Path
from typing import Dict, Any, Optional
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph

class LangGraphRunner:
    """Hidden LangGraph orchestration inside BaseBot."""
    
    def __init__(self, bot_paths):
        self.bot_paths = bot_paths
        self.workspace = bot_paths.workspace_directory
        self.checkpoint_dir = self.workspace / ".graph"
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)
        
        # SQLite checkpoint store
        self.checkpointer = SqliteSaver.from_conn_string(
            str(self.checkpoint_dir / "checkpoints.db")
        )
    
    def run(
        self,
        graph: StateGraph,
        initial_state: Dict[str, Any],
        start_action: Optional[str] = None,
        thread_id: str = "default"
    ) -> Dict[str, Any]:
        """Execute workflow graph.
        
        Args:
            graph: Compiled StateGraph from BehaviorGraphBuilder
            initial_state: Initial state from BaseBotStateAdapter
            start_action: Optional action to start/resume from
            thread_id: Unique ID for this workflow run
        
        Returns:
            Final state after all nodes complete
        """
        # Compile graph with checkpointing
        compiled = graph.compile(checkpointer=self.checkpointer)
        
        # Run graph
        config = {"configurable": {"thread_id": thread_id}}
        
        if start_action:
            # Resume from specific action
            result = compiled.invoke(
                initial_state,
                config=config,
                start_at=start_action
            )
        else:
            result = compiled.invoke(initial_state, config=config)
        
        return result
    
    def get_state(self, thread_id: str = "default") -> Optional[Dict[str, Any]]:
        """Get current state for a thread (for resume)."""
        config = {"configurable": {"thread_id": thread_id}}
        return self.checkpointer.get(config)
    
    def list_checkpoints(self, thread_id: str = "default") -> list:
        """List all checkpoints for a thread."""
        config = {"configurable": {"thread_id": thread_id}}
        return list(self.checkpointer.list(config))
```

### Step 5: Integration with Behavior Class

Modify `Behavior` to optionally use LangGraph.

```python
# Modification to base_bot/src/bot/behavior.py

class Behavior:
    # ... existing code ...
    
    def execute_with_langgraph(
        self,
        action_name: str = None,
        parameters: Dict[str, Any] = None,
        thread_id: str = None
    ) -> Dict[str, Any]:
        """Execute behavior using LangGraph orchestration.
        
        This is the NEW execution path that uses LangGraph internally.
        The existing execute path remains for backwards compatibility.
        """
        from agile_bot.bots.base_bot.src.orchestration.state_adapter import BaseBotStateAdapter
        from agile_bot.bots.base_bot.src.orchestration.graph_builder import BehaviorGraphBuilder
        from agile_bot.bots.base_bot.src.orchestration.action_nodes import create_node_executors
        from agile_bot.bots.base_bot.src.orchestration.runner import LangGraphRunner
        
        # 1. Load current state
        state_adapter = BaseBotStateAdapter(self.bot_paths)
        initial_state = state_adapter.to_dict()
        initial_state["parameters"] = parameters or {}
        
        # 2. Build graph from behavior.json
        graph_builder = BehaviorGraphBuilder(self)
        node_executors = create_node_executors(self)
        graph = graph_builder.build_graph(node_executors)
        
        # 3. Run via LangGraph
        runner = LangGraphRunner(self.bot_paths)
        thread_id = thread_id or f"{self.bot_name}.{self.name}"
        
        result = runner.run(
            graph=graph,
            initial_state=initial_state,
            start_action=action_name,
            thread_id=thread_id
        )
        
        return result
```

---

## Checkpoint Structure

### Directory Layout

```
<workspace>/
├── docs/stories/
│   ├── story-graph.json           # Main knowledge graph (unchanged)
│   └── context/                    # Session context (unchanged)
├── behavior_action_state.json      # Can be deprecated (LangGraph replaces)
├── activity_log.json               # Preserved (ActivityTracker still works)
└── .graph/
    └── checkpoints.db              # SQLite checkpoint database
```

### Checkpoint Content

Each checkpoint contains:
- Full workflow state snapshot
- Current node (action) completed
- Thread ID for resume
- Timestamp

```python
# Example checkpoint data (stored in SQLite)
{
    "thread_id": "story_bot.discovery",
    "checkpoint_id": "abc123",
    "parent_checkpoint_id": "xyz789",
    "channel_values": {
        "story_graph": {...},
        "current_action": "build",
        "completed_actions": ["clarify", "strategy", "build"],
        "instructions": {...}
    },
    "metadata": {
        "step": 3,
        "timestamp": "2025-12-20T15:02:45Z"
    }
}
```

---

## Migration Strategy

### Phase 1: Add LangGraph Alongside Existing

1. Create `src/orchestration/` module
2. Add `execute_with_langgraph()` to Behavior
3. Both paths work — CLI can choose

### Phase 2: Feature Flag

```python
# In bot_config.json
{
    "orchestration": {
        "use_langgraph": true,
        "checkpoint_enabled": true
    }
}
```

### Phase 3: Replace Default

1. CLI uses LangGraph by default
2. Deprecate `ActionStateManager`
3. Keep `ActivityTracker` for logging

---

## Architecture Decisions

1. **LangGraph lives in BaseBot** — StoryBot and other bots remain purely declarative
2. **Existing Action classes unchanged** — they become node bodies
3. **behavior.json drives the graph** — `actions_workflow` defines node order
4. **SQLite checkpointing** — persistent, inspectable, supports resume
5. **Thread-based isolation** — each behavior run gets its own thread_id
6. **ActivityTracker preserved** — continues logging start/complete events
7. **Backwards compatible** — existing execution path remains available

---

## File Deliverables

| File | Location | Purpose |
|------|----------|---------|
| `state_adapter.py` | `src/orchestration/` | Wraps existing state files |
| `graph_builder.py` | `src/orchestration/` | Builds graph from behavior.json |
| `action_nodes.py` | `src/orchestration/` | Wraps Action classes as nodes |
| `runner.py` | `src/orchestration/` | LangGraph execution + checkpoints |
| `checkpoints.db` | `<workspace>/.graph/` | SQLite checkpoint storage |

---

## Result

- **StoryBot remains purely declarative** — behavior.json, rules/, content/
- **BaseBot gains LangGraph orchestration** — hidden under `src/orchestration/`
- **Existing action code unchanged** — Action.execute() becomes node body
- **CLI experience unchanged** — `story_bot_cli --behavior discovery --action build`
- **New capabilities**: checkpoint/resume, branch experiments, temporal debugging
- **Backwards compatible** — existing execution path preserved during migration
