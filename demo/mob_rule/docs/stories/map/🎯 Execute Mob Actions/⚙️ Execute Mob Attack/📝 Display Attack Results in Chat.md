# 📝 Display Attack Results in Chat

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Execute Mob Attack)

**Epic:** Execute Mob Actions
**Feature:** Execute Mob Attack

## Story Description

Chat system receives attack result events from Combat system and displays formatted results for all mob members

## Scenarios

### Background
Given mob has executed attacks through Mutants and Masterminds combat system
And combat system has generated attack result events
And Chat System has received attack result events

### Scenario: Mob Manager intercepts and summarizes attack results
Given Mutants and Masterminds combat system has executed attacks for <member_count> mob members
And combat system sends attack result events to Chat System
When Chat System receives attack result events
Then Mob Manager intercepts the attack result events
And Mob Manager reformats the attack chat dialogue to summarize all mob attacks results in one view
And Mob Manager provides a single resistance button for all mob attacks instead of individual resistance buttons for each attack

**Examples:**
| member_count |
|--------------|
| 3            |
| 5            |
| 10           |

### Scenario: Resistance button executes rolls for all hits
Given Mob Manager has created summary chat dialogue with single resistance button
And <hit_count> attacks actually hit the target
When user or GM clicks on the resistance button
Then Mob Manager intercepts the resistance button click
And Mob Manager runs the resistance roll for every attack that actually hit (<hit_count> rolls)

**Examples:**
| hit_count |
|-----------|
| 1         |
| 3         |
| 5         |
| 0         |

### Scenario: All attacks miss
Given mob has executed attacks
And all attacks miss the target
When Chat System receives attack result events
Then Mob Manager intercepts and creates summary dialogue
And summary dialogue shows all attacks missed
And resistance button is not provided (no hits to resist)

### Scenario: Mixed attack results
Given mob has executed attacks
And some attacks hit and some miss
When Chat System receives attack result events
Then Mob Manager intercepts and creates summary dialogue
And summary dialogue shows which attacks hit and which missed
And single resistance button is provided
And resistance button executes rolls only for attacks that hit

### Scenario: Chat System behavior unchanged
Given Chat System receives attack result events
When Mob Manager intercepts the events
Then Chat System continues to function normally
And Chat System is not modified by Mob Manager
And Mob Manager only wraps/intercepts the display formatting

## Notes

- Mob Manager wraps Chat System - does not modify Chat System behavior
- Single resistance button consolidates multiple individual resistance buttons
- Resistance rolls only execute for attacks that actually hit

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration

