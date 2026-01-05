# 📝 Navigate Using CLI Dot Notation

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Navigate Bot Behaviors and Actions With CLI](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Navigate Using CLI Dot Notation functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User navigates with behavior only (no dots) (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'discovery'
THEN: CLI navigates to discovery.clarify (first action)
```


### Scenario: User navigates with behavior.action (one dot) (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'discovery.build'
THEN: CLI navigates to discovery.build.instructions
```


### Scenario: User navigates with behavior.action.operation (two dots) (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'discovery.build.instructions'
THEN: CLI executes discovery.build.instructions
```


### Scenario: User enters invalid behavior in dot notation (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.clarify.instructions
WHEN: user enters 'invalid_behavior.build.instructions'
THEN: CLI displays error message
```

