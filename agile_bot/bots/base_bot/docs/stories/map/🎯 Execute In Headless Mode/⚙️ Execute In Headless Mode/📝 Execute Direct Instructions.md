# 📝 Execute Direct Instructions

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

1. **CLI executes direct message in headless mode with context file:**
   - WHEN Human executes CLI with --headless and --message parameters
   - AND Context file exists at docs/context/headless-context.md
   - THEN CLI enables headless execution mode
   - AND CLI loads CURSOR_API_KEY from environment
   - AND CLI validates API key is present
   - AND CLI creates timestamped log file path (e.g., logs/headless-2025-12-30-00-31-34.log)
   - AND CLI reads headless-context.md
   - AND CLI loads ExecutionContext from context file (user_message, chat_history, file_references)
   - AND CLI constructs instructions starting with the user message, then appends user intent, chat history, and file references from context
   - AND CLI formats context: User Intent, Chat History, File References
   - AND CLI automatically wraps instructions with "Keep doing this until 100% done or blocked:" directive
   - AND CLI automatically appends "If blocked, report reason clearly." to instructions
   - AND CLI sends combined instructions to Cursor Headless API
   - AND CLI appends session start message to log file with timestamp
   - AND CLI appends full instructions to log file
   - AND CLI appends loop iteration number to log file for each loop (e.g., "Loop 1: Polling...")
   - AND CLI appends AI response status and message to log file for each iteration (e.g., "Loop 1: running - Implementing authentication")
   - AND CLI loops instruction with persistence directive until AI indicates done or blocked
   - AND CLI enforces MAX_LOOPS limit of 50 iterations
   - AND CLI detects AI completion signal (done=true) or blocked signal (blocked=true) from API response
   - AND CLI stops looping when done or blocked or MAX_LOOPS reached
   - AND CLI appends total loops count to log file when execution completes
   - AND CLI reports success with log file path

2. **CLI executes direct message without context file:**
   - WHEN Human executes CLI with --headless and --message parameters
   - AND Context file does not exist at docs/context/headless-context.md
   - THEN CLI enables headless execution mode
   - AND CLI checks for headless-context.md file and finds it doesn't exist
   - AND CLI creates empty ExecutionContext
   - AND CLI automatically wraps message with "Keep doing this until 100% done or blocked:" directive
   - AND CLI automatically appends "If blocked, report reason clearly." to instructions
   - AND CLI sends message to Cursor Headless API
   - AND CLI creates timestamped log file in logs directory (e.g., logs/headless-2025-12-30-00-31-34.log)
   - AND CLI appends session start message to log file with timestamp
   - AND CLI appends full instructions to log file
   - AND CLI appends loop iteration number to log file for each loop (e.g., "Loop 1: Polling...")
   - AND CLI appends AI response status and message to log file for each iteration
   - AND CLI loops instruction with persistence directive until AI indicates done or blocked
   - AND CLI enforces MAX_LOOPS limit of 50 iterations
   - AND CLI detects AI completion signal (done=true) or blocked signal (blocked=true) from API response
   - AND CLI stops looping when done or blocked or MAX_LOOPS reached
   - AND CLI appends total loops count to log file when execution completes
   - AND CLI reports success with log file path

3. **CLI handles blocked execution in direct message mode:**
   - WHEN CLI detects blocked state (blocked=true) from API response
   - THEN CLI writes block reason to log file
   - AND CLI creates ExecutionResult with status='blocked'
   - AND CLI sets block_reason from API response or defaults to 'Waiting for user input'
   - AND CLI reports blocked status to console
   - AND CLI displays block reason from session
   - AND CLI exits with blocked status code (exit_code=2)

