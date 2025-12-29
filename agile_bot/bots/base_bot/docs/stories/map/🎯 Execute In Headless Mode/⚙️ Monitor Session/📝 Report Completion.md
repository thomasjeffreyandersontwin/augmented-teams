# 📝 Report Completion

**Story Type:** user  
**Users:** CLI, Human

## Acceptance Criteria

*(No acceptance criteria defined yet)*

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

