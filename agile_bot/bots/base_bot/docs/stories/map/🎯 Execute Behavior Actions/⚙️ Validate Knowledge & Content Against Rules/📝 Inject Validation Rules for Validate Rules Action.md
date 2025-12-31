# 📝 Inject Validation Rules for Validate Rules Action

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py#L4697)

**User:** Bot Behavior
**Path:** [🎯 Execute Behavior Actions](../..) / [⚙️ Validate Knowledge & Content Against Rules](.)  
**Sequential Order:** 1
**Story Type:** user

## Story Description

Inject Validation Rules for Validate Rules Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** MCP Specific Behavior Action Tool invokes Validate Rules Action

  **then** Action loads common bot rules from base_bot/rules/

  **and** Action loads behavior-specific rules

  **and** Action merges and injects rules into validation section

## Scenarios

### Scenario: Inject Validation Rules for Validate Rules Action (happy_path)

**Steps:**
```gherkin
Given system is ready
When action executes
Then action completes successfully
```
