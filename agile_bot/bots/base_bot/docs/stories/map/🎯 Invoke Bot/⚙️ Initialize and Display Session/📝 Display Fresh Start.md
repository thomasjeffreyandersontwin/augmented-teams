# 📝 Display Fresh Start

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** CLI
**Sequential Order:** 3
**Story Type:** system

## Story Description

Display Fresh Start functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BehaviorActionState does not exist,
  **then** CLI automatically initializes to first behavior/action

- **When** fresh start detected,
  **then** CLI displays Progress with first behavior.action.operation

- **When** user types status command,
  **then** CLI displays full workflow hierarchy

- **When** user navigates workflow,
  **then** BehaviorActionState tracks current position

## Scenarios

### Scenario: User configures workspace in fresh session (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState does not exist
And user enters command: workspace C:\dev\project
When CLI processes workspace command
Then CLI responds "OK workspace=C:\dev\project"
And BehaviorActionState.working_directory is set to "C:\dev\project"
```


### Scenario: CLI auto-initializes on fresh start (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState does not exist
And Bot.behaviors contains all behaviors from Background: Bot Configuration
And first behavior is "shape" with first action "clarify"
When CLI launches in REPL mode
Then CLI initializes BehaviorActionState with story_bot.shape.clarify
And CLI saves state to behavior_action_state.json
And CLI displays "Progress: shape.clarify.instructions"
And CLI displays compact menu: "status", "back", "current", "next", "help", "exit"
```

**Examples:**
| first_behavior | first_action |
| --- | --- |
| shape | clarify |


### Scenario: User views full workflow with status command (happy_path)

**Steps:**
```gherkin
Given CLI has initialized to shape.clarify.instructions
And BehaviorActionState is loaded
When user types "status" command
Then CLI displays "Progress: shape.clarify.instructions"
And CLI displays "Behaviors: shape [*] -> prioritization [ ] -> discovery [ ] -> exploration [ ] -> scenarios [ ] -> tests [ ] -> code [ ]"
And CLI displays "  Actions: clarify [*] -> strategy [ ] -> build [ ] -> validate [ ] -> render [ ]"
And CLI displays "    Operations: instructions [*] -> submit [ ] -> confirm [ ]"
And CLI displays legend "[*] current  [OK] done  [ ] not started"
```

**Examples:**
| current_behavior | current_action | current_operation |
| --- | --- | --- |
| shape | clarify | instructions |

