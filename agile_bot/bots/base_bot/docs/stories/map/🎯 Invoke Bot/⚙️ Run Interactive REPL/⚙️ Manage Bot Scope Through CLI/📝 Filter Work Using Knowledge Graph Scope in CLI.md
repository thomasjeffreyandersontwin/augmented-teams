# 📝 Filter Work Using Knowledge Graph Scope in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli_current.py#L69)

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

### Scenario: User sets scope filter (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli_current.py#L72)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'scope story="Story1"'
THEN: CLI stores scope filter
```


### Scenario: User views current scope (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli_current.py#L101)

**Steps:**
```gherkin
GIVEN: Scope filter is set
WHEN: user enters 'scope'
THEN: CLI displays current scope
```

