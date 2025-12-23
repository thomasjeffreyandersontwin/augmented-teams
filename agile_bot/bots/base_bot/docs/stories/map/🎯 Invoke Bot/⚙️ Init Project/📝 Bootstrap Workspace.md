# 📝 Bootstrap Workspace

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Invoke Bot
**Feature:** Init Project
**User:** Bot Developer
**Sequential Order:** 7
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
