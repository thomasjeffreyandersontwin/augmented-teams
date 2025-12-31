# 📝 Format Output For AI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L366)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 9
**Story Type:** system

## Story Description

Format Output For AI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI detects TTY mode
  **then** CLI uses plain text formatting for output

- **When** CLI detects piped mode
  **then** CLI uses markdown formatting for output

- **When** formatting separators in terminal mode
  **then** CLI uses plain text separators

- **When** formatting separators in piped mode
  **then** CLI uses markdown separators

- **When** formatting status markers
  **then** CLI uses appropriate format for current mode

## Scenarios

### Scenario: Terminal mode uses plain text formatting for separator (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L368)

**Steps:**
```gherkin
Given: Terminal formatter is created
When: Separator is formatted
Then: Separator uses equals signs for visibility
```


### Scenario: Terminal mode uses plain text formatting for completed marker (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L378)

**Steps:**
```gherkin
Given: Terminal formatter is created
When: Completed status marker is formatted
Then: Marker is plain text [OK]
```


### Scenario: Terminal mode uses plain text formatting for current marker (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L388)

**Steps:**
```gherkin
Given: Terminal formatter is created
When: Current status marker is formatted
Then: Marker is plain text [*]
```


### Scenario: Terminal mode uses plain text formatting for pending marker (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L398)

**Steps:**
```gherkin
Given: Terminal formatter is created
When: Pending status marker is formatted
Then: Marker is plain text [ ]
```


### Scenario: Terminal mode uses space indentation for list items (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L408)

**Steps:**
```gherkin
Given: Terminal formatter is created
When: List item is formatted with indent level 2
Then: Item uses space indentation
```


### Scenario: Terminal mode returns text as-is for highlight (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L418)

**Steps:**
```gherkin
Given: Terminal formatter is created
When: Text is highlighted
Then: Text is returned as-is
```


### Scenario: Piped mode uses markdown formatting for separator (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L428)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: Separator is formatted
Then: Separator uses heavy line for visibility
```


### Scenario: Piped mode uses markdown formatting for completed checkbox (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L438)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: Completed status marker is formatted
Then: Marker uses markdown bullet with checkbox emoji
```


### Scenario: Piped mode uses markdown formatting for current checkbox (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L448)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: Current status marker is formatted
Then: Marker uses markdown bullet with emoji
```


### Scenario: Piped mode uses markdown formatting for pending checkbox (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L458)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: Pending status marker is formatted
Then: Marker uses markdown bullet with empty checkbox emoji
```


### Scenario: Piped mode uses markdown lists for list items (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L468)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: List item is formatted with no indent
Then: Item uses markdown list syntax
```


### Scenario: Piped mode indents markdown list items (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L478)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: List item is formatted with indent level 1
Then: Item uses indented markdown list
```


### Scenario: Piped mode uses bold for highlight (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L488)

**Steps:**
```gherkin
Given: Markdown formatter is created
When: Text is highlighted
Then: Text uses markdown bold
```


### Scenario: Formatter created at session initialization for TTY (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L498)

**Steps:**
```gherkin
Given: REPL session is starting
When: Factory creates formatter for TTY mode
Then: Factory creates terminal formatter
```


### Scenario: Formatter created for piped mode (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L506)

**Steps:**
```gherkin
Given: REPL session is starting
When: Factory creates formatter for piped mode
Then: Factory creates markdown formatter
```


### Scenario: Factory creates terminal formatter when requested (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L514)

**Steps:**
```gherkin
Given: Factory is available
When: Terminal formatter is explicitly requested
Then: Factory creates terminal formatter
```


### Scenario: Factory creates markdown formatter when requested (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli.py#L522)

**Steps:**
```gherkin
Given: Factory is available
When: Markdown formatter is explicitly requested
Then: Factory creates markdown formatter
```

