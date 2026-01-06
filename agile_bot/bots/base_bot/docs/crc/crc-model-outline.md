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

BuildKnowledgeAction
    Inject knowledge graph template: Behavior,Content,Knowledge Graph Spec,Knowledge Graph
    Inject builder instructions: Behavior,Content,Build Instructions
    Save Knowledge graph: Behavior,Content,Knowledge Graph

GatherContextAction
    Inject gather context instructions: Behavior,Guardrails,Required Clarifications
    Inject questions and evidence: Behavior,Guardrails,Key Questions,Evidence

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

PlanningAction
    Inject planning instructions: Behavior,Guardrails,Planning
    Inject decision criteria and assumptions: Behavior,Guardrails,Decision Criteria,Assumptions,Recommended Human Activity

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


## Module: agile_bot.bots.story_bot.src.synchronizers.story_io

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

StoryIOFeature
    Owns stories: Story List,Feature Context
    Calculates story count: Story,Count
    Renders feature section: Feature Renderer,Template
    Validates feature structure: Feature Validator,Rules
    Get name: String
    Get description: String
    Get stories: List
    Get story_count: Integer

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

Base Bot
    Executes Actions: Workflow,Behavior,Action
    Execute behavior by name: Behavior Name,BotResult
    Execute current action: BotResult
    Navigate and execute: Behavior Name,Action Name,ActionContext,BotResult
    Validate behavior exists: Behavior Name,Boolean
    Validate action exists: Behavior Name,Action Name,Boolean
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


## Module: display_panel.extension

PanelView (Base)
    Wraps JSON data: JSON
    Spawns subprocess: CLI,Python Process
    Sends command to CLI: Command,Stdin
    Receives JSON from CLI: Stdout
    Parses JSON: String,Dict
    Provides element ID: String
    Renders to HTML: HTML,JSON

Panel: PanelView
    Wraps bot JSON: Bot JSON
    Displays BotHeaderView: BotHeaderView
    Displays PathsSection: PathsSection
    Displays BehaviorsSection: BehaviorsSection
    Displays ScopeSection: ScopeSection
    Displays InstructionsSection: InstructionsSection

BotHeaderView: PanelView
    Wraps bot JSON: Bot JSON
    Displays image: Image
    Displays title: String,Bot JSON
    Displays version number: String,Bot JSON
    Refreshes panel: CLI

PanelHeader
    Displays header image: Image
    Displays title: String

SectionView : PanelView (Base)
    Renders section header: PanelHeader
    Toggles collapsed state: State
    May contain subsections: SubSectionView

PathsSection : SectionView
    Wraps bot paths JSON: BotPaths JSON
    Displays bot directory: String, BotPaths JSON
    Edits workspace directory: CLI, BotPaths JSON
    Displays available bots: AvailableBotsView

AvailableBotsView : PanelView
    Wraps bot registry JSON: BotRegistry JSON
    Displays available bots: List,BotRegistry JSON
    Selects bot: CLI,Bot

SubSectionView: PanelView
    Toggles collapsed state: State

BehaviorsSection : SectionView
    Wraps behaviors JSON: Behaviors JSON
    Displays behavior names list: List,Behavior JSON
    Navigates to behavior: CLI,Behavior
    Toggles collapsed: State,Behavior JSON
    Displays tooltip: String,Behavior JSON
    Displays actions: ActionsView
    Executes behavior: CLI,Behavior
    Displays completion progress: Status,Behavior JSON
    Displays navigation: NavigationView

NavigationView : PanelView  
    Wraps current action JSON: Action JSON
    Reruns action: CLI,Action
    Navigates to next action: CLI,Action
    Navigates to prev action: CLI,Action

ActionsView : PanelView
    Wraps actions JSON: Actions JSON
    Displays action names list: List,Action JSON
    Navigates to action: CLI,Action
    Displays status indicators: Status,Action JSON
    Executes action: CLI, Action
    Displays completion progress: Progress,Action JSON

ScopeSection : SectionView
    Wraps scope JSON: Scope JSON
    Displays filtered files: FileListTabView
    Filters story graph: CLI,Scope JSON
    Filters files: CLI,Scope JSON
    Clears filter: CLI,Scope JSON
    Displays story graph: StoryGraphTabView
 
StoryGraphTabView : PanelView
    Wraps story map JSON: StoryMap JSON
    Displays epic hierarchy: EpicView,Epic JSON
    Searches stories: Filter,StoryGraph JSON
    Opens story graph file: CLI,File JSON
    Opens story map file: CLI,File JSON

EpicView : PanelView
    Wraps epic JSON: Epic JSON
    Displays epic name: String,Epic JSON
    Displays epic icon: Image
    Displays sub epics: SubEpicView,SubEpic JSON
    Toggles collapsed: State
    Opens epic folder: CLI,Epic JSON
    Opens epic test file: CLI,Epic JSON

