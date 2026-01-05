# 📝 Load and Display Workspace Context in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Initialize REPL Session](.)  
**Sequential Order:** 5
**Story Type:** system

## Story Description

Load and Display Workspace Context in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: CLI loads and displays workspace context (happy_path)

**Steps:**
```gherkin
GIVEN: Bot has workspace path
AND: workspace contains story-graph.json
WHEN: REPLSession initializes CLIBot
THEN: CLIBot loads workspace context from bot paths
```

