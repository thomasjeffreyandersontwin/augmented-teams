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
    Route to action: Command Router
    Execute action: Action Executor
    Exit loop: Output Formatter

Behavior Action State
    Track current behavior: Behavior
    Track current action: Action
    Store completed actions: Completed Actions
    Store clarifications: Clarifications
    Store strategy decisions: Strategy Decisions
    Store scope: File Scope, Story Scope
    Persist to file: behavior_action_state.json

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
    Build context: Context Builder
    Navigate to action: Behavior Action State

Context Builder
    Build typed context: Action Context
    Validate parameters: Parameter Parser
    Apply defaults: Scope

Action Executor
    Execute action: Action
    Capture results: Action Results
    Update state: Behavior Action State

Behavior
    Retrieve instructions: Action Instructions
    List available actions: Actions
    Navigate to action: Behavior Action State

Action
    Provide instructions: Action Instructions
    Define required parameters: Action Context
    Execute with context: Action Results

Action Context
    Store scope: File Scope, Story Scope
    Store clarifications: Clarifications
    Store strategy: Strategy Decisions
    Provide to action: Action

Action Instructions
    Display to user: Output Formatter
    List required parameters: File Scope, Story Scope

Action Results
    Save to state: Behavior Action State
    Display to user: Output Formatter
    Advance to next action: Behavior Action State

Completed Actions
    Track action state: Action
    Track timestamp: Action

File Scope
    Include files: File Patterns
    Exclude files: File Patterns
    Apply to action: Action

Story Scope
    Select stories: Story Names
    Select epics: Epic Names
    Apply to action: Action

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
    Generate scope examples: File Scope, Story Scope

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
    Generate instruction commands: Action Instructions
    Generate confirm commands: Action Results

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

### 📝 User --> Launch REPL Loop

**Acceptance Criteria:**
- **When** user runs `story_bot --stdio` from terminal, **then** CLI launches REPL loop
- **When** REPL loop starts, **then** CLI detects if input is TTY (interactive) or piped
- **When** CLI detects input source, **then** appropriate session mode is activated

---

### 📝 CLI --> Display Fresh Start [mock]

**Acceptance Criteria:**
- **When** no behavior_action_state.json exists, **then** CLI displays:
  ```
  story_bot --stdio
  
  > FRESH
  > No workspace configured
  ```

- **When** fresh start is detected, **then** CLI displays available commands:
  ```
  > Commands:
  >   workspace <path>     Set working directory
  >   behavior <name>      Select behavior (shape, discovery, exploration, ...)
  >   help                 Show all commands
  >   exit                 Quit
  ```

- **When** user enters workspace command, **then** CLI responds:
  ```
  < workspace C:\dev\my-project
  > OK workspace=C:\dev\my-project
  ```

- **When** user selects behavior, **then** CLI responds:
  ```
  < behavior shape
  > OK behavior=shape
  > 
  > CURRENT: story_bot.shape.clarify
  > [shape] clarify* -> strategy -> build -> validate -> render
  ```

---

### 📝 CLI --> Display Existing State [mock]

**Acceptance Criteria:**
- **When** behavior_action_state.json exists, **then** CLI displays current position and working directory:
  ```
  story_bot --stdio
  
  > CURRENT: story_bot.shape.build
  > Working Directory: C:\dev\my-project
  ```

- **When** state exists, **then** CLI displays behavior/action progress with status indicators:
  ```
  > ## Behavior/Action Progress
  > ### -> shape
  >   - [OK] clarify
  >   - [OK] strategy
  >   - [>>] build
  >   -  [ ] validate
  >   -  [ ] render
  > ### [ ] discovery
  > ### [ ] exploration
  ```
  Where: [OK] = completed, [>>] = current, [ ] = pending

- **When** state is displayed, **then** CLI shows available commands:
  ```
  > Commands:
  >   run                  Execute current action (build)
  >   current              Continue with current action
  >   close                Mark current complete and advance to next
  >   action <name>        Jump to action (clarify, strategy, build, validate, render)
  >   behavior <name>      Switch behavior
  >   scope.<key>=<val>    Set scope parameters
  >   status               Show current state
  >   back                 Go to previous action
  >   help                 Show all commands
  >   exit                 Quit
  ```

---

### 📝 CLI --> Show Current Position In Workflow Breadcrumbs [mock]

**Acceptance Criteria:**
- **When** displaying workflow breadcrumbs, **then** CLI shows format:
  ```
  [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render
  ```
  Where: `*` = current action, `[OK]` = completed action, `->` = workflow sequence

- **When** action is current, **then** CLI marks it with `*` indicator
- **When** action is completed, **then** CLI marks it with `[OK]` indicator  
- **When** behavior name is shown, **then** CLI displays it in brackets: `[behavior]`

---

### 📝 CLI --> Show Available Behaviors and Actions [mock]

**Acceptance Criteria:**
- **When** user selects behavior, **then** CLI responds:
  ```
  < behavior shape
  > OK behavior=shape
  > 
  > CURRENT: story_bot.shape.clarify
  > [shape] clarify* -> strategy -> build -> validate -> render
  ```

---

