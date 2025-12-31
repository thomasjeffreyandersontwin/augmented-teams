# 📝 Process Behavor Action Instructions Through AI Chat

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** BotLangActionNode
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Orchestrate BotLangFlow](.)  
**Sequential Order:** 12
**Story Type:** system

## Story Description

Process Behavor Action Instructions Through AI Chat functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BotLangActionNode executes in interactive mode

  **then** BotLangActionNode calls run_interactive() method

  **and** BotLangActionNode returns dict with 'prompt' and 'needs_confirmation' flag

  **and** BotLangFlow execution pauses at the interactive node

  **and** SqliteSaver saves checkpoint with BotLangState at the pause point with thread_id

  **and** Human can review AI response and provide confirmation or feedback before flow resumes

- **When** Human reviews the prompt and confirms or provides feedback

  **then** Confirmation/feedback is sent back to the bot, which is processed by LangGraph and the same BotLangActionNode

## Scenarios

### Scenario: Process Behavor Action Instructions Through AI Chat - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Process Behavor Action Instructions Through AI Chat, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```

