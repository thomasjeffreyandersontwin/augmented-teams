# LangGraph Interaction Flow

## Overview

This document explains how the domain model concepts interact with LangGraph checkpoint storage.

## Domain Model → Storage Mapping

### Core Concepts

```
┌─────────────────────────────────────────────────────────────┐
│                    Domain Model Layer                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LangGraphRunner                                            │
│    ├─ Load workflow definition                              │
│    ├─ Compile graph with checkpointer                       │
│    ├─ Execute workflow graph                                │
│    ├─ Manage checkpoint storage ───────────┐                │
│    └─ Resume from checkpoint                │                │
│                                             │                │
│  Checkpoint                                  │                │
│    ├─ Save workflow state ──────────────────┼──┐            │
│    ├─ Restore workflow state ────────────────┼──┼──┐         │
│    ├─ Track execution history                │  │  │         │
│    └─ Enable resume capability                │  │  │         │
│                                               │  │  │         │
│  Workflow State                               │  │  │         │
│    ├─ Track current action                    │  │  │         │
│    ├─ Track completed actions                 │  │  │         │
│    ├─ Determine next action                   │  │  │         │
│    ├─ Pause workflow                          │  │  │         │
│    └─ Resume workflow                         │  │  │         │
│                                               │  │  │         │
└───────────────────────────────────────────────┼──┼──┼─────────┘
                                                │  │  │
                                                ▼  ▼  ▼
┌─────────────────────────────────────────────────────────────┐
│                  Storage Layer (SQLite)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Location: <workspace>/.graph/checkpoints.db               │
│                                                             │
│  Storage Structure:                                         │
│    ├─ thread_id (unique workflow instance)                  │
│    ├─ checkpoint_id (unique checkpoint)                     │
│    ├─ state values:                                         │
│    │   ├─ current_action                                   │
│    │   ├─ completed_actions[]                               │
│    │   ├─ action_state (started/completed)                 │
│    │   └─ other workflow state data                         │
│    └─ metadata:                                            │
│        ├─ step number                                      │
│        ├─ created_at timestamp                            │
│        └─ custom metadata                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Interaction Flow

### 1. Workflow Execution Flow

```
User Request
    │
    ▼
Router (detects --workflow flag)
    │
    ▼
LangGraphRunner.run()
    │
    ├─ Load workflow definition from BehaviorGraphBuilder
    │
    ├─ Compile graph with checkpointer
    │   └─ graph.compile(checkpointer=SqliteSaver)
    │
    ├─ Create/Get thread_id (unique workflow instance)
    │
    └─ Execute workflow
        │
        ├─ ActionNode executes
        │   │
        │   ├─ ActionNode wraps action.execute()
        │   │
        │   └─ Updates Workflow State
        │       ├─ current_action = "story_bot.shape.gather_context"
        │       └─ action_state = "started"
        │
        ├─ Checkpoint saves automatically (after each node)
        │   │
        │   └─ SqliteSaver stores:
        │       ├─ thread_id
        │       ├─ checkpoint_id (auto-generated)
        │       ├─ state values (current_action, completed_actions, etc.)
        │       └─ metadata (step, timestamp)
        │
        └─ Continue to next node...
```

### 2. Checkpoint Save Flow

```
ActionNode completes execution
    │
    ▼
Workflow State updated
    │
    ├─ current_action = "story_bot.shape.gather_context"
    ├─ action_state = "completed"
    └─ completed_actions.append("gather_context")
    │
    ▼
LangGraph automatically saves checkpoint
    │
    ├─ Checkpoint.save_workflow_state()
    │   │
    │   └─ SqliteSaver.put()
    │       │
    │       └─ Writes to .graph/checkpoints.db:
    │           ├─ thread_id: "default" (or custom)
    │           ├─ checkpoint_id: "checkpoint_123"
    │           ├─ values: {
    │           │     "current_action": "story_bot.shape.gather_context",
    │           │     "completed_actions": ["initialize_project", "gather_context"],
    │           │     "action_state": "completed"
    │           │   }
    │           └─ metadata: {
    │                 "step": 2,
    │                 "created_at": "2025-12-22T02:13:37"
    │               }
```

### 3. Resume Flow

```
User requests resume
    │
    ▼
LangGraphRunner.resume_from()
    │
    ├─ Get checkpoint from storage
    │   │
    │   └─ SqliteSaver.get(thread_id, checkpoint_id)
    │       │
    │       └─ Returns checkpoint with:
    │           ├─ state values (current_action, completed_actions, etc.)
    │           └─ metadata
    │
    ├─ Restore Workflow State
    │   │
    │   └─ Checkpoint.restore_workflow_state()
    │       │
    │       └─ Updates Workflow State:
    │           ├─ current_action = checkpoint.values["current_action"]
    │           ├─ completed_actions = checkpoint.values["completed_actions"]
    │           └─ action_state = checkpoint.values["action_state"]
    │
    └─ Continue execution from checkpoint
        │
        └─ Compiled graph resumes from saved state
