# Domain Model Description: Base Bot

**File Name**: `base-bot-domain-model-description.md`
**Location**: `base_bot/docs/stories/base-bot-domain-model-description.md`

## Solution Purpose
Domain model for Base Bot

---

## Domain Model Descriptions

### Action Confirmation

**Key Responsibilities:**
- **ClarifyConfirmation: Saved To, Questions Answered Count, Evidence Provided Count, Success**: ClarifyConfirmation: Saved To, Questions Answered Count, Evidence Provided Count, Success
- **StrategyConfirmation: Saved To, Decisions Count, Assumptions Count, Success**: StrategyConfirmation: Saved To, Decisions Count, Assumptions Count, Success
- **BuildConfirmation: Saved To, Mode (create/update), Items Added, Success**: BuildConfirmation: Saved To, Mode (create/update), Items Added, Success
- **RenderConfirmation: Saved To (list), Documents Created Count, Synchronizers Executed, Success**: RenderConfirmation: Saved To (list), Documents Created Count, Synchronizers Executed, Success
- **ValidateResult: Passed, Violations, Files Validated Count, Scope, Validation Summary**: ValidateResult: Passed, Violations, Files Validated Count, Scope, Validation Summary
- **Save to state**: This responsibility involves collaboration with Behavior Action State.
- **Display to user**: This responsibility involves collaboration with Output Formatter.
- **Advance to next action**: This responsibility involves collaboration with Behavior Action State.

### Action Data Collector

**Key Responsibilities:**
- **Sort behaviors**: This responsibility involves collaboration with Behavior.
- **Get behavior actions**: This responsibility involves collaboration with Action.
- **Get action parameters**: This responsibility involves collaboration with Action Context.
- **Get parameter descriptions**: This responsibility involves collaboration with Action Context.
- **Get action description**: This responsibility involves collaboration with Action.

### Action Executor

**Key Responsibilities:**
- **Detect operation phase**: Detect operation phase
- **Execute instructions operation**: This responsibility involves collaboration with Action, Action Context.
- **Execute submit operation**: This responsibility involves collaboration with Action, Action Context.
- **Execute confirm operation**: This responsibility involves collaboration with Action, Workflow State.
- **Capture typed results**: This responsibility involves collaboration with Action Instructions, Action Confirmation.
- **Update state**: This responsibility involves collaboration with Behavior Action State.

### Action Help Context

**Key Responsibilities:**
- **Store action name**: This responsibility involves collaboration with Action.
- **Store action description**: This responsibility involves collaboration with Action.
- **Store parameters**: This responsibility involves collaboration with Action Context.
- **Store parameter descriptions**: This responsibility involves collaboration with Action Context.
- **Provide to visitor**: This responsibility involves collaboration with Visitor.

### Action Instructions

**Key Responsibilities:**
- **ClarifyInstructions: Key Questions, Evidence Types, Guardrails**: ClarifyInstructions: Key Questions, Evidence Types, Guardrails
- **StrategyInstructions: Strategy Criteria, Typical Assumptions, Recommended Activities**: StrategyInstructions: Strategy Criteria, Typical Assumptions, Recommended Activities
- **BuildInstructions: Knowledge Graph Template, Rules, Scope, Story Names**: BuildInstructions: Knowledge Graph Template, Rules, Scope, Story Names
- **RenderInstructions: Render Specs, Templates, Scope**: RenderInstructions: Render Specs, Templates, Scope
- **Display to user**: This responsibility involves collaboration with Output Formatter.
- **Show examples**: This responsibility involves collaboration with Scope.

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

### Behavior Action State

**Key Responsibilities:**
- **Track current action**: This responsibility involves collaboration with Action.
- **Track completed actions**: This responsibility involves collaboration with Action, Activity Log.
- **Determine next action**: This responsibility involves collaboration with Action, Behavior.
- **Pause workflow**: This responsibility involves collaboration with Human, AI Chat.
- **Resume workflow**: This responsibility involves collaboration with Human, AI Chat.

### Behavior Help Context

**Key Responsibilities:**
- **Store behavior name**: This responsibility involves collaboration with Behavior.
- **Store behavior description**: This responsibility involves collaboration with Behavior.
- **Store actions**: This responsibility involves collaboration with Action.
- **Provide to visitor**: This responsibility involves collaboration with Visitor.

### Behavior Workflow

**Key Responsibilities:**
- **Determine next Action**: This responsibility involves collaboration with Behavior, Action, State.
- **Track state**: This responsibility involves collaboration with Behavior, Action, State.

### BehaviorGraphBuilder

