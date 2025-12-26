# 📝 Advance To Next Action

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** Bot
**Sequential Order:** 14
**Story Type:** system

## Story Description

Advance To Next Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** current action is confirmed complete
  **then** Bot advances to next action in Behavior

- **When** current action is last in Behavior
  **then** Bot advances to next Behavior's first action

- **When** workflow position changes
  **then** Bot persists updated BehaviorActionState

## Scenarios

### Scenario: Bot advances to next action within same behavior (happy_path)

**Steps:**
```gherkin
Given Bot has current behavior "<behavior>"
And current action is "<current_action>"
And behavior "<behavior>" has actions: clarify, strategy, build, validate, render
When current action is confirmed complete
Then Bot advances to next action "<next_action>" in Behavior
And BehaviorActionState.current_action is updated to "<next_action>"
And BehaviorActionState.completed_actions includes "<current_action>"
```

**Examples:**
| behavior | current_action | next_action |
| --- | --- | --- |
| shape | clarify | strategy |
| shape | strategy | build |
| discovery | build | validate |
| exploration | validate | render |


### Scenario: Bot advances to next behavior when last action is complete (happy_path)

**Steps:**
```gherkin
Given Bot has current behavior "<current_behavior>"
And current action is "render" (last action in behavior)
And bot_config.json has behaviors: shape, prioritization, discovery, exploration, scenarios, tests, code
When render action is confirmed complete
Then Bot advances to next Behavior "<next_behavior>"
And Bot sets current action to "clarify" (first action)
And BehaviorActionState.current_behavior is updated to "<next_behavior>"
And BehaviorActionState.current_action is updated to "clarify"
```

**Examples:**
| current_behavior | next_behavior |
| --- | --- |
| shape | prioritization |
| prioritization | discovery |
| discovery | exploration |
| exploration | scenarios |


### Scenario: Bot persists state after workflow position changes (happy_path)

**Steps:**
```gherkin
Given Bot has current behavior "shape" and action "build"
And behavior_action_state.json exists with current state
When build action is confirmed complete
Then Bot advances to next action "validate"
And Bot persists updated BehaviorActionState to behavior_action_state.json
And behavior_action_state.json contains current_behavior="shape" and current_action="validate"
```

