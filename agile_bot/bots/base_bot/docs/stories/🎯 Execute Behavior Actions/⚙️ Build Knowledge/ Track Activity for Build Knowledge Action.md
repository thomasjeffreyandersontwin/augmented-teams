# 📝 Track Activity for Build Knowledge Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Build Knowledge

## Story Description

BuildKnowledgeAction tracks activity during execution so that all build_knowledge action invocations are logged to activity log with timestamps, inputs, outputs, and duration for auditing and debugging.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BuildKnowledgeAction executes, **then** Action tracks activity (per "Track Activity for Action Execution" story in Perform Behavior Action feature)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given activity log is initialized at project_area/activity log
And BuildKnowledgeAction is initialized within a behavior (shape, discovery, exploration, or scenarios)
```

## Scenarios

### Scenario: Track activity when build_knowledge action starts

**Steps:**
```gherkin
Given behavior is 'scenarios'
And action is 'build_knowledge'
When build_knowledge action starts execution
Then Activity logger creates entry with:
  - timestamp=[start timestamp]
  - action_state='story_bot.scenarios.build_knowledge'
  - inputs={criteria_count: 4, assumptions_count: 2, context_file_path: "planning.json"}
And Entry is appended to activity log at project_area/
And Activity log records action initiation
```

### Scenario: Track activity when build_knowledge action completes

**Steps:**
```gherkin
Given build_knowledge action started at timestamp='2025-12-03T10:30:00Z'
And activity log has entry for build_knowledge
When build_knowledge action finishes execution at timestamp='2025-12-03T10:50:00Z'
Then Activity logger creates completion entry with:
  - action_state='story_bot.scenarios.build_knowledge'
  - outputs={concepts_count: 15, relationships_count: 30, rules_count: 8, file_path: "knowledge_graph.json"}
  - duration=1200 (seconds: 20 minutes)
And Entry is appended to activity log
And Activity log shows complete execution record with duration
```

### Scenario: Track knowledge building inputs from previous actions

**Steps:**
```gherkin
Given gather_context outputs are available in clarifications.json
And decide_planning_criteria outputs are available in planning.json  
And behavior is 'scenarios'
When build_knowledge action starts
Then Activity logger captures inputs including:
  - context_from="gather_context and decide_planning_criteria"
  - questions_count=5
  - criteria_count=4
  - assumptions_count=2
And Inputs show connection to previous actions
And Activity log traces workflow dependencies
```

### Scenario: Track knowledge graph outputs

**Steps:**
```gherkin
Given build_knowledge action is complete
And Knowledge graph contains: 15 concepts, 30 relationships, 8 rules
When Activity logger records completion
Then Activity logger captures outputs including:
  - concepts_count=15
  - relationships_count=30
  - rules_count=8
  - file_path="knowledge_graph.json"
  - summary="Built domain knowledge graph for increment 3"
And Outputs capture counts and file paths, not full graph content
And Activity log shows metrics of what knowledge artifacts were produced
```

### Scenario: Activity log maintains sequence through build_knowledge

**Steps:**
```gherkin
Given activity log contains entries for:
  - gather_context (completed at 10:05:30)
  - decide_planning_criteria (completed at 10:25:00)
And build_knowledge completes at 10:50:00
When Activity logger appends build_knowledge entry
Then Activity log shows chronological sequence:
  1. gather_context (10:00:00 - 10:05:30)
  2. decide_planning_criteria (10:15:00 - 10:25:00)
  3. build_knowledge (10:30:00 - 10:50:00)
And Activity log demonstrates workflow progression through knowledge building
```

### Scenario: Track multiple build_knowledge invocations across behaviors

**Steps:**
```gherkin
Given activity log contains entry for story_bot.shape.build_knowledge completed at 09:30
And activity log contains entry for story_bot.exploration.build_knowledge completed at 10:30
When both entries are present in activity log
Then activity log contains 2 separate entries:
  - Entry 1: action_state='story_bot.shape.build_knowledge', timestamp='2025-12-03T09:30:00Z'
  - Entry 2: action_state='story_bot.exploration.build_knowledge', timestamp='2025-12-03T10:30:00Z'
And Each entry has its own inputs, outputs, and duration
And Activity log distinguishes same action in different behaviors
```

### Scenario: Activity log handles file write failure gracefully

**Steps:**
```gherkin
Given build_knowledge action is completing
And project_area/activity log file is write-protected
When Activity logger attempts to append entry
Then Activity logger detects file write error
And Activity logger warns user in chat: "Unable to log activity. Audit trail may be incomplete." (non-blocking)
And build_knowledge action continues execution despite logging failure
And Action is not blocked by activity logging failure
```

## Generated Artifacts

### Activity Log File (activity log)
**Updated by:** BuildKnowledgeAction execution (start and completion)  
**Location:** {project_area}/activity log  
**Content:**
```json
[
  {
    "timestamp": "2025-12-03T10:30:00Z",
    "action_state": "story_bot.scenarios.build_knowledge",
    "inputs": {
      "questions_count": 5,
      "criteria_count": 4,
      "assumptions_count": 2,
      "context_file_path": "planning.json"
    }
  },
  {
    "timestamp": "2025-12-03T10:50:00Z",
    "action_state": "story_bot.scenarios.build_knowledge",
    "outputs": {
      "concepts_count": 15,
      "relationships_count": 30,
      "rules_count": 8,
      "file_path": "knowledge_graph.json",
      "summary": "Built domain knowledge graph for increment 3"
    },
    "duration": 1200
  }
]
```

## Notes

- Activity tracking records BOTH action start and action completion
- Inputs show connection to previous actions (gather_context, decide_planning_criteria)
- Outputs capture knowledge graph artifacts (concepts, relationships, rules)
- Duration provides performance metrics for knowledge building stage
- File write failures are non-blocking: warn user but continue execution
- Activity log maintains chronological sequence showing workflow progression

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Build Knowledge feature, Domain Concepts (Activity Log, Audit Trail)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing generic "Track Activity for Action Execution" story


