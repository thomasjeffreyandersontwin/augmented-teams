# 📝 Filter Work Using Files Scope in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 3
**Story Type:** user

## Story Description

Filter Work Using Files Scope in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user sets files scope filter
  **then** CLI displays active scope filters

- **When** user executes validate with active files scope
  **then** CLI displays validation filtered to matched files

- **When** user provides glob pattern for files
  **then** CLI matches files using glob pattern

- **When** user clears files scope
  **then** CLI removes files filter
  **and** displays unfiltered content

## Scenarios

### Scenario: Filter Work Using Files Scope in CLI (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
