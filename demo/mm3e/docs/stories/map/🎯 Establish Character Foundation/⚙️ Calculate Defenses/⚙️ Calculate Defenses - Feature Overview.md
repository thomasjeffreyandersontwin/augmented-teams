# ⚙️ Calculate Defenses - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Calculate Defenses  
**Stories:** 3 stories

---

## Feature Purpose

Automatically calculate all 5 defense values from ability ranks, distinguishing between active defenses (Dodge, Parry) and resistance defenses (Fortitude, Will, Toughness). Defenses are DERIVED from abilities - user doesn't set them directly, system calculates them based on ability ranks and displays them.

---

## Domain AC (Feature Level)

### Shared Concepts (from Higher Levels)
- **Character**: The superhero being created
- **Abilities**: The 8 core abilities (STR, STA, AGL, DEX, FGT, INT, AWE, PRE) - from Configure Abilities feature

### Feature-Specific Domain Concepts

**The 5 Defenses** (feature-scoped):

**Active Defenses** (opponent rolls against these):
- **Dodge**: Avoid attacks through agility and movement
  - Formula: `10 + Agility rank`
  - Source: Agility ability
  - Can purchase additional ranks (+1 pp per rank)
- **Parry**: Deflect/block attacks with combat skill
  - Formula: `10 + Fighting rank`
  - Source: Fighting ability
  - Can purchase additional ranks (+1 pp per rank)

**Resistance Defenses** (you roll these + d20):
- **Fortitude**: Resist physical effects (poison, disease, fatigue)
  - Formula: `Stamina rank`
  - Source: Stamina ability
  - Can purchase additional ranks (+1 pp per rank)
- **Will**: Resist mental effects (mind control, fear, illusions)
  - Formula: `Awareness rank`
  - Source: Awareness ability
  - Can purchase additional ranks (+1 pp per rank)
- **Toughness**: Resist damage
  - Formula: `Stamina rank`
  - Source: Stamina ability
  - **CANNOT purchase ranks** (only improved via advantages/powers)

**Defense Types Distinction**:
- **Active** (Dodge, Parry): Target number for opponent's attack roll (static value opponent must beat)
  - Formula: `10 + ability` (the +10 represents base defensive readiness)
  - Usage: Attacker rolls d20 + attack bonus vs your Dodge/Parry
- **Resistance** (Fortitude, Will, Toughness): You roll to resist effects
  - Formula: `ability rank` (no +10, because you roll d20 + ability rank + purchased ranks)
  - Usage: You roll d20 + Fortitude/Will/Toughness vs effect DC

**Base Defense Value** (feature-scoped):
- **Definition**: Defense value derived purely from ability (before purchased ranks)
- **Calculation**: Automatic when ability changes
- **Display**: Shown as "base" in defense display

### Domain Behaviors

**Calculate Active Defenses**:
- Apply formula: `10 + ability rank`
- For Dodge: Use Agility rank
- For Parry: Use Fighting rank
- Display immediately

**Calculate Resistance Defenses**:
- Apply formula: `ability rank` (no +10)
- For Fortitude: Use Stamina rank
- For Will: Use Awareness rank
- For Toughness: Use Stamina rank (same as Fortitude)
- Display immediately

**Display Defenses**:
- Show all 5 defenses with base values
- Indicate which ability each derives from
- Show calculation breakdown (base from ability)

### Domain Rules

1. **Active Defense Formula**: `Defense = 10 + Ability Rank` (Dodge, Parry only)
2. **Resistance Defense Formula**: `Defense = Ability Rank` (Fortitude, Will, Toughness)
3. **Toughness Special Rule**: Cannot purchase ranks (only via advantages/powers) - Handbook page 26
4. **Stamina Dual Impact**: Stamina sets BOTH Fortitude and Toughness (same value for both)
5. **Automatic Calculation**: Defenses calculate automatically when abilities set (not user-configured)

---

## Stories and Acceptance Criteria

### 📝 Story 1: System calculates active defenses from abilities

**Story Description**: System calculates active defenses from abilities - Dodge (10 + Agility), Parry (10 + Fighting)

#### Acceptance Criteria

**Dodge Calculation**:
- When Agility rank set or changes, then system calculates Dodge base (10 + Agility rank)
- When Agility = 0, then Dodge base = 10
- When Agility = 5, then Dodge base = 15
- When Agility = 10, then Dodge base = 20
- When Dodge calculated, then system stores Dodge base value

**Parry Calculation**:
- When Fighting rank set or changes, then system calculates Parry base (10 + Fighting rank)
- When Fighting = 0, then Parry base = 10
- When Fighting = 8, then Parry base = 18
- When Fighting = 12, then Parry base = 22
- When Parry calculated, then system stores Parry base value

**Formula Consistency**:
- When calculating any active defense, then system applies formula (10 + ability rank)
- When calculation error occurs, then system defaults to 10 (ability = 0)
- When active defenses calculated, then system marks them as "active" type

---

### 📝 Story 2: System calculates resistance defenses from abilities

**Story Description**: System calculates resistance defenses from abilities - Fortitude (Stamina), Will (Awareness), Toughness (Stamina)

#### Acceptance Criteria

