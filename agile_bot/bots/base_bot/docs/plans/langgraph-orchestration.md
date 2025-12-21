# BaseBot → LangGraph Integration Plan

> ⚠️ **DRAFT — PRELIMINARY IDEAS ONLY**
>
> This document captures initial architectural thinking and rough ideas for integrating LangGraph.  
> **All code examples are suggestions** — they are illustrative, not production-ready.
>
> **Before implementation, this plan requires:**
> 1. **Shape** — Define the problem boundaries and key trade-offs
> 2. **Discovery** — Elaborate domain concepts, responsibilities, and collaborations  
> 3. **Exploration** — Define acceptance criteria and scenarios
>
> The class names, file locations, method signatures, and overall structure will likely change  
> significantly through proper story work. Do not implement directly from this document.

---

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
│   │   ├── action_state_manager.py # REMOVE - replaced by LangGraph
│   │   ├── activity_tracker.py    # REMOVE - replaced by LangGraph
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
| **Actions** | `base_bot/src/actions/actions.py` | Manages workflow, navigation |
| **ActionFactory** | `base_bot/src/actions/action_factory.py` | Dynamically loads action classes |
| **Action** | `base_bot/src/actions/action.py` | Base class: execute() → do_execute() |

---

## Files to Remove (Replaced by LangGraph)

| File | Current Purpose | Replacement |
|------|-----------------|-------------|
| `action_state_manager.py` | Tracks current/completed actions | LangGraph checkpoints |
| `activity_tracker.py` | Logs start/complete timestamps | LangGraph checkpoint history |
| `behavior_action_state.json` | Workflow state file | LangGraph checkpoint DB |
| `activity_log.json` | TinyDB activity log | LangGraph checkpoint history |

**Why remove?** LangGraph checkpoints provide:
- Full state snapshots (not just "action started/completed")
- Resume capability from any checkpoint
- Temporal history with metadata
- Thread-based isolation

---

## State Files (Keep)

| File | Location | Purpose |
|------|----------|---------|
| `story-graph.json` | `<workspace>/docs/stories/` | Main knowledge graph |
| `context/` | `<workspace>/docs/stories/context/` | Session context files |
| `guardrails/` | Per-behavior | Clarification, strategy data |

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

5. Action.execute(parameters)
   → do_execute(parameters) → Returns instructions dict

6. CliExecutor._output_result(result)
   → Prints JSON + base_instructions for AI to execute
```

---

## New Execution Flow (With LangGraph)

```
1. CLI: story_bot_cli --behavior discovery --action build

2. BaseBotCli routes to LangGraphRunner

3. LangGraphRunner:
   → Loads state from checkpoint (if resuming) or creates fresh state
   → Builds graph from behavior.json actions_workflow
   → Executes graph starting at specified action

4. Graph execution:
   Node: clarify → checkpoint saved
   Node: strategy → checkpoint saved
   Node: build → checkpoint saved    ← User requested this action
   Node: validate → checkpoint saved

5. Each node:
   → ActionFactory creates Action instance
   → Action.do_execute(parameters)
   → Returns instructions for AI

6. Checkpoint contains:
   → Full state after each action
   → Can resume from any point
   → History of all actions with timestamps
```

---

## Implementation Plan

> **Note:** The code below is conceptual scaffolding to illustrate the integration approach.  
> Class responsibilities, method signatures, and file organization will be refined through  
> proper shaping and discovery before any implementation begins.

### New Directory Structure

```
agile_bot/bots/base_bot/src/
├── orchestration/                  # NEW: LangGraph integration
│   ├── __init__.py
│   ├── state_adapter.py            # Wraps story-graph.json and context
│   ├── graph_builder.py            # Builds graph from behavior.json
│   ├── runner.py                   # LangGraph execution + checkpointing
│   └── action_nodes.py             # Wraps Action classes as graph nodes
│
├── bot/                            # Keep (unchanged)
├── actions/                        # Keep (simplified - remove tracker/state_manager)
└── cli/                            # Keep (routes to LangGraphRunner)
```

### Step 1: BaseBotStateAdapter

Wraps the essential state files (story-graph, context) for LangGraph.

```python
# base_bot/src/orchestration/state_adapter.py

