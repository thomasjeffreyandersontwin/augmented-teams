# 📝 Access Actions

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_gather_context.py#L925)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Gather Context](.)  
**Sequential Order:** 6
**Story Type:** user

## Story Description

Access Actions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action needs to access other actions

  **then** Action can access action registry

  **and** Action can retrieve action configurations

## Scenarios

### Scenario: Actions accessible from behavior (happy_path)

**Steps:**
```gherkin
GIVEN: Behavior with actions configured
WHEN: Actions are accessed
THEN: Action list is available
```

