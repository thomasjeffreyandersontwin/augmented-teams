# 📝 Resume BotLangFlow from Checkpoint

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** BotLangFlowRunner
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Orchestrate BotLangFlow](.)  
**Sequential Order:** 16
**Story Type:** system

## Story Description

Resume BotLangFlow from Checkpoint functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** User runs CLI with --continue flag and thread_id

  **then** BotLangFlowRunner calls resume_from() with thread_id and optional checkpoint_id

  **and** BotLangFlowRunner loads checkpoint from SqliteSaver using thread_id

  **and** SqliteSaver restores BotLangState from checkpoint

  **and** BotLangFlowRunner invokes compiled graph with restored BotLangState

  **and** BotLangFlow continues execution from the paused node

- **When** Human provides response with --continue

  **then** Response is added to BotLangState and passed to next node

  **and** BotLangFlow proceeds with updated BotLangState

## Scenarios

### Scenario: Resume BotLangFlow from Checkpoint - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Resume BotLangFlow from Checkpoint, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

