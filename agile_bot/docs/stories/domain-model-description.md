# Domain Model Description: Agile Bot

**File Name**: `agile-bot-domain-model-description.md`
**Location**: `agile_bot/docs/stories/agile-bot-domain-model-description.md`

## Solution Purpose
Domain model for Agile Bot

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

#### Workflow State

**Key Responsibilities:**
- **Track current action**: This responsibility involves collaboration with Action.
- **Track completed actions**: This responsibility involves collaboration with Action, Activity Log.
- **Determine next action**: This responsibility involves collaboration with Action, Behavior.
- **Pause workflow**: This responsibility involves collaboration with Human, AI Chat.
- **Resume workflow**: This responsibility involves collaboration with Human, AI Chat.

### Module: agile_bot.bots.base_bot.src.synchronizers


#### Synchronizer

**Key Responsibilities:**
- **Synchronizes formats**: This responsibility involves collaboration with Source Format, Target Format.
- **Extracts from source**: This responsibility involves collaboration with Extractor, Source File.
- **Renders to target**: This responsibility involves collaboration with Renderer, Target File.
- **Validates sync**: This responsibility involves collaboration with Source, Target, Rules.
- **Get source_format**: This responsibility involves collaboration with String.
- **Get target_format**: This responsibility involves collaboration with String.
- **Get extractor**: This responsibility involves collaboration with Extractor.
- **Get renderer**: This responsibility involves collaboration with Renderer.

### Module: agile_bot.bots.story_bot.src.story_bot_cli


#### StoryBotCLI

**Key Responsibilities:**
- **Bootstraps environment**: This responsibility involves collaboration with BOT_DIRECTORY, WORKING_AREA, Bot Config.
- **Delegates to BaseBotCli**: This responsibility involves collaboration with Base Bot CLI, Bot Name, Bot Config Path.
- **Executes CLI**: This responsibility involves collaboration with Base Bot CLI, Command Arguments.
- **Get bot_directory**: This responsibility involves collaboration with Path.
- **Get workspace_directory**: This responsibility involves collaboration with Path.
- **Get bot_name**: This responsibility involves collaboration with String.
- **Get bot_config_path**: This responsibility involves collaboration with Path.

### Module: agile_bot.bots.story_bot.src.story_bot_mcp_server


#### ActionStateManager

**Key Responsibilities:**
- **Closes current action**: This responsibility involves collaboration with Current Action, Behavior, State File.
- **Loads action state**: This responsibility involves collaboration with Behavior, Action State, State File.
- **Determines next action**: This responsibility involves collaboration with Behavior, Action Names, Current Index.
- **Transitions to next action**: This responsibility involves collaboration with Behavior, Current Action, Next Action.
- **Detects behavior completion**: This responsibility involves collaboration with Current Action, Final Action, Behavior.
- **Transitions to next behavior**: This responsibility involves collaboration with Bot, Next Behavior, First Action.
- **Returns transition result**: This responsibility involves collaboration with Status, Completed Action, Next Action.
- **Handles out-of-order confirmation**: This responsibility involves collaboration with Behavior, Confirmation, State File.
- **Validates human confirmation**: This responsibility involves collaboration with Confirmed By, Timestamp.
- **Persists confirmation**: This responsibility involves collaboration with State File, Confirmation Data, JSON.
- **Get state_file**: This responsibility involves collaboration with Path.
- **Get current_action**: This responsibility involves collaboration with Action.
- **Get next_action**: This responsibility involves collaboration with Action.
- **Get behavior_complete**: This responsibility involves collaboration with Boolean.
- **Get out_of_order_confirmations**: This responsibility involves collaboration with Dict.

#### BehaviorToolGenerator

**Key Responsibilities:**
- **Generates behavior tool function**: This responsibility involves collaboration with Behavior, Trigger Patterns.
- **Routes to behavior**: This responsibility involves collaboration with Bot, Behavior Name.
- **Routes to action**: This responsibility involves collaboration with Behavior, Action Name.
- **Executes action**: This responsibility involves collaboration with Action, Parameters.
- **Returns result**: This responsibility involves collaboration with Bot Result, Status, Data.
- **Handles missing action**: This responsibility involves collaboration with Current Action, State.
- **Loads action state**: This responsibility involves collaboration with Behavior, Action State.
- **Get tool_name**: This responsibility involves collaboration with String.
- **Get tool_description**: This responsibility involves collaboration with String.
- **Get trigger_patterns**: This responsibility involves collaboration with List.

