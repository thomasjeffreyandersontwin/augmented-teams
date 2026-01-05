# 📝 Display Active Scope in CLI Status

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 4
**Story Type:** system

## Story Description

Display Active Scope in CLI Status functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user views status with active scope
  **then** CLI displays active scope section

- **When** no scope is active
  **then** CLI displays no active scope filters message

- **When** multiple scope filters are active
  **then** CLI displays all active filters

- **When** scope is cleared
  **then** CLI updates status to show no active scope

## Scenarios

### Scenario: User views active scope in status (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'status'
THEN: CLI displays active scope section
```


### Scenario: Status shows no active scope when cleared (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'status'
THEN: CLI displays 'No active scope filters'
```


### Scenario: Status shows combined scope filters (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at code.validate.instructions
WHEN: user enters 'status'
THEN: CLI displays both knowledge graph and files scope
```

