# 📝 Re-execute Current Operation Using CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L455)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 6
**Story Type:** user

## Story Description

Re-execute Current Operation Using CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User re-executes current instructions (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L458)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions (single behavior setup)
WHEN: user enters 'current'
THEN: CLI re-executes current instructions
```

