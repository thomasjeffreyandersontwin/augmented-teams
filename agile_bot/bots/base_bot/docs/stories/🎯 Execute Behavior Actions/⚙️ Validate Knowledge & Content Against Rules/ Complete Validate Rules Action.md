# 📝 Complete Validate Rules Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Validate Knowledge & Content Against Rules

## Story Description

ValidateRulesAction completes as terminal action indicating workflow completion so that users know all workflow steps are finished and can review final validation results.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** ValidateRulesAction completes execution, **then** Action presents validation results to user
- **And** Human says action is done
- **Then** ValidateRulesAction saves Workflow State (per "Saves Behavior State" story)
- **And** validate_rules is terminal action (next_action: null, workflow completes)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given ValidateRulesAction is executing within a behavior
And validate_rules/action configuration has: workflow=true, order=5, next_action=null
And Workflow State is persisted to project_area/workflow state
```

## Scenarios

### Scenario: Workflow completes at validate_rules (terminal action)

**Steps:**
```gherkin
Given behavior is 'discovery'
And validate_rules action is complete
And validate_rules/action configuration specifies next_action=null
And Human confirms "done" or "proceed"
When validate_rules action finalizes
Then Action saves Workflow State with:
  - current_behavior='story_bot.discovery'
  - current_action='story_bot.discovery.validate_rules'
  - timestamp=[completion time]
And Action detects next_action=null (terminal action)
And Action presents message: "Workflow is complete. No further actions required."
And No next action instructions are injected
And Workflow sequence ends at validate_rules
```

### Scenario: Validation results presented to user before completion

**Steps:**
```gherkin
Given validate_rules action is complete
And Validation results show: 3 violations, 15 rules passed
When validate_rules presents results to user
Then User sees validation report with:
  - Total documents validated: 6
  - Violations found: 3 (with details)
  - Rules passed: 15
  - Validation status: Completed with violations
And User can review validation results
And Human confirms "done" to finalize workflow
```

### Scenario: Workflow state captures validate_rules completion (terminal)

**Steps:**
```gherkin
Given validate_rules action completes at timestamp='2025-12-03T11:10:00Z'
And Human confirms "done"
When Action saves workflow state
Then workflow state is updated with:
  - current_action='story_bot.exploration.validate_rules'
  - timestamp='2025-12-03T11:10:00Z'
  - workflow_complete=true (indicator that terminal action finished)
And completed_actions list includes: {action_state: 'story_bot.exploration.validate_rules', timestamp: '2025-12-03T11:10:00Z'}
And State persists to project_area/workflow state
And State indicates entire workflow is finished
```

### Scenario: No next action instructions injected (terminal action)

**Steps:**
```gherkin
Given validate_rules action is complete
And Human has confirmed "done"
And validate_rules/action configuration specifies next_action=null
When Action checks for next action
Then Action detects next_action is null
And Action does NOT inject next action instructions
And AI context receives: "Workflow is complete. No further actions required."
And User understands workflow has reached its natural end
And No automatic transition occurs
```

### Scenario: Activity log records workflow completion

**Steps:**
```gherkin
Given validate_rules action completes at 11:10:00
And Human confirms "done"
And validate_rules is terminal action
When validate_rules saves state and completes
Then Activity log records:
  - validate_rules completion entry with action_state='story_bot.discovery.validate_rules', duration=600
  - Note: "Terminal action - workflow complete"
  - Workflow state update showing workflow completion
And Audit trail shows complete workflow from gather_context through validate_rules completion
```

### Scenario: User can restart workflow after completion

**Steps:**
```gherkin
Given workflow state shows: workflow_complete=true
And validate_rules is marked complete
When user wants to start new workflow for different increment
Then User can reinitialize workflow by invoking first action (gather_context)
And Workflow state resets to beginning
And New workflow sequence starts fresh
And Previous workflow completion preserved in activity log
```

### Scenario: Workflow completion with validation violations

**Steps:**
```gherkin
Given validation results show 3 violations
And Human has confirmed "done" despite violations
When validate_rules completes as terminal action
Then Workflow completes with status: "Completed with 3 validation violations"
And User is informed that workflow finished but has issues to address
And User can invoke correct_bot independently to fix violations
And Workflow completion doesn't require zero violations
```

### Scenario: Workflow completion with zero violations

**Steps:**
```gherkin
Given validation results show 0 violations
And All 15 rules passed
And Human has confirmed "done"
When validate_rules completes as terminal action
Then Workflow completes with status: "Completed successfully - all validations passed"
And User is informed that workflow finished with no issues
And User can proceed with confidence that content meets all rules
```

### Scenario: Workflow resumes at validate_rules after interruption (near completion)

**Steps:**
```gherkin
Given workflow state shows: current_action='story_bot.exploration.validate_rules'
And validate_rules is NOT in completed_actions (was interrupted)
And user has reopened chat
When Router loads workflow state
Then Router sees validate_rules is started (not completed)
And Router forwards to validate_rules action
And User can choose to retry or continue validate_rules
And After completion, workflow will be complete (terminal action)
```

### Scenario: correct_bot can be invoked independently after workflow completion

**Steps:**
```gherkin
Given validation results show 3 violations
And workflow state shows: workflow_complete=true
And correct_bot/action configuration specifies workflow=false (independent action)
When User wants to address validation violations
Then User can invoke correct_bot independently
And correct_bot does NOT require workflow state
And correct_bot is NOT part of workflow sequence
And Independent actions available after workflow completion
```

## Generated Artifacts

### Updated Workflow State (Final)
**Updated by:** ValidateRulesAction on completion  
**Location:** {project_area}/workflow state  
**Content:**
```json
{
  "current_behavior": "story_bot.exploration",
  "current_action": "story_bot.exploration.validate_rules",
  "workflow_complete": true,
  "timestamp": "2025-12-03T11:10:00Z",
  "completed_actions": [
    {
      "action_state": "story_bot.exploration.gather_context",
      "timestamp": "2025-12-03T10:05:30Z",
      "duration": 330
    },
    {
      "action_state": "story_bot.exploration.decide_planning_criteria",
      "timestamp": "2025-12-03T10:25:00Z",
      "duration": 600
    },
    {
      "action_state": "story_bot.exploration.build_knowledge",
      "timestamp": "2025-12-03T10:50:00Z",
      "duration": 1200
    },
    {
      "action_state": "story_bot.exploration.render_output",
      "timestamp": "2025-12-03T11:00:00Z",
      "duration": 600
    },
    {
      "action_state": "story_bot.exploration.validate_rules",
      "timestamp": "2025-12-03T11:10:00Z",
      "duration": 600
    }
  ]
}
```

### Validation Results Report
**Presented by:** ValidateRulesAction on completion  
**Content:**
- Documents validated count
- Violations found (with details)
- Rules passed count
- Validation status (success or with violations)

## Notes

- validate_rules is terminal action: next_action=null indicates workflow completion
- No next action instructions injected for terminal actions
- Validation results presented to user before workflow completes
- Workflow can complete with or without violations (violations don't block completion)
- correct_bot is independent action (workflow: false), invokable after workflow completion
- Activity log shows complete workflow sequence from start to finish
- Workflow state includes workflow_complete=true indicator
- User can restart workflow by reinitializing at gather_context

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Validate Knowledge & Content Against Rules feature, Domain Concepts (Workflow Action, Independent Action, Sequential Flow, Audit Trail)  
**Domain Rules Referenced:** "CRITICAL: correct_bot has workflow: false - it is NOT part of workflow sequence", "CRITICAL: validate_rules has next_action: null - it is the terminal workflow action"  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria emphasizing terminal action behavior and workflow completion


