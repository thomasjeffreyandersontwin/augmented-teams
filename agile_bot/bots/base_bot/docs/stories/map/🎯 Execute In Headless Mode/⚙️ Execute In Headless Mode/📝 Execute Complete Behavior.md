# 📝 Execute Complete Behavior

**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Execute complete behavior workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user wants to execute shape behavior
- When human invokes CLI with --headless flag for complete behavior
- Then CLI executes clarify action with persistence directive
- And AI loops until clarify action indicates done
- And CLI detects clarify completion
- And CLI executes strategy action with persistence directive
- And AI loops until strategy action indicates done
- And CLI detects strategy completion
- And CLI executes build action with persistence directive
- And AI loops until build action indicates done
- And CLI detects build completion
- And CLI executes validate action with persistence directive
- And AI loops until validate action indicates done
- And CLI detects validate completion
- And CLI executes render action with persistence directive
- And AI loops until render action indicates done
- And CLI detects render completion
- And CLI reports entire behavior completed successfully

### Scenario: Handle block during behavior workflow

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user wants to execute shape behavior
- When human invokes CLI with --headless for complete behavior
- And strategy action blocks waiting for decision
- Then CLI detects blocked state during strategy
- And CLI stops behavior workflow execution
- And CLI reports which action blocked
- And CLI displays block reason
- And CLI preserves completed action results

### Scenario: Restart session when AI gets stuck during behavior workflow

**Steps:**
- Given headless session is executing complete behavior workflow
- And AI is stuck during build action
- And RecoverableError indicates AI unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session for build action only
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes build action with fresh context
- And CLI continues with remaining actions after build completes




**Story Type:** user  
**Users:** Human, CLI

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Execute complete behavior workflow in headless mode

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user wants to execute shape behavior
- When human invokes CLI with --headless flag for complete behavior
- Then CLI executes clarify action with persistence directive
- And AI loops until clarify action indicates done
- And CLI detects clarify completion
- And CLI executes strategy action with persistence directive
- And AI loops until strategy action indicates done
- And CLI detects strategy completion
- And CLI executes build action with persistence directive
- And AI loops until build action indicates done
- And CLI detects build completion
- And CLI executes validate action with persistence directive
- And AI loops until validate action indicates done
- And CLI detects validate completion
- And CLI executes render action with persistence directive
- And AI loops until render action indicates done
- And CLI detects render completion
- And CLI reports entire behavior completed successfully

### Scenario: Handle block during behavior workflow

**Steps:**
- Given AI has written headless-context.md
- And headless mode is configured
- And user wants to execute shape behavior
- When human invokes CLI with --headless for complete behavior
- And strategy action blocks waiting for decision
- Then CLI detects blocked state during strategy
- And CLI stops behavior workflow execution
- And CLI reports which action blocked
- And CLI displays block reason
- And CLI preserves completed action results

### Scenario: Restart session when AI gets stuck during behavior workflow

**Steps:**
- Given headless session is executing complete behavior workflow
- And AI is stuck during build action
- And RecoverableError indicates AI unable to proceed
- And ErrorRecovery tracks recovery attempt count less than 3
- When ErrorRecovery determines error is recoverable
- Then ErrorRecovery waits before retry for 1 minute
- And ErrorRecovery terminates current headless session
- And ErrorRecovery restarts session for build action only
- And ErrorRecovery wraps with Keep doing this until 100% done or blocked directive
- And ErrorRecovery sends to new Cursor Headless API session
- And ErrorRecovery tracks recovery attempt count incremented
- And AI executes build action with fresh context
- And CLI continues with remaining actions after build completes

