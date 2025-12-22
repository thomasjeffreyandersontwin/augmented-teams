# BaseBot → LangGraph Integration Plan

> ⚠️ **DRAFT — DOMAIN MODEL & ARCHITECTURE**
>
> This document defines the architecture for integrating LangGraph as an **optional** orchestration layer.
>
> **Key Principle:** LangGraph is opt-in for complex workflows. Default workflows remain unchanged.
>
> **Before implementation, this plan requires:**
> 1. **Shape** — Define the problem boundaries and key trade-offs
> 2. **Discovery** — Elaborate domain concepts, responsibilities, and collaborations  
> 3. **Exploration** — Define acceptance criteria and scenarios

---

## Executive Summary

**Problem:** BaseBot needs advanced workflow capabilities (conditionals, parallelism, loops, human-in-the-loop) without breaking existing simple workflows.

**Solution:** Two completely separate paths:
1. **Default Path** — Current code stays exactly as-is (legacy files kept)
2. **Custom Path** — LangGraph-based orchestration via `--workflow` flag

**Key Innovation:** Single `ActionNode` class with two-pass pattern (instructions → confirmation) handles ALL behavior/action combinations.

**Migration:** Zero breaking changes. LangGraph workflows are purely additive.

---

## Objective

Integrate **LangGraph** into **BaseBot** as an **optional** orchestration layer for complex workflows.

**Two Completely Separate Paths:**

1. **Default Workflow (Untouched)** — Current code stays exactly as-is
   - CLI → Bot → Behavior → Action
   - No changes, no new parameters, no routing logic
   - **We do not touch this code path**

2. **Custom Workflow (LangGraph)** — Entirely new capability
   - CLI → LangGraphRunner → Graph Nodes → action.execute(context)
   - Enabled via `--workflow <name>` flag
   - For conditional branching, parallel execution, loops, human-in-the-loop
   - **Completely additive — no changes to existing code**

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
│   │   ├── action_state_manager.py # KEEP (legacy default workflow)
│   │   ├── activity_tracker.py    # KEEP (legacy default workflow)
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

## Legacy Files — KEEP (Default Workflow Only)

| File | Purpose | Used By |
|------|---------|---------|
| `action_state_manager.py` | Tracks current/completed actions | Default workflow ONLY |
| `activity_tracker.py` | Logs start/complete timestamps | Default workflow ONLY |
| `behavior_action_state.json` | Workflow state file | Default workflow ONLY |
| `activity_log.json` | TinyDB activity log | Default workflow ONLY |

**CRITICAL: LangGraph workflows do NOT touch these files.**

These are **legacy files** for the default workflow. The two systems are completely separate:

| Aspect | Default Workflow (Legacy) | LangGraph Workflows (New) |
|--------|---------------------------|---------------------------|
| State tracking | `action_state_manager.py` | LangGraph checkpoints |
| Activity log | `activity_tracker.py` | LangGraph checkpoint history |
| State file | `behavior_action_state.json` | `.graph/checkpoints.db` |
| Audit trail | `activity_log.json` | Checkpoint metadata |

**No sharing, no interaction between the two systems.**

---

## State Files (Keep)

| File | Location | Purpose |
|------|----------|---------|
| `story-graph.json` | `<workspace>/docs/stories/` | Main knowledge graph |
| `context/` | `<workspace>/docs/stories/context/` | Session context files |
| `guardrails/` | Per-behavior | Clarification, strategy data |

---

## Execution Flows

### Path A: Default Workflow (UNTOUCHED)

```
CLI: story_bot_cli --behavior discovery --action build

BaseBotCli.main()
  → CliCommandRouter.route(args)
  → CliExecutor.execute_and_output(args, params)

Bot → Behavior → Actions → Action.execute(parameters)
  → Returns instructions dict

CliExecutor._output_result(result)
  → Prints JSON + base_instructions for AI to execute
```

**This code path is NOT modified. Legacy files continue to work.**

### Path B: LangGraph Workflow (NEW)

