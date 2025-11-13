# ⚙️ Configure Abilities - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Configure Abilities  
**Stories:** 5 stories

---

## Feature Purpose

Enable user to configure the 8 core ability ranks for their character (Strength, Stamina, Agility, Dexterity, Fighting, Intellect, Awareness, Presence), with system calculating point costs, updating point budget, and cascading changes to dependent defenses in real-time. Abilities are the foundation of the character - every other trait builds upon them.

---

## Domain AC (Feature Level)

### Shared Concepts (from Solution Level)
- **Character**: The superhero being created
- **Power Points**: Currency for purchasing traits
- **Point Budget**: Total points available (from Power Level selection)

### Feature-Specific Domain Concepts

**The 8 Abilities** (feature-scoped):

| Ability | Abbreviation | Primary Use | Affects |
|---------|--------------|-------------|---------|
| **Strength** | STR | Physical power, lifting, damage | Athletics skill |
| **Stamina** | STA | Endurance, health, toughness | Fortitude defense, Toughness defense |
| **Agility** | AGL | Balance, grace, dodging | Dodge defense, Acrobatics/Stealth skills |
| **Dexterity** | DEX | Coordination, accuracy | Ranged attacks, Sleight of Hand skill |
| **Fighting** | FGT | Close combat skill | Parry defense, Close Combat skill |
| **Intellect** | INT | Reasoning, knowledge | Investigation, Technology skills |
| **Awareness** | AWE | Perception, willpower | Will defense, Perception/Insight skills |
| **Presence** | PRE | Personality, charisma | Persuasion, Intimidation, Deception skills |

**Ability Rank** (feature-scoped):
- **Scale**: -5 (far below average) to 20 (cosmic-level), with 0 = average
- **Rank Meanings**:
  - -5 to 0 = Below average to average
  - 1-2 = Above average
  - 3-4 = Exceptional
  - 5-7 = Peak human
  - 8-12 = Superhuman
  - 13-20 = Cosmic-level
- **Cost**: 2 power points per rank
- **Default**: 0 (average) for all abilities at character creation start

**Ability Points Spent** (feature-scoped):
- **Calculation**: Sum of all ability costs
- **Formula**: `Total Ability Points = Σ(ability_rank × 2)` for all 8 abilities
- **Tracking**: Part of overall point budget (spent/total)

**Cascading Dependencies** (feature-scoped):
- **Ability-to-Defense Mappings**:
  - Agility → Dodge base value
  - Fighting → Parry base value
  - Stamina → Fortitude base value + Toughness base value (two defenses!)
  - Awareness → Will base value
  - Other 4 abilities → No defense impact
- **Trigger**: When any ability rank changes, linked defense(s) must recalculate

### Domain Behaviors

**Set Ability Rank**:
- User adjusts rank for any of 8 abilities
- Calculate cost: `rank × 2`
- Deduct from point budget
- Trigger cascade updates

**Calculate Ability Points**:
- Sum costs for all 8 abilities
- Formula: `Σ(rank × 2)` for STR, STA, AGL, DEX, FGT, INT, AWE, PRE
- Update total spent

**Update Point Budget**:
- Recalculate remaining: `Total - Spent`
- Display spent/total
- Flag overspend if spent > total (warn, don't prevent)

**Cascade to Defenses**:
- When Agility changes → recalculate Dodge (10 + new Agility)
- When Fighting changes → recalculate Parry (10 + new Fighting)
- When Stamina changes → recalculate Fortitude (new Stamina) AND Toughness (new Stamina)
- When Awareness changes → recalculate Will (new Awareness)
- When other abilities change → no defense updates

### Domain Rules

1. **Ability Cost Formula**: `Cost = Ability Rank × 2` (Handbook page 26, Basic Trait Costs table)
2. **Total Ability Cost**: `Total = Σ(rank × 2)` for all 8 abilities
3. **Cascading Rule**: Ability changes trigger immediate defense recalculation (no delay)
4. **Default Rank**: All abilities start at 0 (average) unless explicitly set
5. **Negative Ranks Allowed**: Abilities can be -5 to -1 (below average, refunds points)
6. **Maximum Rank**: No hard cap at ability level (PL caps apply to skills/attacks that USE abilities)

---

## Stories and Acceptance Criteria

### 📝 Story 1: User sets ability rank for any of 8 abilities

**Story Description**: User sets ability rank for any of 8 abilities - and system calculates point cost (rank × 2)

#### Acceptance Criteria

**Set Rank**:
- When user sets Strength rank, then system calculates cost (rank × 2)
- When user sets Stamina rank, then system calculates cost (rank × 2)
- When user sets Agility rank, then system calculates cost (rank × 2)
- When user sets Dexterity rank, then system calculates cost (rank × 2)
- When user sets Fighting rank, then system calculates cost (rank × 2)
- When user sets Intellect rank, then system calculates cost (rank × 2)
- When user sets Awareness rank, then system calculates cost (rank × 2)
- When user sets Presence rank, then system calculates cost (rank × 2)

**Cost Calculation Examples**:
- When ability rank set to 0, then cost = 0 points
- When ability rank set to 5, then cost = 10 points
- When ability rank set to 10, then cost = 20 points
- When ability rank set to -2, then cost = -4 points (refund)

**Immediate Application**:
- When cost calculated, then system deducts/adds points to budget immediately
- When rank changes, then system recalculates cost and updates budget
- When rank set, then system stores new rank value with character

---

### 📝 Story 2: System displays all 8 abilities with current ranks

**Story Description**: System displays all 8 abilities with current ranks - STR, STA, AGL, DEX, FGT, INT, AWE, PRE

#### Acceptance Criteria

**Display All Abilities**:
- When abilities section renders, then system displays all 8 abilities in order (STR, STA, AGL, DEX, FGT, INT, AWE, PRE)
- When each ability displayed, then system shows abbreviation, full name, and current rank
- When ability rank is 0, then system shows "0" (average)

**Ability Details**:
- When ability displayed, then system shows cost for current rank (rank × 2)
- When user hovers over ability, then system displays tooltip with ability description and uses
- When ability has negative rank, then system shows rank in warning color (below average)

**Visual Organization**:
- When abilities rendered, then system groups them logically (physical: STR/STA, reflexes: AGL/DEX, combat: FGT, mental: INT/AWE/PRE)
- When any ability changes, then system updates display immediately
- When abilities section displayed, then system shows total ability points spent

---

### 📝 Story 3: System calculates total ability points spent

**Story Description**: System calculates total ability points spent - sum of all ability costs

#### Acceptance Criteria

**Calculate Total**:
- When any ability rank changes, then system recalculates total ability points (Σ(rank × 2) for all 8)
- When calculation completes, then system displays total ability points spent
- When all abilities at rank 0, then total = 0 points

**Calculation Examples**:
- When STR=5, STA=3, others=0, then total = (5×2) + (3×2) = 16 points
- When all abilities set to rank 2, then total = 8 abilities × 2 ranks × 2 pp/rank = 32 points
- When ability has negative rank (e.g., STR=-2), then reduces total by 4 points

**Display**:
- When total calculated, then system displays in abilities section header
- When total changes, then system updates display in real-time
- When total displayed, then system shows breakdown by ability (e.g., "STR: 10pp, STA: 6pp, ...")

---

### 📝 Story 4: System updates remaining point budget

**Story Description**: System updates remaining point budget - total points - spent points

#### Acceptance Criteria

**Budget Calculation**:
- When ability points spent changes, then system recalculates remaining budget (total - spent)
- When remaining calculated, then system updates budget display immediately
- When spent exceeds total, then system shows negative remaining (overspend warning)

**Budget Display Updates**:
- When abilities configured, then budget shows "spent / total" format (e.g., "16 / 150")
- When remaining positive, then system displays in normal color
- When remaining zero, then system displays "Budget Used" message
- When remaining negative (overspent), then system displays overspend amount in warning color

**Real-time Updates**:
- When any ability rank adjusted, then budget updates within 100ms (immediate feedback)
- When multiple abilities changed in sequence, then budget recalculates after each change
- When budget displayed, then system includes progress bar visual (spent/total ratio)

---

### 📝 Story 5: System updates dependent defenses when linked ability changes

**Story Description**: System updates dependent defenses when linked ability changes - AGL→Dodge, FGT→Parry, STA→Fortitude+Toughness, AWE→Will

#### Acceptance Criteria

**Agility → Dodge**:
- When Agility rank changes, then system recalculates Dodge base (10 + new Agility rank)
- When Dodge recalculated, then system updates Dodge display
- When Agility set to 5, then Dodge base = 15

**Fighting → Parry**:
- When Fighting rank changes, then system recalculates Parry base (10 + new Fighting rank)
- When Parry recalculated, then system updates Parry display  
- When Fighting set to 8, then Parry base = 18

**Stamina → Fortitude + Toughness**:
- When Stamina rank changes, then system recalculates Fortitude base (new Stamina rank)
- When Stamina rank changes, then system recalculates Toughness base (new Stamina rank)
- When both defenses recalculated, then system updates both displays
- When Stamina set to 3, then Fortitude base = 3 AND Toughness base = 3

**Awareness → Will**:
- When Awareness rank changes, then system recalculates Will base (new Awareness rank)
- When Will recalculated, then system updates Will display
- When Awareness set to 2, then Will base = 2

**No Defense Impact**:
- When Strength changes, then system does NOT update any defenses
- When Dexterity changes, then system does NOT update any defenses
- When Intellect changes, then system does NOT update any defenses
- When Presence changes, then system does NOT update any defenses

**Cascade Timing**:
- When ability changes, then defense updates occur immediately (within same update cycle)
- When multiple defenses updated (Stamina case), then all update together
- When user sees ability change, then user sees defense change at same time (synchronous)

---

## Consolidation Decisions

**Why 5 stories (not 8)**:
- **Consolidated**: All 8 abilities use identical cost formula (rank × 2) - same logic, different data
- **Consolidated**: Display logic same for all 8 abilities - same UI pattern
- **Consolidated**: Total calculation sums all 8 - single aggregation operation
- **Consolidated**: Cascading dependencies handled as single system behavior (not per-ability stories)
- **Rationale**: Different abilities are data variations, not logic variations

**AC Consolidation**:
- All 8 ability cost calculations consolidated (same formula)
- All 4 ability-to-defense cascades enumerated in single story (system behavior, not user-facing)
- Budget updates consolidated (same calculation regardless of which ability changed)

**Why NOT 8 separate stories for setting each ability**:
- Same cost formula for all: `rank × 2`
- Same UI interaction pattern for all
- Same budget impact logic for all
- Only difference is which ability and which defense(s) cascade
- Different data (which ability), same logic → ONE story

---

## Domain Rules Referenced

**From M&M 3E Handbook** (Chapter 3, Pages 107-112):
- **Ability Cost** (page 26): 2 power points per rank
- **Ability Descriptions** (pages 108-109): What each ability represents
- **Ability Rank Scale** (page 108): -5 to 20 scale with meanings
- **Defense Calculations** (pages 110-111):
  - Dodge = 10 + Agility
  - Parry = 10 + Fighting
  - Fortitude = Stamina
  - Toughness = Stamina
  - Will = Awareness
- **Character Examples** (pages 51-54):
  - The Rook: Agility 5, Fighting 8 (detective/crime fighter build)
  - Princess: Strength 12, Stamina 12 (powerhouse build)

**Cascading Dependencies Confirmed**:
- Handbook page 110: "Your Dodge defense is 10 + your Agility rank"
- Handbook page 110: "Your Parry defense is 10 + your Fighting rank"
- Handbook page 111: "Your Fortitude defense equals your Stamina rank"
- Handbook page 111: "Your Toughness equals your Stamina rank"
- Handbook page 111: "Your Will defense equals your Awareness rank"

**Key Insights**:
- Stamina is unique - affects TWO defenses (Fortitude + Toughness)
- Active defenses (Dodge, Parry) add +10 base (opponent rolls against them)
- Resistance defenses (Fortitude, Will, Toughness) no +10 (you roll with them + d20)
- Abilities can be negative (-5 to -1) for below-average characters

**Formulas**:
```
Ability Cost = Rank × 2
Total Ability Points = Σ(rank × 2) for all 8 abilities
Remaining Budget = Total Points - Spent Points

Cascading:
  Agility → Dodge = 10 + Agility
  Fighting → Parry = 10 + Fighting
  Stamina → Fortitude = Stamina AND Toughness = Stamina
  Awareness → Will = Awareness
```

---

## Stories and Acceptance Criteria

### 📝 Story 1: User sets ability rank for any of 8 abilities

**Story Description**: User sets ability rank for any of 8 abilities - and system calculates point cost (rank × 2)

#### Acceptance Criteria

**Set Rank (Same Logic for All 8)**:
- When user sets any ability rank (STR/STA/AGL/DEX/FGT/INT/AWE/PRE), then system calculates cost (rank × 2)
- When user increases ability rank, then system deducts cost from remaining budget
- When user decreases ability rank, then system refunds cost to remaining budget
- When ability rank set to negative value, then system adds points to budget (refund for flaw)

**Cost Calculation (Formula: rank × 2)**:
- When ability rank = 0, then cost = 0 points
- When ability rank = 5, then cost = 10 points
- When ability rank = 10, then cost = 20 points
- When ability rank = -2, then cost = -4 points (refund)

**Immediate Storage**:
- When rank calculated, then system stores new rank value with character
- When rank stored, then system marks ability as configured
- When any rank set, then system enables ability-dependent features (skills, defenses)

---

### 📝 Story 2: System displays all 8 abilities with current ranks

**Story Description**: System displays all 8 abilities with current ranks - STR, STA, AGL, DEX, FGT, INT, AWE, PRE

#### Acceptance Criteria

**Display All 8 Abilities**:
- When abilities section renders, then system displays all 8 abilities in standard order (STR, STA, AGL, DEX, FGT, INT, AWE, PRE)
- When each ability displayed, then system shows: abbreviation, full name, current rank, cost
- When abilities displayed, then system shows rank adjustment controls (increment/decrement or number input)

**Ability Details**:
- When ability displayed, then system shows cost for current rank (rank × 2 pp)
- When user hovers over ability name, then system displays tooltip with ability description
- When ability rank is 0, then system displays "0 (Average)"
- When ability rank is negative, then system displays rank in warning style (e.g., "-2 (Below Average)")

**Visual Organization**:
- When abilities section rendered, then system organizes into logical groups:
  - Physical: STR, STA
  - Reflexes: AGL, DEX
  - Combat: FGT
  - Mental: INT, AWE, PRE
- When any ability changes, then system updates that ability's display immediately
- When abilities displayed, then system shows total ability points spent at bottom

---

### 📝 Story 3: System calculates total ability points spent

**Story Description**: System calculates total ability points spent - sum of all ability costs

#### Acceptance Criteria

**Calculate Total**:
- When any ability rank changes, then system recalculates total (Σ(rank × 2) for all 8 abilities)
- When calculation completes, then system displays total in abilities section
- When all abilities at rank 0, then total = 0 points

**Calculation Examples**:
- When STR=5 (10pp), STA=3 (6pp), all others=0, then total = 16 points
- When all 8 abilities set to rank 2, then total = 8 × 2 × 2 = 32 points
- When STR=5 (10pp), DEX=-2 (-4pp), others=0, then total = 6 points

**Display Format**:
- When total calculated, then system displays as "Ability Points: X / [total budget]"
- When total updates, then system animates change (visual feedback)
- When user views abilities, then total always visible (sticky header or summary panel)

---

### 📝 Story 4: System updates remaining point budget

**Story Description**: System updates remaining point budget - total points - spent points

#### Acceptance Criteria

**Budget Recalculation**:
- When ability points spent changes, then system recalculates remaining (Total - Spent for ALL categories)
- When remaining calculated, then system updates main budget display
- When spent > total, then system shows overspend warning (but allows continuing)

**Budget Display**:
- When budget updates, then system shows format "Spent / Total" (e.g., "32 / 150 points")
- When remaining positive, then system displays remaining in normal color
- When remaining = 0, then system displays "Budget Fully Used" indicator
- When remaining negative, then system displays "Over Budget by X points" in warning color

**Real-time Feedback**:
- When ability rank adjusted, then budget updates immediately (< 100ms)
- When multiple abilities changed rapidly, then budget recalculates after each change
- When budget displayed, then system includes visual progress bar (spent/total ratio)

---

### 📝 Story 5: System updates dependent defenses when linked ability changes

**Story Description**: System updates dependent defenses when linked ability changes - AGL→Dodge, FGT→Parry, STA→Fortitude+Toughness, AWE→Will

#### Acceptance Criteria

**Agility → Dodge Cascade**:
- When Agility rank changes, then system immediately recalculates Dodge base (10 + Agility)
- When Agility set to 0, then Dodge base = 10
- When Agility set to 5, then Dodge base = 15
- When Dodge recalculated, then Dodge display updates

**Fighting → Parry Cascade**:
- When Fighting rank changes, then system immediately recalculates Parry base (10 + Fighting)
- When Fighting set to 0, then Parry base = 10
- When Fighting set to 8, then Parry base = 18
- When Parry recalculated, then Parry display updates

**Stamina → Fortitude + Toughness Cascade**:
- When Stamina rank changes, then system recalculates BOTH Fortitude (Stamina) AND Toughness (Stamina)
- When Stamina set to 3, then Fortitude base = 3 AND Toughness base = 3
- When Stamina set to 12, then Fortitude base = 12 AND Toughness base = 12
- When both defenses recalculated, then both defense displays update

**Awareness → Will Cascade**:
- When Awareness rank changes, then system immediately recalculates Will base (Awareness)
- When Awareness set to 0, then Will base = 0
- When Awareness set to 2, then Will base = 2
- When Will recalculated, then Will display updates

**No Cascade for Other 4 Abilities**:
- When Strength changes, then system does NOT update any defenses
- When Dexterity changes, then system does NOT update any defenses
- When Intellect changes, then system does NOT update any defenses
- When Presence changes, then system does NOT update any defenses

**Synchronous Updates**:
- When ability changes, then defense cascade occurs in same update cycle (not delayed)
- When user sees ability value update, then user sees defense value update simultaneously
- When cascade completes, then system marks both ability and defense as updated

---

## Consolidation Decisions

**Why 5 stories (not 8 for abilities or 4 for cascades)**:
- **Story 1**: Setting rank uses same logic for all 8 abilities (consolidated)
- **Story 2**: Displaying all 8 abilities is one UI concern (consolidated)
- **Story 3**: Calculating total is single aggregation (consolidated)
- **Story 4**: Budget update is single calculation (consolidated)
- **Story 5**: Cascade logic enumerated as system behavior (all 4 ability→defense mappings in one story)

**Why NOT separate stories per ability**:
- Cost formula identical for all 8: `rank × 2`
- UI pattern identical for all 8: display + rank control
- Budget impact identical for all 8: deduct cost from budget
- Only difference is WHICH ability and WHICH defense cascades
- **Same logic, different data** → Consolidated

**Why NOT separate stories per cascade**:
- Cascade is system-side behavior (not user-initiated)
- All cascades trigger on same event (ability change)
- Different defense formulas but same triggering logic
- Enumerated in single story for completeness

---

## Domain Rules Referenced

**From M&M 3E Handbook**:
- Chapter 3, Page 107: "Buying Ability Ranks" - costs 2 power points per rank
- Chapter 3, Pages 108-109: Detailed descriptions of all 8 abilities
- Page 26, Basic Trait Costs table: "Ability: 2 per ability rank"
- Page 110-111: Defense base calculations from abilities
- Character creation examples (pages 51-54): Jon assigns abilities first, calculates defenses second

**From Domain Concepts Document**:
- The 8 Abilities table with abbreviations and what they affect
- Ability rank scale (-5 to 20)
- Dependencies & Cascading Updates section

---

## Source Material

**Referenced During Exploration**:
- `demo/mm3e/docs/mm3e-handbook-reference.txt` - Chapter 3 (Abilities), pages 107-112
- `demo/mm3e/docs/mm3e-domain-concepts.md` - The 8 Abilities section, Dependencies section
- Handbook page 26 - Basic Trait Costs table
- Handbook pages 51-54 - Character creation examples showing ability→defense flow





