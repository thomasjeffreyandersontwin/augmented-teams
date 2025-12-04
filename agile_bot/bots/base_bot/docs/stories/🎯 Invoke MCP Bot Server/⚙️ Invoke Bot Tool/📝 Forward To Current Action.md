# 📝 Forward To Current Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Invoke MCP Bot Server
**Feature:** Invoke Bot Tool

## Story Description

Behavior tool forwards invocations to current action within its behavior based on workflow state so that users resume at the correct action within the specific behavior.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Behavior tool receives invocation, **then** Behavior tool loads Workflow State from persistent storage
- **When** Behavior tool loads Workflow State, **then** Behavior tool extracts current_action for this specific behavior from state
- **When** Behavior tool extracts current_action, **then** Behavior tool forwards call to Action[current_action]
- **When** workflow state shows different behavior, **then** Behavior tool sets workflow to current behavior before routing
- **When** workflow state file doesn't exist, **then** Behavior tool defaults to first action

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given Behavior tool is initialized for specific behavior
And Workflow State is persisted to project_area/workflow state
And workflow state contains: current_behavior (full path), current_action (full path), completed_actions[], timestamp
```

## Scenarios

### Scenario: Behavior tool forwards to current action within behavior

**Steps:**
```gherkin
Given a behavior tool for 'discovery' behavior
And workflow state shows: current_behavior='story_bot.discovery', current_action='story_bot.discovery.build_knowledge'
And discovery behavior has ordered actions: gather_context(1), decide_planning_criteria(2), build_knowledge(3), render_output(4), validate_rules(5)
When Behavior tool receives invocation
Then Behavior tool loads workflow state from project_area/workflow state
And Behavior tool extracts current_action='story_bot.discovery.build_knowledge'
And Behavior tool confirms current_behavior matches this behavior ('discovery')
And Behavior tool forwards call to build_knowledge action
And Behavior tool does NOT forward to first action (gather_context)
And User resumes at exact action (build_knowledge) where they left off
```

### Scenario: Behavior tool sets workflow to current behavior when state shows different behavior

**Steps:**
```gherkin
Given a behavior tool for 'exploration' behavior
And workflow state shows: current_behavior='story_bot.discovery', current_action='story_bot.discovery.build_knowledge'
And User explicitly invokes exploration behavior tool
When Behavior tool receives invocation
Then Behavior tool loads workflow state from project_area/workflow state
And Behavior tool detects current_behavior='story_bot.discovery' (different from this behavior)
And Behavior tool updates workflow state to current_behavior='story_bot.exploration'
And Behavior tool defaults to first action='gather_context' for exploration
And Behavior tool forwards call to exploration.gather_context
And Workflow state now reflects exploration behavior
```

### Scenario: Behavior tool defaults to first action when state missing

**Steps:**
```gherkin
Given a behavior tool for 'shape' behavior
And workflow state does NOT exist at project_area/workflow state
When Behavior tool receives invocation
Then Behavior tool attempts to load workflow state
And Behavior tool detects file not found
And Behavior tool defaults to first action='gather_context'
And Behavior tool forwards call to shape.gather_context
And Behavior tool creates initial workflow state with current_behavior='story_bot.shape', current_action='story_bot.shape.gather_context'
```

### Scenario: Behavior tool handles missing current_action field in state

**Steps:**
```gherkin
Given a behavior tool for 'discovery' behavior
And workflow state exists with: current_behavior='story_bot.discovery'
And workflow state is missing current_action field
When Behavior tool receives invocation
Then Behavior tool loads workflow state
And Behavior tool extracts current_behavior='story_bot.discovery'
And Behavior tool confirms current_behavior matches this behavior
And Behavior tool detects missing current_action field
And Behavior tool warns user about incomplete state file (non-blocking)
And Behavior tool defaults to first action of discovery behavior (gather_context)
And Behavior tool forwards call to discovery.gather_context
```

## Generated Artifacts

### Workflow State File (workflow state)
**Used by:** Behavior tool for determining action to forward to  
**Location:** {project_area}/workflow state  
**Content:**
- current_behavior: Full path of current behavior (e.g., story_bot.discovery)
- current_action: Full path of current action (e.g., story_bot.discovery.build_knowledge)
- completed_actions: Audit trail of all completed actions
- timestamp: Last update time

## Notes

- Behavior tool operates at behavior scope, forwarding to actions within that behavior
- If workflow state shows different behavior, behavior tool updates state to current behavior
- Behavior tool is fault-tolerant: defaults to first action on any error
- Full path format (bot.behavior.action) ensures precise routing

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Invoke Bot Tool feature, Domain Concepts (Behavior Tool Routing, Action Execution State)  
**Date Generated:** 2025-12-04  
**Context Note:** Scenarios generated for behavior tool level routing to current action within behavior

