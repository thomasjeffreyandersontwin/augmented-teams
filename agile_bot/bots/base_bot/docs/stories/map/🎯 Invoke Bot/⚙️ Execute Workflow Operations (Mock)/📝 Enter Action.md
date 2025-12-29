# 📝 Enter Action

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 1
**Story Type:** user

## Story Description

Enter Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters action name,
  **then** CLI executes instructions and displays response

## Scenarios

### Scenario: User executes current action (mock) (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
When user enters command: "<action>" or "<action>.instructions"
Then CLI calls action.instructions() with ActionContext
And CLI displays formatted output with:
  - **INSTRUCTIONS SECTION:** header
  - Instructions content for the action
  - CLI STATUS section with current progress
And CLI returns response with status='success'
```

**Examples:**
| behavior | action | command |
| --- | --- | --- |
| shape | clarify | clarify |
| shape | clarify | clarify.instructions |
| shape | strategy | strategy |
| shape | build | build |
| prioritization | validate | validate |
| discovery | render | render |

