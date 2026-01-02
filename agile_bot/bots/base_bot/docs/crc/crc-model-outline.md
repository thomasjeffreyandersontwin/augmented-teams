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


## Module: agile_bot.bots.base_bot.src.synchronizers

Synchronizer
    Synchronizes formats: Source Format,Target Format
    Extracts from source: Extractor,Source File
    Renders to target: Renderer,Target File
    Validates sync: Source,Target,Rules
    Get source_format: String
    Get target_format: String
    Get extractor: Extractor
    Get renderer: Renderer


## Module: agile_bot.bots.story_bot.src.story_bot_cli

StoryBotCLI
    Bootstraps environment: BOT_DIRECTORY,WORKING_AREA,Bot Config
    Delegates to BaseBotCli: Base Bot CLI,Bot Name,Bot Config Path
    Executes CLI: Base Bot CLI,Command Arguments
    Get bot_directory: Path
    Get workspace_directory: Path
    Get bot_name: String
    Get bot_config_path: Path


## Module: agile_bot.bots.story_bot.src.story_bot_mcp_server

ActionStateManager
    Closes current action: Current Action,Behavior,State File
    Loads action state: Behavior,Action State,State File
    Determines next action: Behavior,Action Names,Current Index
    Transitions to next action: Behavior,Current Action,Next Action
    Detects behavior completion: Current Action,Final Action,Behavior
    Transitions to next behavior: Bot,Next Behavior,First Action
    Returns transition result: Status,Completed Action,Next Action
    Handles out-of-order confirmation: Behavior,Confirmation,State File
    Validates human confirmation: Confirmed By,Timestamp
    Persists confirmation: State File,Confirmation Data,JSON
    Get state_file: Path
    Get current_action: Action
    Get next_action: Action
    Get behavior_complete: Boolean
    Get out_of_order_confirmations: Dict

BehaviorToolGenerator
    Generates behavior tool function: Behavior,Trigger Patterns
    Routes to behavior: Bot,Behavior Name
    Routes to action: Behavior,Action Name
    Executes action: Action,Parameters
    Returns result: Bot Result,Status,Data
    Handles missing action: Current Action,State
    Loads action state: Behavior,Action State
    Get tool_name: String
    Get tool_description: String
    Get trigger_patterns: List

StoryBotMCPServer
    Bootstraps environment: BOT_DIRECTORY,WORKING_AREA,Bot Config
    Creates Bot instance: Bot,Bot Config,Bot Directory
    Creates FastMCP server: FastMCP,Server Name
    Registers bot tool: Bot,Current Behavior,Current Action
    Registers behavior tools: Bot,Behavior,Action,Tool Generator
    Registers utility tools: Working Directory Manager,Action State Manager,Server Restart Manager
    Delegates to Bot: Bot,Behavior,Action
    Runs MCP server: FastMCP,Event Loop
    Get bot_directory: Path
    Get workspace_directory: Path
    Get bot: Bot
    Get server: FastMCP

WorkingDirectoryManager
    Gets working directory: Workspace Directory,WORKING_AREA
    Sets working directory: New Path,Persist Flag
    Validates path: Path,Validation Rules
    Updates environment: WORKING_AREA,Environment Variables
    Updates bot config: Bot Config,Working Area,Persist Flag
    Persists to config: Bot Config File,JSON
    Returns previous directory: Previous Path,Workspace Directory
    Get working_directory: Path
    Get previous_directory: Path
    Get persisted: Boolean


## Module: agile_bot.bots.story_bot.src.synchronizers.domain_model.domain_model_synchronizer

DomainModelSynchronizer : Synchronizer
    Syncs CRC text with story graph: CRC Text,Story Graph,Domain Concepts
    Extracts domain concepts: CRC Parser,Concept Extractor
    Renders domain concepts: Concept Renderer,CRC Template
    Validates CRC format: CRC Validator,Format Rules
    Preserves module paths: Module Mapper,Code Structure
    Get crc_path: Path
    Get story_graph_path: Path
    Get domain_concepts: List


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_epic

StoryIOEpic
    Owns features: Feature List,Epic Context
    Calculates total stories: Feature,Story Count
    Renders epic section: Epic Renderer,Template
    Validates epic structure: Epic Validator,Rules
    Get name: String
    Get description: String
    Get features: List
    Get total_stories: Integer
    Get sequential_order: Float


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_feature