```
CLI: story_bot_cli --workflow tdd_workflow --mode autonomous

BaseBotCli.main()
  → Detects --workflow flag
  → Routes to Bot
  → Bot routes to LangGraphRunner

LangGraphRunner.run(workflow_name)
  → Finds workflow in story_bot/orchestration/graphs/
  → Loads workflow definition (Python code)
  → Compiles graph with checkpointer
  → Executes graph

Graph Execution:
  Node A (ActionNode) → calls action.execute(context)
    → If autonomous: get_instructions() → AI call → confirm_with_response()
    → If interactive: get_instructions() → PAUSE → return prompt
  [checkpoint saved]
  Node B (ActionNode) → ...
  [checkpoint saved]
  Decision Node → routes based on result
  ...
  
Results returned to CLI
```

**Key:** LangGraph owns its own state. Never touches legacy files.

---

## Node Execution Model

### Two-Pass Pattern

Every action follows a two-pass pattern:

1. **Instructions Pass** → Action generates instructions/prompts for AI
2. **Confirmation Pass** → AI has responded, confirm with the response

### Execution Modes

| Mode | Behavior | AI Calls | CLI Round-trip |
|------|----------|----------|----------------|
| **Autonomous** | Node calls AI directly, no pause | Internal via API key | None |
| **Interactive** | Returns prompt, pauses for human/Cursor | Cursor/Human | Yes |

### ActionNode: Single Universal Node Class

**Key insight:** One node class handles ALL behavior/action combinations. Just pass different behavior and action names.

**Architecture:**
- `get_instructions()` — First pass: get prompt from action
- `confirm_with_response()` — Second pass: confirm with AI/human response
- `run_autonomous()` — Calls AI directly, no pause
- `run_interactive()` — Returns prompt, pauses for human
- `__call__()` — LangGraph entry point, routes based on mode

**LangGraph only cares about `__call__()`** — internal structure is entirely ours.

### Example: TDD Workflow

```
TEST LOOP (mode=autonomous)
  test.rules → [AI call] → confirm → next
  test.build → [AI call] → confirm → next
  test.validate → [AI call] → confirm → check result
  [Loops internally until pass or max iterations]
        ↓
HUMAN REVIEW (mode=interactive)
  → Returns prompt, pauses
  → Human reviews test results
  → Human runs --continue
        ↓
CODE LOOP (mode=autonomous)
  code.rules → [AI call] → confirm → next
  code.build → [AI call] → confirm → next
  code.validate → [AI call] → confirm → check result
  [Loops internally until pass or max iterations]
        ↓
FINAL APPROVAL (mode=interactive)
  → Returns prompt with options
  → Human chooses: approve / restart / abort
```

### CLI Commands

```bash
# Start workflow in autonomous mode
story_bot_cli --workflow tdd_workflow --mode autonomous

# Start in interactive mode (default)
story_bot_cli --workflow tdd_workflow

# Resume after interactive pause
story_bot_cli --workflow tdd_workflow --continue

# Resume with response/decision
story_bot_cli --workflow tdd_workflow --continue --decision approve

# Check workflow status
story_bot_cli --workflow tdd_workflow --status
```

---

## Implementation Plan

> **Note:** The code below is conceptual scaffolding to illustrate the integration approach.  
> Class responsibilities, method signatures, and file organization will be refined through  
> proper shaping and discovery before any implementation begins.

### Directory Structure

**BaseBot (Framework — Abstract/Base Components Only):**

```
agile_bot/bots/base_bot/src/
├── orchestration/                  # NEW: LangGraph framework support
│   ├── __init__.py
│   ├── langgraph_runner.py         # Loads graphs, compiles, executes
│   └── base_nodes/                 # ABSTRACT/BASE nodes (never instantiated directly)
│       ├── __init__.py
│       └── base_action_node.py     # Base class for action nodes
│
├── bot/                            # UNTOUCHED (default workflow uses this)
├── actions/                        # UNTOUCHED (including tracker/state_manager for legacy)
└── cli/                            # MODIFIED: Add --workflow flag routing
```