**Key Responsibilities:**
- **Read behavior workflow definitions**: This responsibility involves collaboration with Behavior, Behavior Config.
- **Create LangGraph StateGraph**: This responsibility involves collaboration with LangGraph, BotLangState.
- **Build node instances from actions**: This responsibility involves collaboration with BotLangActionNode, Action.
- **Connect nodes based on workflow order**: This responsibility involves collaboration with LangGraph, BotLangActionNode.

### BotLangActionNode

**Key Responsibilities:**
- **Wrap action.execute(context) method**: This responsibility involves collaboration with Action, LangGraph.
- **Implement two-pass pattern**: This responsibility involves collaboration with Action, AI.
- **Support execution modes**: This responsibility involves collaboration with BotMode.
- **Provide LangGraph entry point**: This responsibility involves collaboration with LangGraph.

### BotLangFlow

**Key Responsibilities:**
- **Execute nodes in sequence**: This responsibility involves collaboration with BotLangActionNode, BotLangFlowRunner.
- **Handle conditional branching**: This responsibility involves collaboration with Decision Node, BotLangState.
- **Support loops and iterations**: This responsibility involves collaboration with BotLangActionNode, BotLangState.
- **Pause at interactive points**: This responsibility involves collaboration with Human, BotMode.
- **Resume from checkpoint**: This responsibility involves collaboration with Checkpoint, BotLangFlowRunner.

### BotLangFlowRunner

**Key Responsibilities:**
- **Load BotLangFlow Python files**: This responsibility involves collaboration with BotLangFlow, File System.
- **Compile graph with checkpointer**: This responsibility involves collaboration with LangGraph, SqliteSaver, Checkpoint.
- **Execute workflow graph**: This responsibility involves collaboration with LangGraph, BotLangActionNode, BotLangState.
- **Resume from checkpoint**: This responsibility involves collaboration with Checkpoint, BotLangState.

### BotLangState

**Key Responsibilities:**
- **Contain story graph**: This responsibility involves collaboration with Story Graph.
- **Contain clarification data**: This responsibility involves collaboration with Key Questions, Evidence.
- **Contain strategy data**: This responsibility involves collaboration with Decision Criteria, Assumptions.
- **Contain context files**: This responsibility involves collaboration with Context.
- **Contain files dictionary**: This responsibility involves collaboration with Source Files, Test Files.
- **Contain workspace directory**: This responsibility involves collaboration with Workspace.
- **Contain workflow execution state**: This responsibility involves collaboration with Action, Instructions.

### BotMode

**Key Responsibilities:**
- **Determine AI interaction**: This responsibility involves collaboration with BotLangActionNode, AI Client.
- **Control pause points**: This responsibility involves collaboration with BotLangActionNode, Human.

### BuildKnowledgeAction

**Key Responsibilities:**
- **Inject knowledge graph template**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph Spec, Knowledge Graph.
- **Inject builder instructions**: This responsibility involves collaboration with Behavior, Content, Build Instructions.
- **Save Knowledge graph**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph.

### Checkpoint

**Key Responsibilities:**
- **Save workflow state**: This responsibility involves collaboration with BotLangState, BotLangFlowRunner.
- **Restore workflow state**: This responsibility involves collaboration with BotLangState, BotLangFlowRunner.
- **Track execution history**: This responsibility involves collaboration with BotLangState.
- **Enable resume capability**: This responsibility involves collaboration with BotLangFlow, BotLangFlowRunner.

### Command Router

**Key Responsibilities:**
- **Find behavior**: This responsibility involves collaboration with Behavior.
- **Find action**: This responsibility involves collaboration with Action.
- **Detect command type**: Detect command type
- **Route to appropriate operation**: This responsibility involves collaboration with Action.
- **Build context**: This responsibility involves collaboration with Context Builder.
- **Navigate to action**: This responsibility involves collaboration with Behavior Action State.

### Content

**Key Responsibilities:**
- **Render outputs**: This responsibility involves collaboration with Template, Renderer, Render Spec.
- **Synchronize formats**: This responsibility involves collaboration with Synchronizer, Extractor, Synchronizer Spec.
- **Save knowledge graph**: This responsibility involves collaboration with Knowledge Graph.
- **Load rendered content**: This responsibility involves collaboration with na.
- **Present rendered content**: This responsibility involves collaboration with na.

### Context Builder

**Key Responsibilities:**
- **Build typed context**: This responsibility involves collaboration with Action Context.
- **Build FileScope**: This responsibility involves collaboration with FileScope.
- **Build StoryScope**: This responsibility involves collaboration with StoryScope.
- **Validate parameters**: This responsibility involves collaboration with Parameter Parser.
- **Apply defaults**: This responsibility involves collaboration with Scope.

### CorrectBotAction

**Key Responsibilities:**
- **Inject correct bot instructions**: This responsibility involves collaboration with Behavior, Correct Bot Instructions.
- **Load + inject diagnostics results**: This responsibility involves collaboration with Content, Diagnostic Report, Violations, Suggestions.

