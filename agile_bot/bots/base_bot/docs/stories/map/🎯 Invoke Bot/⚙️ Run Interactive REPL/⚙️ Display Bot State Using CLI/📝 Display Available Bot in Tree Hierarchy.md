# 📝 Display Available Bot in Tree Hierarchy

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 7
**Story Type:** system

## Story Description

Display Available Bot in Tree Hierarchy functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** CLI displays status
  **then** CLI shows current bot name in header

- **When** displaying bot hierarchy
  **then** CLI shows bot name
  **and** available behaviors

- **When** displaying hierarchy
  **then** CLI shows behaviors with actions in tree structure

- **When** displaying hierarchy
  **then** CLI uses indentation to show structure

## Scenarios

### Scenario: CLI displays bot name in header (happy_path)

**Steps:**
```gherkin
Given: CLI displays status
When: CLI renders bot hierarchy
Then: CLI shows current bot name in header
```