### 📝 User --> Navigate To Behavior [mock]**

**Acceptance Criteria:**
- **When** user enters `behavior {name}`, **then** CLI switches behavior and responds:
  ```
  < behavior discovery
  > OK behavior=discovery
  > CURRENT: story_bot.discovery.clarify
  > [discovery] clarify* -> strategy -> build -> validate -> render
  ```

---

### 📝 User --> Navigate To Action [mock]

**Acceptance Criteria:**
- **When** user enters `action {name}`, **then** CLI jumps to specified action and responds:
  ```
  < action validate
  > OK action=validate
  > CURRENT: story_bot.shape.validate
  > [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render
  ```

---

### 📝 User --> Navigate Within Behavior [mock]

**Acceptance Criteria:**
- **When** user enters `current`, **then** CLI continues with current action:
  ```
  < current
  > CURRENT: story_bot.shape.build
  > [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render
  > Ready to run current action
  ```

- **When** user enters `close`, **then** CLI marks current action complete and advances to next:
  ```
  < close
  > Closing current action: build
  > Advancing to next action
  > CURRENT: story_bot.shape.validate
  > [shape] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render
  ```

- **When** user enters `back`, **then** CLI returns to previous action:
  ```
  < back
  > Moving back to previous action
  > CURRENT: story_bot.shape.strategy
  > [shape] clarify [OK] -> strategy* -> build -> validate -> render
  ```

---

### 📝 User --> Request Help [mock]

**Acceptance Criteria:**
- **When** user enters `help`, **then** CLI displays all available commands:
  ```
  < help
  > Commands:
  >   run                  Execute current action
  >   current              Continue with current action
  >   close                Mark current complete and advance to next
  >   action <name>        Jump to specific action
  >   behavior <name>      Switch behavior
  >   scope.<key>=<val>    Set scope parameters
  >   status               Show current state
  >   back                 Go to previous action
  >   help                 Show all commands
  >   exit                 Quit
  ```

---

### 📝 User --> Request Status [mock]**

**Acceptance Criteria:**
- **When** user enters `status`, **then** CLI displays current state:
  ```
  < status
  > CURRENT: story_bot.shape.build
  > Working Directory: C:\dev\my-project
  > [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render
  ```

---

### 📝 User --> Enter Action [mock]**

```
< run
> EXECUTING shape.clarify...
> [mock response - not executing real action]
> {"status": "success", "action": "clarify", "data": {...}}
```

**Acceptance Criteria:**
- **When** user enters `run`, **then** CLI displays "EXECUTING {behavior}.{action}..."
- **When** action executes (mock), **then** CLI returns mock response with status and data
- **When** action completes, **then** CLI displays success status in JSON format

---

### 📝 CLI --> Prompt For Basic Parameters [mock]

**Acceptance Criteria:**
- **When** user runs `shape.clarify` without parameters, **then** CLI prompts for clarification parameters:
  ```
  < run
  > MISSING PARAMETERS for shape.clarify
  > 
  > Required:
  >   key_questions_answered: Dict mapping question keys to answer strings
  >   evidence_provided: Dict mapping evidence types to evidence content
  > 
  > Please provide parameters:
  < clarify.key_questions.q1="What is scope?" clarify.evidence.e1="Requirements doc"
  > OK received 1 key question, 1 evidence
  ```

- **When** user runs `shape.strategy` without parameters, **then** CLI prompts for strategy parameters:
  ```
  < run
  > MISSING PARAMETERS for shape.strategy
  > 
  > Required:
  >   decisions_made: Dict mapping decision criteria keys to selected options
  >   assumptions_made: List of assumption strings
  > 
  > Please provide parameters:
  < strategy.decisions.d1="Use REST API" strategy.assumptions="Single user per session"
  > OK received 1 decision, 1 assumption
  ```

---

### 📝 CLI --> Prompt For Story Scope Parameters [mock]

**Acceptance Criteria:**
- **When** user runs `shape.build` without scope, **then** CLI prompts for story scope:
  ```
  < run
  > MISSING PARAMETERS for shape.build
  > 
  > Required:
  >   scope: Story scope (epic, story, increment, or all)
  > 
  > Enter scope (e.g., scope.type=epic scope.value="Epic Name"):
  < scope.type=epic scope.value="Manage Mobs"
  > OK scope set to epic: Manage Mobs
  ```

- **When** user runs `shape.validate` without scope, **then** CLI prompts for story scope:
  ```
  < run
  > MISSING PARAMETERS for shape.validate
  > 
  > Required:
  >   scope: Story scope (epic, story, increment, or all)
  > 
  > Use scope=all? (y/n/specify):
  < n
  > Enter scope (e.g., scope.type=story scope.value="Story Name"):
  < scope.type=story scope.value="Create Mob","Edit Mob"
  > OK scope set to stories: Create Mob, Edit Mob
  ```

---

### 📝 CLI --> Prompt For File Scope Parameters [mock]

