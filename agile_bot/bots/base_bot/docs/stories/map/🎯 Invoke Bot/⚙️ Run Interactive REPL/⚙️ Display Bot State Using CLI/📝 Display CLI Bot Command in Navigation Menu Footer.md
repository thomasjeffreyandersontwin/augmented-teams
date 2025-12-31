# 📝 Display CLI Bot Command in Navigation Menu Footer

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L681)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 8
**Story Type:** system

## Story Description

Display CLI Bot Command in Navigation Menu Footer functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI displays footer
  **then** CLI shows available navigation commands

- **When** displaying footer
  **then** CLI shows command syntax for navigation and actions

- **When** displaying footer
  **then** CLI includes examples of dot notation commands

- **When** displaying commands
  **then** CLI shows behavior.action.operation format examples

## Scenarios

### Scenario: CLI displays bot command in footer (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L684)

**Steps:**
```gherkin
Given: CLI displays footer
When: CLI renders footer
Then: CLI shows available navigation commands
```

