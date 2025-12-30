# 📝 Execute Single Operation

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

1. **CLI executes instructions operation in headless mode:**
   - WHEN Human executes CLI with behavior.action.operation and --headless flag
   - AND Context file exists at docs/context/headless-context.md
   - THEN CLI enables headless execution mode
   - AND CLI loads CURSOR_API_KEY from environment
   - AND CLI validates API key is present
   - AND CLI creates timestamped log file path (e.g., logs/headless-2025-12-30-00-31-34.log)
   - AND CLI constructs message "Execute operation: {behavior}.{action}.{operation}" (e.g., "Execute operation: shape.build.instructions")
   - AND CLI loads headless-context.md content when available
   - AND CLI constructs instructions starting with the operation message, then appends user intent, chat history, and file references (when available from context file)
   - AND CLI automatically wraps instructions with "Keep doing this until 100% done or blocked:" directive
   - AND CLI automatically appends "If blocked, report reason clearly." to instructions
   - AND CLI sends to Cursor Headless API
   - AND CLI appends session start message to log file with timestamp
   - AND CLI appends full instructions to log file
   - AND CLI appends loop iteration number to log file for each loop (e.g., "Loop 1: Polling...")
   - AND CLI appends AI response status and message to log file for each iteration (e.g., "Loop 1: running - Implementing authentication")
   - AND CLI loops instruction with persistence directive until AI indicates completion or blocked
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects AI completion signal (done=true) or blocked signal (blocked=true) from API response
   - AND CLI stops looping when done or blocked or MAX_LOOPS reached
   - AND CLI appends total loops count to log file when execution completes
   - AND CLI reports operation completion with log path

2. **CLI executes submit operation in headless mode:**
   - WHEN Human executes CLI with behavior.action.submit and --headless flag
   - AND Context file exists at docs/context/headless-context.md
   - THEN CLI enables headless execution mode
   - AND CLI constructs message "Execute operation: {behavior}.{action}.{operation}" (e.g., "Execute operation: shape.build.submit")
   - AND CLI loads headless-context.md content when available
   - AND CLI constructs instructions starting with the operation message, then appends user intent, chat history, and file references (when available from context file)
   - AND CLI automatically wraps instructions with "Keep doing this until 100% done or blocked:" directive
   - AND CLI automatically appends "If blocked, report reason clearly." to instructions
   - AND CLI sends to Cursor Headless API
   - AND CLI appends session start message to log file with timestamp
   - AND CLI appends full instructions to log file
   - AND CLI appends loop iteration number to log file for each loop (e.g., "Loop 1: Polling...")
   - AND CLI appends AI response status and message to log file for each iteration
   - AND CLI loops instruction with persistence directive until AI indicates done or blocked
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects AI completion signal (done=true) or blocked signal (blocked=true) from API response
   - AND CLI stops looping when done or blocked or MAX_LOOPS reached
   - AND CLI appends total loops count to log file when execution completes
   - AND CLI reports data saved successfully

3. **CLI executes confirm operation in headless mode:**
   - WHEN Human executes CLI with behavior.action.confirm and --headless flag
   - AND Context file exists at docs/context/headless-context.md (optional for confirm)
   - THEN CLI enables headless execution mode
   - AND CLI constructs message "Execute operation: {behavior}.{action}.{operation}" (e.g., "Execute operation: shape.build.confirm")
   - AND CLI loads headless-context.md content when available
   - AND CLI constructs instructions starting with the operation message, then appends user intent, chat history, and file references (when available from context file)
   - AND CLI automatically wraps instructions with "Keep doing this until 100% done or blocked:" directive
   - AND CLI automatically appends "If blocked, report reason clearly." to instructions
   - AND CLI sends to Cursor Headless API
   - AND CLI appends session start message to log file with timestamp
   - AND CLI appends full instructions to log file
   - AND CLI appends loop iteration number to log file for each loop
   - AND CLI appends AI response status and message to log file for each iteration
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects AI completion signal (done=true) from API response
   - AND CLI marks action_completed=true when confirm operation completes successfully
   - AND CLI stops looping when done or MAX_LOOPS reached
   - AND CLI appends total loops count to log file when execution completes
   - AND CLI reports action confirmed and moves to next action

4. **CLI recovers from AI getting stuck during single operation:**
   - WHEN ErrorRecovery detects recoverable errors (AI stuck/hung, max loops reached, MAX_LOOPS=50)
   - THEN ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
   - AND ErrorRecovery waits before retry for 2 seconds
   - AND ErrorRecovery terminates current headless session via API
   - AND ErrorRecovery increments recovery attempt count (allows up to 3 attempts)
   - AND ErrorRecovery restarts session with same instructions (instructions automatically wrapped with persistence directive)
   - AND ErrorRecovery sends to new Cursor Headless API session
   - AND ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
   - AND AI executes with fresh context in new session
   - AND CLI continues monitoring new session
   - AND If max recovery attempts exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"

## Scenarios

### Scenario: Execute instructions operation in headless mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- And user wants to execute shape.build.instructions operation
- When human invokes CLI with --headless flag and target shape.build.instructions
- Then CLI constructs message "Execute operation: shape.build.instructions"
- And CLI loads headless-context.md content
- And CLI constructs instructions starting with the operation message, then appends user intent, chat history, and file references (when available from context file)
- And CLI automatically wraps instructions with "Keep doing this until 100% done or blocked:" directive
- And CLI automatically appends "If blocked, report reason clearly." to instructions
- And CLI sends to Cursor Headless API
- And CLI creates timestamped log file in logs directory (e.g., logs/headless-2025-12-30-00-31-34.log)
- And CLI appends session start message to log file with timestamp
- And CLI appends full instructions to log file
- And AI executes instruction and indicates not done (done=false)
- And CLI appends "Loop 1: Polling..." to log file
- And CLI appends "Loop 1: running - Implementing authentication" to log file
- And CLI loops instruction again with persistence directive
- And CLI appends "Loop 2: Polling..." to log file
- And CLI appends "Loop 2: running - Adding tests" to log file
- And AI executes instruction and indicates completion (done=true)
- And CLI appends "Loop 2: completed - All tests passing" to log file
- And CLI appends "Total loops: 2" to log file
- And CLI detects AI completion signal (done=true) from API response
- And CLI stops looping
- And CLI reports operation completion with log path

### Scenario: Execute submit operation in headless mode

**Steps:**
- Given AI has written headless-context.md with submission data
- And headless mode is configured with API key
- And user wants to execute shape.build.submit operation
- When human invokes CLI with --headless flag and target shape.build.submit
- Then CLI constructs message "Execute operation: shape.build.submit"
- And CLI loads headless-context.md content
- And CLI constructs instructions starting with the operation message, then appends user intent, chat history, and file references (when available from context file)
- And CLI wraps with "Keep doing this until 100% done or blocked:" directive
- And CLI appends "If blocked, report reason clearly." to instructions
- And CLI sends to Cursor Headless API
- And AI executes submit and indicates not done (done=false)
- And CLI appends AI response to log file
- And CLI loops instruction again with persistence directive
- And AI completes submission and indicates done (done=true)
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI stops looping
- And CLI reports data saved successfully

### Scenario: Execute confirm operation in headless mode

**Steps:**
- Given headless mode is configured with API key
- And user wants to execute shape.build.confirm operation
- And all required operations (instructions, submit) are complete
- When human invokes CLI with --headless flag and target shape.build.confirm
- Then CLI constructs message "Execute operation: shape.build.confirm"
- And CLI loads headless-context.md content when available
- And CLI constructs instructions starting with the operation message, then appends user intent, chat history, and file references (when available from context file)
- And CLI wraps with "Keep doing this until 100% done or blocked:" directive
- And CLI appends "If blocked, report reason clearly." to instructions
- And CLI sends to Cursor Headless API
- And AI executes confirmation and indicates done (done=true)
- And CLI appends AI response to log file
- And CLI detects AI completion signal
- And CLI marks action_completed=true
- And CLI stops looping
- And CLI reports action confirmed and moves to next action

### Scenario: Restart session when AI gets stuck

**Steps:**
- Given headless session is running
- And AI has looped instructions multiple times (reached MAX_LOOPS limit of 50)
- And RecoverableError indicates AI stuck or unable to proceed with message "Max loops (50) reached without completion"
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
- And ErrorRecovery waits before retry for 2 seconds
- And ErrorRecovery terminates current headless session via API
- And ErrorRecovery increments recovery attempt count to 1
- And ErrorRecovery restarts session with same instructions (instructions automatically wrapped with persistence directive)
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
- And AI executes with fresh context in new session
- And CLI continues monitoring new session
- And If max recovery attempts (3) exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"