#### StoryBotMCPServer

**Key Responsibilities:**
- **Bootstraps environment**: This responsibility involves collaboration with BOT_DIRECTORY, WORKING_AREA, Bot Config.
- **Creates Bot instance**: This responsibility involves collaboration with Bot, Bot Config, Bot Directory.
- **Creates FastMCP server**: This responsibility involves collaboration with FastMCP, Server Name.
- **Registers bot tool**: This responsibility involves collaboration with Bot, Current Behavior, Current Action.
- **Registers behavior tools**: This responsibility involves collaboration with Bot, Behavior, Action, Tool Generator.
- **Registers utility tools**: This responsibility involves collaboration with Working Directory Manager, Action State Manager, Server Restart Manager.
- **Delegates to Bot**: This responsibility involves collaboration with Bot, Behavior, Action.
- **Runs MCP server**: This responsibility involves collaboration with FastMCP, Event Loop.
- **Get bot_directory**: This responsibility involves collaboration with Path.
- **Get workspace_directory**: This responsibility involves collaboration with Path.
- **Get bot**: This responsibility involves collaboration with Bot.
- **Get server**: This responsibility involves collaboration with FastMCP.

#### WorkingDirectoryManager

**Key Responsibilities:**
- **Gets working directory**: This responsibility involves collaboration with Workspace Directory, WORKING_AREA.
- **Sets working directory**: This responsibility involves collaboration with New Path, Persist Flag.
- **Validates path**: This responsibility involves collaboration with Path, Validation Rules.
- **Updates environment**: This responsibility involves collaboration with WORKING_AREA, Environment Variables.
- **Updates bot config**: This responsibility involves collaboration with Bot Config, Working Area, Persist Flag.
- **Persists to config**: This responsibility involves collaboration with Bot Config File, JSON.
- **Returns previous directory**: This responsibility involves collaboration with Previous Path, Workspace Directory.
- **Get working_directory**: This responsibility involves collaboration with Path.
- **Get previous_directory**: This responsibility involves collaboration with Path.
- **Get persisted**: This responsibility involves collaboration with Boolean.

### Module: agile_bot.bots.story_bot.src.synchronizers.domain_model.domain_model_synchronizer


#### DomainModelSynchronizer : Synchronizer

**Key Responsibilities:**
- **Syncs CRC text with story graph**: This responsibility involves collaboration with CRC Text, Story Graph, Domain Concepts.
- **Extracts domain concepts**: This responsibility involves collaboration with CRC Parser, Concept Extractor.
- **Renders domain concepts**: This responsibility involves collaboration with Concept Renderer, CRC Template.
- **Validates CRC format**: This responsibility involves collaboration with CRC Validator, Format Rules.
- **Preserves module paths**: This responsibility involves collaboration with Module Mapper, Code Structure.
- **Get crc_path**: This responsibility involves collaboration with Path.
- **Get story_graph_path**: This responsibility involves collaboration with Path.
- **Get domain_concepts**: This responsibility involves collaboration with List.

### Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_epic


#### StoryIOEpic

**Key Responsibilities:**
- **Owns features**: This responsibility involves collaboration with Feature List, Epic Context.
- **Calculates total stories**: This responsibility involves collaboration with Feature, Story Count.
- **Renders epic section**: This responsibility involves collaboration with Epic Renderer, Template.
- **Validates epic structure**: This responsibility involves collaboration with Epic Validator, Rules.
- **Get name**: This responsibility involves collaboration with String.
- **Get description**: This responsibility involves collaboration with String.
- **Get features**: This responsibility involves collaboration with List.
- **Get total_stories**: This responsibility involves collaboration with Integer.
- **Get sequential_order**: This responsibility involves collaboration with Float.

### Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_feature


#### StoryIOFeature

**Key Responsibilities:**
- **Owns stories**: This responsibility involves collaboration with Story List, Feature Context.
- **Calculates story count**: This responsibility involves collaboration with Story, Count.
- **Renders feature section**: This responsibility involves collaboration with Feature Renderer, Template.
- **Validates feature structure**: This responsibility involves collaboration with Feature Validator, Rules.
- **Get name**: This responsibility involves collaboration with String.
- **Get description**: This responsibility involves collaboration with String.
- **Get stories**: This responsibility involves collaboration with List.
- **Get story_count**: This responsibility involves collaboration with Integer.

### Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_increment


#### StoryIOIncrement

**Key Responsibilities:**
- **Owns story assignments**: This responsibility involves collaboration with Story List, Increment Context.
- **Manages priorities**: This responsibility involves collaboration with Priority Order, Story Sequence.
- **Calculates capacity**: This responsibility involves collaboration with Story Count, Capacity Limit.
- **Renders increment view**: This responsibility involves collaboration with Increment Renderer, Template.
- **Validates increment structure**: This responsibility involves collaboration with Increment Validator, Rules.
- **Get number**: This responsibility involves collaboration with Integer.
- **Get name**: This responsibility involves collaboration with String.
- **Get stories**: This responsibility involves collaboration with List.
- **Get capacity**: This responsibility involves collaboration with Integer.
- **Get priority_order**: This responsibility involves collaboration with List.

### Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_renderer


#### StoryIORenderer

**Key Responsibilities:**
- **Renders epic cells**: This responsibility involves collaboration with Epic, Cell Generator, XML.
- **Renders feature cells**: This responsibility involves collaboration with Feature, Cell Generator, XML.
- **Renders story cells**: This responsibility involves collaboration with Story, Cell Generator, XML.
- **Renders increment lanes**: This responsibility involves collaboration with Increment, Lane Generator, XML.
- **Calculates layout**: This responsibility involves collaboration with Layout Manager, Position Calculator.
- **Formats XML**: This responsibility involves collaboration with XML Formatter, Pretty Print.
- **Get cell_style**: This responsibility involves collaboration with String.
- **Get layout_config**: This responsibility involves collaboration with Dict.
- **Get xml_formatter**: This responsibility involves collaboration with XMLFormatter.

### Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_story


#### StoryIOStory

**Key Responsibilities:**
- **Owns acceptance criteria**: This responsibility involves collaboration with Criteria List, Story Context.
- **Owns increment assignment**: This responsibility involves collaboration with Increment, Priority.
- **Renders story card**: This responsibility involves collaboration with Story Renderer, Template.
- **Validates story format**: This responsibility involves collaboration with Story Validator, Rules.
- **Calculates position**: This responsibility involves collaboration with Position Manager, Layout.
- **Get name**: This responsibility involves collaboration with String.
- **Get description**: This responsibility involves collaboration with String.
- **Get acceptance_criteria**: This responsibility involves collaboration with List.
- **Get increment**: This responsibility involves collaboration with Integer.
- **Get priority**: This responsibility involves collaboration with Integer.
- **Get position**: This responsibility involves collaboration with Position.

### Module: agile_bot.bots.story_bot.src.synchronizers.story_io.story_io_synchronizer


#### StoryIOSynchronizer : Synchronizer

**Key Responsibilities:**
- **Syncs story graph with drawio**: This responsibility involves collaboration with Story Graph, Drawio File.
- **Extracts stories from drawio**: This responsibility involves collaboration with Drawio Parser, Story Components.
- **Renders stories to drawio**: This responsibility involves collaboration with Story Renderer, Drawio Generator.
- **Manages story positions**: This responsibility involves collaboration with Position Manager, Story Layout.
- **Updates increments**: This responsibility involves collaboration with Increment Manager, Priority Data.
- **Validates story structure**: This responsibility involves collaboration with Structure Validator, Story Rules.
- **Get story_graph_path**: This responsibility involves collaboration with Path.
- **Get drawio_path**: This responsibility involves collaboration with Path.
- **Get increments**: This responsibility involves collaboration with List.
- **Get epics**: This responsibility involves collaboration with List.
- **Get stories**: This responsibility involves collaboration with List.

### Module: bot


#### Base Bot

**Key Responsibilities:**
- **Executes Actions**: This responsibility involves collaboration with Workflow, Behavior, Action.
- **Execute behavior by name**: This responsibility involves collaboration with Behavior Name, BotResult.
- **Execute current action**: This responsibility involves collaboration with BotResult.
- **Navigate and execute**: This responsibility involves collaboration with Behavior Name, Action Name, ActionContext, BotResult.
- **Validate behavior exists**: This responsibility involves collaboration with Behavior Name, Boolean.
- **Validate action exists**: This responsibility involves collaboration with Behavior Name, Action Name, Boolean.
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
- **Gets action by name**: This responsibility involves collaboration with Action, String.
- **Gets actions in sequence**: This responsibility involves collaboration with List, Action.

