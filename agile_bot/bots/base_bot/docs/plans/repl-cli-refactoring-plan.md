# REPL CLI Refactoring Plan

**Date:** 2025-12-26  
**Status:** PLANNED  
**Goal:** Refactor REPL CLI to fix code violations and follow clean architecture patterns

---


## Current CLI Output Format (Observed)

Based on testing with `demo/mob_minion`, the actual CLI output has these components:

### Standard Output Pattern
All commands follow this structure:

```
============================================================
STORY_BOT CLI

============================================================
AI AGENT INSTRUCTIONS - PIPED MODE
============================================================
[Piped mode instructions - always present in pipe mode]

------------------------------------------------------------
Bot Path: C:\dev\augmented-teams\agile_bot\bots\story_bot
Work Path: demo\mob_minion
------------------------------------------------------------
[Command-specific output here]

[Optional: Separators for instruction execution]

------------------------------------------------------------
STORY_BOT CLI
*** PIPED MODE DETECTED ***
Bot Path: C:\dev\augmented-teams\agile_bot\bots\story_bot
Work Path: demo\mob_minion
Progress: shape.clarify.instructions
[Optional: Scope Filter display if scope is set]
------------------------------------------------------------
[Status tree with [x], [*], [ ] checkboxes]
------------------------------------------------------------
Commands: status | back | current | next | path [dir] | scope [filter] | help | exit
run echo '[command]' | python repl_main.py to invoke commands
```

### Navigation Output
```
Now at: shape.clarify

Run: echo 'instructions' | python repl_main.py to see instructions for this action.

------------------------------------------------------------
[CLI display at bottom with Progress breadcrumb]
```

### Instruction Execution Output
```
=================================
Executing: shape.clarify.instructions

[Behavior description]
[Action description]
[Instruction content]

--------------------------------------------------------------------------------
[CLI display at bottom with Progress breadcrumb]
```

### Command-Specific Outputs
- **scope**: `Scope Filter: "Story1, Story2"` with validation results
- **path**: `Current path: demo\mob_minion`
- **help**: Full command list and examples
- **status**: Shows status tree
- **Navigation commands** (next, back): Shows "Now at: X" message

---

# Story Graph Refactoring

This refactoring updates the "Run Interactive REPL" epic structure to better reflect the CLI Domain Model architecture and user journeys.

## New Epic Structure

```
Run Interactive REPL
  
  Initialize REPL Session
    Launch CLI in Interactive Mode
    Launch CLI in Pipe Mode (for AI/automation)
    Display Piped Mode Instructions for AI Agents
    Display Bot Status in CLI on Launch  --> PLEASE SEE Display Bot State Using CLI
    Detect and Configure TTY/Non-TTY Input for CLI
    Load and Display Workspace Context in CLI
  
  Navigate Bot Behaviors and Actions With CLI
    Navigate Using CLI Dot Notation (shape.build.instructions, discovery.validate)
    Navigate Sequentially Using CLI Commands (next, back, current)
    Exit CLI REPL
  
  Execute Action Operation Through CLI
    Get Action Instructions Through CLI
    Submit Work Through CLI with String Parameters
    Confirm Action Completion Through CLI
    Re-execute Current Operation Using CLI
    Handle Operation Errors and Validation in CLI
  
  Manage Bot Scope Through CLI
    Set Scope Through CLI Using String Parameters
      [Scenario: Set scope with node names - uses KnowledgeGraphFilter]
      [Scenario: Set scope with file paths - uses FileFilter]
      [Scenario: Set scope to 'all' - uses KnowledgeGraphFilter]
    View Current Scope in CLI (type, value, rendered content)
    Clear Scope Through CLI
    Pass Scope Parameters When Executing Actions Through CLI
      [Scenario: Execute build instructions with node names as scope parameter]
      [Scenario: Execute validate instructions with file paths as scope parameter]
    Validate Scope Against Story Graph in CLI
  
  Display Bot State Using CLI
    Display CLI Header (bot name, paths, progress breadcrumb)
    Display Bot Hierarchy Tree with Progress Indicators
      [Shows all behaviors with [x], [*], [ ] status]
      [Shows current behavior's actions with status]
      [Shows current action's operations with status and parameters]
      [Uses tree/outline indentation]
    Display CLI Navigation Menu Footer (status, back, current, next, help, exit)
  
  Get Help Using CLI
    Request Action Help Through CLI
    View Parameter Documentation in CLI
    View Command Examples in CLI
```

---

## Scenario Development

**Background (Common Setup for all REPL scenarios):**

```gherkin
Background:
  Given Bot is story_bot at path 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
  And Bot has 9 behaviors: shape, domain, prioritization, discovery, design, exploration, scenarios, tests, code
  And Behaviors shape, domain, prioritization, discovery, exploration, scenarios have actions: clarify, strategy, build, validate, render
  And Behavior design has actions: clarify, strategy, build, validate, render, rules
  And Behavior tests has actions: build, render, validate, rules
  And Behavior code has actions: strategy, render, validate, rules
  And Workspace is at 'C:\dev\augmented-teams\demo\minion_test'
```

---

## Initialize REPL Session

### Story: Launch CLI in Interactive Mode

**Scenario: CLI launches in interactive mode**
```gherkin
Given REPLSession is configured for interactive mode
When user runs 'python repl_main.py --stdio'
Then REPLSession creates CLIBot wrapping Bot
And CLI displays header with bot name 'STORY_BOT CLI'
And CLI displays bot path 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
And CLI displays workspace path 'C:\dev\augmented-teams\demo\minion_test'
And CLI displays current position 'shape.clarify.instructions'
And CLI displays bot hierarchy tree with [x], [*], [ ] indicators
And CLI displays navigation menu footer 'status | back | current | next | help | exit'
And CLI waits for user input with prompt '[story_bot] >'
```

**Scenario: CLI loads existing behavior action state on launch**
```gherkin
Given REPLSession is configured for interactive mode
And behavior action state file exists with current_behavior='discovery' current_action='build' operation='instructions'
When user runs 'python repl_main.py --stdio'
Then REPLSession loads stored behavior action state
And CLI displays current position 'discovery.build.instructions'
And bot hierarchy shows discovery behavior with [*] indicator
And bot hierarchy shows build action with [*] indicator
And bot hierarchy shows instructions operation with [*] indicator
```

---

### Story: Launch CLI in Pipe Mode

**Scenario: CLI launches in pipe mode**
```gherkin
Given REPLSession is configured for pipe mode
When commands are piped: echo 'shape.build.instructions' | python repl_main.py --stdio
Then REPLSession creates CLIBot wrapping Bot
And CLI displays warning 'WARNING: Pipe mode detected - AI should not run REPL in interactive mode'
And CLI reads command without displaying '[story_bot] >' prompt
And CLI executes shape.build.instructions
And CLI displays 'EXECUTING shape.build.instructions'
And CLI returns instructions output
And CLI exits silently without 'Exiting REPL...' message
```

**Scenario Outline: CLI processes multiple piped commands in sequence**
```gherkin
Given REPLSession is configured for pipe mode
And behavior action state starts at shape.clarify.instructions
When commands are piped: <commands>
Then CLI executes all commands in single session
And behavior action state advances to <final_position>
And CLI exits after processing all commands

Examples:
| commands | final_position |
| 'shape.clarify.instructions\nshape.strategy.instructions\nshape.build.instructions' | shape.build.instructions |
| 'next\nnext\nnext' | shape.validate.instructions |
| 'discovery.build.instructions\nsubmit' | discovery.build.submit |
```

---

### Story: Display Piped Mode Instructions for AI Agents

