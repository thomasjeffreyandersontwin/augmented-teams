# 📝 Saves Behavior State

**Navigation:** [📋 Story Map](../../story-map.txt) | [⚙️ Feature Overview](../README.md)

**Epic:** Invoke MCP Bot Server
**Feature:** Perform Behavior Action

## Story Description

Bot Behavior persists workflow state at action start and completion so that users can resume workflows after interruptions and have full audit trail of workflow progress.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action execution starts, **then** Behavior updates Workflow State with current_behavior and current_action (full paths)
- **When** Action execution completes, **then** Behavior updates Workflow State and appends to completed_actions
- **State persisted to {project_area}/workflow state file**
- **State includes timestamp of last action execution**
- **State includes completed_actions list showing full history with full paths and timestamps**
- **State includes current_behavior (full path)**
- **State includes current_action (full path)**
- **Persistence ensures workflow can be resumed after interruption (crash, close chat, etc.)**

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given Workflow State is persisted to project_area/workflow state
And workflow state contains: current_behavior (full path), current_action (full path), completed_actions[], timestamp
And completed_actions contains: [{action_state (full path), timestamp, duration}]
```

## Scenarios

### Scenario: State persisted when action starts

**Steps:**
```gherkin
Given behavior is 'discovery'
And action is 'gather_context'
And gather_context has not yet started
When gather_context action starts
Then Behavior updates workflow state with:
  - current_behavior='story_bot.discovery'
  - current_action='story_bot.discovery.gather_context'
  - timestamp=[current timestamp]
And workflow state is written to project_area/workflow state
And State persists to disk before action logic executes
```

### Scenario: State updated when action completes

**Steps:**
```gherkin
Given workflow state shows: current_behavior='story_bot.discovery', current_action='story_bot.discovery.gather_context'
And gather_context is in progress
When gather_context action completes
Then Behavior updates workflow state with:
  - timestamp=[completion timestamp]
And Behavior appends to completed_actions list: {action_state: 'story_bot.discovery.gather_context', timestamp: [completion timestamp]}
And workflow state is written to project_area/workflow state
And State reflects successful completion
```

### Scenario: Completed actions list maintains full audit trail

**Steps:**
```gherkin
Given completed_actions contains: gather_context, decide_planning_criteria (2 entries)
And workflow state shows current_action='story_bot.exploration.build_knowledge'
When build_knowledge action completes
Then Behavior appends to completed_actions: {action_state: 'story_bot.exploration.build_knowledge', timestamp: [timestamp]}
And completed_actions list now contains 3 entries
And completed_actions maintains chronological order
And Each entry includes: action_state (full path), timestamp
And Audit trail shows complete workflow history
```

### Scenario: Resume workflow after interruption (action started but not completed)

**Steps:**
```gherkin
Given workflow state has: current_behavior='story_bot.shape', current_action='story_bot.shape.decide_planning_criteria', timestamp='2025-12-03T10:00:00Z'
And completed_actions does NOT contain decide_planning_criteria entry
And user's chat crashed or closed during decide_planning_criteria execution
And user reopens chat and invokes bot tool
When Router loads workflow state
Then Router detects current_action not in completed_actions (started but not completed)
And Router presents to user: "decide_planning_criteria was started but not completed. Retry or continue?"
And If user chooses retry: Behavior restarts decide_planning_criteria from beginning
And If user chooses continue: Behavior attempts to continue from where it left off
And User can resume workflow despite interruption
```

### Scenario: State persists across chat sessions

**Steps:**
```gherkin
Given workflow state has: current_behavior='story_bot.discovery', current_action='story_bot.discovery.build_knowledge', timestamp='2025-12-03T09:00:00Z'
And user closed chat window after completing build_knowledge
And user opens new chat session hours later
When user invokes bot tool in new session
Then Router loads workflow state from persistent storage
And Router extracts current_behavior='story_bot.discovery', current_action='story_bot.discovery.build_knowledge'
And Router determines next action is render_output (per action configuration)
And Workflow resumes seamlessly from where user left off hours ago
And Persistence ensures workflow continuity across sessions
```

### Scenario: State handles workflow restart (first action)

**Steps:**
```gherkin
Given workflow state does NOT exist
And user is starting new workflow
When first action (gather_context) starts
Then Behavior creates new workflow state with:
  - current_behavior='story_bot.shape' (first behavior)
  - current_action='story_bot.shape.gather_context' (first action)
  - completed_actions=[] (empty)
  - timestamp=[current timestamp]
And workflow state is saved to project_area/
And Fresh workflow state is initialized
```

### Scenario: State tracks multiple completed actions with timestamps

**Steps:**
```gherkin
Given completed_actions contains 3 entries: gather_context (10:00), decide_planning_criteria (10:15), build_knowledge (10:30)
And workflow state shows current_action='story_bot.exploration.build_knowledge'
When render_output action starts at 10:45
Then Behavior updates workflow state with:
  - current_action='story_bot.exploration.render_output'
  - timestamp='2025-12-03T10:45:00Z'
And completed_actions list still contains 3 previous entries with original timestamps
And State shows full chronological history of workflow progression
```

### Scenario: State handles file write failure gracefully

**Steps:**
```gherkin
Given workflow state shows: current_action='story_bot.exploration.validate_rules'
And validate_rules action is complete
And project_area/workflow state file is write-protected or disk is full
When Behavior attempts to save workflow state
Then Behavior detects file write error
And Behavior warns user in chat: "Unable to save workflow state. Progress may not be preserved." (non-blocking)
And Action execution continues despite state persistence failure
And Workflow is not blocked by state save failure
```

### Scenario: State includes duration for completed actions

**Steps:**
```gherkin
Given gather_context action started at timestamp='2025-12-03T10:00:00Z'
When gather_context action completes at timestamp='2025-12-03T10:05:30Z'
Then Behavior calculates duration: 330 seconds (5.5 minutes)
And Behavior updates completed_actions with: {action_state: 'story_bot.shape.gather_context', timestamp: '2025-12-03T10:05:30Z', duration: 330}
And Duration provides performance metrics for workflow analysis
```

## Generated Artifacts

### Workflow State File (workflow state)
**Created by:** Behavior on first action start  
**Updated by:** Behavior on every action start and completion  
**Location:** {project_area}/workflow state  
**Content:**
```json
{
  "current_behavior": "story_bot.discovery",
  "current_action": "story_bot.discovery.build_knowledge",
  "timestamp": "2025-12-03T10:30:00Z",
  "completed_actions": [
    {
      "action_state": "story_bot.discovery.gather_context",
      "timestamp": "2025-12-03T10:00:00Z",
      "duration": 180
    },
    {
      "action_state": "story_bot.discovery.decide_planning_criteria",
      "timestamp": "2025-12-03T10:15:00Z",
      "duration": 240
    }
  ]
}
```

## Notes

- State is updated when action starts and when action completes
- Interrupted workflows detected by checking if current_action is in completed_actions
- completed_actions provides full audit trail with full paths, timestamps and durations
- File write failures are non-blocking: warn user but continue execution
- State persistence enables resumption after crash, chat closure, or any interruption
- Duration tracking provides insights into action execution performance
- Full path format (bot.behavior.action) ensures precise state tracking

---

## Source Material

**Primary Source:** agile_bot/bots/base_bot/docs/stories/increment-3-exploration.txt  
**Sections Referenced:** Perform Behavior Action feature, Domain Concepts (Workflow State, Action Execution State, State Persistence, Auto Resume, Audit Trail)  
**Date Generated:** 2025-12-03  
**Context Note:** Scenarios generated from acceptance criteria and domain rules in increment 3 exploration document


