# 📝 Loop Back To Display State

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** REPLSession
**Sequential Order:** 15
**Story Type:** system

## Story Description

Loop Back To Display State functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** command execution completes
  **then** REPLSession gets state from Bot
  **and** REPLSession displays current position
  **and** REPLSession shows status before prompt
  **and** REPLSession awaits next user input

## Scenarios

### Scenario: REPLSession loops back to display state after command execution (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<action>"
And user has executed command "<command>"
When command execution completes
Then REPLSession gets state from Bot
And REPLSession displays current position: "<behavior>.<action>"
And REPLSession shows status with completed actions marked [OK]
And REPLSession displays prompt "> " awaiting next user input
```

**Examples:**
| behavior | action | command |
| --- | --- | --- |
| shape | build | instructions |
| shape | validate | submit |
| discovery | clarify | help |
| exploration | render | status |


### Scenario: REPLSession shows updated state after confirm advances workflow (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "shape" and action is "build"
And user has executed command "confirm"
When command execution completes and workflow advances to "validate"
Then REPLSession gets updated state from Bot
And REPLSession displays current position: "shape.validate"
And REPLSession shows "build" marked [OK] in status
And REPLSession displays instructions for "validate"
And REPLSession displays prompt "> " awaiting next user input
```


### Scenario: REPLSession displays error and loops back after failed command (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "shape" and action is "build"
And user has executed command "unknown_command"
When command execution fails with error
Then REPLSession displays error: "Unknown command: unknown_command"
And REPLSession gets state from Bot (unchanged)
And REPLSession displays current position: "shape.build"
And REPLSession displays prompt "> " awaiting next user input
```

