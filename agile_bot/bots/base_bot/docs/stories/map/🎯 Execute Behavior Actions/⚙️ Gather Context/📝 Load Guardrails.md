# 📝 Load Guardrails

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_gather_context.py#L1261)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Gather Context](.)  
**Sequential Order:** 8
**Story Type:** user

## Story Description

Load Guardrails functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action needs guardrails

  **then** Action loads guardrails from behavior folder

  **and** Guardrails are available for injection

## Scenarios

### Scenario: Guardrails loaded from behavior directory (happy_path)

**Steps:**
```gherkin
GIVEN: Guardrails files exist for action
WHEN: Action loads guardrails
THEN: Guardrails data is available
```

