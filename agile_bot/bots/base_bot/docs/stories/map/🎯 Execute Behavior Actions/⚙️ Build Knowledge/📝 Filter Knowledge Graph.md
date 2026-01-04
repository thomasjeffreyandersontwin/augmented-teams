# 📝 Filter Knowledge Graph

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_build_knowledge.py#L1460)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 8
**Story Type:** user

## Story Description

Filter Knowledge Graph functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Knowledge graph needs filtering

  **then** Action filters knowledge graph by scope

  **and** Filtered graph contains only relevant content

## Scenarios

### Scenario: Filter returns all when scope is all (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_build_knowledge.py#L1463)

**Steps:**
```gherkin
GIVEN: Scope type is ALL
WHEN: Knowledge graph is filtered
THEN: All content is returned
```


### Scenario: Filter by story names returns matching stories (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_build_knowledge.py#L1480)

**Steps:**
```gherkin
GIVEN: Scope with story names
WHEN: Knowledge graph is filtered
THEN: Only matching stories are returned
```


### Scenario: Filter by epic names returns matching epics (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_build_knowledge.py#L1498)

**Steps:**
```gherkin
GIVEN: Scope with epic names
WHEN: Knowledge graph is filtered
THEN: Only matching epics are returned
```


### Scenario: Filter by increment priorities returns matching increments (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_build_knowledge.py#L1516)

**Steps:**
```gherkin
GIVEN: Scope with increment priorities
WHEN: Knowledge graph is filtered
THEN: Only matching increments are returned
```

