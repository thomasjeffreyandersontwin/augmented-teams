# Domain Model Description: Base Bot

**File Name**: `base-bot-domain-model-description.md`
**Location**: `base_bot/docs/stories/base-bot-domain-model-description.md`

## Solution Purpose
Domain model for Base Bot

---

## Domain Model Descriptions

### Module: actions


#### Base Action

**Key Responsibilities:**
- **Inject Instructions**: This responsibility involves collaboration with Behavior.
- **Load Relevant Content + Inject Into Instructions**: This responsibility involves collaboration with Content.
- **Save content changes**: This responsibility involves collaboration with Content.

#### Behavior Action State

**Key Responsibilities:**
- **Track current action**: This responsibility involves collaboration with Action.
- **Track completed actions**: This responsibility involves collaboration with Action, Activity Log.
- **Determine next action**: This responsibility involves collaboration with Action, Behavior.
- **Pause workflow**: This responsibility involves collaboration with Human, AI Chat.
- **Resume workflow**: This responsibility involves collaboration with Human, AI Chat.

#### Content

**Key Responsibilities:**
- **Render outputs**: This responsibility involves collaboration with Template, Renderer, Render Spec.
- **Synchronize formats**: This responsibility involves collaboration with Synchronizer, Extractor, Synchronizer Spec.
- **Save knowledge graph**: This responsibility involves collaboration with Knowledge Graph.
- **Load rendered content**: This responsibility involves collaboration with na.
- **Present rendered content**: This responsibility involves collaboration with na.

#### Guardrails

**Key Responsibilities:**
- **Provide required context**: This responsibility involves collaboration with Key Questions, Evidence.
- **Guide planning decisions**: This responsibility involves collaboration with Decision Criteria, Assumptions.
- **Define recommended human activity**: This responsibility involves collaboration with Human, Instructions.

#### Workflow State

**Key Responsibilities:**
- **Track current action**: This responsibility involves collaboration with Action.
- **Track completed actions**: This responsibility involves collaboration with Action, Activity Log.
- **Determine next action**: This responsibility involves collaboration with Action, Behavior.
- **Pause workflow**: This responsibility involves collaboration with Human, AI Chat.
- **Resume workflow**: This responsibility involves collaboration with Human, AI Chat.

### Module: actions.build


#### BuildKnowledgeAction

**Key Responsibilities:**
- **Inject knowledge graph template**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph Spec, Knowledge Graph.
- **Inject builder instructions**: This responsibility involves collaboration with Behavior, Content, Build Instructions.
- **Save Knowledge graph**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph.

### Module: actions.clarify


#### GatherContextAction

**Key Responsibilities:**
- **Inject gather context instructions**: This responsibility involves collaboration with Behavior, Guardrails, Required Clarifications.
- **Inject questions and evidence**: This responsibility involves collaboration with Behavior, Guardrails, Key Questions, Evidence.

### Module: actions.render


#### RenderOutputAction

**Key Responsibilities:**
- **Inject render output instructions**: This responsibility involves collaboration with Behavior, Content, Render Spec, Renderer.
- **Inject templates**: This responsibility involves collaboration with Behavior, Content, Render Spec, Template.
- **Inject transformers**: This responsibility involves collaboration with Behavior, Content, Transformer.
- **Load + inject structured content**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph.

#### Renderer

**Key Responsibilities:**
- **Render complex output**: This responsibility involves collaboration with Template, Knowledge Graph, Transformer.
- **Render outputs using components in context**: This responsibility involves collaboration with AI Chat, Template, Content.

#### Template

**Key Responsibilities:**
- **Define output structure**: This responsibility involves collaboration with Placeholder.
- **Transform content**: This responsibility involves collaboration with Transformer, Content.
- **Load template**: This responsibility involves collaboration with Behavior, Content.

### Module: actions.rules


#### Rule

**Key Responsibilities:**
- **Validate content**: This responsibility involves collaboration with Knowledge Graph, Violations.
- **Find behavior specific rules from context**: This responsibility involves collaboration with Behavior.
- **Find common bot rules from context**: This responsibility involves collaboration with Base Bot.
- **Load + inject diagnostics results**: This responsibility involves collaboration with AI Chat, Violations, Corrections.
- **Suggest corrections**: This responsibility involves collaboration with Violations, Suggestions, Fixes.
- **Provide examples - Do**: This responsibility involves collaboration with Example, Description.
- **Provide examples - Dont**: This responsibility involves collaboration with Example, Description.
- **Specialized examples**: This responsibility involves collaboration with Language, Framework, Pattern.

#### ValidateRulesAction

