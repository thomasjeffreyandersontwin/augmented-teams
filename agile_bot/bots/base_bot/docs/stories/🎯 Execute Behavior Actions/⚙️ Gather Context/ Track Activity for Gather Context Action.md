# 📝 GatherContextAction --> Track Activity for Gather Context Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Gather Context

## Story Description

GatherContextAction tracks activity during execution so that all gather_context action invocations are logged to activity log with timestamps, inputs, outputs, and duration for auditing and debugging.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** GatherContextAction executes, **then** Action tracks activity (per "Track Activity for Action Execution" story in Perform Behavior Action feature)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given activity log is initialized at project_area/activity log
And GatherContextAction is initialized within a behavior (shape, discovery, exploration, or scenarios)
```

## Scenarios

### Scenario: Track activity when gather_context action starts

**Steps:**
```gherkin
Given behavior is 'discovery'
And action is 'gather_context'
When gather_context action starts execution
Then Activity logger creates entry with:
  - timestamp=[start timestamp]
  - action_state='story_bot.discovery.gather_context'
  - inputs={source_files_count: 2, context_type: "exploration"}
And Entry is appended to activity log at project_area/
And Activity log records action initiation
```

### Scenario: Track activity when gather_context action completes

**Steps:**
```gherkin
Given gather_context action started at timestamp='2025-12-03T10:00:00Z'
And activity log has entry for gather_context  
When gather_context action finishes execution at timestamp='2025-12-03T10:05:30Z'
Then Activity logger creates completion entry with:
  - action_state='story_bot.discovery.gather_context'
  - outputs={questions_count: 5, evidence_count: 3, file_path: "clarifications.json"}
  - duration=330 (seconds: 5.5 minutes)
And Entry is appended to activity log
And Activity log shows complete execution record with metrics and file path
```

### Scenario: Track multiple gather_context invocations across behaviors

**Steps:**
```gherkin
Given activity log contains entry for story_bot.shape.gather_context completed at 09:00
And activity log contains entry for story_bot.discovery.gather_context completed at 10:00
When both entries are present in activity log
Then activity log contains 2 separate entries:
  - Entry 1: action_state='story_bot.shape.gather_context', timestamp='2025-12-03T09:00:00Z'
  - Entry 2: action_state='story_bot.discovery.gather_context', timestamp='2025-12-03T10:00:00Z'
And Each entry has its own inputs (metrics/paths), outputs (metrics/paths), and duration
And Activity log distinguishes same action in different behaviors using full path
```

### Scenario: Track activity with user-provided context inputs

**Steps:**
```gherkin
Given user context is available: story map document, increment details, source material
And behavior is 'exploration'
When gather_context action starts
Then Activity logger records inputs including:
  - source_files_count=3
  - source_files_paths=["story-map.txt", "increment-2.txt", "source-material.md"]
  - context_type="exploration"
And Inputs capture file paths and counts, not full content
And Activity log tracks what context was provided
```

### Scenario: Track activity with gathered outputs

**Steps:**
```gherkin
Given gather_context action completion is ready to log
And Action results include: 5 key questions, 3 evidence items, 2 assumptions
When Activity logger records completion
Then Activity logger captures outputs including:
  - questions_count=5
  - evidence_count=3
  - assumptions_count=2
  - file_path="clarifications.json"
  - summary="Gathered context for 3 stories in increment 2"
And Outputs capture counts and file paths, not full content
And Activity log shows metrics of what was produced
```

### Scenario: Activity log handles file write failure gracefully

**Steps:**
```gherkin
Given gather_context action is completing
And project_area/activity log file is write-protected
When Activity logger attempts to append entry
Then Activity logger detects file write error
And Activity logger warns user in chat: "Unable to log activity. Audit trail may be incomplete." (non-blocking)
And gather_context action continues execution despite logging failure
And Action is not blocked by activity logging failure
```

### Scenario: Activity log maintains chronological order

**Steps:**
```gherkin
Given activity log contains 10 previous action entries
And gather_context action completes at timestamp='2025-12-03T10:30:00Z'
When Activity logger appends gather_context entry
Then New entry is appended to end of activity log array
And Activity log maintains chronological order by timestamp
And Most recent actions appear at end of log
```

## Generated Artifacts

### Activity Log File (activity log)
**Created by:** First action execution in workflow  
**Updated by:** Every action execution (start and completion)  
**Location:** {project_area}/activity log  
**Content:**
```json
[
  {
    "timestamp": "2025-12-03T10:00:00Z",
    "action_state": "story_bot.discovery.gather_context",
    "inputs": {
      "source_files_count": 2,
      "source_files_paths": ["story-map.txt", "increment-2-exploration.txt"],
      "context_type": "discovery"
    }
  },
  {
    "timestamp": "2025-12-03T10:05:30Z",
    "action_state": "story_bot.discovery.gather_context",
    "outputs": {
      "questions_count": 5,
      "evidence_count": 3,
      "file_path": "clarifications.json",
      "summary": "Gathered context successfully"
    },
    "duration": 330
  }
]
```

## Notes

- Activity tracking records BOTH action start and action completion
- Each entry includes timestamp, behavior, action, state, inputs, outputs, duration
- Activity log provides complete audit trail for debugging and analysis
- File write failures are non-blocking: warn user but continue execution
- Same action in different behaviors creates separate entries
- Activity log is append-only: maintains chronological history

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Gather Context feature, Domain Concepts (Activity Log, Audit Trail)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing generic "Track Activity for Action Execution" story