#### Specific Bot

**Key Responsibilities:**
- **Provide Behavior config**: This responsibility involves collaboration with Bot Config, Behavior.
- **Provide MCP config**: This responsibility involves collaboration with MCP Config.
- **Provide Renderers**: Provide Renderers
- **Provide Extractors**: Provide Extractors
- **Provide Synchronizer**: Provide Synchronizer
- **Provide Trigger Words**: Provide Trigger Words

### Module: display_panel.extension


#### ActionsView

**Key Responsibilities:**
- **Wraps actions JSON**: This responsibility involves collaboration with Actions JSON.
- **Displays action names list**: This responsibility involves collaboration with List, Action JSON.
- **Navigates to action**: This responsibility involves collaboration with CLI Client, Action.
- **Displays status indicators**: This responsibility involves collaboration with Status, Action JSON.
- **Executes action**: This responsibility involves collaboration with CLI Client, Action.
- **Displays completion progress**: This responsibility involves collaboration with Progress, Action JSON.

#### AvailableBotsView

**Key Responsibilities:**
- **Wraps bot registry JSON**: This responsibility involves collaboration with BotRegistry JSON.
- **Displays available bots**: This responsibility involves collaboration with List, BotRegistry JSON.
- **Selects bot**: This responsibility involves collaboration with CLI Client, Bot.

#### BehaviorsSection

**Key Responsibilities:**
- **Wraps behaviors JSON**: This responsibility involves collaboration with Behaviors JSON.
- **Displays behavior names list**: This responsibility involves collaboration with List, Behavior JSON.
- **Navigates to behavior**: This responsibility involves collaboration with CLI Client, Behavior.
- **Toggles collapsed**: This responsibility involves collaboration with State, Behavior JSON.
- **Displays tooltip**: This responsibility involves collaboration with String, Behavior JSON.
- **Displays actions**: This responsibility involves collaboration with ActionsView.
- **Executes behavior**: This responsibility involves collaboration with CLI Client, Behavior.
- **Displays completion progress**: This responsibility involves collaboration with Status, Behavior JSON.
- **Displays navigation**: This responsibility involves collaboration with NavigationView.

#### BotHeaderView

**Key Responsibilities:**
- **Wraps bot JSON**: This responsibility involves collaboration with Bot JSON.
- **Displays image**: This responsibility involves collaboration with Image.
- **Displays title**: This responsibility involves collaboration with String, Bot JSON.
- **Displays version number**: This responsibility involves collaboration with String, Bot JSON.
- **Refreshes panel**: This responsibility involves collaboration with CLI Client.

#### BuildInstructionsSection

**Key Responsibilities:**
- **Wraps build JSON**: This responsibility involves collaboration with Build JSON.
- **Displays knowledge graph spec**: This responsibility involves collaboration with Object, KnowledgeGraphSpec JSON.
- **Displays graph structure**: This responsibility involves collaboration with Object, KnowledgeGraphSpec JSON.
- **Displays builder instructions**: This responsibility involves collaboration with String, BuilderInstructions JSON.
- **Opens graph file**: This responsibility involves collaboration with CLI Client, Path JSON.

#### ClarifyInstructionsSection

**Key Responsibilities:**
- **Wraps key questions JSON**: This responsibility involves collaboration with KeyQuestions JSON.
- **Displays key questions**: This responsibility involves collaboration with List, KeyQuestion JSON.
- **Updates evidence**: This responsibility involves collaboration with CLI Client, Evidence JSON.
- **Edits answer**: This responsibility involves collaboration with CLI Client, KeyQuestion JSON.

#### EpicView

**Key Responsibilities:**
- **Wraps epic JSON**: This responsibility involves collaboration with Epic JSON.
- **Displays epic name**: This responsibility involves collaboration with String, Epic JSON.
- **Displays epic icon**: This responsibility involves collaboration with Image.
- **Displays sub epics**: This responsibility involves collaboration with SubEpicView, SubEpic JSON.
- **Toggles collapsed**: This responsibility involves collaboration with State.
- **Opens epic folder**: This responsibility involves collaboration with CLI Client, Epic JSON.
- **Opens epic test file**: This responsibility involves collaboration with CLI Client, Epic JSON.

