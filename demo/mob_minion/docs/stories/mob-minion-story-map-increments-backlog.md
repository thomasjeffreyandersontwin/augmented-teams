# Incremental Backlog: Mob Minion

**Navigation:** [📋 Story Map](story-map.txt) | [📊 Increments DrawIO](story-map-increments.drawio)

**File Name**: `mob-minion-story-map-increments-backlog.md`
**Location**: `demo/mob_minion/docs/stories/mob-minion-story-map-increments-backlog.md`

> **Purpose**: Flat list view of stories per increment for backlog management and sprint planning.

---

## Increment 1: Foundational Integration + Basic Mob

**Priority:** NOW (Priority 1)  
**Goal:** Validate Foundry API and deliver core mob coordination  
**Estimated Stories:** 11

### Map Foundry API (8 stories)
- 📝 Mob System --> Retrieve Token Selection State
- 📝 Mob System --> Update Token State
- 📝 Mob System --> Load Actor Statistics
- 📝 Mob System --> Evaluate Actor Combat Capabilities
- 📝 Mob System --> Register Combatant In Tracker
- 📝 Mob System --> Determine Attack Feasibility
- 📝 Mob System --> Identify Valid Combat Targets
- 📝 Mob System --> Set Target

### Manage Mobs (2 stories)
- 📝 Game Master --> Select Minions
- 📝 Game Master --> Group Minions Into Mob

### Execute Mob Actions (1 story)
- 📝 Game Master --> Execute Melee Attack

---

## Increment 2: Strategy System

**Priority:** NEXT (Priority 2)  
**Goal:** Add intelligent targeting and tactical behavior  
**Estimated Stories:** 8

### Assign Strategies (4 stories)
- 📝 Game Master --> Choose Attack Strongest
- 📝 Game Master --> Choose Attack Weakest
- 📝 Game Master --> Choose Defend Leader
- 📝 Game Master --> Choose Attack Most Damaged

### Execute Mob Actions (4 stories)
- 📝 Mob System --> Identify Valid Targets
- 📝 Mob System --> Apply Strategy Criteria
- 📝 Game Master --> Execute Ranged Attack
- 📝 Game Master --> Execute Area Attack

---

## Increment 3: Advanced Mob Management

**Priority:** LATER (Priority 3)  
**Goal:** Add convenience and polish features  
**Estimated Stories:** 5

### Manage Mobs (5 stories)
- 📝 Game Master --> Add Minions To Mob
- 📝 Game Master --> Remove Minions From Mob
- 📝 Game Master --> Disband Mob
- 📝 Game Master --> Spawn Mob From Template
- 📝 Game Master --> Spawn Mob From Actors

---

## Summary

**Total Stories:** 24 stories across 3 increments

**Increment Distribution:**
- Increment 1: 11 stories (46%)
- Increment 2: 8 stories (33%)
- Increment 3: 5 stories (21%)

**Approach:** Risk-first vertical slicing - each increment delivers end-to-end working flow validating key risks while providing user value.

---

## Source Material

**Shape phase:**
- Primary source: demo/mob_minion/input.txt
- Date generated: 2024-12-26
- Context: Mob minion coordination system for Foundry Virtual Tabletop. Focus on reducing GM token-clicking tedium through coordinated mob actions and strategic targeting behaviors.

