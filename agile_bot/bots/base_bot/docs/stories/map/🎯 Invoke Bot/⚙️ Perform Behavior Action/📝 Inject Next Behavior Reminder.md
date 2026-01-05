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

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: Next behavior reminder injected when final action (happy_path)

**Steps:**
```gherkin
Given validate is the final action in behavior workflow
And bot_config.json defines behavior sequence
When validate action executes
Then base_instructions include next behavior reminder
And reminder contains next behavior name and prompt text
```


### Scenario: Next behavior reminder not injected when not final action (happy_path)

**Steps:**
```gherkin
Given validate is NOT the final action (render comes after)
And bot_config.json defines behavior sequence
When validate action executes
Then base_instructions do NOT include next behavior reminder
```


### Scenario: Next behavior reminder not injected when no next behavior (happy_path)

**Steps:**
```gherkin
Given discovery is the last behavior in bot_config.json
And render is the final action
When render action executes
Then base_instructions do NOT include next behavior reminder
```

