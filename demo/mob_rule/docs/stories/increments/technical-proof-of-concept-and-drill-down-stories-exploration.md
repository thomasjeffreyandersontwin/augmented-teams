# Technical Proof of Concept and Drill-Down Stories - Increment Exploration

**Navigation:** [📋 Story Map](../map/mob-rule-story-map.md) | [📊 Increments](mob-rule-story-map-increments.md)

**File Name**: `technical-proof-of-concept-and-drill-down-stories-exploration.md`
**Location**: `mob_rule/docs/stories/increments/technical-proof-of-concept-and-drill-down-stories-exploration.md`

**Priority:** NOW
**Relative Size:** Small

## Increment Purpose

Validate Foundry VTT integration, Mob domain object, basic Combat Tracker/Actor/Actions integration. Complete all drill-down stories that showcase architectural complexity. Establishes strategy pattern foundation.

---

## Domain AC (Increment Level)

### Core Domain Concepts

#### Mob
A collection of tokens that act together as a single unit. Has a leader token and member tokens. The leader token represents the mob in Combat Tracker and is clicked to execute mob actions. Any token type can be a mob member.

#### Leader Token
The token that represents the mob in Combat Tracker. Assigned when a member token is added to the combat tracker (by dragging to combat tracker or right-clicking and choosing "add to tracker"). The member added becomes the leader immediately. Clicked by GM to execute mob actions. All mob members execute the same action as the leader.

#### Attack Common Target Strategy
A strategy that determines all mob members attack the same target with the same attack. The target and attack are associated with the mob when GM executes an attack from the mob leader onto another token. Once associated, the strategy executes automatically when it's the mob's turn in Combat Tracker.

#### Mob Manager Dialog
A dialog box that displays mob configuration and status information. Shows mob members, current strategy, target, and attack information. Updated when Mob Manager determines target and attack for a strategy.

---

### Domain Behaviors

#### Mob Behavior
Created when GM initiates minion selection mode (via hotkey) and selects multiple tokens on canvas. Mob Manager creates mob with selected tokens. When a mob member is added to combat tracker (by dragging or right-clicking "add to tracker"), that member becomes the mob leader. Mob must have at least one member token. Any token type can be a mob member.

#### Leader Token Behavior
Assigned when a mob member is added to combat tracker (by dragging to combat tracker or right-clicking and choosing "add to tracker"). The member added becomes the mob leader immediately. Represents mob in Combat Tracker. When GM executes an attack from the mob leader, Mob Manager associates that attack and target with the mob for strategy execution.

#### Attack Common Target Strategy Behavior
Strategy waits for GM to execute an attack from the mob leader onto another token. When GM executes the attack, Mob Manager associates that target and attack with the mob. When it's the mob's turn in Combat Tracker and a target and attack have been associated, the strategy executes automatically, forwarding the same attack to all mob members against the same target.

---

### Domain Rules

#### Mob must have at least one member token
**Business rule:** A mob cannot be created with zero tokens. Validation occurs when Mob domain object creates mob.

#### Leader is assigned when member is added to combat tracker
**Business rule:** When a mob member is added to combat tracker (by dragging to combat tracker or right-clicking and choosing "add to tracker"), that member becomes the mob leader immediately. If the mob leader is removed from the mob and the leader was in combat tracker, the leader is removed from combat tracker. No new leader is automatically assigned until another member is added to combat tracker.

#### Mob actions execute only during mob leader turn in Combat Tracker
**Business rule:** Combat Tracker moves to mob leader's turn. GM can only execute mob actions when it's the leader's turn. Other mob member turns are skipped.

#### All members execute same attack action as leader
**Business rule:** When GM executes an attack from the mob leader (choosing attack and target), Mob Manager associates that attack and target with the mob. When the strategy executes, Mob Manager forwards the exact same attack action to all mob member tokens. All members attack the same target with the same attack.

#### Attack Common Target strategy waits for GM attack then executes
**Business rule:** Attack Common Target strategy waits for GM to execute an attack from the mob leader onto another token. When GM executes the attack, Mob Manager associates that target and attack with the mob. When it's the mob's turn in Combat Tracker and both target and attack have been associated, the strategy executes automatically for all mob members.

---

## Stories (6 total)

### Story 1: Create Mob from Selected Tokens
*GM selects multiple tokens on canvas and Mob domain object creates mob with selected tokens*

**Acceptance Criteria:**
- When GM initates minion selection mode through hotkey then a simple dialog box appears with a default mob name field and empty list of members
- When GM selects multiple tokens on canvas, then Canvas System forwards token selection event to Mob Manager
- When Mob Manager recieves token selection event, then the Mob Manager aligns the mob membership with all selected tokens
- When Mob aligns it membership then it queries Token System to identify all selected tokens and add or remove from membership
- When Mob domain object updates Mob membership, then Mob domain object stores Mob instance and member tokens with the Mob Manager
- When a member of the mob is added to the combat tracker (by dragging or right-clicking "add to tracker"), then that member becomes the Mob leader
---

### Story 2: Display Mob Grouping in Combat Tracker
*Combat Tracker receives mob creation notification from Mob domain object and updates display to show mob membership*

**Acceptance Criteria:**

- When a mob member is added to combat tracker (by dragging or right-clicking "add to tracker"), then that member becomes the Mob leader
- When Mob leader is added to combat tracker, then combat tracker displays token indicating mob leader status, and indicating the number of members in the mob
- When any other mob member is added to the combat tracker a dialog box appears indicating that mob leader already added and the mob member is not added to the combat tracker
- When the membership is updated, then the mob leader indicator will change to reflect the updated number of people in the mob
- When the mob leader is removed from the mob and the leader was in combat tracker, then the mob leader is removed from the combat tracker

