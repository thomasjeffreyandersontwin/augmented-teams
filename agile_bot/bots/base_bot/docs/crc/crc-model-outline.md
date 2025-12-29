## Module: actions

Base Action
    Inject Instructions: Behavior
    Load Relevant Content + Inject Into Instructions: Content
    Save content changes: Content

Behavior Action State
    Track current action: Action
    Track completed actions: Action,Activity Log
    Determine next action: Action,Behavior
    Pause workflow: Human,AI Chat
    Resume workflow: Human,AI Chat

Content
    Render outputs: Template,Renderer,Render Spec
    Synchronize formats: Synchronizer,Extractor,Synchronizer Spec
    Save knowledge graph: Knowledge Graph
    Load rendered content: na
    Present rendered content: na

Guardrails
    Provide required context: Key Questions,Evidence
    Guide planning decisions: Decision Criteria,Assumptions
    Define recommended human activity: Human,Instructions

Workflow State
    Track current action: Action
    Track completed actions: Action,Activity Log
    Determine next action: Action,Behavior
    Pause workflow: Human,AI Chat
    Resume workflow: Human,AI Chat


## Module: actions.build

BuildKnowledgeAction
    Inject knowledge graph template: Behavior,Content,Knowledge Graph Spec,Knowledge Graph
    Inject builder instructions: Behavior,Content,Build Instructions
    Save Knowledge graph: Behavior,Content,Knowledge Graph


## Module: actions.clarify

GatherContextAction
    Inject gather context instructions: Behavior,Guardrails,Required Clarifications
    Inject questions and evidence: Behavior,Guardrails,Key Questions,Evidence


## Module: actions.render

RenderOutputAction
    Inject render output instructions: Behavior,Content,Render Spec,Renderer
    Inject templates: Behavior,Content,Render Spec,Template
    Inject transformers: Behavior,Content,Transformer
    Load + inject structured content: Behavior,Content,Knowledge Graph

Renderer
    Render complex output: Template,Knowledge Graph,Transformer
    Render outputs using components in context: AI Chat,Template,Content

Template
    Define output structure: Placeholder
    Transform content: Transformer,Content
    Load template: Behavior,Content


## Module: actions.rules

Rule
    Validate content: Knowledge Graph,Violations
    Find behavior specific rules from context: Behavior
    Find common bot rules from context: Base Bot
    Load + inject diagnostics results: AI Chat,Violations,Corrections
    Suggest corrections: Violations,Suggestions,Fixes
    Provide examples - Do: Example,Description
    Provide examples - Dont: Example,Description
    Specialized examples: Language,Framework,Pattern

ValidateRulesAction
    Inject common bot rules: Base Bot,Rules,Common Rules
    Inject behavior specific rules: Behavior,Rules,Behavior Rules
    Load + inject content for validation: Behavior,Content,Knowledge Graph,Rendered Outputs


## Module: actions.strategy

PlanningAction
    Inject planning instructions: Behavior,Guardrails,Planning
    Inject decision criteria and assumptions: Behavior,Guardrails,Decision Criteria,Assumptions,Recommended Human Activity


## Module: actions.validate

CorrectBotAction
    Inject correct bot instructions: Behavior,Correct Bot Instructions
    Load + inject diagnostics results: Content,Diagnostic Report,Violations,Suggestions


## Module: bot

Base Bot
    Executes Actions: Workflow,Behavior,Action
    Track activity: Behavior,Action
    Route to behaviors and actions: Router,Trigger Words
    Persist content: Content
    Manage Project State: Project
    Render: 

Behavior
    Perform Configured Actions: Actions
    Invoke On Trigger Words: List
    Inject Instructions: Text
    Provide Guardrails: GuardRails
    Provide Rules: Rule,Validation
    Provide Content Specs: Content

Behavior Workflow
    Determine next Action: Behavior,Action,State
    Track state: Behavior,Action,State

