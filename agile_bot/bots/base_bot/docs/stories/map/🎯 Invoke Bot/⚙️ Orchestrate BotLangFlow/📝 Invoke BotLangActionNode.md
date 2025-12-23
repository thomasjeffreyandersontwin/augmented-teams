# 📝 Invoke BotLangActionNode

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Orchestrate BotLangFlow
**User:** LangGraph
**Sequential Order:** 9
**Story Type:** system

## Story Description

Invoke BotLangActionNode functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** LangGraph invokes a node in the StateGraph

  **then** LangGraph calls the node's __call__ method with current BotLangState

  **and** BotLangActionNode receives BotLangState via __call__ entry point

  **and** BotLangActionNode extracts behavior/action/context from BotLangState

  **and** BotLangActionNode invokes action.execute(context) with extracted context

  **and** BotLangActionNode returns updated BotLangState to LangGraph

## Scenarios

### Scenario: Invoke BotLangActionNode - See Common Examples (happy_path)

**Steps:**
```gherkin
See [Common Examples Table](./common_examples_table.md) for detailed test data including input_data, expected_instruction_snippet, and expected_output for all behavior-action combinations.
This story tests the orchestration framework with real behavior-action combinations.
The common examples table contains:
- Real input data (story graphs, requests, questions)
- Expected instruction snippets that must appear in get_instructions() output
- Expected output after action.execute() completes
For Invoke BotLangActionNode, verify that:
- Node is created successfully
- Instructions are generated correctly
- Action executes and produces expected output
- State is updated properly
```


### Scenario: Test node operations in autonomous mode for each behavior-action (happy_path)

**Steps:**
```gherkin
Given BotLangFlow with one BotLangActionNode for "<behavior>" and "<action>"
And BotLangState initialized with behavior="<behavior>" and action="<action>"
And BotMode is set to autonomous
When BotLangFlow executes the single node
Then Node is created successfully
And get_instructions() returns instructions containing "<expected_instruction>"
And Node calls AI and gets response
And Node confirms response automatically
And Node completes without pausing
```

**Examples:**
| behavior | action | expected_instruction |
| --- | --- | --- |
| shape | clarify | Gather context for both story mapping and domain modeling |
| shape | strategy | Include domain modeling planning criteria alongside story mapping criteria |
| shape | build | shape: build story map structure AND domain model |
| shape | validate | shape: validate hierarchy, story structure, AND domain model |
| shape | render | shape: render story map documents AND domain model documents |
| shape | rules | Display digested rules for this behavior as AI context |
| prioritization | clarify | Gather context for prioritization |
| prioritization | strategy | Determine prioritization approach |
| prioritization | build | Build increment prioritization |
| prioritization | validate | Validate prioritization structure |
| prioritization | render | Render prioritization documents |
| prioritization | rules | Display digested rules for this behavior as AI context |
| discovery | clarify | Gather context for story discovery |
| discovery | strategy | Determine discovery approach |
| discovery | build | Build detailed story flows |
| discovery | validate | Validate story flows and domain rules |
| discovery | render | Render discovery documents |
| discovery | rules | Display digested rules for this behavior as AI context |
| exploration | clarify | Gather context for acceptance criteria |
| exploration | strategy | Determine exploration approach |
| exploration | build | Build acceptance criteria |
| exploration | validate | Validate acceptance criteria |
| exploration | render | Render exploration documents |
| exploration | rules | Display digested rules for this behavior as AI context |
| scenarios | clarify | Gather context for scenario specification |
| scenarios | strategy | Determine scenario approach |
| scenarios | build | specification_scenarios: build scenarios AND refine domain model based on scenario details |
| scenarios | validate | specification_scenarios: validate scenario structure AND domain model refinements |
| scenarios | render | specification_scenarios: render story documents with scenarios |
| scenarios | rules | Display digested rules for this behavior as AI context |
| tests | clarify | Gather context for test generation |
| tests | strategy | Determine test approach |
| tests | build | Build test code from scenarios |
| tests | validate | Validate test code |
| tests | render | Render test files |
| tests | rules | Display digested rules for this behavior as AI context |
| code | clarify | Gather context for code review |
| code | strategy | Determine code review approach |
| code | build | Analyze code against stories |
| code | validate | Validate code quality |
| code | render | Render code review reports |
| code | rules | Display digested rules for this behavior as AI context |


### Scenario: Test node operations in interactive mode for each behavior-action (happy_path)

**Steps:**
```gherkin
Given BotLangFlow with one BotLangActionNode for "<behavior>" and "<action>"
And BotLangState initialized with behavior="<behavior>" and action="<action>"
And BotMode is set to interactive
When BotLangFlow executes the single node
Then Node is created successfully
And get_instructions() returns instructions containing "<expected_instruction>"
And Node returns to chat with prompt for human
And Node pauses for human confirmation
```

**Examples:**
| behavior | action | expected_instruction |
| --- | --- | --- |
| shape | clarify | Gather context for both story mapping and domain modeling |
| shape | strategy | Include domain modeling planning criteria alongside story mapping criteria |
| shape | build | shape: build story map structure AND domain model |
| shape | validate | shape: validate hierarchy, story structure, AND domain model |
| shape | render | shape: render story map documents AND domain model documents |
| shape | rules | Display digested rules for this behavior as AI context |
| prioritization | clarify | Gather context for prioritization |
| prioritization | strategy | Determine prioritization approach |
| prioritization | build | Build increment prioritization |
| prioritization | validate | Validate prioritization structure |
| prioritization | render | Render prioritization documents |
| prioritization | rules | Display digested rules for this behavior as AI context |
| discovery | clarify | Gather context for story discovery |
| discovery | strategy | Determine discovery approach |
| discovery | build | Build detailed story flows |
| discovery | validate | Validate story flows and domain rules |
| discovery | render | Render discovery documents |
| discovery | rules | Display digested rules for this behavior as AI context |
| exploration | clarify | Gather context for acceptance criteria |
| exploration | strategy | Determine exploration approach |
| exploration | build | Build acceptance criteria |
| exploration | validate | Validate acceptance criteria |
| exploration | render | Render exploration documents |
| exploration | rules | Display digested rules for this behavior as AI context |
| scenarios | clarify | Gather context for scenario specification |
| scenarios | strategy | Determine scenario approach |
| scenarios | build | specification_scenarios: build scenarios AND refine domain model based on scenario details |
| scenarios | validate | specification_scenarios: validate scenario structure AND domain model refinements |
| scenarios | render | specification_scenarios: render story documents with scenarios |
| scenarios | rules | Display digested rules for this behavior as AI context |
| tests | clarify | Gather context for test generation |
| tests | strategy | Determine test approach |
| tests | build | Build test code from scenarios |
| tests | validate | Validate test code |
| tests | render | Render test files |
| tests | rules | Display digested rules for this behavior as AI context |
| code | clarify | Gather context for code review |
| code | strategy | Determine code review approach |
| code | build | Analyze code against stories |
| code | validate | Validate code quality |
| code | render | Render code review reports |
| code | rules | Display digested rules for this behavior as AI context |

