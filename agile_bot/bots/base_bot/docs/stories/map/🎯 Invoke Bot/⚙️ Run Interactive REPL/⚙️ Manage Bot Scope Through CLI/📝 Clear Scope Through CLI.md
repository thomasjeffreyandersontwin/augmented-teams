# 📝 Clear Scope Through CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Manage Bot Scope Through CLI](.)  
**Sequential Order:** 6
**Story Type:** user

## Story Description

Clear Scope Through CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User clears all scope filters (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
AND: active scope filters are story="Story1" AND files="docs/**/*.md"
WHEN: user enters 'scope clear'
THEN: REPLSession clears all scope filters from context
AND: CLI displays 'All scope filters cleared'
AND: StatusDisplay shows no active scope
```


### Scenario: User executes build after clearing scope (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
AND: user has cleared all scope filters
WHEN: user enters 'shape.build.instructions'
THEN: CLIAction passes no scope filters to action
AND: CLI displays unfiltered instructions
```

