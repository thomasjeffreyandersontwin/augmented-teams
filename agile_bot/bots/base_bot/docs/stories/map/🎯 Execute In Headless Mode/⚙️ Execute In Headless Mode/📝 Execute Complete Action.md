# 📝 Execute Complete Action

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Execute complete action workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless flag for complete action
- Then CLI executes instructions operation with persistence directive
- And AI loops until instructions operation indicates done
- And CLI detects instructions completion
- And CLI executes submit operation with persistence directive
- And AI loops until submit operation indicates done
- And CLI detects submit completion
- And CLI executes confirm operation with persistence directive
- And AI completes confirmation and indicates done
- And CLI detects confirm completion
- And CLI reports entire action completed successfully

### Scenario: Handle block during action workflow

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user is at shape.build action
- When human invokes CLI with --headless for complete action
- And submit operation blocks waiting for clarification
- Then CLI detects blocked state during submit
- And CLI stops action workflow execution
- And CLI reports which operation blocked
- And CLI displays block reason
- And CLI preserves completed operation results

### Scenario: Restart session when AI gets stuck during action workflow

**Steps:**
- Given headless session is executing complete action workflow
- And AI is stuck during build operation
- And RecoverableError indicates AI unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session for build operation only
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes build with fresh context
- And CLI continues with remaining operations after build completes


- And CLI preserves completed operation results

### Scenario: Restart session when AI gets stuck during action workflow

**Steps:**
- Given headless session is executing complete action workflow
- And AI is stuck during build operation
- And RecoverableError indicates AI unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session for build operation only
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes build with fresh context
- And CLI continues with remaining operations after build completes


- And CLI preserves completed operation results

### Scenario: Restart session when AI gets stuck during action workflow

**Steps:**
- Given headless session is executing complete action workflow
- And AI is stuck during build operation
- And RecoverableError indicates AI unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session for build operation only
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes build with fresh context
- And CLI continues with remaining operations after build completes

