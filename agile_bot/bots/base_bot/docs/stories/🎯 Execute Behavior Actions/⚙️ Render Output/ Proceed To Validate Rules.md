# 📝 Proceed To Validate Rules

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Render Output

## Story Description

RenderOutputAction transitions to validate_rules action after completion so that workflow proceeds seamlessly from output rendering to validation without user needing to remember next step.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** RenderOutputAction completes execution, **and** Human says action is done, **then** RenderOutputAction saves Workflow State (per "Saves Behavior State" story)
- **And** Workflow injects next action instructions (per "Inject Next Behavior-Action" story)
- **And** Workflow proceeds to validate_rules

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given RenderOutputAction is executing within a behavior
And render_output/action configuration has: workflow=true, order=4, next_action='validate_rules'
And Workflow State is persisted to project_area/workflow state
```

## Scenarios

### Scenario: Seamless transition from render_output to validate_rules

**Steps:**
```gherkin
Given behavior is 'discovery'
And render_output action is complete
And Human confirms "done" or "proceed"
When render_output action finalizes
Then Action saves Workflow State with:
  - current_behavior='story_bot.discovery'
  - current_action='story_bot.discovery.render_output'
  - timestamp=[completion time]
And Action loads render_output/action configuration
And Action reads next_action='validate_rules'
And Action injects AI instructions: "When done, proceed to validate_rules"
And AI invokes validate_rules tool
And Workflow transitions seamlessly to next action
```

### Scenario: User must confirm before transition

**Steps:**
```gherkin
Given render_output action is complete
And Human has NOT yet confirmed completion
When render_output action waits for human feedback
Then Action does NOT save workflow state as completed
And Action does NOT inject next action instructions
And Action does NOT proceed to validate_rules
And AI waits for human to say "done" before transitioning
```

### Scenario: Workflow state captures render_output completion

**Steps:**
```gherkin
Given render_output action completes at timestamp='2025-12-03T11:00:00Z'
And Human confirms "done"
When Action saves workflow state
Then workflow state is updated with:
  - current_action='story_bot.exploration.render_output'
  - timestamp='2025-12-03T11:00:00Z'
And completed_actions list includes: {action_state: 'story_bot.exploration.render_output', timestamp: '2025-12-03T11:00:00Z'}
And State persists to project_area/workflow state
And If workflow is interrupted after this point, render_output is marked as completed
```

### Scenario: Next action instructions injected into AI context

**Steps:**
```gherkin
Given render_output action is complete
And Human has confirmed "done"
And render_output/action configuration specifies next_action='validate_rules'
When Action injects next action instructions
Then AI context receives: "When done, proceed to validate_rules"
And AI knows to invoke validate_rules tool next
And User doesn't need to remember that validate_rules comes after render_output
And Seamless transition is enabled by instruction injection
```

### Scenario: Transition to terminal action (validate_rules)

**Steps:**
```gherkin
Given render_output is complete  
And validate_rules specifies next_action=null (terminal action)
When Workflow transitions to validate_rules
Then validate_rules is recognized as final action in workflow sequence
And After validate_rules completes, workflow will be complete
And User understands validate_rules is the last workflow step
```

### Scenario: Workflow resumes at validate_rules after interruption

**Steps:**
```gherkin
Given workflow state shows: current_action='story_bot.discovery.render_output'
And completed_actions contains render_output entry
And validate_rules has not yet started
And chat session was interrupted
When user reopens chat and invokes bot tool
Then Router loads workflow state
And Router sees render_output is completed
And Router determines next action is validate_rules
And Router forwards to validate_rules action
And Workflow resumes at correct next step despite interruption
```

### Scenario: Activity log records transition to validation

**Steps:**
```gherkin
Given render_output action completes at 11:00:00
And Human confirms "done"
When render_output saves state and transitions
Then Activity log records:
  - render_output completion entry with action_state='story_bot.discovery.render_output', duration=600
  - Workflow state update showing transition to validate_rules
And Audit trail shows render_output completed before validate_rules started
```

### Scenario: Rendered outputs become validation inputs

**Steps:**
```gherkin
Given render_output outputs are available: 6 documents generated
And Human has confirmed "done"
When render_output transitions to validate_rules
Then Workflow state includes rendered outputs in context
And validate_rules action receives rendered documents as inputs
And Validation checks the documents that were just rendered
And Workflow maintains data flow from render to validate
```

## Generated Artifacts

### Updated Workflow State
**Updated by:** RenderOutputAction on completion  
**Location:** {project_area}/workflow state  
**Content:**
- current_action updated to '<bot>.<behavior>.render_output'
- completed_actions list appended with full path render_output entry
- timestamp updated to completion time

### Injected AI Instructions
**Injected by:** RenderOutputAction on completion  
**Content:** "When done, proceed to validate_rules"

## Notes

- Transition requires human confirmation ("done")
- AI follows injected instructions to save rendered content
- validate_rules is terminal action (next_action=null, workflow completion follows)
- Seamless transition means user doesn't need to remember workflow sequence
- State persistence enables resumption at correct step after interruption
- Activity log and workflow state both updated during transition
- Rendered outputs (file paths) become inputs for validation action

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Render Output feature, Domain Concepts (Seamless Transition, Sequential Flow, State Persistence)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing "Saves Behavior State" and "Inject Next Behavior-Action" stories


