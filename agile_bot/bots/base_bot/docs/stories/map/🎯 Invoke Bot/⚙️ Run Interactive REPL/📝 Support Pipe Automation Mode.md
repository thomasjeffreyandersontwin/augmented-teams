# 📝 Support Pipe Automation Mode

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Run Interactive REPL
**User:** AI Agent / Automation Script
**Sequential Order:** 2.5
**Story Type:** system

## Story Description

REPL supports pipe/automation mode for non-interactive use by AI agents and scripts, detecting when stdin is not a TTY and adjusting behavior accordingly.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** stdin is piped (not a TTY)

  **then** REPL reads commands from stdin without displaying prompts

  **and** REPL processes commands sequentially until EOF

  **and** REPL exits silently without "Exiting REPL..." message

  **and** REPL outputs command responses without extra newlines

  **and** REPL maintains state between commands within single session

## Scenarios

### Scenario: REPL processes piped commands without prompts (happy_path)

**Steps:**
```gherkin
Given stdin is piped (not a TTY)
And behavior_action_state.json exists with current_action="story_bot.shape.clarify"
When commands are piped: "shape\nstatus\n"
Then REPL reads first command "shape" without displaying prompt
And REPL executes shape.clarify.instructions
And REPL outputs execution result
And REPL reads second command "status" without displaying prompt
And REPL displays current status
And REPL reaches EOF
And REPL exits silently without "Exiting REPL..." message
And exit code is 0
```

### Scenario: REPL processes batch commands in single session (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And commands file contains:
  """
  shape
  build
  submit
  confirm
  status
  """
When commands are piped from file
Then REPL executes all 5 commands in single session
And state persists between commands
And "shape" navigates to shape.clarify.instructions
And "build" navigates to shape.build.instructions
And "submit" advances to shape.build.submit
And "confirm" advances to shape.strategy.instructions
And "status" shows current position as shape.strategy.instructions
And exit code is 0
```

### Scenario: REPL handles EOF gracefully in pipe mode (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And single command "shape" is piped
When REPL processes command
And REPL reaches EOF after first command
Then REPL executes "shape" command
And REPL exits silently
And no "Exiting REPL..." message is displayed
And exit code is 0
```

### Scenario: Interactive mode still shows prompts when TTY (happy_path)

**Steps:**
```gherkin
Given stdin is a TTY (interactive mode)
And behavior_action_state.json exists
When REPL starts
Then REPL displays "[story_bot] > " prompt
And REPL waits for user input
When user types "shape"
Then REPL executes command
And REPL displays "[story_bot] > " prompt again
When user types "exit"
Then REPL displays "Exiting REPL..." message
And REPL exits
```

## Source Material

**Generated:** 2025-12-23
**Context:** Implementation of pipe/automation mode support for AI agent and script integration
**Primary Source:** repl_main.py lines 116-156 implementing TTY detection and pipe mode handling
**Sections Referenced:** Main REPL loop, TTY detection, command input handling, output formatting

