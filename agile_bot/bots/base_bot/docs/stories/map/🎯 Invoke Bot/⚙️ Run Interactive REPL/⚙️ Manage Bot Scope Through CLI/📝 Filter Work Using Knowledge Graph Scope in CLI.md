# 📝 Filter Work Using Knowledge Graph Scope in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 2
**Story Type:** user

## Story Description

Filter Work Using Knowledge Graph Scope in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user sets epic scope filter
  **then** CLI displays active scope filters

- **When** user sets story scope filter
  **then** CLI displays active scope filters

- **When** user executes build with active knowledge graph scope
  **then** CLI displays instructions filtered to specified stories

- **When** user clears scope
  **then** CLI removes all scope filters
  **and** displays unfiltered content

## Scenarios

### Scenario: User sets knowledge graph scope filter (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'scope <filter>'
THEN: CLI displays active scope filters
```


### Scenario: User executes build with active knowledge graph scope (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
AND: active scope filter is story="Story1"
WHEN: user enters 'shape.build.instructions'
THEN: CLIAction passes scope filter to action.get_instructions()
AND: CLI displays instructions filtered to Story1
```

