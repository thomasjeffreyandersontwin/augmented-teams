# 📝 Load Base Action Config

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Gather Context](.)  
**Sequential Order:** 5
**Story Type:** user

## Story Description

Load Base Action Config functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action loads configuration

  **then** Action loads base action configuration

  **and** Configuration includes action settings

## Scenarios

### Scenario: Base action config loaded from file (happy_path)

**Steps:**
```gherkin
GIVEN: Base action config file exists
WHEN: Action is initialized
THEN: Config is loaded
```

