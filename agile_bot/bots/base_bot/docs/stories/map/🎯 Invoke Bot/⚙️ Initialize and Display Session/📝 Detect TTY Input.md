# 📝 Detect TTY Input

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** CLI
**Sequential Order:** 2
**Story Type:** system

## Story Description

Detect TTY Input functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI starts in STDIO mode,
  **then** it detects if stdin is a TTY

- **When** stdin is TTY,
  **then** CLI enables interactive prompts

- **When** stdin is piped,
  **then** CLI disables interactive prompts

## Scenarios

### Scenario: CLI detects TTY when stdin is a TTY (happy_path)

**Steps:**
```gherkin
Given stdin is a TTY
When CLI checks for TTY
Then CLI enables interactive prompts
```


### Scenario: CLI disables interactive prompts when stdin is piped (happy_path)

**Steps:**
```gherkin
Given stdin is piped (not a TTY)
When CLI checks for TTY
Then CLI disables interactive prompts
```

