# 📝 Display Selected Common Target

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Choose Target by Strategy)

**Epic:** Handle Mob Strategies
**Feature:** Choose Target by Strategy

## Story Description

Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected common target

## Scenarios

### Background
Given Attack Common Target strategy is configured for mob
And Mob Manager dialog is open or available

### Scenario: Mob Manager dialog displays target and attack
Given Mob Manager has determined target <target_name> and attack <attack_type> for strategy
When Mob Manager stores the target and attack
And Mob Manager notifies Mob Manager dialog of the changes
Then Mob Manager dialog receives target / attack change notification
And Mob Manager dialog is updated to indicate target is <target_name>
And Mob Manager dialog is updated to indicate attack is <attack_type>

**Examples:**
| target_name | attack_type |
|-------------|-------------|
| Hero A      | Blast       |
| Villain B   | Strike      |
| Minion C    | Grab        |

### Scenario: Dialog updates when target changes
Given Mob Manager dialog is displaying target <old_target> and attack <attack_type>
When GM executes a new attack from mob leader onto target <new_target>
And Mob Manager associates new target <new_target> with mob
And Mob Manager notifies dialog of changes
Then Mob Manager dialog updates to show target <new_target>
And attack remains <attack_type> (if same attack) or updates to new attack

**Examples:**
| old_target | new_target | attack_type |
|------------|------------|-------------|
| Hero A     | Villain B  | Blast       |
| Villain B  | Minion C   | Strike      |

### Scenario: Dialog updates when attack changes
Given Mob Manager dialog is displaying target <target_name> and attack <old_attack>
When GM executes a new attack <new_attack> from mob leader onto same target <target_name>
And Mob Manager associates new attack <new_attack> with mob
And Mob Manager notifies dialog of changes
Then Mob Manager dialog updates to show attack <new_attack>
And target remains <target_name>

**Examples:**
| target_name | old_attack | new_attack |
|-------------|-----------|------------|
| Hero A      | Blast     | Strike     |
| Villain B   | Strike    | Grab       |

### Scenario: Dialog not open when target/attack determined
Given Mob Manager has determined target and attack for strategy
When Mob Manager dialog is not open
Then Mob Manager stores the target and attack
And Mob Manager stores notification for when dialog is opened
And when dialog is opened, it displays the stored target and attack

### Scenario: Multiple target/attack changes
Given Mob Manager dialog is displaying current target and attack
When GM executes multiple attacks from mob leader
And Mob Manager associates new target and attack each time
Then Mob Manager dialog updates each time with the latest target and attack
And dialog always shows the most recent association

### Scenario: GM clears attack and target selection
Given Mob Manager dialog is displaying target <target_name> and attack <attack_type>
When GM clicks clear button in Mob Manager dialog
Then Mob Manager clears the target and attack association for the mob
And Mob Manager dialog updates to show no target and no attack selected
And on the next round when it is the mob leader's turn, the strategy will wait for a new attack to be executed
And the strategy will not execute until a new attack and target are selected

**Examples:**
| target_name | attack_type |
|-------------|-------------|
| Hero A      | Blast       |
| Villain B   | Strike      |
| Minion C    | Grab        |

## Notes

- Mob Manager dialog displays current strategy state (target and attack)
- Dialog updates automatically when target or attack changes
- Dialog may not be open when changes occur - updates when opened
- Clear button allows GM to reset attack and target selection, forcing new selection on next round

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration

