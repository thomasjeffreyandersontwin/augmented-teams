# 📝 Confirm Action and Display Results

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 13
**Story Type:** user

## Story Description

Confirm completed work and advance to the next action. Confirm is the only workflow operation that marks an action as complete - there is no separate submit operation. Some actions have auto_confirm enabled which automatically runs confirm after instructions complete.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters confirm command
  **then** REPLSession routes to Bot

- **When** Bot receives confirm
  **then** Bot delegates to current Action for confirmation
  **and** Action validates and confirms work

- **When** confirmation succeeds
  **then** Bot marks action as complete
  **and** Bot navigates to next action
  **and** Bot automatically runs next action instructions
  **and** REPLSession returns result for display

- **When** action has auto_confirm property set to true
  **then** confirm runs automatically after instructions complete

## Scenarios

### Scenario: User confirms action and advances to next action (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<current_action>"
And user has completed work for current action
When user enters command: "confirm"
Then REPLSession routes confirm command to Bot
And Bot delegates to <current_action>.confirm with ActionContext
And Action validates and confirms work
And Bot marks "<current_action>" as complete in BehaviorActionState
And Bot advances to next action "<next_action>"
And Bot automatically runs <next_action>.instructions
And REPLSession displays formatted output with:
  - **INSTRUCTIONS SECTION:** header
  - Instructions for next action
  - CLI STATUS section showing:
    - Current position: <behavior>.<next_action>.instructions
    - Completed actions marked with checkmarks
    - Current action marked with arrow
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
And user has completed work for render action
When user enters command: "confirm"
Then Bot marks "render" as complete in BehaviorActionState
And Bot advances to next behavior "prioritization"
And Bot sets current action to "clarify"
And Bot automatically runs prioritization.clarify.instructions
And REPLSession displays "shape.render confirmed. Next: prioritization.clarify"
And REPLSession displays instructions for prioritization.clarify
```


### Scenario: Auto-confirm runs after instructions for configured actions (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<action>"
And action configuration specifies auto_confirm=true
When user navigates to "<behavior>.<action>"
Then CLI automatically runs action.instructions()
And CLI displays instructions output
And CLI automatically runs action.confirm() after instructions complete
And Bot marks "<action>" as complete
And Bot advances to next action
And CLI automatically runs next action instructions
```

**Examples:**
| behavior | action | auto_confirm |
| --- | --- | --- |
| shape | clarify | true |
| shape | strategy | true |
| discovery | clarify | true |

