# 📝 Surface Block Reason

**Story Type:** user  
**Users:** CLI, Human

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Display block reason to user

**Steps:**
- Given headless session has blocked
- And session log contains block reason Waiting for API key configuration
- When CLI prepares blocked report
- Then CLI extracts block reason from session log
- And CLI formats block reason for console display
- And CLI displays Blocked: Waiting for API key configuration to console
- And CLI shows log file path for details

### Scenario: Display block reason with context

**Steps:**
- Given headless session has blocked during submit operation
- And session log contains block reason Missing required parameter --data
- When CLI prepares blocked report
- Then CLI displays operation context submit operation
- And CLI displays block reason Missing required parameter --data
- And CLI suggests resolution Check --data parameter
- And CLI shows log file path

