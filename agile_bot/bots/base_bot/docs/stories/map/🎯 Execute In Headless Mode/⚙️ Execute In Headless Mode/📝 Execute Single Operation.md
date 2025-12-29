# 📝 Execute Single Operation

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Execute instructions operation in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for instructions operation
- Then CLI retrieves instructions for shape.build.instructions
- And CLI prepends headless-context.md content to instructions
- And CLI wraps with Keep doing this until 100% done or blocked directive
- And CLI sends to Cursor Headless API
- And AI executes instruction and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI executes instruction and indicates completion
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports operation completion with log path

### Scenario: Execute submit operation in headless mode

**Steps:**
- Given AI has written headless-context.md with submission data
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for submit operation
- Then CLI retrieves submit instructions for shape.build.submit
- And CLI includes submission parameters from context
- And CLI wraps with Keep doing this until 100% done or blocked directive
- And CLI sends to Cursor Headless API
- And AI executes submit and indicates not done
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI completes submission and indicates done
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports data saved successfully

### Scenario: Execute confirm operation in headless mode

**Steps:**
- Given headless mode is configured
- And user is at shape.build action
- And all required operations are complete
- When human invokes CLI with --headless flag for confirm operation
- Then CLI retrieves confirm instructions
- And CLI wraps with Keep doing this until 100% done or blocked directive
- And CLI sends to Cursor Headless API
- And AI executes confirmation and indicates done
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports action confirmed and moves to next action

### Scenario: Restart session when AI gets stuck

**Steps:**
- Given headless session is running
- And AI has looped instructions multiple times
- And RecoverableError indicates AI stuck or unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes with fresh context
- And CLI continues monitoring new session


- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes with fresh context
- And CLI continues monitoring new session


- And ErrorRecovery restarts session with same instructions
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes with fresh context
- And CLI continues monitoring new session

