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

### Scenario: Generator creates behavior tools for test_bot with 4 behaviors

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has 4 behaviors configured as ['shape', 'discovery', 'exploration', 'specification']
And each behavior has 6 base actions configured
When Generator processes Bot Config
Then Generator enumerates 4 behaviors from Bot Config
And Generator creates 4 behavior tool instances (ONE tool per behavior)
And tools 'shape_bot', 'discovery_bot', 'exploration_bot', 'specification_bot' are created
And each behavior tool includes routing logic to invoke Bot.Behavior.Action
And Tool catalog contains all 4 generated behavior tool instances
```

### Scenario: Generator loads action configuration for workflow transitions

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'shape'
And behavior has action 'gather_context'
And action has action_config.json with workflow=true, order=1, next_action='decide_planning_criteria'
When Generator creates tool for shape behavior
Then Generator loads action configuration from exact path: base_actions/gather_context/action_config.json
And Generated behavior tool is configured with workflow transitions
And shape_bot includes method to route to gather_context with automatic transition to decide_planning_criteria
And Tool uses action configuration to determine workflow transitions
```

### Scenario: Generator handles independent actions without workflow transitions

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'shape'
And behavior has action 'correct_bot'
And action has action_config.json with workflow=false, order=null, next_action=null
When Generator creates tool for shape behavior
Then Generator loads action configuration from exact path: base_actions/correct_bot/action_config.json
And Generated behavior tool detects workflow=false for correct_bot
And shape_bot does NOT include workflow transition logic for correct_bot
And Tool is still created with forwarding logic but no workflow transitions
```

### Scenario: Generator creates behavior tool with action routing

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'shape'
And behavior has actions with order: gather_context(1), decide_planning_criteria(2), build_knowledge(3), render_output(4), validate_rules(5)
When Generator creates tool 'shape_bot'
Then Generated behavior tool includes method to route to all 6 actions
And Generated behavior tool includes method to load action configuration from base_actions/
And Generated behavior tool includes method to determine action sequence from order fields
And Tool catalog contains behavior tool with routing capabilities
```

### Scenario: Generator handles terminal actions in behavior sequence

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'exploration'
And behavior has action 'validate_rules'
And action has action_config.json with workflow=true, order=5, next_action=null
When Generator creates tool for exploration behavior
Then Generated behavior tool detects next_action=null (terminal action)
And exploration_bot does NOT include transition logic after validate_rules
And Tool is still created with forwarding logic but indicates workflow completion
```

### Scenario: Generator handles auto_progress for seamless transitions

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'discovery'
And behavior has action 'build_knowledge'
And action has action_config.json with workflow=true, order=3, next_action='render_output', auto_progress=true
When Generator creates tool for discovery behavior
Then Generated behavior tool detects auto_progress=true for build_knowledge
And discovery_bot includes method to automatically transition to render_output
And Tool is still created with forwarding logic and automatic progression
```

### Scenario: Generator handles missing behavior in Bot Config

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has 2 behaviors configured as ['shape', 'discovery']
And Bot Config does NOT include 'exploration' behavior
When Generator processes Bot Config
Then Generator enumerates 2 behaviors from Bot Config
And Generator creates 2 behavior tool instances (shape_bot, discovery_bot)
And Generator does NOT create exploration_bot tool
And Generator logs warning 'exploration behavior not configured in Bot Config'
And Tool catalog contains only configured behavior tools
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