**Scenario: CLI displays piped mode instructions in pipe mode**
```gherkin
Given REPLSession detects piped input (TTYDetector.is_interactive() == False)
When CLI initializes
Then CLI displays piped mode instructions header:
  """
  ============================================================
  AI AGENT INSTRUCTIONS - PIPED MODE
  ============================================================
  
  *** THIS REPL WILL EXIT AFTER PROCESSING YOUR COMMAND ***
  This is NORMAL and EXPECTED behavior in piped mode.
  
  [PowerShell command examples]
  [What works / what doesn't work]
  [Piped mode workflow]
  [Critical rules]
  """
And piped mode instructions appear before every command output
```

**Scenario: CLI omits piped mode instructions in interactive mode**
```gherkin
Given REPLSession detects interactive TTY (TTYDetector.is_interactive() == True)
When CLI initializes
Then CLI does not display piped mode instructions
And CLI displays normal prompt '[story_bot] >'
```

---

### Story: Detect and Configure TTY/Non-TTY Input for CLI

**Scenario: TTYDetector identifies interactive terminal**
```gherkin
Given stdin is connected to a TTY terminal
When TTYDetector.is_interactive() is called
Then TTYDetector returns True
And REPLSession configures for interactive mode
And CLI enables command prompts
And CLI enables colored output
And CLI enables progress indicators
```

**Scenario: TTYDetector identifies piped input**
```gherkin
Given stdin is piped from another process
When TTYDetector.is_interactive() is called
Then TTYDetector returns False
And REPLSession configures for pipe mode
And CLI disables command prompts
And CLI disables colored output
And CLI displays warning about pipe mode
```

---

### Story: Load and Display Workspace Context in CLI

**Scenario: CLI loads and displays workspace context**
```gherkin
Given Bot has workspace path 'C:\dev\augmented-teams\demo\minion_test'
And workspace contains story-graph.json
When REPLSession initializes CLIBot
Then CLIBot loads workspace context from bot paths
And WorkspaceDisplay shows workspace path
And WorkspaceDisplay shows story graph location
And CLI displays:
  """
  ==========================================
  Work Path: C:\dev\augmented-teams\demo\minion_test
  Story Graph: C:\dev\augmented-teams\demo\minion_test\docs\stories\story-graph.json
  ==========================================
  """
```

---

## Navigate Bot Behaviors and Actions With CLI

### Story: Navigate Using CLI Dot Notation

**Scenario Outline: User navigates with behavior only (no dots)**
```gherkin
Given CLI is at shape.clarify.instructions
When user enters '<behavior>'
Then CommandParser parses behavior='<behavior>'
And CLIBot navigates to behavior '<behavior>'
And CLIBehavior defaults to first action 'clarify'
And CLIAction defaults to operation 'instructions'
And CLI displays 'EXECUTING <behavior>.clarify.instructions'
And behavior action state updates to '<behavior>.clarify.instructions'

Examples:
| behavior |
| discovery |
| code |
| scenarios |
```

**Scenario Outline: User navigates with behavior.action (one dot)**
```gherkin
Given CLI is at shape.clarify.instructions
When user enters '<behavior>.<action>'
Then CommandParser parses behavior='<behavior>' action='<action>'
And CLIBot navigates to behavior '<behavior>'
And CLIBehavior navigates to action '<action>'
And CLIAction defaults to operation 'instructions'
And CLI displays 'EXECUTING <behavior>.<action>.instructions'
And behavior action state updates to '<behavior>.<action>.instructions'

Examples:
| behavior | action |
| discovery | build |
| code | validate |
| scenarios | render |
```

**Scenario Outline: User navigates with behavior.action.operation (two dots)**
```gherkin
Given CLI is at shape.clarify.instructions
When user enters '<dot_notation>'
Then CommandParser parses behavior='<behavior>' action='<action>' operation='<operation>'
And CLIBot navigates to behavior '<behavior>'
And CLIBehavior navigates to action '<action>'
And CLIAction executes operation '<operation>'
And CLI displays 'EXECUTING <behavior>.<action>.<operation>'
And behavior action state updates to '<behavior>.<action>.<operation>'

Examples:
| dot_notation | behavior | action | operation |
| discovery.build.instructions | discovery | build | instructions |
| code.validate.submit | code | validate | submit |
| scenarios.render.confirm | scenarios | render | confirm |
```

**Scenario: User enters invalid behavior in dot notation**
```gherkin
Given CLI is at shape.clarify.instructions
When user enters 'invalid_behavior.build.instructions'
Then CommandParser attempts to parse 'invalid_behavior'
And CLIBehaviors.navigate_to('invalid_behavior') fails
And CLI displays 'ERROR: Behavior 'invalid_behavior' not found'
And CLI displays 'Available behaviors: shape, prioritization, discovery, exploration, scenarios, tests, code'
And behavior action state remains at shape.clarify.instructions
```

---

### Story: Navigate Sequentially Using CLI Commands

**Scenario Outline: User navigates with next command**
```gherkin
Given CLI is at <current_position>
When user enters 'next'
Then CLIBehaviors.current.actions.next returns <next_action>
And CLI navigates to <next_position>
And CLI executes instructions at <next_position>
And CLI displays bot hierarchy with updated [*] indicator

Examples:
| current_position | next_action | next_position |
| shape.clarify.instructions | strategy | shape.strategy.instructions |
| shape.render.instructions | None (crosses to next behavior) | prioritization.clarify.instructions |
| code.render.instructions | None (last action of last behavior) | code.render.instructions |
```

**Scenario Outline: User navigates with back command**
```gherkin
Given CLI is at <current_position>
When user enters 'back'
Then CLIBehaviors.current.actions.previous returns <previous_action>
And CLI navigates to <previous_position>
And CLI executes operation at <previous_position>

Examples:
| current_position | previous_action | previous_position |
| shape.strategy.instructions | clarify | shape.clarify.instructions |
| prioritization.clarify.instructions | None (crosses to previous behavior) | shape.render.confirm |
| shape.clarify.instructions | None (first action of first behavior) | shape.clarify.instructions |
```

---

### Story: Exit CLI REPL

**Scenario: User exits REPL with exit command**
```gherkin
Given CLI is running in interactive mode
And CLI is at discovery.build.instructions
When user enters 'exit'
Then REPLSession saves current behavior action state
And CLI displays 'Exiting REPL...'
And CLI terminates REPL loop
And Process exits with code 0
```

**Scenario: User exits REPL with Ctrl+C**
```gherkin
Given CLI is running in interactive mode
When user presses Ctrl+C
Then REPLSession handles KeyboardInterrupt
And REPLSession saves current behavior action state
And CLI displays 'Exiting REPL...'
And CLI terminates gracefully
```

---

## Execute Action Operation Through CLI

### Story: Get Action Instructions Through CLI

**Scenario: User gets instructions for build action without scope**
```gherkin
Given CLI is at shape.build.instructions
When user enters 'shape.build.instructions'
Then CLIAction calls _parse_args_to_context('')
And CLIAction creates empty BuildActionContext (no scope parameter)
And CLIAction calls action.get_instructions(context)
And domain BuildKnowledgeAction returns instructions dict with template, rules, scope='all'
And CLIAction calls _format_result(instructions_dict)
And CLI displays formatted instructions:
  """
  ==========================================
  [INSTRUCTIONS]
  Action: build
  Behavior: shape
  Template: docs/templates/story-map-template.md
  Rules: use_domain_language, shape_relationships_from_story_map
  Scope: all
  Build knowledge graph following template structure...
  ==========================================
  """
```

