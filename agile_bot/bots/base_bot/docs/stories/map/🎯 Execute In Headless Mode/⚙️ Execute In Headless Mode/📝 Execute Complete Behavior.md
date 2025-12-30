# 📝 Execute Complete Behavior

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

1. **CLI executes complete behavior workflow in headless mode:**
   - WHEN Human executes CLI with behavior and --headless flag
   - AND Context file exists at docs/context/headless-context.md
   - THEN CLI enables headless execution mode
   - AND CLI reads headless-context.md
   - AND CLI executes clarify action: runs operations ['instructions', 'submit', 'confirm'] in sequence
   - AND CLI automatically wraps each operation with "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly."
   - AND CLI loops each operation until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects clarify completion (action_completed=true) or blocked state from API response
   - AND CLI tracks actions_executed list with "clarify"
   - AND CLI executes strategy action: runs operations ['instructions', 'submit', 'confirm'] in sequence
   - AND CLI automatically wraps each operation with persistence directive
   - AND CLI loops each operation until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects strategy completion (action_completed=true) or blocked state from API response
   - AND CLI tracks actions_executed list with "clarify", "strategy"
   - AND CLI executes build action: runs operations ['instructions', 'submit', 'confirm'] in sequence
   - AND CLI automatically wraps each operation with persistence directive
   - AND CLI loops each operation until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects build completion (action_completed=true) or blocked state from API response
   - AND CLI tracks actions_executed list with "clarify", "strategy", "build"
   - AND CLI executes validate action: runs operations ['instructions', 'submit', 'confirm'] in sequence
   - AND CLI automatically wraps each operation with persistence directive
   - AND CLI loops each operation until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects validate completion (action_completed=true) or blocked state from API response
   - AND CLI tracks actions_executed list with "clarify", "strategy", "build", "validate"
   - AND CLI executes render action: runs operations ['instructions', 'submit', 'confirm'] in sequence
   - AND CLI automatically wraps each operation with persistence directive
   - AND CLI loops each operation until AI indicates done or blocked
   - AND CLI appends loop iteration numbers and responses to log file for each loop
   - AND CLI enforces MAX_LOOPS limit of 50 iterations per operation
   - AND CLI detects render completion (action_completed=true) or blocked state from API response
   - AND CLI tracks actions_executed list with "clarify", "strategy", "build", "validate", "render"
   - AND CLI appends total loops count to log file when each operation completes
   - AND CLI marks behavior_completed=true when all actions complete
   - AND CLI reports entire behavior completed successfully

2. **CLI handles block during behavior workflow:**
   - WHEN CLI detects blocked state (blocked=true) during any action
   - THEN CLI stops behavior workflow execution when blocked
   - AND CLI sets blocked_action to indicate which action blocked
   - AND CLI sets actions_status to show completed vs blocked actions
   - AND CLI reports which action blocked
   - AND CLI displays block reason from API response
   - AND CLI preserves completed action results in actions_executed list
   - AND CLI exits with blocked status code (exit_code=2)

3. **CLI recovers from AI getting stuck during behavior workflow:**
   - WHEN ErrorRecovery detects recoverable errors (AI stuck/hung, max loops reached, MAX_LOOPS=50) at operation level
   - THEN ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
   - AND ErrorRecovery waits before retry for 2 seconds
   - AND ErrorRecovery terminates current headless session via API
   - AND ErrorRecovery increments recovery attempt count (allows up to 3 attempts)
   - AND ErrorRecovery restarts session for the stuck operation (instructions automatically wrapped with persistence directive)
   - AND ErrorRecovery sends to new Cursor Headless API session
   - AND ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
   - AND AI executes action with fresh context in new session
   - AND CLI continues with remaining actions after recovery completes
   - AND If max recovery attempts (3) exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"

## Scenarios

### Scenario: Execute complete behavior workflow in headless mode

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- And user wants to execute shape behavior
- When human invokes CLI with --headless flag and target shape
- Then CLI executes clarify action: runs operations ['instructions', 'submit', 'confirm'] in sequence
- And CLI automatically wraps each operation with "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly."
- And CLI loops each operation until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects clarify completion (action_completed=true) from API response
- And CLI tracks actions_executed list with "clarify"
- And CLI appends total loops count to log file
- And CLI executes strategy action: runs operations ['instructions', 'submit', 'confirm'] in sequence
- And CLI automatically wraps each operation with persistence directive
- And CLI loops each operation until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects strategy completion (action_completed=true) from API response
- And CLI tracks actions_executed list with "clarify", "strategy"
- And CLI appends total loops count to log file
- And CLI executes build action: runs operations ['instructions', 'submit', 'confirm'] in sequence
- And CLI automatically wraps each operation with persistence directive
- And CLI loops each operation until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects build completion (action_completed=true) from API response
- And CLI tracks actions_executed list with "clarify", "strategy", "build"
- And CLI appends total loops count to log file
- And CLI executes validate action: runs operations ['instructions', 'submit', 'confirm'] in sequence
- And CLI automatically wraps each operation with persistence directive
- And CLI loops each operation until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects validate completion (action_completed=true) from API response
- And CLI tracks actions_executed list with "clarify", "strategy", "build", "validate"
- And CLI appends total loops count to log file
- And CLI executes render action: runs operations ['instructions', 'submit', 'confirm'] in sequence
- And CLI automatically wraps each operation with persistence directive
- And CLI loops each operation until AI indicates done
- And CLI appends loop iteration numbers and responses to log file for each loop
- And CLI enforces MAX_LOOPS limit of 50 iterations per operation
- And CLI detects render completion (action_completed=true) from API response
- And CLI tracks actions_executed list with "clarify", "strategy", "build", "validate", "render"
- And CLI appends total loops count to log file
- And CLI marks behavior_completed=true
- And CLI reports entire behavior completed successfully

### Scenario: Handle block during behavior workflow

**Steps:**
- Given AI has written headless-context.md with user intent and chat history
- And headless mode is configured with API key
- And user wants to execute shape behavior
- When human invokes CLI with --headless flag and target shape
- And clarify action completes successfully (action_completed=true)
- And strategy action blocks waiting for decision (blocked=true)
- Then CLI detects blocked state (blocked=true) during strategy
- And CLI stops behavior workflow execution
- And CLI sets blocked_action to "strategy"
- And CLI sets actions_status: {"clarify": "completed", "strategy": "blocked"}
- And CLI reports which action blocked (strategy)
- And CLI displays block reason from API response
- And CLI preserves completed action results in actions_executed=["clarify"]
- And CLI exits with blocked status code (exit_code=2)

### Scenario: Restart session when AI gets stuck during behavior workflow

**Steps:**
- Given headless session is executing complete behavior workflow
- And AI is stuck during build action operation (reached MAX_LOOPS limit of 50)
- And RecoverableError indicates AI unable to proceed with message "Max loops (50) reached without completion"
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery logs recoverable error with attempt number to log file (e.g., "Recoverable error: Max loops (50) reached without completion. Attempt 1")
- And ErrorRecovery waits before retry for 2 seconds
- And ErrorRecovery terminates current headless session via API
- And ErrorRecovery increments recovery attempt count to 1
- And ErrorRecovery restarts session for build action only (instructions automatically wrapped with persistence directive)
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery allows up to 3 recovery attempts before raising NonRecoverableError
- And AI executes operation with fresh context in new session
- And CLI continues with remaining operations in the action after recovery completes
- And If max recovery attempts (3) exceeded, CLI raises NonRecoverableError with message "Max recovery attempts (3) exceeded"
