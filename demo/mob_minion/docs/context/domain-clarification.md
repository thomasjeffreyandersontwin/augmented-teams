# Domain Clarification - Mob Minion System

## User Context

**Question:** Who are the distinct types of users?
**Answer:** Game Masters (GMs) who run role-playing game sessions in Foundry Virtual Tabletop system. They manage combat encounters with multiple minion NPCs.

**Question:** What are the key goals, behaviors, or decisions each group is trying to accomplish?
**Answer:** GMs want to efficiently control groups of minion tokens during combat without clicking each individual token. They assign strategies (attack strongest, weakest, defend leader, attack damaged) and have all minions execute actions together based on the strategy.

**Question:** Who are the primary users or stakeholder groups impacted?
**Answer:** Game Masters using Foundry Virtual Tabletop for running RPG combat encounters.

**Question:** What is the first thing users will try to do?
**Answer:** Group existing minion tokens into a mob so they can control them as a single coordinated unit.

**Question:** What problems is this trying to eliminate?
**Answer:** Eliminates tedious individual token clicking during combat, which disrupts game flow and creates GM cognitive overload.

**Question:** Where are users currently struggling?
**Answer:** During combat encounters with multiple minions - having to manually click each token to coordinate actions causes significant delays.

**Question:** What are the key drivers for value?
**Answer:** Streamline combat management, improve game flow, reduce GM cognitive load, make minion encounters feel tactical rather than tedious.

**Question:** What is the user journey?
**Answer:**
1. Create/spawn minions in Foundry VTT
2. Group minions into a mob
3. Assign a strategy to the mob
4. During combat, click any minion in the mob
5. All minions execute the strategy automatically
6. Minions select targets and attack based on strategy rules

**Question:** Where is friction in the journey?
**Answer:** Individual token clicking stage - selecting each minion separately breaks immersion and slows gameplay.

**Question:** What moments of delight should users experience?
**Answer:** When clicking one minion triggers coordinated action from the entire mob, creating a satisfying "swarm" effect.

**Question:** What are the critical pain points?
**Answer:** Lack of group control mechanism; no way to define and execute coordinated tactical behaviors for minion groups.

**Question:** What systems does this integrate with?
**Answer:** Foundry Virtual Tabletop system - token/actor system, combat system, targeting system, movement/range calculations, attack mechanics.

**Question:** What are the key integration points?
**Answer:** Token selection, targeting UI, actor data model, combat tracker, movement system (melee vs range), action execution framework. Strategy behaviors query actor stats to choose targets.

## Domain Context

**Question:** What is the business domain we are modeling?
**Answer:** Combat encounter management for tabletop role-playing games, specifically coordinated minion control within Foundry Virtual Tabletop system.

**Question:** What are the core business concepts and their relationships?
**Answer:**
- **Mob**: A coordinated group of minions that act together
- **Minion**: An individual NPC combatant represented by a token
- **Token**: Visual representation of a minion on the game map
- **Actor**: Foundry's data model containing minion statistics and capabilities
- **Strategy**: A targeting/behavior rule that determines how mob selects targets (attack strongest, weakest, defend leader, attack damaged)
- **Target**: An enemy combatant selected for attack based on strategy criteria
- **Attack**: A coordinated action executed by mob minions (melee, ranged, or area)
- **Combat Tracker**: Foundry system managing turn order and combat state
- **Selection State**: Currently selected tokens that can be grouped into a mob

**Relationships:**
- Mob contains multiple Minions
- Each Minion has one Token and one Actor
- Mob has one assigned Strategy
- Strategy determines Target selection
- Mob executes Attack on Target(s)
- Attack type depends on Actor capabilities and range

**Question:** What are the distinct sub-domains or business capabilities?
**Answer:**
1. **Foundry API Integration**: Interacting with Foundry VTT's token, actor, combat, and targeting systems
2. **Mob Management**: Creating, editing, spawning, and disbanding mobs
3. **Strategy Management**: Selecting and applying combat strategies
4. **Combat Execution**: Target selection and coordinated attack execution

**Question:** What are the boundaries between different parts of the domain?
**Answer:**
- **Foundry VTT Boundary**: External system providing token, actor, combat, and targeting APIs
- **Mob System Boundary**: Our system managing mob groupings, strategies, and coordination
- **Strategy Engine Boundary**: Logic for evaluating target selection criteria
- **Combat Coordination Boundary**: Orchestrating multiple minion actions

**Question:** What domain events occur in this business domain?
**Answer:**
- **Mob Created**: Minions grouped into new mob
- **Mob Modified**: Minions added to or removed from mob
- **Mob Disbanded**: Mob dissolved, minions become independent
- **Mob Spawned**: New mob created from template or actors
- **Strategy Assigned**: Combat strategy selected for mob
- **Targets Identified**: Valid targets found based on strategy
- **Strategy Applied**: Target selection criteria evaluated
- **Attack Initiated**: Mob begins coordinated attack
- **Melee Attack Executed**: Close combat attack performed
- **Ranged Attack Executed**: Distance attack performed
- **Area Attack Executed**: Multi-target attack performed
- **Token Selected**: User selects minion token triggering mob action
- **Combatant Registered**: Minion added to combat tracker

**Question:** What are the key business rules and constraints?
**Answer:**
- Minions must be grouped into a mob before coordinated action
- Each mob has exactly one active strategy
- Strategies must select targets from valid combatants
- Attack type (melee/ranged/area) depends on actor capabilities
- Melee attacks require movement to target if out of range
- All minions in mob execute the same action type simultaneously
- Target selection criteria vary by strategy:
  - Attack Strongest: Target highest power/stats
  - Attack Weakest: Target lowest HP/power
  - Defend Leader: Protect designated leader
  - Attack Most Damaged: Target lowest HP
- Mob actions triggered by clicking any minion in the mob
- Minions removed from mob revert to independent control

**Question:** What domain language do business experts use to describe this domain?
**Answer:**
- **Mob**: Group of coordinated minions
- **Minion**: Low-power NPC combatant
- **Swarm**: Many minions attacking together
- **Strategy**: Targeting behavior/tactic
- **Token**: Visual game piece on map
- **Actor**: Character/NPC with stats
- **Combatant**: Entity in combat tracker
- **Turn**: Combat round segment
- **Target**: Enemy being attacked
- **Melee**: Close-range attack
- **Ranged**: Distance attack
- **Area/AOE**: Multi-target attack
- **HP**: Hit points/health
- **Power Level**: Combat effectiveness measure
- **Leader**: Protected/important character
- **Spawn**: Create new entities
- **Template**: Reusable mob configuration
- **Selection**: Currently chosen tokens
- **Coordination**: Simultaneous group action

## Domain Model Summary

**Core Aggregates:**
- **Mob Aggregate**: Mob (root), Minions, Strategy
- **Combat Aggregate**: Attack, Targets, Execution

**Value Objects:**
- Strategy Type (Attack Strongest, Attack Weakest, Defend Leader, Attack Most Damaged)
- Attack Type (Melee, Ranged, Area)
- Selection State
- Combat Statistics

**Services:**
- Target Selection Service (applies strategy criteria)
- Foundry Integration Service (API interactions)
- Combat Coordination Service (orchestrates mob actions)

**Domain Events:**
- Mob lifecycle events (Created, Modified, Disbanded, Spawned)
- Strategy events (Assigned, Applied)
- Combat events (Targets Identified, Attack Executed)

