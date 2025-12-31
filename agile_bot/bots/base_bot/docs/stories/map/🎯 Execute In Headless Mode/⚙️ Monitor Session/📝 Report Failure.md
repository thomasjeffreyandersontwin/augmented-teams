# 📝 Recover and Report Failures

**Story Type:** user  
**Users:** CLI, Human

## Acceptance Criteria

1. **CLI reports non-recoverable failure to console:**
   - WHEN Session fails or times out
   - THEN CLI writes failure reason to stdout
   - AND CLI writes log file path for debugging
   - AND CLI extracts error message from session log
   - AND CLI displays "Headless execution failed (non-recoverable)" to console
   - AND CLI shows error message details
   - AND NonRecoverableError cannot be retried
   - AND CLI displays log file path for full details
   - AND CLI exits with failure status code

2. **CLI reports non-recoverable API connection failure:**
   - CLI detects API connection failures (e.g., timeout)
   - CLI retries connection up to 3 times
   - NonRecoverableError indicates API connection failure after retries
   - CLI displays "Failed to connect to Cursor Headless API (non-recoverable)" to console
   - CLI shows error details (e.g., "Connection timeout after 30 seconds")
   - NonRecoverableError cannot be retried
   - CLI suggests checking API key configuration
   - CLI exits with failure status code

3. **CLI recovers from AI hang by restarting session:**
   - ErrorRecovery detects AI hang (max loops reached, MAX_LOOPS=50)
   - RecoverableError indicates AI hang
   - ErrorRecovery tracks recovery attempt count less than 3
   - ErrorRecovery logs recovery attempt to log file
   - ErrorRecovery waits before retry for 2 seconds
   - ErrorRecovery terminates current headless session
   - ErrorRecovery restarts session with same instructions
   - ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
   - ErrorRecovery appends "If blocked, report reason clearly." to instructions
   - ErrorRecovery sends to new Cursor Headless API session
   - ErrorRecovery tracks recovery attempt count incremented
   - ErrorRecovery logs session restart reason to log file
   - CLI continues monitoring new session

4. **CLI recovers from AI stuck in planning mode:**
   - ErrorRecovery detects AI stuck in planning mode (max loops reached, MAX_LOOPS=50)
   - RecoverableError indicates AI stuck in planning
   - ErrorRecovery tracks recovery attempt count less than 3
   - ErrorRecovery logs recovery attempt to log file
   - ErrorRecovery waits before retry for 2 seconds
   - ErrorRecovery terminates current headless session
   - ErrorRecovery restarts session with same instructions
   - ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
   - ErrorRecovery appends "If blocked, report reason clearly." to instructions
   - ErrorRecovery sends to new Cursor Headless API session
   - ErrorRecovery tracks recovery attempt count incremented
   - ErrorRecovery logs session restart reason to log file
   - CLI continues monitoring new session

5. **CLI stops after 3 consecutive recovery attempts:**
   - ErrorRecovery enforces max retry limit of 3 attempts
   - When recovery attempt count equals 3, NonRecoverableError indicates max recovery attempts exceeded
   - CLI logs "Maximum recovery attempts (3) reached, treating as non-recoverable" to log file
   - CLI displays "Headless execution failed after 3 recovery attempts" to console
   - CLI shows all recovery attempts made
   - NonRecoverableError cannot be retried
   - CLI displays log file path for full details
   - CLI exits with failure status code

6. **CLI reports non-recoverable failure with partial results:**
   - CLI tracks completed actions during behavior execution
   - CLI tracks failed action with error details
   - CLI displays behavior execution failure with action context (e.g., "Behavior execution failed at strategy action (non-recoverable)")
   - CLI shows completed actions
   - CLI shows failed action with error
   - NonRecoverableError cannot be retried
   - CLI displays log file path
   - CLI exits with failure status code

## Scenarios

### Scenario: Report non-recoverable failure to console

**Steps:**
- Given headless session has failed
- And NonRecoverableError indicates CLI failure
- And session log contains error message File not found: config.json
- When CLI prepares failure report
- Then CLI extracts error message from session log
- And CLI displays Headless execution failed (non-recoverable) to console
- And CLI shows error message File not found: config.json
- And NonRecoverableError cannot be retried
- And CLI displays log file path for full details
- And CLI exits with failure status code

### Scenario: Report non-recoverable API connection failure

