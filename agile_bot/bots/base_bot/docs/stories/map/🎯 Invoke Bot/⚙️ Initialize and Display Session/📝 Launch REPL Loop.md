# 📝 Launch REPL Loop

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** User
**Sequential Order:** 1
**Story Type:** user

## Story Description

Launch REPL Loop functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user runs story_bot --stdio from terminal,
  **then** CLI launches REPL loop

- **When** REPL loop starts,
  **then** CLI loads BehaviorActionState if it exists

- **When** BehaviorActionState exists,
  **then** CLI displays current position from state

- **When** BehaviorActionState does not exist,
  **then** CLI initializes to first behavior/action/operation

## Scenarios

### Scenario: Launch REPL with existing state (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState exists with current_behavior=story_bot.<behavior>
And BehaviorActionState has current_action=story_bot.<behavior>.<action>
And BehaviorActionState has action_phase=<phase>
And BehaviorActionState has working_directory="C:\dev\project"
When user runs command with --stdio flag
Then CLI loads BehaviorActionState
And CLI displays header with "STORY_BOT CLI"
And CLI displays "Bot Path: <bot_path>"
And CLI displays "Work Path: C:\dev\project"
And CLI displays "Progress: <behavior>.<action>.<operation>"
And CLI displays "Behaviors: shape | prioritization | discovery | exploration | scenarios | tests | code"
And CLI displays "Actions: clarify | strategy | build | validate | render"
And CLI displays compact menu with status, back, current, next, help, exit
```

**Examples:**
| behavior | action | phase | operation |
| --- | --- | --- | --- |
| shape | build | instructions_given | instructions |
| discovery | clarify | not_started | instructions |
| scenarios | validate | submitted | submit |


### Scenario: Launch REPL with no state (fresh start) (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState does not exist
And Bot has behaviors loaded from bot_config.json
And first behavior is "shape" with first action "clarify"
When user runs command with --stdio flag
Then CLI initializes BehaviorActionState
And CLI sets current_behavior to story_bot.shape
And CLI sets current_action to story_bot.shape.clarify
And CLI sets action_phase to not_started
And CLI saves BehaviorActionState to behavior_action_state.json
And CLI displays header with "STORY_BOT CLI"
And CLI displays "Bot Path: <bot_path>"
And CLI displays "Work Path: <workspace_path>"
And CLI displays "Progress: shape.clarify.instructions"
And CLI displays "Behaviors: shape | prioritization | discovery | exploration | scenarios | tests | code"
And CLI displays "Actions: clarify | strategy | build | validate | render"
And CLI displays compact menu with status, back, current, next, help, exit
```

**Examples:**
| bot_path | workspace_path |
| --- | --- |
| C:\dev\augmented-teams\agile_bot\bots\story_bot | C:\dev\augmented-teams\agile_bot\bots\base_bot |

