# 📝 Display Current Position in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 3
**Story Type:** system

## Story Description

Display Current Position in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user views status
  **then** CLI displays current behavior, action, and operation

- **When** user navigates to different action
  **then** CLI updates current position display

- **When** displaying position
  **then** CLI shows behavior.action.operation format

- **When** position is at first action
  **then** CLI indicates start of workflow

## Scenarios

### Scenario: User views current position in status (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at <behavior>.<action>.<operation>
WHEN: user enters 'status'
THEN: CLI displays current position
```


### Scenario: Current position updates after navigation (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user navigates to discovery behavior
THEN: CLI updates current position display to show discovery
```