### Dot Notation Parameters

**Key Responsibilities:**
- **Parse key=value pairs**: This responsibility involves collaboration with File Scope, Story Scope.
- **Parse quoted values**: This responsibility involves collaboration with File Scope, Story Scope.
- **Parse comma lists**: This responsibility involves collaboration with File Scope, Story Scope.

### FileScope

**Key Responsibilities:**
- **Include file paths: List of paths**: Include file paths: List of paths
- **Exclude file paths: List of patterns**: Exclude file paths: List of patterns
- **Apply to build/render**: This responsibility involves collaboration with BuildActionContext, RenderActionContext.

### GatherContextAction

**Key Responsibilities:**
- **Inject gather context instructions**: This responsibility involves collaboration with Behavior, Guardrails, Required Clarifications.
- **Inject questions and evidence**: This responsibility involves collaboration with Behavior, Guardrails, Key Questions, Evidence.

### Guardrails

**Key Responsibilities:**
- **Provide required context**: This responsibility involves collaboration with Key Questions, Evidence.
- **Guide planning decisions**: This responsibility involves collaboration with Decision Criteria, Assumptions.
- **Define recommended human activity**: This responsibility involves collaboration with Human, Instructions.

### Help Generator

**Key Responsibilities:**
- **Generate command help**: This responsibility involves collaboration with Behavior, Action.
- **Generate parameter help**: This responsibility involves collaboration with Action Context.
- **Generate scope examples**: This responsibility involves collaboration with FileScope, StoryScope.
- **Display available nodes**: This responsibility involves collaboration with StoryScope.
- **Display available folders**: This responsibility involves collaboration with FileScope.

### Node

**Key Responsibilities:**
- **Node type: STORY, EPIC, SUB_EPIC, INCREMENT**: Node type: STORY, EPIC, SUB_EPIC, INCREMENT
- **Node name: String identifier**: Node name: String identifier

### Orchestrator

**Key Responsibilities:**
- **Walk behaviors**: This responsibility involves collaboration with Bot.
- **Walk actions**: This responsibility involves collaboration with Behavior.
- **Call visitor methods**: This responsibility involves collaboration with Visitor.
- **Provide help context**: This responsibility involves collaboration with Action Data Collector.

### Output Formatter

**Key Responsibilities:**
- **Display state**: This responsibility involves collaboration with Behavior Action State.
- **Display instructions**: This responsibility involves collaboration with Action Instructions.
- **Display results**: This responsibility involves collaboration with Action Results.
- **Display help**: This responsibility involves collaboration with Help Generator.
- **Display errors**: This responsibility involves collaboration with Parameter Parser.

### Parameter Parser

**Key Responsibilities:**
- **Parse text input**: This responsibility involves collaboration with Dot Notation Parameters.
- **Extract behavior name**: This responsibility involves collaboration with Behavior.
- **Extract action name**: This responsibility involves collaboration with Action.
- **Extract scope**: This responsibility involves collaboration with File Scope, Story Scope.

### PlanningAction

**Key Responsibilities:**
- **Inject planning instructions**: This responsibility involves collaboration with Behavior, Guardrails, Planning.
- **Inject decision criteria and assumptions**: This responsibility involves collaboration with Behavior, Guardrails, Decision Criteria, Assumptions, Recommended Human Activity.

### Project

**Key Responsibilities:**
- **Move project to working area**: This responsibility involves collaboration with Working Directory.
- **Save project in context**: This responsibility involves collaboration with Working Directory, Workflow State.
- **Update project area**: This responsibility involves collaboration with Working Directory, Content.

### REPL Command Generator

**Key Responsibilities:**
- **Walk bot structure**: This responsibility involves collaboration with Orchestrator, Bot.
- **Collect action data**: This responsibility involves collaboration with Action Data Collector.
- **Generate command definitions**: This responsibility involves collaboration with REPL Command Visitor.
- **Generate cursor shortcuts**: This responsibility involves collaboration with Cursor REPL Visitor.
- **Generate help docs**: This responsibility involves collaboration with Help REPL Visitor.

### REPL Command Visitor

**Key Responsibilities:**
- **Visit behavior**: This responsibility involves collaboration with Behavior Help Context.
- **Visit action**: This responsibility involves collaboration with Action Help Context.
- **Generate navigate commands**: This responsibility involves collaboration with Behavior, Action.
- **Generate scope commands**: This responsibility involves collaboration with File Scope, Story Scope.
- **Generate instructions commands**: This responsibility involves collaboration with Scope.
- **Generate submit commands**: This responsibility involves collaboration with Action Context.
- **Generate confirm commands**: This responsibility involves collaboration with Workflow State.

### REPL Session

