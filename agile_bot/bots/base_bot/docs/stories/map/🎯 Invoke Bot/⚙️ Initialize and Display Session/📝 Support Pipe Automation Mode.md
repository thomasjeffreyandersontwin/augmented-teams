# 📝 Support Pipe Automation Mode

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** AI Agent, Automation Script
**Sequential Order:** 2.5
**Story Type:** system

## Story Description

Support Pipe Automation Mode functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** stdin is piped (not a TTY),
  **then** REPL reads commands without displaying prompts

- **When** commands are piped,
  **then** REPL processes commands sequentially until EOF

- **When** REPL reaches EOF in pipe mode,
  **then** REPL exits silently without 'Exiting REPL...' message

- **When** multiple commands are piped,
  **then** REPL maintains state between commands within single session

## Scenarios

### Scenario: REPL processes piped commands without prompts (happy_path)

**Steps:**
```gherkin
Given stdin is piped (not a TTY)
And BehaviorActionState exists with current_action=story_bot.shape.clarify
When command 'shape' is piped to REPL
Then REPL reads command without displaying '[story_bot] >' prompt
And REPL displays 'EXECUTING' in output
And REPL executes shape.clarify.instructions
And REPL returns shape.clarify.instructions to caller
```


### Scenario: REPL maintains state between piped commands (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And BehaviorActionState exists with current_action=story_bot.shape.clarify
When commands 'shape', 'build', 'submit', 'status' are piped sequentially
Then REPL executes all commands in single session
And state persists between commands
And final status shows current position as shape.build
And BehaviorActionState.current_action is 'story_bot.shape.build'
```


### Scenario: REPL returns all instructions for multiple actions in single behavior (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And BehaviorActionState exists with current_behavior=story_bot.shape
When commands 'shape.clarify', 'shape.strategy', 'shape.build', 'shape.validate', 'shape.render' are piped sequentially
Then REPL executes instructions for each action
And REPL returns clarify instructions
And REPL returns strategy instructions
And REPL returns build instructions
And REPL returns validate instructions
And REPL returns render instructions
And all instructions are returned in single response batch
```


### Scenario: REPL handles EOF gracefully in pipe mode (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And single command 'shape' is piped
When REPL processes command and reaches EOF
Then REPL executes command successfully with status='success'
And REPL displays 'EXECUTING' in output
And REPL exits silently without 'Exiting REPL...' message
```