#### FileListTabView

**Key Responsibilities:**
- **Wraps file list JSON**: This responsibility involves collaboration with Path JSON.
- **Displays file names**: This responsibility involves collaboration with List, Path JSON.
- **Searches files**: This responsibility involves collaboration with Filter, Path JSON.
- **Opens file**: This responsibility involves collaboration with CLI Client, Path JSON.

#### InstructionsSection

**Key Responsibilities:**
- **Wraps instructions JSON**: This responsibility involves collaboration with Instructions JSON.
- **Wraps action JSON**: This responsibility involves collaboration with Action JSON.
- **Displays base instructions**: This responsibility involves collaboration with String, Instructions JSON.
- **Displays action data**: This responsibility involves collaboration with Object, Action JSON.
- **Displays raw format**: This responsibility involves collaboration with String, Instructions JSON.
- **Submits to AI chat**: This responsibility involves collaboration with CLI Client, Instructions JSON.

#### NavigationView

**Key Responsibilities:**
- **Wraps current action JSON**: This responsibility involves collaboration with Action JSON.
- **Reruns action**: This responsibility involves collaboration with CLI Client, Action.
- **Navigates to next action**: This responsibility involves collaboration with CLI Client, Action.
- **Navigates to prev action**: This responsibility involves collaboration with CLI Client, Action.

#### Panel

**Key Responsibilities:**
- **Wraps bot JSON**: This responsibility involves collaboration with Bot JSON.
- **Displays BotHeaderView**: This responsibility involves collaboration with BotHeaderView.
- **Displays PathsSection**: This responsibility involves collaboration with PathsSection.
- **Displays BehaviorsSection**: This responsibility involves collaboration with BehaviorsSection.
- **Displays ScopeSection**: This responsibility involves collaboration with ScopeSection.
- **Displays InstructionsSection**: This responsibility involves collaboration with InstructionsSection.

#### PanelHeader

**Key Responsibilities:**
- **Displays header image**: This responsibility involves collaboration with Image.
- **Displays title**: This responsibility involves collaboration with String.

#### PanelView

**Key Responsibilities:**
- **Wraps JSON data**: This responsibility involves collaboration with JSON.
- **Spawns subprocess**: This responsibility involves collaboration with CLI Client, Python Process.
- **Sends command to CLI**: This responsibility involves collaboration with Command, Stdin.
- **Receives JSON from CLI**: This responsibility involves collaboration with Stdout.
- **Parses JSON**: This responsibility involves collaboration with String, Dict.
- **Provides element ID**: This responsibility involves collaboration with String.
- **Renders to HTML**: This responsibility involves collaboration with HTML, JSON.

#### PathsSection

**Key Responsibilities:**
- **Wraps bot paths JSON**: This responsibility involves collaboration with BotPaths JSON.
- **Displays bot directory**: This responsibility involves collaboration with String, BotPaths JSON.
- **Edits workspace directory**: This responsibility involves collaboration with CLI Client, BotPaths JSON.
- **Displays available bots**: This responsibility involves collaboration with AvailableBotsView.

#### RenderInstructionsSection

**Key Responsibilities:**
- **Wraps render JSON**: This responsibility involves collaboration with Render JSON.
- **Displays render spec**: This responsibility involves collaboration with Object, RenderSpec JSON.
- **Displays templates**: This responsibility involves collaboration with List, Template JSON.
- **Displays render instructions**: This responsibility involves collaboration with String, RenderInstructions JSON.
- **Opens template file**: This responsibility involves collaboration with CLI Client, Path JSON.

#### ScenarioView

**Key Responsibilities:**
- **Wraps scenario JSON**: This responsibility involves collaboration with Scenario JSON.
- **Displays scenario name**: This responsibility involves collaboration with String, Scenario JSON.
- **Displays scenario icon**: This responsibility involves collaboration with Image.
- **Opens test at scenario**: This responsibility involves collaboration with CLI Client, Scenario JSON.

#### ScopeSection

