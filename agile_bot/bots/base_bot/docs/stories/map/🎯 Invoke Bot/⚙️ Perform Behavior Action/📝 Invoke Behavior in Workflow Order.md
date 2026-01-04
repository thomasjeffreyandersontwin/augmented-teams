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

### Scenario: Actions execute in workflow order (happy_path)

**Steps:**
```gherkin
GIVEN: Behavior with workflow order defined
WHEN: Behavior is executed
THEN: Actions run in configured sequence
```

