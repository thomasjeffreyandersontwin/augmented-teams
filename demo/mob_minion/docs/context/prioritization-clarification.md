# Prioritization Clarification - Mob Minion System

## Risk Assessment

**Question:** Which areas of the story map carry the most business or delivery risk?

**Answer:** 
1. **Foundry API Integration (Epic 1)** - HIGHEST RISK
   - Proprietary API with potential breaking changes
   - Unknown API stability and capabilities
   - Integration complexity with token, actor, combat, and targeting systems
   - Risk: API may not support required mob coordination features

2. **Strategy Execution (Epic 4)** - MODERATE RISK
   - Complex coordination logic across multiple minions
   - Performance concerns with many simultaneous actions
   - Edge cases around range, movement, and target validity

3. **Mob Management (Epic 2)** - LOW RISK
   - Standard CRUD operations
   - Well-understood patterns

4. **Strategy Selection (Epic 3)** - LOW RISK
   - Simple assignment logic

## Value Delivery

**Question:** Which areas are expected to deliver the most value if delivered early?

**Answer:**
1. **Create Basic Mob + Execute Simple Attack (Epics 2 & 4)** - HIGHEST VALUE
   - Core "wow" moment: Click one minion, mob attacks together
   - Eliminates primary pain point (individual token clicking)
   - Delivers immediate GM delight

2. **Strategy Assignment (Epic 3)** - HIGH VALUE
   - Differentiates mob behavior
   - Makes mobs tactical, not just grouped
   - Enables strategic gameplay

3. **Foundry API Mapping (Epic 1)** - ENABLING VALUE
   - Must complete first to enable other features
   - Not directly valuable to users but required foundation

4. **Advanced Mob Features (Edit, Spawn, Templates)** - MODERATE VALUE
   - Quality of life improvements
   - Can wait until after core loop works

## Complexity vs Value

**Question:** Which areas are the most complex or hardest to implement, relative to their value?

**Answer:**
1. **Mob Templates (Epic 2 - Spawn Mob)** - HIGH COMPLEXITY, MODERATE VALUE
   - Requires template storage, configuration UI, spawning logic
   - Value is convenience, not core functionality
   - Can defer to later increment

2. **Strategy Evaluation (Epic 4 - Select Targets)** - MODERATE COMPLEXITY, HIGH VALUE
   - Must query actor stats, evaluate criteria, rank targets
   - Critical for strategy differentiation
   - Worth the complexity for value delivered

3. **Foundry API Integration (Epic 1)** - MODERATE-HIGH COMPLEXITY, ENABLING VALUE
   - Required foundation but complex
   - Must be first increment despite complexity

## End-to-End Slices

**Question:** Do you want thin slices to be as end-to-end as possible?

**Answer:** YES - Absolutely. Each increment should deliver a complete, testable user experience:
- Increment 1: GM can create a basic mob and see coordinated attack
- Increment 2: GM can assign strategies and see different targeting behaviors
- Increment 3: GM can modify mobs and use templates for spawning

Each slice should be demonstrable and valuable to GMs.

## Reusable Components

**Question:** Are there any components, capabilities, or services that need to be reused across multiple stories or features?

**Answer:**
1. **Foundry API Integration Layer (Epic 1)** - FOUNDATIONAL
   - Token selection, actor data, combat tracker, targeting
   - Required by ALL other epics
   - Must be Increment 1

2. **Target Selector** - REUSED
   - Used by strategy evaluation AND attack execution
   - Build once in early increment

3. **Mob Data Model** - REUSED
   - Create/Edit/Spawn all work with same mob structure
   - Define early, extend later

## Project Constraints

**Question:** Are there any project or program constraints that impact delivery order?

**Answer:**
- **Foundry VTT API Stability**: Must validate API capabilities early before building dependent features
- **GM Testing Availability**: Need early feedback on mob coordination UX
- **Game Session Schedule**: Want usable feature for upcoming game sessions (time pressure)
- **No Constraints on**: Budget, team size, technology stack (all Foundry VTT based)

## User Rollout Order

**Question:** Are there users or groups that must go first to enable others to follow?

**Answer:**
- **Single User Type**: Only Game Masters use this feature
- **No Sequential Rollout**: All GMs can adopt simultaneously
- **Self-Contained**: No dependencies on other user groups
- **Phased Feature Rollout**: Could release increments progressively:
  1. Basic mob creation + simple attacks (early adopters)
  2. Strategy system (all GMs)
  3. Advanced features (power users)

## Recommended Increment Strategy

Based on the above analysis:

### Increment 1: Foundational Integration + Basic Mob
**Goal:** Prove Foundry API works, deliver core value
- Map Foundry API (all sub-epics)
- Create Mob (select + group minions)
- Execute simple coordinated melee attack
- **Value:** GM can group minions and attack together
- **Risk Mitigation:** Validates Foundry API early

### Increment 2: Strategy System
**Goal:** Make mobs tactical and intelligent
- Assign Strategies (all strategy types)
- Select Targets (identify + apply criteria)
- Execute all attack types (melee, ranged, area)
- **Value:** Strategic mob behavior differentiation
- **Builds On:** Increment 1 foundation

### Increment 3: Advanced Mob Management
**Goal:** Polish and convenience features
- Edit Mob (add/remove/disband)
- Spawn Mob (templates + actors)
- Mob Templates
- **Value:** Quality of life improvements
- **Low Risk:** Well-understood CRUD operations

Each increment is end-to-end, testable, and delivers independent value.