**StoryBot (Concrete Implementation):**

```
agile_bot/bots/story_bot/
├── orchestration/                  # StoryBot's LangGraph workflows
│   ├── __init__.py
│   │
│   ├── graphs/                     # Workflow definitions (Python code)
│   │   ├── __init__.py
│   │   ├── tdd_workflow.py         # TDD: tests → code → approve
│   │   └── discovery_flow.py       # Discovery workflow
│   │
│   ├── nodes/                      # Simple structure
│   │   ├── __init__.py
│   │   ├── action_node.py          # ActionNode - ONE class for ALL behavior.action combos
│   │   ├── decision_nodes.py       # Routing functions
│   │   └── approval_nodes.py       # Human approval nodes
│   │
│   └── state/                      # StoryBot state schemas
│       ├── __init__.py
│       └── story_workflow_state.py # TypedDict for story workflows
│
├── behaviors/                      # UNTOUCHED
└── src/                            # UNTOUCHED
```

**Key Principle:** BaseBot provides framework, StoryBot provides concrete implementations.

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

### Step 3: ActionNode (Universal Node Class)

**One class handles ALL behavior/action combinations.** Just instantiate with different behavior and action names.

This is defined in `story_bot/orchestration/nodes/action_node.py`:

```python
class ActionNode:
    """Universal node for any behavior/action combination.
    
    Two-pass pattern:
    - get_instructions(): First pass - generate prompt
    - confirm_with_response(): Second pass - confirm with AI response
    
    Execution modes:
    - autonomous: Calls AI directly, no CLI round-trip
    - interactive: Returns prompt, pauses for human
    """
    
    def __init__(self, bot, behavior_name: str, action_name: str):
        self.bot = bot
        behavior = bot.behaviors.find_by_name(behavior_name)
        self.action = behavior.actions.find_by_name(action_name)
    
    def get_instructions(self, context: dict) -> str:
        """First pass: Get instructions from action."""
        result = self.action.execute(context)
        return result.get("instructions", "")
    
    def confirm_with_response(self, context: dict, response: str) -> dict:
        """Second pass: Confirm with AI/human response."""
        return self.action.execute({**context, "response": response})
    
    def run_autonomous(self, context: dict, ai_client) -> dict:
        """Autonomous: call AI directly, no pause."""
        instructions = self.get_instructions(context)
        ai_response = ai_client.chat(instructions)
        return self.confirm_with_response(context, ai_response)
    
    def run_interactive(self, context: dict) -> dict:
        """Interactive: return prompt, pause for human."""
        instructions = self.get_instructions(context)
        return {"prompt": instructions, "needs_confirmation": True}
    
    def __call__(self, state: dict) -> dict:
        """LangGraph entry point."""
        if state.get("mode") == "autonomous":
            return self.run_autonomous(state["context"], state["ai_client"])
        else:
            return self.run_interactive(state["context"])
```

**Usage in workflow:**
```python
# In tdd_workflow.py
test_build = ActionNode(bot, "tests", "build")
test_validate = ActionNode(bot, "tests", "validate")
code_build = ActionNode(bot, "code", "build")

graph.add_node("test_build", test_build)
graph.add_node("test_validate", test_validate)
graph.add_node("code_build", code_build)
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

### Note: Action Class UNCHANGED

**The existing `Action` class is NOT modified.**

LangGraph workflows call `action.execute(context)` exactly as the default workflow does.
The ActionNode handles the two-pass pattern (instructions → confirmation) internally.

No changes to:
- `action.py`
- `activity_tracker.py`
- `action_state_manager.py`

**These files continue to work for the default workflow.**

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

## Workspace Structure (With LangGraph Workflows)

```
<workspace>/
├── docs/stories/
│   ├── story-graph.json           # Main knowledge graph (unchanged)
│   └── context/                    # Session context (unchanged)
│
├── behavior_action_state.json     # KEPT - default workflow uses this
├── activity_log.json              # KEPT - default workflow uses this
│
└── .graph/                        # NEW - LangGraph workflows ONLY
    └── checkpoints.db              # SQLite - LangGraph state lives here
