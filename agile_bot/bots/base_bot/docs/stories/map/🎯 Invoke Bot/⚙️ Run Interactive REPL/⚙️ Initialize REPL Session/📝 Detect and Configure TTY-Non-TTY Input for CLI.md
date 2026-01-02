# 📝 Detect and Configure TTY/Non-TTY Input for CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_initialize_repl_session.py#L263)

**User:** TTYDetector
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Initialize REPL Session](.)  
**Sequential Order:** 4
**Story Type:** system

## Story Description

Detect and Configure TTY/Non-TTY Input for CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: TTYDetector identifies interactive terminal (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_initialize_repl_session.py#L266)

**Steps:**
```gherkin
GIVEN: stdin is connected to a TTY terminal
WHEN: TTYDetector.is_interactive() is called
THEN: TTYDetector returns True
```


### Scenario: TTYDetector identifies piped input (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_initialize_repl_session.py#L294)

**Steps:**
```gherkin
GIVEN: stdin is piped from another process
WHEN: TTYDetector.is_interactive() is called
THEN: TTYDetector returns False
```