**Key Responsibilities:**
- **Wraps scope JSON**: This responsibility involves collaboration with Scope JSON.
- **Displays filtered files**: This responsibility involves collaboration with FileListTabView.
- **Filters story graph**: This responsibility involves collaboration with CLI Client, Scope JSON.
- **Filters files**: This responsibility involves collaboration with CLI Client, Scope JSON.
- **Clears filter**: This responsibility involves collaboration with CLI Client, Scope JSON.
- **Displays story graph**: This responsibility involves collaboration with StoryGraphTabView.

#### SectionView

**Key Responsibilities:**
- **Renders section header**: This responsibility involves collaboration with PanelHeader.
- **Toggles collapsed state**: This responsibility involves collaboration with State.
- **May contain subsections**: This responsibility involves collaboration with SubSectionView.

#### StoryGraphTabView

**Key Responsibilities:**
- **Wraps story map JSON**: This responsibility involves collaboration with StoryMap JSON.
- **Displays epic hierarchy**: This responsibility involves collaboration with EpicView, Epic JSON.
- **Searches stories**: This responsibility involves collaboration with Filter, StoryGraph JSON.
- **Opens story graph file**: This responsibility involves collaboration with CLI Client, File JSON.
- **Opens story map file**: This responsibility involves collaboration with CLI Client, File JSON.

#### StoryView

**Key Responsibilities:**
- **Wraps story JSON**: This responsibility involves collaboration with Story JSON.
- **Displays story name**: This responsibility involves collaboration with String, Story JSON.
- **Displays story icon**: This responsibility involves collaboration with Image.
- **Displays scenarios**: This responsibility involves collaboration with ScenarioView, Scenario JSON.
- **Toggles collapsed**: This responsibility involves collaboration with State.
- **Opens test at class**: This responsibility involves collaboration with CLI Client, Story JSON.

#### StrategyInstructionsSection

**Key Responsibilities:**
- **Wraps strategy JSON**: This responsibility involves collaboration with Strategy JSON.
- **Displays decision criteria**: This responsibility involves collaboration with List, DecisionCriteria JSON.
- **Displays assumptions**: This responsibility involves collaboration with String, Assumptions JSON.
- **Edits decision criterion**: This responsibility involves collaboration with CLI Client, DecisionCriterion JSON.
- **Edits assumption**: This responsibility involves collaboration with CLI Client, Assumption JSON.

#### SubEpicView

**Key Responsibilities:**
- **Wraps sub epic JSON**: This responsibility involves collaboration with SubEpic JSON.
- **Displays sub epic name**: This responsibility involves collaboration with String, SubEpic JSON.
- **Displays sub epic icon**: This responsibility involves collaboration with Image.
- **Displays nested sub epics**: This responsibility involves collaboration with SubEpicView, SubEpic JSON.
- **Displays stories**: This responsibility involves collaboration with StoryView, Story JSON.
- **Toggles collapsed**: This responsibility involves collaboration with State.
- **Opens sub epic folder**: This responsibility involves collaboration with CLI Client, SubEpic JSON.
- **Opens sub epic test file**: This responsibility involves collaboration with CLI Client, SubEpic JSON.

#### SubSectionView

**Key Responsibilities:**
- **Toggles collapsed state**: This responsibility involves collaboration with State.

#### ValidateInstructionsSection

**Key Responsibilities:**
- **Wraps validate JSON**: This responsibility involves collaboration with Validate JSON.
- **Displays rules**: This responsibility involves collaboration with List, Rule JSON.
- **Displays rule descriptions**: This responsibility involves collaboration with String, Rule JSON.
- **Displays rule examples**: This responsibility involves collaboration with List, Rule JSON.
- **Opens rule file**: This responsibility involves collaboration with CLI Client, Path JSON.

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
- **Determine channel adapter**: This responsibility involves collaboration with ChannelAdapter.
- **Read and execute command**: This responsibility involves collaboration with Command String, REPLCommandResponse.
- **Parse command**: This responsibility involves collaboration with Command String, Command Verb, Params.
- **Route to bot domain methods**: This responsibility involves collaboration with Bot, Command Verb, Params, BotResult.
- **Serializes via channel adapter**: This responsibility involves collaboration with ChannelAdapter, String.
- **Displays serialized output**: This responsibility involves collaboration with Stdout.

### Module: repl_cli.adapters


#### ChannelAdapter

