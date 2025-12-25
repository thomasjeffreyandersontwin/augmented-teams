Action Confirmation
    ClarifyConfirmation: Saved To, Questions Answered Count, Evidence Provided Count, Success: 
    StrategyConfirmation: Saved To, Decisions Count, Assumptions Count, Success: 
    BuildConfirmation: Saved To, Mode (create/update), Items Added, Success: 
    RenderConfirmation: Saved To (list), Documents Created Count, Synchronizers Executed, Success: 
    ValidateResult: Passed, Violations, Files Validated Count, Scope, Validation Summary: 
    Save to state: Behavior Action State
    Display to user: Output Formatter
    Advance to next action: Behavior Action State

Action Data Collector
    Sort behaviors: Behavior
    Get behavior actions: Action
    Get action parameters: Action Context
    Get parameter descriptions: Action Context
    Get action description: Action

Action Executor
    Detect operation phase: 
    Execute instructions operation: Action,Action Context
    Execute submit operation: Action,Action Context
    Execute confirm operation: Action,Workflow State
    Capture typed results: Action Instructions,Action Confirmation
    Update state: Behavior Action State

Action Help Context
    Store action name: Action
    Store action description: Action
    Store parameters: Action Context
    Store parameter descriptions: Action Context
    Provide to visitor: Visitor

Action Instructions
    ClarifyInstructions: Key Questions, Evidence Types, Guardrails: 
    StrategyInstructions: Strategy Criteria, Typical Assumptions, Recommended Activities: 
    BuildInstructions: Knowledge Graph Template, Rules, Scope, Story Names: 
    RenderInstructions: Render Specs, Templates, Scope: 
    Display to user: Output Formatter
    Show examples: Scope

Base Action
    Inject Instructions: Behavior
    Load Relevant Content + Inject Into Instructions: Content
    Save content changes: Content

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

Behavior Action State
    Track current action: Action
    Track completed actions: Action,Activity Log
    Determine next action: Action,Behavior
    Pause workflow: Human,AI Chat
    Resume workflow: Human,AI Chat

Behavior Help Context
    Store behavior name: Behavior
    Store behavior description: Behavior
    Store actions: Action
    Provide to visitor: Visitor

Behavior Workflow
    Determine next Action: Behavior,Action,State
    Track state: Behavior,Action,State

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

BuildKnowledgeAction
    Inject knowledge graph template: Behavior,Content,Knowledge Graph Spec,Knowledge Graph
    Inject builder instructions: Behavior,Content,Build Instructions
    Save Knowledge graph: Behavior,Content,Knowledge Graph

Checkpoint
    Save workflow state: BotLangState,BotLangFlowRunner
    Restore workflow state: BotLangState,BotLangFlowRunner
    Track execution history: BotLangState
    Enable resume capability: BotLangFlow,BotLangFlowRunner

Command Router
    Find behavior: Behavior
    Find action: Action
    Detect command type: 
    Route to appropriate operation: Action
    Build context: Context Builder
    Navigate to action: Behavior Action State

Content
    Render outputs: Template,Renderer,Render Spec
    Synchronize formats: Synchronizer,Extractor,Synchronizer Spec
    Save knowledge graph: Knowledge Graph
    Load rendered content: na
    Present rendered content: na

Context Builder
    Build typed context: Action Context
    Build FileScope: FileScope
    Build StoryScope: StoryScope
    Validate parameters: Parameter Parser
    Apply defaults: Scope

CorrectBotAction
    Inject correct bot instructions: Behavior,Correct Bot Instructions
    Load + inject diagnostics results: Content,Diagnostic Report,Violations,Suggestions

Dot Notation Parameters
    Parse key=value pairs: File Scope,Story Scope
    Parse quoted values: File Scope,Story Scope
    Parse comma lists: File Scope,Story Scope

FileScope
    Include file paths: List of paths: 
    Exclude file paths: List of patterns: 
    Apply to build/render: BuildActionContext,RenderActionContext

GatherContextAction
    Inject gather context instructions: Behavior,Guardrails,Required Clarifications
    Inject questions and evidence: Behavior,Guardrails,Key Questions,Evidence

Guardrails
    Provide required context: Key Questions,Evidence
    Guide planning decisions: Decision Criteria,Assumptions
    Define recommended human activity: Human,Instructions

Help Generator
    Generate command help: Behavior,Action
    Generate parameter help: Action Context
    Generate scope examples: FileScope,StoryScope
    Display available nodes: StoryScope
    Display available folders: FileScope

