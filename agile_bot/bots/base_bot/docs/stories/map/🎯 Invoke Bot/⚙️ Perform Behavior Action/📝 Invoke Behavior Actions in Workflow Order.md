# 📝 Invoke Behavior Actions In Workflow Order

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Perform Behavior Action](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Invoke Behavior Actions In Workflow Order functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: Complete workflow end-to-end (happy_path)

**Steps:**
```gherkin
Given Bot has multiple behaviors (shape, discovery)
And each behavior has standard action workflow
When execute clarify action in shape behavior
And close clarify (transitions to strategy)
And jump to discovery.clarify (out of order)
And close discovery.clarify
Then state correctly shows current action at each step
And transitions occur as expected
And completed actions tracked across multiple behaviors
And out-of-order navigation works correctly
```

