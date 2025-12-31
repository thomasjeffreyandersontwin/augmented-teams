# 📝 Validate Scope Against Story Graph in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 8
**Story Type:** system

## Story Description

Validate Scope Against Story Graph in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user sets scope with story name
  **then** CLI stores scope filter without validation

- **When** user sets scope with epic name
  **then** CLI stores scope filter without validation

- **When** scope is set
  **then** CLI accepts scope
  **and** stores it in state file

- **When** scope is applied to action
  **then** action validates scope against story graph during execution

## Scenarios

### Scenario: Validate Scope Against Story Graph in CLI (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
