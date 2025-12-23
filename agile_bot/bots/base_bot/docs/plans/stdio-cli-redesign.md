# STDIO CLI Redesign Plan

> CLI redesign to support interactive STDIO mode, dot-notation parameters,
> and human-friendly interfaces while maintaining AI/automation compatibility.

---

## The Problem

Current CLI has these pain points:

1. **JSON in shell is brutal:**

   ```bash
   --scope "{'type': 'epic', 'value': ['Epic Name']}"
   ```

   Quoting hell, escaping nightmares, impossible to type correctly.
2. **All-or-nothing parameters** - must know everything upfront
3. **No conversation** - can't ask follow-up questions when info is missing
4. **AI must construct perfect strings** - fragile, error-prone

---

## Core Design Insight

STDIO just means this:

Instead of stuffing meaning into command-line arguments,
your CLI has a conversation through standard input and output.

Think of it like this:

- The command line starts the program
- Then the program asks for what it needs
- Something else (AI, a script, or even a human) answers

So instead of:
one giant command with fragile parameters
You get:
a stable command + a structured exchange

This is why STDIO works so well with AI:

- Ordering is explicit
- No quoting problems
- No shell parsing issues
- You can evolve it without breaking callers

It's basically RPC over stdin/stdout, not "arguments".

---

## Domain Model

```
REPL Session
    Display current state: Behavior Action State, Output Formatter
    Read command input: TTY Input
    Parse command input: Parameter Parser
    Detect command type: Instruction Command, Confirm Command, Navigation Command
    Route to action operation: Command Router
    Execute action operation: Action Executor
    Display results: Output Formatter
    Loop or exit: REPL Session

Behavior Action State
    Track current behavior: Behavior
    Track current action: Action
    Track action phase: Provide Instructions Phase, Confirm Submit Phase
    Store completed actions: Completed Actions
    Store clarifications: Clarifications
    Store strategy decisions: Strategy Decisions
    Store scope: File Scope, Story Scope
    Persist to file: behavior_action_state.json

Command Types
    Instruction Command: Run action.provide_instructions with scope
    Confirm Command: Run action.confirm_submit with completed work  
    Navigation Command: Change current behavior or action
    Status Command: Display current state
    Help Command: Display available commands and parameters

Action Phases
    Provide Instructions Phase
        User provides: Scope (optional)
        Action returns: AI instructions with templates, rules, questions
        State: Waiting for user to complete work
    Confirm Submit Phase
        User provides: Completed work (clarifications, decisions, graphs, documents)
        Action returns: Confirmation with saved files, validation results
        State: Ready to advance to next action

Parameter Parser
    Parse text input: Dot Notation Parameters
    Extract behavior name: Behavior
    Extract action name: Action
    Extract scope: File Scope, Story Scope

Dot Notation Parameters
    Parse key=value pairs: File Scope, Story Scope
    Parse quoted values: File Scope, Story Scope
    Parse comma lists: File Scope, Story Scope

Command Router
    Find behavior: Behavior
    Find action: Action
    Detect command type: Instruction Command, Confirm Command, Navigation Command
    Route to appropriate operation: provide_instructions, confirm_submit
    Build context: Context Builder
    Navigate to action: Behavior Action State

Context Builder
    Build typed context: Action Context
    Build FileScope: Include paths, Exclude patterns
    Build StoryScope: Parse nodes (type + name)
    Validate parameters: Parameter Parser
    Apply defaults: Scope

Action Executor
    Detect operation phase: Provide Instructions Phase, Confirm Submit Phase
    Execute provide_instructions: Action, ActionContext → ActionInstructions
    Execute confirm_submit: Action, ActionContext → ActionConfirmation
    Capture typed results: ActionInstructions, ActionConfirmation, ValidateResult
    Update state: Behavior Action State

Behavior
    Retrieve instructions: Action Instructions
    List available actions: Actions
    Navigate to action: Behavior Action State

Action
    Has two operations: Provide Instructions Operation, Confirm Submit Operation
    Define required parameters: Action Context
    
Action: Provide Instructions Operation
    Accept typed context: ActionContext with minimal fields (scope)
    Load behavior-specific data: Templates, Rules, Questions, Criteria
    Generate typed instructions: ActionInstructions (ClarifyInstructions, StrategyInstructions, BuildInstructions, RenderInstructions)
    Return typed result to CLI: Output Formatter
    
Action: Confirm Submit Operation  
    Accept typed context: ActionContext with completed work fields
    Validate completed work: Validation Rules
    Save to persistent storage: Clarifications File, Strategy File, Knowledge Graph File, Rendered Files
    Return typed confirmation: ActionConfirmation (ClarifyConfirmation, StrategyConfirmation, BuildConfirmation, RenderConfirmation)
    Advance workflow: Behavior Action State

Action Context
    Base class for all action contexts
    ClarifyActionContext: Store clarifications (key_questions_answered, evidence_provided)
    StrategyActionContext: Store strategy decisions (decisions_made, assumptions_made)
    BuildActionContext: Store scope (FileScope OR StoryScope)
    ValidateActionContext: Store validation config (rules_to_exclude, rules_to_include, skip_cross_file, background)
    RenderActionContext: Store scope (FileScope OR StoryScope)
    Provide to action: Action

Action Instructions (typed result classes)
    ClarifyInstructions: Key Questions, Evidence Types, Guardrails
    StrategyInstructions: Strategy Criteria, Typical Assumptions, Recommended Activities
    BuildInstructions: Knowledge Graph Template, Rules, Scope, Story Names
    RenderInstructions: Render Specs, Templates, Scope
    Display to user: Output Formatter
    Show examples: Scope Examples, Parameter Examples

Action Confirmation (typed result classes)
    ClarifyConfirmation: Saved To, Questions Answered Count, Evidence Provided Count, Success
    StrategyConfirmation: Saved To, Decisions Count, Assumptions Count, Success
    BuildConfirmation: Saved To, Mode (create/update), Items Added, Success
    RenderConfirmation: Saved To (list), Documents Created Count, Synchronizers Executed, Success
    ValidateResult: Passed, Violations, Files Validated Count, Scope, Validation Summary
    Save to state: Behavior Action State
    Display to user: Output Formatter
    Advance to next action: Behavior Action State

Completed Actions
    Track action state: Action
    Track timestamp: Action

Scope (base class)
    Common interface for all scope types

FileScope (extends Scope)
    Include file paths: List of paths
    Exclude file paths: List of patterns
    Apply to build/render: BuildActionContext, RenderActionContext

StoryScope (extends Scope)
    List of nodes: Node (type + name)
    Node types: STORY, EPIC, SUB_EPIC, INCREMENT
    Apply to build/render: BuildActionContext, RenderActionContext

Node
    Node type: STORY, EPIC, SUB_EPIC, INCREMENT
    Node name: String identifier

Completed Work (passed in ActionContext for confirm_submit)
    Clarifications: Key Questions Answered (dict), Evidence Provided (dict)
    Strategy Decisions: Decisions Made (dict), Assumptions Made (list)
    Knowledge Graph: JSON structure following template (dict or file reference)
    Rendered Documents: Generated files from templates (file references)
    
Typed Results (returned from action operations)
    Instructions Phase: ClarifyInstructions, StrategyInstructions, BuildInstructions, RenderInstructions
    Confirmation Phase: ClarifyConfirmation, StrategyConfirmation, BuildConfirmation, RenderConfirmation
    Validation: ValidateResult (no separate phases)

Clarifications
    Store key questions answered: Key Questions
    Store evidence provided: Evidence

Strategy Decisions
    Store assumptions: Assumptions
    Store decisions: Decision Criteria

Output Formatter
    Display state: Behavior Action State
    Display instructions: Action Instructions
    Display results: Action Results
    Display help: Help Generator
    Display errors: Parameter Parser

Help Generator
    Generate command help: Behavior, Action
    Generate parameter help: Action Context
    Generate scope examples: FileScope (include/exclude), StoryScope (nodes)
    Display available nodes: StoryScope from story_graph
    Display available folders: FileScope from workspace

REPL Command Generator
    Walk bot structure: Orchestrator, Bot
    Collect action data: Action Data Collector
    Generate command definitions: REPL Command Visitor
    Generate cursor shortcuts: Cursor REPL Visitor
    Generate help docs: Help REPL Visitor

Orchestrator
    Walk behaviors: Bot
    Walk actions: Behavior
    Call visitor methods: Visitor
    Provide help context: Action Data Collector

REPL Command Visitor
    Visit behavior: Behavior Help Context
    Visit action: Action Help Context
    Generate navigate commands: Behavior, Action
    Generate scope commands: File Scope, Story Scope
    Generate provide_instructions commands: Scope Parameters
    Generate confirm_submit commands: Completed Work Parameters

Action Data Collector
    Sort behaviors: Behavior
    Get behavior actions: Action
    Get action parameters: Action Context
    Get parameter descriptions: Action Context
    Get action description: Action

Behavior Help Context
    Store behavior name: Behavior
    Store behavior description: Behavior
    Store actions: Action
    Provide to visitor: Visitor

Action Help Context
    Store action name: Action
    Store action description: Action
    Store parameters: Action Context
    Store parameter descriptions: Action Context
    Provide to visitor: Visitor
```

---

## Story Map

```
(E) Generate REPL CLI
    (S) Generator --> Generate REPL Command Definitions
        - Create REPL Command Visitor
        - Walk Bot Structure via Orchestrator
        - Collect Action Data via ActionDataCollector
        - Generate Navigate Commands
        - Generate Scope Commands  
        - Generate Instruction Commands
        - Generate Confirm Commands
        - Generate Help Commands
    (S) Generator --> Generate CLI Entry Point
        - Update base_bot_cli.py with REPL mode
        - Add TTY Detection
        - Add REPL Loop Handler
        - Integrate with existing CliCommandRouter
    (S) Generator --> Generate Cursor Commands
        - Create Cursor REPL Visitor
        - Generate Navigate Shortcuts via Orchestrator
        - Update Cursor Help Files
        - Generate REPL Examples
    (S) Generator --> Generate Help Documentation
        - Create Help REPL Visitor
        - Generate Command Reference via Orchestrator
        - Generate Parameter Reference
        - Generate Scope Examples
        - Generate Dot Notation Examples

(E) Run Interactive REPL
    (E) Start Interactive Session
            (S) User --> Launch REPL Loop
            (S) CLI --> Detect TTY Input
      
            (S) CLI --> Display Fresh Start or 
            (S) CLI --> Display Existing State
    (E) Display State To User
            (S) CLI --> Show Current Position In Workflow Breadcrumbs
            (S) CLI --> Show Available Behaviors and Actions
   
        opt 
            (S) user --> Display File Scope (default is current)
            (S) user --> Display Story Scope (default is current)
            (S) user --> Display Clarifications (default is current)
            (S) user --> Display Strategy (default is current)
    (E) Navigate Bot
            (S) User --> Request Help
            (S) User --> Request Status
            (S) User --> Navigate To Behavior
            (S) User --> Navigate To Action
            (S) User --> Navigate Within Behavior
            (S) User --> Set Scope Parameter
            (S) User --> Exit REPL
    (E) Enter Instruction Command
            (S) User --> Enter Action
                (S) CLI --> Prompt For Basic Parameters
            or
                (S) CLI --> Prompt For Story Scope Parameters
            or
                (S) CLI --> Prompt For File Scope Parameters
            or
                (S) User --> Enter Action with Parameters

            (S) CLI --> Validate Instruction Syntax and Regular Parameters
            opt (S) CLI --> Validate Story Scope Parameters
            opt (S) CLI --> Validate File Scope Parameters
          
            (S) CLI --> Retrive and Display Bot Behavior Action Instructions
   
     (E) Enter Confirm COmmand
                (S) CLI --> Display Confirm and Continue Prompt
                opt (user) --> Feedback and review
                (S) User -->  Enters Confirm Results and CLI Saves and Continue to Next Action
                (S) CLI -->  Validate Confirm Syntax and Regular Parameters
                opt (S) CLI --> Validate Confirm Story Scope Parameters
                 opt (S) CLI --> Validate Confirm File Scope Parameters

    (E) Execute Action Request
            (S) CLI --> Execute Current Action
            (S) CLI --> Display Action Output
            (S) CLI --> Advance To Next Action
            (S) CLI --> Loop Back To Display State
    (E) Exit Interactive Session
            (S) User --> Exit Command
            (S) CLI --> Cleanup And Exit


```

