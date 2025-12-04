# 📝 Inject Validation Rules for Validate Rules Action

**Navigation:** [📋 Story Map](../../story-map.txt) | [Story Graph](../../story-graph.json) | [Increment 2 AC](../../increment-2-acceptance-criteria-DRAFT.md)

**Epic:** Invoke MCP Bot Server  
**Feature:** Perform Behavior Action

**User:** Bot Behavior  
**Sequential Order:** 14  
**Story Type:** system

## Story Description

Bot Behavior injects action instructions and validation rules so that AI Chat knows how to validate generated content and has the rules to validate against.

## Acceptance Criteria

- **WHEN** MCP Specific Behavior Action Tool invokes Validate Rules Action (7_validate_rules)
- **THEN** Action loads action-specific instructions from `base_actions/7_validate_rules/instructions.json`
- **AND** Action loads common bot rules from `base_bot/rules/`
- **AND** Action loads behavior-specific rules from `{bot}/behaviors/{behavior}/rules/` or `{bot}/behaviors/{behavior}/3_rules/`
- **AND** Action merges action instructions, common rules, and behavior-specific rules
- **AND** Action injects instructions and rules into compiled instructions
- **AND** Instructions guide AI on validation process (load clarification.json, planning.json, evaluate against rules)
- **AND** Rules define validation criteria for generated content

## Background

**Common setup steps shared across all scenarios:**

```gherkin
Given a bot with name 'test_bot'
And bot instance is preloaded in MCP Server
And generated content exists to validate
```

## Scenarios

### Scenario: Action loads and injects action instructions plus validation rules

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'exploration'
And behavior has action 'validate_rules'
And action instructions exist in base_actions/7_validate_rules/instructions.json
And action has behavior-specific rules configured
And common bot rules exist
When Tool invokes test_bot.Exploration.ValidateRules() method
Then Action loads action instructions from base_actions/7_validate_rules/instructions.json
And Action loads common rules from base_bot/rules/
And Action loads behavior-specific rules from behaviors/exploration/3_rules/ or behaviors/exploration/rules/
And Action merges action instructions, common rules, and behavior-specific rules
And Action injects all content into compiled instructions
And Instructions guide AI Chat on validation process (load clarification.json, planning.json, evaluate)
And Instructions include all validation rules for content checking
```

### Scenario: Action uses common rules when behavior-specific rules do not exist

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'exploration'
And behavior has action 'validate_rules'
And action does NOT have behavior-specific rules configured
And common bot rules exist
When Tool invokes test_bot.Exploration.ValidateRules() method
Then Action loads common rules from exact path: base_bot/rules/story_structure_rules.json
And Action checks for behavior-specific rules at exact path: agile_bot/bots/test_bot/behaviors/exploration/rules/
And Action injects common rules only into validation section
And Action logs info 'No behavior-specific rules found for exploration, using common rules only'
```

### Scenario: Action handles missing common rules

**Steps:**
```gherkin
Given a bot with name 'test_bot'
And bot has a behavior configured as 'exploration'
And behavior has action 'validate_rules'
And common bot rules do NOT exist
When Tool invokes test_bot.Exploration.ValidateRules() method
Then Action attempts to load from exact path: base_bot/rules/
And Action raises FileNotFoundError with message 'Common bot rules not found at base_bot/rules/'
And Action does not return compiled instructions
And Tool returns error to AI Chat
```

---

## Source Material

**Primary Source**: agile_bot/bots/base_bot/docs/stories/increment-2-acceptance-criteria-DRAFT.md  
**Phase**: Specification - Detailed scenario writing from acceptance criteria  
**Date Generated**: 2025-12-03  
**Context**: System-centric scenarios focusing on validation rule loading, merging, and injection.


