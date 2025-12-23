# 📝 Generate Violation Report

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Validate Knowledge & Content Against Rules
**User:** Bot Behavior
**Sequential Order:** 5
**Story Type:** user

## Story Description

Generate Violation Report functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** violation report is generated
  **then** report is generated in requested format

- **When** violations are grouped
  **then** violations are organized by behavior_name, rule_name, location, or severity

- **When** report is written to file
  **then** file is created at specified output destination

## Scenarios

### Scenario: Violation report generation in different formats (happy_path)

**Steps:**
```gherkin
Given Agent is initialized with agent_name='test_story_bot'
And Project has finished generating knowledge graph
And Behavior is '{behavior_name}'
And Common rules directory exists at 'agile_bot/bots/test_story_bot/rules/'
And Behavior rules directory exists at 'agile_bot/bots/test_story_bot/behaviors/{behavior_number}_{behavior_name}/3_rules/'
And Scanners have executed against knowledge graph
Given Violations have been detected: '{violations_data}'
And Report format is '{report_format}'
When Violation report is generated with violations '{violations_data}' and format '{report_format}'
Then Report structure is '{expected_report_structure}'
```


### Scenario: Violation grouping and organization (happy_path)

**Steps:**
```gherkin
Given Violations have been detected: '{violations_data}'
And Violations are from behaviors '{behaviors}'
When Violations are grouped and organized with violations '{violations_data}' from behaviors '{behaviors}'
Then Grouping is '{expected_grouping}'
And Organization is '{expected_organization}'
```


### Scenario: Report output and persistence (happy_path)

**Steps:**
```gherkin
Given Violations have been detected: '{violations_data}'
And Report format is '{report_format}'
And Output destination is '{output_destination}'
When Report is generated with format '{report_format}' and violations '{violations_data}' and written to '{output_destination}'
Then Output is '{expected_output}'
```

