# 📝 Display Existing State

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** CLI
**Sequential Order:** 4
**Story Type:** system

## Story Description

Display Existing State functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BehaviorActionState exists,
  **then** CLI displays current position in header Progress line

- **When** state exists,
  **then** CLI displays compact menu with navigation commands

- **When** user types status,
  **then** CLI displays full workflow hierarchy with progress indicators

## Scenarios

### Scenario: CLI displays existing state in header (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState exists
And BehaviorActionState.current_behavior is story_bot.<behavior>
And BehaviorActionState.current_action is story_bot.<behavior>.<action>
And BehaviorActionState.action_phase is <phase>
And BehaviorActionState.working_directory is "C:\dev\project"
And Bot.behaviors contains all behaviors from Background: Bot Configuration
When CLI launches in REPL mode
Then CLI displays header with "STORY_BOT CLI"
And CLI displays "Bot Path: <bot_path>"
And CLI displays "Work Path: C:\dev\project"
And CLI displays "Progress: <behavior>.<action>.<operation>"
And CLI displays compact menu with status, back, current, next, help, exit commands
```

**Examples:**
| behavior | action | phase | operation |
| --- | --- | --- | --- |
| shape | build | instructions_given | instructions |
| discovery | validate | submitted | submit |
| scenarios | clarify | not_started | instructions |

