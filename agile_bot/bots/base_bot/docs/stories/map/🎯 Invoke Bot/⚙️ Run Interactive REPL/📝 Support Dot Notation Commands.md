# 📝 Support Dot Notation Commands

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Run Interactive REPL
**User:** AI Agent / Human
**Sequential Order:** 11.5
**Story Type:** user

## Story Description

REPL supports dot notation for direct navigation to specific behavior, action, or operation, enabling efficient workflow control without multiple sequential commands.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters command in format `behavior.action`

  **then** REPL navigates to specified behavior and action

  **and** REPL executes instructions operation for that action

  **and** REPL updates behavior_action_state.json with new position

- **When** user enters command in format `behavior.action.operation`

  **then** REPL navigates to specified behavior and action

  **and** REPL executes specified operation (instructions, submit, or confirm)

  **and** REPL updates state accordingly

- **When** user enters invalid behavior name in dot notation

  **then** REPL returns error message specifying behavior not found

  **and** REPL does not change current state

- **When** user enters invalid action name in dot notation

  **then** REPL returns error message specifying action not found

  **and** REPL does not change current state

- **When** user enters invalid operation name in dot notation

  **then** REPL returns error message listing valid operations

  **and** REPL does not execute operation

## Scenarios

### Scenario: Navigate to behavior and action using dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And all standard behaviors exist
When user enters "discovery.build"
Then REPL navigates to discovery behavior
And REPL navigates to build action
And REPL executes build.instructions operation
And behavior_action_state.json updates to current_action="story_bot.discovery.build"
And REPL displays "EXECUTING discovery.build.instructions"
And REPL displays build instructions
```

### Scenario: Navigate and execute specific operation using dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
When user enters "shape.build.submit"
Then REPL navigates to shape.build
And REPL executes submit operation
And behavior_action_state.json updates action_phase="submitted"
And REPL displays "EXECUTING shape.build.submit"
And REPL displays submit acknowledgment
```

### Scenario: Execute multiple dot notation commands in sequence (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And commands are:
  """
  shape.build.instructions
  shape.build.submit
  shape.build.confirm
  status
  """
When commands are executed
Then first command navigates to shape.build and shows instructions
And second command executes submit for shape.build
And third command confirms and advances to shape.strategy
And fourth command shows current position as shape.strategy.instructions
```

### Scenario: Handle invalid behavior in dot notation (error_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And behavior "invalid" does not exist
When user enters "invalid.build"
Then REPL displays "ERROR: Behavior 'invalid' not found"
And behavior_action_state.json remains unchanged
And current position stays at story_bot.shape.clarify
```

### Scenario: Handle invalid action in dot notation (error_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And shape behavior exists with actions [clarify, strategy, build, validate, render]
When user enters "shape.nonexistent"
Then REPL displays "ERROR: Action 'nonexistent' not found in behavior 'shape'"
And behavior_action_state.json remains unchanged
And current position stays at story_bot.shape.clarify
```

### Scenario: Handle invalid operation in dot notation (error_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
When user enters "shape.build.invalid"
Then REPL displays "ERROR: Unknown operation 'invalid'. Use: instructions, submit, or confirm"
And behavior_action_state.json remains unchanged
And current position stays at story_bot.shape.clarify
```

### Scenario: Batch process all behaviors with same action using dot notation (happy_path)

**Steps:**
```gherkin
Given stdin is piped
And all 7 behaviors exist (shape, prioritization, discovery, exploration, scenarios, tests, code)
And commands are:
  """
  shape.render.instructions
  prioritization.render.instructions
  discovery.render.instructions
  exploration.render.instructions
  scenarios.render.instructions
  tests.render.instructions
  code.render.instructions
  """
When commands are executed
Then all 7 commands execute successfully
And each displays render instructions for respective behavior
And state ends at code.render.instructions
```

## Source Material

**Generated:** 2025-12-23
**Context:** Implementation of dot notation command parsing for efficient workflow navigation
**Primary Source:** repl_session.py lines 282-342 implementing dot notation parsing and execution
**Sections Referenced:** Command parsing logic, behavior/action/operation validation, error handling

