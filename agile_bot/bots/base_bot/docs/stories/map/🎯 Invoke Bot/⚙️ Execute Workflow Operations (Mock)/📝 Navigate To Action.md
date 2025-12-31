# 📝 Navigate To Action

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 1
**Story Type:** user

## Story Description

Navigate to an action and automatically run instructions. When user navigates to a behavior.action, instructions are automatically executed without requiring a separate instructions command.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user navigates to behavior.action
  **then** CLI automatically runs instructions for that action
  **and** CLI displays formatted instructions response

- **When** action has auto_confirm property set to true
  **then** CLI automatically runs confirm after instructions complete
  **and** CLI advances to next action

## Scenarios

### Scenario: User navigates to action and instructions auto-run (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
When user enters command: "<behavior>.<action>"
Then CLI automatically runs action.instructions() with ActionContext
And CLI displays formatted output with:
  - **INSTRUCTIONS SECTION:** header
  - Instructions content for the action
  - CLI STATUS section with current progress
And CLI returns response with status='success'
```

**Examples:**
| behavior | action |
| --- | --- |
| shape | clarify |
| shape | strategy |
| shape | build |
| prioritization | validate |
| discovery | render |


### Scenario: User navigates to action with auto_confirm enabled (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And action configuration specifies auto_confirm=true
When user enters command: "<behavior>.<action>"
Then CLI automatically runs action.instructions() with ActionContext
And CLI displays instructions output
And CLI automatically runs action.confirm() after instructions complete
And CLI advances to next action
And CLI displays next action instructions
```

**Examples:**
| behavior | action | auto_confirm |
| --- | --- | --- |
| shape | clarify | true |
| shape | strategy | true |
| discovery | clarify | true |


### Scenario: User navigates to action without auto_confirm (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is "shape"
And BehaviorActionState.current_action is "build"
And action configuration specifies auto_confirm=false
When user enters command: "shape.build"
Then CLI automatically runs action.instructions() with ActionContext
And CLI displays instructions output
And CLI waits for user to complete work
And CLI displays "Enter 'confirm' when work is complete"
```