```

**Note:** Legacy files are KEPT. LangGraph uses its own separate state in `.graph/`.

---

## LangGraph Checkpoints (Custom Workflows Only)

**Note:** This applies ONLY to custom LangGraph workflows. Default workflow continues to use legacy files.

### Checkpoint State

```python
runner.get_current_state("tdd_workflow_thread")
# Returns: {
#   "mode": "autonomous",
#   "current_phase": "test_loop",
#   "completed_actions": ["test.rules", "test.build"],
#   "loop_count": 2,
#   ...
# }
```

### Checkpoint History

```python
runner.list_history("tdd_workflow_thread")
# Returns: [
#   {"step": 1, "current_action": "test.rules", "timestamp": "..."},
#   {"step": 2, "current_action": "test.build", "timestamp": "..."},
#   ...
# ]
```

### Resume from Checkpoint

```python
# Resume after interactive pause
runner.resume_from(graph, "tdd_workflow_thread", checkpoint_id)
```

---

## Files Status

**DO NOT DELETE — Default Workflow Still Uses:**

| File | Status | Used By |
|------|--------|---------|
| `src/actions/activity_tracker.py` | KEEP | Default workflow |
| `src/actions/action_state_manager.py` | KEEP | Default workflow |
| `behavior_action_state.json` | KEEP | Default workflow |
| `activity_log.json` | KEEP | Default workflow |

**NEW FILES — For LangGraph Workflows:**

| File | Location | Purpose |
|------|----------|---------|
| `langgraph_runner.py` | `base_bot/src/orchestration/` | Load, compile, run graphs |
| `base_action_node.py` | `base_bot/src/orchestration/base_nodes/` | Abstract base for action nodes |
| `action_node.py` | `story_bot/orchestration/nodes/` | Concrete ActionNode class |
| `decision_nodes.py` | `story_bot/orchestration/nodes/` | Routing functions |
| `approval_nodes.py` | `story_bot/orchestration/nodes/` | Human approval nodes |
| `tdd_workflow.py` | `story_bot/orchestration/graphs/` | TDD workflow definition |
| `.graph/checkpoints.db` | `<workspace>/` | LangGraph checkpoint storage |

---

## Architecture Decisions

1. **Two completely separate systems (no interaction):**
   - Default workflow → Legacy files (activity_tracker, action_state_manager, JSON files)
   - LangGraph workflows → LangGraph checkpoints (`.graph/checkpoints.db`)

2. **Legacy files are ONLY for default workflow** — LangGraph does NOT touch them

3. **LangGraph workflows use ONLY LangGraph checkpoints** — No legacy file access

4. **Single ActionNode class** — Handles ALL behavior/action combinations

5. **Two-pass pattern** — `get_instructions()` → `confirm_with_response()`

6. **Mode determines AI execution:**
   - Autonomous: Node calls AI directly via API
   - Interactive: Returns prompt, pauses for human

7. **Graphs defined in Python code** — Not JSON config files (LangGraph standard)

### Open Questions (To Address in Discovery)

- How do we handle AI API errors in autonomous mode?
- Should action.execute() support async for parallel nodes?
- How is action result transformed into LangGraph state update?
- What's the right granularity for checkpoints?

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

- **Zero breaking changes** — Default workflow completely untouched
- **Optional complexity** — LangGraph only when needed via `--workflow` flag
- **Powerful workflows** — Conditionals, loops, parallelism, human-in-the-loop
- **Single ActionNode class** — No proliferation of node classes per action
- **Two-pass pattern** — Clean separation of instruction generation and confirmation
- **Mode flexibility** — Same workflow can run autonomous or interactive
- **Framework/Implementation separation** — BaseBot = runner + base nodes, StoryBot = concrete graphs + nodes
