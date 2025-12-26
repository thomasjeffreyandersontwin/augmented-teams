# 📝 Request Status

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Help
**User:** User
**Sequential Order:** 2
**Story Type:** user

## Story Description

Request Status functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters status command
  **then** REPLSession routes to Bot for status

- **When** Bot receives status request
  **then** Bot reads current BehaviorActionState
  **and** Bot assembles current Behavior, Action, and scope into Result

- **When** REPLSession receives status Result
  **then** REPLSession displays current Behavior and Action

- **When** scope has been set for current Behavior/Action
  **then** REPLSession displays current scope

- **When** no scope has been set
  **then** REPLSession displays "No scope set"

## Scenarios

### Scenario: User requests status display (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And BehaviorActionState.working_directory is "<working_dir>"
And BehaviorActionState.completed_actions are: <completed_actions>
When user enters command: "status"
Then CLI displays "Progress: <behavior>.<action>.<stage>"
And CLI displays "Behaviors:" with current behavior marked [*]
And CLI displays "Actions:" with completed actions marked [OK] and current marked [*]
And CLI displays "Operations:" showing current stage
```

**Examples:**
| behavior | action | working_dir | completed_actions | breadcrumbs |
| --- | --- | --- | --- | --- |
| shape | build | C:\dev\my-project | [clarify,strategy] | [shape] clarify [OK] -> strategy [OK] -> build* -> validate -> render |
| prioritization | clarify | C:\dev\my-project | [] | [prioritization] clarify* -> strategy -> build -> validate -> render |
| discovery | validate | C:\dev\another-proj | [clarify,strategy,build] | [discovery] clarify [OK] -> strategy [OK] -> build [OK] -> validate* -> render |