**Scenario: User gets instructions for build action with scope**
```gherkin
Given CLI is at shape.build.instructions
When user enters 'shape.build.instructions scope="Story1, Story2"'
Then CLIAction calls _parse_args('scope="Story1, Story2"')
And CLIAction uses CLIScope to parse scope string
And CLIScope._parse_scope_string('scope="Story1, Story2"') returns Scope(type=inferred, value=['Story1', 'Story2'])
And CLIAction creates BuildActionContext with parsed scope
And Scope.__post_init__ injects KnowledgeGraphFilter (type is not FILES)
And CLIAction calls action.get_instructions(context)
And domain BuildKnowledgeAction returns filtered instructions for Story1, Story2
And CLIAction calls _format_result(instructions_dict)
And CLI displays formatted instructions:
  """
  ==========================================
  [INSTRUCTIONS]
  Action: build
  Behavior: shape
  Scope: Story1, Story2
  Template: docs/templates/story-map-template.md
  Rules: use_domain_language, shape_relationships_from_story_map
  Build knowledge graph for Story1 and Story2...
  ==========================================
  """
```

---

### Story: Submit Work Through CLI with String Parameters

**Scenario: User submits build work**
```gherkin
Given CLI is at shape.build.instructions
And user has created knowledge graph content
When user enters 'submit'
Then CLIAction calls _parse_args('')
And CLIAction creates BuildActionContext with no scope
And CLIAction calls action.submit(context)
And domain BuildKnowledgeAction saves knowledge graph
And domain action returns confirmation dict: saved_to='story-graph.json', mode='update', items_added=5
And CLIAction calls _format_result(confirmation_dict)
And CLI displays:
  """
  ==========================================
  [SUBMITTED]
  Saved to: story-graph.json
  Mode: update
  Items added: 5
  ==========================================
  """
```

**Scenario: User submits with clarify parameters**
```gherkin
Given CLI is at shape.clarify.instructions
And user has gathered clarification context
When user enters 'submit answers="q1=answer1, q2=answer2"'
Then CLIAction calls _parse_args('answers="q1=answer1, q2=answer2"')
And CLIAction creates ClarifyActionContext with answers
And CLIAction calls action.submit(context)
And domain action saves clarification responses
And CLI displays confirmation
```

**Scenario: User submits with strategy parameters**
```gherkin
Given CLI is at shape.strategy.instructions
And user has made strategic decisions
When user enters 'submit choice1=value1 assumptions="assumption text"'
Then CLIAction calls _parse_args('choice1=value1 assumptions="assumption text"')
And CLIAction creates StrategyActionContext with choices and assumptions
And CLIAction calls action.submit(context)
And domain action saves strategic decisions
And CLI displays confirmation
```

---

### Story: Confirm Action Completion Through CLI

**Scenario: User confirms build action completion**
```gherkin
Given CLI is at shape.build.submit
And user has submitted build work
When user enters 'confirm'
Then CLIAction calls action.confirm()
And domain action marks build as complete
And domain action updates behavior action state
And CLI displays:
  """
  ==========================================
  [CONFIRMED]
  Action: shape.build
  Status: complete
  Next: shape.validate.instructions
  ==========================================
  """
And CLI automatically navigates to shape.validate.instructions
```

**Scenario: User confirms without prior submit**
```gherkin
Given CLI is at shape.build.instructions
And no submit has been executed
When user enters 'confirm'
Then CLIAction detects no pending work to confirm
And CLI displays:
  """
  ==========================================
  [ERROR]
  Nothing to confirm
  Submit work first with: submit
  ==========================================
  """
And CLI remains at shape.build.instructions
```

---

### Story: Re-execute Current Operation Using CLI

**Scenario: User re-executes current instructions**
```gherkin
Given CLI is at discovery.build.instructions
And user previously executed instructions
When user enters 'current'
Then CLI re-executes discovery.build.instructions
And CLI displays 'EXECUTING discovery.build.instructions'
And CLI displays fresh instructions output
And behavior action state remains at discovery.build.instructions
```

**Scenario: User re-executes current submit**
```gherkin
Given CLI is at shape.build.submit
And user previously submitted build work
When user enters 'current'
Then CLI re-executes submit with same context
And CLI displays 'EXECUTING shape.build.submit'
And domain action re-processes submission
And CLI displays updated confirmation
```

---

## Manage Bot Scope Through CLI

### Story: Set Scope Through CLI Using String Parameters

**Scenario: User sets scope with node names (knowledge graph filter)**
```gherkin
Given CLI session has no stored scope
When user enters 'scope="Story1, Story2"'
Then CLIScope.filter setter is called with 'scope="Story1, Story2"'
And CLIScope._parse_scope_string() detects scope type from input format (no 'files:' prefix)
And CLIScope creates Scope(type=inferred, value=['Story1', 'Story2'], exclude=[], skiprule=[])
And Scope.__post_init__ injects KnowledgeGraphFilter
And REPLSession stores scope in session.stored_scope
And CLI displays 'Scope set to: Story1, Story2'
```

**Scenario: User sets scope with file paths (file filter)**
```gherkin
Given CLI session has no stored scope
When user enters 'scope="files:src/**, exclude:*.bak, exclude:__pycache__"'
Then CLIScope.filter setter is called with 'scope="files:src/**, exclude:*.bak, exclude:__pycache__"'
And CLIScope._parse_scope_string() detects 'files:' prefix
And CLIScope creates Scope(type=FILES, value=['src/**'], exclude=['*.bak', '__pycache__'], skiprule=[])
And Scope.__post_init__ injects FileFilter
And REPLSession stores scope in session.stored_scope
And CLI displays 'Scope set to: files matching src/** (excluding *.bak, __pycache__)'
```

---

### Story: Pass Scope Parameters When Executing Actions Through CLI

**Scenario: User passes scope with build instructions**
```gherkin
Given CLI is at shape.build.instructions
When user enters 'shape.build.instructions scope="Epic1, Epic2"'
Then CLIAction._parse_args('scope="Epic1, Epic2"') is called
And CLIAction uses CLIScope to parse scope
And CLIScope creates Scope(type=inferred, value=['Epic1', 'Epic2'])
And Scope injects KnowledgeGraphFilter
And CLIAction creates BuildActionContext(scope=<scope_object>)
And CLIAction calls action.get_instructions(context)
And domain action receives context with scope filter
And domain action returns instructions filtered to Epic1, Epic2
And CLI displays instructions:
  """
  ==========================================
  [INSTRUCTIONS]
  Action: build
  Behavior: shape
  Scope: Epic1, Epic2
  Stories in scope: 15 stories across 2 epics
  Build knowledge graph for Epic1 and Epic2...
  ==========================================
  """
```

**Scenario: User passes scope with validate instructions**
```gherkin
Given CLI is at code.validate.instructions
When user enters 'code.validate.instructions scope="files:src/repl_cli/**, exclude:test_*.py"'
Then CLIAction._parse_args parses scope parameter
And CLIAction uses CLIScope to parse scope
And CLIScope creates Scope(type=FILES, value=['src/repl_cli/**'], exclude=['test_*.py'])
And Scope injects FileFilter
And CLIAction creates ValidateActionContext(scope=<scope_object>)
And CLIAction calls action.get_instructions(context)
And domain action uses FileFilter to filter files list
And domain action returns instructions for 23 files in src/repl_cli/ (excluding tests)
And CLI displays:
  """
  ==========================================
  [INSTRUCTIONS]
  Action: validate
  Behavior: code
  Scope: files in src/repl_cli/** (excluding test_*.py)
  Files to validate: 23 files
  Validate code quality for specified files...
  ==========================================
  """
```

---

### Story: View Current Scope in CLI

**Scenario: User views active scope with node names**
```gherkin
Given CLI session has stored scope with type='STORY' value=['Story1', 'Story2']
When user enters 'scope'
Then CLIScope validates scope against story graph
And CLI displays:
  """
  Scope Filter: "Story1, Story2"
    - Story1 ✓
    - Story2 ✓
  """
And CLI displays standard status at bottom
```

**Scenario: User views active scope with invalid node names**
```gherkin
Given CLI session has stored scope with value=['ValidStory', 'InvalidStory']
And story graph contains ValidStory but not InvalidStory
When user enters 'scope'
Then CLIScope validates scope against story graph
And CLI displays:
  """
  Scope Filter: "ValidStory, InvalidStory"
    - ValidStory ✓
    - InvalidStory (no match)
  """
And CLI displays standard status at bottom
```

**Scenario: User views active scope with file paths**
```gherkin
Given CLI session has stored scope with type='FILES' value=['src/**'] exclude=['*.bak']
When user enters 'scope'
Then CLI displays:
  """
  Scope Filter: "files:src/**, exclude:*.bak"
  Type: files
  Filter: FileFilter
  """
And CLI displays standard status at bottom
```

**Scenario: User views scope when none is set**
```gherkin
Given CLI session has no stored scope
When user enters 'scope'
Then CLI displays:
  """
  No scope set
  """
And CLI displays standard status at bottom
```

---

### Story: Clear Scope Through CLI

**Scenario: User clears active scope**
```gherkin
Given CLI session has stored scope with value=['Story1', 'Story2']
When user enters 'scope clear'
Then CLIScope.filter setter receives 'clear'
And REPLSession sets stored_scope to None
And CLI displays 'Scope cleared: filtering on all content'
```

**Scenario: User sets scope to 'all' (same as clear)**
```gherkin
Given CLI session has stored scope with value=['Epic1']
When user enters 'scope all'
Then CLIScope.filter setter receives 'all'
And REPLSession sets stored_scope to None
And CLI displays 'Scope set to: all'
```

---

### Story: Validate Scope Against Story Graph in CLI

**Scenario: User validates scope with valid node names**
```gherkin
Given CLI session has scope="Story1, Story2"
And story graph contains Story1 and Story2
When user enters 'scope validate'
Then ScopeValidator checks scope against loaded story graph
And Validator finds Story1 in graph
And Validator finds Story2 in graph
And CLI displays:
  """
  ==========================================
  [SCOPE VALIDATION]
  Valid: Story1 ✓
  Valid: Story2 ✓
  Scope is valid: 2/2 nodes found
  ==========================================
  """
```

**Scenario: User validates scope with invalid node names**
```gherkin
Given CLI session has scope="Story1, NonExistentStory"
And story graph contains Story1 but not NonExistentStory
When user enters 'scope validate'
Then ScopeValidator checks scope against story graph
And Validator finds Story1
And Validator fails to find NonExistentStory
And CLI displays:
  """
  ==========================================
  [SCOPE VALIDATION]
  Valid: Story1 ✓
  Invalid: NonExistentStory ✗ (not found in story graph)
  Scope has errors: 1/2 nodes found
  ==========================================
  """
```

---

## Display Bot State Using CLI

### Story: Display CLI Header

**Scenario: CLI displays header components**
```gherkin
Given CLIBot is initialized with Bot
And REPLSession has created StatusDisplay
When StatusDisplay.render() is called
Then HeaderDisplay.render(cli_bot) is called
And HeaderDisplay shows bot name: 'STORY_BOT CLI'
And HeaderDisplay shows bot path: 'C:\dev\augmented-teams\agile_bot\bots\story_bot'
And HeaderDisplay shows workspace path: 'C:\dev\augmented-teams\agile_bot\bots\base_bot'
And HeaderDisplay shows breadcrumb: 'Progress: shape.build.instructions'
And CLI displays:
  """
  ==========================================
  STORY_BOT CLI
  Bot Path: C:\dev\augmented-teams\agile_bot\bots\story_bot
  Work Path: C:\dev\augmented-teams\agile_bot\bots\base_bot
  Progress: shape.build.instructions
  ==========================================
  """
```

---

### Story: Display Bot Hierarchy Tree with Progress Indicators

**Scenario: CLI displays complete bot hierarchy**
```gherkin
Given CLI is at discovery.build.instructions
And shape behavior is complete (all actions done)
And prioritization behavior is complete
And discovery behavior is at build action
When HierarchyTreeDisplay.render(cli_bot) is called
Then BreadcrumbVisitor traverses cli_bot.behaviors
And Visitor visits each behavior and action
And Visitor builds hierarchy with progress indicators
And CLI displays:
  """
  [x] shape - Shape story map and high-level domain model
      [x] clarify
      [x] strategy
      [x] build
      [x] validate
      [x] render
  [x] prioritization - Organize stories into delivery increments
  [*] discovery - Elaborate stories with detailed flows and rules
      [x] clarify
      [x] strategy
      [*] build
          [*] instructions --scope="..."
          [ ] submit --knowledge_graph={...}
          [ ] confirm
      [ ] validate
      [ ] render
  [ ] exploration
  [ ] scenarios
  [ ] tests
  [ ] code
  
  Legend: [*] current  [x] done  [ ] not started
  """
```

---

### Story: Display CLI Navigation Menu Footer

**Scenario: CLI displays navigation menu footer**
```gherkin
Given CLI is in interactive mode
When FooterDisplay.render() is called
Then FooterDisplay shows available commands
And CLI displays:
  """
  ==========================================
  Commands: status | back | current | next | help | exit
  ==========================================
  """
```

**Scenario: Footer updates based on navigation context**
```gherkin
Given CLI is at shape.clarify.instructions (first action)
When FooterDisplay.render() is called
Then FooterDisplay shows 'back' as disabled
And FooterDisplay shows 'next' as enabled
And CLI displays:
  """
  Commands: status | back[disabled] | current | next | help | exit
  """
```

---

## Get Help Using CLI

### Story: Request Action Help Through CLI

**Scenario: User requests help for current action**
```gherkin
Given CLI is at shape.build.instructions
When user enters 'help'
Then CLI retrieves action help from CLIAction
And CLI displays action description
And CLI displays available operations (instructions, submit, confirm)
And CLI displays parameters with types and descriptions
And CLI displays:
  """
  ==========================================
  [HELP: shape.build]
  Description: Build knowledge graph from user context
  Operations:
    instructions  - Get instructions for building knowledge graph
    submit        - Submit built knowledge graph
    confirm       - Confirm build completion
  Parameters:
    --scope       string    Filter to specific stories/epics/files
    --exclude     string    Exclude specific items from scope
    --skiprule    string    Skip specific validation rules
  Examples:
    shape.build.instructions
    shape.build.instructions scope="Story1, Story2"
    shape.build.submit
    shape.build.confirm
  ==========================================
  """
```

**Scenario: User requests help for specific behavior**
```gherkin
Given CLI is at any position
When user enters 'help discovery'
Then CLI retrieves behavior help from CLIBehavior
And CLI displays behavior description
And CLI lists all actions in behavior
And CLI displays:
  """
  ==========================================
  [HELP: discovery behavior]
  Description: Elaborate stories with detailed flows and rules
  Actions:
    clarify   - Gather context for discovery
    strategy  - Make strategic decisions
    build     - Build detailed story specifications
    validate  - Validate story specifications
    render    - Render story documents
  Current position: discovery.build.instructions
  ==========================================
  """
```

---

### Story: View Parameter Documentation in CLI

**Scenario: User views scope parameter documentation**
```gherkin
Given CLI is at any position
When user enters 'help --scope'
Then CLI displays scope parameter documentation
And CLI displays:
  """
  ==========================================
  [PARAMETER: --scope]
  Type: string
  Description: Filter operations to specific stories, epics, increments, or files
  Formats:
    Node names:  scope="Story1, Story2"
    Epic:        scope="epic:Epic Name"
    Increment:   scope="increment:1,2"
    Files:       scope="files:src/**, exclude:*.bak"
    All:         scope="all"
  Used by actions: build, validate, render
  Examples:
    shape.build.instructions scope="Story1, Story2"
    code.validate.instructions scope="files:src/**"
  ==========================================
  """
```

