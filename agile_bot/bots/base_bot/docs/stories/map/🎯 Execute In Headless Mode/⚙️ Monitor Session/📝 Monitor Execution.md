# 📝 Monitor Execution

**Story Type:** system  
**Users:** CLI

## Acceptance Criteria

1. **CLI polls session status during execution:**
   - WHEN Headless session is active
   - THEN CLI streams responses to log file
   - AND CLI maintains full execution transcript
   - AND CLI polls session status periodically
   - AND CLI checks for completion or block signals
   - AND CLI detects block markers in output
   - AND CLI captures block reason when detected
   - AND CLI appends loop iteration number to log file for each loop
   - AND CLI appends instruction sent to log file for each iteration
   - AND CLI appends AI response summary to log file for each iteration
   - AND CLI appends work completed in iteration to log file
   - AND CLI tracks total number of loops executed
   - AND CLI appends total loops count to log file when execution completes

2. **CLI detects completion during monitoring:**
   - WHEN CLI detects completion signal (done=true) from API response
   - THEN CLI stops polling when completion detected
   - AND CLI appends final status to log file when completed
   - AND CLI prepares completion report with log file path

3. **CLI detects blocked state during monitoring:**
   - WHEN CLI detects blocked state (blocked=true) from API response
   - THEN CLI stops polling when blocked detected
   - AND CLI appends block reason to log file when blocked
   - AND CLI prepares blocked report with block reason

## Scenarios

### Scenario: Poll session status during execution

**Steps:**
- Given headless session is running with session ID session_abc123
- And session log file is created at logs/headless-2025-12-29.log
- And this is loop iteration 3
- When CLI polls Cursor Headless API for session status
- Then API returns session status as running
- And API returns progress message Implementing authentication
- And CLI appends loop number 3 to log file
- And CLI appends instruction sent to log file
- And CLI appends AI response summary to log file
- And CLI appends work completed in this iteration to log file
- And CLI continues polling at regular intervals

### Scenario: Detect completion during monitoring

**Steps:**
- Given headless session is running
- And CLI is polling session status
- When API returns session status as completed
- Then CLI stops polling
- And CLI appends final status to log file
- And CLI prepares completion report

### Scenario: Log multiple loop iterations with progress tracking

**Steps:**
- Given headless session is running
- And CLI is executing instruction loop
- When CLI completes loop iteration 1
- Then CLI appends Loop 1 to log file
- And CLI appends instruction sent Keep doing this until 100% done or blocked: Implement authentication
- And CLI appends AI response summary Created user model and login endpoint
- And AI indicates not done
- When CLI completes loop iteration 2
- Then CLI appends Loop 2 to log file
- And CLI appends instruction sent Keep doing this until 100% done or blocked: Implement authentication
- And CLI appends AI response summary Added JWT token generation and validation
- And AI indicates not done
- When CLI completes loop iteration 3
- Then CLI appends Loop 3 to log file
- And CLI appends instruction sent Keep doing this until 100% done or blocked: Implement authentication
- And CLI appends AI response summary Added tests and documentation, authentication complete
- And AI indicates done
- And CLI stops looping (within MAX_LOOPS limit of 50)
- And CLI appends Total loops: 3 to log file

### Scenario: Detect blocked state during monitoring

**Steps:**
- Given headless session is running
- And CLI is polling session status
- When API returns session status as blocked
- And API returns block reason Waiting for API key configuration
- Then CLI stops polling
- And CLI appends block reason to log file
- And CLI prepares blocked report

