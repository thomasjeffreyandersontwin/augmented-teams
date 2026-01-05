# 📝 Proceed To Render Output

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 5
**Story Type:** user

## Story Description

Proceed To Render Output functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BuildKnowledgeAction completes execution

  **then** BuildKnowledgeAction saves Workflow State (per "Saves Behavior State" story)

  **and** BuildKnowledgeAction processes content for saving

  **and** Workflow automatically proceeds to render_output (auto_progress: true, no human confirmation needed)

## Scenarios

### Scenario: Seamless transition from build knowledge to validate rules (happy_path)

**Steps:**
```gherkin
GIVEN: Bot directory and workspace directory are set up
WHEN: Build knowledge action completes
THEN: Workflow transitions to validate
```


### Scenario: Workflow state captures build knowledge completion (happy_path)

**Steps:**
```gherkin
GIVEN: Bot directory and workspace directory are set up
WHEN: Build knowledge action completes
THEN: Workflow state captures completion
```