---

### Story 3: Execute Mob Attack with Strategy
*Combat Tracker moves to mob leader's turn, Mob domain object determines target from Select Target strategy, GM attacks with mob leader choosing attack and target, and Mob domain object forwards action to all members*

**Acceptance Criteria:**
- When Combat Tracker advances to next turn, then Combat Tracker notifies the Mob Manager about the the turn advancement
- When the Mob Manager is notified about turn advancement, the Mob Manager checks to see if the current turn's token is a mob leader
- When the Mob Manager identifies that it is a mob leader's turn, then the Mob Manager asks the Mob domain object to evaluate and execute the strategy associated with it
- When the Mob Manager evaluates the strategy associated with itand determines that the strategy has all the appropriate parameters determined it then executes the strategy (see story 3)
- when the Mob domain object executes the strategy it executes the attack as determined by the strategy on the target as determined by the strategy
- when the Mob domain object executes the attack on the target as determined by the strategy then it forwards that attackto the Mutants and masterminds combat system for every member in the mob

---

### Story 4: Display Attack Results in Chat
*Chat system receives attack result events from Combat system and displays formatted results for all mob members*

**Acceptance Criteria:**
- When Mob Manager forwards attacks to the Mutants and Masterminds combat system for all mob members, then the combat system executes attacks normally and sends attack result events to Chat System
- When Chat System receives attack result events, then Mob Manager intercepts the attack result events and reformats the attack chat dialogue to summarize all mob attacks results in one view
- When Mob Manager creates the summary chat dialogue, then Mob Manager provides a single resistance button for all mob attacks instead of individual resistance buttons for each attack
- When the user or GM clicks on the resistance button, then Mob Manager intercepts the resistance button click and runs the resistance roll for every attack that actually hit

---

### Story 5: Apply Attack Common Target Strategy
*GM selects Attack Common Target strategy for mob, and Mob domain object applies strategy when mob's turn begins by querying Combat Tracker for common target*

**Acceptance Criteria:**
- When GM selects Attack Common Target strategy for mob (currently automatically selected whenever we initiate creating a new mob ), then Mob Manager associates the mob being edited with the Attack Common Target strategy
- When Combat Tracker advances to next turn, then Combat Tracker notifies Mob Manager about the turn advancement
- When Mob Manager is notified about turn advancement, then Mob Manager checks to see if the current turn's token is a mob leader
- When Mob Manager identifies that it is a mob leader's turn, then Mob Manager retrieves the Attack Common Target strategy configuration for the mob
- When Mob Manager retrieves the strategy configuration, then Mob Manager determines if a common attack and or target has been selected for the mob
- when a common attack and target has not been selected for the mob then the Mob Manager waits for an attack to be executed by the mob leader on another token
- when the GM executes an attack from the mob leader onto another target with a specific attack then that target and that attack is associated with the mob
- when it is the mob's turn in the Combat tracker and an attack and a target has been associated with the mob strategy then the mob strategy executes (see story 3 for how this plays out)

---

### Story 6: Display Selected Common Target
*Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected common target*

**Acceptance Criteria:**
- When Mob Manager has determined the target and attack for a strategy, then Mob Manager stores the target and notifies the Mob Manager dialog of the changes in attack and target 
- When the Mob Manager dialog receives target / attack change notification, the Mob Manager dialog is updated to indicate who the target is and what the attack is

---

## Consolidation Decisions

No consolidation decisions made at this time. Acceptance criteria follow Inner System granularity with detailed component interactions. Similar logic patterns (e.g., "Display Selected Target" for different strategies) may be consolidated in future increments when those strategies are explored.

---

## Domain Rules Referenced

All domain rules are defined in the Domain Rules section above. Stories reference these rules implicitly through their acceptance criteria:
- Story 1 (Create Mob) references: "Mob must have at least one member token" and "Leader is assigned when member is added to combat tracker"
- Story 2 (Display Mob Grouping) references: "Leader is assigned when member is added to combat tracker" and "Leader is removed from combat tracker when removed from mob"
- Story 3 (Execute Mob Attack) references: "Mob actions execute only during mob leader turn" and "All members execute same attack action as leader"
- Story 4 (Display Attack Results) references: "Mob Manager wraps/intercepts existing systems to add new behavior"
- Story 5 (Apply Attack Common Target Strategy) references: "Attack Common Target strategy waits for GM attack then executes"

---

## Source Material

- **Story map from Shape stage:** Overarching epics, features, and stories for Manage Mobs in Foundry VTT
- **Discovery refinements from Discovery stage:** Enumerated all 6 stories for Increment 1 with component-level interactions
- **Planning decisions from Exploration stage:**
  - Acceptance criteria granularity: Inner System - Focus on technical interaction points, system-to-system communication, and internal system behavior. CRITICAL: Be MORE granular wherever there is an explicit business rule being activated that changes state or is an important decision.
  - Acceptance criteria count: Stop when criteria capture a full back-and-forth (user-system-user). Be detailed about business rules, state changes, and important decisions even if it increases AC count.
  - Acceptance criteria consolidation: Same logic, different data → Consolidate (even if data differs significantly). Focus on reusability.
- **Technical specifications:** Foundry VTT system integration requirements. Mutants & Masterminds system integration (https://github.com/Ethaks/foundry-mm3)
- **Component interactions:** Canvas System, Mob Domain Object, Combat Tracker, Token System, Combat System, Chat System

