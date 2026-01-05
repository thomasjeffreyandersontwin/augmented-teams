# 📝 Inject Knowledge Graph Template and Builder Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 2
**Story Type:** user

## Story Description

Inject Knowledge Graph Template and Builder Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Build Knowledge Action executes

  **then** Action loads knowledge graph template from behavior/content/knowledge_graph/

  **and** Action injects knowledge graph template path into instructions

  **and** knowledge_graph_template field is present in instructions

  **and** template file path exists and is accessible

- **When** knowledge graph template does not exist

  **then** Action raises FileNotFoundError with appropriate error message

## Scenarios

### Scenario: Action injects knowledge graph template (happy_path)

**Steps:**
```gherkin
GIVEN: Knowledge graph config and template exist
WHEN: Action executes
THEN: Template path is injected into instructions
```


### Scenario: Action loads and merges instructions (happy_path)

**Steps:**
```gherkin
GIVEN: Base and behavior-specific instructions exist
WHEN: Action method is invoked
THEN: Instructions are loaded from both locations and merged
```


### Scenario: All template variables are replaced in instructions (happy_path)

**Steps:**
```gherkin
GIVEN: Base instructions with {{rules}}, {{schema}}, {{description}}, {{instructions}} placeholders
WHEN: Action loads and merges instructions with all injections
THEN: All template variables are replaced with actual content
```

