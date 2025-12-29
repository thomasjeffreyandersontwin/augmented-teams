# 📝 Add Headless Mode To Help

**Story Type:** system  
**Users:** REPL

## Acceptance Criteria

*(No acceptance criteria defined yet)*

## Scenarios

### Scenario: Display headless mode documentation in help

**Steps:**
- Given REPL is initialized
- And headless mode is configured with API key
- When user runs help command
- Then help output includes headless mode section
- And section explains --headless flag purpose
- And section shows --message parameter usage
- And section includes example command with headless flag

### Scenario: Show headless mode unavailable when not configured

**Steps:**
- Given REPL is initialized
- And headless mode API key is not configured
- When user runs help command
- Then help output includes headless mode section
- And section indicates headless mode is unavailable
- And section explains configuration requirement

