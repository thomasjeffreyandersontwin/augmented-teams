# 📝 Enforce Mutually Exclusive Scope Types

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py#L207)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 4
**Story Type:** system

## Story Description

Enforce Mutually Exclusive Scope Types functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user sets file scope while story scope is active
  **then** CLI replaces story scope with file scope

- **When** user sets story scope while file scope is active
  **then** CLI replaces file scope with story scope

- **When** checking stored scope
  **then** only one filter type is active

- **When** user clears scope
  **then** CLI removes all scope filters

## Scenarios

### Scenario: Setting file scope replaces existing story scope (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py#L214)

**Steps:**
```gherkin
GIVEN: CLI has story scope set
WHEN: user enters file scope
THEN: file scope replaces story scope (not combined)
```


### Scenario: Setting story scope replaces existing file scope (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py#L252)

**Steps:**
```gherkin
GIVEN: CLI has file scope set
WHEN: user enters story scope
THEN: story scope replaces file scope (not combined)
```


### Scenario: Scope object can only have one type at a time (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py#L290)

**Steps:**
```gherkin
GIVEN: Any scope is set
WHEN: checking the stored scope
THEN: only one filter type is active (knowledge_graph_filter OR file_filter, never both)
```

