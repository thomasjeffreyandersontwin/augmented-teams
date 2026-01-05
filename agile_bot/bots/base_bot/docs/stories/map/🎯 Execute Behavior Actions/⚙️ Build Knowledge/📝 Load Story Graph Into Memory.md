# 📝 Load Story Graph Into Memory

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Load Story Graph Into Memory functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Story graph file exists

  **then** StoryMap loads epics, sub_epics, story_groups, stories, and scenarios

  **and** StoryMap provides walk method to traverse all nodes

- **When** Story graph file does not exist

  **then** StoryMap raises FileNotFoundError

## Scenarios

### Scenario: Story map loads epics (happy_path)

**Steps:**
```gherkin
GIVEN: Story graph JSON with epics
WHEN: StoryMap is loaded
THEN: Epics are accessible
```


### Scenario: Epic has sub epics (happy_path)

**Steps:**
```gherkin
GIVEN: Epic with sub-epics in story graph
WHEN: Epic is accessed
THEN: Sub-epics are available
```


### Scenario: Sub epic has story groups (happy_path)

**Steps:**
```gherkin
GIVEN: Sub-epic with story groups
WHEN: Sub-epic is accessed
THEN: Story groups are available
```


### Scenario: Story group has stories (happy_path)

**Steps:**
```gherkin
GIVEN: Story group with stories
WHEN: Story group is accessed
THEN: Stories are available
```


### Scenario: Story has properties (happy_path)

**Steps:**
```gherkin
GIVEN: Story with properties (name, description, etc.)
WHEN: Story is accessed
THEN: Properties are available
```


### Scenario: Story has scenarios (happy_path)

**Steps:**
```gherkin
GIVEN: Story with scenarios
WHEN: Story is accessed
THEN: Scenarios are available
```


### Scenario: Story map walk traverses all nodes (happy_path)

**Steps:**
```gherkin
GIVEN: Story map with epics, sub-epics, stories
WHEN: walk() is called
THEN: All nodes are traversed
```


### Scenario: From bot loads story graph (happy_path)

**Steps:**
```gherkin
GIVEN: Bot with story-graph.json in workspace
WHEN: StoryMap.from_bot() is called
THEN: Story graph is loaded
```