---

## Incremental Backlog

### Increment 1: Front-End REPL (Interactive Testing)

**Purpose:** Validate core REPL interaction patterns work for both AI and human users with hard-coded responses. Test the conversational flow, state display, navigation, and confirm workflow before building real backend integration.

- User --> Launch REPL Loop
- CLI --> Detect TTY Input
- CLI --> Display Fresh Start or Existing State [mock]
- CLI --> Show Current Position In Workflow Breadcrumbs [mock]
- CLI --> Show Available Behaviors and Actions [mock]
- User --> Navigate To Behavior [mock]
- User --> Navigate To Action [mock]
- User --> Navigate Within Behavior [mock]
- User --> Request Help [mock]
- User --> Request Status [mock]
- User --> Enter Action [mock]
- CLI --> Prompt For Basic Parameters [mock]
- CLI --> Prompt For Story Scope Parameters [mock]
- CLI --> Prompt For File Scope Parameters [mock]
- CLI --> Display Confirm and Continue Prompt [mock]
- User --> Enters Confirm Results [mock]
- CLI --> Advance To Next Action [mock]
- CLI --> Loop Back To Display State [mock]
- User --> Exit REPL

### Increment 2: Generation

**Purpose:** Validate that we can automatically generate REPL commands from existing behavior_action_state infrastructure. Ensure the generator discovers all behaviors/actions and creates the same interactive experience as Increment 1 without manual coding.

- Generator --> Generate REPL Command Definitions
- Generator --> Generate CLI Entry Point
- Generator --> Generate Cursor Commands
- Generator --> Generate Help Documentation

### Increment 3: Base Parameters (No Scope)

**Purpose:** Validate that REPL can call real behaviors/actions with actual parameters (clarifications, strategy decisions, etc.) and that interactive parameter prompting works correctly. Assume scope=all to avoid complex scope parsing. Test full execute → display → advance workflow loop.

- CLI --> Display Fresh Start or Existing State [real]
- CLI --> Show Current Position In Workflow Breadcrumbs [real]
- CLI --> Show Available Behaviors and Actions [real]
- User --> Navigate To Behavior [real]
- User --> Navigate To Action [real]
- User --> Request Help [real]
- User --> Request Status [real]
- User --> Enter Action [real]
- CLI --> Parse Command Input [real]
- CLI --> Validate Instruction Syntax and Regular Parameters [real]
- CLI --> Prompt User For Missing Parameters [real]
- CLI --> Display Confirm and Continue Prompt [real]
- User --> Enters Confirm Results [real]
- CLI --> Execute Current Action [real, scope=all]
- CLI --> Display Action Output [real]
- CLI --> Advance To Next Action [real]
- CLI --> Loop Back To Display State [real]

### Increment 4a: Story Parameters (Mock Backend)

**Purpose:** Validate story/epic scope syntax parsing, validation, and interactive prompting work correctly without the complexity of executing real backend actions. Test dot-notation parsing for scope.type, scope.value, etc.

- User --> Display Story Scope [mock]
- User --> Set Scope Parameter (story/epic) [mock]
- User --> Enter Action [mock]
- CLI --> Parse Command Input [mock]
- CLI --> Validate Instruction Syntax and Regular Parameters [mock]
- CLI --> Validate Story Scope Parameters [mock]
- CLI --> Prompt User For Missing Story Scope [mock]
- CLI --> Display Confirm and Continue Prompt [mock]
- User --> Enters Confirm Results [mock]
- CLI --> Execute Current Action [mock]
- CLI --> Display Action Output [mock]
- CLI --> Advance To Next Action [mock]

### Increment 4b: Story Parameters (Real Backend)

**Purpose:** Validate that story/epic scope filters correctly target specific stories/epics when executing real behavior actions. Ensure scope is properly passed through ActionContext to actions and produces correct filtered results.

- User --> Display Story Scope [real]
- User --> Set Scope Parameter (story/epic) [real]
- User --> Enter Action [real]
- CLI --> Parse Command Input [real]
- CLI --> Validate Instruction Syntax and Regular Parameters [real]
- CLI --> Parse Story Scope [real]
- CLI --> Validate Story Scope Parameters [real]
- CLI --> Prompt User For Missing Story Scope [real]
- CLI --> Display Confirm and Continue Prompt [real]
- User --> Enters Confirm Results [real]
- CLI --> Apply Story Scope Filter [real]
- CLI --> Execute Action With Story Scope [real]
- CLI --> Display Action Output [real]
- CLI --> Advance To Next Action [real]

### Increment 5a: File Parameters (Mock Backend)

**Purpose:** Validate file scope syntax parsing (include/exclude patterns, file lists) and interactive prompting work correctly without backend complexity. Test dot-notation for scope.value, scope.exclude patterns.

- User --> Display File Scope [mock]
- User --> Set Scope Parameter (files) [mock]
- User --> Enter Action [mock]
- CLI --> Parse Command Input [mock]
- CLI --> Validate Instruction Syntax and Regular Parameters [mock]
- CLI --> Validate File Scope Parameters [mock]
- CLI --> Prompt User For Missing File Scope [mock]
- CLI --> Display Confirm and Continue Prompt [mock]
- User --> Enters Confirm Results [mock]
- CLI --> Execute Current Action [mock]
- CLI --> Display Action Output [mock]
- CLI --> Advance To Next Action [mock]

### Increment 5b: File Parameters (Real Backend)

**Purpose:** Validate that file scope filters correctly target specific files/patterns when executing real behavior actions. Ensure include/exclude logic works correctly and produces expected filtered file sets for validation and other file-based actions.

- User --> Display File Scope [real]
- User --> Set Scope Parameter (files) [real]
- User --> Enter Action [real]
- CLI --> Parse Command Input [real]
- CLI --> Validate Instruction Syntax and Regular Parameters [real]
- CLI --> Parse File Scope [real]
- CLI --> Validate File Scope Parameters [real]
- CLI --> Prompt User For Missing File Scope [real]
- CLI --> Display Confirm and Continue Prompt [real]
- User --> Enters Confirm Results [real]
- CLI --> Apply File Scope Filter [real]
- CLI --> Execute Action With File Scope [real]
- CLI --> Display Action Output [real]
- CLI --> Advance To Next Action [real]

---

## Story Details

### Increment 1: Front-End REPL (Interactive Testing)

All stories in this increment use hard-coded/mock responses.

---

## Background: Across All Incrmeent 1 Stories

**Given** a bot  configured with the following behaviors:

### Global Test Tables

#### Bot Behaviors

| bot_name  | behaviors                                                                          |
| --------- | ---------------------------------------------------------------------------------- |
| story_bot | ["shape", "prioritization", "discovery", "exploration", "scenarios", "tests", "code"] |

and each behavior is configured with the following actions and scope types

#### Behavior Actions and Scope Configuration

| behavior       | workflow_order | actions                                          | scope_types_used                      | notes                                                                 |
| -------------- | -------------- | ------------------------------------------------ | ------------------------------------- | --------------------------------------------------------------------- |
| shape          | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all              | Works with story_graph to create initial story maps and outlines      |
| prioritization | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all              | Works with story_graph to organize stories into increments            |
| discovery      | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all              | Works with story_graph to elaborate stories with flows and rules      |
| exploration    | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all              | Works with story_graph to define acceptance criteria                  |
| scenarios      | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all              | Works with story_graph to write detailed scenarios                    |
| tests          | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all OR files     | build: Works with story_graph, existing tests, or existing code to generate tests. validate: Validates test files |
| code           | 1→2→3→4→5      | clarify, strategy, build, validate, render       | story/epic/increment/all OR files     | build: Works with story_graph, existing code, or existing tests to generate code that makes tests pass. validate: Validates code |

##### Action Operations Table (Two-Phase Model)

Each action has two operations: **provide_instructions** (initial call) and **confirm_submit** (submit completed work):

| action   | provide_instructions_context | provide_instructions_returns | confirm_submit_context | confirm_submit_returns | scope_types |
| -------- | ---------------------------- | ---------------------------- | ---------------------- | ---------------------- | ----------- |
| clarify  | **ClarifyActionContext**<br>(empty - no parameters needed) | **ClarifyInstructions**<br>- action: str<br>- behavior: str<br>- base_instructions: List[str]<br>- guardrails: RequiredContext<br>&nbsp;&nbsp;- key_questions: List[str]<br>&nbsp;&nbsp;- evidence: List[str] | **ClarifyActionContext**<br>`key_questions_answered: Dict`<br>`evidence_provided: Dict` | **ClarifyConfirmation**<br>- saved_to: Path<br>- questions_answered: int<br>- evidence_provided: int<br>- success: bool | N/A |
| strategy | **StrategyActionContext**<br>(empty - no parameters needed) | **StrategyInstructions**<br>- action: str<br>- behavior: str<br>- base_instructions: List[str]<br>- strategy: StrategyData<br>&nbsp;&nbsp;- strategy_criteria: Dict<br>&nbsp;&nbsp;- assumptions: List[str]<br>&nbsp;&nbsp;- recommended_activities: List[str] | **StrategyActionContext**<br>`decisions_made: Dict`<br>`assumptions_made: List[str]` | **StrategyConfirmation**<br>- saved_to: Path<br>- decisions_count: int<br>- assumptions_count: int<br>- success: bool | N/A |
| build    | **BuildActionContext**<br>`scope: Optional[FileScope OR StoryScope]`<br>**Default: all**<br><br>**Story behaviors (shape/prioritization/discovery/exploration/scenarios):**<br>Default: `StoryScope(nodes=[Node(type='all')])`<br>Optional: `StoryScope(nodes=[Node(type='epic', name='Epic Name')])`<br><br>**File behaviors (tests/code):**<br>Default: `FileScope(include=[behavior_default])`<br>Optional: `FileScope(include=['src/', 'tests/'], exclude=['*.bak'])` | **BuildInstructions**<br>- action: str<br>- behavior: str<br>- base_instructions: List[str]<br>- knowledge_graph_template: TemplatePointer<br>&nbsp;&nbsp;- template_path: str (file pointer)<br>&nbsp;&nbsp;- exists: bool<br>- knowledge_graph_config: GraphConfig<br>- rules: List[RuleDict]<br>- scope: ScopeDict<br>- scope_story_names: List[str]<br>- existing_file: FileInfo | **BuildActionContext**<br>`scope: FileScope OR StoryScope`<br>+ knowledge_graph: Dict (completed graph) | **BuildConfirmation**<br>- saved_to: Path<br>- mode: str ('create' or 'update')<br>- items_added: List[str]<br>- success: bool | **FileScope** OR **StoryScope** |
| validate | **ValidateActionContext**<br>`scope: Optional[FileScope OR StoryScope]`<br>`rules_to_exclude: Optional[List[str]]`<br>`rules_to_include: Optional[List[str]]`<br>`skip_cross_file: Optional[bool]`<br>`background: Optional[bool]`<br>**Defaults:** scope=all, rules=all, skip_cross_file=false, background=false<br><br>**Story behaviors:** Default `StoryScope(all)`<br>**File behaviors:** Default `FileScope(include=[behavior_default])`<br>**Rules filtering:** Optional `rules_to_exclude=['deprecated']` | **ValidateInstructions**<br>- action: str<br>- behavior: str<br>- base_instructions: List[str]<br>- validation_rules: List[ProcessedRule]<br>&nbsp;&nbsp;- rule_file: str<br>&nbsp;&nbsp;- scanner_status: ScannerStatus<br>&nbsp;&nbsp;- violations: List[Violation]<br>- report_path: str<br>- report_link: str | **ValidateActionContext**<br>(empty - validation already executed) | **ValidateConfirmation**<br>- confirmed: bool<br>- message: str ('confirmed') | **FileScope** OR **StoryScope** |
| render   | **RenderActionContext**<br>`scope: Optional[FileScope OR StoryScope]`<br>**Default: all**<br><br>**Story behaviors:** Default `StoryScope(all)`<br>**File behaviors:** Default `FileScope(include=[behavior_default])`<br>Optional: Specify epic/story/increment OR specific files | **RenderInstructions**<br>- action: str<br>- behavior: str<br>- instructions: RenderInstructions<br>- executed_specs: List[RenderSpec]<br>- template_specs: List[RenderSpec] | **RenderActionContext**<br>`scope: FileScope OR StoryScope`<br>+ documents: List[Path] (completed docs) | **RenderConfirmation**<br>- saved_to: List[Path]<br>- documents_created: int<br>- synchronizers_executed: List[str]<br>- success: bool | **FileScope** OR **StoryScope** |

