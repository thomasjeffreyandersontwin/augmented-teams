# 📝 Close Current Action

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Perform Behavior Action](.)  
**Sequential Order:** 7
**Story Type:** user

## Story Description

Close Current Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: Close current action marks complete and transitions (happy_path)

**Steps:**
```gherkin
Given workflow is at action strategy
And action has NOT been marked complete yet
When user closes current action
Then action is saved to completed_actions
And workflow transitions to next action
And completed_actions count increases
And current action is updated in state file
```


### Scenario: Close action at final action stays at final (happy_path)

**Steps:**
```gherkin
Given workflow is at final action (render)
When user closes final action
Then action is saved to completed_actions
And state stays at final action (no transition)
```


### Scenario: Close final action transitions to next behavior (happy_path)

**Steps:**
```gherkin
Given workflow is at final action
When user closes final action
Then action is marked complete
```


### Scenario: Close action saves to completed actions list (happy_path)

**Steps:**
```gherkin
Given workflow is at an action (clarify)
When user closes action
Then action is in completed_actions list
And completed_actions count is 1
```


### Scenario: Close handles action already completed gracefully (happy_path)

**Steps:**
```gherkin
Given action has already been completed
When user attempts to close already completed action
Then operation completes gracefully
And no duplicate entry added to completed_actions
```


### Scenario: Bot class has close current action method (happy_path)

**Steps:**
```gherkin
Given Bot is initialized
Then Bot has close_current method available
```