Node
    Node type: STORY, EPIC, SUB_EPIC, INCREMENT: 
    Node name: String identifier: 

Orchestrator
    Walk behaviors: Bot
    Walk actions: Behavior
    Call visitor methods: Visitor
    Provide help context: Action Data Collector

Output Formatter
    Display state: Behavior Action State
    Display instructions: Action Instructions
    Display results: Action Results
    Display help: Help Generator
    Display errors: Parameter Parser

Parameter Parser
    Parse text input: Dot Notation Parameters
    Extract behavior name: Behavior
    Extract action name: Action
    Extract scope: File Scope,Story Scope

PlanningAction
    Inject planning instructions: Behavior,Guardrails,Planning
    Inject decision criteria and assumptions: Behavior,Guardrails,Decision Criteria,Assumptions,Recommended Human Activity

Project
    Move project to working area: Working Directory
    Save project in context: Working Directory,Workflow State
    Update project area: Working Directory,Content

REPL Command Generator
    Walk bot structure: Orchestrator,Bot
    Collect action data: Action Data Collector
    Generate command definitions: REPL Command Visitor
    Generate cursor shortcuts: Cursor REPL Visitor
    Generate help docs: Help REPL Visitor

REPL Command Visitor
    Visit behavior: Behavior Help Context
    Visit action: Action Help Context
    Generate navigate commands: Behavior,Action
    Generate scope commands: File Scope,Story Scope
    Generate instructions commands: Scope
    Generate submit commands: Action Context
    Generate confirm commands: Workflow State

REPL Session
    Display current state: Behavior Action State,Output Formatter
    Read command input: TTY Input
    Parse command input: Parameter Parser
    Detect command type: Command Router
    Route to action operation: Command Router
    Execute action operation: Action Executor
    Display results: Output Formatter
    Loop or exit: 

RenderOutputAction
    Inject render output instructions: Behavior,Content,Render Spec,Renderer
    Inject templates: Behavior,Content,Render Spec,Template
    Inject transformers: Behavior,Content,Transformer
    Load + inject structured content: Behavior,Content,Knowledge Graph

Renderer
    Render complex output: Template,Knowledge Graph,Transformer
    Render outputs using components in context: AI Chat,Template,Content

Router
    Match trigger patterns: Trigger Words,Route
    Route to MCP bot tool: Base Bot,Trigger Words
    Route to behavior tool: Behavior,Trigger Words
    Route to action tool: Action,Trigger Words
    Forward to behavior: Behavior,Base Bot
    Forward to action: Action,Behavior
    Forward to current behavior and action: Behavior,Action,Base Bot

Rule
    Validate content: Knowledge Graph,Violations
    Find behavior specific rules from context: Behavior
    Find common bot rules from context: Base Bot
    Load + inject diagnostics results: AI Chat,Violations,Corrections
    Suggest corrections: Violations,Suggestions,Fixes
    Provide examples - Do: Example,Description
    Provide examples - Dont: Example,Description
    Specialized examples: Language,Framework,Pattern

Scope
    Common interface for all scope types: 

Specific Bot
    Provide Behavior config: Bot Config,Behavior
    Provide MCP config: MCP Config
    Provide Renderers: 
    Provide Extractors: 
    Provide Synchronizer: 
    Provide Trigger Words: 

StoryScope
    List of nodes: Node (type + name): Node
    Node types: STORY, EPIC, SUB_EPIC, INCREMENT: 
    Apply to build/render: BuildActionContext,RenderActionContext

Template
    Define output structure: Placeholder
    Transform content: Transformer,Content
    Load template: Behavior,Content

Typed Results
    Instructions Phase: ClarifyInstructions, StrategyInstructions, BuildInstructions, RenderInstructions: 
    Confirmation Phase: ClarifyConfirmation, StrategyConfirmation, BuildConfirmation, RenderConfirmation: 
    Validation: ValidateResult (no separate phases): 

ValidateRulesAction
    Inject common bot rules: Base Bot,Rules,Common Rules
    Inject behavior specific rules: Behavior,Rules,Behavior Rules
    Load + inject content for validation: Behavior,Content,Knowledge Graph,Rendered Outputs

Workflow State
    Track current action: Action
    Track completed actions: Action,Activity Log
    Determine next action: Action,Behavior
    Pause workflow: Human,AI Chat
    Resume workflow: Human,AI Chat