**Action Descriptions:**

| action   | description                                    |
| -------- | ---------------------------------------------- |
| clarify  | Gather context and clarify requirements        |
| strategy | Determine planning approach and criteria       |
| build    | Build knowledge graph and content              |
| validate | Validate against behavior-specific rules       |
| render   | Generate output documents from knowledge graph |

**Scope Class Hierarchy:**
```python
@dataclass
class Scope:
    """Base class for all scope types"""
    pass

@dataclass
class FileScope(Scope):
    """Scope for file-based operations (code, tests validation)"""
    include: List[str]  # File paths to include: ["src/", "tests/file.py"]
    exclude: List[str]  # File paths to exclude: ["*.bak", "__pycache__"]

@dataclass
class NodeType(Enum):
    STORY = 'story'
    EPIC = 'epic'
    SUB_EPIC = 'sub_epic'
    INCREMENT = 'increment'

@dataclass
class Node:
    """A node in the story graph"""
    type: NodeType
    name: str

@dataclass
class StoryScope(Scope):
    """Scope for story-based operations (shape, discovery, exploration, etc.)"""
    nodes: List[Node]  # List of story graph nodes to work on
```

**ActionContext Class Hierarchy (inputs to action operations):**
```python
ActionContext (base)

├── ClarifyActionContext
│   ├── key_questions_answered: Optional[Dict[str, Any]]
│   └── evidence_provided: Optional[Dict[str, Any]]
│
├── StrategyActionContext
│   ├── decisions_made: Optional[Dict[str, Any]]
│   └── assumptions_made: Optional[List[str]]
│
├── BuildActionContext
│   └── scope: Optional[Union[FileScope, StoryScope]]  # EITHER file OR story
│
├── ValidateActionContext
│   ├── rules_to_exclude: List[str]  # Rules to skip
│   ├── rules_to_include: List[str]  # Rules to explicitly include
│   ├── skip_cross_file: bool
│   └── background: bool
│
└── RenderActionContext
    └── scope: Optional[Union[FileScope, StoryScope]]  # EITHER file OR story
```

**Scope Examples:**

**FileScope Examples (for code/tests behaviors):**
```python
# Include specific files/folders
FileScope(
    include=["src/", "tests/test_file.py"],
    exclude=[]
)

# Include with exclusions
FileScope(
    include=["src/", "tests/"],
    exclude=["*.bak", "__pycache__", "*.pyc", "*.tmp"]
)

# Just src folder, exclude legacy code
FileScope(
    include=["src/"],
    exclude=["src/legacy/", "*.old.py"]
)
```

**StoryScope Examples (for shape/prioritization/discovery/exploration/scenarios behaviors):**
```python
# Work on specific stories
StoryScope(
    nodes=[
        Node(type=NodeType.STORY, name="Create Mob"),
        Node(type=NodeType.STORY, name="Edit Mob"),
        Node(type=NodeType.STORY, name="Delete Mob")
    ]
)

# Work on entire epic
StoryScope(
    nodes=[
        Node(type=NodeType.EPIC, name="Manage Mobs")
    ]
)

# Work on multiple epics and specific stories
StoryScope(
    nodes=[
        Node(type=NodeType.EPIC, name="Manage Mobs"),
        Node(type=NodeType.EPIC, name="Execute Mob Actions"),
        Node(type=NodeType.STORY, name="Configure Game Settings")
    ]
)

# Work on specific increments
StoryScope(
    nodes=[
        Node(type=NodeType.INCREMENT, name="1"),
        Node(type=NodeType.INCREMENT, name="2")
    ]
)

# Work on sub-epic
StoryScope(
    nodes=[
        Node(type=NodeType.SUB_EPIC, name="Character Management"),
        Node(type=NodeType.SUB_EPIC, name="Item Management")
    ]
)
```

**ValidateActionContext Examples:**
```python
# Validate with specific rules excluded
ValidateActionContext(
    rules_to_exclude=["use_type_hints", "use_dataclasses"],
    rules_to_include=[],
    skip_cross_file=False,
    background=False
)

# Background validation with cross-file checks skipped
ValidateActionContext(
    rules_to_exclude=[],
    rules_to_include=[],
    skip_cross_file=True,
    background=True
)

# Only run specific rules
ValidateActionContext(
    rules_to_exclude=[],
    rules_to_include=["use_consistent_naming", "avoid_duplication"],
    skip_cross_file=False,
    background=False
)
```

**Action Workflow Pattern:**
```
User: Run action with scope parameters
  → CLI: Build typed ActionContext with FileScope or StoryScope
  → CLI: action.provide_instructions(context: ActionContext) → ActionInstructions
User: Complete work following instructions
  → User: Run action with completed work parameters
  → CLI: Build typed ActionContext with completed work
  → CLI: action.confirm_submit(context: ActionContext) → ActionConfirmation
```

**Example: build action with StoryScope (shape behavior):**
```
Phase 1: provide_instructions
User: run build epic="Manage Mobs"
  → CLI: Build StoryScope with nodes
  → CLI: context = BuildActionContext(
           scope=StoryScope(
             nodes=[Node(type=NodeType.EPIC, name="Manage Mobs")]
           )
         )
  → CLI: result = action.provide_instructions(context)
  → Returns: BuildInstructions(
        knowledge_graph_template=Path("..."),
        rules=[...],
        scope={...},
        scope_story_names=["Create Mob", "Edit Mob", ...]
      )
  → CLI displays instructions to user

Phase 2: confirm_submit
User: submit knowledge_graph={...}
  → CLI: context = BuildActionContext(
           scope=StoryScope(nodes=[...])
         ) + knowledge_graph data
  → CLI: result = action.confirm_submit(context)
  → Returns: BuildConfirmation(
        saved_to=Path("story-graph.json"),
        mode="update",
        items_added=["Create Mob", "Edit Mob"],
        success=True
      )
```

**Example: validate action (executes immediately, no separate confirm phase):**
```
User: run validate skip_cross_file=true rules_to_exclude=["use_type_hints"]
  → CLI: context = ValidateActionContext(
           rules_to_exclude=["use_type_hints"],
           rules_to_include=[],
           skip_cross_file=True,
           background=False
         )
  → CLI: result = action.provide_instructions(context)
  → Returns: ValidateInstructions(
        validation_rules=["avoid_duplication", "use_consistent_naming", ...],
        files_to_validate=[Path("src/file1.py"), Path("src/file2.py"), ...],
        rules_to_apply=["avoid_duplication", "use_consistent_naming"],  # excludes use_type_hints
        skip_cross_file=True
      )
  → CLI displays rules to user
  → User: execute (or validate action runs immediately)
  → Action executes validation
  → Returns: ValidateResult(
        passed=False,
        violations=[
          {"file": "src/file1.py", "rule": "avoid_duplication", "line": 42, ...}
        ],
        files_validated=42,
        validation_summary="Found 3 violations in 2 files"
      )
```

**Example: build action with FileScope (code behavior):**
```
Phase 1: provide_instructions
User: run build files="src/" exclude="*.bak"
  → CLI: Build FileScope
  → CLI: context = BuildActionContext(
           scope=FileScope(
             include=["src/"],
             exclude=["*.bak"]
           )
         )
  → CLI: result = action.provide_instructions(context)
  → Returns: BuildInstructions(
        knowledge_graph_template=Path("..."),
        rules=[...],
        scope={...}
      )
```

**Note:** Scenarios below reference these background tables:
- **Bot Behaviors** - All available behaviors for story_bot
- **Behavior Actions and Scope Configuration** - Each behavior's actions, workflow order, and scope types
- **Action Operations Table** - Two-phase operations (provide_instructions, confirm_submit) with typed inputs/outputs
- **Action Descriptions** - What each action does

**Action Two-Phase Model:**
All actions (except validate) have two operations:
1. **provide_instructions** - User runs action with minimal params (usually just scope), CLI builds typed ActionContext, action returns AI instructions
2. **confirm_submit** - User completes work following instructions, runs action with results, CLI builds typed ActionContext with completed work, action saves and confirms

**Type-Safe Action Operations:**
- **Inputs**: All parameters are passed via typed ActionContext dataclasses (ClarifyActionContext, StrategyActionContext, BuildActionContext, ValidateActionContext, RenderActionContext)
- **Outputs**: All results are returned as typed ActionResult objects (ClarifyInstructions/Confirmation, StrategyInstructions/Confirmation, BuildInstructions/Confirmation, ValidateResult, RenderInstructions/Confirmation)
- **Scopes**: Two distinct scope types - FileScope (include/exclude paths) and StoryScope (list of nodes)
- **No mixed scopes**: Actions accept EITHER FileScope OR StoryScope, never both
- **Validation**: ValidateActionContext has its own fields (rules_to_exclude, rules_to_include, skip_cross_file, background) - no scope object
- **No floating dicts**: Everything is strongly typed with dataclasses
- **Type safety**: CLI builds context from user input, action returns typed result, CLI formats result for display

**Behavior-Specific Scope Usage:**
- **Story-only behaviors** (shape, prioritization, discovery, exploration, scenarios): Use **StoryScope** with list of nodes (Node has type + name). When CLI prompts for scope, displays available epics/stories/increments from story_graph.
- **Dual-scope behaviors** (tests, code): Can use EITHER **StoryScope** OR **FileScope**. CLI prompts user to choose which scope type:
  - If StoryScope: Display available nodes (epics/stories/increments) from story_graph
  - If FileScope: Display top-level workspace folders + default include paths (src/ for code, tests/ for tests)
- **Validation**: Uses **ValidateActionContext** with rule filtering (rules_to_exclude, rules_to_include) instead of scope objects

---

### 📝 User --> Launch REPL Loop

**Acceptance Criteria:**

- **When** user runs `story_bot --stdio` from terminal, **then** CLI launches REPL loop
- **When** REPL loop starts, **then** CLI loads BehaviorActionState if it exists
- **When** BehaviorActionState exists, **then** CLI displays current position from state
- **When** BehaviorActionState does not exist, **then** CLI displays fresh start message

## Background

```gherkin
Given CLI executable is available in PATH or via python command
And Bot has behaviors from Background: Bot Behaviors
And Each Behavior has actions from Background: Behavior Actions
And Each Action has three operations: instructions, submit, and confirm
And instructions takes minimal params (scope) and returns AI instructions
And submit takes completed work and returns saved confirmation
And confirm marks action complete and advances to next action
```

## Scenarios

### Scenario Outline: Launch REPL with existing state

**Steps:**

```gherkin
Given BehaviorActionState exists with current_behavior=<behavior>
And BehaviorActionState has current_action=<action>
And BehaviorActionState has working_directory="C:\dev\project"
When user runs command with --stdio flag
Then CLI loads BehaviorActionState
And CLI displays "CURRENT: story_bot.<behavior>.<action>"
And CLI displays "Working Directory: C:\dev\project"
And CLI displays breadcrumbs: "[<behavior>] <action_breadcrumbs>"
```

**Examples:**

| behavior  | action   | action_breadcrumbs                                                  |
| --------- | -------- | ------------------------------------------------------------------- |
| shape     | build    | clarify [OK] -> strategy [OK] -> build* -> validate -> render      |
| discovery | clarify  | clarify* -> strategy -> build -> validate -> render                |
| scenarios | validate | clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render |

**Example output for each case:**

```
# Case 1: shape.build (mid-workflow, 2 completed)
> CURRENT: story_bot.shape.build
> Working Directory: C:\dev\project
> [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render

# Case 2: discovery.clarify (fresh start of behavior)
> CURRENT: story_bot.discovery.clarify
> Working Directory: C:\dev\project
> [discovery] clarify* -> strategy -> build -> validate -> render

# Case 3: scenarios.validate (near end, 3 completed)
> CURRENT: story_bot.scenarios.validate
> Working Directory: C:\dev\project
> [scenarios] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render
```

---

### 📝 CLI --> Display Fresh Start [mock]

