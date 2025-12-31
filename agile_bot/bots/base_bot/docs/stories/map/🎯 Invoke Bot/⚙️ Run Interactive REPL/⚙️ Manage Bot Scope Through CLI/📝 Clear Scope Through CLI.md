# 📝 Clear Scope Through CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli_current.py#L133)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 6
**Story Type:** user

## Story Description

Clear Scope Through CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User clears all scope filters (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli_current.py#L136)

**Steps:**
```gherkin
GIVEN: Scope filter is set
WHEN: user enters 'scope clear'
THEN: CLI clears scope filter
```

