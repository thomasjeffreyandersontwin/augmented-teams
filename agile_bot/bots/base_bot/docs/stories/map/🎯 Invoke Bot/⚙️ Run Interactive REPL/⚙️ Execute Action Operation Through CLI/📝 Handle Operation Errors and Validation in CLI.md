# 📝 Handle Operation Errors and Validation in CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** CLI
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 7
**Story Type:** system

## Story Description

Handle Operation Errors and Validation in CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User enters invalid scope format with instructions (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions
WHEN: user enters 'shape.build.instructions scope="invalid{format}"'
THEN: CLI displays error message with valid formats
```