**Key Responsibilities:**
- **Display current state**: This responsibility involves collaboration with Behavior Action State, Output Formatter.
- **Read command input**: This responsibility involves collaboration with TTY Input.
- **Parse command input**: This responsibility involves collaboration with Parameter Parser.
- **Detect command type**: This responsibility involves collaboration with Command Router.
- **Route to action operation**: This responsibility involves collaboration with Command Router.
- **Execute action operation**: This responsibility involves collaboration with Action Executor.
- **Display results**: This responsibility involves collaboration with Output Formatter.
- **Loop or exit**: Loop or exit

### RenderOutputAction

**Key Responsibilities:**
- **Inject render output instructions**: This responsibility involves collaboration with Behavior, Content, Render Spec, Renderer.
- **Inject templates**: This responsibility involves collaboration with Behavior, Content, Render Spec, Template.
- **Inject transformers**: This responsibility involves collaboration with Behavior, Content, Transformer.
- **Load + inject structured content**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph.

### Renderer

**Key Responsibilities:**
- **Render complex output**: This responsibility involves collaboration with Template, Knowledge Graph, Transformer.
- **Render outputs using components in context**: This responsibility involves collaboration with AI Chat, Template, Content.

### Router

**Key Responsibilities:**
- **Match trigger patterns**: This responsibility involves collaboration with Trigger Words, Route.
- **Route to MCP bot tool**: This responsibility involves collaboration with Base Bot, Trigger Words.
- **Route to behavior tool**: This responsibility involves collaboration with Behavior, Trigger Words.
- **Route to action tool**: This responsibility involves collaboration with Action, Trigger Words.
- **Forward to behavior**: This responsibility involves collaboration with Behavior, Base Bot.
- **Forward to action**: This responsibility involves collaboration with Action, Behavior.
- **Forward to current behavior and action**: This responsibility involves collaboration with Behavior, Action, Base Bot.

### Rule

**Key Responsibilities:**
- **Validate content**: This responsibility involves collaboration with Knowledge Graph, Violations.
- **Find behavior specific rules from context**: This responsibility involves collaboration with Behavior.
- **Find common bot rules from context**: This responsibility involves collaboration with Base Bot.
- **Load + inject diagnostics results**: This responsibility involves collaboration with AI Chat, Violations, Corrections.
- **Suggest corrections**: This responsibility involves collaboration with Violations, Suggestions, Fixes.
- **Provide examples - Do**: This responsibility involves collaboration with Example, Description.
- **Provide examples - Dont**: This responsibility involves collaboration with Example, Description.
- **Specialized examples**: This responsibility involves collaboration with Language, Framework, Pattern.

### Scope

**Key Responsibilities:**
- **Common interface for all scope types**: Common interface for all scope types

### Specific Bot

**Key Responsibilities:**
- **Provide Behavior config**: This responsibility involves collaboration with Bot Config, Behavior.
- **Provide MCP config**: This responsibility involves collaboration with MCP Config.
- **Provide Renderers**: Provide Renderers
- **Provide Extractors**: Provide Extractors
- **Provide Synchronizer**: Provide Synchronizer
- **Provide Trigger Words**: Provide Trigger Words

### StoryScope

**Key Responsibilities:**
- **List of nodes: Node (type + name)**: This responsibility involves collaboration with Node.
- **Node types: STORY, EPIC, SUB_EPIC, INCREMENT**: Node types: STORY, EPIC, SUB_EPIC, INCREMENT
- **Apply to build/render**: This responsibility involves collaboration with BuildActionContext, RenderActionContext.

### Template

**Key Responsibilities:**
- **Define output structure**: This responsibility involves collaboration with Placeholder.
- **Transform content**: This responsibility involves collaboration with Transformer, Content.
- **Load template**: This responsibility involves collaboration with Behavior, Content.

### Typed Results

**Key Responsibilities:**
- **Instructions Phase: ClarifyInstructions, StrategyInstructions, BuildInstructions, RenderInstructions**: Instructions Phase: ClarifyInstructions, StrategyInstructions, BuildInstructions, RenderInstructions
- **Confirmation Phase: ClarifyConfirmation, StrategyConfirmation, BuildConfirmation, RenderConfirmation**: Confirmation Phase: ClarifyConfirmation, StrategyConfirmation, BuildConfirmation, RenderConfirmation
- **Validation: ValidateResult (no separate phases)**: Validation: ValidateResult (no separate phases)

### ValidateRulesAction

**Key Responsibilities:**
- **Inject common bot rules**: This responsibility involves collaboration with Base Bot, Rules, Common Rules.
- **Inject behavior specific rules**: This responsibility involves collaboration with Behavior, Rules, Behavior Rules.
- **Load + inject content for validation**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph, Rendered Outputs.

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
