# 📝 Show Current Behavior Action Help

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Help
**User:** User
**Sequential Order:** 3
**Story Type:** user

## Story Description

Show Current Behavior Action Help functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user has navigated to a Behavior and Action
  **and** user requests help
  **then** REPLSession routes help request to Bot

- **When** Bot receives help request
  **then** Bot gathers current Behavior details
  **and** Bot gathers current Action details
  **and** Bot assembles parameters specific to Behavior/Action combination

- **When** Bot returns help Result
  **then** REPLSession displays Behavior context
  **and** REPLSession displays Action description
  **and** REPLSession displays available parameters for this Behavior/Action

## Scenarios

### Scenario: User requests parameter help for action with parameters (happy_path)

**Steps:**
```gherkin
Given current behavior is <behavior>
And Action "<action>" exists in behavior
And Action has parameters: <parameters>
And user enters command: help <action>
When CLI processes detailed help request
Then CLI displays "action <action> <parameter_syntax>"
And CLI displays "Parameters:" with type annotations for each parameter
```

**Examples:**
| behavior | action | parameters | parameter_syntax |
| --- | --- | --- | --- |
| shape | build | ["--scope <dict>"] | --scope '{"type": "epic", "value": ["Epic Name"]}' |
| discovery | validate | ["--scope <dict>", "--background <flag>"] | --scope '{"type": "all"}' --background |

