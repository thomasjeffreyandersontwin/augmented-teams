# 📝 Store Scope Context

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Execute Workflow Operations (Mock)
**User:** Bot
**Sequential Order:** 10
**Story Type:** system

## Story Description

Store Scope Context functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Bot receives Scope in context
  **then** Bot stores scope parameters (filter criteria) in BehaviorActionState
  **and** Bot does NOT store resolved/matched items

- **When** BehaviorActionState is updated
  **then** Bot persists scope parameters to storage

- **When** scope parameters are used in subsequent actions
  **then** Bot re-evaluates parameters against current knowledge source
  **and** newly added content matching parameters is automatically included

## Scenarios

### Scenario: Bot stores scope parameters not resolved results (happy_path)

**Steps:**
```gherkin
Given story graph contains increment 11 with 3 stories: Story A, Story B, Story C
And Bot has current behavior "shape" and action "build"
And ActionContext contains scope with type "increment" and value [11]
When Bot receives ActionContext for instruction operation
Then Bot stores scope parameters in BehaviorActionState
And BehaviorActionState.scope contains type="increment" and value=[11]
And BehaviorActionState.scope does NOT contain resolved stories [Story A, Story B, Story C]
```


### Scenario: Bot persists scope parameters to state file (happy_path)

**Steps:**
```gherkin
Given Bot has current behavior "shape" and action "build"
And ActionContext contains scope with type "epic" and value ["Run Interactive REPL"]
When Bot stores scope parameters in BehaviorActionState
Then Bot persists BehaviorActionState to behavior_action_state.json
And behavior_action_state.json contains scope parameters: type="epic", value=["Run Interactive REPL"]
```


### Scenario: Stored scope parameters find newly added content on subsequent action (happy_path)

**Steps:**
```gherkin
Given story graph contains increment 11 with 3 stories: Provide Context, Store Scope, Get Instructions
And Bot has persisted BehaviorActionState with scope type "increment" and value [11]
And user completes build action and confirms
And Bot advances to validate action
And meanwhile, new story "Loop Back To Display" is added to increment 11
When Bot executes validate.instructions with stored scope parameters
Then Bot re-evaluates scope parameters against current story graph
And Bot finds 4 matching stories: Provide Context, Store Scope, Get Instructions, Loop Back To Display
And Action receives ActionContext with all 4 stories in scope
```


### Scenario: Stored file scope parameters find newly added files on subsequent action (happy_path)

**Steps:**
```gherkin
Given workspace contains src/bot/ with files: bot.py, behavior.py
And Bot has persisted BehaviorActionState with scope type "files" and value ["src/bot/"]
And user completes build action and confirms
And Bot advances to validate action
And meanwhile, new file action.py is added to src/bot/
When Bot executes validate.instructions with stored scope parameters
Then Bot re-evaluates scope parameters against current workspace
And Bot finds 3 matching files: bot.py, behavior.py, action.py
And Action receives ActionContext with all 3 files in scope
```

