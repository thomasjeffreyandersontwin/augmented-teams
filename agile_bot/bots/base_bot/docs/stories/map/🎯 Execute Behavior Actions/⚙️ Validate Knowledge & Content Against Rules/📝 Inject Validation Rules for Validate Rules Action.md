# 📝 Inject Validation Rules for Validate Rules Action

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Validate Knowledge & Content Against Rules](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Inject Validation Rules for Validate Rules Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** MCP Specific Behavior Action Tool invokes Validate Rules Action

  **then** Action loads common bot rules from base_bot/rules/

  **and** Action loads behavior-specific rules

  **and** Action merges and injects rules into validation section

## Scenarios

### Scenario: Validation rules injected into instructions (happy_path)

**Steps:**
```gherkin
GIVEN: Validation rules exist in guardrails
WHEN: Validate action loads instructions
THEN: Rules are injected into instructions
```

