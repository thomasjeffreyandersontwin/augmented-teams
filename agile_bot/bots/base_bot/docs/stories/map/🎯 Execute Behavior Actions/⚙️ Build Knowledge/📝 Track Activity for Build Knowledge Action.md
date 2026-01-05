# 📝 Track Activity for Build Knowledge Action

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 3
**Story Type:** user

## Story Description

Track Activity for Build Knowledge Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BuildKnowledgeAction executes

  **then** Action creates activity entry with timestamp, action name, behavior name

  **and** Activity entry appended to {project_area}/activity_log.json

## Scenarios

### Scenario: Track activity when build action starts (happy_path)

**Steps:**
```gherkin
GIVEN: Bot directory and workspace directory are set up
WHEN: Build knowledge action starts
THEN: Activity is tracked
```


### Scenario: Track activity when build action completes (happy_path)

**Steps:**
```gherkin
GIVEN: Build knowledge outputs and duration
WHEN: Build knowledge action completes
THEN: Activity is tracked with outputs and duration
```

