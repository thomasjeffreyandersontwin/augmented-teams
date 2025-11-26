# Story Map Increments: Manage Mobs in Foundry VTT

**Navigation:** [📋 Story Map](../map/mob-rule-story-map.md)

**File Name**: `mob-rule-story-map-increments.md`
**Location**: `mob_rule/docs/stories/increments/mob-rule-story-map-increments.md`

## Increment Strategy

**Approach**: Technical Proof of Concept → Mob Panel + Basic Strategies → Advanced Strategies → Attack Selection → AI-Assisted

**Risk Mitigation**: Foundry integration with components carries the most risk - technical POC addresses this first

**Architecture**: Mob as domain object with logic. Strategy objects (target selection, attack selection) as reusable components.

**Progression**: Basic mob creation → Mob panel + target strategies → Advanced target strategies → Attack selection strategies → Movement strategies → AI-assisted

---

## Increments

### Increment 1: Technical Proof of Concept and Drill-Down Stories
**Priority**: NOW  
**Relative Size**: Small  
**Approach**: Validating Impact - Feasibility + Delivering End-to-End Journey  
**Focus**: Foundry integration risk reduction and complete drill-down stories

**Stories**:
- 📝 Create Mob from Selected Tokens  
  *GM selects multiple minion tokens on canvas and Mob domain object creates mob with selected tokens and assigns random leader*
- 📝 Display Mob Grouping in Combat Tracker  
  *Combat Tracker receives mob creation notification from Mob domain object and updates display to show mob membership*
- 📝 Apply Attack Common Target Strategy  
  *GM selects Attack Common Target strategy for mob, and Mob domain object applies strategy when mob's turn begins by querying Combat Tracker for common target*
- 📝 Execute Mob Attack with Strategy  
  *Combat Tracker moves to mob leader's turn, Mob domain object determines target from Select Target strategy, GM attacks with mob leader choosing attack and target, and Mob domain object forwards action to all members*
- 📝 Display Attack Results in Chat  
  *Chat system receives attack result events from Combat system and displays formatted results for all mob members*

- 📝 Display Selected Common Target  
  *Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected common target*

**Purpose**: Validate Foundry VTT integration, Mob domain object, basic Combat Tracker/Actor/Actions integration. Complete all drill-down stories that showcase architectural complexity. Establishes strategy pattern foundation.

---

### Increment 2: Mob Panel and Basic Target Strategies
**Priority**: NEXT  
**Relative Size**: Medium  
**Approach**: Quick Win + Increasing Reuse/Dependency  
**Focus**: Mob panel UI and simplest target-focused strategies

**Stories**:
- 📝 Open Mob Configuration Panel  
  *GM clicks on mob leader token or mob entry in Combat Tracker, and Mob Panel UI opens displaying mob configuration options*
- 📝 Display Mob Configuration in Panel  
  *Mob Panel UI receives mob configuration from Mob domain object and displays mob members, current strategy, and available strategy options*
- 📝 Select Mob Strategy from Panel  
  *GM selects a strategy from Mob Panel UI dropdown, and Mob Panel UI sends strategy selection to Mob domain object which saves strategy configuration*
- 📝 Apply Attack Most Powerful Strategy  
  *When mob's turn begins, Mob domain object applies Attack Most Powerful strategy by querying Combat Tracker for all available targets, calculating power levels, and selecting most powerful target*
- 📝 Display Selected Most Powerful Target  
  *Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected most powerful target*
- 📝 Apply Attack Weakest Strategy  
  *When mob's turn begins, Mob domain object applies Attack Weakest strategy by querying Combat Tracker for all available targets, calculating power levels, and selecting weakest target*
- 📝 Display Selected Weakest Target  
  *Combat Tracker receives target selection notification from Mob domain object and updates display to show mob's selected weakest target*

**Purpose**: Establish mob panel UI and enable GM to select and configure basic target-focused strategies. Builds reusable strategy infrastructure and UI foundation.

---

### Increment 3: Advanced Target Strategies and Leader Configuration
**Priority**: NEXT  
**Relative Size**: Medium  
**Approach**: Maximizing Earned Value  
**Focus**: Advanced target strategies, leader configuration, and mob membership management

**Stories**:
- 📝 Apply Defend Leader Strategy
- 📝 Apply Retaliation Strategy
- 📝 Set Mob Leader (inside or outside mob)
- 📝 Modify Mob Membership (drag tokens from canvas onto panel mob member area)