**Acceptance Criteria:**
- **When** user runs `code.validate` without scope, **then** CLI prompts for file scope:
  ```
  < run
  > MISSING PARAMETERS for code.validate
  > 
  > Required:
  >   scope: File scope (files with optional exclude patterns)
  > 
  > Enter file scope (e.g., scope.type=files scope.value=src/ scope.exclude=*.test.py):
  < scope.type=files scope.value=src/,tests/
  > OK scope set to files: src/, tests/
  ```

- **When** user runs `code.validate` with files but wants exclusions, **then** CLI allows adding exclusions:
  ```
  < run
  > MISSING PARAMETERS for code.validate
  > 
  > Required:
  >   scope: File scope (files with optional exclude patterns)
  > 
  > Enter file scope:
  < scope.type=files scope.value=agile_bot/bots/ scope.exclude=*.bak,*.tmp,__pycache__
  > OK scope set to files: agile_bot/bots/ (excluding: *.bak, *.tmp, __pycache__)
  ```
- **When** parameters are listed, **then** CLI prompts user to provide parameters

---

### 📝 CLI --> Display Confirm and Continue Prompt [mock]**

```
> EXECUTED shape.clarify
> 
> Results:
>   - Answered 7 key questions
>   - Provided 3 evidence types
>   - Saved to clarification.json
> 
> Continue to next action (strategy)? (y/n/review)
```

**Acceptance Criteria:**
- **When** action completes execution, **then** CLI displays "EXECUTED {behavior}.{action}"
- **When** results are available, **then** CLI displays summary of results
- **When** results are displayed, **then** CLI prompts "Continue to next action ({next})? (y/n/review)"

---

### 📝 User --> Enters Confirm Results [mock]**

```
< y
> OK advancing to strategy
> CURRENT: story_bot.shape.strategy
> [shape] clarify [OK] -> strategy* -> build -> validate -> render
```

**Acceptance Criteria:**
- **When** user enters `y` at confirm prompt, **then** CLI displays "OK advancing to {next_action}"
- **When** user confirms, **then** CLI advances to next action in workflow
- **When** action advances, **then** CLI updates breadcrumbs to show new current action

---

### 📝 CLI --> Advance To Next Action [mock]**

Automatically moves to next action in workflow after confirm.

**Acceptance Criteria:**
- **When** user confirms action completion, **then** CLI moves to next action in behavior workflow
- **When** advancing to next action, **then** CLI marks previous action as [OK] in breadcrumbs
- **When** workflow advances, **then** CLI updates current action indicator `*` to new position

---

### 📝 CLI --> Loop Back To Display State [mock]**

After each action completes, returns to displaying current state and waiting for next command.

**Acceptance Criteria:**
- **When** action completes and advances, **then** CLI returns to displaying current state
- **When** state is redisplayed, **then** CLI shows updated breadcrumbs with new position
- **When** waiting for command, **then** CLI displays command prompt and waits for user input

---

### 📝 User --> Exit REPL**

```
< exit
> Goodbye!
```

**Acceptance Criteria:**
- **When** user enters `exit`, **then** CLI displays "Goodbye!"
- **When** exit command is processed, **then** CLI terminates REPL loop
- **When** CLI exits, **then** process returns to shell


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

| Command              | Description                                   |
|----------------------|-----------------------------------------------|
| workspace <path>     | Set working directory                         |
| behavior <name>      | Switch to behavior                            |
| action <name>        | Jump to action within current behavior        |
| scope.<key>=<val>    | Set scope parameter                           |
| run                  | Execute current action                        |
| back                 | Go to previous action                         |
| status               | Show current state and scope                  |
| reset [scope]        | Clear accumulated state or just scope         |
| help                 | Show available commands                       |
| exit                 | Quit the REPL                                 |

**Responses:**

| Response             | Meaning                                       |
|----------------------|-----------------------------------------------|
| FRESH                | No existing state, need workspace             |
| CURRENT: <path>      | Current behavior.action position              |
| OK <detail>          | Command accepted                              |
| ERROR: <message>     | Command failed                                |
| EXECUTING <action>   | Action running                                |
| COMPLETE             | Behavior workflow finished                    |
| GOODBYE              | Session ended                                 |

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

| Layer         | Interface                              | Who Uses It    | Complexity |
|---------------|----------------------------------------|----------------|------------|
| Flags         | --behavior, --action, --skip-cross-file | Everyone       | Low        |
| Dot-notation  | scope.type=epic scope.value=X          | Humans & AI    | Medium     |
| STDIO         | Line-based conversation                | AI, Automation | High       |
| Interactive   | Prompts when info missing              | Humans         | Zero       |
| Config file   | --config-file advanced.json            | Power users    | Optional   |

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

| File                           | Purpose                              |
|--------------------------------|--------------------------------------|
| cli/stdio_handler.py           | STDIO mode handler                   |
| cli/dot_notation_parser.py     | Dot-notation parsing                 |
| cli/interactive_prompt.py      | Interactive prompting                |
| cli/input_normalizer.py        | Merge all input sources              |

### Modified Files

| File                           | Changes                              |
|--------------------------------|--------------------------------------|
| cli/base_bot_cli.py            | Add --stdio routing, prompt flow     |
| cli/cli_parameter_parser.py    | Integrate dot-notation               |
| cli/cli_context_builder.py     | Accept normalized config             |

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