StoryIOFeature
    Owns stories: Story List,Feature Context
    Calculates story count: Story,Count
    Renders feature section: Feature Renderer,Template
    Validates feature structure: Feature Validator,Rules
    Get name: String
    Get description: String
    Get stories: List
    Get story_count: Integer


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_increment

StoryIOIncrement
    Owns story assignments: Story List,Increment Context
    Manages priorities: Priority Order,Story Sequence
    Calculates capacity: Story Count,Capacity Limit
    Renders increment view: Increment Renderer,Template
    Validates increment structure: Increment Validator,Rules
    Get number: Integer
    Get name: String
    Get stories: List
    Get capacity: Integer
    Get priority_order: List


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_renderer

StoryIORenderer
    Renders epic cells: Epic,Cell Generator,XML
    Renders feature cells: Feature,Cell Generator,XML
    Renders story cells: Story,Cell Generator,XML
    Renders increment lanes: Increment,Lane Generator,XML
    Calculates layout: Layout Manager,Position Calculator
    Formats XML: XML Formatter,Pretty Print
    Get cell_style: String
    Get layout_config: Dict
    Get xml_formatter: XMLFormatter


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_story

StoryIOStory
    Owns acceptance criteria: Criteria List,Story Context
    Owns increment assignment: Increment,Priority
    Renders story card: Story Renderer,Template
    Validates story format: Story Validator,Rules
    Calculates position: Position Manager,Layout
    Get name: String
    Get description: String
    Get acceptance_criteria: List
    Get increment: Integer
    Get priority: Integer
    Get position: Position


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_synchronizer

StoryIOSynchronizer : Synchronizer
    Syncs story graph with drawio: Story Graph,Drawio File
    Extracts stories from drawio: Drawio Parser,Story Components
    Renders stories to drawio: Story Renderer,Drawio Generator
    Manages story positions: Position Manager,Story Layout
    Updates increments: Increment Manager,Priority Data
    Validates story structure: Structure Validator,Story Rules
    Get story_graph_path: Path
    Get drawio_path: Path
    Get increments: List
    Get epics: List
    Get stories: List


## Module: bot

Action
    Gets instructions for operation: String,Operation

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
    Gets action by name: Action,String
    Gets actions in sequence: List,Action

Behavior Workflow
    Determine next Action: Behavior,Action,State
    Track state: Behavior,Action,State

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


## Module: repl_cli.headless

ActionSummary
    Aggregates operation results: ActionSummary,List,OperationResult
    Reports action completion: String,ActionSummary

BehaviorSummary
    Aggregates action results: BehaviorSummary,List,ActionResult
    Reports behavior completion: String,BehaviorSummary

ErrorRecovery
    Tracks recovery attempt count: RecoveryAttemptCount
    Waits before retry: Duration
    Restarts session: HeadlessSession
    Determines if error is recoverable: RecoverableError,NonRecoverableError
    Enforces max retry limit: RecoveryAttemptCount

ExecutionContext
    Loads from context file: Path
    Get user message: UserMessage
    Get chat history: ChatHistory
    Get file references: FileReference

HeadlessSession
    Invokes with message and context file: Message,ContextFile,ExecutionResult
    Invokes operation with behavior, action, operation, and context file: ExecutionResult,Behavior,Action,Operation,ContextFile
    Invokes complete action with behavior, action, and context file: ExecutionResult,Behavior,Action,ContextFile
    Invokes complete behavior with behavior name and context file: ExecutionResult,Behavior,ContextFile

NonRecoverableError
    Indicates CLI failure: 
    Indicates API connection failure: 
    Indicates max recovery attempts exceeded: RecoveryAttemptCount
    Cannot be retried: 

RecoverableError
    Indicates AI hang: 
    Indicates AI stuck in planning: 
    Can be retried: 

SessionLog
    Creates with timestamped path: Path
    Appends response: Response
    Appends total loops: 
    Get transcript: 


## Module: repl_cli.repl_help

REPLHelp
    Includes headless mode documentation: HeadlessConfig
    Shows headless command examples: 


## Module: repl_cli.status_display

StatusDisplay
    Shows headless availability: HeadlessConfig
    Shows active session status: HeadlessSession


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

