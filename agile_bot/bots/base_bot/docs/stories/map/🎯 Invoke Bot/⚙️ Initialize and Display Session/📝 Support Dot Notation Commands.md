# 📝 Support Dot Notation Commands

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Initialize and Display Session
**User:** User, AI Agent
**Sequential Order:** 2.6
**Story Type:** user

## Story Description

Support Dot Notation Commands functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters command in format 'behavior.action',
  **then** REPL navigates to specified behavior and action

- **When** user enters command in format 'behavior.action.operation',
  **then** REPL executes specified operation

- **When** user enters invalid behavior in dot notation,
  **then** REPL returns error and state remains unchanged

- **When** user enters invalid action in dot notation,
  **then** REPL returns error and state remains unchanged

- **When** user enters invalid operation in dot notation,
  **then** REPL returns error listing valid operations

## Scenarios

### Scenario: Navigate to behavior and action using dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And all standard behaviors exist
When user enters 'discovery.build'
Then REPL displays 'EXECUTING'
And REPL displays 'discovery.build'
And BehaviorActionState.current_action is updated to 'story_bot.discovery.build'
```


### Scenario: Navigate and execute operation using dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And shape behavior exists with actions
When user enters 'shape.build.instructions' then 'shape.build.submit'
Then REPL displays 'EXECUTING'
And REPL displays 'shape.build.submit'
And BehaviorActionState.current_action is 'story_bot.shape.build'
```


### Scenario: Dot notation with all operations (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And behavior '<behavior>' exists with actions
When user enters '<behavior>.<action>.<operation>'
Then response status is 'success'
And REPL displays '<behavior>.<action>.<operation>'
```

**Examples:**
| behavior | action | operation |
| --- | --- | --- |
| shape | build | instructions |
| discovery | validate | instructions |


### Scenario: Handle invalid behavior in dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And behavior 'invalid' does not exist
When user enters 'invalid.build'
Then REPL displays 'ERROR: Behavior 'invalid' not found'
And BehaviorActionState remains unchanged
```


### Scenario: Handle invalid action in dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
And shape behavior exists with actions [clarify, strategy, build, validate, render]
When user enters 'shape.nonexistent'
Then REPL displays 'ERROR: Action 'nonexistent' not found in behavior 'shape''
And BehaviorActionState remains unchanged
```


### Scenario: Handle invalid operation in dot notation (happy_path)

**Steps:**
```gherkin
Given REPL is at story_bot.shape.clarify
When user enters 'shape.build.invalid'
Then REPL displays 'ERROR: Unknown operation 'invalid''
And REPL displays 'Use: instructions, submit, or confirm'
And BehaviorActionState remains unchanged
```


### Scenario: Batch process all behaviors with dot notation (happy_path)

**Steps:**
```gherkin
Given all 7 behaviors exist (shape, prioritization, discovery, exploration, scenarios, tests, code)
And REPL is at story_bot.shape.clarify
When user enters '<behavior>.render.instructions' for each behavior
Then all 7 commands execute successfully
And BehaviorActionState.current_action ends at 'story_bot.code.render'
```

