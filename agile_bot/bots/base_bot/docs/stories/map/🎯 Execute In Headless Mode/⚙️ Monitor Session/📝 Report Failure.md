# 📝 Recover and Report Failures

**Story Type:** user  
**Users:** CLI, Human

## Acceptance Criteria

*(No acceptance criteria defined yet)*

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
- And ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
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
- And ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
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


- And ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
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
- And ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
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


- And ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
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
- And ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
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

