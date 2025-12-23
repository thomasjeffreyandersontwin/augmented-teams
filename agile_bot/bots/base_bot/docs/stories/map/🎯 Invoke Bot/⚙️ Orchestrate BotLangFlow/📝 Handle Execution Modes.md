# 📝 Handle Execution Modes

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Orchestrate BotLangFlow
**User:** BotLangActionNode
**Sequential Order:** 15
**Story Type:** system

## Story Description

Handle Execution Modes functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BotLangActionNode executes and BotLangState.mode is 'autonomous'

  **then** BotLangActionNode calls run_autonomous() which submits to AI and continues without pausing

- **When** BotLangActionNode executes and BotLangState.mode is 'interactive'

  **then** BotLangActionNode calls run_interactive() which returns prompt and pauses BotLangFlow

  **and** run_interactive() returns dict with 'prompt' and 'needs_confirmation' flag

  **and** BotLangFlow execution pauses until human provides response via --continue

  **and** SqliteSaver preserves BotLangState in checkpoint with thread_id

## Scenarios

### Scenario: Handle Execution Modes - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Handle Execution Modes, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

