# 📝 Add Headless Mode To Help

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** REPL
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Execute In Headless Mode](..) / [⚙️ Document Headless Mode Requirements](.)  
**Sequential Order:** 1
**Story Type:** system

## Story Description

Add Headless Mode To Help functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** AI executes echo 'help' | python repl_main.py
  **then** REPL adds headless mode section to main_help output
  **and** REPL explains --headless flag purpose
  **and** REPL explains context file requirement (docs/context/headless-context.md)
  **and** REPL lists required context content (user message, chat history, file references)

- **When** REPL displays headless mode section
  **then** REPL shows headless command format with --headless flag
  **and** REPL shows --message parameter usage
  **and** REPL documents CURSOR_API_KEY environment variable requirement
  **and** REPL provides example: echo 'shape.build.instructions --headless' | python repl_main.py
  **and** REPL includes example command with headless flag

- **When** REPL documents headless mode behavior
  **then** REPL explains persistence directive: "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly."
  **and** REPL documents MAX_LOOPS limit of 50 iterations per operation
  **and** REPL explains looping behavior: CLI loops instructions until AI indicates done (done=true) or blocked (blocked=true)
  **and** REPL documents error recovery: up to 3 recovery attempts when AI gets stuck

- **When** Headless mode API key is not configured
  **then** REPL indicates headless mode is unavailable when API key not configured
  **and** REPL explains configuration requirement when unavailable

## Scenarios

### Scenario: Display headless mode documentation in help (happy_path)

**Steps:**
```gherkin
Given REPL is initialized
And headless mode is configured with API key
When user runs help command
Then help output includes headless mode section
And section explains --headless flag purpose
And section shows --message parameter usage
And section includes example command with headless flag
```


### Scenario: Show headless mode unavailable when not configured (happy_path)

**Steps:**
```gherkin
Given REPL is initialized
And headless mode API key is not configured
When user runs help command
Then help output includes headless mode section
And section indicates headless mode is unavailable
And section explains configuration requirement
```

