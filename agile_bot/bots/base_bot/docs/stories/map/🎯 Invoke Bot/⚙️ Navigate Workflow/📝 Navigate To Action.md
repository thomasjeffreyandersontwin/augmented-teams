# 📝 Navigate To Action

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Navigate Workflow
**User:** User
**Sequential Order:** 4
**Story Type:** user

## Story Description

Navigate To Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters action name
  **then** REPLSession routes command to Bot

- **When** Bot receives action navigation
  **then** Bot locates Action within current Behavior
  **and** Bot updates BehaviorActionState with new current action

- **When** Action is set as current
  **then** Bot executes Action's instruction operation
  **and** Bot returns Result with instructions

- **When** REPLSession receives Result
  **then** REPLSession displays instructions to user

## Scenarios

### Scenario: User navigates to action within current behavior (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is <current_behavior>
And BehaviorActionState.current_action is <current_action>
And Behavior "<current_behavior>" has actions from Background: Behavior Actions
And BehaviorActionState.completed_actions contains: <completed_actions>
When user enters command: "<target_action>"
Then CLI displays "EXECUTING <current_behavior>.<target_action>.instructions"
And BehaviorActionState.current_action is updated to "story_bot.<current_behavior>.<target_action>"
```

**Examples:**
| current_behavior | current_action | completed_actions | target_action |
| --- | --- | --- | --- |
| shape | clarify | [] | validate |
| shape | build | ["clarify", "strategy"] | validate |
| discovery | validate | ["clarify", "strategy", "build"] | render |
| scenarios | strategy | ["clarify"] | build |


### Scenario: User navigates to invalid action (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is <current_behavior>
And Behavior "<current_behavior>" has actions from Background: Behavior Actions
And user enters command: action <invalid_action>
When CLI processes navigation command
Then CLI responds "ERROR: action '<invalid_action>' not found in behavior '<current_behavior>'"
And CLI displays "Available actions: clarify, strategy, build, validate, render"
And BehaviorActionState.current_action remains unchanged
```

**Examples:**
| current_behavior | invalid_action |
| --- | --- |
| shape | test |
| discovery | invalid |
| code | nonexistent |

