# 📝 Provide Story Scope Context For Instructions

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** REPLSession
**Sequential Order:** 8
**Story Type:** system

## Story Description

Provide Story Scope Context For Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user runs instructions command with story scope parameter
  **then** REPLSession gathers story scope parameters from command
  **and** REPLSession parses scope type and values and validates it against Story Scope schema
  **and** REPLSession creates a new Story Scope from the parameters
  **and** REPLSession adds the new Story Scope to the Action Context
  **and** passes the Action Context with Scope to the instruction operation

- **When** validation fails
  **then** REPLSession displays story scope validation errors to user

## Scenarios

### Scenario: Scope filters story graph and passes matching stories to action (happy_path)

**Steps:**
```gherkin
Given story graph contains epic "Run Interactive REPL" with stories: Navigate To Behavior, Navigate To Action, Request Help, Request Status
And story graph contains epic "Execute Behavior Actions" with stories: Confirm Action, Advance To Next
And REPLSession is active with Bot at behavior "shape" action "build"
And user enters command: "instructions --scope '{"type": "<scope_type>", "value": ["<scope_value>"]}'"
When REPLSession processes the command with scope
Then Bot filters story graph using scope type "<scope_type>" and value "<scope_value>"
And Bot returns <matched_count> matching stories: <matched_stories>
And Bot passes filtered stories to build action
And Action receives ActionContext with <matched_count> stories in scope
```

**Examples:**
| scope_type | scope_value | matched_count | matched_stories |
| --- | --- | --- | --- |
| story | Navigate To Behavior | 1 | Navigate To Behavior |
| story | Request Help | 1 | Request Help |
| epic | Run Interactive REPL | 4 | Navigate To Behavior, Navigate To Action, Request Help, Request Status |
| epic | Execute Behavior Actions | 2 | Confirm Action, Advance To Next |


### Scenario: Scope filters by increment returns stories with matching priority (happy_path)

**Steps:**
```gherkin
Given story graph contains stories with priority 10: Start REPL, Exit REPL
And story graph contains stories with priority 11: Provide Context For Instructions, Store Scope Context, Get Instructions and Display
And REPLSession is active with Bot at behavior "scenarios" action "build"
And user enters command: "instructions --scope '{"type": "increment", "value": [11]}'"
When REPLSession processes the command with scope
Then Bot filters story graph for stories with priority 11
And Bot returns 3 matching stories: Provide Context For Instructions, Store Scope Context, Get Instructions and Display
And Bot passes filtered stories to build action
```


### Scenario: Scope with non-existent story returns empty result (happy_path)

**Steps:**
```gherkin
Given story graph contains epic "Run Interactive REPL" with stories: Navigate To Behavior, Navigate To Action
And REPLSession is active with Bot at behavior "shape" action "build"
And user enters command: "instructions --scope '{"type": "story", "value": ["Nonexistent Story"]}'"
When REPLSession processes the command with scope
Then Bot filters story graph using scope type "story" and value "Nonexistent Story"
And Bot returns 0 matching stories
And Bot displays warning: "No stories found matching scope: Nonexistent Story"
```


### Scenario: REPLSession displays validation error for invalid story scope (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And user enters command: "instructions --scope '{"type": "story", "value": []}'"
When REPLSession processes the command
Then REPLSession validates empty value array against Story Scope schema
And validation fails with error: "Story scope requires at least one story name"
And REPLSession displays story scope validation errors to user
```