from pathlib import Path
from typing import Dict, Any, Optional
import json

class BaseBotStateAdapter:
    """Wraps BaseBot's state files for LangGraph orchestration.
    
    Only wraps the ESSENTIAL state:
    - story-graph.json (knowledge graph)
    - context files
    
    Workflow state (current action, completed actions) is handled
    entirely by LangGraph checkpoints - no separate files needed.
    """
    
    def __init__(self, bot_paths):
        self.bot_paths = bot_paths
        self.workspace = bot_paths.workspace_directory
    
    def load_initial_state(self) -> Dict[str, Any]:
        """Load initial state for a workflow run."""
        return {
            # Main knowledge graph
            "story_graph": self._load_story_graph(),
            
            # Context files
            "context": self._collect_context(),
            
            # Runtime config
            "mode": "interactive",  # or "autonomous"
            
            # Parameters passed from CLI
            "parameters": {},
            
            # Will be populated by nodes
            "current_action": None,
            "completed_actions": [],
            "instructions": {},
        }
    
    def _load_story_graph(self) -> Optional[Dict]:
        path = self.workspace / "docs/stories/story-graph.json"
        if path.exists():
            return json.loads(path.read_text(encoding='utf-8'))
        return None
    
    def _collect_context(self) -> Dict[str, Any]:
        context_dir = self.workspace / "docs/stories/context"
        return {
            "path": str(context_dir),
            "files": [str(f) for f in context_dir.glob("*")] if context_dir.exists() else []
        }
```

### Step 2: BehaviorGraphBuilder

Reads `behavior.json` and builds a LangGraph from `actions_workflow`.

```python
# base_bot/src/orchestration/graph_builder.py

from typing import Dict, Any, List, Callable
from langgraph.graph import StateGraph, START, END

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
        from typing import TypedDict, Annotated
        from operator import add
        
        class WorkflowState(TypedDict):
            story_graph: dict
            context: dict
            mode: str
            parameters: dict
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
                graph.add_edge(action_name, END)
        
        # Set entry point
        if sorted_actions:
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
**Note:** Actions are simplified — no ActivityTracker calls.

```python
# base_bot/src/orchestration/action_nodes.py

from typing import Dict, Any, Callable
from agile_bot.bots.base_bot.src.actions.action_factory import ActionFactory

def create_node_executors(behavior) -> Dict[str, Callable]:
    """Create LangGraph node executors from existing Action classes.
    
    Each node executor:
    1. Creates Action instance via ActionFactory
    2. Calls action.do_execute(parameters) directly
    3. Returns state update for LangGraph
    
    NOTE: We call do_execute() directly, NOT execute().
    The execute() method contains ActivityTracker calls which we're removing.
    LangGraph checkpoints replace activity tracking.
    """
    factory = ActionFactory(behavior)
    
    def make_node_executor(action_name: str, action_config: dict):
        def node_executor(state: Dict[str, Any]) -> Dict[str, Any]:
            # Create action instance
            action = factory.create_action_instance(
                action_name=action_name,
                action_config=action_config
            )
            
            # Execute action logic directly (skip ActivityTracker)
            parameters = state.get("parameters", {})
            result = action.do_execute(parameters)
            
            # Return state update
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

The core orchestration layer with checkpointing.

```python
# base_bot/src/orchestration/runner.py

from pathlib import Path
from typing import Dict, Any, Optional, List
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph

class LangGraphRunner:
    """LangGraph orchestration for BaseBot.
    
    Provides:
    - Workflow execution with automatic checkpointing
    - Resume from any checkpoint
    - History/audit via checkpoint listing
    - Thread-based isolation for parallel workflows
    """
    
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
            graph: StateGraph from BehaviorGraphBuilder
            initial_state: Initial state from BaseBotStateAdapter
            start_action: Optional action to start/resume from
            thread_id: Unique ID for this workflow run
        
        Returns:
            Final state after execution
        """
        # Compile graph with checkpointing
        compiled = graph.compile(checkpointer=self.checkpointer)
        
        config = {"configurable": {"thread_id": thread_id}}
        
        if start_action:
            # Resume from specific action
            result = compiled.invoke(
                initial_state,
                config=config,
                interrupt_before=[start_action]
            )
        else:
            result = compiled.invoke(initial_state, config=config)
        
        return result
    
    def get_current_state(self, thread_id: str) -> Optional[Dict[str, Any]]:
        """Get current state for a thread (for status display)."""
        config = {"configurable": {"thread_id": thread_id}}
        snapshot = self.checkpointer.get(config)
        return snapshot.values if snapshot else None
    
    def list_history(self, thread_id: str) -> List[Dict[str, Any]]:
        """List checkpoint history for a thread.
        
        This replaces ActivityTracker - provides complete audit trail.
        """
        config = {"configurable": {"thread_id": thread_id}}
        checkpoints = list(self.checkpointer.list(config))
        
        history = []
        for cp in checkpoints:
            history.append({
                "checkpoint_id": cp.config["configurable"]["checkpoint_id"],
                "step": cp.metadata.get("step", 0),
                "current_action": cp.values.get("current_action"),
                "completed_actions": cp.values.get("completed_actions", []),
                "timestamp": cp.metadata.get("created_at"),
            })
        
        return history
    
    def resume_from(
        self,
        graph: StateGraph,
        thread_id: str,
        checkpoint_id: str
    ) -> Dict[str, Any]:
        """Resume workflow from a specific checkpoint."""
        compiled = graph.compile(checkpointer=self.checkpointer)
        
        config = {
            "configurable": {
                "thread_id": thread_id,
                "checkpoint_id": checkpoint_id
            }
        }
        
        return compiled.invoke(None, config=config)
```

### Step 5: Simplified Action Base Class

Remove ActivityTracker and ActionStateManager from the Action class.

```python
# Modifications to base_bot/src/actions/action.py

class Action:
    """Simplified Action base class.
    
    REMOVED:
    - ActivityTracker (replaced by LangGraph checkpoints)
    - ActionStateManager references
    - track_activity_on_start()
    - track_activity_on_completion()
    
    KEPT:
    - do_execute() - core action logic
    - instructions property
    - behavior/bot_paths references
    """
    
    def __init__(self, behavior, action_config=None, action_name=None):
        self.behavior = behavior
        self.action_config = action_config
        self._action_name = action_name or self._derive_action_name_from_class()
        self._base_config = self._load_base_config()
        if action_config:
            self._apply_action_config()
        self._initialize_properties()
    
    # ... keep existing config loading ...
    
    def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Execute action logic. Subclasses implement this."""
        raise NotImplementedError("Subclasses must implement do_execute()")
    
    # REMOVED: execute() wrapper - LangGraph handles orchestration
    # REMOVED: track_activity_on_start()
    # REMOVED: track_activity_on_completion()
```

### Step 6: Integration Point (CLI)

Route CLI to LangGraphRunner.

```python
# Modification to cli_executor.py or base_bot_cli.py

def run_with_langgraph(behavior_name: str, action_name: str, params: dict):
    """Execute via LangGraph orchestration."""
    from agile_bot.bots.base_bot.src.orchestration.state_adapter import BaseBotStateAdapter
    from agile_bot.bots.base_bot.src.orchestration.graph_builder import BehaviorGraphBuilder
    from agile_bot.bots.base_bot.src.orchestration.action_nodes import create_node_executors
    from agile_bot.bots.base_bot.src.orchestration.runner import LangGraphRunner
    
    # Get behavior
    behavior = bot.behaviors.find_by_name(behavior_name)
    
    # Build initial state
    adapter = BaseBotStateAdapter(behavior.bot_paths)
    initial_state = adapter.load_initial_state()
    initial_state["parameters"] = params
    
    # Build graph
    builder = BehaviorGraphBuilder(behavior)
    executors = create_node_executors(behavior)
    graph = builder.build_graph(executors)
    
    # Run
    runner = LangGraphRunner(behavior.bot_paths)
    thread_id = f"{behavior.bot_name}.{behavior.name}"
    
    result = runner.run(
        graph=graph,
        initial_state=initial_state,
        start_action=action_name,
        thread_id=thread_id
    )
    
    return result
```

---

## Workspace Structure (After Migration)

```
<workspace>/
├── docs/stories/
│   ├── story-graph.json           # Main knowledge graph (unchanged)
│   └── context/                    # Session context (unchanged)
│
└── .graph/
    └── checkpoints.db              # SQLite - ALL workflow state lives here
```

**Removed:**
- `behavior_action_state.json`
- `activity_log.json`

---

## LangGraph Checkpoint Provides Everything

### What Was in behavior_action_state.json

```json
{
  "current_behavior": "story_bot.discovery",
  "current_action": "story_bot.discovery.build",
  "completed_actions": [...]
}
```

**Now in checkpoint:**
```python
runner.get_current_state("story_bot.discovery")
# Returns: {"current_action": "build", "completed_actions": ["clarify", "strategy"], ...}
```

### What Was in activity_log.json

```json
{"action_state": "story_bot.discovery.clarify", "status": "completed", "timestamp": "..."}
```

**Now in checkpoint history:**
```python
runner.list_history("story_bot.discovery")
# Returns: [
#   {"step": 1, "current_action": "clarify", "timestamp": "..."},
#   {"step": 2, "current_action": "strategy", "timestamp": "..."},
#   {"step": 3, "current_action": "build", "timestamp": "..."},
# ]
```

---

## Files to Delete

| File | Reason |
|------|--------|
| `src/actions/activity_tracker.py` | Replaced by `runner.list_history()` |
| `src/actions/action_state_manager.py` | Replaced by LangGraph checkpoints |
| References in `action.py` to tracker | Simplify to just `do_execute()` |
| References in `actions.py` to state manager | LangGraph handles state |

---

## Architecture Decisions (Preliminary)

> These are initial decisions based on exploration of the codebase and LangGraph capabilities.  
> Each decision should be validated through proper discovery and may change.

1. **LangGraph handles ALL workflow state** — no separate state files
2. **Remove ActivityTracker entirely** — checkpoint history is better
3. **Remove ActionStateManager entirely** — checkpoint state is better
4. **Remove behavior_action_state.json** — redundant
5. **Remove activity_log.json** — redundant
6. **Action.do_execute() is the core** — no tracking wrapper needed
7. **Single source of truth** — `.graph/checkpoints.db`

### Open Questions (To Address in Discovery)

- How does LangGraph handle human-in-the-loop vs autonomous execution?
- What's the right granularity for checkpoints — per action or more fine-grained?
- How do we handle parallel behavior runs (multiple stories in progress)?
- Should the graph be built once at startup or dynamically per invocation?
- How do we migrate existing state files during transition?
- What's the rollback strategy if LangGraph integration fails?

---

## File Deliverables

| File | Location | Purpose |
|------|----------|---------|
| `state_adapter.py` | `src/orchestration/` | Wraps story-graph and context |
| `graph_builder.py` | `src/orchestration/` | Builds graph from behavior.json |
| `action_nodes.py` | `src/orchestration/` | Wraps Action.do_execute() as nodes |
| `runner.py` | `src/orchestration/` | LangGraph execution + checkpoints |
| `checkpoints.db` | `<workspace>/.graph/` | Single source of workflow state |

---

## Result

- **Single source of truth** — `.graph/checkpoints.db` replaces 4 separate state mechanisms
- **Simpler Action class** — just `do_execute()`, no tracking boilerplate
- **Better history** — full state snapshots, not just "started/completed"
- **Resume capability** — can resume from any checkpoint
- **StoryBot unchanged** — remains purely declarative
- **CLI experience unchanged** — hidden orchestration
