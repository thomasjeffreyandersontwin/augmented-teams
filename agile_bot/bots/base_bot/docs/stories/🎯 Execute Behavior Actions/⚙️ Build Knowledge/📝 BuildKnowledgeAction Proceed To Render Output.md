# 📝 Proceed To Render Output

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Build Knowledge

## Story Description

BuildKnowledgeAction automatically transitions to render_output action without human confirmation so that workflow proceeds seamlessly from knowledge building to output rendering with auto_progress enabled.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BuildKnowledgeAction completes execution, **then** BuildKnowledgeAction saves Workflow State (per "Saves Behavior State" story)
- **And** Workflow automatically proceeds to render_output (auto_progress: true, no human confirmation needed)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given BuildKnowledgeAction is executing within a behavior
And build_knowledge/action configuration has: workflow=true, order=3, next_action='render_output', auto_progress=true
And Workflow State is persisted to project_area/workflow state
```

## Scenarios

### Scenario: Automatic transition from build_knowledge to render_output (no human confirmation)

**Steps:**
```gherkin
Given behavior is 'discovery'
And build_knowledge action is complete
And build_knowledge/action configuration specifies auto_progress=true
When build_knowledge action finalizes
Then Action saves Workflow State with:
  - current_behavior='story_bot.discovery'
  - current_action='story_bot.discovery.build_knowledge'
  - timestamp=[completion time]
And Action loads build_knowledge/action configuration
And Action reads next_action='render_output' and auto_progress=true
And Action injects AI instructions: "Automatically proceed to render_output now (no human confirmation needed)"
And AI immediately invokes render_output tool without waiting for user
And Workflow transitions automatically to render_output
```

### Scenario: Auto_progress distinguishes build_knowledge from other actions

**Steps:**
```gherkin
Given gather_context action requires human confirmation (auto_progress not set)
And decide_planning_criteria action requires human confirmation (auto_progress not set)
And build_knowledge action specifies auto_progress=true
When build_knowledge completes
Then build_knowledge proceeds to render_output automatically
And User is NOT prompted to say "done" before transition
And Workflow is more efficient due to automatic progression
```

### Scenario: Workflow state captures build_knowledge completion before auto-transition

**Steps:**
```gherkin
Given build_knowledge action completes at timestamp='2025-12-03T10:50:00Z'
And auto_progress=true is configured
When Action saves workflow state before transitioning
Then workflow state is updated with:
  - current_action='story_bot.exploration.build_knowledge'
  - timestamp='2025-12-03T10:50:00Z'
And completed_actions list includes: {action_state: 'story_bot.exploration.build_knowledge', timestamp: '2025-12-03T10:50:00Z'}
And State persists BEFORE automatic transition to render_output
And If workflow is interrupted during transition, build_knowledge is marked as completed
```

### Scenario: Next action instructions indicate automatic progression

**Steps:**
```gherkin
Given build_knowledge action is complete
And build_knowledge/action configuration specifies auto_progress=true, next_action='render_output'
When Action injects next action instructions
Then AI context receives: "Automatically proceed to render_output now (no human confirmation needed)"
And AI understands to invoke render_output immediately
And User sees seamless transition without being prompted
And Automatic progression is clearly communicated
```

### Scenario: Workflow resumes at render_output after interruption during auto-transition

**Steps:**
```gherkin
Given workflow state shows: current_action='story_bot.discovery.build_knowledge'
And completed_actions contains build_knowledge entry
And render_output has not yet started
And chat session was interrupted during transition
When user reopens chat and invokes bot tool
Then Router loads workflow state
And Router sees build_knowledge is completed
And Router determines next action is render_output
And Router forwards to render_output action
And Workflow resumes at render_output despite interruption during auto-transition
```

### Scenario: Activity log records automatic transition

**Steps:**
```gherkin
Given build_knowledge action completes at 10:50:00
And auto_progress=true triggers automatic transition
When build_knowledge saves state and auto-progresses
Then Activity log records:
  - build_knowledge completion entry with action_state='story_bot.discovery.build_knowledge', duration=1200
  - Workflow state update showing automatic transition to render_output
  - Note indicating auto_progress was enabled
And Audit trail distinguishes automatic vs manual transitions
```

### Scenario: Auto-transition fails gracefully if render_output unavailable

**Steps:**
```gherkin
Given build_knowledge completes with auto_progress=true
And render_output tool is unavailable or disabled
When Action attempts automatic transition
Then Action detects render_output tool unavailable
And Action warns user in chat: "Cannot auto-progress to render_output. Tool unavailable." (non-blocking)
And Action saves workflow state with build_knowledge completed
And Workflow pauses at build_knowledge completion
And User can manually invoke render_output when available
```

## Generated Artifacts

### Updated Workflow State
**Updated by:** BuildKnowledgeAction on completion (before auto-transition)  
**Location:** {project_area}/workflow state  
**Content:**
- current_action updated to '<bot>.<behavior>.build_knowledge'
- completed_actions list appended with full path build_knowledge entry
- timestamp updated to completion time

### Injected AI Instructions
**Injected by:** BuildKnowledgeAction on completion  
**Content:** "Automatically proceed to render_output now (no human confirmation needed)"

## Notes

- auto_progress=true enables automatic transition without human confirmation
- Workflow state saved BEFORE automatic transition (ensures consistency)
- AI follows injected instructions to save knowledge content (no automatic submission)
- Automatic progression improves workflow efficiency for deterministic transitions
- Router handles interruption during auto-transition gracefully
- Activity log distinguishes automatic vs manual transitions
- Failure to auto-progress is non-blocking: warn user and pause at current action

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Build Knowledge feature, Domain Concepts (Seamless Transition, Sequential Flow, State Persistence)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria with special focus on auto_progress feature enabling automatic transitions


