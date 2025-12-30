# 📝 Surface Block Reason

**Story Type:** user  
**Users:** CLI, Human

## Acceptance Criteria

1. **CLI displays block reason to user:**
   - WHEN Block condition is detected
   - THEN CLI writes block reason to stdout
   - AND CLI writes block reason to log file
   - AND CLI extracts block reason from session log
   - AND CLI formats block reason for console display
   - AND CLI displays blocked status with reason to console (e.g., "Blocked: Waiting for API key configuration")
   - AND CLI shows log file path for details

2. **CLI displays block reason with context:**
   - WHEN Block condition is detected with operation context
   - THEN CLI displays operation context where block occurred (e.g., "submit operation")
   - AND CLI displays block reason
   - AND CLI suggests resolution when applicable
   - AND CLI shows log file path

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