---

### Story: View Command Examples in CLI

**Scenario: User views navigation command examples**
```gherkin
Given CLI is at any position
When user enters 'help examples navigation'
Then CLI displays navigation command examples
And CLI displays:
  """
  ==========================================
  [EXAMPLES: Navigation]
  Dot notation:
    shape.build.instructions
    discovery.validate.instructions scope="Story1"
    code.render.confirm
  Sequential navigation:
    next                    # Move to next action
    back                    # Move to previous action
    current                 # Re-execute current operation
  Direct navigation:
    shape                   # Navigate to shape behavior
    discovery.build         # Navigate to discovery.build action
  ==========================================
  """
```

**Scenario: User views scope command examples**
```gherkin
Given CLI is at any position
When user enters 'help examples scope'
Then CLI displays scope command examples
And CLI displays:
  """
  ==========================================
  [EXAMPLES: Scope]
  Set scope:
    scope="Story1, Story2"
    scope="epic:Manage Users"
    scope="files:src/**, exclude:test_*.py"
  View scope:
    scope                   # Show current scope
  Clear scope:
    scope clear             # Clear current scope
    scope all               # Set to all content
  Validate scope:
    scope validate          # Check scope against story graph
  Use with actions:
    shape.build.instructions scope="Story1"
    code.validate.instructions scope="files:src/**"
  ==========================================
  """
```

---

### Story: Handle Operation Errors and Validation in CLI

**Scenario: User enters invalid scope format with instructions**
```gherkin
Given CLI is at shape.build.instructions
When user enters 'shape.build.instructions scope="invalid{format}"'
Then CLIScope._parse_scope_string('scope="invalid{format}"') raises parsing error
And CLIAction catches parsing exception
And CLIAction formats error message
And CLI displays:
  """
  ==========================================
  [ERROR]
  Invalid scope format: 'invalid{format}'
  Valid formats:
  - Node names: "Story1, Story2"
  - Epic: "epic:Epic Name"
  - Files: "files:src/**, exclude:*.bak"
  - All: "all"
  ==========================================
  """
And behavior action state remains at shape.build.instructions
```

**Scenario: User enters invalid clarify parameters with submit**
```gherkin
Given CLI is at shape.clarify.instructions
When user enters 'submit answers="incomplete'
Then CLIAction._parse_args parses malformed string
And Parser fails to parse quoted string properly
And CLI displays:
  """
  ==========================================
  [ERROR]
  Invalid parameter format
  Expected: answers="q1=a1, q2=a2"
  ==========================================
  """
And behavior action state remains at shape.clarify.instructions
```


# Domain Model

This domain model represents the REPL CLI architecture using domain-driven design principles.

## Interactive REPL Session

Manages the interactive read-eval-print loop, routing user input to CLI operations. Common  displays including header, hierarchy, and footer.

```
REPLSession
    Reads input line: str
    Routes to CLI operation: str, CLIBot, CommandParser
    Displays output: str
    Loops until exit: bool
    Has CLI bot: CLIBot
    References command parser: CommandParser
    References TTY detector: TTYDetector

TTYDetector
    Detects interactive mode: bool
    Detects pipe mode: bool

CommandParser
    Parses dot notation: str, Behavior, Action, Operation
    Extracts arguments: str, Dict

StatusDisplay
    Renders bot status: CLIBot, str
    Has header: HeaderDisplay
    Has hierarchy tree: HierarchyTreeDisplay
    Has footer: FooterDisplay

HeaderDisplay
    Renders header: CLIBot, str
    Shows bot name: str
    Shows bot path: str
    Shows breadcrumb: str

HierarchyTreeDisplay
    Renders hierarchy: CLIBot, str
    Shows all behaviors: List[CLIBehavior], str
    Shows current actions: List[CLIAction], str
    Shows current operations: List[str], str
    Indicates progress: str, str
    References breadcrumb visitor: BreadcrumbVisitor

FooterDisplay
    Renders footer: str
    Shows navigation commands: List[str]

BreadcrumbVisitor
    Visits behavior: CLIBehavior, str
    Visits action: CLIAction, str
    Visits operation: str, str
    Builds breadcrumb: List[str], str
```
## CLI Bot

String-based wrappers for Bot and Behavior providing CLI interface.

```
CLIBot
    Get name: str
    Get path: str
    Get status: str, StatusDisplay
    Has behaviors: CLIBehaviors
    Has scope: CLIScope
    References domain bot: Bot

CLIBehaviors
    Get current behavior: CLIBehavior
    Get next behavior: CLIBehavior
    Get all names: List[str]
    Navigates to behavior: str, CLIBehavior
    Has many behaviors: CLIBehavior
    References domain behaviors: Behaviors

CLIBehavior
    Get name: str
    Get description: str
    Get status: str
    Has actions: CLIActions
    References domain behavior: Behavior
```
## CLI Actions
String-based wrappers for Bot and Behavior providing CLI interface to action operations.
CLIActions
    Get current action: CLIAction
    Get next action: CLIAction
    Get all names: List[str]
    Navigates to action: str, CLIAction
    Has many actions: CLIAction
    References domain actions: Actions

CLIAction
    Get name: str
    Get description: str
    Get parameters: str
    Get status: str
    Executes instructions: str, str
    Executes submit: str, str
    Executes confirm: str
    Parses arguments internally (subclass-specific)
    Formats results internally (subclass-specific)
    References domain action: Action

    
Scope (from actions/action_context.py)
    Get type: ScopeType
    Get value: List[str]
    Get exclusions: List[str]
    Filters knowledge graph: Dict, Dict
    Filters files: List[Path], List[Path]
    References knowledge graph filter: KnowledgeGraphFilter
    References file filter: FileFilter

KnowledgeGraphFilter
    Filters by node names: Dict, Dict
    Matches stories: Dict, List[str]
    Matches epics: Dict, List[str]

FileFilter
    Filters by file paths: List[Path], List[Path]
    Matches include patterns: List[Path], List[str]
    Excludes patterns: List[Path], List[str]

ActionContext (from actions/action_context.py)
    Base context for all actions

ScopeActionContext (from actions/action_context.py)
    Has scope: Scope
    Extends: ActionContext
``
## Object Flow

Demonstrates how objects collaborate through nested message passing to fulfill responsibilities.

### Example: Execute Instructions Operation

```
REPLSession
    output = REPLSession.run_repl_loop()
        ->True =  is_interactive()
            ->= TTYDetector.is_interactive()
        -> command: {behavior: "shape", action: "build", operation: "instructions"}  = CommandParser.parse_command(input_line: "shape.build.instructions")
            -> behavior_name: "shape" = CommandParser.extract_behavior(input_line: "shape.build.instructions")
            -> action_name: "build" = CommandParser.extract_action(input_line: "shape.build.instructions")
            -> operation_name: "instructions" = CommandParser.extract_operation(input_line: "shape.build.instructions")
            return command: {behavior: "shape", action: "build", operation: "instructions"}
        -> cli_behavior: <CLIBehavior wrapping shape> = CLIBot.behaviors.get_behavior(name: "shape")
            -> domain_behavior: <Behavior shape> = Bot.behaviors.find_behavior(name: "shape")
            return cli_behavior: <CLIBehavior wrapping shape>
        -> cli_action: <CLIAction wrapping build> = cli_behavior.actions.get_action(name: "build")
            -> domain_action: <Action build> = Behavior.actions.find_action(name: "build")
            return cli_action: <CLIAction wrapping build>
        -> result: "Build knowledge graph..." = cli_action.execute_operation(operation: "instructions", args: "")
            -> context: {} = CLIAction._parse_args_to_context(args: "")
            -> instruction_dict: {template: "...", rules: [...]} = Action.get_instructions(context)
            -> formatted: "Build knowledge graph..." = CLIAction._format_result(instruction_dict)
            return result: "Build knowledge graph..."
        -> status: "STORY_BOT CLI\n[x] shape..." = StatusDisplay.render(CLIBot)
            -> header: "STORY_BOT CLI\nBot Path: ..." = HeaderDisplay.render(CLIBot)
            -> tree: "[x] shape\n[*] domain..." = HierarchyTreeDisplay.render(CLIBot)
            -> footer: "Commands: status | back..." = FooterDisplay.render()
            return status: "STORY_BOT CLI\n...\nCommands: ..."
        return output: "Build knowledge graph...\n\nSTORY_BOT CLI\n..."
```
### Example: Set and View Scope

```
CLIBot
    result: "Scope set to: Story1, Story2" = CLIScope.set_scope(scope_string: "Story1, Story2")
        -> scope: {type: STORY, value: ["Story1", "Story2"], filter: <KnowledgeGraphFilter>} = CLIScope._parse_scope_string(scope_string: "Story1, Story2")
            -> scope_type: STORY = Scope.infer_type(value: ["Story1", "Story2"])
            -> filter: <KnowledgeGraphFilter> = Scope.__post_init__(type: STORY)
                return filter: <KnowledgeGraphFilter>
            return scope: {type: STORY, value: ["Story1", "Story2"], filter: <KnowledgeGraphFilter>}
        -> session.scope = scope
        return result: "Scope set to: Story1, Story2"
    
    display: "Scope Filter: Story1 ✓, Story2 ✓" = CLIScope.view_scope()
        -> validation: [("Story1", True), ("Story2", True)] = Scope.validate_scope(story_graph)
            -> results: [("Story1", True), ("Story2", True)] = KnowledgeGraphFilter.check_nodes(nodes: ["Story1", "Story2"], graph)
                -> story1_exists: True = KnowledgeGraphFilter.find_node(graph, "Story1")
                -> story2_exists: True = KnowledgeGraphFilter.find_node(graph, "Story2")
                return results: [("Story1", True), ("Story2", True)]
            return validation: [("Story1", True), ("Story2", True)]
        -> formatted: "Scope Filter: Story1 ✓, Story2 ✓" = CLIScope._format_scope_display(scope, validation_results)
        return display: "Scope Filter: Story1 ✓, Story2 ✓"

### Example: Navigate and Execute

```
REPLSession
    result: "Prioritize stories...\n\nSTORY_BOT CLI..." = REPLSession.navigate_and_execute(input: "next")
        -> current_position: {behavior: "shape", action: "render", operation: "confirm"} = CLIBot.get_current_position()
            -> behavior: "shape" = CLIBot.behaviors.get_current_behavior()
            -> action: "render" = behavior.actions.get_current_action()
            -> operation: "confirm" = action.get_current_operation()
            return current_position: {behavior: "shape", action: "render", operation: "confirm"}
        -> next_action: <CLIAction wrapping prioritization.clarify> = CLIBot.behaviors.get_next_action()
            -> next: "prioritization.clarify" = Behaviors.find_next_action(current_behavior: "shape", current_action: "render")
            -> domain_action: <Action prioritization.clarify> = Behaviors.get_domain_action(next)
            return next_action: <CLIAction wrapping prioritization.clarify>
        -> REPLSession.update_state(next_action)
        -> instructions: "Prioritize stories by business value..." = next_action.execute_operation(operation: "instructions")
            -> context: {} = CLIAction._parse_args_to_context(args: "")
            -> instruction_result: {instructions: "Prioritize stories..."} = Action.get_instructions(context)
            -> formatted: "Prioritize stories by business value..." = CLIAction._format_result(instruction_result)
            return instructions: "Prioritize stories by business value..."
        return result: "Prioritize stories...\n\nSTORY_BOT CLI\n[x] shape\n[*] prioritization..."
```
# Key Architectural Decisions

1. **CLI Mirror Pattern**: CLI objects (CLIBot, CLIBehavior, CLIAction) mirror domain structure with string interfaces
2. **CLIAction owns parsing**: Each CLIAction subclass implements `_parse_args_to_context()` to convert strings to typed contexts (including scope strings → Scope objects)
3. **Domain owns state**: Bot.behavior_action_state handles persistence, not CLI
4. **Scope in business domain**: Scope/ActionContext live in `actions/action_context.py`, used by CLIAction
5. **One display file**: All display classes in `status_display.py`, no sub-packages
6. **Action extensions**: Each CLIAction subclass (build, validate, render) in separate file in `cli_actions/`
7. **Navigation via properties**: Use `.current`, `.next` properties for traversal



## File Structure

Based on domain model organization:

```
repl_cli/
├── repl_session.py          # Interactive REPL Session: REPLSession
├── tty_detector.py           # Interactive REPL Session: TTYDetector  
├── command_parser.py         # Interactive REPL Session: CommandParser
├── status_display.py         # Interactive REPL Session: StatusDisplay, HeaderDisplay, 
│                             #   HierarchyTree, Footer, BreadcrumbVisitor
└── cli_bot/                  # CLI Bot domain
    ├── cli_bot.py            # CLI Bot: CLIBot
    ├── cli_behaviors.py      # CLI Bot: CLIBehaviors
    ├── cli_behavior.py       # CLI Bot: CLIBehavior
    └── cli_actions/          # CLI Actions sub-package
        ├── cli_actions.py    # CLI Actions: CLIActions
        ├── cli_action.py     # CLI Actions: CLIAction (base)
        ├── build_cli_action.py       # BuildCLIAction extension
        ├── validate_cli_action.py    # ValidateCLIAction extension
        ├── render_cli_action.py      # RenderCLIAction extension
        └── ...               # Other action extensions

actions/action_context.py     # Core domain: Scope, ActionContext, ScopeActionContext
                              #   KnowledgeGraphFilter, FileFilter
```

**Key Points:**
- **1 package**: `cli_bot/` with `cli_actions/` sub-package
- **4 top-level files** in `repl_cli/`: session, tty, parser, display
- **All displays in one file**: `status_display.py` contains all display classes
- **Action extensions in cli_actions/**: Each CLIAction subclass in its own file
- **Scope in business domain**: Lives in `actions/action_context.py`, used by CLIAction for parsing
- **No state package**: Bot owns `behavior_action_state`, not CLI

---

# Code
## Code Rules

1. No comments
2. No `Dict[str, Any]` in domain (CLI layer exception)
3. 0-2 parameters per function
4. Constructor injection
5. Small classes (under 200 lines)
6. Small functions (under 20 lines)
7. Encapsulation
8. Group by domain
9. DRY

---

## Actions Domain: Scope & Contexts (`actions/action_context.py`)

```python
@dataclass
class Scope:
    type: ScopeType
    value: List[str]
    exclude: List[str] = field(default_factory=list)
    skiprule: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        if self.type == ScopeType.FILES:
            self._filter = FileFilter(self)
        else:
            self._filter = KnowledgeGraphFilter(self)
    
    def filter_graph(self, graph: Dict) -> Dict:
    return self._filter.apply_graph(graph)
    
    def filter_files(self, files: List[Path], bot_paths: BotPaths) -> List[Path]:
        return self._filter.apply_files(files, bot_paths)

class KnowledgeGraphFilter(Filter):
    def apply_graph(self, graph: Dict) -> Dict:
        pass

