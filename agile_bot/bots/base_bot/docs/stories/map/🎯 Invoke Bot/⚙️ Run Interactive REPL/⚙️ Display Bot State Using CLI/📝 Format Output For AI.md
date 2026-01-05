# 📝 Format Output For AI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

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

### Scenario: Terminal mode uses plain text formatting for separator (happy_path)

**Steps:**
```gherkin
GIVEN: Terminal formatter is created
WHEN: Separator is formatted
THEN: Separator uses equals signs for visibility
```


### Scenario: Terminal mode uses plain text formatting for completed marker (happy_path)

**Steps:**
```gherkin
GIVEN: Terminal formatter is created
WHEN: Completed status marker is formatted
THEN: Marker is plain text [OK]
```


### Scenario: Terminal mode uses plain text formatting for current marker (happy_path)

**Steps:**
```gherkin
GIVEN: Terminal formatter is created
WHEN: Current status marker is formatted
THEN: Marker is plain text [*]
```


### Scenario: Terminal mode uses plain text formatting for pending marker (happy_path)

**Steps:**
```gherkin
GIVEN: Terminal formatter is created
WHEN: Pending status marker is formatted
THEN: Marker is plain text [ ]
```


### Scenario: Terminal mode uses space indentation for list items (happy_path)

**Steps:**
```gherkin
GIVEN: Terminal formatter is created
WHEN: List item is formatted with indent level 2
THEN: Item uses space indentation
```


### Scenario: Terminal mode returns text as is for highlight (happy_path)

**Steps:**
```gherkin
GIVEN: Terminal formatter is created
WHEN: Text is highlighted
THEN: Text is returned as-is
```


### Scenario: Piped mode uses markdown formatting for separator (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: Separator is formatted
THEN: Separator uses heavy line for visibility
```


### Scenario: Piped mode uses markdown formatting for completed checkbox (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: Completed status marker is formatted
THEN: Marker uses markdown bullet with checkbox emoji
```


### Scenario: Piped mode uses markdown formatting for current checkbox (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: Current status marker is formatted
THEN: Marker uses markdown bullet with emoji
```


### Scenario: Piped mode uses markdown formatting for pending checkbox (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: Pending status marker is formatted
THEN: Marker uses markdown bullet with empty checkbox emoji
```


### Scenario: Piped mode uses markdown lists for list items (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: List item is formatted with no indent
THEN: Item uses markdown list syntax
```


### Scenario: Piped mode indents markdown list items (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: List item is formatted with indent level 1
THEN: Item uses indented markdown list
```


### Scenario: Piped mode uses bold for highlight (happy_path)

**Steps:**
```gherkin
GIVEN: Markdown formatter is created
WHEN: Text is highlighted
THEN: Text uses markdown bold
```


### Scenario: Formatter created at session initialization for tty (happy_path)

**Steps:**
```gherkin
GIVEN: REPL session is starting
WHEN: Factory creates formatter for TTY mode
THEN: Factory creates terminal formatter
```


### Scenario: Formatter created for piped mode (happy_path)

**Steps:**
```gherkin
GIVEN: REPL session is starting
WHEN: Factory creates formatter for piped mode
THEN: Factory creates markdown formatter
```


### Scenario: Factory creates terminal formatter when requested (happy_path)

**Steps:**
```gherkin
GIVEN: Factory is available
WHEN: Terminal formatter is explicitly requested
THEN: Factory creates terminal formatter
```


### Scenario: Factory creates markdown formatter when requested (happy_path)

**Steps:**
```gherkin
GIVEN: Factory is available
WHEN: Markdown formatter is explicitly requested
THEN: Factory creates markdown formatter
```

