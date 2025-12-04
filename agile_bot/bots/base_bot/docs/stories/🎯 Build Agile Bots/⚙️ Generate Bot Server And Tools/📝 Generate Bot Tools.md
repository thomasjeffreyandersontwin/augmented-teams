# 📝 Generate Bot Tools

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Build Agile Bots
**Feature:** Generate Bot Server And Tools

## Story Description

MCP Server Generator creates ONE overall bot tool that reads workflow state to determine current behavior/action and executes the correct one so that users don't need to specify which behavior/action to invoke.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** MCP Server Generator scans base_actions/ folder, **then** Generator discovers actions by reading each action folder
- **When** Generator reads action configuration from each action folder, **then** action configuration specifies: name, workflow (true/false), order, next_action
- **When** Generator creates tools for all discovered actions, **then** Tools include workflow state awareness based on action workflow configuration flag

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given base_actions/ folder exists with action subfolders
And Generator is initialized
And action configuration schema is defined with fields: name, workflow, order, next_action
```

## Scenarios

### Scenario: Generator creates bot tool for test_bot

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has 4 behaviors configured as ['shape', 'discovery', 'exploration', 'specification']
And each behavior has 6 base actions configured
When Generator processes Bot Config
Then Generator creates 1 bot tool instance (not separate tools per behavior/action)
And bot tool 'test_bot' is created with workflow state awareness
And bot tool reads workflow state to determine current behavior/action
And bot tool routes to correct behavior/action based on workflow state
And bot tool includes routing logic to invoke Bot.Behavior.Action
```

### Scenario: Bot tool loads workflow state to determine routing

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot tool is created
And workflow state shows: current_action='story_bot.discovery.build_knowledge'
And build_knowledge action configuration specifies workflow=true, next_action='render_output'
When bot tool is invoked
Then bot tool loads workflow state from exact path: project_area/workflow_state.json
And bot tool extracts current behavior and action from state
And bot tool routes invocation to discovery.build_knowledge
And bot tool includes method to execute build_knowledge with workflow transitions
```

### Scenario: Bot tool handles independent actions via parameter

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot tool is created
And correct_bot action configuration specifies workflow=false (independent action)
When bot tool is invoked with parameter action='correct_bot'
Then bot tool routes to correct_bot action (parameter overrides workflow state)
And bot tool does NOT use workflow state for routing independent actions
And bot tool does NOT include workflow transition logic for correct_bot
And Tool is still created with forwarding logic but no workflow transitions
```

### Scenario: Bot tool handles missing workflow state file

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot tool is created
And workflow state does NOT exist at project_area/workflow_state.json
And Bot Config first behavior is 'shape' with first action 'gather_context'
When bot tool is invoked without parameters
Then bot tool attempts to load from exact path: project_area/workflow_state.json
And bot tool detects file not found
And bot tool defaults to first behavior ('shape') and first action ('gather_context')
And bot tool creates initial workflow state
And Tool is still created with routing logic using default behavior/action
```

### Scenario: Bot tool handles terminal actions with workflow completion

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot tool is created
And workflow state shows: current_action='story_bot.exploration.validate_rules'
And validate_rules action configuration specifies workflow=true, next_action=null
When bot tool is invoked
Then bot tool loads workflow state from exact path: project_area/workflow_state.json
And bot tool routes invocation to exploration.validate_rules
And bot tool detects next_action=null (terminal action)
And bot tool does NOT include transition logic after validate_rules
And Tool is still created with forwarding logic but indicates workflow completion
```

### Scenario: Bot tool handles auto_progress for seamless transitions

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot tool is created
And workflow state shows: current_action='story_bot.discovery.build_knowledge'
And build_knowledge action configuration specifies auto_progress=true, next_action='render_output'
When bot tool is invoked
Then bot tool loads workflow state from exact path: project_area/workflow_state.json
And bot tool routes invocation to discovery.build_knowledge
And bot tool detects auto_progress=true
And bot tool includes method to automatically transition to render_output
And Tool is still created with forwarding logic and automatic progression
```

## Generated Artifacts

### Bot Tool
**Generated by:** MCP Server Generator  
**Location:** MCP server configuration  
**Content:**
- ONE bot tool (not separate tools per behavior/action)
- Tool reads workflow state to determine current behavior/action
- Tool routes to correct behavior/action based on state or parameters
- Tool uses action configuration for workflow transitions
- Tool handles workflow actions, independent actions, terminal actions, auto_progress

## Notes

- Generator creates ONE overall bot tool (not separate tools per behavior/action)
- Bot tool is workflow-state-aware: reads workflow state to determine current behavior/action
- Bot tool can route based on workflow state OR explicit action parameter
- Workflow actions (workflow: true) trigger automatic transitions using next_action
- Independent actions (workflow: false) can be invoked via parameter, no workflow transitions
- Terminal actions (next_action=null) indicate workflow completion
- Auto_progress actions transition automatically without human confirmation
- Bot tool is fault-tolerant: handles missing state, malformed configuration gracefully

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Generate Bot Server And Tools feature, Domain Concepts (Action Configuration, Workflow Action, Independent Action)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria and domain rules in increment 3 exploration document


