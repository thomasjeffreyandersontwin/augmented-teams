# 📝 Confirm Work Through CLI with String Parameters

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L237)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 3
**Story Type:** user

## Story Description

Confirm Work Through CLI with String Parameters functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user confirms build action
  **then** CLI processes work
  **and** advances to next action

- **When** user confirms clarify with answers parameter
  **then** CLI saves clarification data
  **and** advances to next action

- **When** user confirms clarify with evidence parameter
  **then** CLI saves evidence
  **and** advances to next action

- **When** user confirms from instructions phase
  **then** CLI advances to next action using 2-phase model

## Scenarios

### Scenario: User confirms build work (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L240)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'confirm'
THEN: CLI processes work and advances to next action
```


### Scenario: User confirms clarify with answers (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L269)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'confirm' with answers parameter
THEN: CLI saves clarification data and advances to next action
```


### Scenario: User confirms clarify with evidence (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L300)

**Steps:**
```gherkin
GIVEN: CLI is at discovery.clarify.instructions
WHEN: user enters 'confirm' with evidence-provided parameter
THEN: CLI saves evidence and advances to next action
```