class FileFilter(Filter):
    def apply_files(self, files: List[Path], bot_paths: BotPaths) -> List[Path]:
        pass
```

---

## CLI Bot (`repl_cli/cli_bot/`)

**Purpose:** Mirror domain structure with string-based interfaces

### `cli_bot.py`
```python
class CLIBot:
    def __init__(self, bot: Bot, session: REPLSession):
        self._bot = bot
        self._behaviors = CLIBehaviors(bot.behaviors, session)
    
    @property
    def name(self) -> str:
        return self._bot.name
    
    @property
    def path(self) -> str:
        return str(self._bot.bot_paths.workspace_directory)
    
    @property
    def behaviors(self) -> CLIBehaviors:
        return self._behaviors
    
    @property
    def status(self) -> str:
        return StatusDisplay(self).render()
```

#### `cli_behaviors.py` & `cli_behavior.py`
```python
class CLIBehaviors:
    @property
    def current(self) -> CLIBehavior:
        pass
    
    @property
    def next(self) -> CLIBehavior:
        pass
    
    @property
    def all(self) -> List[str]:
        pass
    
    def navigate_to(self, name: str) -> str:
        pass

class CLIBehavior:
    @property
    def name(self) -> str:
        pass
    
    @property
    def description(self) -> str:
        pass
    
    @property
    def status(self) -> str:
        pass
    
    @property
    def actions(self) -> CLIActions:
        pass
```

---

## CLI Actions (`repl_cli/cli_bot/cli_actions/`)

#### `cli_actions.py` & `cli_action.py`
```python
class CLIActions:
    @property
    def current(self) -> CLIAction:
        pass
    
    @property
    def next(self) -> CLIAction:
        pass
    
    def navigate_to(self, name: str) -> str:
        pass

class CLIAction:
    def __init__(self, action: Action, session: REPLSession):
        self._action = action
        self._session = session
    
    def instructions(self, args: str = "") -> str:
        context = self._parse_args_to_context(args)
        result = self._action.get_instructions(context)
        return self._format_result(result)
    
    def submit(self, args: str) -> str:
        context = self._parse_args_to_context(args)
        result = self._action.submit(context)
        return self._format_result(result)
    
    def confirm(self) -> str:
        context = self._action.context_class()()
        result = self._action.confirm(context)
        return self._format_result(result)
    
    def _parse_args_to_context(self, args: str):
        pass
    
    def _format_result(self, action_result):
        return action_result.get('output', str(action_result))
```

#### Action Extensions (examples)

`build_cli_action.py`, `validate_cli_action.py`, `render_cli_action.py` - each extends CLIAction with specific parsing logic

---

## Interactive REPL Session (`repl_cli/`)

#### `repl_session.py`
```python
class REPLSession:
    def __init__(self, bot, workspace_directory):
        self.cli_bot = CLIBot(bot, self)
        self.status_display = StatusDisplay(self.cli_bot)
        self.tty_detector = TTYDetector()
        self.command_parser = CommandParser()
    
    @property
    def current_behavior(self):
        return self.cli_bot.behaviors.current
    
    @property
    def current_action(self):
        return self.cli_bot.behaviors.current.actions.current
    
    def execute_submit(self, args: str = "") -> str:
        return self.current_action.submit(args)
    
    def execute_confirm(self) -> str:
        return self.current_action.confirm()
    
    def execute_instructions(self, args: str = "") -> str:
        return self.current_action.instructions(args)
```

#### `tty_detector.py`
```python
class TTYDetector:
    @staticmethod
    def detect_input_mode() -> TTYDetectionResult:
        pass
```

#### `command_parser.py`
```python
class CommandParser:
    def parse_and_route(self, input_line: str):
        pass
```

#### `status_display.py`
```python
class StatusDisplay:
    def __init__(self, cli_bot):
        self.cli_bot = cli_bot
    
    def render(self) -> str:
        pass

class HeaderDisplay:
    def render(self, cli_bot) -> str:
        pass

class HierarchyTreeDisplay:
    def render(self, cli_bot) -> str:
        pass

class FooterDisplay:
    def render(self) -> str:
        pass

class BreadcrumbVisitor:
    def visit_behavior(self, behavior):
        pass
    
    def visit_action(self, action):
        pass
    
    def get_output(self) -> str:
        pass
```

---


# Testing Strategy

### Implement Scenarios as pytest Tests

**Replace existing tests** in `agile_bot/bots/base_bot/test/test_run_interactive_repl.py` - start from scratch.

Implement **ALL scenarios from this document** following the **pytest Given-When-Then Orchestrator Pattern** defined in `agile_bot/bots/story_bot/behaviors/tests/rules/`.

### Test Structure Requirements

**File Structure:**
```
agile_bot/bots/base_bot/test/
├── test_initialize_repl_session.py      # Sub-epic: Initialize REPL Session
├── test_navigate_bot_behaviors_and_actions_with_cli.py  # Sub-epic: Navigate Bot Behaviors and Actions With CLI
├── test_execute_action_operation_through_cli.py     # Sub-epic: Execute Action Operation Through CLI
├── test_manage_bot_scope_through_cli.py             # Sub-epic: Manage Bot Scope Through CLI
├── test_display_bot_state_using_cli.py              # Sub-epic: Display Bot State Using CLI
└── test_get_help_using_cli.py                       # Sub-epic: Get Help Using CLI
```

**Naming Conventions** (from `use_class_based_organization.json`):
- **File**: One per sub-epic in snake_case: `test_<sub_epic_name>.py`
- **Class**: One per story, EXACT story name in PascalCase: `class Test<ExactStoryName>`
- **Method**: One per scenario, EXACT scenario name in snake_case: `def test_<exact_scenario_name>(self)`
- **Class order**: Same order as stories appear in story map

**Example:**
```python
# File: test_initialize_repl_session.py
# Sub-epic: Initialize REPL Session

class TestLaunchCLIInInteractiveMode:
    """Story: Launch CLI in Interactive Mode"""
    
    def test_cli_launches_in_interactive_mode(self):
        """
        SCENARIO: CLI launches in interactive mode
        GIVEN: REPLSession is configured for interactive mode
        WHEN: user runs 'python repl_main.py --stdio'
        THEN: REPLSession creates CLIBot wrapping Bot
        """
        pass
    
    def test_cli_loads_existing_behavior_action_state_on_launch(self):
        """SCENARIO: CLI loads existing behavior action state on launch"""
        pass

class TestLaunchCLIInPipeMode:
    """Story: Launch CLI in Pipe Mode"""
    
    def test_cli_launches_in_pipe_mode(self):
        """SCENARIO: CLI launches in pipe mode"""
        pass