4. **CLI recovers from AI getting stuck in direct message mode:**
   - WHEN ErrorRecovery detects recoverable errors (AI stuck/hung, max loops reached, MAX_LOOPS=50)
   - THEN ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
   - AND ErrorRecovery waits before retry for 2 seconds
   - AND ErrorRecovery terminates current headless session via API
   - AND ErrorRecovery increments recovery attempt count (allows up to 3 attempts)
   - AND ErrorRecovery restarts session with same message and context (instructions automatically wrapped with persistence directive)
   - AND ErrorRecovery sends to new Cursor Headless API session
   - AND ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
   - AND AI executes with fresh context in new session
   - AND CLI continues monitoring new session
   - AND If max recovery attempts (3) exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"

## Scenarios

### Scenario: Execute direct message in headless mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- When human invokes CLI with --headless flag and --message "Implement user authentication"
- Then CLI reads headless-context.md file
- And CLI loads ExecutionContext from context file (user_message, chat_history, file_references)
- And CLI constructs instructions starting with the user message "Implement user authentication", then appends user intent, chat history, and file references from context
- And CLI formats context: User Intent, Chat History, File References
- And CLI automatically wraps instructions with "Keep doing this until 100% done or blocked:" directive
- And CLI automatically appends "If blocked, report reason clearly." to instructions
- And CLI sends combined instructions to Cursor Headless API
- And CLI creates timestamped log file in logs directory (e.g., logs/headless-2025-12-30-00-31-34.log)
- And CLI appends session start message to log file with timestamp
- And CLI appends full instructions to log file
- And AI executes instruction and indicates not done (done=false)
- And CLI appends "Loop 1: Polling..." to log file
- And CLI appends "Loop 1: running - Creating user model" to log file
- And CLI loops instruction again with persistence directive
- And CLI enforces MAX_LOOPS limit of 50 iterations
- And AI continues work and indicates not done (done=false)
- And CLI appends "Loop 2: Polling..." to log file
- And CLI appends "Loop 2: running - Adding authentication endpoints" to log file
- And CLI loops instruction again with persistence directive
- And CLI enforces MAX_LOOPS limit of 50 iterations
- And AI completes work and indicates done (done=true)
- And CLI appends "Loop 3: completed - Authentication implemented" to log file
- And CLI appends "Total loops: 3" to log file
- And CLI detects AI completion signal (done=true) from API response
- And CLI stops looping
- And CLI reports success with log file path

### Scenario: Execute direct message without context file

**Steps:**
- Given headless mode is configured with API key
- And headless-context.md file does not exist
- When human invokes CLI with --headless flag and --message "Run tests"
- Then CLI checks for headless-context.md file and finds it doesn't exist
- And CLI creates empty ExecutionContext
- And CLI automatically wraps message with "Keep doing this until 100% done or blocked:" directive
- And CLI automatically appends "If blocked, report reason clearly." to instructions
- And CLI sends message to Cursor Headless API
- And CLI creates timestamped log file in logs directory (e.g., logs/headless-2025-12-30-00-31-34.log)
- And CLI appends session start message to log file with timestamp
- And CLI appends full instructions to log file
- And AI executes instruction and indicates not done (done=false)
- And CLI appends "Loop 1: Polling..." to log file
- And CLI appends "Loop 1: running - Running test suite" to log file
- And CLI loops instruction again with persistence directive
- And CLI enforces MAX_LOOPS limit of 50 iterations
- And AI completes tests and indicates done (done=true)
- And CLI appends "Loop 1: completed - All tests passing" to log file
- And CLI appends "Total loops: 1" to log file
- And CLI detects AI completion signal (done=true) from API response
- And CLI stops looping
- And CLI reports success with log file path

### Scenario: Handle blocked execution in direct message mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- When human invokes CLI with --headless and --message "Deploy application"
- And headless session blocks waiting for user input (blocked=true)
- Then CLI detects blocked state (blocked=true) from API response
- And CLI writes block reason to log file
- And CLI creates ExecutionResult with status='blocked'
- And CLI sets block_reason from API response or defaults to 'Waiting for user input'
- And CLI reports blocked status to console
- And CLI displays block reason from session
- And CLI exits with blocked status code (exit_code=2)
