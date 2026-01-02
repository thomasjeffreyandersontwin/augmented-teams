# 📝 Inject Strategy Into Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py#L359)

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

### Scenario: Inject Strategy Into Instructions (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