**Purpose**: Enable advanced target strategies that require leader configuration. Enable GM to set leaders (internal or external) and manage mob membership through panel UI.

---

### Increment 4: Attack Selection Strategies
**Priority**: LATER  
**Relative Size**: Medium  
**Approach**: Quick Win + Increasing Reuse/Dependency  
**Focus**: Attack effectiveness strategies and sequential attack patterns

**Stories**:
- 📝 Apply Most Powerful Attack Strategy
- 📝 Apply Most Effective Attack Against Target Strategy
- 📝 Apply Sequential Attack Strategy (apply attacks in order, when one succeeds move to next)
- 📝 Apply Manual Attack Selection Strategy
- 📝 Apply Per-Member Attack Strategy

**Purpose**: Extend strategy pattern to attack selection. Enables mobs to choose optimal attacks based on target, including sequential attack patterns for tactical combinations (weaken then devastate).

---

### Increment 5: Movement and Range Strategies
**Priority**: LATER  
**Relative Size**: Medium  
**Approach**: Quick Win + Increasing Reuse/Dependency  
**Focus**: Movement strategies for positioning and range management

**Stories**:
- 📝 Move When Out of Range Strategy
- 📝 Determine Available Attacks (range, melee, pathfinding, area attack)
- 📝 Apply Pathfinding to Target Strategy

**Purpose**: Enable mobs to move strategically when out of range and determine appropriate attack types based on positioning.

---

### Increment 6: AI-Assisted Behavior - Targeting
**Priority**: LATER  
**Relative Size**: Large  
**Approach**: Validating Impact - Feasibility  
**Focus**: AI-assisted target selection

**Stories**:
- 📝 AI-Assisted Target Selection (foundation)
- 📝 AI-Assisted Target Analysis
- 📝 AI-Assisted Threat Assessment

**Purpose**: Enable AI-assisted behavior for intelligent target selection decisions.

---

### Increment 7: AI-Assisted Behavior - Attacks
**Priority**: LATER  
**Relative Size**: Large  
**Approach**: Validating Impact - Feasibility  
**Focus**: AI-assisted attack selection

**Stories**:
- 📝 AI-Assisted Attack Selection
- 📝 AI-Assisted Attack Effectiveness Analysis
- 📝 AI-Assisted Attack Sequencing

**Purpose**: Enable AI-assisted behavior for intelligent attack selection and sequencing decisions.

---

### Increment 8: AI-Assisted Behavior - Movement and Other
**Priority**: LATER  
**Relative Size**: Large  
**Approach**: Validating Impact - Feasibility  
**Focus**: AI-assisted movement and other behaviors

**Stories**:
- 📝 AI-Assisted Movement Decisions
- 📝 AI-Assisted Positioning
- 📝 AI-Assisted Other Behaviors

**Purpose**: Enable AI-assisted behavior for intelligent movement, positioning, and other tactical decisions.

---

### Increment 9: Aggression System
**Priority**: LATER  
**Relative Size**: Large  
**Approach**: Validating Impact - Feasibility  
**Focus**: MOB aggression component with MMO-style rules

**Stories**:
- 📝 Create Aggro System Component
- 📝 Calculate Aggro Values
- 📝 Apply Aggro-Based Target Selection Strategy
- 📝 Apply Automated Aggro Management

**Purpose**: Advanced strategy system using MMO-style aggression/threat mechanics.

---

### Increment 10: Player Mob Management
**Priority**: LATER  
**Relative Size**: Medium  
**Approach**: Maximizing Earned Value  
**Focus**: Enable players to manage mobs with GM permission

**Stories**:
- 📝 Player Requests Mob Creation
- 📝 GM Approves Player Mob
- 📝 Player Configures Mob Strategy
- 📝 Player Executes Mob Actions

**Purpose**: Extend mob management to players while maintaining GM oversight.

---

## Architectural Notes

**Mob Domain Object**: Core domain object containing mob logic, not a separate "mob manager". Contains member tokens, leader, strategy references.

**Strategy Objects**: Reusable components responsible for:
- Target selection (first set of strategies)
- Attack selection (second set of strategies)
- Movement and positioning (later iterations)
- Advanced behaviors (AI-assisted, aggression)

**Integration Priority**: Combat Tracker → Actor System → Actions → Mob Panel UI → Advanced Features

**Reuse Strategy**: Build strategy infrastructure early (Increment 2) to enable all subsequent strategy features.

**AI Strategy**: AI-assisted behavior split into three increments (targeting, attacks, movement) as it's complex and should be last.
