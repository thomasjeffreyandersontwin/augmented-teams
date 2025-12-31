# 📝 Display Bot Hierarchy Tree with Progress Indicators

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L69)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Display Bot State Using CLI](.)  
**Sequential Order:** 2
**Story Type:** system

## Story Description

Display Bot Hierarchy Tree with Progress Indicators functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** user views status
  **then** CLI displays bot hierarchy tree with behaviors and actions

- **When** displaying hierarchy
  **then** CLI shows progress indicators for each action

- **When** action is completed
  **then** CLI displays action with completed marker

- **When** action is current
  **then** CLI displays action with current marker

- **When** action is pending
  **then** CLI displays action with pending marker

## Scenarios

### Scenario: User views bot hierarchy with status command (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_display_bot_state_using_cli_current.py#L72)

**Steps:**
```gherkin
GIVEN: CLI is at discovery.build.instructions
WHEN: user enters 'status'
THEN: CLI displays bot hierarchy tree
AND: CLI displays bot hierarchy tree with [x], [*], [ ] indicators
AND: CLI shows discovery behavior marked with [*]
AND: CLI shows build action under discovery
```


### Scenario: CLI shows completed actions with completed marker (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at discovery.build.instructions
AND: discovery.clarify action is completed
WHEN: user views status
THEN: StatusDisplay marks completed actions with completed marker
AND: CLI displays clarify action with completed marker
```

