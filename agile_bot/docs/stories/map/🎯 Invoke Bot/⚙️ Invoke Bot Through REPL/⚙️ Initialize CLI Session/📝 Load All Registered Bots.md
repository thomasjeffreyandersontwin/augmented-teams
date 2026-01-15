# 📝 Load All Registered Bots

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Invoke Bot Through REPL](..) / [⚙️ Initialize CLI Session](.)  
**Sequential Order:** 6
**Story Type:** system

## Story Description

Load All Registered Bots functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI initializes
  **then** CLI loads bot from configured bot directory

- **When** bot directory is specified
  **then** CLI loads bot configuration from bot_config.json

- **When** bot config is missing
  **then** CLI displays error message
  **and** exits gracefully

- **When** bot is loaded
  **then** CLI makes bot available for use

## Scenarios

### Scenario: Load All Registered Bots (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
