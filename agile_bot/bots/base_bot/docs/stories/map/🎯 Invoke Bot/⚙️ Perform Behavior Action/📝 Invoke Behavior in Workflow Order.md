# 📝 Invoke Behavior in Workflow Order

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Perform Behavior Action](.)  
**Sequential Order:** 3
**Story Type:** user

## Story Description

Invoke Behavior in Workflow Order functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Behavior is invoked

  **then** Behavior loads workflow order from behavior-specific behavior.json

  **and** Behavior executes actions in configured order

## Scenarios

### Scenario: Invoke Behavior in Workflow Order (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
