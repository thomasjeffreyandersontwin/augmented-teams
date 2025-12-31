# 📝 Return to chat and pause for human-in-the-loop Node

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** BotLangFlow
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Orchestrate BotLangFlow](.)  
**Sequential Order:** 14
**Story Type:** system

## Story Description

Return to chat and pause for human-in-the-loop Node functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BotLangFlow includes a dedicated human-in-the-loop node

  **then** Node returns instructions/prompt to CLI

  **and** CLI outputs prompt to chat interface

  **and** BotLangFlow execution pauses at that node

  **and** SqliteSaver saves checkpoint with BotLangState at pause point with thread_id

  **and** Human can review prompt and provide response before BotLangFlow resumes

## Scenarios

### Scenario: Return to chat and pause for human-in-the-loop Node - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Return to chat and pause for human-in-the-loop Node, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

