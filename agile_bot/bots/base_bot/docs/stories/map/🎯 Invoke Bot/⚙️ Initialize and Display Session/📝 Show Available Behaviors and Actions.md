# 📝 Show Available Behaviors and Actions

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** REPLSession
**Sequential Order:** 2
**Story Type:** system

## Story Description

Show Available Behaviors and Actions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** REPLSession starts with Bot
  **then** REPLSession displays Bot's available Behaviors

- **When** user selects Behavior
  **then** REPLSession displays Behavior's available Actions

- **When** actions are listed
  **then** Actions come from current Behavior

## Scenarios

### Scenario: Show available behaviors and actions (happy_path)

**Steps:**
```gherkin
Given bot has multiple behaviors loaded from bot_config.json
When CLI displays startup menu
Then CLI displays "Behaviors: shape | prioritization | discovery | exploration | scenarios | tests | code"
And CLI displays "Actions: clarify | strategy | build | validate | render"
```

