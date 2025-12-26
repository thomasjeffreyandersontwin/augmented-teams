# 📝 Navigate Within Behavior

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Navigate Workflow
**User:** User
**Sequential Order:** 5
**Story Type:** user

## Story Description

Navigate Within Behavior functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user types next,
  **then** CLI advances to next action and executes instructions

- **When** user types back,
  **then** CLI moves to previous action and executes instructions

- **When** user types current,
  **then** CLI re-executes current operation

- **When** next reaches last action of behavior,
  **then** CLI crosses to next behavior's first action

- **When** back reaches first action of behavior,
  **then** CLI crosses to previous behavior's last action

## Scenarios

### Scenario: User advances with next command (happy_path)

**Steps:**
```gherkin
Given user is at <current_position>
When user types "next"
Then CLI moves to <next_position>
And CLI executes <next_position>
And CLI displays instructions/results to user
```

**Examples:**
| current_position | next_position |
| --- | --- |
| shape.clarify.instructions | shape.strategy.instructions |
| shape.render.confirm | prioritization.clarify.instructions |
| discovery.validate.submit | discovery.validate.confirm |


### Scenario: User moves back with back command (happy_path)

**Steps:**
```gherkin
Given user is at <current_position>
When user types "back"
Then CLI moves to <previous_position>
And CLI executes <previous_position>
And CLI displays instructions/results to user
```

**Examples:**
| current_position | previous_position |
| --- | --- |
| shape.strategy.instructions | shape.clarify.instructions |
| prioritization.clarify.instructions | shape.render.confirm |
| discovery.validate.confirm | discovery.validate.submit |


### Scenario: User re-executes with current command (happy_path)

**Steps:**
```gherkin
Given user is at shape.build.instructions
And user has already seen instructions
When user types "current"
Then CLI re-executes shape.build.instructions
And CLI displays instructions again
```

