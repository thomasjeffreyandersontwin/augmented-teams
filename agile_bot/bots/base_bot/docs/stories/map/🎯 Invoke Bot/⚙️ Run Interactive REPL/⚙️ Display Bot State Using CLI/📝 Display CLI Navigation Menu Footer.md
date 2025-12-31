# 📝 Display CLI Navigation Menu Footer

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L542)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 5
**Story Type:** system

## Story Description

Display CLI Navigation Menu Footer functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI displays status
  **then** CLI shows footer with available commands

- **When** displaying footer
  **then** CLI lists navigation commands
  **and** action commands

- **When** in terminal mode
  **then** CLI uses plain text formatting for footer

- **When** in piped mode
  **then** CLI uses markdown formatting for footer

## Scenarios

### Scenario: CLI displays commands menu footer (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L545)

**Steps:**
```gherkin
Given: CLI displays status
When: CLI renders commands menu footer
Then: CLI displays Commands section header
AND: CLI shows command list: status | back | current | next | path [dir] | scope [filter] | headless "msg" | help | exit
AND: CLI shows command usage example with echo syntax
AND: CLI shows behaviors list: shape | prioritization | discovery | exploration | scenarios | tests | code
AND: CLI shows actions list: clarify | strategy | build | validate | render
AND: CLI applies section separator after footer
```

