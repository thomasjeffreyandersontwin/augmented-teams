# 📝 Validate Rules According To Scope

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Validate Knowledge & Content Against Rules](.)  
**Sequential Order:** 3
**Story Type:** user

## Story Description

Validate Rules According To Scope functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** ValidateRulesAction receives scope parameter

  **then** Action validates only files matching scope

  **and** Action respects test_file, code_file, or knowledge_graph scope

## Scenarios

### Scenario: Validation applies scope filters (happy_path)

**Steps:**
```gherkin
GIVEN: Scope with specific stories or epics
WHEN: Validate action executes
THEN: Only scoped content is validated
```

