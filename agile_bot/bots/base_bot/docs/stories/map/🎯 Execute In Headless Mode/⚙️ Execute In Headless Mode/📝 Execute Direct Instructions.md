# 📝 Execute Direct Instructions

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Execute direct message in headless mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- When human invokes CLI with --headless flag and --message Implement user authentication
- Then CLI reads headless-context.md file
- And CLI prepends message before context content
- And CLI wraps instructions with Keep doing this until 100% done or blocked directive
- And CLI sends combined instructions to Cursor Headless API
- And CLI creates timestamped log file in logs directory
- And AI executes instruction and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI continues work and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI completes work and indicates done
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports success with log file path

### Scenario: Execute direct message without context file

**Steps:**
- Given headless mode is configured with API key
- And headless-context.md file does not exist
- When human invokes CLI with --headless flag and --message Run tests
- Then CLI wraps message with Keep doing this until 100% done or blocked directive
- And CLI sends message to Cursor Headless API
- And CLI creates timestamped log file
- And AI executes instruction and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI completes tests and indicates done
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports success with log file path

### Scenario: Handle blocked execution in direct message mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- When human invokes CLI with --headless and --message Deploy application
- And headless session blocks waiting for user input
- Then CLI detects blocked state from API response
- And CLI writes block reason to log file
- And CLI reports blocked status to console
- And CLI displays block reason from session
- And CLI exits with blocked status code

### Scenario: Restart session when AI gets stuck in direct message mode

**Steps:**
- Given headless session is executing direct message
- And AI has looped instructions multiple times
- And RecoverableError indicates AI stuck or unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same message and context
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes with fresh context
- And CLI continues monitoring new session


### Scenario: Handle blocked execution in direct message mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- When human invokes CLI with --headless and --message Deploy application
- And headless session blocks waiting for user input
- Then CLI detects blocked state from API response
- And CLI writes block reason to log file
- And CLI reports blocked status to console
- And CLI displays block reason from session
- And CLI exits with blocked status code

### Scenario: Restart session when AI gets stuck in direct message mode

**Steps:**
- Given headless session is executing direct message
- And AI has looped instructions multiple times
- And RecoverableError indicates AI stuck or unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same message and context
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes with fresh context
- And CLI continues monitoring new session


### Scenario: Handle blocked execution in direct message mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- When human invokes CLI with --headless and --message Deploy application
- And headless session blocks waiting for user input
- Then CLI detects blocked state from API response
- And CLI writes block reason to log file
- And CLI reports blocked status to console
- And CLI displays block reason from session
- And CLI exits with blocked status code

### Scenario: Restart session when AI gets stuck in direct message mode

**Steps:**
- Given headless session is executing direct message
- And AI has looped instructions multiple times
- And RecoverableError indicates AI stuck or unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same message and context
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes with fresh context
- And CLI continues monitoring new session

