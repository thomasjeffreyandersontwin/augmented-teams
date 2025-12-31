# 📝 Enforce Mutually Exclusive Scope Types

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 4
**Story Type:** system

## Story Description

Enforce Mutually Exclusive Scope Types functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user sets file scope while story scope is active
  **then** CLI replaces story scope with file scope

- **When** user sets story scope while file scope is active
  **then** CLI replaces file scope with story scope

- **When** checking stored scope
  **then** only one filter type is active

- **When** user clears scope
  **then** CLI removes all scope filters

## Scenarios

### Scenario: Enforce Mutually Exclusive Scope Types (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