SubEpicView : PanelView
    Wraps sub epic JSON: SubEpic JSON
    Displays sub epic name: String,SubEpic JSON
    Displays sub epic icon: Image
    Displays nested sub epics: SubEpicView,SubEpic JSON
    Displays stories: StoryView,Story JSON
    Toggles collapsed: State
    Opens sub epic folder: CLI,SubEpic JSON
    Opens sub epic test file: CLI,SubEpic JSON

StoryView : PanelView
    Wraps story JSON: Story JSON
    Displays story name: String,Story JSON
    Displays story icon: Image
    Displays scenarios: ScenarioView,Scenario JSON
    Toggles collapsed: State
    Opens test at class: CLI,Story JSON

ScenarioView : PanelView
    Wraps scenario JSON: Scenario JSON
    Displays scenario name: String,Scenario JSON
    Displays scenario icon: Image
    Opens test at scenario: CLI,Scenario JSON

FileListTabView : PanelView
    Wraps file list JSON: Path JSON
    Displays file names: List,Path JSON
    Searches files: Filter,Path JSON
    Opens file: CLI,Path JSON

InstructionsSection : SectionView (Base)
    Wraps instructions JSON: Instructions JSON
    Wraps action JSON: Action JSON
    Displays base instructions subsection: BaseInstructionsSubSection
    Displays raw format subsection: RawFormatSubSection
    Submits to AI chat: CLI,Instructions JSON

BaseInstructionsSubSection : SubSectionView
    Wraps instructions JSON: Instructions JSON
    Displays behavior name: String,Instructions JSON
    Displays action name: String,Instructions JSON
    Displays  Instructions: Instructions JSON

ActionDataSubSection : SubSectionView
    Wraps action JSON: Action JSON
    Displays action properties: Object,Action JSON

RawFormatSubSection : SubSectionView
    Wraps instructions JSON: Instructions JSON
    Displays raw instructions: String,Instructions JSON

ClarifyInstructionsSection : InstructionsSection
    Wraps clarify subsection: ClarifyDataSubSection

ClarifyDataSubSection : SubSectionView
    Wraps key questions JSON: KeyQuestions JSON
    Displays key questions: List,KeyQuestion JSON
    Updates evidence: CLI,Evidence JSON
    Edits answer: CLI,KeyQuestion JSON

StrategyInstructionsSection : InstructionsSection
    Wraps strategy subsection: StrategyDataSubSection

StrategyDataSubSection : SubSectionView
    Wraps strategy JSON: Strategy JSON
    Displays decision criteria: List,DecisionCriteria JSON
    Displays assumptions: String,Assumptions JSON
    Edits decision criterion: CLI,DecisionCriterion JSON
    Edits assumption: CLI,Assumption JSON

BuildInstructionsSection : InstructionsSection
    Wraps build subsection: BuildDataSubSection

BuildDataSubSection : SubSectionView
    Wraps build JSON: Build JSON
    Displays knowledge graph spec: Object,KnowledgeGraphSpec JSON
    Displays graph structure: Object,KnowledgeGraphSpec JSON
    Displays builder instructions: String,BuilderInstructions JSON
    Opens graph file: CLI,Path JSON

ValidateInstructionsSection : InstructionsSection
    Wraps validate subsection: ValidateDataSubSection

ValidateDataSubSection : SubSectionView
    Wraps validate JSON: Validate JSON
    Displays rules: List,Rule JSON
    Displays rule descriptions: String,Rule JSON
    Displays rule examples: List,Rule JSON
    Opens rule file: CLI,Path JSON

RenderInstructionsSection : InstructionsSection
    Wraps render subsection: RenderDataSubSection

RenderDataSubSection : SubSectionView
    Wraps render JSON: Render JSON
    Displays render spec: Object,RenderSpec JSON
    Displays templates: List,Template JSON
    Displays render instructions: String,RenderInstructions JSON
    Opens template file: CLI,Path JSON


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
    Determine channel adapter: ChannelAdapter
    Read and execute command: Command String,REPLCommandResponse
    Parse command: Command String,Command Verb,Params
    Route to bot domain methods: Bot,Command Verb,Params,BotResult
    Serializes via channel adapter: ChannelAdapter,String
    Displays serialized output: Stdout
    

## Module: repl_cli.adapters

ChannelAdapter (Abstract)
    Serialize domain object to format: Domain Object,Format
    Deserialize format to domain object: Format,Domain Object

TextAdapter : ChannelAdapter (Abstract)
    Parse command text: Text String,Command,Params

TTYAdapter : TextAdapter (Abstract)
    Serialize to TTY text: Domain Object,String
    Deserialize TTY text: String,Domain Object
    Add color: Text,Color
    Format indentation: Indent Level,Spaces

