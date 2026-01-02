# 📝 Handle Operation Errors and Validation in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L489)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 7
**Story Type:** system

## Story Description

Handle Operation Errors and Validation in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User enters invalid scope format with instructions (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L492)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'shape.build.instructions scope="invalid{format}"'
THEN: CLI displays error message with valid formats
```

