# 📝 Validate Rules According To Scope

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L2718)

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

