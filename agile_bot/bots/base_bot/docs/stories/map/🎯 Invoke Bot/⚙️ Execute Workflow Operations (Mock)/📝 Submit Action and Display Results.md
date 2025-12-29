# 📝 Submit Action and Display Results

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** User
**Sequential Order:** 12
**Story Type:** user

## Story Description

Submit Action and Display Results functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user enters submit command
  **then** REPLSession routes to Bot

- **When** Bot receives submit
  **then** Bot delegates to current Action for submission
  **and** Action processes submission (stubbed - no file writes)

- **When** Action completes submission
  **then** Bot returns Result with submission summary

## Scenarios

### Scenario: User submits action and sees submission summary (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "<action>"
And user has completed work for current action
When user enters command: "submit"
Then REPLSession routes submit command to Bot
And Bot delegates to <action>.submit with ActionContext
And Action processes submission (stubbed - no file writes)
And Bot returns Result with submission summary
And REPLSession displays "<action> submission complete"
And REPLSession displays list of files that would be saved (stubbed)
```

**Examples:**
| behavior | action |
| --- | --- |
| shape | build |
| shape | clarify |
| discovery | clarify |
| exploration | validate |
| scenarios | build |


### Scenario: Submit with stubbed file writes shows what would be saved (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "shape" and action is "build"
And ActionContext has scope for story "Navigate To Behavior"
When user enters command: "submit"
Then Bot delegates to build.submit with ActionContext
And Action returns stubbed result with files: ["story-graph.json", "Navigate To Behavior.md"]
And REPLSession displays "[STUBBED] Would save: story-graph.json, Navigate To Behavior.md"
```


### Scenario: User submits clarify answers (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "<behavior>" and action is "clarify"
And user has reviewed key questions
When user enters command: "submit {"answers": {"What are goals?": "Create bot"}}"
Then REPLSession parses JSON to ClarifyActionContext
And REPLSession calls action.submit(context)
And Action saves clarification.json with answers
And REPLSession displays formatted output with:
  - **INSTRUCTIONS SECTION:** header (if navigating to next action)
  - "Clarification saved: N question(s) and answer(s) saved to <path>"
  - CLI STATUS section showing current progress
```

**Examples:**
| behavior | answers | evidence_provided |
| --- | --- | --- |
| shape | {"What are goals?": "Create bot"} | {} |
| discovery | {} | {"domain_doc": "path/to/doc.md"} |
| scenarios | {"Who are users?": "Developers"} | {"story_map": "path/to/map.md"} |


### Scenario: User submits clarify with evidence (happy_path)

**Steps:**
```gherkin
Given REPLSession is active with Bot
And current behavior is "discovery" and action is "clarify"
When user enters command: "submit {"evidence_provided": {"domain_doc": "path/to/doc.md"}}"
Then REPLSession parses JSON to ClarifyActionContext
And Action saves evidence to clarification.json
And REPLSession displays "Clarification saved: 1 evidence item(s) saved to <path>"
And REPLSession wraps output with CLI STATUS section
```