**Steps:**
- Given CLI attempts to connect to Cursor Headless API
- And API connection fails with timeout
- And CLI has retried connection 3 times
- And NonRecoverableError indicates API connection failure
- When CLI prepares failure report
- Then CLI displays Failed to connect to Cursor Headless API (non-recoverable) to console
- And CLI shows error details Connection timeout after 30 seconds
- And NonRecoverableError cannot be retried
- And CLI suggests checking API key configuration
- And CLI exits with failure status code

### Scenario: Recover from AI hang by restarting session

**Steps:**
- Given headless session is running
- And AI has not responded for 5 minutes
- And RecoverableError indicates AI hang
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery logs AI hung, attempting recovery (attempt 1 of 3) to log file
- And ErrorRecovery waits before retry for 2 seconds
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery appends "If blocked, report reason clearly." to instructions
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented to 1
- And ErrorRecovery logs Session restarted due to AI hang to log file
- And CLI continues monitoring new session

### Scenario: Recover from AI stuck in planning mode

**Steps:**
- Given headless session is running
- And AI indicates stuck in planning mode
- And RecoverableError indicates AI stuck in planning
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery logs AI stuck in planning, attempting recovery (attempt 1 of 3) to log file
- And ErrorRecovery waits before retry for 2 seconds
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery appends "If blocked, report reason clearly." to instructions
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented to 1
- And ErrorRecovery logs Session restarted due to AI stuck to log file
- And CLI continues monitoring new session

### Scenario: Stop after 3 consecutive recovery attempts

**Steps:**
- Given headless session is running
- And RecoverableError indicates AI hung or stuck
- And ErrorRecovery tracks recovery attempt count equals 3
- And ErrorRecovery has already recovered 3 times in a row
- When ErrorRecovery determines error is recoverable
- And ErrorRecovery enforces max retry limit
- Then NonRecoverableError indicates max recovery attempts exceeded
- And CLI logs Maximum recovery attempts (3) reached, treating as non-recoverable to log file
- And CLI displays Headless execution failed after 3 recovery attempts to console
- And CLI shows all recovery attempts made
- And NonRecoverableError cannot be retried
- And CLI displays log file path for full details
- And CLI exits with failure status code

### Scenario: Report non-recoverable failure with partial results

**Steps:**
- Given headless session was executing shape behavior
- And clarify action completed successfully
- And strategy action failed with validation error
- And NonRecoverableError indicates CLI failure
- When CLI prepares failure report
- Then CLI displays Behavior execution failed at strategy action (non-recoverable)
- And CLI shows completed actions clarify
- And CLI shows failed action strategy with error
- And NonRecoverableError cannot be retried
- And CLI displays log file path
- And CLI exits with failure status code

### Scenario: Recover from AI stuck in planning mode**Steps:**
- Given headless session is running
- And AI indicates stuck in planning mode (reached MAX_LOOPS limit of 50)
- And RecoverableError indicates AI stuck in planning
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery logs AI stuck in planning, attempting recovery (attempt 1 of 3) to log file
- And ErrorRecovery waits before retry for 2 seconds
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery appends "If blocked, report reason clearly." to instructions
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented to 1
- And ErrorRecovery logs Session restarted due to AI stuck to log file
- And CLI continues monitoring new session

### Scenario: Stop after 3 consecutive recovery attempts

**Steps:**
- Given headless session is running
- And RecoverableError indicates AI hung or stuck
- And ErrorRecovery tracks recovery attempt count equals 3
- And ErrorRecovery has already recovered 3 times in a row
- When ErrorRecovery determines error is recoverable
- And ErrorRecovery enforces max retry limit
- Then NonRecoverableError indicates max recovery attempts exceeded
- And CLI logs Maximum recovery attempts (3) reached, treating as non-recoverable to log file
- And CLI displays Headless execution failed after 3 recovery attempts to console
- And CLI shows all recovery attempts made
- And NonRecoverableError cannot be retried
- And CLI displays log file path for full details
- And CLI exits with failure status code

### Scenario: Report non-recoverable failure with partial results**Steps:**
- Given headless session was executing shape behavior
- And clarify action completed successfully
- And strategy action failed with validation error
- And NonRecoverableError indicates CLI failure
- When CLI prepares failure report
- Then CLI displays Behavior execution failed at strategy action (non-recoverable)
- And CLI shows completed actions clarify
- And CLI shows failed action strategy with error
- And NonRecoverableError cannot be retried
- And CLI displays log file path
- And CLI exits with failure status code
