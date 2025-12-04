# 📝 GatherContextAction --> Proceed To Decide Planning

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Gather Context

## Story Description

GatherContextAction transitions to decide_planning_criteria action after completion so that workflow proceeds seamlessly from context gathering to planning criteria without user needing to remember next step.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** GatherContextAction completes execution, **and** Human says action is done, **then** GatherContextAction saves Workflow State (per "Saves Behavior State" story)
- **And** Workflow injects next action instructions (per "Inject Next Behavior-Action" story)
- **And** Workflow proceeds to decide_planning_criteria

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given GatherContextAction is executing within a behavior
And gather_context/action configuration has: workflow=true, order=1, next_action='decide_planning_criteria'
And Workflow State is persisted to project_area/workflow state
```

## Scenarios

### Scenario: Seamless transition from gather_context to decide_planning_criteria

**Steps:**
```gherkin
Given behavior is 'discovery'
And gather_context action is complete
And Human confirms "done" or "proceed"
When gather_context action finalizes
Then Action saves Workflow State with:
  - current_behavior='story_bot.discovery'
  - current_action='story_bot.discovery.gather_context'
  - timestamp=[completion time]
And Action loads gather_context/action configuration
And Action reads next_action='decide_planning_criteria'
And Action injects AI instructions: "When done, proceed to decide_planning_criteria"
And AI invokes decide_planning_criteria tool
And Workflow transitions seamlessly to next action
```

### Scenario: User must confirm before transition

**Steps:**
```gherkin
Given gather_context action is complete
And Human has NOT yet confirmed completion
When gather_context action waits for human feedback
Then Action does NOT save workflow state as completed
And Action does NOT inject next action instructions
And Action does NOT proceed to decide_planning_criteria
And AI waits for human to say "done" before transitioning
```

### Scenario: Workflow state captures gather_context completion

**Steps:**
```gherkin
Given gather_context action completes at timestamp='2025-12-03T10:05:30Z'
And Human confirms "done"
When Action saves workflow state
Then workflow state is updated with:
  - current_action='story_bot.exploration.gather_context'
  - timestamp='2025-12-03T10:05:30Z'
And completed_actions list includes: {action_state: 'story_bot.exploration.gather_context', timestamp: '2025-12-03T10:05:30Z'}
And State persists to project_area/workflow state
And If workflow is interrupted after this point, gather_context is marked as completed
```

### Scenario: Next action instructions injected into AI context

**Steps:**
```gherkin
Given gather_context action is complete
And Human has confirmed "done"
And gather_context/action configuration specifies next_action='decide_planning_criteria'
When Action injects next action instructions
Then AI context receives: "When done, proceed to decide_planning_criteria"
And AI knows to invoke decide_planning_criteria tool next
And User doesn't need to remember what comes after gather_context
And Seamless transition is enabled by instruction injection
```

### Scenario: Transition works across different behaviors

**Steps:**
```gherkin
Given behavior is 'shape' (first behavior)
And gather_context is complete in shape behavior
And Human has confirmed "done"
When gather_context transitions to next action
Then Workflow proceeds to shape_decide_planning_criteria (not discovery_decide_planning_criteria)
And Transition stays within same behavior
And Each behavior has its own workflow sequence
```

### Scenario: Workflow resumes at decide_planning_criteria after interruption

**Steps:**
```gherkin
Given workflow state shows: current_action='story_bot.discovery.gather_context'
And completed_actions contains gather_context entry
And decide_planning_criteria has not yet started
And chat session was interrupted
When user reopens chat and invokes bot tool
Then Router loads workflow state
And Router sees gather_context is completed
And Router determines next action is decide_planning_criteria
And Router forwards to decide_planning_criteria action
And Workflow resumes at correct next step despite interruption
```

### Scenario: Activity log records transition

**Steps:**
```gherkin
Given gather_context action completes at 10:05:30
And Human confirms "done"
When gather_context saves state and transitions
Then Activity log records:
  - gather_context completion entry with action_state='story_bot.discovery.gather_context', duration=330
  - Workflow state update showing transition to next action
And Audit trail shows gather_context completed before decide_planning_criteria started
```

## Generated Artifacts

### Updated Workflow State
**Updated by:** GatherContextAction on completion  
**Location:** {project_area}/workflow state  
**Content:**
- current_action updated to '<bot>.<behavior>.gather_context'
- completed_actions list appended with full path gather_context entry
- timestamp updated to completion time

### Injected AI Instructions
**Injected by:** GatherContextAction on completion  
**Content:** "When done, proceed to decide_planning_criteria"

## Notes

- Transition requires human confirmation ("done")
- Workflow state saved BEFORE transition instructions injected
- Instruction injection tells AI what to do next
- Seamless transition means user doesn't need to remember workflow sequence
- State persistence enables resumption at correct step after interruption
- Activity log and workflow state both updated during transition

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Gather Context feature, Domain Concepts (Seamless Transition, State Persistence, Automatic Next Step Injection)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing "Saves Behavior State" and "Inject Next Behavior-Action" stories


