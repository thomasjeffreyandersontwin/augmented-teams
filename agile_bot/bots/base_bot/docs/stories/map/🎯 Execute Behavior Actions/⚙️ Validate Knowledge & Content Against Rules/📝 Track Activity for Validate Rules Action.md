# 📝 Track Activity for Validate Rules Action

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L2252)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Validate Knowledge & Content Against Rules](.)  
**Sequential Order:** 2
**Story Type:** user

## Story Description

Track Activity for Validate Rules Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** ValidateRulesAction executes

  **then** Action creates activity entry with timestamp, action name, behavior name, violations count

  **and** Activity entry appended to {project_area}/activity_log.json

## Scenarios

### Scenario: Track activity when validate action starts (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L2255)

**Steps:**
```gherkin
GIVEN: Bot directory and workspace directory are set up
WHEN: Validate rules action starts
THEN: Activity is tracked
```


### Scenario: Track activity when validate action completes (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L2272)

**Steps:**
```gherkin
GIVEN: Bot directory and workspace directory are set up
WHEN: Validate rules action completes
THEN: Activity is tracked with outputs and duration
```

