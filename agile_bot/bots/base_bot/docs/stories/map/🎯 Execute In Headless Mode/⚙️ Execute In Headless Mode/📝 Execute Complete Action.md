# 📝 Execute Complete Action

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

1. **CLI executes complete action workflow in headless mode:**
   - WHEN Human executes CLI with behavior.action and --headless flag
   - AND Context file exists at docs/context/headless-context.md
   - THEN CLI enables headless execution mode
   - AND CLI reads headless-context.md
   - AND CLI executes instructions operation: constructs "Execute operation: {behavior}.{action}.instructions"
   - AND CLI automatically wraps each operation with "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly." (via instruction preparation)
   - AND CLI sends to Cursor Headless API and loops until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects instructions completion (done=true) or blocked state from API response
   - AND CLI tracks operations_executed list with "instructions"
   - AND CLI executes submit operation: constructs "Execute operation: {behavior}.{action}.submit"
   - AND CLI automatically wraps submit with persistence directive and loops until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects submit completion (done=true) or blocked state from API response
   - AND CLI tracks operations_executed list with "instructions", "submit"
   - AND CLI executes confirm operation: constructs "Execute operation: {behavior}.{action}.confirm"
   - AND CLI automatically wraps confirm with persistence directive and loops until AI indicates done
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects confirm completion (done=true) from API response and marks action_completed=true
   - AND CLI tracks operations_executed list with "instructions", "submit", "confirm"
   - AND CLI appends total loops count to log file when each operation completes
   - AND CLI reports entire action completed successfully

2. **CLI handles block during action workflow:**
   - WHEN CLI detects blocked state (blocked=true) during any operation
   - THEN CLI stops action workflow execution when blocked
   - AND CLI sets blocked_operation to indicate which operation blocked
   - AND CLI sets operations_status to show completed vs blocked operations
   - AND CLI reports which operation blocked
   - AND CLI displays block reason from API response
   - AND CLI preserves completed operation results in operations_executed list
   - AND CLI exits with blocked status code (exit_code=2)

3. **CLI recovers from AI getting stuck during action workflow:**
   - WHEN ErrorRecovery detects recoverable errors (AI stuck/hung, max loops reached, MAX_LOOPS=50) at operation level
   - THEN ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
   - AND ErrorRecovery waits before retry for 2 seconds
   - AND ErrorRecovery terminates current headless session via API
   - AND ErrorRecovery increments recovery attempt count (allows up to 3 attempts)
   - AND ErrorRecovery restarts session for the stuck operation (instructions automatically wrapped with persistence directive)
   - AND ErrorRecovery sends to new Cursor Headless API session
   - AND ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
   - AND AI executes operation with fresh context in new session
   - AND CLI continues with remaining operations in the action after recovery completes
   - AND If max recovery attempts (3) exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"

## Scenarios

### Scenario: Execute complete action workflow in headless mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- And user wants to execute shape.build action
- When human invokes CLI with --headless flag and target shape.build
- Then CLI executes instructions operation: constructs "Execute operation: shape.build.instructions"
- And CLI automatically wraps each operation with "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly." (via instruction preparation)
- And CLI sends to Cursor Headless API and loops until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects instructions completion (done=true) from API response
- And CLI tracks operations_executed list with "instructions"
- And CLI appends total loops count to log file
- And CLI executes submit operation: constructs "Execute operation: shape.build.submit"
- And CLI automatically wraps submit with persistence directive and loops until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects submit completion (done=true) from API response
- And CLI tracks operations_executed list with "instructions", "submit"
- And CLI appends total loops count to log file
- And CLI executes confirm operation: constructs "Execute operation: shape.build.confirm"
- And CLI automatically wraps confirm with persistence directive and loops until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects confirm completion (done=true) from API response and marks action_completed=true
- And CLI tracks operations_executed list with "instructions", "submit", "confirm"
- And CLI appends total loops count to log file
- And CLI reports entire action completed successfully

### Scenario: Handle block during action workflow

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- And user wants to execute shape.build action
- When human invokes CLI with --headless flag and target shape.build
- And instructions operation completes successfully (done=true)
- And submit operation blocks waiting for clarification (blocked=true)
- Then CLI detects blocked state (blocked=true) during submit
- And CLI stops action workflow execution
- And CLI sets blocked_operation to "submit"
- And CLI sets operations_status: {"instructions": "completed", "submit": "blocked"}
- And CLI reports which operation blocked (submit)
- And CLI displays block reason from API response
- And CLI preserves completed operation results in operations_executed=["instructions"]
- And CLI exits with blocked status code (exit_code=2)

### Scenario: Restart session when AI gets stuck during action workflow

**Steps:**
- Given headless session is executing complete action workflow
- And AI is stuck during submit operation (reached MAX_LOOPS limit of 50)
- And RecoverableError indicates AI unable to proceed with message "Max loops (50) reached without completion"
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
- And ErrorRecovery waits before retry for 2 seconds
- And ErrorRecovery terminates current headless session via API
- And ErrorRecovery increments recovery attempt count to 1
- And ErrorRecovery restarts session for the stuck operation only (instructions automatically wrapped with persistence directive)
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
- And AI executes operation with fresh context in new session
- And CLI continues with remaining operations in the action after recovery completes
- And If max recovery attempts (3) exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"
