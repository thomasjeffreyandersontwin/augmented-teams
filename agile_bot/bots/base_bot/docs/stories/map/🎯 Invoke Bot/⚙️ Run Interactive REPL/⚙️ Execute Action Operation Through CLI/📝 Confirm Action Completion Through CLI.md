# 📝 Confirm Action Completion Through CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L331)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 4
**Story Type:** user

## Story Description

Confirm Action Completion Through CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User confirms build action completion (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L334)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'confirm'
THEN: CLI automatically navigates to shape.validate.instructions
```


### Scenario: User confirms clarify action completion (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L362)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'confirm'
THEN: CLI automatically navigates to shape.strategy.instructions
```


### Scenario: User confirms action and advances to next action (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L391)

**Steps:**
```gherkin
GIVEN: CLI is at shape.strategy.instructions
WHEN: user enters 'confirm'
THEN: CLI advances to next action and auto-executes instructions
AND: Does not crash with 'object is not callable' error
```


### Scenario: User confirms from instructions (2-phase model) (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L423)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'confirm'
THEN: CLI advances to next action (valid - 2-phase model: instructions -> confirm)
```

