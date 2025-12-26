# Discovery Clarification - Increment 1: Foundational Integration + Basic Mob

## Increment Scope

**Question:** What is the full scope of the next increment or release?

**Answer:** Increment 1 includes 11 stories across 3 epics:
- **Map Foundry API** (8 stories) - All sub-epics: Map Token System, Map Actor System, Map Combat System, Map Targeting System
- **Manage Mobs - Create Mob** (2 stories) - Select Minions, Group Minions Into Mob
- **Execute Mob Actions - Coordinate Attack** (1 story) - Execute Melee Attack

**Goal:** Validate Foundry VTT API integration works and deliver core mob coordination feature (group minions, execute coordinated melee attack).

## Major Workflows

**Question:** What are the major workflows or process segments it touches?

**Answer:**

### Workflow 1: Foundry API Integration
1. Token selection and state management
2. Actor data loading and capability evaluation
3. Combat tracker registration
4. Target identification and setting
5. Attack feasibility determination

### Workflow 2: Mob Creation
1. GM selects multiple minion tokens in Foundry
2. System groups selected minions into mob
3. Mob data structure created and persisted

### Workflow 3: Coordinated Melee Attack
1. GM clicks any minion in mob
2. System identifies all mob members
3. System identifies valid targets
4. Each minion in mob executes melee attack on target
5. Combat results displayed in Foundry

## Systems, Teams, and Roles

**Question:** What systems, teams, or roles are involved across this flow?

**Answer:**

### External Systems:
- **Foundry Virtual Tabletop** - VTT platform providing token, actor, combat, and targeting APIs
  - Token Management System
  - Actor Data System
  - Combat Tracker System
  - Targeting System

### Internal Components:
- **Mob System** - Our system managing mob groupings and coordination

### User Roles:
- **Game Master (GM)** - Primary user creating mobs and triggering actions
- **Foundry API** - System-to-system integration layer

### Teams (Development):
- Single development team implementing Foundry VTT module

## Story Groupings

**Question:** What story groupings or capabilities define this increment?

**Answer:**

### Group 1: Foundry API Foundation (8 stories - ENABLER)
**Capability:** Integrate with Foundry VTT systems
- Sub-group: Token System (2 stories)
- Sub-group: Actor System (2 stories)  
- Sub-group: Combat System (2 stories)
- Sub-group: Targeting System (2 stories)

### Group 2: Basic Mob Management (2 stories - USER VALUE)
**Capability:** Create mobs from minions
- Story: Select Minions
- Story: Group Minions Into Mob

### Group 3: Coordinated Attack (1 story - USER VALUE)
**Capability:** Execute synchronized mob action
- Story: Execute Melee Attack

## Story Sequence and Order

**Question:** What order or sequence do these stories need to follow?

**Answer:**

### Phase 1: API Foundation (Parallel Development Possible)
Can be developed in parallel within each sub-system:
1. Token System integration (2 stories)
2. Actor System integration (2 stories)
3. Combat System integration (2 stories)
4. Targeting System integration (2 stories)

**All must complete before Phase 2**

### Phase 2: Mob Creation (Sequential)
Requires Token System from Phase 1:
1. Select Minions (depends on: Retrieve Token Selection State)
2. Group Minions Into Mob (depends on: Select Minions + Actor System)

### Phase 3: Coordinated Attack (Sequential)
Requires all of Phase 1 + Phase 2:
1. Execute Melee Attack (depends on: Mob exists, Combat System, Targeting System, Attack Feasibility)

**Critical Path:** API Foundation → Mob Creation → Coordinated Attack

## Major Transitions and Integration Points

**Question:** Where are the major transitions or integration points in the flow?

**Answer:**

### Integration Point 1: Foundry → Mob System
**Transition:** Token selection to mob creation
- **FROM:** Foundry Token System (GM selects tokens)
- **TO:** Mob System (creates mob data structure)
- **Data:** Token IDs, Actor references

### Integration Point 2: Mob System → Foundry
**Transition:** Mob action trigger to Foundry execution
- **FROM:** Mob System (GM clicks mob minion)
- **TO:** Foundry Combat/Action System
- **Data:** Mob member list, target selection, action type

### Integration Point 3: Actor Data Query
**Transition:** Need actor stats for capabilities
- **FROM:** Mob System (determining what actions possible)
- **TO:** Foundry Actor System
- **Data:** HP, power level, attack capabilities, range

### Integration Point 4: Combat State
**Transition:** Register and track combatants
- **FROM:** Mob System (mob members in combat)
- **TO:** Foundry Combat Tracker
- **Data:** Initiative, turn order, combatant state

### Integration Point 5: Target Selection
**Transition:** Identify and set attack targets
- **FROM:** Mob System (coordinating attack)
- **TO:** Foundry Targeting System
- **Data:** Valid target list, target selection

## Dependencies

**Question:** Are any stories or features dependent on others being completed first?

**Answer:**

### Hard Dependencies (Must Complete First):

**Retrieve Token Selection State** enables:
- Select Minions (can't select without knowing selection state)

**Update Token State** + **Load Actor Statistics** enable:
- Group Minions Into Mob (need to update token membership and access actor data)

**Register Combatant In Tracker** enables:
- Execute Melee Attack (minions must be in combat tracker)

**Determine Attack Feasibility** + **Identify Valid Combat Targets** + **Set Target** enable:
- Execute Melee Attack (must know if attack possible and who to target)

**Group Minions Into Mob** enables:
- Execute Melee Attack (must have mob before coordinated action)

### Soft Dependencies (Recommended Order):

**Evaluate Actor Combat Capabilities** should precede:
- Determine Attack Feasibility (capabilities inform feasibility)

### Parallel Work Opportunities:

These can be developed simultaneously:
- All 4 Foundry API sub-systems (Token, Actor, Combat, Targeting)
- Update Token State and Load Actor Statistics (different systems)

## Risk Areas

**Critical Integration Risks:**
1. **Foundry API Documentation** - May be incomplete or inaccurate
2. **API Stability** - Proprietary API may change between versions
3. **Event System** - May not have hooks we need for mob coordination
4. **Action Execution** - Programmatic action triggering may have limitations

**Validation Strategy:**
- Build API integration stories first (Phase 1)
- Fail fast if Foundry doesn't support required features
- Spike/prototype API calls before full implementation

