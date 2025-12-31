# 📝 Get Action Instructions Through CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

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

### Scenario: Get Action Instructions Through CLI (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
