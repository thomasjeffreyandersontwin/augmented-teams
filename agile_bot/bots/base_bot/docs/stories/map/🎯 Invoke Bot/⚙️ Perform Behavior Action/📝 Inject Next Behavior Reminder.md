# 📝 Inject Next Behavior Reminder

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Perform Behavior Action](.)  
**Sequential Order:** 6
**Story Type:** user

## Story Description

Inject Next Behavior Reminder functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action is final action in behavior

  **then** Next behavior reminder is injected into instructions

- **When** Action is not final action

  **then** Next behavior reminder is NOT injected

## Scenarios

### Scenario: Inject Next Behavior Reminder (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
