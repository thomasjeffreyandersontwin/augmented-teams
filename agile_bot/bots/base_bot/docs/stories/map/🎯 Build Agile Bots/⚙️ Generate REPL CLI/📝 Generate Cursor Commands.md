# 📝 Generate Cursor Commands

**Navigation:** [📋 Story Map](../../../story-map-outline.drawio) | [⚙️ Feature Overview](../../../../README.md)

**Epic:** Build Agile Bots
**Feature:** Generate REPL CLI
**User:** Generator
**Sequential Order:** 3
**Story Type:** user

## Story Description

Generate Cursor Commands functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** generator creates CursorReplVisitor,
  **then** it follows existing visitor pattern

- **When** visitor generates shortcuts,
  **then** it creates navigate shortcuts for behaviors

- **When** visitor generates action shortcuts,
  **then** it creates shortcuts for behavior-action combinations

- **When** visitor generates help shortcuts,
  **then** it creates help and status commands

## Scenarios

### Scenario: Generate Cursor Commands (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
