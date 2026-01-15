# 📝 Save Guardrails Via CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Save Bot Guardrails](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Save guardrail data using dedicated save command.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** User runs save command with answers parameter

  **then** System saves answers to clarification.json under current behavior

  **and** System merges with existing answers

- **When** User runs save command with evidence parameter

  **then** System saves evidence to clarification.json under current behavior

- **When** User runs save command with decisions parameter

  **then** System saves decisions to strategy.json under current behavior

- **When** User runs save command with assumptions parameter

  **then** System saves assumptions to strategy.json under current behavior

## Scenarios

<a id="scenario-save-guardrail-data"></a>
### Scenario: [Save guardrail data](#scenario-save-guardrail-data) (happy_path)

**Steps:**
```gherkin
Given Bot is at shape behavior
When User runs 'save --<param> <value>'
  | param               | value                                                           | file                 |
  | answers             | {"What is the scope of this work?": "Building bot system"}      | clarification.json   |
  | evidence_provided   | {"Requirements doc": "spec.md", "User interviews": "notes.md"}  | clarification.json   |
  | decisions           | {"drill_down_approach": "Dig deep on system interactions"}      | strategy.json        |
  | assumptions         | ["Focus on user flow over internal systems"]                    | strategy.json        |
Then System loads existing <file> for current behavior
And System merges new data with existing data
And System saves updated data to <file>
And System returns success
```

<a id="scenario-merge-with-existing"></a>
### Scenario: [Merge with existing data](#scenario-merge-with-existing) (happy_path)

**Steps:**
```gherkin
Given Guardrail file contains existing data for shape behavior
  | existing_data                                                                                                |
  | {"What is the scope of this work?": "Building bot system", "Who are the target users?": "AI Agents"}        |
  | {"drill_down_approach": "High and wide across all epics", "depth_of_shaping": "Extensive"}                  |
When User runs save command with new data
  | new_data                                                                | merged_result                                                                                                           |
  | {"Who are the target users?": "Developers and AI Agents"}               | {"What is the scope of this work?": "Building bot system", "Who are the target users?": "Developers and AI Agents"}    |
  | {"drill_down_approach": "Dig deep on system interactions"}              | {"drill_down_approach": "Dig deep on system interactions", "depth_of_shaping": "Extensive"}                            |
Then System preserves existing values for other fields
And System overwrites only the provided field
And Result matches merged_result
```

