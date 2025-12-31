# 📝 Get Render Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_render_output.py#L591)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Render Output](.)  
**Sequential Order:** 7
**Story Type:** user

## Story Description

Get Render Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action needs render instructions

  **then** Action retrieves render instructions

  **and** Instructions are available for rendering

## Scenarios

### Scenario: Get Render Instructions (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
