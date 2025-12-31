# 📝 Prepare Action Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** BotLangActionNode
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Orchestrate BotLangFlow](.)  
**Sequential Order:** 10
**Story Type:** system

## Story Description

Prepare Action Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BotLangActionNode executes in autonomous or interactive mode

  **then** BotLangActionNode calls get_instructions() method

  **and** get_instructions() invokes action.execute(context) to collect instructions

  **and** Instructions are returned as string ready for AI submission

  **and** Action context is included in the instructions

## Scenarios

### Scenario: Prepare Action Instructions - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Prepare Action Instructions, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