**Acceptance Criteria:**

- **When** BehaviorActionState does not exist, **then** CLI displays:

  ```
  story_bot --stdio

  > FRESH
  > No workspace configured
  ```
- **When** fresh start is detected, **then** CLI displays available commands with Bot.behaviors list:

  ```
  > Commands:
  >   workspace <path>     Set working directory
  >   behavior <name>      Select behavior (shape, discovery, exploration, ...)
  >   help                 Show all commands
  >   exit                 Quit
  ```
- **When** user enters workspace command, **then** BehaviorActionState.working_directory is set and CLI responds:

  ```
  < workspace C:\dev\my-project
  > OK workspace=C:\dev\my-project
  ```
- **When** user selects behavior, **then** BehaviorActionState is initialized with that behavior and CLI responds:

  ```
  < behavior shape
  > OK behavior=shape
  > 
  > CURRENT: story_bot.shape.clarify
  > [shape] clarify* -> strategy -> build -> validate -> render
  ```

## Scenarios

### Scenario Outline: CLI displays fresh start with no state file

**Steps:**

```gherkin
Given BehaviorActionState does not exist
And Bot.behaviors contains all behaviors from Background: Bot Configuration
And user has not specified workspace path
When CLI launches in REPL mode
Then CLI displays "FRESH"
And CLI displays "No workspace configured"
And CLI displays "Commands:"
And CLI displays "  workspace <path>     Set working directory"
And CLI displays "  behavior <name>      Select behavior (<behaviors_list>)"
And CLI displays "  help                 Show all commands"
And CLI displays "  exit                 Quit"
```

**Examples:**

| behaviors_list                                                     |
| ------------------------------------------------------------------ |
| shape, prioritization, discovery, exploration, scenarios, tests, code |

### Scenario: User configures workspace in fresh session

**Steps:**

```gherkin
Given BehaviorActionState does not exist
And user enters command: workspace C:\dev\project
When CLI processes workspace command
Then CLI responds "OK workspace=C:\dev\project"
And BehaviorActionState.working_directory is set to "C:\dev\project"
```

### Scenario Outline: User selects initial behavior

**Steps:**

```gherkin
Given CLI is in fresh start state with workspace configured
And Bot.behaviors contains all behaviors from Background: Bot Configuration
And Behavior "<selected_behavior>" has actions from Background: Behavior Actions
And user enters command: behavior <selected_behavior>
When CLI processes behavior command
Then CLI responds "OK behavior=<selected_behavior>"
And CLI displays "CURRENT: story_bot.<selected_behavior>.clarify"
And CLI displays breadcrumbs: "[<selected_behavior>] clarify* -> strategy -> build -> validate -> render"
And BehaviorActionState.current_behavior is set to <selected_behavior>
And BehaviorActionState.current_action is set to clarify
```

**Examples:**

| selected_behavior |
| ----------------- |
| shape             |
| discovery         |
| scenarios         |
| code              |

**Note:** All behaviors start with "clarify" action and follow the same workflow from Background: Action Workflow.

---

### 📝 CLI --> Display Help with Parameters

**Acceptance Criteria:**

- **When** user requests help for current behavior, **then** CLI displays all actions in that behavior with their parameters
- **When** user requests help for specific action, **then** CLI displays full parameter details with types and examples
- **When** displaying help, **then** CLI shows same detailed format as Cursor command files

## Scenarios

### Scenario Outline: User requests help for current behavior

**Steps:**

```gherkin
Given current behavior is <behavior>
And Behavior has actions: <actions>
And Action "<action>" has parameters: <parameters>
And user enters command: help
When CLI processes help request
Then CLI displays "Available Actions for behavior: <behavior>"
And CLI displays action list with descriptions:
  | action | description | parameters |
And CLI displays navigation commands
```

**Examples:**

| behavior | actions | action | parameters |
|----------|---------|--------|------------|
| shape | ["clarify", "strategy", "build", "validate", "render"] | build | ["--scope <dict>"] |
| discovery | ["clarify", "strategy", "build", "validate", "render"] | validate | ["--scope <dict>", "--background <flag>"] |
| scenarios | ["clarify", "strategy", "build", "validate", "render"] | clarify | ["--key-questions-answered <dict>", "--evidence-provided <dict>"] |

### Scenario Outline: User requests detailed help for specific action

**Steps:**

```gherkin
Given current behavior is <behavior>
And Action "<action>" exists in behavior
And Action has description: <description>
And Action has parameters: <parameters>
And user enters command: help <action>
When CLI processes detailed help request
Then CLI displays "## <action> - <description>"
And CLI displays "Full command:"
And CLI displays "  action <action> <parameter_syntax>"
And CLI displays "Parameters:" with type annotations
And CLI displays "Examples:" with concrete values
```

**Examples:**

| behavior | action | description | parameters | parameter_syntax |
|----------|--------|-------------|------------|------------------|
| shape | build | Build knowledge graph for build | ["--scope <dict>"] | --scope '{"type": "epic", "value": ["Epic Name"]}' |
| discovery | validate | Validate knowledge graph against rules | ["--scope <dict>", "--background <flag>"] | --scope '{"type": "all"}' --background |
| scenarios | clarify | Gather context by asking questions | ["--key-questions-answered <dict>"] | --key-questions-answered '{"q1": "answer"}' |

---

### 📝 CLI --> Display Existing State [mock]

**Acceptance Criteria:**

- **When** BehaviorActionState exists, **then** CLI displays current position and working directory from state
- **When** state exists, **then** CLI displays behavior/action progress with status indicators based on completed actions
- **When** state is displayed, **then** CLI shows available commands

## Scenarios

### Scenario Outline: CLI displays existing state with progress

**Steps:**

```gherkin
Given BehaviorActionState exists
And BehaviorActionState.current_behavior is <behavior>
And BehaviorActionState.current_action is <action>
And BehaviorActionState.working_directory is "C:\dev\project"
And BehaviorActionState.completed_actions contains: <completed_actions>
And Bot.behaviors contains all behaviors from Background: Bot Configuration
When CLI launches in REPL mode
Then CLI displays "CURRENT: story_bot.<behavior>.<action>"
And CLI displays "Working Directory: C:\dev\project"
And CLI displays "## Behavior/Action Progress"
And CLI displays behavior "<behavior>" with marker "->"
And CLI displays completed actions with "[OK]" marker
And CLI displays current action "<action>" with "[>>]" marker
And CLI displays pending actions with "[ ]" marker
And CLI displays other behaviors with "[ ]" marker
```

**Examples:**

| behavior  | action   | completed_actions           |
| --------- | -------- | --------------------------- |
| shape     | build    | ["clarify", "strategy"]     |
| discovery | validate | ["clarify", "strategy", "build"] |
| scenarios | clarify  | []                          |

---

### 📝 CLI --> Show Current Position In Workflow Breadcrumbs [mock]

**Acceptance Criteria:**

- **When** displaying workflow breadcrumbs from BehaviorActionState, **then** CLI shows format:

  ```
  [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render
  ```

  Where: `*` = current action, `[OK]` = completed action, `->` = workflow sequence
- **When** BehaviorActionState.current_action is displayed, **then** CLI marks it with `*` indicator
- **When** action is in BehaviorActionState.completed_actions, **then** CLI marks it with `[OK]` indicator
- **When** BehaviorActionState.current_behavior is shown, **then** CLI displays it in brackets: `[behavior]`

---

### 📝 CLI --> Show Available Behaviors and Actions [mock]

**Acceptance Criteria:**

- **When** user selects behavior, **then** CLI responds using BehaviorHelpContext:
  ```
  < behavior shape
  > OK behavior=shape
  > 
  > CURRENT: story_bot.shape.clarify
  > [shape] clarify* -> strategy -> build -> validate -> render
  > 
  > Available actions: clarify|strategy|build|validate|render
  > Type 'help' to see detailed action parameters
  > Type 'help <action>' for specific action help
  ```

---

### 📝 User --> Navigate To Behavior [mock]**

**Acceptance Criteria:**

- **When** user enters `behavior {name}`, **then** CLI updates BehaviorActionState.current_behavior and responds:
  ```
  < behavior discovery
  > OK behavior=discovery
  > CURRENT: story_bot.discovery.clarify
  > [discovery] clarify* -> strategy -> build -> validate -> render
  ```

## Scenarios

