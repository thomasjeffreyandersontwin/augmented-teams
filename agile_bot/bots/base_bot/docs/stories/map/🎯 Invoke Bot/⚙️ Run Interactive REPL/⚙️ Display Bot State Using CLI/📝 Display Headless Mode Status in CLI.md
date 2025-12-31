# 📝 Display Headless Mode Status in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L575)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 6
**Story Type:** system

## Story Description

Display Headless Mode Status in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI displays status
  **then** CLI shows headless mode section

- **When** headless mode is configured
  **then** CLI shows headless mode status as Available
  **and** : CLI shows configured API key prefix
  **and** : CLI shows usage examples
  **and** : CLI shows command examples

- **When** headless mode is not configured
  **then** CLI shows headless mode status as unavailable

- **When** active headless session exists
  **then** CLI shows active session section
  **and** : CLI shows session ID
  **and** : CLI shows session status
  **and** : CLI shows log file path

## Scenarios

### Scenario: CLI displays headless mode section when configured (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L447)

**Steps:**
```gherkin
Given: CLI is initialized
And: headless mode is configured with API key
When: user enters 'status'
Then: CLI displays headless mode section
AND: CLI shows 'Headless Mode:' label
AND: CLI shows 'Status: Available (configured)'
AND: CLI shows 'API Key: key_2780b8...' (masked)
AND: CLI shows 'Usage:' section with headless command format
AND: CLI shows 'Examples:' section with example commands
AND: CLI shows subsection separator after headless mode section
```


### Scenario: CLI displays active headless session when running (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L476)

**Steps:**
```gherkin
Given: CLI is initialized
And: headless mode is configured
And: active headless session is running
When: user enters 'status'
Then: CLI displays 'Active Session:' section
AND: CLI shows 'Session ID: 2025-12-30-01-31-17'
AND: CLI shows 'Status: running'
AND: CLI shows 'Log:' with log file path
```

