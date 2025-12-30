# 📝 Add Headless Mode To Status

**Story Type:** system  
**Users:** REPL

## Acceptance Criteria

1. **Status command displays headless mode configuration status:**
   - WHEN AI executes echo 'status' | python repl_main.py
   - THEN REPL adds headless mode section to status output
   - AND REPL shows headless mode is available when API key configured
   - AND REPL displays configured API key prefix when available
   - AND REPL shows headless mode is unavailable when API key not configured
   - AND REPL shows context preparation reminder if headless-context.md missing
   - AND REPL displays active session section when headless session is running
   - AND REPL shows session ID in active session section
   - AND REPL shows session status (running) in active session section
   - AND REPL shows log file path in active session section
   - AND REPL shows current iteration count (if available) in active session section
   - AND REPL shows MAX_LOOPS limit (50 iterations) in active session section
   - AND REPL indicates if session is looping (waiting for done/blocked signal) in active session section
   - AND REPL shows blocked state when session is blocked (blocked=true)
   - AND REPL displays block reason when session is blocked
   - AND REPL shows recovery attempt count when error recovery is active (up to 3 attempts)

## Scenarios

### Scenario: Show headless mode available in status

**Steps:**
- Given REPL is initialized
- And headless mode is configured with API key
- When user runs status command
- Then status display includes headless mode section
- And section shows headless mode is available
- And section displays configured API key prefix

### Scenario: Show active headless session in status

**Steps:**
- Given REPL is initialized
- And headless session is running with session ID session_abc123
- When user runs status command
- Then status display includes active session section
- And section shows session ID session_abc123
- And section shows session status as running
- And section shows log file path
- And section shows current iteration count
- And section shows MAX_LOOPS limit (50 iterations)
- And section indicates if session is looping (waiting for done/blocked signal)

### Scenario: Show headless mode unavailable in status

**Steps:**
- Given REPL is initialized
- And headless mode API key is not configured
- When user runs status command
- Then status display includes headless mode section
- And section shows headless mode is unavailable

### Scenario: Show blocked headless session in status

**Steps:**
- Given REPL is initialized
- And headless session is running
- And headless session becomes blocked (blocked=true) waiting for user input
- When user runs status command
- Then status display includes active session section
- And section shows session status as blocked
- And section displays block reason
- And section shows recovery attempt count if error recovery is active

### Scenario: Show completed headless session in status

**Steps:**
- Given REPL is initialized
- And headless session has completed successfully (done=true)
- When user runs status command
- Then status display shows session completion status
- And status accurately reflects no active session