**Key Responsibilities:**
- **Inject common bot rules**: This responsibility involves collaboration with Base Bot, Rules, Common Rules.
- **Inject behavior specific rules**: This responsibility involves collaboration with Behavior, Rules, Behavior Rules.
- **Load + inject content for validation**: This responsibility involves collaboration with Behavior, Content, Knowledge Graph, Rendered Outputs.

### Module: actions.strategy


#### PlanningAction

**Key Responsibilities:**
- **Inject planning instructions**: This responsibility involves collaboration with Behavior, Guardrails, Planning.
- **Inject decision criteria and assumptions**: This responsibility involves collaboration with Behavior, Guardrails, Decision Criteria, Assumptions, Recommended Human Activity.

### Module: actions.validate


#### CorrectBotAction

**Key Responsibilities:**
- **Inject correct bot instructions**: This responsibility involves collaboration with Behavior, Correct Bot Instructions.
- **Load + inject diagnostics results**: This responsibility involves collaboration with Content, Diagnostic Report, Violations, Suggestions.

### Module: bot


#### Base Bot

**Key Responsibilities:**
- **Executes Actions**: This responsibility involves collaboration with Workflow, Behavior, Action.
- **Track activity**: This responsibility involves collaboration with Behavior, Action.
- **Route to behaviors and actions**: This responsibility involves collaboration with Router, Trigger Words.
- **Persist content**: This responsibility involves collaboration with Content.
- **Manage Project State**: This responsibility involves collaboration with Project.
- **Render**: Render

#### Behavior

**Key Responsibilities:**
- **Perform Configured Actions**: This responsibility involves collaboration with Actions.
- **Invoke On Trigger Words**: This responsibility involves collaboration with List.
- **Inject Instructions**: This responsibility involves collaboration with Text.
- **Provide Guardrails**: This responsibility involves collaboration with GuardRails.
- **Provide Rules**: This responsibility involves collaboration with Rule, Validation.
- **Provide Content Specs**: This responsibility involves collaboration with Content.

#### Behavior Workflow

**Key Responsibilities:**
- **Determine next Action**: This responsibility involves collaboration with Behavior, Action, State.
- **Track state**: This responsibility involves collaboration with Behavior, Action, State.

#### Project

**Key Responsibilities:**
- **Move project to working area**: This responsibility involves collaboration with Working Directory.
- **Save project in context**: This responsibility involves collaboration with Working Directory, Workflow State.
- **Update project area**: This responsibility involves collaboration with Working Directory, Content.

#### Specific Bot

**Key Responsibilities:**
- **Provide Behavior config**: This responsibility involves collaboration with Bot Config, Behavior.
- **Provide MCP config**: This responsibility involves collaboration with MCP Config.
- **Provide Renderers**: Provide Renderers
- **Provide Extractors**: Provide Extractors
- **Provide Synchronizer**: Provide Synchronizer
- **Provide Trigger Words**: Provide Trigger Words

### Module: ext


#### Router

**Key Responsibilities:**
- **Match trigger patterns**: This responsibility involves collaboration with Trigger Words, Route.
- **Route to MCP bot tool**: This responsibility involves collaboration with Base Bot, Trigger Words.
- **Route to behavior tool**: This responsibility involves collaboration with Behavior, Trigger Words.
- **Route to action tool**: This responsibility involves collaboration with Action, Trigger Words.
- **Forward to behavior**: This responsibility involves collaboration with Behavior, Base Bot.
- **Forward to action**: This responsibility involves collaboration with Action, Behavior.
- **Forward to current behavior and action**: This responsibility involves collaboration with Behavior, Action, Base Bot.

### Module: repl_cli


#### REPLSession

**Key Responsibilities:**
- **Runs REPL loop**: Runs REPL loop
- **Reads input from stdin or terminal**: Reads input from stdin or terminal
- **Parses command input**: This responsibility involves collaboration with CLIBot.
- **Routes commands to CLI bot**: This responsibility involves collaboration with CLIBot.
- **Displays status and results**: This responsibility involves collaboration with CLIBot.
- **Has CLI bot**: This responsibility involves collaboration with CLIBot.

### Module: repl_cli.cli_bot


#### CLIAction

**Key Responsibilities:**
- **Get name: str**: Get name: str
- **Get description: str**: Get description: str
- **Is current: bool**: Is current: bool
- **Is completed: bool**: Is completed: bool
- **Executes: ActionResult**: This responsibility involves collaboration with Action.
- **Wraps domain action**: This responsibility involves collaboration with Action.

#### CLIActions

**Key Responsibilities:**
- **Get all: List[CLIAction]**: This responsibility involves collaboration with CLIAction.
- **Get current: CLIAction**: This responsibility involves collaboration with CLIAction.
- **Find by name: CLIAction**: This responsibility involves collaboration with CLIAction.
- **Wraps domain actions**: This responsibility involves collaboration with Actions.

