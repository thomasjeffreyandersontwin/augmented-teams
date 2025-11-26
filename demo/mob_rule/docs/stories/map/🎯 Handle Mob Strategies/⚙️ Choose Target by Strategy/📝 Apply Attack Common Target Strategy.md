# 📝 Apply Attack Common Target Strategy

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Choose Target by Strategy)

**Epic:** Handle Mob Strategies
**Feature:** Choose Target by Strategy

## Story Description

GM selects Attack Common Target strategy for mob, and Mob domain object applies strategy when mob's turn begins by querying Combat Tracker for common target

## Scenarios

### Background
Given a mob exists
And mob leader is in combat tracker
And Attack Common Target strategy is configured for the mob

### Scenario: Strategy automatically selected on mob creation
Given GM initiates creating a new mob
When mob is created
Then Attack Common Target strategy is automatically selected
And Mob Manager associates the mob with Attack Common Target strategy

### Scenario: Strategy waits for GM attack when parameters not set
Given Attack Common Target strategy is configured for mob
And it is mob leader's turn
When Mob Manager retrieves strategy configuration
And Mob Manager determines attack and target have not been selected
Then Mob Manager waits for an attack to be executed by the mob leader
And strategy does not execute

### Scenario: GM attack associates target and attack with mob
Given Attack Common Target strategy is configured for mob
And it is mob leader's turn
And attack and target have not been selected
When GM executes an attack from the mob leader onto target <target_name> with attack <attack_type>
Then that target (<target_name>) is associated with the mob
And that attack (<attack_type>) is associated with the mob
And Mob Manager stores the target and attack association

**Examples:**
| target_name | attack_type |
|-------------|-------------|
| Hero A      | Blast       |
| Villain B   | Strike      |
| Minion C    | Grab        |

### Scenario: Strategy executes automatically after GM attack sets parameters
Given Attack Common Target strategy is configured for mob
And it is mob leader's turn
And attack and target have not been selected
When GM executes an attack from the mob leader onto target <target_name> with attack <attack_type>
Then that target (<target_name>) is associated with the mob
And that attack (<attack_type>) is associated with the mob
And Mob Manager stores the target and attack association
And Mob Manager automatically executes the strategy for all mob members except the leader
And the same attack (<attack_type>) is forwarded to all mob members except the leader against the same target (<target_name>)
But the leader's attack has already been executed, so it is not repeated

**Examples:**
| target_name | attack_type |
|-------------|-------------|
| Hero A      | Blast       |
| Villain B   | Strike      |
| Minion C    | Grab        |

### Scenario: Strategy executes when attack and target associated
Given Attack Common Target strategy is configured for mob
And attack <attack_type> and target <target_name> have been associated with mob
And it is mob's turn in Combat tracker
When Mob Manager retrieves strategy configuration
And Mob Manager determines attack and target have been selected
Then mob strategy executes (see Story 3: Execute Mob Attack with Strategy for execution details)

**Examples:**
| attack_type | target_name |
|-------------|-------------|
| Blast       | Hero A      |
| Strike      | Villain B   |
| Grab        | Minion C    |

### Scenario: Strategy not executed when not mob's turn
Given Attack Common Target strategy is configured for mob
And attack and target have been associated
When it is not the mob's turn in Combat tracker
Then Mob Manager does not execute the strategy
And strategy waits for mob's turn

### Scenario: Turn advancement triggers strategy check
Given Attack Common Target strategy is configured for mob
When Combat Tracker advances to next turn
Then Combat Tracker notifies Mob Manager about turn advancement
And Mob Manager checks if current turn's token is a mob leader
And if it is mob leader's turn, Mob Manager retrieves strategy configuration

### Scenario: Strategy waits after attack and target cleared
Given Attack Common Target strategy is configured for mob
And attack and target were previously associated with mob
And GM has cleared the attack and target using clear button
When it is mob leader's turn
And Mob Manager retrieves strategy configuration
And Mob Manager determines attack and target have been cleared (not selected)
Then Mob Manager waits for an attack to be executed by the mob leader
And strategy does not execute
And GM must execute a new attack to set new parameters

## Notes

- Attack Common Target strategy waits for GM to execute an attack first, then associates that attack and target
- When GM executes an attack from the mob leader during the leader's turn, the strategy automatically executes for all mob members except the leader (since the leader already executed the attack)
- Strategy executes automatically when it's the mob's turn and parameters are complete
- GM can clear attack and target selection using clear button in Mob Manager dialog, which forces new selection on next round
- After clearing, strategy waits for new attack to be executed before executing again
- Mob Manager wraps Combat Tracker notifications - does not modify Combat Tracker

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration

