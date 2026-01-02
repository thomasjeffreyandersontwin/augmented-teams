# 📝 Advance Action And Persist State

**Navigation:** [📋 Story Map](../../../../story-map.drawio) | [Test](/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py)

**User:** System
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Run Interactive REPL](..) / [⚙️ Navigate Bot Behaviors and Actions Via Domain Model](.)  
**Sequential Order:** 2
**Story Type:** system

## Story Description

Advance Action And Persist State functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** action executes, **then** action completes successfully

## Scenarios

### Scenario: Close current advances and persists state (happy_path) | [Test](/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py#L54)

**Steps:**
```gherkin
GIVEN: bot.behaviors.current is at clarify action
WHEN: actions.close_current() is called
THEN: actions.current_action_name == 'strategy'
AND: 'story_bot.shape.clarify' in completed_actions
AND: state.current_action == 'story_bot.shape.strategy'
```

