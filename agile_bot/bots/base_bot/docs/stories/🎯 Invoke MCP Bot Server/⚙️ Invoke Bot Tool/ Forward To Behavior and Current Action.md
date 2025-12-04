# 📝 Forward To Behavior and Current Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Invoke MCP Bot Server
**Feature:** Invoke Bot Tool

## Story Description

Router forwards tool invocations to the exact action within the current behavior based on saved workflow state so that users resume at the precise point they left off (not just the right behavior, but the right action within that behavior).

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Router receives behavior tool invocation, **then** Router loads Workflow State from persistent storage
- **When** Router loads Workflow State, **then** Router extracts current_behavior and current_action from state
- **When** Router extracts current_behavior and current_action, **then** Router forwards call to Bot.Behavior[current_behavior].Action[current_action]
- **When** Router forwards to current action, **then** Forwarding ensures user resumes at exact point they left off
- **When** workflow state file doesn't exist, **then** Router defaults to first behavior/first action

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given MCP Bot Server is running with ONE behavior tool per behavior
And Bot Config defines behaviors with ordered actions
And Workflow State is persisted to project_area/workflow state
And workflow state contains: current_behavior (full path), current_action (full path), completed_actions[], timestamp
```

## Scenarios

### Scenario: Router forwards to current action within behavior

**Steps:**
```gherkin
Given workflow state shows: current_behavior='story_bot.discovery', current_action='story_bot.discovery.build_knowledge'
And discovery behavior has ordered actions: gather_context(1), decide_planning_criteria(2), build_knowledge(3), render_output(4), validate_rules(5)
When Router receives discovery_bot tool invocation
Then Router loads workflow state from project_area/
And Router extracts current_behavior='story_bot.discovery'
And Router extracts current_action='story_bot.discovery.build_knowledge'
And Router forwards call to discovery_bot with parameter action='build_knowledge'
And Router does NOT forward to first action (gather_context)
And User resumes at exact action (build_knowledge) where they left off
```

### Scenario: Router defaults to first behavior and first action when state missing

**Steps:**
```gherkin
Given workflow state does NOT exist at project_area/workflow state
And Bot Config first behavior is 'shape' with first action 'gather_context'
When Router receives bot tool invocation
Then Router attempts to load workflow state
And Router detects file not found
And Router defaults to first behavior='shape'
And Router defaults to first action='gather_context' within shape
And Router forwards call to shape_bot with parameter action='gather_context'
And Router creates initial workflow state with current_behavior='story_bot.shape', current_action='story_bot.shape.gather_context'
```

### Scenario: Router resumes mid-workflow at specific action

**Steps:**
```gherkin
Given workflow state shows: current_behavior='story_bot.exploration', current_action='story_bot.exploration.decide_planning_criteria'
And exploration behavior actions: gather_context(1), decide_planning_criteria(2), build_knowledge(3), render_output(4), validate_rules(5)
And decide_planning_criteria is NOT in completed_actions (was interrupted)
When Router receives exploration_bot tool invocation
Then Router loads workflow state
And Router extracts current_action='story_bot.exploration.decide_planning_criteria'
And current_action indicates action was previously started
And Router forwards to exploration_bot with parameter action='decide_planning_criteria'
And Router notifies user: action was previously started (not completed)
And User can choose to retry or continue decide_planning_criteria
```

### Scenario: Router handles missing current_action field in state

**Steps:**
```gherkin
Given workflow state exists with: current_behavior='story_bot.discovery'
And workflow state is missing current_action field
When Router receives bot tool invocation
Then Router loads workflow state
And Router extracts current_behavior='story_bot.discovery'
And Router attempts to extract current_action
And Router detects missing current_action field
And Router warns user about incomplete state file (non-blocking)
And Router defaults to first action of discovery behavior (gather_context)
And Router forwards to discovery_bot with parameter action='gather_context'
```

### Scenario: Router handles invalid action name in state

**Steps:**
```gherkin
Given workflow state exists with: current_behavior='story_bot.shape', current_action='story_bot.shape.invalid_action_name'
And shape behavior has valid actions: gather_context, decide_planning_criteria, build_knowledge, render_output, validate_rules
And 'invalid_action_name' is NOT in shape behavior's action list
When Router receives bot tool invocation
Then Router loads workflow state
And Router extracts current_behavior='story_bot.shape', current_action='story_bot.shape.invalid_action_name'
And Router attempts to find 'invalid_action_name' in shape behavior
And Router fails to find matching action
And Router warns user that action not found in behavior (non-blocking)
And Router defaults to first action of shape behavior (gather_context)
And Router forwards to shape_bot with parameter action='gather_context'
```

### Scenario: Router forwards to terminal action

**Steps:**
```gherkin
Given workflow state exists with: current_behavior='story_bot.scenarios', current_action='story_bot.scenarios.validate_rules'
And validate_rules is terminal action (next_action=null)
When Router receives bot tool invocation
Then Router loads workflow state
And Router extracts current_action='story_bot.scenarios.validate_rules'
And Router forwards to scenarios_bot with parameter action='validate_rules'
And Router identifies validate_rules as terminal action
And Router indicates workflow is complete (no next action available)
```

### Scenario: Router preserves action execution state when resuming

**Steps:**
```gherkin
Given workflow state exists with: current_behavior='story_bot.discovery', current_action='story_bot.discovery.render_output', timestamp='2025-12-03T10:30:00Z'
And completed_actions list contains: [{action_state: 'story_bot.discovery.gather_context', timestamp: '2025-12-03T10:00:00Z'}, {action_state: 'story_bot.discovery.decide_planning_criteria', timestamp: '2025-12-03T10:15:00Z'}]
When Router receives bot tool invocation
Then Router loads workflow state with full state history
And Router extracts current_action='story_bot.discovery.render_output'
And Router preserves completed_actions audit trail
And Router forwards to discovery_bot with parameter action='render_output' and context about previous actions
And User sees that render_output was started but not completed
And User sees audit trail of previously completed actions
```

## Generated Artifacts

### Workflow State File (workflow state)
**Used by:** Router for determining forward target  
**Location:** {project_area}/workflow state  
**Content:**
- current_behavior: Full path to forward to (e.g., story_bot.discovery)
- current_action: Full path to forward to (e.g., story_bot.discovery.build_knowledge)
- completed_actions: Audit trail of all completed actions with full paths
- timestamp: Last update time

## Notes

- Router forwards to behavior tool with action parameter for precise resumption
- ONE behavior tool per behavior routes to specific actions
- Router is fault-tolerant: defaults to first behavior/first action on any error
- Audit trail (completed_actions) provides context for resumed workflows
- Terminal actions (next_action=null) indicate workflow completion
- Full path format (bot.behavior.action) ensures precise routing

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Invoke Bot Tool feature, Domain Concepts (Workflow State, Action Execution State, Auto Resume, State-Based Routing)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria and domain rules in increment 3 exploration document


