# 📝 Navigate Sequentially Using CLI Commands

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Navigate Bot Behaviors and Actions With CLI](.)  
**Sequential Order:** 2
**Story Type:** user

## Story Description

Navigate Sequentially Using CLI Commands functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User navigates with next command (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'next'
THEN: CLI navigates to shape.strategy
```


### Scenario: User navigates with back command (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.strategy.instructions
WHEN: user enters 'back'
THEN: CLI navigates to shape.clarify
```