#### CLIBehavior

**Key Responsibilities:**
- **Get name: str**: Get name: str
- **Get description: str**: Get description: str
- **Get actions: CLIActions**: This responsibility involves collaboration with CLIActions.
- **Is current: bool**: Is current: bool
- **Wraps domain behavior**: This responsibility involves collaboration with Behavior.

#### CLIBehaviors

**Key Responsibilities:**
- **Get all: List[CLIBehavior]**: This responsibility involves collaboration with CLIBehavior.
- **Get current: CLIBehavior**: This responsibility involves collaboration with CLIBehavior.
- **Find by name: CLIBehavior**: This responsibility involves collaboration with CLIBehavior.
- **Wraps domain behaviors**: This responsibility involves collaboration with Behaviors.

#### CLIBot

**Key Responsibilities:**
- **Get name: str**: Get name: str
- **Get workspace directory: Path**: Get workspace directory: Path
- **Get behaviors: CLIBehaviors**: This responsibility involves collaboration with CLIBehaviors.
- **Get status text: str**: This responsibility involves collaboration with CLIBehaviors, CLIBehavior, CLIActions, CLIAction.
- **Wraps domain bot**: This responsibility involves collaboration with Bot.

### Module: workflow


#### BehaviorGraphBuilder

**Key Responsibilities:**
- **Read behavior workflow definitions**: This responsibility involves collaboration with Behavior, Behavior Config.
- **Create LangGraph StateGraph**: This responsibility involves collaboration with LangGraph, BotLangState.
- **Build node instances from actions**: This responsibility involves collaboration with BotLangActionNode, Action.
- **Connect nodes based on workflow order**: This responsibility involves collaboration with LangGraph, BotLangActionNode.

#### BotLangActionNode

**Key Responsibilities:**
- **Wrap action.execute(context) method**: This responsibility involves collaboration with Action, LangGraph.
- **Implement two-pass pattern**: This responsibility involves collaboration with Action, AI.
- **Support execution modes**: This responsibility involves collaboration with BotMode.
- **Provide LangGraph entry point**: This responsibility involves collaboration with LangGraph.

#### BotLangFlow

**Key Responsibilities:**
- **Execute nodes in sequence**: This responsibility involves collaboration with BotLangActionNode, BotLangFlowRunner.
- **Handle conditional branching**: This responsibility involves collaboration with Decision Node, BotLangState.
- **Support loops and iterations**: This responsibility involves collaboration with BotLangActionNode, BotLangState.
- **Pause at interactive points**: This responsibility involves collaboration with Human, BotMode.
- **Resume from checkpoint**: This responsibility involves collaboration with Checkpoint, BotLangFlowRunner.

#### BotLangFlowRunner

**Key Responsibilities:**
- **Load BotLangFlow Python files**: This responsibility involves collaboration with BotLangFlow, File System.
- **Compile graph with checkpointer**: This responsibility involves collaboration with LangGraph, SqliteSaver, Checkpoint.
- **Execute workflow graph**: This responsibility involves collaboration with LangGraph, BotLangActionNode, BotLangState.
- **Resume from checkpoint**: This responsibility involves collaboration with Checkpoint, BotLangState.

#### BotLangState

**Key Responsibilities:**
- **Contain story graph**: This responsibility involves collaboration with Story Graph.
- **Contain clarification data**: This responsibility involves collaboration with Key Questions, Evidence.
- **Contain strategy data**: This responsibility involves collaboration with Decision Criteria, Assumptions.
- **Contain context files**: This responsibility involves collaboration with Context.
- **Contain files dictionary**: This responsibility involves collaboration with Source Files, Test Files.
- **Contain workspace directory**: This responsibility involves collaboration with Workspace.
- **Contain workflow execution state**: This responsibility involves collaboration with Action, Instructions.

#### BotMode

**Key Responsibilities:**
- **Determine AI interaction**: This responsibility involves collaboration with BotLangActionNode, AI Client.
- **Control pause points**: This responsibility involves collaboration with BotLangActionNode, Human.

#### Checkpoint

**Key Responsibilities:**
- **Save workflow state**: This responsibility involves collaboration with BotLangState, BotLangFlowRunner.
- **Restore workflow state**: This responsibility involves collaboration with BotLangState, BotLangFlowRunner.
- **Track execution history**: This responsibility involves collaboration with BotLangState.
- **Enable resume capability**: This responsibility involves collaboration with BotLangFlow, BotLangFlowRunner.

---

## Source Material

**Primary Source:** `input.txt`
**Date Generated:** 2025-01-27
**Context:** Shape phase - Domain model extracted from story-graph.json
