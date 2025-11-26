# 📝 Execute Mob Attack with Strategy

**Navigation:** [📋 Story Map](../../mob-rule-story-map.md) | [⚙️ Feature Overview](../⚙️ Execute Mob Attack)

**Epic:** Execute Mob Actions
**Feature:** Execute Mob Attack

## Story Description

Combat Tracker moves to mob leader's turn, Mob domain object determines target from Select Target strategy, GM attacks with mob leader choosing attack and target, and Mob domain object forwards action to all members

## Scenarios

### Background
Given a mob exists with multiple member tokens
And mob leader is in combat tracker
And Attack Common Target strategy is configured for the mob
And attack and target have been associated with the mob
And it is the mob's turn in combat tracker

### Scenario: Mob attack executes when strategy parameters are complete
Given Combat Tracker advances to next turn
When Combat Tracker notifies Mob Manager about turn advancement
And Mob Manager checks if current turn's token is a mob leader
And Mob Manager identifies it is a mob leader's turn
And Mob Manager retrieves strategy configuration
And strategy has all appropriate parameters determined (attack and target associated)
Then Mob Manager asks Mob domain object to evaluate and execute the strategy
And Mob domain object executes the attack as determined by the strategy on the target as determined by the strategy
And Mob domain object forwards that attack to the Mutants and Masterminds combat system for every member in the mob

### Scenario: Strategy does not execute when parameters incomplete
Given Combat Tracker advances to next turn
And it is mob leader's turn
When Mob Manager retrieves strategy configuration
And strategy does not have all parameters determined (attack or target not associated)
Then Mob Manager does not execute the strategy
And no attacks are forwarded to Mutants and Masterminds combat system
And Mob Manager waits for GM to execute attack to associate attack and target

### Scenario Outline: Different attack types executed for all mob members
Given mob has <member_count> member tokens
And attack <attack_type> and target <target_name> are associated with mob
And it is mob leader's turn
When strategy executes
Then Mob domain object forwards <attack_type> attack to Mutants and Masterminds combat system for all <member_count> members
And all members attack <target_name> with <attack_type>

**Examples:**
| member_count | attack_type | target_name |
|--------------|-------------|-------------|
| 3            | Blast       | Hero A      |
| 5            | Strike      | Villain B   |
| 10           | Grab        | Minion C    |

### Scenario: Not mob leader's turn
Given Combat Tracker advances to next turn
When Combat Tracker notifies Mob Manager about turn advancement
And Mob Manager checks if current turn's token is a mob leader
And current turn's token is not a mob leader
Then Mob Manager does not evaluate or execute strategy
And no attacks are executed

### Scenario: No strategy configured
Given mob exists
And it is mob leader's turn
When Mob Manager retrieves strategy configuration
And no strategy is configured for the mob
Then Mob Manager does not execute any strategy
And no attacks are forwarded

## Notes

- Strategy execution requires both attack and target to be associated (see Story 5)
- Mob Manager wraps Combat Tracker turn notifications - does not modify Combat Tracker
- All mob members execute the same attack on the same target

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Acceptance criteria from Exploration phase: Technical Proof of Concept and Drill-Down Stories - Increment Exploration