**Key Responsibilities:**
- **Serialize domain object to format**: This responsibility involves collaboration with Domain Object, Format.
- **Deserialize format to domain object**: This responsibility involves collaboration with Format, Domain Object.

#### JSONActionAdapter

**Key Responsibilities:**
- **Serialize action to JSON dict**: This responsibility involves collaboration with Action, Dict.
- **Include action metadata**: This responsibility involves collaboration with Name, Description, Status.
- **Wraps domain action**: This responsibility involves collaboration with Action.

#### JSONAdapter

**Key Responsibilities:**
- **Serialize to JSON dict**: This responsibility involves collaboration with Dict.
- **Deserialize JSON dict**: This responsibility involves collaboration with Dict, Domain Object.
- **Convert to JSON string**: This responsibility involves collaboration with Dict, String.
- **Parse JSON string**: This responsibility involves collaboration with String, Dict.
- **Validate JSON structure**: This responsibility involves collaboration with Dict, Schema.

#### JSONBehaviorAdapter

**Key Responsibilities:**
- **Serialize behavior to JSON dict**: This responsibility involves collaboration with Behavior, Dict.
- **Include behavior metadata**: This responsibility involves collaboration with Name, Description, Status.
- **Include actions**: This responsibility involves collaboration with Actions, Array.
- **Wraps domain behavior**: This responsibility involves collaboration with Behavior.

#### JSONBotAdapter

**Key Responsibilities:**
- **Serialize bot to JSON dict**: This responsibility involves collaboration with Bot, Dict.
- **Include bot metadata**: This responsibility involves collaboration with Name, Directory, Paths.
- **Include behaviors**: This responsibility involves collaboration with Behaviors, Array.
- **Wraps domain bot**: This responsibility involves collaboration with Bot.

#### JSONHelpAdapter

**Key Responsibilities:**
- **Serialize help to JSON**: This responsibility involves collaboration with Help, Dict.
- **Include help sections**: This responsibility involves collaboration with Sections, Array.
- **Wraps domain help**: This responsibility involves collaboration with Help.

#### JSONInstructionsAdapter

**Key Responsibilities:**
- **Serialize instructions to JSON**: This responsibility involves collaboration with Instructions, Dict.
- **Include instruction sections**: This responsibility involves collaboration with Sections, Array.
- **Wraps domain instructions**: This responsibility involves collaboration with Instructions.

#### JSONScopeAdapter

**Key Responsibilities:**
- **Serialize scope to JSON dict**: This responsibility involves collaboration with Scope, Dict.
- **Include scope type**: This responsibility involves collaboration with Scope Type, String.
- **Include scope values**: This responsibility involves collaboration with List, Array.
- **Include filtered files**: This responsibility involves collaboration with Files, Array.
- **Wraps domain scope**: This responsibility involves collaboration with Scope.

#### JSONStatusAdapter

**Key Responsibilities:**
- **Include status fields**: This responsibility involves collaboration with Is Completed, Is Current.
- **Include completion markers**: This responsibility involves collaboration with Status String.

#### MarkdownActionAdapter

**Key Responsibilities:**
- **Serialize action to Markdown**: This responsibility involves collaboration with Action, String.
- **Format action documentation**: This responsibility involves collaboration with Action Name, Description, Subsection.
- **Wraps domain action**: This responsibility involves collaboration with Action.

#### MarkdownAdapter

**Key Responsibilities:**
- **Serialize to Markdown**: This responsibility involves collaboration with String.
- **Deserialize Markdown**: This responsibility involves collaboration with String, Domain Object.
- **Parse markdown sections**: This responsibility involves collaboration with Markdown, Sections.
- **Format header**: This responsibility involves collaboration with Level, Text.
- **Format list item**: This responsibility involves collaboration with Marker, Text, Indent.
- **Format code block**: This responsibility involves collaboration with Language, Content.

#### MarkdownBehaviorAdapter

**Key Responsibilities:**
- **Serialize behavior to Markdown**: This responsibility involves collaboration with Behavior, String.
- **Format behavior documentation**: This responsibility involves collaboration with Behavior Name, Description, Section.
- **Format actions**: This responsibility involves collaboration with Actions, Markdown Subsections.
- **Wraps domain behavior**: This responsibility involves collaboration with Behavior.

