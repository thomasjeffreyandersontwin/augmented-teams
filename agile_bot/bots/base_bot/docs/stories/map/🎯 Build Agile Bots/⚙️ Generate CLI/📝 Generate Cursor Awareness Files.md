# 📝 Generate Cursor Awareness Files

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Build Agile Bots
**Feature:** Generate CLI
**User:** MCP Server Generator
**Sequential Order:** 4
**Story Type:** user

## Story Description

Generate Cursor Awareness Files functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Generator runs generate_awareness_files() method

  **then** Generator creates workspace rules file with trigger patterns

  **and** File includes bot name and behavior descriptions

  **and** File includes trigger words sectioned by behavior

## Scenarios

### Scenario: Generate Cursor Awareness Files (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
