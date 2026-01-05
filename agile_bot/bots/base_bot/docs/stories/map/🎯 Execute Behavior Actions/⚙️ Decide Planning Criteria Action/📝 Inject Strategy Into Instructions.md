# 📝 Inject Strategy Into Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Decide Planning Criteria Action](.)  
**Sequential Order:** 5
**Story Type:** user

## Story Description

Inject Strategy Into Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Strategy is generated

  **then** Strategy is injected into action instructions

  **and** Instructions include strategy guidance

## Scenarios

### Scenario: Action injects decision criteria and assumptions (happy_path)

**Steps:**
```gherkin
GIVEN: Environment is bootstrapped with strategy guardrails
WHEN: Action injects strategy criteria and assumptions
THEN: Instructions contain strategy criteria and assumptions
```

