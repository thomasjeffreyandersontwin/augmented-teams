# Domain Model Description: Base Bot

**File Name**: `base-bot-domain-model-description.md`
**Location**: `base_bot/docs/stories/base-bot-domain-model-description.md`

## Solution Purpose
Domain model for Base Bot

---

## Domain Model Descriptions

### ActionNode

**Key Responsibilities:**
- **Wrap action execution**: This responsibility involves collaboration with Action, Behavior.
- **Get instructions from action**: This responsibility involves collaboration with Action.
- **Confirm with response**: This responsibility involves collaboration with Action, AI Chat.
- **Run in autonomous mode**: This responsibility involves collaboration with AI Client, ExecutionMode.
- **Run in interactive mode**: This responsibility involves collaboration with Human, ExecutionMode.

### Base Action

**Key Responsibilities:**
- **Inject Instructions**: This responsibility involves collaboration with Behavior.
- **Load Relevant Content + Inject Into Instructions**: This responsibility involves collaboration with Content.
- **Save content changes**: This responsibility involves collaboration with Content.

### Base Bot

**Key Responsibilities:**
- **Executes Actions**: This responsibility involves collaboration with Workflow, Behavior, Action.
- **Track activity**: This responsibility involves collaboration with Behavior, Action.
- **Route to behaviors and actions**: This responsibility involves collaboration with Router, Trigger Words.
- **Persist content**: This responsibility involves collaboration with Content.
- **Manage Project State**: This responsibility involves collaboration with Project.
- **Render**: Render

### Behavior

**Key Responsibilities:**
- **Perform Configured Actions**: This responsibility involves collaboration with Actions.
- **Invoke On Trigger Words**: This responsibility involves collaboration with List.
- **Inject Instructions**: This responsibility involves collaboration with Text.
- **Provide Guardrails**: This responsibility involves collaboration with GuardRails.
- **Provide Rules**: This responsibility involves collaboration with Rule, Validation.
- **Provide Content Specs**: This responsibility involves collaboration with Content.

### Behavior Workflow

**Key Responsibilities:**
- **Determine next Action**: This responsibility involves collaboration with Behavior, Action, State.
- **Track state**: This responsibility involves collaboration with Behavior, Action, State.

### Checkpoint

**Key Responsibilities:**
- **Save workflow state**: This responsibility involves collaboration with State, LangGraphRunner.
- **Restore workflow state**: This responsibility involves collaboration with State, LangGraphRunner.
- **Track execution history**: This responsibility involves collaboration with State.
- **Enable resume capability**: This responsibility involves collaboration with Workflow, LangGraphRunner.

### ExecutionMode

**Key Responsibilities:**
- **Determine AI interaction**: This responsibility involves collaboration with ActionNode, AI Client.
- **Control pause points**: This responsibility involves collaboration with ActionNode, Human.

### GatherContextAction

**Key Responsibilities:**
- **Inject gather context instructions**: This responsibility involves collaboration with Behavior, Guardrails, Required Clarifications.
- **Inject questions and evidence**: This responsibility involves collaboration with Behavior, Guardrails, Key Questions, Evidence.

### Guardrails

**Key Responsibilities:**
- **Provide required context**: This responsibility involves collaboration with Key Questions, Evidence.
- **Guide planning decisions**: This responsibility involves collaboration with Decision Criteria, Assumptions.
- **Define recommended human activity**: This responsibility involves collaboration with Human, Instructions.

### LangGraph workflow

**Key Responsibilities:**
- **Execute nodes in sequence**: This responsibility involves collaboration with ActionNode, LangGraphRunner.
- **Handle conditional branching**: This responsibility involves collaboration with Decision Node, State.
- **Support loops and iterations**: This responsibility involves collaboration with ActionNode, State.
- **Pause at interactive points**: This responsibility involves collaboration with Human, ExecutionMode.
- **Resume from checkpoint**: This responsibility involves collaboration with Checkpoint, LangGraphRunner.

### LangGraphRunner

**Key Responsibilities:**
- **Compile graph with checkpointer**: This responsibility involves collaboration with LangGraph workflow, Checkpoint.
- **Execute workflow graph**: This responsibility involves collaboration with LangGraph workflow, ActionNode.
- **Manage checkpoint storage**: This responsibility involves collaboration with Checkpoint.
- **Resume from checkpoint**: This responsibility involves collaboration with Checkpoint, LangGraph workflow.

### Project

**Key Responsibilities:**
- **Move project to working area**: This responsibility involves collaboration with Working Directory.
- **Save project in context**: This responsibility involves collaboration with Working Directory, Workflow State.
- **Update project area**: This responsibility involves collaboration with Working Directory, Content.

### Router

**Key Responsibilities:**
- **Match trigger patterns**: This responsibility involves collaboration with Trigger Words, Route.
- **Route to MCP bot tool**: This responsibility involves collaboration with Base Bot, Trigger Words.
- **Route to behavior tool**: This responsibility involves collaboration with Behavior, Trigger Words.
- **Route to action tool**: This responsibility involves collaboration with Action, Trigger Words.
- **Forward to behavior**: This responsibility involves collaboration with Behavior, Base Bot.
- **Forward to action**: This responsibility involves collaboration with Action, Behavior.
- **Forward to current behavior and action**: This responsibility involves collaboration with Behavior, Action, Base Bot.

### Specific Bot

**Key Responsibilities:**
- **Provide Behavior config**: This responsibility involves collaboration with Bot Config, Behavior.
- **Provide MCP config**: This responsibility involves collaboration with MCP Config.
- **Provide Renderers**: Provide Renderers
- **Provide Extractors**: Provide Extractors
- **Provide Synchronizer**: Provide Synchronizer
- **Provide Trigger Words**: Provide Trigger Words

### LangGraph State Container

**Key Responsibilities:**
- **Contain story graph**: This responsibility involves collaboration with Story Graph.
- **Contain clarification data**: This responsibility involves collaboration with Key Questions, Evidence.
- **Contain strategy data**: This responsibility involves collaboration with Decision Criteria, Assumptions.
- **Contain context files**: This responsibility involves collaboration with Context.
- **Contain files dictionary**: This responsibility involves collaboration with Source Files, Test Files. The files dictionary is a flexible structure that can dynamically contain any file type (source, test, docs, etc.) as needed by different bots and workflows.
- **Contain workspace directory**: This responsibility involves collaboration with Workspace.
- **Contain workflow execution state**: This responsibility involves collaboration with Action, Instructions.

### Workflow State

**Key Responsibilities:**
- **Track current action**: This responsibility involves collaboration with Action.
- **Track completed actions**: This responsibility involves collaboration with Action, Activity Log.
- **Determine next action**: This responsibility involves collaboration with Action, Behavior.
- **Pause workflow**: This responsibility involves collaboration with Human, AI Chat.
- **Resume workflow**: This responsibility involves collaboration with Human, AI Chat.

---

## Source Material

**Primary Source:** `input.txt`
**Date Generated:** 2025-01-27
**Context:** Shape phase - Domain model extracted from story-graph.json
