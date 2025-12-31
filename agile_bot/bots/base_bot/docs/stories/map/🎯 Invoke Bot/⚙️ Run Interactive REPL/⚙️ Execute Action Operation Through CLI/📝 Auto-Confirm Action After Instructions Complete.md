# 📝 Auto-Confirm Action After Instructions Complete

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 5
**Story Type:** system

## Story Description

Auto-Confirm Action After Instructions Complete functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action has auto-confirm enabled
  **then** CLI automatically runs confirm after displaying instructions

- **When** auto-confirm triggers
  **then** CLI displays instructions
  **and** confirm output without user prompt

- **When** action does not have auto-confirm
  **then** CLI waits for manual confirm command

- **When** auto-confirm completes
  **then** CLI displays confirmation output
  **and** waits for user input

## Scenarios

### Scenario: Auto-Confirm Action After Instructions Complete (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
