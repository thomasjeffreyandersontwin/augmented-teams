# ⚙️ Select Power Level - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Select Power Level  
**Stories:** 5 stories

---

## Feature Purpose

Enable user to select the Power Level (PL) for their character, which determines the character's overall power scale, starting power points budget, and all power level caps that govern character building. PL is the foundational decision that sets constraints for all subsequent character creation choices.

---

## Domain AC (Feature Level)

### Shared Concepts (from Solution Level)
- **Character**: The superhero being created
- **User**: The player creating the character  
- **Power Points**: Currency for purchasing traits (defined at solution level)

### Feature-Specific Domain Concepts

**Power Level (PL)** (feature-scoped):
- **Definition**: Numerical rating from 1-20+ representing overall character power scale
- **Purpose**: Sets budget and caps for character building
- **Common Values**: 
  - PL 8 = Masked Adventurers (street-level heroes)
  - PL 10 = Standard Superheroes (default, recommended)
  - PL 12 = Big Leagues (experienced heroes)
  - PL 14+ = World-Protectors (cosmic-level)
- **Immutability**: Rarely changed after creation (represents character tier)

**Starting Power Points Budget**:
- **Formula**: `PL × 15 = Starting Power Points`
- **Examples**:
  - PL 8 = 120 points
  - PL 10 = 150 points  
  - PL 12 = 180 points
  - PL 14 = 210 points
- **Single Pool**: All trait categories (abilities, skills, advantages, powers, defenses) draw from same pool

**Power Level Caps** (6 types):
1. **Skill Modifier Cap**: `(Ability rank + Skill rank + Advantages) ≤ PL + 10`
2. **Attack & Effect Cap**: `(Attack bonus + Effect rank) ≤ PL × 2`
3. **Dodge & Toughness Cap**: `(Dodge + Toughness) ≤ PL × 2`
4. **Parry & Toughness Cap**: `(Parry + Toughness) ≤ PL × 2`
5. **Fortitude & Will Cap**: `(Fortitude + Will) ≤ PL × 2`
6. **Non-attack Effect Cap**: `Effect rank ≤ PL` (for effects without attack check)

### Domain Behaviors

**Calculate Starting Points**:
- Apply formula: `PL × 15`
- Store result as character's point budget
- Display immediately upon selection

**Calculate Caps**:
- Derive all 6 cap values from selected PL
- Present in summary format
- Update if PL changes

**Store Foundation**:
- Persist PL as character's immutable foundation
- Enable dependent trait configuration
- Mark character as having foundation established

### Domain Rules

1. **Point Budget Formula**: `Starting Points = PL × 15` (Handbook page 26, table)
2. **Cap Trade-offs**: Paired traits allow flexibility (high attack/low damage OR high damage/low attack)
3. **Immutability**: PL represents character tier, rarely changes post-creation
4. **Validation Philosophy**: Caps are warnings, not blocks ("warn don't prevent")
5. **PL Range**: Typically 1-20, with 8/10/12/14 as common breakpoints

---

## Stories and Acceptance Criteria

### 📝 Story 1: System displays power level options

**Story Description**: System displays power level options - PL 8, 10, 12, 14 in dropdown

#### Acceptance Criteria

**Display Options**:
- When character creation screen loads, then system displays power level dropdown with options (PL 8, 10, 12, 14, 16, 18, 20)
- When dropdown opened, then system displays each PL with description (e.g., "PL 10 - Standard Heroes")
- When no PL selected yet, then system shows placeholder "Select Power Level"

**Option Details**:
- When each PL option displayed, then system shows starting points (e.g., "PL 10 - 150 points")
- When user hovers over PL option, then system displays tooltip with archetype description
- When options rendered, then system highlights PL 10 as recommended default

---

### 📝 Story 2: User selects power level

**Story Description**: User selects power level - and system calculates starting power points (PL × 15)

#### Acceptance Criteria

**Selection**:
- When user selects PL from dropdown, then system captures selected PL value
- When PL selected, then system calculates starting power points using formula (PL × 15)
- When calculation completes, then system stores PL and starting points with character

**Calculation Examples**:
- When PL 8 selected, then system calculates 120 starting points
- When PL 10 selected, then system calculates 150 starting points
- When PL 12 selected, then system calculates 180 starting points
- When PL 14 selected, then system calculates 210 starting points

**State Update**:
- When PL stored, then system marks character foundation as established
- When PL changes (if user re-selects), then system recalculates all dependent values (caps, validations)

---

### 📝 Story 3: System displays point budget

**Story Description**: System displays point budget - showing total available points

#### Acceptance Criteria

**Budget Display**:
- When starting points calculated, then system displays total budget prominently (e.g., "0 / 150 points")
- When budget displayed, then system shows format "spent / total" with progress indicator
- When character creation begins, then budget shows "0 / [total]" (nothing spent yet)

**Budget Updates**:
- When any trait purchased, then system updates spent points in real-time
- When spent points change, then system recalculates remaining points (total - spent)
- When spent exceeds total, then system displays overspend in warning color (but allows)

**Visual Formatting**:
- When budget rendered, then system uses progress bar or fraction display
- When under budget, then system displays remaining in normal color
- When over budget, then system displays overspend amount in warning color

---

### 📝 Story 4: System displays power level caps summary

**Story Description**: System displays power level caps summary - 6 cap types: skill mod, attack+effect, 3 defense pairs

#### Acceptance Criteria

**Caps Display**:
- When PL selected, then system calculates and displays all 6 PL cap formulas:
  1. Skill Modifier ≤ PL + 10
  2. Attack + Effect ≤ PL × 2
  3. Dodge + Toughness ≤ PL × 2
  4. Parry + Toughness ≤ PL × 2
  5. Fortitude + Will ≤ PL × 2
- When caps displayed, then system shows calculated values with formulas (e.g., "Skill Modifier ≤ 20 (PL 10 + 10)")
- When user views caps, then system displays in organized summary section (reference panel)

**Caps Examples for PL 10**:
- When PL 10 selected, then skill modifier cap = 20
- When PL 10 selected, then attack + effect cap = 20
- When PL 10 selected, then each defense pair cap = 20

**Caps Updates**:
- When PL changes, then system recalculates all 6 cap values
- When caps recalculated, then system updates display immediately
- When any trait approaches cap, then system highlights relevant cap formula

---

### 📝 Story 5: System stores selected power level

**Story Description**: System stores selected power level - as character foundation

#### Acceptance Criteria

**Storage**:
- When PL selected and validated, then system stores PL value with character
- When PL stored, then system marks character as having foundation (status indicator)
- When character saved, then PL included in persisted character data

**Foundation Established**:
- When PL stored, then system enables ability configuration section (previously disabled)
- When PL stored, then system enables defense calculation
- When PL stored, then system displays "Foundation Established ✓" status

**Retrieval**:
- When character loaded from storage, then system retrieves stored PL value
- When PL retrieved, then system recalculates starting points (PL × 15) and all 6 caps
- When PL restoration completes, then system validates PL is valid value (range 1-20)

---

## Consolidation Decisions

**Why 5 stories**:
- **Story 1**: Display options (UI presentation) - separate from user interaction
- **Story 2**: User selection + calculation - atomic interaction (select → calculate → store)
- **Story 3**: Budget display - ongoing concern (updates as traits purchased throughout creation)
- **Story 4**: Caps display - reference information panel (needed throughout creation)
- **Story 5**: Storage + foundation state - persistence concern (different from display/calculation)

**AC Consolidation**:
- All PL values use identical calculation formula (consolidated: `PL × 15`)
- All 6 caps calculated from same PL input (consolidated: use PL as parameter)
- Display, calculation, and storage are separate concerns (not consolidated)

---

## Domain Rules Referenced

**From M&M 3E Handbook** (Chapter 2, Pages 24-27):
- **Starting Power Points Table** (page 26): Shows PL 1-20 with point values
- **Point Budget Formula** (page 26): `PL × 15 = Starting Points`
- **Power Level Limits** (pages 26-27): All 6 cap formulas with paired traits
- **Trade-offs** (page 27): Paired traits allow flexibility (balance attack/effect, defense/toughness, etc.)
- **Power Level Tiers** (pages 24-25): Descriptions of PL 8, 10, 12, 14 archetypes

**Key Insights from Handbook**:
- Single point pool shared across ALL trait categories (not separate budgets)
- Caps enforce balance while allowing trade-offs within pairs
- PL represents "tier" of play (street-level vs world-protector vs cosmic)
- Most campaigns use PL 10 as standard starting point

**Formulas**:
```
Starting Points = PL × 15
Skill Cap = PL + 10
Attack+Effect Cap = PL × 2  
Defense Pair Caps = PL × 2 (three pairs)
```

---

## Source Material

**Referenced During Exploration**:
- `demo/mm3e/docs/mm3e-handbook-reference.txt` - Chapter 2, pages 24-27 (Power Points and Power Level)
- `demo/mm3e/docs/mm3e-domain-concepts.md` - Power Level System section
- Handbook table (page 26) - Starting Power Points by PL
- Handbook examples (pages 51-54) - The Rook (PL 10), Princess (PL 10) character creation





