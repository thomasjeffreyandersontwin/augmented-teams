# 📝 Display Confirm and Continue Prompt

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Navigate Workflow
**User:** CLI
**Sequential Order:** 1
**Story Type:** system

## Story Description

Display Confirm and Continue Prompt functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action completes,
  **then** CLI displays results summary

- **When** results are displayed,
  **then** CLI identifies next action

- **When** prompting to continue,
  **then** CLI asks user to confirm (y/n/review)

## Scenarios

### Scenario: CLI displays action completion and prompts for continuation (happy_path)

**Steps:**
```gherkin
Given BehaviorActionState.current_behavior is "<behavior>"
And BehaviorActionState.current_action is "<action>"
And User has completed work following instructions
And Action "<action>" has completed with results: <results_summary>
When user prepares to run submit operation
Then CLI displays "EXECUTED <behavior>.<action>"
And CLI displays "Results:"
And CLI displays results summary: "<results_display>"
And CLI identifies next action: "<next_action>"
And CLI prompts "Continue to next action (<next_action>)? (y/n/review)"
```

**Examples:**
| behavior | action | results_summary | results_display | next_action |
| --- | --- | --- | --- | --- |
| shape | clarify | {questions_answered: 7, evidence_types: 3} | - Answered 7 key questions\n- Provided 3 evidence types | strategy |
| shape | strategy | {decisions_made: 5, assumptions: 2} | - Made 5 decisions\n- Listed 2 assumptions | build |
| shape | build | {items_added: 12, mode: 'create'} | - Added 12 items\n- Mode: create | validate |

