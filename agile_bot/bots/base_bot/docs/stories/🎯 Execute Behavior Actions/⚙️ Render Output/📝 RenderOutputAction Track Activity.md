# 📝 Track Activity for Render Output Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Render Output

## Story Description

RenderOutputAction tracks activity during execution so that all render_output action invocations are logged to activity log with timestamps, inputs, outputs, and duration for auditing and debugging.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** RenderOutputAction executes, **then** Action tracks activity (per "Track Activity for Action Execution" story in Perform Behavior Action feature)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given activity log is located at project_area/activity log
And activity log tracks: timestamp, action_state (full path), inputs (metrics/paths), outputs (metrics/paths), duration
And RenderOutputAction is initialized within a behavior (shape, discovery, exploration, or scenarios)
```

## Scenarios

### Scenario: Track activity when render_output action starts

**Steps:**
```gherkin
Given behavior is 'exploration'
And action is 'render_output'
When render_output action starts execution
Then Activity logger creates entry with:
  - timestamp=[start timestamp]
  - action_state='story_bot.exploration.render_output'
  - inputs={knowledge_graph_path: "knowledge_graph.json", templates_count: 2}
And Entry is appended to activity log at project_area/
And Activity log records action initiation
```

### Scenario: Track activity when render_output action completes

**Steps:**
```gherkin
Given render_output action started at timestamp='2025-12-03T10:50:00Z'
And activity log has entry for render_output
When render_output action finishes execution at timestamp='2025-12-03T11:00:00Z'
Then Activity logger creates completion entry with:
  - action_state='story_bot.exploration.render_output'
  - outputs={documents_generated: 6, file_paths: ["story-map.md", "increment-3.md", "story-1.md"]}
  - duration=600 (seconds: 10 minutes)
And Entry is appended to activity log
And Activity log shows complete execution record with duration
```

### Scenario: Track rendering inputs from knowledge graph

**Steps:**
```gherkin
Given knowledge_graph.json contains 15 concepts, 30 relationships
And behavior is 'exploration'
When render_output action starts
Then Activity logger captures inputs including:
  - knowledge_graph_path="knowledge_graph.json"
  - concepts_count=15
  - relationships_count=30
  - templates_count=2
And Inputs capture file paths and metrics, not full content
And Activity log traces workflow dependencies
```

### Scenario: Track rendered output artifacts

**Steps:**
```gherkin
Given render_output action is complete
And Rendered outputs include: 3 story documents, 1 story map, 2 increment documents
When Activity logger records completion
Then Activity logger captures outputs including:
  - documents_generated=6
  - file_paths=["story-map.md", "increment-3.md", "story-1.md", "story-2.md", "story-3.md", "structured.json"]
  - summary="Rendered output documents for increment 3"
And Outputs capture file paths and counts, not document content
And Activity log shows metrics of what rendering artifacts were produced
```

### Scenario: Activity log maintains sequence through render_output

**Steps:**
```gherkin
Given activity log contains entries for:
  - gather_context (completed at 10:05:30)
  - decide_planning_criteria (completed at 10:25:00)
  - build_knowledge (completed at 10:50:00)
And render_output completes at 11:00:00
When Activity logger appends render_output entry
Then Activity log shows chronological sequence:
  1. gather_context (10:00:00 - 10:05:30)
  2. decide_planning_criteria (10:15:00 - 10:25:00)
  3. build_knowledge (10:30:00 - 10:50:00)
  4. render_output (10:50:00 - 11:00:00)
And Activity log demonstrates workflow progression through rendering
```

### Scenario: Track multiple render_output invocations across behaviors

**Steps:**
```gherkin
Given activity log contains entry for story_bot.shape.render_output completed at 09:45
And activity log contains entry for story_bot.exploration.render_output completed at 10:50
When both entries are present in activity log
Then activity log contains 2 separate entries:
  - Entry 1: action_state='story_bot.shape.render_output', timestamp='2025-12-03T09:45:00Z'
  - Entry 2: action_state='story_bot.exploration.render_output', timestamp='2025-12-03T10:50:00Z'
And Each entry has its own inputs, outputs, and duration
And Activity log distinguishes same action in different behaviors
```

### Scenario: Activity log handles file write failure gracefully

**Steps:**
```gherkin
Given render_output action is completing
And project_area/activity log file is write-protected
When Activity logger attempts to append entry
Then Activity logger detects file write error
And Activity logger warns user in chat: "Unable to log activity. Audit trail may be incomplete." (non-blocking)
And render_output action continues execution despite logging failure
And Action is not blocked by activity logging failure
```

## Generated Artifacts

### Activity Log File (activity log)
**Updated by:** RenderOutputAction execution (start and completion)  
**Location:** {project_area}/activity log  
**Content:**
```json
[
  {
    "timestamp": "2025-12-03T10:50:00Z",
    "action_state": "story_bot.exploration.render_output",
    "inputs": {
      "knowledge_graph_path": "knowledge_graph.json",
      "concepts_count": 15,
      "relationships_count": 30,
      "templates_count": 2
    }
  },
  {
    "timestamp": "2025-12-03T11:00:00Z",
    "action_state": "story_bot.exploration.render_output",
    "outputs": {
      "documents_generated": 6,
      "file_paths": ["story-map.md", "increment-3.md", "story-1.md"],
      "summary": "Rendered output documents for increment 3"
    },
    "duration": 600
  }
]
```

## Notes

- Activity tracking records BOTH action start and action completion
- Inputs show connection to build_knowledge (knowledge graph source)
- Outputs capture rendered artifacts (documents, files, formats)
- Duration provides performance metrics for rendering stage
- File write failures are non-blocking: warn user but continue execution
- Activity log maintains chronological sequence showing workflow progression

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Render Output feature, Domain Concepts (Activity Log, Audit Trail)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing generic "Track Activity for Action Execution" story


