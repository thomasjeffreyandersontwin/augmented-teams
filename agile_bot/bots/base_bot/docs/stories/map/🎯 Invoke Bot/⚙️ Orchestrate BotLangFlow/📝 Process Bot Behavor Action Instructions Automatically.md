# 📝 Process Bot Behavor Action Instructions Automatically

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** BotLangActionNode
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Orchestrate BotLangFlow](.)  
**Sequential Order:** 11
**Story Type:** system

## Story Description

Process Bot Behavor Action Instructions Automatically functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BotLangActionNode executes in autonomous mode

  **then** BotLangActionNode calls run_autonomous() method

  **and** run_autonomous() sends instructions to AI via API client

  **and** BotLangActionNode waits for AI response

## Scenarios

### Scenario: Process Bot Behavor Action Instructions Automatically - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Process Bot Behavor Action Instructions Automatically, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

