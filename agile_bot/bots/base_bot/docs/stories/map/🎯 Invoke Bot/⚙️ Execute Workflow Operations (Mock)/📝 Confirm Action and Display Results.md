# 📝 Confirm Action and Display Results

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 13
**Story Type:** user

## Story Description

Confirm Action and Display Results functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters confirm command
  **then** REPLSession routes to Bot

- **When** Bot receives confirm
  **then** Bot delegates to current Action for confirmation
  **and** Action validates and confirms work

- **When** confirmation succeeds
  **then** Bot returns Result with next action info to REPLSession for display
  **and** Bot navigates to next action and returns instructions
  **and** REPLSession returns result for display

## Scenarios

### Scenario: User confirms action and advances to next action (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<current_action>"
And user has submitted work for current action
When user enters command: "confirm"
Then REPLSession routes confirm command to Bot
And Bot delegates to <current_action>.confirm with ActionContext
And Action validates and confirms work
And Bot marks "<current_action>" as complete in BehaviorActionState
And Bot advances to next action "<next_action>"
And Bot returns Result with next action info
And REPLSession displays "<current_action> confirmed. Next: <next_action>"
And REPLSession displays instructions for "<next_action>"
```

**Examples:**
| behavior | current_action | next_action |
| --- | --- | --- |
| shape | clarify | strategy |
| shape | strategy | build |
| shape | build | validate |
| shape | validate | render |


### Scenario: User confirms last action in behavior and advances to next behavior (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "shape" and action is "render"
And user has submitted work for render action
When user enters command: "confirm"
Then Bot marks "render" as complete in BehaviorActionState
And Bot advances to next behavior "prioritization"
And Bot sets current action to "clarify"
And REPLSession displays "shape.render confirmed. Next: prioritization.clarify"
And REPLSession displays instructions for prioritization.clarify
```

