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

### Scenario: Inject Knowledge Graph Template and Builder Instructions (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
