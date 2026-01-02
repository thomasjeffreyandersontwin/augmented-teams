# 📝 Get Action Instructions Through CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L85)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Get Action Instructions Through CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user navigates to behavior.action.instructions
  **then** CLI displays formatted instructions for that action

- **When** user enters action name only as shortcut
  **then** CLI executes instructions on current behavior's action

- **When** user provides scope parameter with instructions
  **then** CLI displays filtered instructions for specified scope

- **When** user requests clarify action instructions
  **then** CLI displays key questions and required evidence from guardrails

## Scenarios

### Scenario: User gets instructions for build action without scope (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L88)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'shape.build.instructions'
THEN: CLI displays formatted instructions
```


### Scenario: User calls action by name shortcut (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L117)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters just 'build' (action name only)
THEN: CLI executes instructions operation on current behavior's build action
AND: Instructions are formatted as strings, not JSON
```


### Scenario: User gets instructions for build action with scope (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L150)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'shape.build.instructions scope="Story1, Story2"'
THEN: CLI displays filtered instructions for Story1, Story2
```


### Scenario: User gets instructions for clarify action without context (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L179)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'shape.clarify.instructions'
THEN: CLI displays key questions and required evidence from guardrails
```


### Scenario: User calls clarify by name shortcut (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_execute_action_operation_through_cli.py#L207)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters just 'clarify' (action name only)
THEN: CLI executes instructions operation on current behavior's clarify action
```

