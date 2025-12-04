# 📝 Generate Behavior Tools

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Build Agile Bots
**Feature:** Generate Bot Server And Tools

## Story Description

Generator creates behavior-specific tools for each action based on bot configuration and action sequence so that each behavior has its own MCP tool namespace with automatic workflow transitions.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Generator enumerates behaviors from Bot Config, **then** Generator creates behavior-specific tools for each action in base_actions/
- **When** Generator loads action configuration from each action folder, **then** Workflow actions (workflow: true) get automatic transition logic using next_action field
- **When** Generator loads action configuration from each action folder, **then** Independent actions (workflow: false) get no automatic transition logic
- **When** Generator creates behavior tools, **then** Each behavior tool knows action sequence from ordered action configuration files

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given Bot Config (agent.json) exists with behaviors defined
And base_actions/ folder contains action folders with action configuration files
And Generator has successfully scanned base_actions/ (per Generate Bot Tools story)
And Generator is ready to create behavior-specific tools
```

## Scenarios

### Scenario: Generator creates behavior tools for all defined behaviors

**Steps:**
```gherkin
Given Bot Config defines behaviors: ['shape', 'discovery', 'exploration', 'scenarios']
And base_actions/ contains: gather_context, decide_planning_criteria, build_knowledge, render_output, validate_rules
When Generator enumerates behaviors from Bot Config
Then Generator creates 4 behavior tools (ONE tool per behavior)
And Each behavior tool can route to all 5 actions
And Tools are named: shape_bot, discovery_bot, exploration_bot, scenarios_bot
And Each tool routes between actions based on parameters or workflow state
```

### Scenario: Generator applies workflow transitions to workflow actions

**Steps:**
```gherkin
Given behavior 'shape' is being processed
And gather_context/action configuration specifies workflow=true, order=1, next_action='decide_planning_criteria'
And decide_planning_criteria/action configuration specifies workflow=true, order=2, next_action='build_knowledge'
When Generator creates shape_bot tool
Then shape_bot tool knows about all actions and their workflow configuration
And When shape_bot routes to gather_context, it includes automatic transition logic to decide_planning_criteria
And When shape_bot routes to decide_planning_criteria, it includes automatic transition logic to build_knowledge
And Tool uses action configuration to determine transitions
```

### Scenario: Generator excludes transition logic for independent actions

**Steps:**
```gherkin
Given behavior 'shape' is being processed
And correct_bot/action configuration specifies workflow=false, order=null, next_action=null
When Generator creates shape_bot tool
And shape_bot is invoked with action parameter 'correct_bot'
Then shape_bot routes to correct_bot action
And shape_bot does NOT include automatic transition logic for correct_bot
And shape_bot does NOT inject next action instructions after correct_bot
And correct_bot is independently invokable via parameter
```

### Scenario: Generator orders action sequence from action configuration

**Steps:**
```gherkin
Given behavior 'shape' is being processed
And action configuration files specify: gather_context(order=1), decide_planning_criteria(order=2), build_knowledge(order=3), render_output(order=4), validate_rules(order=5)
And correct_bot specifies workflow=false (no order)
When Generator creates shape_bot tool
Then shape_bot knows action sequence from action configuration order fields
And shape_bot workflow sequence is: gather_context → decide_planning_criteria → build_knowledge → render_output → validate_rules
And shape_bot can route to correct_bot independently (not in workflow sequence)
```

### Scenario: Generator handles terminal action in behavior sequence

**Steps:**
```gherkin
Given behavior 'exploration' is being processed
And validate_rules/action configuration specifies workflow=true, order=5, next_action=null
When Generator creates exploration_bot tool
And exploration_bot routes to validate_rules
Then exploration_bot recognizes validate_rules specifies next_action=null (terminal)
And exploration_bot does NOT inject next action instructions after validate_rules
And exploration_bot indicates workflow completion when validate_rules finishes
```

### Scenario: Generator applies auto_progress for seamless transitions

**Steps:**
```gherkin
Given behavior 'discovery' is being processed
And build_knowledge/action configuration specifies workflow=true, order=3, next_action='render_output', auto_progress=true
When Generator creates discovery_bot tool
And discovery_bot routes to build_knowledge
Then discovery_bot recognizes auto_progress=true for build_knowledge
And discovery_bot automatically transitions to render_output without human confirmation
And discovery_bot automatically invokes render_output after build_knowledge completes
```

### Scenario: Generator handles missing behavior in Bot Config

**Steps:**
```gherkin
Given Bot Config defines behaviors: ['shape', 'discovery']
And user expects 'exploration' behavior to be available
When Generator enumerates behaviors from Bot Config
Then Generator creates tools only for 'shape' and 'discovery' behaviors: shape_bot, discovery_bot
And Generator does NOT create exploration_bot tool
And Generator warns user that some behaviors may be missing (non-blocking)
```

## Generated Artifacts

### Behavior-Specific Tools
**Generated by:** MCP Server Generator  
**Location:** Generated MCP server configuration  
**Content:**
- ONE tool per behavior (e.g., shape_bot, discovery_bot, exploration_bot, scenarios_bot)
- Each behavior tool routes to all actions based on parameters or workflow state
- Behavior tool includes automatic transition logic based on action configuration
- Independent actions (workflow: false) are routable but not in workflow sequence

## Notes

- ONE tool per behavior (e.g., shape_bot, discovery_bot, exploration_bot, scenarios_bot)
- Each behavior tool routes between actions based on parameters or workflow state
- Workflow sequence is determined by order field in action configuration
- Auto-progress actions transition automatically without human confirmation
- Terminal actions (next_action=null) indicate workflow completion
- Independent actions are routable but don't participate in workflow sequence

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Generate Bot Server And Tools feature, Domain Concepts (Workflow Action, Independent Action, Sequential Flow)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria and domain rules in increment 3 exploration document


