# 📝 Get Instructions and Display

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 11
**Story Type:** user

## Story Description

Get Instructions and Display functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user requests instructions
  **then** REPLSession routes to Bot

- **When** Bot receives instructions request
  **then** Bot delegates to current Action with ActionContext
  **and** Action returns instructions based on scope

- **When** Bot receives Action result
  **then** Bot returns Result to REPLSession for display

## Scenarios

### Scenario: User requests instructions and sees formatted output (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<action>"
And ActionContext has scope type "<scope_type>" with value "<scope_value>"
When user enters command: "instructions"
Then REPLSession routes instructions request to Bot
And Bot delegates to <action>.get_instructions with ActionContext
And Action returns instructions for scope "<scope_value>"
And Bot returns Result with instructions to REPLSession
And REPLSession displays formatted instructions to user
```

**Examples:**
| behavior | action | scope_type | scope_value |
| --- | --- | --- | --- |
| shape | build | story | Navigate To Behavior |
| shape | clarify | all | all |
| discovery | clarify | epic | Invoke Bot |
| exploration | validate | increment | 11 |
| scenarios | build | epic | Run Interactive REPL |
| scenarios | clarify | story | Request Help |


### Scenario: User requests instructions with inline scope parameter (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "shape" and action is "build"
When user enters command: "instructions --scope '{"type": "story", "value": ["Request Status"]}'"
Then REPLSession parses inline scope parameter
And REPLSession builds ActionContext with scope
And REPLSession routes to Bot
And Bot delegates to build.get_instructions with ActionContext
And REPLSession displays instructions for story "Request Status"
```


### Scenario: User requests clarify instructions without parameters (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "clarify"
When user enters command: "clarify" or "clarify.instructions"
Then REPLSession routes to CLIBot
And CLIBot calls action.instructions() with empty ClarifyActionContext
And Action returns required questions and evidence from guardrails
And REPLSession displays formatted instructions with:
  - **INSTRUCTIONS SECTION:** header
  - Key questions to answer
  - Required evidence to provide
  - CLI STATUS section with current progress
```

**Examples:**
| behavior | key_questions_shown | evidence_shown |
| --- | --- | --- |
| shape | Yes | Yes |
| discovery | Yes | Yes |
| scenarios | Yes | Yes |