### Scenario Outline: User navigates to different behavior

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is <current_behavior>
And BehaviorActionState.current_action is <current_action>
And Bot.behaviors contains all behaviors from Background: Bot Configuration
And Behavior "<target_behavior>" has actions from Background: Behavior Actions
And user enters command: behavior <target_behavior>
When CLI processes navigation command
Then CLI responds "OK behavior=<target_behavior>"
And CLI displays "CURRENT: story_bot.<target_behavior>.clarify"
And CLI displays breadcrumbs: "[<target_behavior>] clarify* -> strategy -> build -> validate -> render"
And BehaviorActionState.current_behavior is updated to <target_behavior>
And BehaviorActionState.current_action is set to clarify
```

**Examples:**

| current_behavior | current_action | target_behavior |
| ---------------- | -------------- | --------------- |
| shape            | build          | discovery       |
| discovery        | validate       | exploration     |
| scenarios        | clarify        | tests           |
| code             | validate       | scenarios       |

**Note:** When navigating to a new behavior, it always starts at the first action (clarify) from Background: Action Workflow. All behaviors have the same actions from Background: Behavior Actions.

### Scenario Outline: User navigates to invalid behavior

**Steps:**

```gherkin
Given Bot.behaviors contains all behaviors from Background: Bot Configuration
And user enters command: behavior <invalid_behavior>
When CLI processes navigation command
Then CLI responds "ERROR: behavior '<invalid_behavior>' not found"
And CLI displays "Available behaviors: shape, prioritization, discovery, exploration, scenarios, tests, code"
And BehaviorActionState remains unchanged
```

**Examples:**

| invalid_behavior |
| ---------------- |
| invalid          |
| nonexistent      |
| test             |

---

### 📝 User --> Navigate To Action [mock]

**Acceptance Criteria:**

- **When** user enters `action {name}`, **then** CLI updates BehaviorActionState.current_action and responds:
  ```
  < action validate
  > OK action=validate
  > CURRENT: story_bot.shape.validate
  > [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render
  ```

## Scenarios

### Scenario Outline: User navigates to action within current behavior

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is <current_behavior>
And BehaviorActionState.current_action is <current_action>
And Behavior "<current_behavior>" has actions from Background: Behavior Actions
And BehaviorActionState.completed_actions contains: <completed_actions>
And user enters command: action <target_action>
When CLI processes navigation command
Then CLI responds "OK action=<target_action>"
And CLI displays "CURRENT: story_bot.<current_behavior>.<target_action>"
And CLI displays breadcrumbs showing <target_action> as current with * marker
And breadcrumbs show <completed_actions> with [OK] markers
And BehaviorActionState.current_action is updated to <target_action>
```

**Examples:**

| current_behavior | current_action | completed_actions            | target_action |
| ---------------- | -------------- | ---------------------------- | ------------- |
| shape            | clarify        | []                           | validate      |
| shape            | build          | ["clarify", "strategy"]      | validate      |
| discovery        | validate       | ["clarify", "strategy", "build"] | render        |
| scenarios        | strategy       | ["clarify"]                  | build         |

### Scenario Outline: User navigates to invalid action

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is <current_behavior>
And Behavior "<current_behavior>" has actions from Background: Behavior Actions
And user enters command: action <invalid_action>
When CLI processes navigation command
Then CLI responds "ERROR: action '<invalid_action>' not found in behavior '<current_behavior>'"
And CLI displays "Available actions: clarify, strategy, build, validate, render"
And BehaviorActionState.current_action remains unchanged
```

**Examples:**

| current_behavior | invalid_action |
| ---------------- | -------------- |
| shape            | test           |
| discovery        | invalid        |
| code             | nonexistent    |

**Note:** All behaviors have the same actions from Background: Behavior Actions.

---

### 📝 User --> Navigate Within Behavior [mock]

**Acceptance Criteria:**

- **When** user enters `current`, **then** CLI displays BehaviorActionState.current_action with breadcrumbs
- **When** user enters `close`, **then** CLI marks current action complete and advances to next
- **When** user enters `back`, **then** CLI moves to previous action in workflow

**Scenarios:**

### Scenario Outline: User executes workflow navigation commands

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<current_action>"
And BehaviorActionState.completed_actions are: <completed_actions>
When user enters command: "<command>"
Then CLI responds "<response_message>"
And BehaviorActionState.current_action becomes "<new_action>"
And BehaviorActionState.completed_actions become <new_completed_actions>
And CLI displays breadcrumbs: "<breadcrumbs>"
```

**Examples:**

| behavior | current_action | completed_actions       | command | response_message                                | new_action | new_completed_actions         | breadcrumbs                                               |
| -------- | -------------- | ----------------------- | ------- | ----------------------------------------------- | ---------- | ----------------------------- | --------------------------------------------------------- |
| shape    | build          | [clarify,strategy]      | current | CURRENT: story_bot.shape.build\nReady to run    | build      | [clarify,strategy]            | [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render |
| shape    | build          | [clarify,strategy]      | close   | Closing current action: build\nAdvancing        | validate   | [clarify,strategy,build]      | [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render |
| shape    | validate       | [clarify,strategy,build]| back    | Moving back to previous action                  | build      | [clarify,strategy]            | [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render |
| shape    | clarify        | []                      | back    | ERROR: Already at first action                  | clarify    | []                            | [shape] clarify* -> strategy -> build -> validate -> render |
| shape    | render         | [clarify,strategy,build,validate] | close | Closing current action: render\nCOMPLETE: shape behavior finished | render     | [clarify,strategy,build,validate,render] | [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate [OK] -> render [OK] |

---

### 📝 User --> Request Help [mock]

**Acceptance Criteria:**

- **When** user enters `help`, **then** CLI displays all available commands using ActionDataCollector:

  ```
  < help
  > 
  > ## Available Actions for behavior: shape
  > 
  > ### clarify
  > Gather context by asking required questions and collecting evidence in order to increase understanding
  >   Optional: --key-questions-answered <dict>
  >   Optional: --evidence-provided <dict>
  > 
  > ### strategy
  > Decide approach by presenting assumptions and decision criteria, then capturing decisions
  >   Optional: --decisions-made <dict>
  >   Optional: --assumptions-made <list>
  > 
  > ### build
  > Build knowledge graph for build
  >   Optional: scope.type=epic|story|increment|files scope.value="Name" scope.exclude=pattern
  >   Examples: scope.type=epic scope.value="Manage Mobs"
  >             scope.type=files scope.value=src/ scope.exclude=*.bak
  > 
  > ### validate
  > Validate knowledge graph and/or artifacts against behavior-specific rules
  >   Optional: scope.type=epic|story|increment|files scope.value="Name"
  >   Optional: rules.exclude=deprecated_rule rules.include=critical_rule
  >   Optional: --background
  >   Optional: --skip-cross-file
  > 
  > ### render
  > Render output documents and artifacts from knowledge graph using templates
  >   Optional: scope.type=epic|story|increment|files scope.value="Name"
  > 
  > ## Navigation Commands:
  >   action <name>        Jump to action
  >   behavior <name>      Switch behavior
  >   close                Mark current complete and advance to next
  >   back                 Go to previous action
  >   status               Show current state
  >   help <action>        Show detailed help for specific action
  >   exit                 Quit
  ```
- **When** user enters `help <action>`, **then** CLI displays detailed action help using ActionHelpContext:

  ```
  < help build
  > 
  > ## build - Build knowledge graph for build
  > 
  > Parameters:
  >   --scope (story scope OR file scope)
  > 
  > Examples:
  >   # Work on specific epic:
  >   action build scope.type=epic scope.value="Epic Name"
  > 
  >   # Work on multiple stories:
  >   action build scope.type=story scope.value="Story 1","Story 2"
  > 
  >   # Work on increment:
  >   action build scope.type=increment scope.value=1
  >   
  >   # Build from files (tests/code behaviors):
  >   action build scope.type=files scope.value=src/,tests/ scope.exclude=*.bak
  ```

---

### 📝 User --> Request Status [mock]**

**Acceptance Criteria:**

- **When** user enters `status`, **then** CLI displays current behavior/action, working directory, and breadcrumbs

**Scenarios:**

### Scenario Outline: User requests status display

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And BehaviorActionState.working_directory is "<working_dir>"
And BehaviorActionState.completed_actions are: <completed_actions>
When user enters command: "status"
Then CLI displays "CURRENT: story_bot.<behavior>.<action>"
And CLI displays "Working Directory: <working_dir>"
And CLI displays breadcrumbs: "<breadcrumbs>"
```

**Examples:**

| behavior       | action   | working_dir         | completed_actions       | breadcrumbs                                                        |
| -------------- | -------- | ------------------- | ----------------------- | ------------------------------------------------------------------ |
| shape          | build    | C:\dev\my-project   | [clarify,strategy]      | [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render |
| prioritization | clarify  | C:\dev\my-project   | []                      | [prioritization] clarify* -> strategy -> build -> validate -> render |
| discovery      | validate | C:\dev\another-proj | [clarify,strategy,build]| [discovery] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render |

---

### 📝 User --> Enter Action [mock]**

**Acceptance Criteria:**

- **When** user enters `run`, **then** CLI executes current action and displays mock response

**Scenarios:**

### Scenario Outline: User executes current action (mock)

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
When user enters command: "run"
Then CLI displays "EXECUTING <behavior>.<action>..."
And CLI displays "[mock response - not executing real action]"
And CLI displays mock response: {"status": "success", "action": "<action>", "data": {...}}
```

**Examples:**

| behavior       | action   |
| -------------- | -------- |
| shape          | clarify  |
| shape          | strategy |
| shape          | build    |
| prioritization | validate |
| discovery      | render   |

---

### 📝 CLI --> Prompt For Basic Parameters [mock]

**Acceptance Criteria:**

- **When** user runs action without required parameters, **then** CLI prompts with parameter descriptions
- **When** user provides parameters via dot-notation, **then** CLI acknowledges receipt

**Scenarios:**

### Scenario Outline: CLI prompts for missing action parameters

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And Action "<action>" requires parameters: <required_params>
When user enters command: "run"
And user has not provided: <required_params>
Then CLI displays "MISSING PARAMETERS for <behavior>.<action>"
And CLI displays parameter descriptions for: <required_params>
And CLI prompts "Please provide parameters:"
When user enters: "<param_input>"
Then CLI responds "<acknowledgment>"
```

**Examples:**

| behavior | action   | required_params                                   | param_input                                                                  | acknowledgment                       |
| -------- | -------- | ------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------ |
| shape    | clarify  | [key_questions_answered,evidence_provided]        | clarify.key_questions.q1="What is scope?" clarify.evidence.e1="Requirements" | OK received 1 key question, 1 evidence |
| shape    | strategy | [decisions_made,assumptions_made]                 | strategy.decisions.d1="Use REST API" strategy.assumptions="Single user"      | OK received 1 decision, 1 assumption |

---

### 📝 CLI --> Prompt For Story Scope Parameters [mock]

**Story:** User provides invalid story scope parameter for build/render/validate action

**User:** Runs action with malformed or invalid story scope

**Acceptance Criteria:**

- **When** user provides invalid story scope syntax, **then** CLI displays error and shows correct format with examples
- **When** story map exists, **then** CLI displays available epics/stories/increments to choose from
- **When** story map does not exist, **then** CLI displays format examples only

**Scenarios:**

### Scenario Outline: CLI handles invalid story scope and provides helpful prompt

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And Story graph exists with epics: <available_epics>
And Story graph has increments: <available_increments>
When user enters command: "run <invalid_scope>"
Then CLI displays "ERROR: Invalid scope syntax"
And CLI displays "Expected format:"
And CLI displays "  scope.type=epic|story|increment|all scope.value=\"Name\""
And CLI displays "Available in current story graph:"
And CLI displays "  Epics: <epics_list>"
And CLI displays "  Increments: <increments_list>"
And CLI displays "Examples:"
And CLI displays "  scope.type=epic scope.value=\"Manage Mobs\""
And CLI displays "  scope.type=increment scope.value=1"
And CLI displays "  scope.type=all"
And CLI prompts user to re-enter
```

**Examples:**

| behavior | action   | invalid_scope                      | available_epics                                        | available_increments | epics_list                                    | increments_list |
| -------- | -------- | ---------------------------------- | ------------------------------------------------------ | -------------------- | --------------------------------------------- | --------------- |
| shape    | build    | scope="wrong format"               | [Manage Mobs,Execute Mob Actions,Configure Game]       | [1,2,3]              | Manage Mobs, Execute Mob Actions, Configure Game | 1, 2, 3         |
| shape    | validate | scope.type=epic                    | [Manage Mobs,Execute Mob Actions,Configure Game]       | [1,2,3]              | Manage Mobs, Execute Mob Actions, Configure Game | 1, 2, 3         |
| shape    | render   | scope.value="Manage Mobs"          | [Manage Mobs,Execute Mob Actions]                      | [1,2]                | Manage Mobs, Execute Mob Actions              | 1, 2            |

---

### 📝 CLI --> Prompt For File Scope Parameters [mock]

**Story:** User provides invalid file scope parameter for build/render/validate action in tests/code behaviors

**User:** Runs tests or code action with malformed or invalid file scope

**Acceptance Criteria:**

- **When** user provides invalid file scope syntax, **then** CLI displays error and shows correct format for file scope AND story scope
- **When** displaying file scope help, **then** CLI shows behavior default folder and workspace folders
- **When** displaying story scope help, **then** CLI shows available epics/stories/increments

**Scenarios:**

### Scenario Outline: CLI handles invalid file/story scope in dual-scope behaviors and provides helpful prompt

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And Workspace has top-level folders: <workspace_folders>
And Behavior "<behavior>" has default folder: "<default_folder>"
And Story graph has epics: <available_epics>
When user enters command: "run <invalid_scope>"
Then CLI displays "ERROR: Invalid scope syntax"
And CLI displays "For '<behavior>' behavior, scope can be:"
And CLI displays "  File scope: scope.type=files scope.value=<path> scope.exclude=<pattern>"
And CLI displays "  Story scope: scope.type=epic|story|increment|all scope.value=\"Name\""
And CLI displays ""
And CLI displays "File scope options:"
And CLI displays "  Default for '<behavior>': <default_folder>"
And CLI displays "  Available folders: <folder_list>"
And CLI displays ""
And CLI displays "Story scope options:"
And CLI displays "  Available epics: <epics_list>"
And CLI displays ""
And CLI displays "Examples:"
And CLI displays "  scope.type=files scope.value=src/ scope.exclude=*.bak"
And CLI displays "  scope.type=epic scope.value=\"Manage Mobs\""
And CLI prompts user to re-enter
```

**Examples:**

| behavior | action   | invalid_scope           | workspace_folders                        | default_folder | available_epics                | folder_list                      | epics_list                 |
| -------- | -------- | ----------------------- | ---------------------------------------- | -------------- | ------------------------------ | -------------------------------- | -------------------------- |
| code     | validate | scope=wrongformat       | [src/,tests/,docs/,agile_bot/]           | src/           | [Manage Mobs,Execute Actions]  | src/, tests/, docs/, agile_bot/  | Manage Mobs, Execute Actions |
| tests    | build    | scope.type=files        | [src/,tests/,docs/]                      | tests/         | [Manage Mobs]                  | src/, tests/, docs/              | Manage Mobs              |
| code     | render   | scope.value=src/        | [src/,tests/,agile_bot/]                 | src/           | [Manage Mobs,Configure Game]   | src/, tests/, agile_bot/         | Manage Mobs, Configure Game |

---

### 📝 CLI --> Display Confirm and Continue Prompt [mock]**

**Acceptance Criteria:**

- **When** action completes, **then** CLI displays results summary and prompts to continue

**Scenarios:**

### Scenario Outline: CLI displays action completion and prompts for continuation

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And Action "<action>" has completed with results: <results_summary>
When action execution finishes
Then CLI displays "EXECUTED <behavior>.<action>"
And CLI displays "Results:"
And CLI displays results summary: "<results_display>"
And CLI identifies next action: "<next_action>"
And CLI prompts "Continue to next action (<next_action>)? (y/n/review)"
```

**Examples:**

| behavior | action   | results_summary                                            | results_display                                                | next_action |
| -------- | -------- | ---------------------------------------------------------- | -------------------------------------------------------------- | ----------- |
| shape    | clarify  | {questions_answered: 7, evidence_types: 3}                 | - Answered 7 key questions\n- Provided 3 evidence types       | strategy    |
| shape    | strategy | {decisions_made: 5, assumptions: 2}                        | - Made 5 decisions\n- Listed 2 assumptions                     | build       |
| shape    | build    | {items_added: 12, mode: 'create'}                          | - Added 12 items\n- Mode: create                               | validate    |

---

### 📝 User --> Enters Confirm Results [mock]**

**Acceptance Criteria:**

- **When** user confirms with 'y', **then** CLI advances to next action and updates breadcrumbs

**Scenarios:**

### Scenario Outline: User confirms action completion and advances workflow

**Steps:**

```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<current_action>"
And BehaviorActionState.completed_actions are: <completed_actions>
And CLI is prompting to continue to: "<next_action>"
When user enters: "y"
Then CLI displays "OK advancing to <next_action>"
And BehaviorActionState.current_action becomes "<next_action>"
And BehaviorActionState.completed_actions become <new_completed_actions>
And CLI displays "CURRENT: story_bot.<behavior>.<next_action>"
And CLI displays breadcrumbs: "<breadcrumbs>"
```

**Examples:**

| behavior | current_action | next_action | completed_actions  | new_completed_actions        | breadcrumbs                                                   |
| -------- | -------------- | ----------- | ------------------ | ---------------------------- | ------------------------------------------------------------- |
| shape    | clarify        | strategy    | []                 | [clarify]                    | [shape] clarify [OK] -> strategy* -> build -> validate -> render |
| shape    | strategy       | build       | [clarify]          | [clarify,strategy]           | [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render |
| shape    | build          | validate    | [clarify,strategy] | [clarify,strategy,build]     | [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render |

---

### 📝 CLI --> Advance To Next Action [mock]**

**Acceptance Criteria:**

- **When** user confirms, **then** CLI automatically moves to next action and updates state

(Covered by "User --> Enters Confirm Results" scenario above)

---

### 📝 CLI --> Loop Back To Display State [mock]**

**Acceptance Criteria:**

- **When** action completes, **then** CLI loops back to display state and wait for next command

(Covered by workflow navigation scenarios - CLI always returns to display state after any command)

---

### 📝 User --> Exit REPL**

**Acceptance Criteria:**

- **When** user enters exit, **then** CLI terminates gracefully

**Scenarios:**

### Scenario: User exits REPL

**Steps:**

```gherkin
Given CLI is running in REPL mode
When user enters command: "exit"
Then CLI displays "Goodbye!"
And CLI terminates REPL loop
And Process returns to shell
```

---

### Increment 2: Generation

---

### 📝 Generator --> Generate REPL Command Definitions**

Uses existing generator architecture:

- **Orchestrator** - Walks bot structure via `orchestrator.generate()`
- **Visitor Pattern** - Create new `ReplCommandVisitor`
- **ActionDataCollector** - Reuse to gather behavior/action metadata
- **HelpContext** - Reuse `BehaviorHelpContext` and `ActionHelpContext`

Generate command definitions by:

1. Walk all behaviors via `Orchestrator`
2. For each behavior, get actions from `ActionDataCollector`
3. For each action, get parameters from action's `context_class`
4. Generate navigate commands (behavior, action)
5. Generate scope commands (scope.type, scope.value, etc.)
6. Generate instruction commands (run)
7. Generate confirm commands (confirm, y/n)
8. Generate help commands (help, status)

See `cli_generator.py`, `cli_code_visitor.py` for reference patterns.

**Acceptance Criteria:**

- **When** generator runs, **then** `Orchestrator` walks all bot behaviors
- **When** behaviors are walked, **then** `ActionDataCollector` gathers action metadata for each behavior
- **When** actions are gathered, **then** generator extracts parameters from each action's `context_class`
- **When** metadata is collected, **then** `ReplCommandVisitor` generates navigate commands for all behaviors and actions
- **When** commands are generated, **then** scope commands are created for scope.type, scope.value, scope.exclude
- **When** all commands are defined, **then** generator outputs command definition file

---

### 📝 Generator --> Generate CLI Entry Point**

**Acceptance Criteria:**

- **When** generator updates `base_bot_cli.py`, **then** it adds REPL mode:
  ```python
  def run(self, behavior_name: str=None, action_name: str=None, 
          cli_args: list=None, stdio_mode: bool=False):
      if stdio_mode:
          return self._run_repl_mode()
      else:
          return self.router.route_to_action(behavior_name, action_name, cli_args or [])

  def _run_repl_mode(self):
      # Detect TTY vs piped input
      # Display initial state
      # Loop: read command → parse → execute → display result
      pass
  ```
- **When** REPL mode is added, **then** it integrates with existing `CliCommandRouter` for routing logic
- **When** REPL loop is generated, **then** it includes TTY detection, state display, command parsing, and execution

---

### 📝 Generator --> Generate Cursor Commands**

**Acceptance Criteria:**

- **When** generator creates `CursorReplVisitor`, **then** it follows existing pattern:
  ```python
  visitor = CursorReplVisitor(workspace_root, cli_script_path, bot)
  orchestrator = Orchestrator(visitor)
  orchestrator.generate()
  ```
- **When** visitor generates shortcuts, **then** it creates navigate shortcuts: `/story_bot-shape`, `/story_bot-discovery`
- **When** visitor generates action shortcuts, **then** it creates: `/story_bot-shape-clarify`, `/story_bot-shape-validate`
- **When** visitor generates help shortcuts, **then** it creates: `/story_bot-help`, `/story_bot-status`

---

### 📝 Generator --> Generate Help Documentation**

**Acceptance Criteria:**

- **When** generator creates `HelpReplVisitor`, **then** it generates command reference with all REPL commands
- **When** help is generated, **then** it includes parameter reference with descriptions for all action parameters
- **When** examples are generated, **then** it includes scope examples: `scope.type=epic scope.value="Epic Name"`
- **When** documentation is output, **then** it creates Markdown help files in `.cursor/commands/` and terminal help via `CliHelpGenerator`

### Increment 3: Base Parameters (No Scope)

All stories execute REAL backend code (scope=all assumed).

---

### 📝 CLI --> Parse Command Input [real]**

**Acceptance Criteria:**

- **When** user enters dot-notation parameters, **then** parser creates nested structure:
  ```python
  # Input: clarify.key_questions.q1="What is the scope?" strategy.decisions.d1="Use REST"

  # Parser creates tree:
  {
      "clarify": {"key_questions": {"q1": "What is the scope?"}},
      "strategy": {"decisions": {"d1": "Use REST"}}
  }
  ```
- **When** parsing dot-notation, **then** parser splits on `.` to create nested structure
- **When** values are quoted, **then** parser extracts quoted strings
- **When** values are comma-separated, **then** parser creates arrays

---

### 📝 CLI --> Validate Instruction Syntax and Regular Parameters [real]**

**Acceptance Criteria:**

- **When** validating parameters, **then** CLI checks against action's `context_class`:
  ```python
  action_class = ActionFactory.get_action_class('clarify')
  context_class = action_class.context_class  # ClarifyActionContext

  for field in dataclasses.fields(context_class):
      if field.name in required_params:
          # Validate parameter type and value
  ```
- **When** parameters are invalid, **then** CLI returns validation error with details

---

### 📝 CLI --> Prompt User For Missing Parameters [real]**

**Acceptance Criteria:**

- **When** parameters are missing, **then** CLI prompts interactively:
  ```
  < run

  > MISSING PARAMETERS for shape.clarify
  > 
  > key_questions_answered: Dict mapping question keys to answer strings
  > 
  > Enter key_questions_answered (or 'skip'):
  < clarify.key_questions.q1="What is scope?" clarify.key_questions.q2="Who are users?"
  > OK received 2 key questions
  ```

---

### 📝 CLI --> Execute Current Action [real, scope=all]**

**Acceptance Criteria:**

- **When** executing action, **then** CLI builds ActionContext and sets default scope:
  ```python
  context = CliContextBuilder().build_context(action, cli_args)
  context.scope = ScopeConfig(type='all', value=[])
  result_data = action.execute(context)
  ```
- **When** scope is not specified, **then** CLI defaults to `scope=all`

---

### 📝 CLI --> Display Action Output [real]**

**Acceptance Criteria:**

- **When** action completes, **then** CLI displays real results:
  ```
  > EXECUTED shape.clarify
  > 
  > Results:
  >   - Answered 7 key questions
  >   - Provided 3 evidence types
  >   - Saved to C:\dev\my-project\clarification.json
  >   - Duration: 2.3s
  > 
  > {"status": "success", "action": "clarify", "data": {...}}
  ```

---

### 📝 CLI --> Advance To Next Action [real]**

**Acceptance Criteria:**

- **When** action completes, **then** CLI updates behavior_action_state.json:
  ```python
  behavior.actions.close_current()  # Mark current as complete
  next_action = behavior.actions.forward_to_current()  # Advance
  ```
- **When** advancing, **then** CLI saves updated state to behavior_action_state.json

---

### 📝 CLI --> Loop Back To Display State [real]**

**Acceptance Criteria:**

- **When** workflow advances, **then** CLI reads updated behavior_action_state.json
- **When** state is read, **then** CLI displays new current state with updated breadcrumbs

### Increment 4a: Story Parameters (Mock Backend)

Test story/epic scope parsing without executing backend.

---

### 📝 CLI --> Parse Story Scope [mock]**

**Acceptance Criteria:**

- **When** user enters story scope dot-notation, **then** parser creates structure:
  ```bash
  # Input
  scope.type=epic scope.value="Manage Mobs"

  # Parsed output
  {
      "scope": {
          "type": "epic",
          "value": ["Manage Mobs"]
      }
  }
  ```
- **When** `scope.type=epic`, **then** scope.value contains epic names
- **When** `scope.type=story`, **then** scope.value contains story names
- **When** `scope.type=increment`, **then** scope.value contains increment numbers

---

### 📝 CLI --> Validate Story Scope Parameters [mock]**

**Acceptance Criteria:**

- **When** validating scope, **then** `scope.type` must be one of: epic, story, increment, all
- **When** scope.type is epic/story/increment, **then** `scope.value` is required
- **When** scope.value is provided, **then** it can be single value or comma-separated list
- **When** validation runs (mock), **then** CLI returns mock validation result without checking if stories/epics actually exist

---

### 📝 CLI --> Prompt User For Missing Story Scope [mock]**

**Acceptance Criteria:**

- **When** story scope is missing, **then** CLI prompts interactively:
  ```
  < run

  > Scope not specified. Use scope=all? (y/n/specify):
  < n

  > Enter scope (e.g., scope.type=epic scope.value="Epic Name"):
  < scope.type=epic scope.value="Manage Mobs"
  > OK scope set to epic: Manage Mobs
  ```

---

### Increment 4b: Story Parameters (Real Backend)

Execute with real story/epic scope filtering.

---

### 📝 CLI --> Parse Story Scope [real]**

**Acceptance Criteria:**

- **When** parsing story scope (real), **then** uses same parsing logic as Increment 4a
- **When** parsed, **then** scope is passed through to real backend via ActionContext

---

### 📝 CLI --> Apply Story Scope Filter [real]**

**Acceptance Criteria:**

- **When** applying story scope filter, **then** CLI creates scoped ActionContext:
  ```python
  context = ClarifyActionContext(
      scope=ScopeConfig(type='epic', value=['Manage Mobs'])
  )

  # Action receives context and filters:
  if context.scope.type == 'epic':
      stories = story_map.filter_by_epic(context.scope.value)
  elif context.scope.type == 'story':
      stories = story_map.filter_by_story(context.scope.value)
  ```

---

### 📝 CLI --> Execute Action With Story Scope [real]**

**Acceptance Criteria:**

- **When** executing with story scope, **then** CLI produces results only for targeted stories/epics:
  ```
  > EXECUTING shape.validate with scope: epic=Manage Mobs
  > 
  > Validating stories in epic "Manage Mobs":
  >   - Create Mob: PASS
  >   - Edit Mob: FAIL - Missing acceptance criteria
  >   - Delete Mob: PASS
  > 
  > {"status": "success", "epic": "Manage Mobs", "validated": 3, "failed": 1}
  ```

### Increment 5a: File Parameters (Mock Backend)

Test file scope parsing without executing backend.

---

### 📝 CLI --> Parse File Scope [mock]**

**Acceptance Criteria:**

- **When** user enters file scope dot-notation, **then** parser creates structure:
  ```bash
  # Input
  scope.type=files scope.value=src/,tests/ scope.exclude=*.bak

  # Parsed output
  {
      "scope": {
          "type": "files",
          "value": ["src/", "tests/"],
          "exclude": ["*.bak"]
      }
  }
  ```
- **When** parsing file scope, **then** `scope.value` contains file paths or patterns (comma-separated)
- **When** parsing file scope, **then** `scope.exclude` contains exclusion patterns (comma-separated)

---

### 📝 CLI --> Validate File Scope Parameters [mock]**

**Acceptance Criteria:**

- **When** validating file scope, **then** `scope.type` must be `files`
- **When** scope.type is files, **then** `scope.value` is required
- **When** validating, **then** `scope.exclude` is optional
- **When** validation runs (mock), **then** CLI returns mock result without checking if files actually exist

---

### 📝 CLI --> Prompt User For Missing File Scope [mock]**

**Acceptance Criteria:**

- **When** file scope is missing, **then** CLI prompts interactively:
  ```
  < run

  > File scope not specified. Validate all files? (y/n/specify):
  < n

  > Enter file scope (e.g., scope.type=files scope.value=src/ scope.exclude=*.test.py):
  < scope.type=files scope.value=src/,tests/
  > OK scope set to files: src/, tests/
  ```

---

### Increment 5b: File Parameters (Real Backend)

Execute with real file scope filtering.

---

### 📝 CLI --> Parse File Scope [real]**

**Acceptance Criteria:**

- **When** parsing file scope (real), **then** uses same parsing logic as Increment 5a
- **When** parsed, **then** scope is passed through to real backend via ActionContext

---

### 📝 CLI --> Apply File Scope Filter [real]**

**Acceptance Criteria:**

- **When** applying file scope filter, **then** CLI creates scoped ActionContext:
  ```python
  context = ValidateActionContext(
      scope=ScopeConfig(
          type='files',
          value=['src/', 'tests/'],
          exclude=['*.bak', '*.tmp']
      )
  )

  # Action receives context and filters:
  files = []
  for pattern in context.scope.value:
      files.extend(glob.glob(pattern + '**/*.py', recursive=True))

  # Apply exclusions
  for exclude_pattern in context.scope.exclude:
      files = [f for f in files if not fnmatch.fnmatch(f, exclude_pattern)]
  ```

---

### 📝 CLI --> Execute Action With File Scope [real]**

**Acceptance Criteria:**

- **When** executing with file scope, **then** CLI produces results only for targeted files:
  ```
  > EXECUTING code.validate with scope: files=src/,tests/ exclude=*.bak
  > 
  > Validating files:
  >   src/bot.py: 3 issues
  >   src/cli.py: PASS
  >   tests/test_bot.py: PASS
  > 
  > Scanned 127 files, found 3 issues in 1 file
  > 
  > {"status": "success", "files_scanned": 127, "issues_found": 3}
  ```

---

## Detailed REPL Examples

### Full Shape Workflow Example

Complete shape behavior session showing ACTUAL content from shape guardrails:

```
story_bot --stdio

> CURRENT: story_bot.shape.clarify
> Working Directory: C:\dev\mm3e
> 
> [shape] clarify* -> strategy -> build -> validate -> render
> 
> Ready for commands.

< run
> EXECUTING shape.clarify...
> 
> ## Clarify: Gathering Context
> 
> Loaded context from: C:\dev\mm3e\docs\context\input.txt
> 
> **Key Questions to Answer:**
> 
> 1. Who are the distinct types of users?
>    -> Player (creates/manages character), GM (reviews/approves), System
> 
> 2. What are the key goals each group is trying to accomplish?
>    -> Player: Create character, assign abilities, track power points
>    -> GM: Review builds, manage campaign rules
> 
> 3. What is the first thing users will try to do?
>    -> Create a new character with basic abilities
> 
> 4. What problems or workarounds is this eliminating?
>    -> Manual calculation of power points, paper character sheets
> 
> 5. What is the user journey from start to finish?
>    -> Select archetype -> Assign abilities -> Configure powers -> Calculate costs -> Save
> 
> 6. What is the business domain we are modeling?
>    -> Mutants & Masterminds 3rd Edition character creation
> 
> 7. What are the core business concepts and relationships?
>    -> Character, Ability, Power, PowerPoint, Effect, Modifier, Archetype
> 
> **Evidence Provided:**
> - MM3E Handbook reference (primary source)
> - Character sheet examples
> - Power point calculation rules
> 
> Saved to: clarification.json
> 
> {"status": "success", "action": "clarify", ...}
> 
> CURRENT: story_bot.shape.strategy
> [shape] clarify [OK] -> strategy* -> build -> validate -> render
> 
> (Review answers above. Type 'run' to continue, or provide corrections)

< run
> EXECUTING shape.strategy...
> 
> ## Strategy: Decision Criteria
> 
> **Typical Assumptions (confirm or modify):**
> [x] Focus on user flow over internal systems
> [x] Cover the end-to-end scenario
> [x] Prioritize customer-facing features
> [x] Assume stories should be independently testable
> [x] Focus on core domain over supporting domains
> [x] Use ubiquitous language from domain sources
> 
> **Decision: Flow Scope and Granularity**
> Question: How wide are we going with the flow?
> Options:
>   1. End-to-end user-system behavior (one interaction -> one response)
>   2. Journey level (complete user journey across touchpoints)
>   3. Intra-system level (within single system)
>   4. Domain boundary level (by business domain boundaries)
> Selected: [1] End-to-end user-system behavior
> 
> **Decision: Depth of Shaping**
> Question: How deep should we drill down?
> Options:
>   1. Estimates -> story_count only
>   2. Decompose -> Discover all stories listed
>   3. Workflow -> Figure out logical process, conditions
>   4. Extensive -> Specify all scenarios
> Selected: [2] Decompose -> Discover all stories listed
> 
> **Decision: Drill-Down Approach**
> Question: What areas to explore more deeply?
> Options:
>   1. Dig deep on business complexity
>   2. Dig deep on user workflows
>   3. High and wide across all epics
>   4. Focus on highest value areas
> Selected: [2, 4] User workflows + Highest value areas
> 
> Saved to: strategy.json
> 
> {"status": "success", "action": "strategy", ...}
> 
> CURRENT: story_bot.shape.build
> [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render

< run
> EXECUTING shape.build...
> 
> ## Build: Creating Story Map + Domain Model
> 
> Building story-graph.json...
> 
> **Epics Created:**
>   - Create Character (5 features, 12 stories)
>   - Manage Abilities (3 features, 8 stories)
>   - Configure Powers (4 features, 15 stories)
> 
> **Domain Concepts Identified:**
>   - Character (aggregate root)
>   - Ability (entity: Strength, Agility, Fighting, etc.)
>   - Power (entity with Effects and Modifiers)
>   - PowerPoint (value object)
>   - Archetype (entity)
> 
> Saved to: story-graph.json
> 
> {"status": "success", "action": "build", "epics": 3, "stories": 35, ...}
> 
> CURRENT: story_bot.shape.validate
> [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render

< scope.type=epic scope.value="Create Character"
> OK scope.type=epic
> OK scope.value=Create Character

< run
> EXECUTING shape.validate (scope: epic="Create Character")...
> 
> ## Validate: Checking Rules
> 
> Scanning 12 stories in "Create Character" epic...
> 
> **Violations Found: 2**
> 
> 1. Story "Power Setup" violates: use_verb_noun_format
>    Suggestion: Rename to "Configure Initial Powers"
> 
> 2. Story "Ability Configuration" violates: enforce_functional_accomplishment
>    Issue: Too vague - what is the functional outcome?
>    Suggestion: "Assign Ability Scores" or "Select Ability Values"
> 
> {"status": "success", "action": "validate", "violations": 2, ...}
> 
> CURRENT: story_bot.shape.validate
> [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render
> 
> (Fix violations and re-run, or proceed with 'action render')

< run
> EXECUTING shape.validate (scope: epic="Create Character")...
> 
> ## Validate: Checking Rules
> 
> Scanning 12 stories in "Create Character" epic...
> 
> **Violations: 0**
> All stories pass validation rules.
> 
> {"status": "success", "action": "validate", "violations": 0, ...}
> 
> CURRENT: story_bot.shape.render
> [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate [OK] -> render*

< run
> EXECUTING shape.render...
> 
> ## Render: Generating Output Documents
> 
> "Going to be going away for a little while to render the output. 
>  Go get a cup of coffee :)"
> 
> **Generated Files:**
>   - docs/stories/story-map-outline.drawio
>   - docs/stories/story-map.md
>   - docs/stories/mm3e-domain-model-description.md
>   - docs/stories/mm3e-domain-model-diagram.mmd
> 
> {"status": "success", "action": "render", ...}
> 
> COMPLETE: shape behavior finished
> 
> CURRENT: story_bot.discovery.clarify
> [discovery] clarify* -> strategy -> build -> validate -> render
> 
> (Shape complete. Ready for discovery, or type 'exit' to quit)

< exit
> GOODBYE
```

---

## REPL Example: Jump Around

You can navigate freely within the session:

```
> CURRENT: story_bot.shape.validate

< action clarify
> OK action=clarify
> CURRENT: story_bot.shape.clarify

< behavior discovery
> OK behavior=discovery
> CURRENT: story_bot.discovery.clarify

< back
> OK back to shape
> CURRENT: story_bot.shape.clarify

< action build
> OK action=build
> CURRENT: story_bot.shape.build

< status
> ## Current State
> behavior: shape
> action: build
> workspace: C:\dev\mm3e
> scope: (none)
> 
> [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render
```

---

## REPL Example: Scoped Validation

Setting scope before running:

```
> CURRENT: story_bot.shape.validate

< scope.type increment
> OK scope.type=increment

< scope.value 1
> OK scope.value=[1]

< scope.value 2
> OK scope.value=[1, 2]

< scope.exclude test_*.py
> OK scope.exclude=[test_*.py]

< status
> scope:
>   type: increment
>   value: [1, 2]
>   exclude: [test_*.py]

< run
> EXECUTING shape.validate (scope: increment=[1,2], exclude=[test_*.py])...

< reset scope
> OK scope cleared

< status
> scope: (none)
```

---

## Protocol Summary

**Commands:**


| Command           | Description                            |
| ------------------- | ---------------------------------------- |
| workspace<path>   | Set working directory                  |
| behavior<name>    | Switch to behavior                     |
| action<name>      | Jump to action within current behavior |
| scope.<key>=<val> | Set scope parameter                    |
| run               | Execute current action                 |
| back              | Go to previous action                  |
| status            | Show current state and scope           |
| reset [scope]     | Clear accumulated state or just scope  |
| help              | Show available commands                |
| exit              | Quit the REPL                          |

**Responses:**


| Response          | Meaning                           |
| ------------------- | ----------------------------------- |
| FRESH             | No existing state, need workspace |
| CURRENT:<path>    | Current behavior.action position  |
| OK<detail>        | Command accepted                  |
| ERROR:<message>   | Command failed                    |
| EXECUTING<action> | Action running                    |
| COMPLETE          | Behavior workflow finished        |
| GOODBYE           | Session ended                     |

**The REPL stays open** until you type `exit`. This allows:

- Iterating through workflow steps
- Re-running actions after fixes
- Adjusting scope between runs
- Navigating freely through behaviors/actions

---

## Where STDIO Lives

At the very front door of your CLI.

Right where your program starts. Think of your CLI in three layers:

### Entry Point (where STDIO happens)

This is your main or command handler. Here's where you decide:

- Did the user pass flags?
- Did they pass --stdin?
- Did they pass nothing?

If --stdio is present:

- Stop parsing arguments
- Read from standard input
- Treat stdin as the source of truth

This is where AI talks to your tool.

### Input Normalization Layer (the magic)

Everything - flags, dot-notation, env vars, files, stdin - gets converted
into one internal config object.

This layer:

- Merges inputs
- Applies defaults
- Validates structure
- Produces a single canonical shape

This is where dot-notation gets expanded into nested objects.

### Execution Layer (never knows where input came from)

This layer does the real work:

- validate
- generate
- transform
- run rules

It does not care whether input came from:

- flags
- STDIO
- config file
- AI
- human typing

That separation is what keeps everything sane.

### Where humans vs AI split

- Humans mostly interact at layer 1 with flags or prompts
- AI mostly interacts at layer 1 using STDIO
- Both meet cleanly at layer 2

---

## Interactive Prompt Mode (Human-First)

When no parameters are passed:

```bash
story_bot
```

The CLI asks questions:

- What behavior do you want?
- Which action?
- What scope?
- Any advanced options?

This is fantastic for humans, and AI can still automate it via STDIO.

Add --non-interactive mode for scripts that must not prompt.

---

## Hybrid Approach: Flags + Escape Hatch

Most parameters stay normal flags:

```bash
story_bot --behavior shape --action validate --skip-cross-file
```

Only the hard ones use something special:

```bash
story_bot --behavior shape --action validate --config-file advanced.json
```

Humans use flags.
AI or power users use files or STDIO.
Everyone wins.

This avoids forcing JSON everywhere.

---

## Implementation Components

### 1. StdioHandler Class (REPL)

Handles interactive STDIO REPL for AI/automation/humans:

- run() - Main REPL loop: show state, read lines, process, respond, loop
- show_current_state() - Display breadcrumbs and available commands
- process_line(line) - Parse command, update state, return response
- set_dotted(path, value) - Handle dot-notation like scope.type=epic
- execute_action() - Run current action, show result, advance workflow
- navigate(behavior, action) - Jump to specific behavior/action

**Key difference from one-shot:** After execute, show NEW state and wait for next command.

State tracking:
workspace          -> state["workspace"] = "C:\dev\project"
behavior shape     -> state["behavior"] = "shape"
action validate    -> state["action"] = "validate"
scope.type epic    -> state["scope"]["type"] = "epic"
scope.value X      -> state["scope"]["value"] = ["X"]
run                -> execute, show result, advance to next action, loop
exit               -> break loop, goodbye

### 2. DotNotationParser Class

Parse dot-notation arguments into nested config:

Input:  ["scope.type=epic", "scope.value=Mob,Action"]
Output: {"scope": {"type": "epic", "value": ["Mob", "Action"]}}

Features:

- Split on dots to create nesting
- Comma-separated values become lists
- Repeated keys append to lists
- Numeric strings convert to integers

### 3. InteractivePrompt Class

Prompt for missing required information when running interactively:

- prompt_if_needed(args, context) - Fill in missing params
- prompt_choice(prompt, options) - Show numbered menu, get selection
- prompt_scope() - Build ScopeConfig interactively

Only activates when:

- stdin is a TTY (human at keyboard)
- --non-interactive flag is NOT set
- Required information is missing

### 4. Updated Entry Point Flow

```
main():
    # STDIO REPL mode - stays open until exit
    if "--stdio" in sys.argv:
        StdioHandler(self).run()  # REPL loop - doesn't exit until 'exit' command
        return

    # One-shot mode (current behavior)
    non_interactive = "--non-interactive" in sys.argv

    # Parse traditional arguments
    args, cli_args = parse_arguments()

    # Parse dot-notation from CLI args
    dot_config = DotNotationParser.parse(cli_args)

    # Interactive prompting if missing info
    if not non_interactive and sys.stdin.isatty():
        dot_config = InteractivePrompt(self).prompt_if_needed(args, dot_config)

    # Merge and normalize all inputs
    context = normalize_inputs(args, dot_config)

    # Execute single command and exit
    dispatch_command(args, context)
```

**Key difference:**

- `--stdio` runs a REPL that stays open (loop until 'exit')
- Normal mode runs one command and exits (current behavior)

---

## Usage Examples

### Human Usage (Simple)

```bash
# Interactive - prompts for what you need
story_bot

# Quick validate with dot-notation
story_bot --behavior shape --action validate scope.type=epic scope.value="Manage Mobs"

# Multiple increments
story_bot -b shape -a validate scope.type=increment scope.value=1,2,3

# Files with exclude
story_bot -b code -a validate scope.type=files scope.value=src/ scope.exclude=*.bak

# Short form with flags
story_bot -b shape -a build --skip-cross-file --all-files
```

### AI Usage (STDIO)

```bash
story_bot --stdio
```

Then via stdin (AI or human - doesn't matter):

```
> CURRENT: story_bot.shape.build
> [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render

< action validate
> OK action=validate

< scope.type=epic scope.value="Manage Mobs"
> OK scope.type=epic
> OK scope.value=Manage Mobs

< run
> EXECUTING shape.validate (scope: epic="Manage Mobs")...
> {"status": "success", "violations": 0, ...}
> 
> CURRENT: story_bot.shape.render

< run
> EXECUTING shape.render...
> {"status": "success", ...}
> 
> COMPLETE: shape behavior finished

< exit
> GOODBYE
```

The REPL stays open - iterate, fix, re-run, navigate freely.

### Scripted/CI Usage (Non-Interactive)

```bash
# Non-interactive with dot-notation
story_bot --non-interactive --behavior shape --action validate scope.type=all

# Or pipe commands via STDIO
echo -e "behavior shape\naction validate\nscope.type all\nrun" | story_bot --stdio
```

---

## Layer Summary


| Layer        | Interface                               | Who Uses It    | Complexity |
| -------------- | ----------------------------------------- | ---------------- | ------------ |
| Flags        | --behavior, --action, --skip-cross-file | Everyone       | Low        |
| Dot-notation | scope.type=epic scope.value=X           | Humans & AI    | Medium     |
| STDIO        | Line-based conversation                 | AI, Automation | High       |
| Interactive  | Prompts when info missing               | Humans         | Zero       |
| Config file  | --config-file advanced.json             | Power users    | Optional   |

**JSON is never required.** It's an optional power-user escape hatch.

---

## Value Handling in STDIO

- Comma-separated values become lists: scope.value=a,b,c
- Repeated commands append: scope.value=a then scope.value=b -> ["a", "b"]
- Numeric strings convert: scope.value=1,2,3 -> [1, 2, 3]
- Quoted values preserve spaces: scope.value="Manage Mobs"
- Dot-notation works with = or space: scope.type=epic OR scope.type epic

---

## Migration Path

1. **Phase 1: Add dot-notation parser**

   - New DotNotationParser class
   - Integrate into existing CLI flow
   - Existing --scope JSON still works (backward compatible)
2. **Phase 2: Add STDIO mode**

   - New StdioHandler class
   - New --stdio flag
   - No changes to existing command parsing
3. **Phase 3: Add interactive prompts**

   - New InteractivePrompt class
   - Only activates for TTY + missing info
   - Add --non-interactive flag
4. **Phase 4: Deprecate raw JSON**

   - Keep JSON support but document dot-notation as preferred
   - Update all documentation and examples

---

## Files to Create/Modify

### New Files


| File                       | Purpose                 |
| ---------------------------- | ------------------------- |
| cli/stdio_handler.py       | STDIO mode handler      |
| cli/dot_notation_parser.py | Dot-notation parsing    |
| cli/interactive_prompt.py  | Interactive prompting   |
| cli/input_normalizer.py    | Merge all input sources |

### Modified Files


| File                        | Changes                          |
| ----------------------------- | ---------------------------------- |
| cli/base_bot_cli.py         | Add --stdio routing, prompt flow |
| cli/cli_parameter_parser.py | Integrate dot-notation           |
| cli/cli_context_builder.py  | Accept normalized config         |

---

## Type Definitions (Implementation Reference)

### Action Return Value Types (Type-Safe Structure)

All actions return `Dict[str, Any]`, but with well-defined typed structure:

```python
# Type definitions for return values

@dataclass
class ClarifyResult:
    """Result from clarify action"""
    instructions: ClarifyInstructions

@dataclass  
class ClarifyInstructions:
    """Instructions for clarify action"""
    action: str  # 'clarify'
    behavior: str  # e.g. 'shape'
    base_instructions: List[str]
    guardrails: RequiredContext
    # Plus other instruction data from action_config.json

@dataclass
class RequiredContext:
    """Required context structure in guardrails"""
    key_questions: List[str]
    evidence: List[str]

# ---

@dataclass
class StrategyResult:
    """Result from strategy action"""
    instructions: StrategyInstructions

@dataclass
class StrategyInstructions:
    """Instructions for strategy action"""
    action: str  # 'strategy'
    behavior: str
    base_instructions: List[str]
    strategy: StrategyData
    # Plus other instruction data

@dataclass
class StrategyData:
    """Strategy data structure"""
    strategy_criteria: Dict[str, Any]
    assumptions: List[str]
    recommended_activities: List[str]

# ---

@dataclass
class BuildResult:
    """Result from build action"""
    instructions: BuildInstructions

@dataclass
class BuildInstructions:
    """Instructions for build action"""
    action: str  # 'build'
    behavior: str
    base_instructions: List[str]
    knowledge_graph_template: TemplatePointer
    knowledge_graph_config: GraphConfig
    rules: List[Dict[str, Any]]
    scope: Dict[str, Any]
    scope_story_names: List[str]
    existing_file: FileInfo
    # Plus other instruction data

@dataclass
class TemplatePointer:
    """Pointer to template file (not the content)"""
    template_path: Optional[str]  # Path to template file
    exists: bool

@dataclass
class GraphConfig:
    """Knowledge graph configuration"""
    output: str  # Output filename
    path: str    # Output directory path
    template: str  # Template filename

@dataclass
class FileInfo:
    """File existence info"""
    path: str
    exists: bool

# ---

@dataclass
class ValidateResult:
    """Result from validate action"""
    instructions: ValidateInstructions

@dataclass
class ValidateInstructions:
    """Instructions/results from validate action"""
    action: str  # 'validate'
    behavior: str
    base_instructions: List[str]  # Includes scanner status and violation summary
    validation_rules: List[ProcessedRule]  # Rules with violations from scanners
    content_to_validate: None
    report_path: str  # Path to validation report file
    report_link: str  # Clickable hyperlink to report

@dataclass
class ProcessedRule:
    """Processed validation rule with scanner results"""
    rule_file: str
    rule_content: Dict[str, Any]
    scanner_status: ScannerStatus
    violations: ViolationData

@dataclass
class ScannerStatus:
    """Scanner execution status"""
    status: str  # 'EXECUTED', 'LOAD_FAILED', 'EXECUTION_FAILED', 'NO_SCANNER'
    scanner_path: str
    execution_status: str
    # ... other status fields

@dataclass
class ViolationData:
    """Violation data from scanner"""
    file_by_file: Optional[Dict[str, List[Violation]]]
    cross_file: Optional[Dict[str, List[Violation]]]

@dataclass
class Violation:
    """A single violation found by scanner"""
    file: str
    line: Optional[int]
    column: Optional[int]
    message: str
    severity: str  # 'error', 'warning', etc.
    rule: str

# ---

@dataclass
class RenderResult:
    """Result from render action"""
    instructions: RenderInstructions
    executed_specs: List[RenderSpec]  # Specs that ran synchronizers
    template_specs: List[RenderSpec]  # Specs requiring AI template rendering

@dataclass
class RenderInstructions:
    """Merged render instructions with template data"""
    # Structure varies based on render configuration
    pass

@dataclass
class RenderSpec:
    """Render specification"""
    name: str
    config_data: Dict[str, Any]
    # ... other spec fields
```

---

## Key Design Principles

1. **Humans speak in flags** - Simple, familiar
2. **Power users speak in dot-notation** - Structured, no JSON
3. **AI speaks in STDIO** - Conversational, explicit
4. **The engine only hears one language** - Normalized config
5. **JSON is optional** - Never required, always accepted as escape hatch
6. **STDIO belongs in the command entry point** - Everything flows into
   a single normalized config before execution
7. **Interactive prompts fill gaps** - Missing info triggers questions,
   not errors (unless --non-interactive)

---

## One-Sentence Takeaway

STDIO turns your CLI from a fragile sentence into a durable dialogue.

---

## Related Documents

- langgraph-orchestration.md - LangGraph integration (--workflow flag)
- CLI context builder - cli_context_builder.py
- Action contexts - action_context.py (ScopeConfig, etc.)
