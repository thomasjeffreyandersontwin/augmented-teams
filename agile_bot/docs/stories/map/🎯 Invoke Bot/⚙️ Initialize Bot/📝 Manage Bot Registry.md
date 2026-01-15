# 📝 Manage Bot Registry

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Initialize Bot](.)  
**Sequential Order:** 5
**Story Type:** system

## Story Description

Provide domain model properties for managing registered bots and the active bot. The Bot class exposes a `bots` property that returns a list of all registered bots, and an `active_bot` property that can be set to switch the currently active bot. This enables the CLI and Panel layers to interact with bot management through a clean domain interface.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** `bot.bots` property is accessed
  **then** System returns list of all registered bot names
  **and** List includes all bots found in configured bot directories

- **When** `bot.active_bot` property is accessed
  **then** System returns currently active bot instance

- **When** `bot.active_bot` is set to a registered bot name
  **and** bot name is valid and registered
  **then** System switches to the specified bot
  **and** System loads bot configuration from bot_config.json
  **and** System loads bot behaviors and actions
  **and** System updates active_bot to new bot instance

- **When** `bot.active_bot` is set to an invalid bot name
  **and** bot name is not registered
  **then** System raises BotNotFoundError
  **and** System keeps current active_bot unchanged

- **When** `bot.active_bot` is set to current active bot
  **then** System returns current bot without reloading
  **and** No state change occurs

## Scenarios

<a id="scenario-get-list-of-registered-bots"></a>
### Scenario: [Get List of Registered Bots](#scenario-get-list-of-registered-bots) (happy_path)

**Steps:**
```gherkin
Given bot registry has multiple registered bots (story_bot, task_bot, crc_bot)
When bot.bots property is accessed
Then System returns ["story_bot", "task_bot", "crc_bot"]
```

<a id="scenario-get-active-bot"></a>
### Scenario: [Get Active Bot](#scenario-get-active-bot) (happy_path)

**Steps:**
```gherkin
Given story_bot is currently active
When bot.active_bot property is accessed
Then System returns story_bot instance
And Instance contains loaded behaviors and actions
```

<a id="scenario-set-active-bot-to-registered-bot"></a>
### Scenario: [Set Active Bot to Registered Bot](#scenario-set-active-bot-to-registered-bot) (happy_path)

**Steps:**
```gherkin
Given story_bot is currently active
And task_bot is registered
When bot.active_bot is set to "task_bot"
Then System switches to task_bot
And System loads task_bot configuration from bot_config.json
And System loads task_bot behaviors and actions
And bot.active_bot returns task_bot instance
```

<a id="scenario-attempt-to-set-unregistered-bot"></a>
### Scenario: [Attempt to Set Unregistered Bot](#scenario-attempt-to-set-unregistered-bot) (error_path)

**Steps:**
```gherkin
Given story_bot is currently active
And "invalid_bot" is not registered
When bot.active_bot is set to "invalid_bot"
Then System raises BotNotFoundError with message "Bot 'invalid_bot' not found"
And bot.active_bot still returns story_bot instance
And No bot state changes occur
```

<a id="scenario-set-active-bot-to-current-bot"></a>
### Scenario: [Set Active Bot to Current Bot](#scenario-set-active-bot-to-current-bot) (happy_path)

**Steps:**
```gherkin
Given story_bot is currently active
When bot.active_bot is set to "story_bot"
Then System returns current story_bot instance
And No reload or reconfiguration occurs
And bot.active_bot still returns same story_bot instance
```
