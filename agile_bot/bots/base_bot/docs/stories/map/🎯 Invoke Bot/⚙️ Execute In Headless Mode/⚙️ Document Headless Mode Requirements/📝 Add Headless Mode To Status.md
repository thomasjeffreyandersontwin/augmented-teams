# 📝 Add Headless Mode To Status

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** REPL
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Execute In Headless Mode](..) / [⚙️ Document Headless Mode Requirements](.)  
**Sequential Order:** 2
**Story Type:** system

## Story Description

Add Headless Mode To Status functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** AI executes echo 'status' | python repl_main.py
  **then** REPL adds headless mode section to status output
  **and** REPL shows headless mode is available when API key configured
  **and** REPL displays configured API key prefix when available

- **When** Headless mode API key is not configured
  **then** REPL shows headless mode is unavailable when API key not configured
  **and** REPL shows context preparation reminder if headless-context.md missing

- **When** Headless session is running
  **then** REPL displays active session section when headless session is running
  **and** REPL shows session ID in active session section
  **and** REPL shows session status (running) in active session section
  **and** REPL shows log file path in active session section
  **and** REPL shows current iteration count (if available) in active session section
  **and** REPL shows MAX_LOOPS limit (50 iterations) in active session section
  **and** REPL indicates if session is looping (waiting for done/blocked signal) in active session section

- **When** Session is blocked (blocked=true)
  **then** REPL shows blocked state when session is blocked
  **and** REPL displays block reason when session is blocked
  **and** REPL shows recovery attempt count when error recovery is active (up to 3 attempts)

## Scenarios

### Scenario: Show headless mode available in status (happy_path)

**Steps:**
```gherkin
Given REPL is initialized
And headless mode is configured with API key
When user runs status command
Then status display includes headless mode section
And section shows headless mode is available
And section displays configured API key prefix
```


### Scenario: Show active headless session in status (happy_path)

**Steps:**
```gherkin
Given REPL is initialized
And headless session is running with session ID session_abc123
When user runs status command
Then status display includes active session section
And section shows session ID session_abc123
And section shows session status as running
And section shows log file path
```


### Scenario: Show headless mode unavailable in status (happy_path)

**Steps:**
```gherkin
Given REPL is initialized
And headless mode API key is not configured
When user runs status command
Then status display includes headless mode section
And section shows headless mode is unavailable
```