TTYStatusAdapter : TTYAdapter (Abstract)
    Format line with marker: Marker,Text,Indent
    Render marker: Status,Completion

TTYInstructionsAdapter : TTYAdapter
    Serialize instructions to TTY: Instructions,String
    Format instruction sections: Sections,String
    Wraps domain instructions: Instructions

TTYHelpAdapter : TTYAdapter
    Serialize help to TTY: Help,String
    Format help sections: Sections,String
    Wraps domain help: Help

TTYBotAdapter : TTYStatusAdapter
    Serialize bot to TTY: Bot,String
    Format bot header: Bot Name,String
    Format behaviors: Behaviors,String
    Wraps domain bot: Bot

TTYBehaviorAdapter : TTYStatusAdapter
    Serialize behavior to TTY: Behavior,String
    Format behavior line: Behavior Name,Marker,Color
    Format actions: Actions,String
    Wraps domain behavior: Behavior

TTYActionAdapter : TTYStatusAdapter
    Serialize action to TTY: Action,String
    Format action line: Action Name,Marker,Indent
    Wraps domain action: Action

TTYScopeAdapter : TTYAdapter
    Serialize scope to TTY: Scope,String
    Format scope type: Scope Type,String
    Format scope values: List,String
    Wraps domain scope: Scope

JSONAdapter : ChannelAdapter (Abstract)
    Serialize to JSON dict: Dict
    Deserialize JSON dict: Dict, Domain Object
    Convert to JSON string: Dict, String
    Parse JSON string: String, Dict
    Validate JSON structure: Dict, Schema

JSONStatusAdapter : JSONAdapter (Abstract)
    Include status fields: Is Completed, Is Current
    Include completion markers: Status String

JSONInstructionsAdapter : JSONAdapter
    Serialize instructions to JSON: Instructions,Dict
    Include instruction sections: Sections,Array
    Wraps domain instructions: Instructions

JSONHelpAdapter : JSONAdapter
    Serialize help to JSON: Help,Dict
    Include help sections: Sections,Array
    Wraps domain help: Help

JSONBotAdapter : JSONStatusAdapter
    Serialize bot to JSON dict: Bot,Dict
    Include bot metadata: Name,Directory,Paths
    Include behaviors: Behaviors,Array
    Wraps domain bot: Bot

JSONBehaviorAdapter : JSONStatusAdapter
    Serialize behavior to JSON dict: Behavior,Dict
    Include behavior metadata: Name,Description,Status
    Include actions: Actions,Array
    Wraps domain behavior: Behavior

JSONActionAdapter : JSONStatusAdapter
    Serialize action to JSON dict: Action,Dict
    Include action metadata: Name,Description,Status
    Wraps domain action: Action

JSONScopeAdapter : JSONAdapter
    Serialize scope to JSON dict: Scope,Dict
    Include scope type: Scope Type,String
    Include scope values: List,Array
    Include filtered files: Files,Array
    Wraps domain scope: Scope

MarkdownAdapter : TextAdapter (Abstract)
    Serialize to Markdown: String
    Deserialize Markdown: String, Domain Object
    Parse markdown sections: Markdown, Sections
    Format header: Level,Text
    Format list item: Marker, Text, Indent
    Format code block: Language, Content

MarkdownStatusAdapter : MarkdownAdapter (Abstract)
    Render status marker: Status, Marker String
    Format status line: Name, Status, String

MarkdownInstructionsAdapter : MarkdownAdapter
    Serialize instructions to Markdown: Instructions,String
    Format instruction sections: Sections,Markdown
    Wraps domain instructions: Instructions

MarkdownHelpAdapter : MarkdownAdapter
    Serialize help to Markdown: Help,String
    Format help sections: Sections,Markdown
    Wraps domain help: Help

MarkdownBotAdapter : MarkdownStatusAdapter
    Serialize bot to Markdown: Bot,String
    Format bot documentation: Bot Name,Description,Header
    Format behaviors: Behaviors,Markdown Sections
    Wraps domain bot: Bot

MarkdownBehaviorAdapter : MarkdownStatusAdapter
    Serialize behavior to Markdown: Behavior,String
    Format behavior documentation: Behavior Name,Description,Section
    Format actions: Actions,Markdown Subsections
    Wraps domain behavior: Behavior

MarkdownActionAdapter : MarkdownStatusAdapter
    Serialize action to Markdown: Action,String
    Format action documentation: Action Name,Description,Subsection
    Wraps domain action: Action

MarkdownScopeAdapter : MarkdownAdapter
    Serialize scope to Markdown: Scope,String
    Format scope documentation: Scope Type,Values,Section
    Wraps domain scope: Scope