# 📝 Track Activity for Planning Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Decide Planning Criteria

## Story Description

PlanningAction tracks activity during execution so that all decide_planning_criteria action invocations are logged to activity log with timestamps, inputs, outputs, and duration for auditing and debugging.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** PlanningAction executes, **then** Action tracks activity (per "Track Activity for Action Execution" story in Perform Behavior Action feature)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given activity log is located at project_area/activity log
And activity log tracks: timestamp, action_state (full path), inputs (metrics/paths), outputs (metrics/paths), duration
And PlanningAction is initialized within a behavior (shape, discovery, exploration, or scenarios)
```

## Scenarios

### Scenario: Track activity when planning action starts

**Steps:**
```gherkin
Given behavior is 'exploration'
And action is 'decide_planning_criteria'
When decide_planning_criteria action starts execution
Then Activity logger creates entry with:
  - timestamp=[start timestamp]
  - action_state='story_bot.exploration.decide_planning_criteria'
  - inputs={questions_count: 5, evidence_count: 3, context_file_path: "clarifications.json"}
And Entry is appended to activity log at project_area/
And Activity log records action initiation
```

### Scenario: Track activity when planning action completes

**Steps:**
```gherkin
Given decide_planning_criteria action started at timestamp='2025-12-03T10:15:00Z'
And activity log has entry for decide_planning_criteria
When decide_planning_criteria action finishes execution at timestamp='2025-12-03T10:25:00Z'
Then Activity logger creates completion entry with:
  - action_state='story_bot.exploration.decide_planning_criteria'
  - outputs={criteria_count: 4, assumptions_count: 2, decisions_count: 3, file_path: "planning.json"}
  - duration=600 (seconds: 10 minutes)
And Entry is appended to activity log
And Activity log shows complete execution record with duration
```

### Scenario: Track planning inputs from previous gather_context

**Steps:**
```gherkin
Given gather_context outputs are available: 5 questions, 3 evidence items in clarifications.json
And behavior is 'exploration'
When decide_planning_criteria action starts
Then Activity logger captures inputs including:
  - gathered_questions=5
  - gathered_evidence=3
  - context_from="gather_context action output"
And Inputs show connection to previous action
And Activity log traces workflow dependencies
```

### Scenario: Track planning outputs (criteria and assumptions)

**Steps:**
```gherkin
Given decide_planning_criteria action is complete
And Action results include: 4 planning criteria, 2 assumptions, 3 decisions
When Activity logger records completion
Then Activity logger captures outputs including:
  - criteria_count=4
  - assumptions_count=2
  - decisions_count=3
  - summary="Defined planning approach for increment 3"
And Outputs are captured in activity log entry
And Activity log shows what planning artifacts were produced
```

### Scenario: Activity log maintains sequence across actions

**Steps:**
```gherkin
Given activity log contains entry for gather_context (completed at 10:05:30)
And decide_planning_criteria completes at 10:25:00
When Activity logger appends decide_planning_criteria entry
Then Activity log shows chronological sequence:
  1. gather_context started (10:00:00)
  2. gather_context completed (10:05:30)
  3. decide_planning_criteria started (10:15:00)
  4. decide_planning_criteria completed (10:25:00)
And Activity log demonstrates workflow progression
```

### Scenario: Track multiple planning invocations across behaviors

**Steps:**
```gherkin
Given activity log contains entry for story_bot.shape.decide_planning_criteria completed at 09:20
And activity log contains entry for story_bot.discovery.decide_planning_criteria completed at 10:15
When both entries are present in activity log
Then activity log contains 2 separate entries:
  - Entry 1: action_state='story_bot.shape.decide_planning_criteria', timestamp='2025-12-03T09:20:00Z'
  - Entry 2: action_state='story_bot.discovery.decide_planning_criteria', timestamp='2025-12-03T10:15:00Z'
And Each entry has its own inputs (metrics/paths), outputs (metrics/paths), and duration
And Activity log distinguishes same action in different behaviors
```

### Scenario: Activity log handles file write failure gracefully

**Steps:**
```gherkin
Given decide_planning_criteria action is completing
And project_area/activity log file is write-protected
When Activity logger attempts to append entry
Then Activity logger detects file write error
And Activity logger warns user in chat: "Unable to log activity. Audit trail may be incomplete." (non-blocking)
And decide_planning_criteria action continues execution despite logging failure
And Action is not blocked by activity logging failure
```

## Generated Artifacts

### Activity Log File (activity log)
**Updated by:** PlanningAction execution (start and completion)  
**Location:** {project_area}/activity log  
**Content:**
```json
[
  {
    "timestamp": "2025-12-03T10:15:00Z",
    "action_state": "story_bot.exploration.decide_planning_criteria",
    "inputs": {
      "questions_count": 5,
      "evidence_count": 3,
      "context_file_path": "clarifications.json"
    }
  },
  {
    "timestamp": "2025-12-03T10:25:00Z",
    "action_state": "story_bot.exploration.decide_planning_criteria",
    "outputs": {
      "criteria_count": 4,
      "assumptions_count": 2,
      "decisions_count": 3,
      "file_path": "planning.json",
      "summary": "Defined planning approach for increment 3"
    },
    "duration": 600
  }
]
```

## Notes

- Activity tracking records BOTH action start and action completion
- Inputs show connection to previous action outputs (workflow dependencies)
- Outputs capture planning artifacts (criteria, assumptions, decisions)
- Duration provides performance metrics for planning stage
- File write failures are non-blocking: warn user but continue execution
- Activity log maintains chronological sequence showing workflow progression

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Decide Planning Criteria feature, Domain Concepts (Activity Log, Audit Trail)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing generic "Track Activity for Action Execution" story


