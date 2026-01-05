# 📝 Update Existing Knowledge Graph

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 4
**Story Type:** user

## Story Description

Update Existing Knowledge Graph functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Build Knowledge Action updates existing story graph

  **then** Action updates existing story-graph.json file

  **and** Action adds increments array to existing file

  **and** Existing epics and data are preserved

## Scenarios

### Scenario: Behavior updates existing story graph JSON (happy_path)

**Steps:**
```gherkin
GIVEN: Existing story-graph.json file exists
WHEN: Build Knowledge Action executes for behavior
THEN: Action updates existing story-graph.json
AND: Action adds increments array
AND: Existing epics are preserved
```

