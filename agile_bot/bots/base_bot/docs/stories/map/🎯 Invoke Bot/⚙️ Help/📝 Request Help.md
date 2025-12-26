# 📝 Request Help

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Help
**User:** User
**Sequential Order:** 1
**Story Type:** user

## Story Description

Request Help functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters help command
  **then** REPLSession routes to Bot for help content

- **When** Bot receives general help request
  **then** Bot gathers available commands, Behaviors, and current Behavior's Actions
  **and** Bot returns Result with help overview

- **When** REPLSession receives help Result
  **then** REPLSession displays available commands, Behaviors, and Actions

## Scenarios

### Scenario: User requests help for current behavior (happy_path)

**Steps:**
```gherkin
Given current behavior is <behavior>
And Behavior has actions: <actions>
And user enters command: help
When CLI processes help request
Then CLI displays "Core Commands:"
And CLI displays available behaviors
And CLI displays available actions with descriptions
And CLI displays available operations
And CLI displays navigation commands
```

**Examples:**
| behavior | actions | action | parameters |
| --- | --- | --- | --- |
| shape | ["clarify", "strategy", "build", "validate", "render"] | build | ["--scope <dict>"] |
| discovery | ["clarify", "strategy", "build", "validate", "render"] | validate | ["--scope <dict>", "--background <flag>"] |
| scenarios | ["clarify", "strategy", "build", "validate", "render"] | clarify | ["--key-questions-answered <dict>", "--evidence-provided <dict>"] |


### Scenario: User requests detailed help for specific action (happy_path)

**Steps:**
```gherkin
Given current behavior is <behavior>
And Action "<action>" exists in behavior
And user enters command: help <action>
When CLI processes detailed help request
Then CLI displays "## <action>"
And CLI displays "Usage:"
And CLI displays action stages: instructions, submit, confirm
And CLI displays "Context Parameters" if action has parameters
```

**Examples:**
| behavior | action | description | parameters | parameter_syntax |
| --- | --- | --- | --- | --- |
| shape | build | Build knowledge graph for build | ["--scope <dict>"] | --scope '{"type": "epic", "value": ["Epic Name"]}' |
| discovery | validate | Validate knowledge graph against rules | ["--scope <dict>", "--background <flag>"] | --scope '{"type": "all"}' --background |
| scenarios | clarify | Gather context by asking questions | ["--key-questions-answered <dict>"] | --key-questions-answered '{"q1": "answer"}' |

