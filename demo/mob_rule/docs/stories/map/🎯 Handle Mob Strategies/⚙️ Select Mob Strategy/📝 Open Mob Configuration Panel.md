# 📝 Open Mob Configuration Panel

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Select Mob Strategy)

**Epic:** Handle Mob Strategies
**Feature:** Select Mob Strategy

## Story Description

GM clicks on mob leader token or mob entry in Combat Tracker, and Mob Panel UI opens displaying mob configuration options

## Scenarios

### Background
Given a mob exists with a leader token
And mob leader is in combat tracker
And Mob Panel UI is available

### Scenario: GM clicks mob leader token to open panel
Given GM has a mob with leader token on canvas
When GM clicks on the mob leader token
Then Mob Panel UI receives token click event
And Mob Panel UI opens displaying mob configuration options
And Mob Panel UI queries Mob domain object for mob configuration

### Scenario: GM clicks mob entry in Combat Tracker to open panel
Given GM has a mob with leader in combat tracker
When GM clicks on the mob entry in Combat Tracker
Then Combat Tracker forwards click event to Mob Panel UI
And Mob Panel UI opens displaying mob configuration options
And Mob Panel UI queries Mob domain object for mob configuration

### Scenario: Panel opens with mob configuration
Given Mob Panel UI has opened
And Mob Panel UI has queried Mob domain object
When Mob domain object returns mob configuration
Then Mob Panel UI displays mob members
And Mob Panel UI displays current strategy
And Mob Panel UI displays available strategy options

### Scenario: Multiple mobs exist - panel opens for clicked mob
Given multiple mobs exist
And each mob has a leader token
When GM clicks on a specific mob leader token
Then Mob Panel UI opens for that specific mob
And Mob Panel UI displays configuration for the clicked mob only

### Scenario: Panel already open - switches to clicked mob
Given Mob Panel UI is already open displaying one mob's configuration
When GM clicks on a different mob leader token
Then Mob Panel UI updates to display the newly clicked mob's configuration
And previous mob's configuration is replaced

## Notes

- Mob Panel UI wraps/intercepts token click events and Combat Tracker click events
- Panel queries Mob domain object for configuration data
- Panel can be opened from either canvas token click or Combat Tracker entry click

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Mob Panel and Basic Target Strategies - Increment Exploration

