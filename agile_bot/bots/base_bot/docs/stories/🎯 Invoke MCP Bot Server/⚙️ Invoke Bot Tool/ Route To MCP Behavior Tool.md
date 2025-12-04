# 📝 Route To MCP Behavior  Tool

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Invoke MCP Bot Server
**Feature:** Invoke Bot Tool

## Story Description

AI Chat routes bot tool invocations to current behavior based on workflow state so that users resume at their last saved position without needing to specify which behavior to invoke.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** AI Chat invokes bot tool without specifying specific action, **then** Router checks Workflow State for current behavior
- **When** Router checks Workflow State, **then** Router loads workflow state from {project_area}/workflow state
- **When** Router loads workflow state, **then** Router extracts current_behavior from state
- **When** Router extracts current_behavior, **then** Router routes to current behavior's MCP tool (not default/first behavior)
- **When** Router routes to behavior tool, **then** Routing uses saved state to determine correct behavior dynamically

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given MCP Bot Server is running with ONE behavior tool per behavior
And Bot Config defines behaviors: shape, discovery, exploration, scenarios
And Workflow State is persisted to project_area/workflow state
And workflow state contains: current_behavior (full path), current_action (full path), completed_actions[], timestamp
```

## Scenarios

### Scenario: Router routes to current behavior from saved state

**Steps:**
```gherkin
Given workflow state exists at project_area/workflow state
And workflow state contains: current_behavior='story_bot.discovery', current_action='story_bot.discovery.gather_context'
And AI Chat invokes bot tool without specifying behavior
When Router receives bot tool invocation
Then Router loads workflow state from project_area/
And Router parses workflow state successfully
And Router extracts current_behavior='story_bot.discovery'
And Router routes invocation to discovery_bot tool
And Router does NOT route to default 'shape' behavior (first behavior)
```

### Scenario: Router defaults to first behavior when workflow state missing

**Steps:**
```gherkin
Given workflow state does NOT exist at project_area/workflow state
And AI Chat invokes bot tool without specifying behavior
When Router receives bot tool invocation
Then Router attempts to load workflow state from project_area/
And Router detects file not found
And Router defaults to first behavior ('shape') from Bot Config
And Router routes invocation to shape_bot tool
And Router creates initial workflow state with current_behavior='story_bot.shape', current_action='story_bot.shape.gather_context'
```

### Scenario: Router handles malformed workflow state file

**Steps:**
```gherkin
Given workflow state exists at project_area/workflow state
And workflow state contains invalid JSON syntax (malformed)
And AI Chat invokes bot tool without specifying behavior
When Router receives bot tool invocation
Then Router attempts to parse workflow state
And Router detects JSON parsing error
And Router warns user in chat about malformed state file (non-blocking)
And Router defaults to first behavior ('shape') from Bot Config
And Router routes invocation to shape_bot tool
```

### Scenario: Router handles missing current_behavior field in state

**Steps:**
```gherkin
Given workflow state exists at project_area/workflow state
And workflow state is valid JSON but missing current_behavior field
And AI Chat invokes bot tool without specifying behavior
When Router receives bot tool invocation
Then Router loads workflow state successfully
And Router attempts to extract current_behavior field
And Router detects missing current_behavior field
And Router warns user in chat about incomplete state file (non-blocking)
And Router defaults to first behavior ('shape') from Bot Config
And Router routes invocation to shape_bot tool
```

### Scenario: Router routes to non-default behavior mid-workflow

**Steps:**
```gherkin
Given workflow state contains: current_behavior='story_bot.exploration', current_action='story_bot.exploration.build_knowledge'
And Bot Config behaviors list is: shape, discovery, exploration, scenarios
And 'exploration' is the third behavior (not first)
And AI Chat invokes bot tool without specifying behavior
When Router receives bot tool invocation
Then Router loads workflow state
And Router extracts current_behavior='story_bot.exploration'
And Router routes to exploration_bot tool (third behavior, not first)
And Router demonstrates state-based routing (not hardcoded to default)
```

### Scenario: Router handles behavior not found in Bot Config

**Steps:**
```gherkin
Given workflow state contains: current_behavior='story_bot.invalid_behavior', current_action='story_bot.invalid_behavior.gather_context'
And Bot Config defines behaviors: shape, discovery, exploration, scenarios
And 'invalid_behavior' is NOT in Bot Config behaviors list
And AI Chat invokes bot tool without specifying behavior
When Router receives bot tool invocation
Then Router loads workflow state
And Router extracts current_behavior='story_bot.invalid_behavior'
And Router attempts to find 'invalid_behavior' in Bot Config
And Router fails to find matching behavior
And Router warns user that behavior not found in configuration (non-blocking)
And Router defaults to first behavior ('shape') from Bot Config
And Router routes invocation to shape_bot tool
```

## Generated Artifacts

### Workflow State File (workflow state)
**Created by:** Router (if missing)  
**Location:** {project_area}/workflow state  
**Content:**
- current_behavior: Full path of current behavior (e.g., story_bot.discovery)
- current_action: Full path of current action (e.g., story_bot.discovery.gather_context)
- completed_actions: Array of completed action records with full paths
- timestamp: Last update timestamp

## Notes

- Router is fault-tolerant: warns on errors but doesn't fail (defaults to first behavior)
- State-based routing ensures users resume at saved position, not hardcoded default
- Missing workflow state triggers initialization to first behavior/first action
- Router validates both file existence AND structure before extracting current_behavior

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Invoke Bot Tool feature, Domain Concepts (Workflow State, State-Based Routing, Auto Resume)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria and domain rules in increment 3 exploration document


