# 📝 Run Scanners against Knowledge Graph

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L2607)

**User:** Scanner
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Validate Knowledge & Content Against Rules](.)  
**Sequential Order:** 2
**Story Type:** user

## Story Description

Run Scanners against Knowledge Graph functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** scanners are executed against knowledge graph
  **then** violations are detected at exact line numbers

- **When** violations are detected
  **then** violation details include rule_name, location, violation_message, and severity

- **When** multiple scanners execute
  **then** violations from all scanners are aggregated

## Scenarios

### Scenario: Scanners detect violations in knowledge graph (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L2654)

**Steps:**
```gherkin
Given Agent is initialized with agent_name='test_story_bot'
And Project has finished generating knowledge graph
And Behavior is '{behavior_name}'
And Common rules directory exists at 'agile_bot/bots/test_story_bot/rules/'
And Behavior rules directory exists at 'agile_bot/bots/test_story_bot/behaviors/{behavior_number}_{behavior_name}/3_rules/'
And Scanners are discovered and registered for {behavior} and {rule file}:
- Common rules: 'agile_bot/bots/test_story_bot/rules/'
- Behavior rules: 'agile_bot/bots/test_story_bot/behaviors/{behavior_number}_{behavior_name}/3_rules/'
And Knowledge graph exists at 'agile_bot/bots/test_story_bot/docs/stories/story-graph.json'
Given Knowledge graph contains '{knowledge_graph_problems}'
And Rule file is '{rule_file}'
When Scanners are executed against knowledge graph containing '{knowledge_graph_problems}'
Then Violations are detected at '{expected_violation_line}'
And Violation details are '{expected_violation_details}'
And Report format is '{expected_report_format}'
And Report structure is '{expected_report_structure}'
```


### Scenario: Single scanner execution detects violations (happy_path)

**Steps:**
```gherkin
Given Knowledge graph contains '{knowledge_graph_problems}'
And Scanner '{scanner}' is selected for execution
When Single scanner '{scanner}' is executed against knowledge graph containing '{knowledge_graph_problems}'
Then Violation line is '{expected_violation_line}'
And Violation details are '{expected_violation_details}'
```


### Scenario: Multiple scanners execute and aggregate violations (happy_path)

**Steps:**
```gherkin
Given Scanners are discovered and registered
And Knowledge graph exists at 'agile_bot/bots/test_story_bot/docs/stories/story-graph.json'
And Knowledge graph contains '{knowledge_graph_problems}'
And Multiple scanners '{scanners}' are selected for execution
When Multiple scanners '{scanners}' are executed against knowledge graph containing '{knowledge_graph_problems}'
Then Violations per scanner are '{expected_violations_per_scanner}'
And Total violations are '{expected_total_violations}'
```


### Scenario: Scanner execution order and isolation (happy_path)

**Steps:**
```gherkin
Given Scanners are discovered and registered
And Knowledge graph exists at 'agile_bot/bots/test_story_bot/docs/stories/story-graph.json'
And Knowledge graph contains '{knowledge_graph_problems}'
And Scanner execution order is '{scanner_execution_order}'
And Scanner failure behavior is '{scanner_failure_behavior}'
When Scanners execute in '{scanner_execution_order}' order against knowledge graph containing '{knowledge_graph_problems}'
Then Result is '{expected_result}'
```