```

### 4. History/Audit Trail Flow

```
User requests workflow history
    │
    ▼
LangGraphRunner.list_history(thread_id)
    │
    ├─ Checkpoint.track_execution_history()
    │   │
    │   └─ SqliteSaver.list(thread_id)
    │       │
    │       └─ Returns all checkpoints for thread:
    │           [
    │             {
    │               "checkpoint_id": "checkpoint_1",
    │               "step": 1,
    │               "current_action": "initialize_project",
    │               "completed_actions": [],
    │               "timestamp": "2025-12-22T02:10:00"
    │             },
    │             {
    │               "checkpoint_id": "checkpoint_2",
    │               "step": 2,
    │               "current_action": "gather_context",
    │               "completed_actions": ["initialize_project"],
    │               "timestamp": "2025-12-22T02:11:00"
    │             },
    │             ...
    │           ]
    │
    └─ Returns formatted history
```

## Key Interactions

### LangGraphRunner ↔ Checkpoint Storage

**LangGraphRunner manages checkpoint storage:**
- Creates `SqliteSaver` instance pointing to `.graph/checkpoints.db`
- Compiles graph with checkpointer (enables automatic checkpointing)
- Provides methods to resume from checkpoints
- Lists checkpoint history for audit trail

**Checkpoint storage provides:**
- Persistent state storage (survives server restarts)
- Thread isolation (multiple workflows can run in parallel)
- Automatic checkpointing after each node execution
- History/audit trail via checkpoint listing

### Workflow State ↔ Checkpoint Storage

**Workflow State is stored in checkpoints:**
- `current_action`: Which action is currently executing
- `completed_actions`: List of completed actions
- `action_state`: "started" or "completed"
- Other workflow-specific state data

**Checkpoint storage persists Workflow State:**
- After each node execution, state is automatically saved
- State can be restored to resume workflow
- State changes are tracked in checkpoint history

### ActionNode ↔ Checkpoint Storage

**ActionNode execution triggers checkpoint saves:**
- When ActionNode completes, LangGraph automatically saves checkpoint
- Checkpoint includes updated Workflow State
- Enables resume capability if workflow is interrupted

**Checkpoint storage enables ActionNode resumption:**
- ActionNode can resume from last checkpoint
- State is restored before ActionNode execution continues

## Storage Location

```
<workspace>/
└── .graph/
    └── checkpoints.db  (SQLite database)
```

**Database Schema (managed by LangGraph SqliteSaver):**
- `checkpoints` table: Stores checkpoint data
- `thread_id`: Unique identifier for workflow instance
- `checkpoint_id`: Unique identifier for each checkpoint
- `values`: JSON blob containing workflow state
- `metadata`: JSON blob containing checkpoint metadata

## Differences from Legacy System

| Aspect | Legacy System | LangGraph System |
|--------|--------------|-------------------|
| **Storage** | `workflow_state.json` (single file) | `.graph/checkpoints.db` (SQLite) |
| **State Tracking** | Manual save/load | Automatic checkpointing |
| **History** | `activity_log.json` (separate file) | Built into checkpoint storage |
| **Resume** | Manual state restoration | Automatic resume from checkpoint |
| **Isolation** | Single workflow state | Thread-based isolation (multiple workflows) |
| **Persistence** | JSON file in project area | SQLite database in workspace |

## Example: Complete Workflow Lifecycle

1. **Start Workflow**
   ```
   User: /story_bot-shape gather_context --workflow
   → Router detects --workflow flag
   → LangGraphRunner.run() called
   → Creates thread_id: "default"
   → Compiles graph with checkpointer
   → Executes first node (initialize_project)
   → Checkpoint saved automatically
   ```

2. **Continue Execution**
   ```
   → Next node executes (gather_context)
   → Workflow State updated
   → Checkpoint saved automatically
   → Continues to next node...
   ```

3. **Interrupt Workflow**
   ```
   → User stops workflow (Ctrl+C or timeout)
   → Last checkpoint remains in storage
   → Workflow State preserved
   ```

4. **Resume Workflow**
   ```
   User: /story_bot-shape gather_context --workflow --resume
   → LangGraphRunner.resume_from() called
   → Loads last checkpoint from storage
   → Restores Workflow State
   → Continues from last checkpoint
   ```

5. **View History**
   ```
   User: /story_bot-shape gather_context --workflow --history
   → LangGraphRunner.list_history() called
   → Returns all checkpoints for thread
   → Shows complete audit trail
   ```

## Summary

The domain model concepts (LangGraphRunner, Checkpoint, Workflow State) interact with storage through:

1. **LangGraphRunner** manages the checkpoint storage (SqliteSaver)
2. **Checkpoint** saves/restores workflow state to/from storage
3. **Workflow State** is persisted in checkpoint storage after each node
4. **ActionNode** execution triggers automatic checkpoint saves
5. **Storage** provides persistence, history, and resume capability

All interactions happen automatically through LangGraph's checkpointing system - no manual file management required.

