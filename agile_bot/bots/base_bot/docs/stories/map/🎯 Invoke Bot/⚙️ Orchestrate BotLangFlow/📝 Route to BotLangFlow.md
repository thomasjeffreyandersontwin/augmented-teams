# 📝 Route to BotLangFlow

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Orchestrate BotLangFlow
**User:** Bot
**Sequential Order:** 8
**Story Type:** user

## Story Description

Route to BotLangFlow functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Bot receives CLI command with --botlangflow <botlangflow_name>

  **then** Bot detects --botlangflow parameter

  **and** Bot routes to BotLangFlowRunner instead of default behavior/action flow

  **and** Bot builds initial BotLangState directly from CLI context (botlangflow_name, behavior, action, parameters)

  **and** Bot passes botlangflow_name and initial BotLangState to BotLangFlowRunner

- **When** BotLangFlowRunner receives botlangflow_name and initial BotLangState

  **then** BotLangFlowRunner loads the BotLangFlow Python file matching botlangflow_name

  **and** BotLangFlowRunner calls the flow's build function to create the StateGraph

  **and** BotLangFlowRunner compiles the StateGraph with SqliteSaver checkpointer

  **and** BotLangFlowRunner invokes the compiled graph with initial BotLangState and thread_id

## Scenarios

### Scenario: Route to BotLangFlow - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Route to BotLangFlow, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

