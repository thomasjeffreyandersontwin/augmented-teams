# 📝 Route to Default Behavior Action

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Orchestrate BotLangFlow
**User:** Bot
**Sequential Order:** 7
**Story Type:** user

## Story Description

Route to Default Behavior Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Bot receives CLI command without --botlangflow flag

  **then** Bot routes via the default behavior/action path (existing router/forward logic)

  **and** Bot preserves legacy behavior_action_state and activity log behavior

  **and** LangGraph state/runner is not invoked

  **and** Action receives the original context parameter unchanged

## Scenarios

### Scenario: Route to Default Behavior Action - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Route to Default Behavior Action, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

