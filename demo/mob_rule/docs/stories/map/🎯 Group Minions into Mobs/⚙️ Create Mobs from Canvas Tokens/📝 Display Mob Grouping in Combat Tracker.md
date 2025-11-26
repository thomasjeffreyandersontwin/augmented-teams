# 📝 Display Mob Grouping in Combat Tracker

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Create Mobs from Canvas Tokens)

**Epic:** Group Minions into Mobs
**Feature:** Create Mobs from Canvas Tokens

## Story Description

Combat Tracker receives mob creation notification from Mob domain object and updates display to show mob membership

## Scenarios

### Background
Given a mob exists with multiple member tokens
And mob has a leader token assigned
And combat tracker is available

### Scenario: Mob leader added to combat tracker displays indicator
Given a mob exists with <member_count> member tokens
And mob has no leader assigned
When a mob member is added to combat tracker (by dragging to combat tracker or right-clicking and choosing "add to tracker")
Then that member becomes the Mob leader
And combat tracker displays token indicating mob leader status
And combat tracker displays the number of members in the mob (<member_count>)

**Examples:**
| member_count |
|--------------|
| 1            |
| 3            |
| 5            |
| 10           |

### Scenario: Other mob members prevented from being added to combat tracker
Given mob leader is already added to combat tracker
And mob has other member tokens
When GM attempts to add another mob member to combat tracker (by dragging to combat tracker or right-clicking and choosing "add to tracker")
Then Mob Manager intercepts the add to combat tracker action
And a dialog box appears indicating that mob leader already added
And the mob member is not added to the combat tracker
And only the mob leader appears in combat tracker

### Scenario: Mob membership update reflects in combat tracker indicator
Given mob leader is displayed in combat tracker with member count indicator
When mob membership is updated (tokens added or removed)
Then mob leader indicator changes to reflect the updated number of members in the mob
And combat tracker display updates automatically

### Scenario: Mob leader removal removes leader from combat tracker
Given mob leader is in combat tracker
And mob has other member tokens
When mob leader is removed from the mob
Then the mob leader is removed from the combat tracker
And no new leader is assigned
And mob has no leader until another member is added to combat tracker

### Scenario: All mob members removed
Given mob leader is in combat tracker
When all mob members are removed from the mob
Then mob leader is removed from combat tracker
And mob no Longer Part of the Combat tracker

## Notes

- Combat Tracker displays mob information but does not change its behavior 
- Leader indicator updates automatically when membership changes
- Only one mob member (the leader) can be in combat tracker at a time
- Mob Manager intercepts attempts to add other members when leader already exists

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration

