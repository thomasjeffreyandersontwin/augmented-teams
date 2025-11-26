# 📝 Select and Unselect Mob Tokens

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Create Mobs from Canvas Tokens)

**Epic:** Group Minions into Mobs
**Feature:** Create Mobs from Canvas Tokens

## Story Description

GM selects and unselects tokens on canvas and Mob domain object updates mob membership with selected tokens

## Scenarios

### Background
Given GM has opened Mob dialog box
And a mob is active for editing (either newly created or selected from list)
And canvas has tokens available

### Scenario: GM selects tokens to add to mob
Given an active mob exists with <current_count> member tokens
When GM selects <selected_count> tokens on canvas
Then Canvas System forwards token selection event to Mob Manager
And Mob Manager aligns mob membership with all selected tokens
And Mob queries Token System to identify all selected tokens
And Mob domain object adds selected tokens to mob membership
And mob now has <new_count> member tokens
And Mob domain object stores updated Mob instance with member tokens with Mob Manager

**Examples:**
| current_count | selected_count | new_count |
|--------------|---------------|-----------|
| 0            | 3             | 3         |
| 2            | 2             | 4         |
| 5            | 3             | 8         |

### Scenario: GM unselects tokens to remove from mob
Given an active mob exists with <current_count> member tokens
And mob has specific tokens as members
When GM unselects <unselected_count> tokens that are currently mob members
Then Canvas System forwards token selection event to Mob Manager
And Mob Manager aligns mob membership with all selected tokens
And Mob queries Token System to identify all selected tokens
And Mob domain object removes unselected tokens from mob membership
And mob now has <new_count> member tokens
And if the leader token was unselected and leader was in combat tracker, Mob Manager removes leader from combat tracker
And Mob domain object stores updated Mob instance with member tokens with Mob Manager

**Examples:**
| current_count | unselected_count | new_count |
|---------------|------------------|-----------|
| 5             | 2                | 3         |
| 3             | 1                | 2         |
| 10            | 5                | 5         |

### Scenario: GM selects and unselects tokens simultaneously
Given an active mob exists with <current_count> member tokens
When GM selects <selected_count> new tokens and unselects <unselected_count> existing member tokens
Then Canvas System forwards token selection event to Mob Manager
And Mob Manager aligns mob membership with all selected tokens
And Mob queries Token System to identify all selected tokens
And Mob domain object adds new tokens and removes unselected tokens from mob membership
And mob now has <new_count> member tokens
And if the leader token was unselected and leader was in combat tracker, Mob Manager removes leader from combat tracker
And Mob domain object stores updated Mob instance with member tokens with Mob Manager

**Examples:**
| current_count | selected_count | unselected_count | new_count |
|---------------|----------------|-------------------|-----------|
| 3             | 2              | 1                 | 4         |
| 5             | 3              | 2                 | 6         |

### Scenario: Leader assigned when member added to combat tracker
Given a mob exists with multiple member tokens
And mob has no leader assigned
When GM adds a member token to the combat tracker (by dragging to combat tracker or right-clicking and choosing "add to tracker")
Then that member token becomes the Mob leader
And Mob Manager stores the leader token with the Mob instance

### Scenario: No tokens selected
Given an active mob exists
When GM does not select any tokens
Then dialog box remains open with current member list
And Mob Manager does not update mob membership
And mob remains in current state

### Scenario: All tokens unselected
Given an active mob exists with member tokens
When GM unselects all tokens
Then Mob Manager removes all tokens from mob membership
And mob has zero member tokens

## Notes

- Mob membership is updated based on currently selected tokens on canvas
- Leader is assigned when a member token is added to the combat tracker (by dragging or right-clicking "add to tracker")
- Mob becomes active when leader is added to combat tracker and it becomes their turn
- Any token type can be a mob member
- Mob Manager wraps Canvas System and Token System - does not modify them

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration

