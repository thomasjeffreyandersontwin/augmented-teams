# 📝 Navigate To First Behavior Action

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py)

**User:** System
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Navigate Bot Behaviors and Actions Via Domain Model](.)  
**Sequential Order:** 1
**Story Type:** system

## Story Description

Navigate To First Behavior Action functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: Navigate sets current behavior and first action (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py#L40)

**Steps:**
```gherkin
GIVEN: Bot has behaviors configured
WHEN: bot.behaviors.navigate_to('shape') is called
THEN: bot.behaviors.current.name == 'shape'
AND: bot.behaviors.current.actions.current_action_name == 'clarify'
```

