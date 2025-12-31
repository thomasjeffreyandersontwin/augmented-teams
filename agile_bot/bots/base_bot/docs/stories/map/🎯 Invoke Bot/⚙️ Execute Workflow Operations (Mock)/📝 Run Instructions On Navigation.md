# 📝 Run Instructions On Navigation

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 11
**Story Type:** user

## Story Description

Instructions automatically run when navigating to an action. Navigating to behavior.action triggers instructions to run without requiring a separate "instructions" command. This simplifies the workflow by combining navigation and instruction retrieval into a single step.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user navigates to behavior.action
  **then** instructions automatically run for that action
  **and** CLI displays formatted instructions response

- **When** re-running instructions explicitly
  **then** user can type "run" to re-execute current instructions

- **When** Bot receives Action result
  **then** Bot returns Result to REPLSession for display

## Scenarios

### Scenario: Navigation triggers auto-run of instructions (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<prev_behavior>" and action is "<prev_action>"
When user enters command: "<behavior>.<action>"
Then CLI navigates to <behavior>.<action>
And CLI automatically runs action.instructions() with ActionContext
And Action returns instructions for current scope
And REPLSession displays formatted instructions with:
  - **INSTRUCTIONS SECTION:** header
  - Instructions content for the action
  - CLI STATUS section with current progress
```

**Examples:**
| prev_behavior | prev_action | behavior | action |
| --- | --- | --- | --- |
| shape | clarify | shape | strategy |
| shape | build | shape | validate |
| shape | render | prioritization | clarify |
| discovery | clarify | discovery | build |


### Scenario: User re-runs instructions with run command (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<action>"
And instructions have already been displayed
When user enters command: "run"
Then CLI re-executes action.instructions() with ActionContext
And REPLSession displays formatted instructions to user
```

**Examples:**
| behavior | action |
| --- | --- |
| shape | build |
| discovery | clarify |
| scenarios | validate |


### Scenario: Instructions run with scope parameter (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "shape" and action is "build"
When user enters command: "shape.build --scope '{"type": "story", "value": ["Request Status"]}'"
Then CLI navigates to shape.build
And CLI parses inline scope parameter
And CLI builds ActionContext with scope
And CLI automatically runs action.instructions() with scope context
And REPLSession displays instructions for story "Request Status"
```


### Scenario: Clarify action auto-runs with questions and evidence prompts (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<prev_behavior>" and action is "<prev_action>"
When user enters command: "<behavior>.clarify"
Then CLI navigates to <behavior>.clarify
And CLI automatically runs action.instructions() with ClarifyActionContext
And Action returns required questions and evidence from guardrails
And REPLSession displays formatted instructions with:
  - **INSTRUCTIONS SECTION:** header
  - Key questions to answer
  - Required evidence to provide
  - CLI STATUS section with current progress
```

**Examples:**
| prev_behavior | prev_action | behavior |
| --- | --- | --- |
| shape | render | prioritization |
| prioritization | render | discovery |
| discovery | render | exploration |

