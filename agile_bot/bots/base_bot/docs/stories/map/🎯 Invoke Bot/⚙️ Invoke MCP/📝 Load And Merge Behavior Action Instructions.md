# 📝 Load And Merge Behavior Action Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_invoke_mcp.py#L560)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Invoke MCP](.)  
**Sequential Order:** 2
**Story Type:** user

## Story Description

Load And Merge Behavior Action Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Action method is invoked

  **then** Action loads instructions from base_actions and behavior-specific locations

  **and** Instructions are merged and returned

## Scenarios

### Scenario: Action Loads And Merges Instructions (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_invoke_mcp.py#L563)

**Steps:**
```gherkin
Given Base and behavior-specific instructions exist
When Action method is invoked
Then Instructions are loaded from both locations and merged
```


### Scenario: Action uses Instructions class to merge base and behavior instructions (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_invoke_mcp.py#L587)

**Steps:**
```gherkin
Given Action with BaseActionConfig and Behavior
When Action initialized
Then Action uses Instructions class to merge instructions
```


### Scenario: Action uses MergedInstructions class when render instructions present (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_invoke_mcp.py#L608)

**Steps:**
```gherkin
Given RenderOutputAction with render instructions
When Action initialized
Then Action uses MergedInstructions class for merging
```

