BotLangActionNode
    Wrap action execution: Action,Behavior
    Get instructions from action: Action
    Confirm with response: Action,AI Chat
    Run in autonomous mode: AI Client,BotLangMode
    Run in interactive mode: Human,BotLangMode



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

Behavior Workflow
    Determine next Action: Behavior,Action,State
    Track state: Behavior,Action,State

Checkpoint
    Save workflow state: BotLangState,BotLangFlowRunner
    Restore workflow state: BotLangState,BotLangFlowRunner
    Track execution history: BotLangState
    Enable resume capability: BotLangFlow,BotLangFlowRunner

BotLangMode
    Determine AI interaction: BotLangActionNode,AI Client
    Control pause points: BotLangActionNode,Human

GatherContextAction
    Inject gather context instructions: Behavior,Guardrails,Required Clarifications
    Inject questions and evidence: Behavior,Guardrails,Key Questions,Evidence

Guardrails
    Provide required context: Key Questions,Evidence
    Guide planning decisions: Decision Criteria,Assumptions
    Define recommended human activity: Human,Instructions

BotLangFlow
    Execute nodes in sequence: BotLangActionNode,BotLangFlowRunner
    Handle conditional branching: Decision Node,BotLangState
    Support loops and iterations: BotLangActionNode,BotLangState
    Pause at interactive points: Human,BotLangMode
    Resume from checkpoint: Checkpoint,BotLangFlowRunner

BotLangFlowRunner
    Compile graph with checkpointer: BotLangFlow,Checkpoint
    Execute workflow graph: BotLangFlow,BotLangActionNode
    Manage checkpoint storage: Checkpoint
    Resume from checkpoint: Checkpoint,BotLangFlow

Project
    Move project to working area: Working Directory
    Save project in context: Working Directory,Workflow State
    Update project area: Working Directory,Content

Router
    Match trigger patterns: Trigger Words,Route
    Route to MCP bot tool: Base Bot,Trigger Words
    Route to behavior tool: Behavior,Trigger Words
    Route to action tool: Action,Trigger Words
    Forward to behavior: Behavior,Base Bot
    Forward to action: Action,Behavior
    Forward to current behavior and action: Behavior,Action,Base Bot

Specific Bot
    Provide Behavior config: Bot Config,Behavior
    Provide MCP config: MCP Config
    Provide Renderers: 
    Provide Extractors: 
    Provide Synchronizer: 
    Provide Trigger Words: 

BotLangState
    Contain story graph: Story Graph
    Contain clarification data: Key Questions,Evidence
    Contain strategy data: Decision Criteria,Assumptions
    Contain context files: Context
    Contain files dictionary: Source Files,Test Files
    Contain workspace directory: Workspace
    Contain workflow execution state: Action,Instructions

Behavior Action State
    Track current action: Action
    Track completed actions: Action,Activity Log
    Determine next action: Action,Behavior
    Pause workflow: Human,AI Chat
    Resume workflow: Human,AI Chat