#### MarkdownBotAdapter

**Key Responsibilities:**
- **Serialize bot to Markdown**: This responsibility involves collaboration with Bot, String.
- **Format bot documentation**: This responsibility involves collaboration with Bot Name, Description, Header.
- **Format behaviors**: This responsibility involves collaboration with Behaviors, Markdown Sections.
- **Wraps domain bot**: This responsibility involves collaboration with Bot.

#### MarkdownHelpAdapter

**Key Responsibilities:**
- **Serialize help to Markdown**: This responsibility involves collaboration with Help, String.
- **Format help sections**: This responsibility involves collaboration with Sections, Markdown.
- **Wraps domain help**: This responsibility involves collaboration with Help.

#### MarkdownInstructionsAdapter

**Key Responsibilities:**
- **Serialize instructions to Markdown**: This responsibility involves collaboration with Instructions, String.
- **Format instruction sections**: This responsibility involves collaboration with Sections, Markdown.
- **Wraps domain instructions**: This responsibility involves collaboration with Instructions.

#### MarkdownScopeAdapter

**Key Responsibilities:**
- **Serialize scope to Markdown**: This responsibility involves collaboration with Scope, String.
- **Format scope documentation**: This responsibility involves collaboration with Scope Type, Values, Section.
- **Wraps domain scope**: This responsibility involves collaboration with Scope.

#### MarkdownStatusAdapter

**Key Responsibilities:**
- **Render status marker**: This responsibility involves collaboration with Status, Marker String.
- **Format status line**: This responsibility involves collaboration with Name, Status, String.

#### TTYActionAdapter

**Key Responsibilities:**
- **Serialize action to TTY**: This responsibility involves collaboration with Action, String.
- **Format action line**: This responsibility involves collaboration with Action Name, Marker, Indent.
- **Wraps domain action**: This responsibility involves collaboration with Action.

#### TTYAdapter

**Key Responsibilities:**
- **Serialize to TTY text**: This responsibility involves collaboration with Domain Object, String.
- **Deserialize TTY text**: This responsibility involves collaboration with String, Domain Object.
- **Add color**: This responsibility involves collaboration with Text, Color.
- **Format indentation**: This responsibility involves collaboration with Indent Level, Spaces.

#### TTYBehaviorAdapter

**Key Responsibilities:**
- **Serialize behavior to TTY**: This responsibility involves collaboration with Behavior, String.
- **Format behavior line**: This responsibility involves collaboration with Behavior Name, Marker, Color.
- **Format actions**: This responsibility involves collaboration with Actions, String.
- **Wraps domain behavior**: This responsibility involves collaboration with Behavior.

#### TTYBotAdapter

**Key Responsibilities:**
- **Serialize bot to TTY**: This responsibility involves collaboration with Bot, String.
- **Format bot header**: This responsibility involves collaboration with Bot Name, String.
- **Format behaviors**: This responsibility involves collaboration with Behaviors, String.
- **Wraps domain bot**: This responsibility involves collaboration with Bot.

#### TTYHelpAdapter

**Key Responsibilities:**
- **Serialize help to TTY**: This responsibility involves collaboration with Help, String.
- **Format help sections**: This responsibility involves collaboration with Sections, String.
- **Wraps domain help**: This responsibility involves collaboration with Help.

#### TTYInstructionsAdapter

**Key Responsibilities:**
- **Serialize instructions to TTY**: This responsibility involves collaboration with Instructions, String.
- **Format instruction sections**: This responsibility involves collaboration with Sections, String.
- **Wraps domain instructions**: This responsibility involves collaboration with Instructions.

#### TTYScopeAdapter

**Key Responsibilities:**
- **Serialize scope to TTY**: This responsibility involves collaboration with Scope, String.
- **Format scope type**: This responsibility involves collaboration with Scope Type, String.
- **Format scope values**: This responsibility involves collaboration with List, String.
- **Wraps domain scope**: This responsibility involves collaboration with Scope.

#### TTYStatusAdapter

**Key Responsibilities:**
- **Format line with marker**: This responsibility involves collaboration with Marker, Text, Indent.
- **Render marker**: This responsibility involves collaboration with Status, Completion.

#### TextAdapter

**Key Responsibilities:**
- **Parse command text**: This responsibility involves collaboration with Text String, Command, Params.

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
