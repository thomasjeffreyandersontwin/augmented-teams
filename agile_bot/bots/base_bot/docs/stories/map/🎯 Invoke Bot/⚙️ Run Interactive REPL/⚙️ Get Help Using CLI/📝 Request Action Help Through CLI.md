# 📝 Request Action Help Through CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_get_help_using_cli_current.py#L69)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Get Help Using CLI](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Request Action Help Through CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters help command
  **then** CLI displays available commands
  **and** their descriptions

- **When** user requests help for specific action
  **then** CLI displays detailed help for that action

- **When** displaying help
  **then** CLI shows command syntax
  **and** parameter descriptions

- **When** help is requested for non-existent command
  **then** CLI displays error message with available commands

## Scenarios

### Scenario: User views all available commands (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_get_help_using_cli_current.py#L72)

**Steps:**
```gherkin
GIVEN: CLI is running
WHEN: user enters 'help'
THEN: CLI displays help menu with commands
```

