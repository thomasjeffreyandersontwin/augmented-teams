# 📝 Track Activity for Validate Rules Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Execute Behavior Actions
**Feature:** Validate Knowledge & Content Against Rules

## Story Description

ValidateRulesAction tracks activity during execution so that all validate_rules action invocations are logged to activity log with timestamps, inputs, outputs, and duration for auditing and debugging.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** ValidateRulesAction executes, **then** Action tracks activity (per "Track Activity for Action Execution" story in Perform Behavior Action feature)

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given activity log is located at project_area/activity log
And activity log tracks: timestamp, action_state (full path), inputs (metrics/paths), outputs (metrics/paths), duration
And ValidateRulesAction is initialized within a behavior (shape, discovery, exploration, or scenarios)
```

## Scenarios

### Scenario: Track activity when validate_rules action starts

**Steps:**
```gherkin
Given behavior is 'scenarios'
And action is 'validate_rules'
When validate_rules action starts execution
Then Activity logger creates entry with:
  - timestamp=[start timestamp]
  - action_state='story_bot.scenarios.validate_rules'
  - inputs={documents_count: 6, rules_files_paths: ["story-scenarios-rules.json", "story-structure-rules.json"]}
And Entry is appended to activity log at project_area/
And Activity log records action initiation
```

### Scenario: Track activity when validate_rules action completes

**Steps:**
```gherkin
Given validate_rules action started at timestamp='2025-12-03T11:00:00Z'
And activity log has entry for validate_rules
When validate_rules action finishes execution at timestamp='2025-12-03T11:10:00Z'
Then Activity logger creates completion entry with:
  - action_state='story_bot.scenarios.validate_rules'
  - outputs={violations_count: 3, rules_passed: 15, report_path: "validation_report.json"}
  - duration=600 (seconds: 10 minutes)
And Entry is appended to activity log
And Activity log shows complete execution record with duration
```

### Scenario: Track validation inputs from rendered content

**Steps:**
```gherkin
Given rendered documents are available: 6 documents in docs/stories/
And behavior is 'scenarios'
When validate_rules action starts
Then Activity logger captures inputs including:
  - documents_count=6
  - documents_paths=["story-1.md", "story-2.md", "story-3.md"]
  - rules_files_paths=["story-scenarios-rules.json", "story-structure-rules.json"]
And Inputs capture file paths and counts, not full content
And Activity log traces workflow dependencies
```

### Scenario: Track validation outputs (results and violations)

**Steps:**
```gherkin
Given validate_rules action is complete
And Validation results show: 6 documents, 3 violations, 15 rules passed
When Activity logger records completion
Then Activity logger captures outputs including:
  - documents_validated=6
  - violations_count=3
  - rules_passed=15
  - report_path="validation_report.json"
  - summary="Validation completed with 3 violations"
And Outputs capture counts and file paths, not full report content
And Activity log shows metrics of what validation results were produced
```

### Scenario: Activity log shows complete workflow sequence

**Steps:**
```gherkin
Given activity log contains entries for:
  - gather_context (completed at 10:05:30)
  - decide_planning_criteria (completed at 10:25:00)
  - build_knowledge (completed at 10:50:00)
  - render_output (completed at 11:00:00)
And validate_rules completes at 11:10:00
When Activity logger appends validate_rules entry
Then Activity log shows complete workflow sequence:
  1. gather_context (10:00:00 - 10:05:30)
  2. decide_planning_criteria (10:15:00 - 10:25:00)
  3. build_knowledge (10:30:00 - 10:50:00)
  4. render_output (10:50:00 - 11:00:00)
  5. validate_rules (11:00:00 - 11:10:00)
And Activity log demonstrates complete workflow from start to finish
```

### Scenario: Track validate_rules as terminal action

**Steps:**
```gherkin
Given validate_rules action completes
And validate_rules/action configuration specifies next_action=null (terminal action)
When Activity logger records completion
Then Activity log entry includes note: "Terminal action - workflow complete"
And Activity log indicates this is final action in workflow
And Audit trail shows workflow reached its intended end
```

### Scenario: Track multiple validate_rules invocations across behaviors

**Steps:**
```gherkin
Given activity log contains entry for story_bot.shape.validate_rules completed at 09:55
And activity log contains entry for story_bot.exploration.validate_rules completed at 11:00
When both entries are present in activity log
Then activity log contains 2 separate entries:
  - Entry 1: action_state='story_bot.shape.validate_rules', timestamp='2025-12-03T09:55:00Z'
  - Entry 2: action_state='story_bot.exploration.validate_rules', timestamp='2025-12-03T11:00:00Z'
And Each entry has its own inputs, outputs, and duration
And Activity log distinguishes same action in different behaviors
```

### Scenario: Activity log handles file write failure gracefully

**Steps:**
```gherkin
Given validate_rules action is completing
And project_area/activity log file is write-protected
When Activity logger attempts to append entry
Then Activity logger detects file write error
And Activity logger warns user in chat: "Unable to log activity. Audit trail may be incomplete." (non-blocking)
And validate_rules action continues execution despite logging failure
And Action is not blocked by activity logging failure
```

## Generated Artifacts

### Activity Log File (activity log)
**Updated by:** ValidateRulesAction execution (start and completion)  
**Location:** {project_area}/activity log  
**Content:**
```json
[
  {
    "timestamp": "2025-12-03T11:00:00Z",
    "action_state": "story_bot.scenarios.validate_rules",
    "inputs": {
      "documents_count": 6,
      "documents_paths": ["story-1.md", "story-2.md", "story-3.md"],
      "rules_files_paths": ["story-scenarios-rules.json", "story-structure-rules.json"]
    }
  },
  {
    "timestamp": "2025-12-03T11:10:00Z",
    "action_state": "story_bot.scenarios.validate_rules",
    "outputs": {
      "documents_validated": 6,
      "violations_count": 3,
      "rules_passed": 15,
      "report_path": "validation_report.json",
      "summary": "Validation completed with 3 violations"
    },
    "duration": 600,
    "note": "Terminal action - workflow complete"
  }
]
```

## Notes

- Activity tracking records BOTH action start and action completion
- Inputs show connection to render_output (documents to validate)
- Outputs capture validation results (violations, passed rules, report)
- Duration provides performance metrics for validation stage
- Terminal action indicator shows workflow completion
- File write failures are non-blocking: warn user but continue execution
- Activity log maintains complete workflow sequence from gather_context through validate_rules

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Execute Behavior Actions > Validate Knowledge & Content Against Rules feature, Domain Concepts (Activity Log, Audit Trail)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria referencing generic "Track Activity for Action Execution" story


