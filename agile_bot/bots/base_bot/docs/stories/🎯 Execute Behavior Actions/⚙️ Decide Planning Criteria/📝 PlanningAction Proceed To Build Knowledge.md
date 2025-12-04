# 📝 Proceed To Build Knowledge

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Decide Planning Criteria

## Story Description

PlanningAction transitions to build_knowledge action after completion so that workflow proceeds seamlessly from planning criteria to knowledge building without user needing to remember next step.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** PlanningAction completes execution, **and** Human says action is done, **then** PlanningAction saves Workflow State (per "Saves Behavior State" story)
- **And** Workflow injects next action instructions (per "Inject Next Behavior-Action" story)
- **And** Workflow proceeds to build_knowledge

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given PlanningAction is executing within a behavior
And decide_planning_criteria/action configuration has: workflow=true, order=2, next_action='build_knowledge'
And Workflow State is persisted to project_area/workflow state
```

## Scenarios

### Scenario: Seamless transition from planning to build_knowledge

**Steps:**
```gherkin
Given behavior is 'discovery'
And decide_planning_criteria action is complete
And Human confirms "done" or "proceed"
When decide_planning_criteria action finalizes
Then Action saves Workflow State with:
  - current_behavior='story_bot.discovery'
  - current_action='story_bot.discovery.decide_planning_criteria'
  - timestamp=[completion time]
And Action loads decide_planning_criteria/action configuration
And Action reads next_action='build_knowledge'
And Action injects AI instructions: "When done, proceed to build_knowledge"
And AI invokes build_knowledge tool
And Workflow transitions seamlessly to next action
```

### Scenario: User must confirm before transition

**Steps:**
```gherkin
Given decide_planning_criteria action is complete
And Human has NOT yet confirmed completion
When decide_planning_criteria action waits for human feedback
Then Action does NOT save workflow state as completed
And Action does NOT inject next action instructions
And Action does NOT proceed to build_knowledge
And AI waits for human to say "done" before transitioning
```

### Scenario: Workflow state captures planning completion

**Steps:**
```gherkin
Given decide_planning_criteria action completes at timestamp='2025-12-03T10:25:00Z'
And Human confirms "done"
When Action saves workflow state
Then workflow state is updated with:
  - current_action='story_bot.exploration.decide_planning_criteria'
  - timestamp='2025-12-03T10:25:00Z'
And completed_actions list includes: {action_state: 'story_bot.exploration.decide_planning_criteria', timestamp: '2025-12-03T10:25:00Z'}
And State persists to project_area/workflow state
And If workflow is interrupted after this point, planning is marked as completed
```

### Scenario: Next action instructions injected into AI context

**Steps:**
```gherkin
Given decide_planning_criteria action is complete
And Human has confirmed "done"
And decide_planning_criteria/action configuration specifies next_action='build_knowledge'
When Action injects next action instructions
Then AI context receives: "When done, proceed to build_knowledge"
And AI knows to invoke build_knowledge tool next
And User doesn't need to remember that build_knowledge comes after planning
And Seamless transition is enabled by instruction injection
```

### Scenario: Transition carries planning outputs to build_knowledge

**Steps:**
```gherkin
Given decide_planning_criteria outputs are available: 4 criteria, 2 assumptions, 3 decisions in planning.json
And Human has confirmed "done"
When decide_planning_criteria transitions to build_knowledge
Then Workflow state includes planning outputs in context
And build_knowledge action receives planning criteria and assumptions as inputs
And Knowledge building is informed by planning decisions
```

### Scenario: Workflow resumes at build_knowledge after interruption

**Steps:**
```gherkin
Given workflow state shows: current_action='story_bot.discovery.decide_planning_criteria'
And completed_actions contains decide_planning_criteria entry
And build_knowledge has not yet started
And chat session was interrupted
When user reopens chat and invokes bot tool
Then Router loads workflow state
And Router sees decide_planning_criteria is completed
And Router determines next action is build_knowledge
And Router forwards to build_knowledge action
And Workflow resumes at correct next step despite interruption
```

### Scenario: Activity log records transition

**Steps:**
```gherkin
Given decide_planning_criteria action completes at 10:25:00
And Human confirms "done"
When decide_planning_criteria saves state and transitions
Then Activity log records:
  - decide_planning_criteria completion entry with action_state='story_bot.discovery.decide_planning_criteria', duration=600
  - Workflow state update showing transition to build_knowledge
And Audit trail shows planning completed before build_knowledge started
```

### Scenario: Transition works mid-workflow

**Steps:**
```gherkin
Given workflow state shows gather_context is complete (order=1)
And decide_planning_criteria is at order=2 in workflow
And build_knowledge is next at order=3
And Human has confirmed "done"
When decide_planning_criteria transitions
Then Workflow proceeds to build_knowledge (middle of workflow sequence)
And Sequential flow continues: gather_context → decide_planning_criteria → build_knowledge
And Mid-workflow transitions work identically to first transition
```

## Generated Artifacts

### Updated Workflow State
**Updated by:** PlanningAction on completion  
**Location:** {project_area}/workflow state  
**Content:**
- current_action updated to '<bot>.<behavior>.decide_planning_criteria'
- completed_actions list appended with full path decide_planning_criteria entry
- timestamp updated to completion time

### Injected AI Instructions
**Injected by:** PlanningAction on completion  
**Content:** "When done, proceed to build_knowledge"

## Notes

- Transition requires human confirmation ("done")
- Workflow state saved BEFORE transition instructions injected
- Planning outputs become inputs for build_knowledge action
- Seamless transition means user doesn't need to remember workflow sequence
- State persistence enables resumption at correct step after interruption
- Activity log and workflow state both updated during transition

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Decide Planning Criteria feature, Domain Concepts (Seamless Transition, Sequential Flow, State Persistence)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing "Saves Behavior State" and "Inject Next Behavior-Action" stories