Project
    Move project to working area: Working Directory
    Save project in context: Working Directory,Workflow State
    Update project area: Working Directory,Content

Specific Bot
    Provide Behavior config: Bot Config,Behavior
    Provide MCP config: MCP Config
    Provide Renderers: 
    Provide Extractors: 
    Provide Synchronizer: 
    Provide Trigger Words: 


## Module: ext

Router
    Match trigger patterns: Trigger Words,Route
    Route to MCP bot tool: Base Bot,Trigger Words
    Route to behavior tool: Behavior,Trigger Words
    Route to action tool: Action,Trigger Words
    Forward to behavior: Behavior,Base Bot
    Forward to action: Action,Behavior
    Forward to current behavior and action: Behavior,Action,Base Bot


## Module: repl_cli

REPLSession
    Runs REPL loop: 
    Reads input from stdin or terminal: 
    Parses command input: CLIBot
    Routes commands to CLI bot: CLIBot
    Displays status and results: CLIBot
    Has CLI bot: CLIBot


## Module: repl_cli.cli_bot

CLIAction
    Get name: str: 
    Get description: str: 
    Is current: bool: 
    Is completed: bool: 
    Executes: ActionResult: Action
    Wraps domain action: Action

CLIActions
    Get all: List[CLIAction]: CLIAction
    Get current: CLIAction: CLIAction
    Find by name: CLIAction: CLIAction
    Wraps domain actions: Actions

CLIBehavior
    Get name: str: 
    Get description: str: 
    Get actions: CLIActions: CLIActions
    Is current: bool: 
    Wraps domain behavior: Behavior

CLIBehaviors
    Get all: List[CLIBehavior]: CLIBehavior
    Get current: CLIBehavior: CLIBehavior
    Find by name: CLIBehavior: CLIBehavior
    Wraps domain behaviors: Behaviors

CLIBot
    Get name: str: 
    Get workspace directory: Path: 
    Get behaviors: CLIBehaviors: CLIBehaviors
    Get status text: str: CLIBehaviors,CLIBehavior,CLIActions,CLIAction
    Wraps domain bot: Bot


## Module: workflow

BehaviorGraphBuilder
    Read behavior workflow definitions: Behavior,Behavior Config
    Create LangGraph StateGraph: LangGraph,BotLangState
    Build node instances from actions: BotLangActionNode,Action
    Connect nodes based on workflow order: LangGraph,BotLangActionNode

BotLangActionNode
    Wrap action.execute(context) method: Action,LangGraph
    Implement two-pass pattern: Action,AI
    Support execution modes: BotMode
    Provide LangGraph entry point: LangGraph

BotLangFlow
    Execute nodes in sequence: BotLangActionNode,BotLangFlowRunner
    Handle conditional branching: Decision Node,BotLangState
    Support loops and iterations: BotLangActionNode,BotLangState
    Pause at interactive points: Human,BotMode
    Resume from checkpoint: Checkpoint,BotLangFlowRunner

BotLangFlowRunner
    Load BotLangFlow Python files: BotLangFlow,File System
    Compile graph with checkpointer: LangGraph,SqliteSaver,Checkpoint
    Execute workflow graph: LangGraph,BotLangActionNode,BotLangState
    Resume from checkpoint: Checkpoint,BotLangState

BotLangState
    Contain story graph: Story Graph
    Contain clarification data: Key Questions,Evidence
    Contain strategy data: Decision Criteria,Assumptions
    Contain context files: Context
    Contain files dictionary: Source Files,Test Files
    Contain workspace directory: Workspace
    Contain workflow execution state: Action,Instructions

BotMode
    Determine AI interaction: BotLangActionNode,AI Client
    Control pause points: BotLangActionNode,Human

Checkpoint
    Save workflow state: BotLangState,BotLangFlowRunner
    Restore workflow state: BotLangState,BotLangFlowRunner
    Track execution history: BotLangState
    Enable resume capability: BotLangFlow,BotLangFlowRunner

