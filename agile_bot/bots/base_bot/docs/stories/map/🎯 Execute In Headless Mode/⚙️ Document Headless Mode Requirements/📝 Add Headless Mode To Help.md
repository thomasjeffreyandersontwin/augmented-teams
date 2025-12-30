# 📝 Add Headless Mode To Help

**Story Type:** system  
**Users:** REPL

## Acceptance Criteria

1. **Help command displays headless mode section when configured:**
   - WHEN AI executes echo 'help' | python repl_main.py
   - THEN REPL adds headless mode section to main_help output
   - AND REPL explains --headless flag purpose
   - AND REPL explains context file requirement (docs/context/headless-context.md)
   - AND REPL lists required context content (user message, chat history, file references)
   - AND REPL shows headless command format with --headless flag
   - AND REPL shows --message parameter usage
   - AND REPL documents CURSOR_API_KEY environment variable requirement
   - AND REPL provides example: echo 'shape.build.instructions --headless' | python repl_main.py
   - AND REPL includes example command with headless flag
   - AND REPL explains persistence directive: "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly."
   - AND REPL documents MAX_LOOPS limit of 50 iterations per operation
   - AND REPL explains looping behavior: CLI loops instructions until AI indicates done (done=true) or blocked (blocked=true)
   - AND REPL documents error recovery: up to 3 recovery attempts when AI gets stuck
   - AND REPL indicates headless mode is unavailable when API key not configured
   - AND REPL explains configuration requirement when unavailable

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
- And section explains persistence directive: "Keep doing this until 100% done or blocked:" and "If blocked, report reason clearly."
- And section documents MAX_LOOPS limit of 50 iterations per operation
- And section explains looping behavior until done or blocked
- And section documents error recovery mechanisms (up to 3 attempts)

### Scenario: Show headless mode unavailable when not configured

**Steps:**
- Given REPL is initialized
- And headless mode API key is not configured
- When user runs help command
- Then help output includes headless mode section
- And section indicates headless mode is unavailable
- And section explains configuration requirement

