# 📝 Report Completion

**Story Type:** user  
**Users:** CLI, Human

## Acceptance Criteria

1. **CLI reports successful completion to console:**
   - WHEN Session completes successfully
   - THEN CLI writes completion status to stdout
   - AND CLI writes log file path
   - AND CLI extracts transcript from session log
   - AND CLI displays "Headless execution completed" to console
   - AND CLI shows summary of work completed
   - AND CLI displays log file path
   - AND CLI exits with success status code

2. **CLI reports completion with operation details:**
   - WHEN Session completes with operation context
   - THEN CLI displays action name that was completed (e.g., "Action completed: shape.build")
   - AND CLI shows files created during execution
   - AND CLI displays log file path
   - AND CLI exits with success status code

## Scenarios

### Scenario: Report successful completion to console

**Steps:**
- Given headless session has completed successfully
- And session log contains execution transcript
- When CLI prepares completion report
- Then CLI extracts transcript from session log
- And CLI displays Headless execution completed to console
- And CLI shows summary of work completed
- And CLI displays log file path logs/headless-2025-12-29.log
- And CLI exits with success status code

### Scenario: Report completion with operation details

**Steps:**
- Given headless session completed shape.build action
- And session log shows story-graph.json was created
- When CLI prepares completion report
- Then CLI displays Action completed: shape.build
- And CLI shows files created story-graph.json
- And CLI displays log file path
- And CLI exits with success status code