**Fortitude Calculation**:
- When Stamina rank set or changes, then system calculates Fortitude base (Stamina rank, no +10)
- When Stamina = 0, then Fortitude base = 0
- When Stamina = 3, then Fortitude base = 3
- When Stamina = 12, then Fortitude base = 12
- When Fortitude calculated, then system stores Fortitude base value

**Will Calculation**:
- When Awareness rank set or changes, then system calculates Will base (Awareness rank, no +10)
- When Awareness = 0, then Will base = 0
- When Awareness = 2, then Will base = 2
- When Awareness = 8, then Will base = 8
- When Will calculated, then system stores Will base value

**Toughness Calculation**:
- When Stamina rank set or changes, then system calculates Toughness base (Stamina rank, no +10)
- When Stamina = 3, then Toughness base = 3 (same as Fortitude from Stamina)
- When Stamina = 12, then Toughness base = 12 (same as Fortitude from Stamina)
- When Toughness calculated, then system stores Toughness base value

**Formula Consistency**:
- When calculating any resistance defense, then system applies formula (ability rank, no +10)
- When Stamina changes, then BOTH Fortitude and Toughness recalculate (dual impact)
- When resistance defenses calculated, then system marks them as "resistance" type

---

### 📝 Story 3: System displays all 5 defense values

**Story Description**: System displays all 5 defense values - showing base calculation breakdown

#### Acceptance Criteria

**Display All Defenses**:
- When defenses section renders, then system displays all 5 defenses (Dodge, Parry, Fortitude, Will, Toughness)
- When each defense displayed, then system shows: name, current value, source ability, calculation formula
- When defenses displayed, then system groups by type (Active: Dodge/Parry, Resistance: Fortitude/Will/Toughness)

**Calculation Breakdown**:
- When Dodge displayed, then system shows "Dodge: 15 (10 + Agility 5)"
- When Parry displayed, then system shows "Parry: 18 (10 + Fighting 8)"
- When Fortitude displayed, then system shows "Fortitude: 3 (Stamina 3)"
- When Will displayed, then system shows "Will: 2 (Awareness 2)"
- When Toughness displayed, then system shows "Toughness: 3 (Stamina 3)"

**Real-time Updates**:
- When any linked ability changes, then defense display updates immediately
- When Stamina changes, then both Fortitude and Toughness displays update
- When defense values update, then system highlights changed value briefly (visual feedback)

**Purchase Indication**:
- When defense displayed, then system shows "(base)" for non-purchased defenses
- When defense displayed, then system shows purchase availability (Dodge, Parry, Fortitude, Will = Yes; Toughness = No)
- When user hovers over Toughness, then system displays tooltip "Cannot purchase Toughness ranks (use advantages/powers instead)"

---

## Consolidation Decisions

**Why 3 stories (not 5 for each defense)**:
- **Story 1**: Active defenses (Dodge, Parry) - same formula pattern (10 + ability), different abilities
- **Story 2**: Resistance defenses (Fort, Will, Tough) - same formula pattern (ability only), different abilities  
- **Story 3**: Display all 5 - single UI concern showing all defenses together
- **Rationale**: Consolidated by PATTERN (active vs resistance), not by individual defense

**Why NOT 5 separate stories (one per defense)**:
- Dodge and Parry use identical formula pattern (10 + ability)
- Fortitude, Will, Toughness use identical formula pattern (ability only)
- All defenses display in same section with same UI
- **Same formula pattern, different source ability** → Consolidate by pattern

**AC Consolidation**:
- Active defense calculations consolidated (same formula: 10 + ability)
- Resistance defense calculations consolidated (same formula: ability only)
- All defense displays consolidated (single UI section)
- Stamina's dual impact (Fortitude + Toughness) documented in resistance defense story

---

## Domain Rules Referenced

**From M&M 3E Handbook** (Chapter 3, Pages 110-111, "Defenses & Initiative"):
- **Dodge** (page 110): "Your Dodge defense equals 10 plus your Agility rank"
- **Parry** (page 110): "Your Parry defense equals 10 plus your Fighting rank"
- **Fortitude** (page 111): "Your Fortitude defense equals your Stamina rank"
- **Toughness** (page 111): "Your Toughness equals your Stamina rank" + "cannot be increased directly by spending power points"
- **Will** (page 111): "Your Will defense equals your Awareness rank"

**Active vs Resistance Distinction**:
- Handbook page 110: Active defenses (Dodge, Parry) are "target numbers" for attack rolls
- Handbook implies resistance defenses are rolled (d20 + defense vs DC) - standard M&M mechanic

**Key Insights**:
- Active defenses have +10 base because attacker rolls against static value
- Resistance defenses have no +10 because defender rolls d20 + defense value
- Toughness is special: derived like Fortitude but cannot purchase ranks
- Stamina is unique ability: affects TWO defenses simultaneously

**Formulas**:
```
Active Defenses:
  Dodge = 10 + Agility
  Parry = 10 + Fighting

Resistance Defenses:
  Fortitude = Stamina
  Will = Awareness
  Toughness = Stamina (same as Fortitude, but no rank purchase allowed)
```

---

## Source Material

**Referenced During Exploration**:
- Handbook pages 110-111 - Defense calculations and formulas
- Domain concepts document - The 5 Defenses table
- User clarification - Active vs resistance defense distinction (opponent rolls vs you roll)