# ... all other stories in this sub-epic ...
```

### Test Rules to Follow

**All tests MUST follow these rules** from `agile_bot/bots/story_bot/behaviors/tests/rules/`:

#### Core Structure Rules
1. **`pytest_bdd_orchestrator_pattern.json`** - Master pattern with complete example
2. **`use_class_based_organization.json`** - File per sub-epic, class per story, method per scenario
3. **`use_given_when_then_helpers.json`** - Given-When-Then structure with helper functions
4. **`test_observable_behavior.json`** - Test through public API only

#### Test Quality Rules
5. **`use_domain_language.json`** - Use domain terms from this doc (CLIBot, CLIAction, etc.)
6. **`self_documenting_tests.json`** - Tests are self-documenting through code
7. **`consistent_vocabulary.json`** - One word per concept throughout
8. **`match_specification_scenarios.json`** - Match scenarios from this doc EXACTLY
9. **`use_exact_variable_names.json`** - Variable names match domain model

#### Test Implementation Rules
10. **`design_api_through_failing_tests.json`** - Write tests against real expected API first
11. **`call_production_code_directly.json`** - Call real production code, let tests fail naturally
12. **`cover_all_behavior_paths.json`** - Test normal, edge, and error paths
13. **`mock_only_boundaries.json`** - Mock external APIs only, not business logic
14. **`helper_extraction_and_reuse.json`** - Extract duplicate setup to reusable helpers
15. **`create_parameterized_tests_for_scenarios.json`** - Use @pytest.mark.parametrize for scenario outlines

#### Production Code Rules
16. **`production_code_clean_functions.json`** - Keep functions under 20 lines
17. **`production_code_explicit_dependencies.json`** - Constructor injection only
18. **`no_defensive_code_in_tests.json`** - No defensive code in test setup

#### Code Quality Rules
19. **`use_ascii_only.json`** - ASCII only (no Unicode) for Windows compatibility
20. **`place_imports_at_top.json`** - All imports at top of file
21. **`define_fixtures_in_test_file.json`** - Define fixtures in same file as tests
22. **`bug_fix_test_first.json`** - Write failing test first for bugs

### Validation

After implementing tests, run:
```bash
python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action validate --scope "files:agile_bot/bots/base_bot/test/test_*.py"
```

All 22 test rules MUST pass before code is considered complete. Since the solution largely works as is, most errors will come from something wrong with the test vs. fixing the code.

---

## Functional Differences (What's New or Changed)

**Most functionality already exists** - this is primarily an architectural refactor. Test Phase 1 will verify what's actually different.

**Potential New/Changed Functionality to Verify:**

- **Progress breadcrumb**: `Progress: behavior.action.operation` - observed in testing, verify if consistently shown
- **Scope validation display**: Format may differ - verify `✓` vs `(no match)` indicators are consistent
- **Help system completeness**: Verify if `help <behavior>`, `help --<param>`, `help examples` all exist

**Action:** Write tests against current implementation in Phase 1. Any missing functionality will be identified when tests fail or scenarios can't be implemented.

---

## Testing Strategy for New Features

### Phase 1 (Current Implementation)
- **Skip** new features that don't exist yet
- Write tests for existing behavior only
- Document which scenarios are skipped as "NOT IMPLEMENTED YET"

### Phase 3 (During Refactor)
- Implement new features incrementally
- Add tests for new features as they're built
- Use TDD: write test → implement feature → test passes

### Validation Checkpoints

Before starting refactor:
1. ✅ Identify which scenarios test EXISTING behavior (test these in Phase 1)
2. ✅ Identify which scenarios test NEW behavior (implement during Phase 3)
3. ✅ Mark skipped tests with `@pytest.mark.skip(reason="New feature - not yet implemented")`

During refactor:
1. ✅ Implement new feature
2. ✅ Remove skip marker from test
3. ✅ Verify test passes
4. ✅ Commit



# Success Criteria

1. All classes under 200 lines
2. All functions under 20 lines
3. Domain-based organization
4. CLI mirror pattern implemented
5. String-based interface throughout CLI
6. Proper visitor pattern for displays
7. Scope domain simplified
8. All code validation rules pass
9. Existing functionality preserved
10. Tests pass


# Migration Notes

- Break changes and fix!
- NOT Backwards compatible, no fallbacks! 

# Implementation Plan

### Phase 0: Update Story Graph (FIRST)

**Location:** `agile_bot/bots/base_bot/docs/stories/story-graph.json`

The structure in this document is the **point of truth**. Update the story graph before any code or test changes.

**Actions:**
1. **Replace Epic Structure**: Replace "Run Interactive REPL" epic and all its sub epics and stories with the structure defined in "New Epic Structure" section
2. **Add Domain Model Elements**: Add domain model objects from "Domain Model" section:
   - REPLSession, TTYDetector, CommandParser, StatusDisplay (Interactive REPL Session)
   - CLIBot, CLIBehaviors, CLIBehavior (CLI Bot)
   - CLIActions, CLIAction (CLI Actions)
   - Scope, KnowledgeGraphFilter, FileFilter, ActionContext, ScopeActionContext (Actions Domain)

---

### Phase 1: Write Tests Against Current Implementation (SAFETY NET)

**Goal:** Create comprehensive test suite for EXISTING working code before refactoring.

**Why test-first?**
- Tests validate current behavior is correctly understood
- Tests serve as safety net during refactoring
- If tests fail during refactor, we know refactor broke something
- Classic "characterization testing" pattern for legacy code

**Implementation:**

Create test files following pytest orchestrator pattern as defined in "Testing Strategy" section.

**Test files to create:**
- `test_initialize_repl_session.py` - Test current session initialization
- `test_navigate_bot_behaviors_and_actions_with_cli.py` - Test current navigation
- `test_execute_action_operation_through_cli.py` - Test current action execution
- `test_manage_bot_scope_through_cli.py` - Test current scope management
- `test_display_bot_state_using_cli.py` - Test current display rendering
- `test_get_help_using_cli.py` - Test current help system

**Test against:**
- Current implementation in `agile_bot/bots/base_bot/src/repl_cli/`
- Use actual CLI commands from scenarios
- Test outputs match observed behavior (from testing with `demo/mob_minion`)

---

### Phase 2: Validate All Tests Pass

**Goal:** Ensure test suite is correct BEFORE refactoring.

**Actions:**
1. Run all tests: `pytest agile_bot/bots/base_bot/test/test_*.py -v`
2. Fix any failing tests (tests should match current working behavior)
3. Run code validation:
   ```bash
   python agile_bot/bots/story_bot/src/story_bot_cli.py --behavior tests --action validate --scope "files:agile_bot/bots/base_bot/test/test_*.py"
   ```
4. Ensure all 22 test rules pass
5. **CHECKPOINT**: All tests green = safe to refactor

---

### Phase 3: Refactor Code (With Safety Net)

**Goal:** Refactor to clean architecture while keeping tests passing.

**Strategy:** Small incremental refactors, running tests after each change.

#### Step 3.1: Simplify Scope Domain
1. Refactor `actions/action_context.py`: Scope, KnowledgeGraphFilter, FileFilter
2. Run tests - should still pass
3. Commit if green

#### Step 3.2: Create CLI Bot Layer
1. Create `cli_bot/`: cli_bot, cli_behaviors, cli_behavior
2. Wire into existing code
3. Run tests - should still pass
4. Commit if green

#### Step 3.3: Create CLI Actions Layer
1. Create `cli_bot/cli_actions/`: cli_actions, cli_action
2. Create action extensions (build_cli_action, validate_cli_action, etc.)
3. Implement `_parse_args_to_context()` and `_format_result()` in each
4. Run tests - should still pass
5. Commit if green

#### Step 3.4: Create Interactive REPL Session
1. Create session coordination (repl_session, tty_detector, command_parser)
2. Create displays in single file (status_display)
3. Run tests - should still pass
4. Commit if green

#### Step 3.5: Integration & Cleanup
1. Update repl_main.py to use new architecture
2. Remove legacy code (only after new code proven working)
3. Run tests - should still pass
4. Commit if green

---

### Phase 4: Final Validation

**Goal:** Verify refactored code meets all quality standards.

**Actions:**
1. Run full test suite: `pytest agile_bot/bots/base_bot/test/test_*.py -v`
2. Verify all tests still pass
3. Run code validation to ensure all 22 test rules pass
4. Manual testing with `demo/mob_minion` to verify CLI behavior unchanged
5. Review code against clean architecture principles

**Success Criteria:**
- ✅ All tests pass
- ✅ All 22 test rules pass
- ✅ CLI behavior matches documented scenarios
- ✅ Code follows clean architecture patterns
- ✅ No breaking changes to public API

