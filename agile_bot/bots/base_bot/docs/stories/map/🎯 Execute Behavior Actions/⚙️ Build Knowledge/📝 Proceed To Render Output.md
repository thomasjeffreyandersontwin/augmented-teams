# 📝 Proceed To Render Output

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_build_knowledge.py#L255)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Build Knowledge](.)  
**Sequential Order:** 5
**Story Type:** user

## Story Description

Proceed To Render Output functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** BuildKnowledgeAction completes execution

  **then** BuildKnowledgeAction saves Workflow State (per "Saves Behavior State" story)

  **and** BuildKnowledgeAction processes content for saving

  **and** Workflow automatically proceeds to render_output (auto_progress: true, no human confirmation needed)

## Scenarios

### Scenario: Proceed To Render Output (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
