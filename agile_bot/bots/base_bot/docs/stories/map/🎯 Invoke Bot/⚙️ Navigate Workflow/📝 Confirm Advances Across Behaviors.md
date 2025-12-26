# 📝 Confirm Advances Across Behaviors

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Navigate Workflow
**User:** User
**Sequential Order:** 9
**Story Type:** user

## Story Description

Confirm Advances Across Behaviors functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user confirms last action of behavior,
  **then** CLI marks behavior complete

- **When** behavior is complete,
  **then** CLI moves to next behavior's first action

- **When** CLI moves to next behavior,
  **then** CLI executes next behavior's first action's instructions

- **When** user confirms last action of last behavior,
  **then** CLI shows workflow complete

## Scenarios

### Scenario: Confirm at last action moves to next behavior (happy_path)

**Steps:**
```gherkin
Given current position is <current_behavior>.render
And <current_behavior>.render is the last action of <current_behavior> behavior
And completed_actions contains [clarify, strategy, build, validate]
And <next_behavior> behavior exists
When user executes 'render' then 'confirm'
Then CLI displays 'EXECUTING <next_behavior>.clarify.instructions'
And BehaviorActionState.current_behavior is updated to 'story_bot.<next_behavior>'
And BehaviorActionState.current_action is updated to 'story_bot.<next_behavior>.clarify'
```

**Examples:**
| current_behavior | next_behavior |
| --- | --- |
| shape | prioritization |
| prioritization | discovery |
| discovery | exploration |
| exploration | scenarios |
| scenarios | tests |
| tests | code |


### Scenario: Confirm at last action marks behavior complete (happy_path)

**Steps:**
```gherkin
Given current position is shape.render
And completed_actions contains [clarify, strategy, build, validate]
And prioritization behavior exists
When user executes 'render' then 'confirm'
Then completed_actions includes 'story_bot.shape.render'
```


### Scenario: Confirm at last behavior shows workflow complete (happy_path)

**Steps:**
```gherkin
Given current position is code.render
And code is the last behavior
And completed_actions contains [clarify, strategy, build, validate]
When user executes 'render' then 'confirm'
Then CLI displays 'COMPLETE'
And CLI displays 'code'
```

