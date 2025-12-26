# Story Map Clarification - Mob Minion System

## User Types

**Question:** Who are the distinct types of users?

**Answer:** Game Masters (GMs) who run role-playing games in Foundry Virtual Tabletop system. They manage combat encounters with multiple minion NPCs.

## Key Goals and Behaviors

**Question:** What are the key goals, behaviors, or decisions each group is trying to accomplish using this capability?

**Answer:** GMs want to efficiently control groups of minion tokens during combat without clicking each individual token. They want to assign group behaviors/strategies (attack strongest, attack weakest, defend leader, attack most damaged) and have all minions in a mob execute the same action together.

## Primary Users

**Question:** Who are the primary users or stakeholder groups impacted?

**Answer:** Game Masters using Foundry Virtual Tabletop system for running RPG sessions with minion encounters.

## First Use Case

**Question:** What is the first thing users will try to do with this new capability or system?

**Answer:** Group existing minion tokens into a mob so they can control them as a single unit instead of individually.

## Problems Being Solved

**Question:** What problems, inefficiencies, or workarounds is this request trying to eliminate?

**Answer:** Eliminates the need to click on every individual minion token to make them perform actions during combat, which is time-consuming and disrupts game flow.

## Current Pain Points

**Question:** Where are users currently struggling, getting stuck, or experiencing delays in the process we're aiming to improve?

**Answer:** During combat encounters with multiple minions, GMs experience significant delays clicking each token individually to coordinate their actions.

## Value Drivers

**Question:** What are the key drivers for customer value or business value that this capability addresses, and what specific customer or business outcomes are we trying to achieve?

**Answer:** Streamline combat management, improve game flow, reduce GM cognitive load during encounters, make minion encounters feel more cohesive and tactical rather than tedious micromanagement.

## User Journey

**Question:** What is the user journey from start to finish for the primary use case, and what are the key stages or steps in the user journey?

**Answer:** 
1. Create or spawn minions in Foundry VTT
2. Group minions into a mob
3. Assign a strategy to the mob (attack strongest, weakest, etc.)
4. During combat, click any minion in the mob
5. All minions execute the chosen strategy automatically
6. Minions choose targets and attack based on strategy rules (range, melee, area)

## Journey Friction Points

**Question:** Where in the user journey are users experiencing frustration, friction, or unhappiness?

**Answer:** At the individual token clicking stage - having to select each minion separately to coordinate group actions causes frustration and breaks immersion.

## Moments of Delight

**Question:** What moments of delight or value should users experience during their journey?

**Answer:** The moment when clicking one minion triggers coordinated action from the entire mob, creating a satisfying "swarm" effect and dramatically reducing combat management time.

## Critical Pain Points

**Question:** What are the critical pain points that prevent users from achieving their goals?

**Answer:** Lack of group control mechanism forces tedious individual token manipulation; no way to define and execute coordinated tactical behaviors for minion groups.

## System Integrations

**Question:** What other systems, data sources, or tools does this capability need to interact with in order to deliver value?

**Answer:** Foundry Virtual Tabletop system - specifically the token/actor system, combat system, targeting system, movement/range calculations, and attack mechanics.

## Integration Points

**Question:** What are the key behaviors or integration points that define how these systems support or depend on one another?

**Answer:** Must integrate with Foundry's token selection, targeting UI, actor data model, combat tracker, movement system (melee vs range), and action execution framework. Strategy behaviors depend on querying actor stats (HP, power level) to choose appropriate targets.

