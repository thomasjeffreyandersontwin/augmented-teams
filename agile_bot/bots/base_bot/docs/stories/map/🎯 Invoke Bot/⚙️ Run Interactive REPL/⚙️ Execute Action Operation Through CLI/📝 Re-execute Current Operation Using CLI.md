# 📝 Re-execute Current Operation Using CLI

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Execute Action Operation Through CLI](.)  
**Sequential Order:** 6
**Story Type:** user

## Story Description

Re-execute Current Operation Using CLI functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: User re-executes current instructions (happy_path)

**Steps:**
```gherkin
GIVEN: CLI is at shape.build.instructions (single behavior setup)
WHEN: user enters 'current'
THEN: CLI re-executes current instructions
```

