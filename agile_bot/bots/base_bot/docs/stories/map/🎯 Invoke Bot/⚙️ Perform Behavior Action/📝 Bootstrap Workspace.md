# 📝 Bootstrap Workspace

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_perform_behavior_action.py#L4697)

**User:** Bot Developer
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Perform Behavior Action](.)  
**Sequential Order:** 0.5
**Story Type:** user

## Story Description

Bootstrap Workspace functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Entry points (MCP/CLI) bootstrap environment

  **then** Environment is configured before importing modules

  **and** All directory resolution reads from environment variables only

  **and** agent.json provides default workspace location

  **and** Environment variables can override agent.json

## Scenarios

### Scenario: Bootstrap Workspace (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
