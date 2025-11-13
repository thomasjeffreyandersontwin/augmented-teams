# ⚙️ Purchase Defense Ranks - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Purchase Defense Ranks  
**Stories:** 1 story

---

## Feature Purpose

Enable user to purchase additional ranks for 4 defenses (Dodge, Parry, Fortitude, Will) to increase defense values beyond ability-derived bases, while preventing Toughness rank purchases per M&M 3E rules. This allows characters to be more defensive without increasing abilities.

---

## Domain AC (Feature Level)

### Shared Concepts (from Higher Levels)
- **The 5 Defenses**: Dodge, Parry, Fortitude, Will, Toughness (from Calculate Defenses feature)
- **Power Points**: Currency for purchasing
- **Point Budget**: Total available points

### Feature-Specific Domain Concepts

**Purchased Defense Ranks** (feature-scoped):
- **Definition**: Additional ranks bought with power points, added to ability-derived base
- **Cost**: 1 power point per rank (Handbook page 26)
- **Purchasable Defenses**: Dodge, Parry, Fortitude, Will (4 of 5)
- **Non-Purchasable**: Toughness (special rule - only via advantages/powers)

**Defense Total Value** (feature-scoped):
- **Formula**: `Total Defense = Base (from ability) + Purchased Ranks`
- **Examples**:
  - Dodge = (10 + Agility) + purchased ranks
  - Fortitude = Stamina + purchased ranks
  - Toughness = Stamina (no purchased ranks allowed)

**Toughness Exception Rule** (feature-scoped):
- Toughness CANNOT be purchased with power points
- Only improved via:
  - **Advantages**: Defensive Roll, Protection
  - **Powers**: Protection effect, Enhanced Stamina
- Rationale: Game balance (Toughness too powerful if directly purchasable)

### Domain Behaviors

**Purchase Ranks**:
- User selects defense to improve
- User specifies number of ranks to add
- System calculates cost (1 pp per rank)
- System adds ranks to base value
- System deducts cost from budget

**Validate Purchase**:
- Check defense is purchasable (not Toughness)
- Check sufficient points in budget
- If Toughness selected, prevent and explain
- If insufficient points, warn but allow (overspend)

**Calculate Total Defense**:
- Add purchased ranks to ability-derived base
- Display new total defense value
- Update character sheet

### Domain Rules

1. **Defense Rank Cost**: 1 power point per rank (Handbook page 26, Basic Trait Costs table)
2. **Total Defense Formula**: `Total = Base + Purchased Ranks`
   - Dodge Total = (10 + Agility) + purchased
   - Parry Total = (10 + Fighting) + purchased
   - Fortitude Total = Stamina + purchased
   - Will Total = Awareness + purchased
   - Toughness Total = Stamina (no purchased ranks)
3. **Toughness Purchase Prohibition**: "Toughness can only be improved using advantages and powers, and his hero doesn't have any powers" (Handbook page 52, The Rook example)
4. **No Maximum**: Can purchase unlimited ranks (subject to PL caps and point budget)
5. **Warn Don't Prevent**: Overspending points warns but doesn't block

---

## Stories and Acceptance Criteria

### 📝 Story 1: User purchases additional defense ranks

**Story Description**: User purchases additional defense ranks - and system adds to base value (Dodge, Parry, Fortitude, Will only), deducts cost (1 pp/rank), prevents Toughness purchase

#### Acceptance Criteria

**Purchase Dodge Ranks**:
- When user purchases Dodge rank, then system adds 1 to Dodge value and deducts 1 point from budget
- When Dodge base = 15 and user purchases 2 ranks, then Dodge total = 17
- When Dodge rank purchased, then system displays "Dodge: 17 (10 + Agilit 5 + 2 purchased)"

**Purchase Parry Ranks**:
- When user purchases Parry rank, then system adds 1 to Parry value and deducts 1 point from budget
- When Parry base = 18 and user purchases 1 rank, then Parry total = 19
- When Parry rank purchased, then system displays "Parry: 19 (10 + Fighting 8 + 1 purchased)"

**Purchase Fortitude Ranks**:
- When user purchases Fortitude rank, then system adds 1 to Fortitude value and deducts 1 point from budget
- When Fortitude base = 3 and user purchases 5 ranks, then Fortitude total = 8
- When Fortitude rank purchased, then system displays "Fortitude: 8 (Stamina 3 + 5 purchased)"

**Purchase Will Ranks**:
- When user purchases Will rank, then system adds 1 to Will value and deducts 1 point from budget
- When Will base = 2 and user purchases 6 ranks, then Will total = 8
- When Will rank purchased, then system displays "Will: 8 (Awareness 2 + 6 purchased)"

**Toughness Purchase Prevention**:
- When user attempts to purchase Toughness rank, then system prevents purchase and displays message
- When Toughness selected, then system shows "Cannot purchase Toughness ranks. Use advantages (Defensive Roll) or powers (Protection) instead."
- When Toughness displayed, then system shows "No purchase available" indicator

**Cost Deduction**:
- When any defense rank purchased, then system deducts 1 point from remaining budget per rank
- When multiple ranks purchased, then system deducts total cost (ranks × 1 pp)
- When budget insufficient but purchase allowed, then system shows overspend warning

**Decrease Ranks**:
- When user decreases purchased defense ranks, then system refunds 1 point per rank to budget
- When all purchased ranks removed, then defense returns to base value only
- When ranks decreased, then system updates defense display and budget immediately

---

## Consolidation Decisions

**Why 1 story (not 4 for each purchasable defense, not 5 for all defenses)**:
- **Consolidated**: All 4 purchasable defenses (Dodge, Parry, Fortitude, Will) use identical logic:
  - Cost: 1 pp per rank
  - Operation: Add rank to base
  - Budget impact: Deduct cost
- **Included**: Toughness prevention is validation rule (not separate story), included in same story
- **Rationale**: Same logic, different data (which defense) → ONE story

**Why NOT separate stories**:
- Purchase operation identical for all 4 purchasable defenses
- Cost calculation identical (1 pp/rank)
- Budget deduction identical
- Only difference is WHICH defense and WHICH base formula (but base already calculated by previous feature)
- Toughness prevention is edge case validation (part of same purchase flow)

**AC Structure**:
- Enumerate all 4 purchasable defenses explicitly (show examples for each)
- Include Toughness prevention as validation within same story
- Show calculation breakdown for each defense type

---

## Domain Rules Referenced

**From M&M 3E Handbook**:
- Page 26, Basic Trait Costs: "Defense: 1 per defense rank"
- Page 111: "Toughness can only be improved using advantages and powers" (cannot purchase directly)
- Character creation example - The Rook (page 52): Purchases Dodge (+9 ranks), Parry (+6 ranks), Will (+6 ranks), Fortitude (+5 ranks)
- Character creation example - Princess (page 54): Purchases Dodge, Parry, Will to reach PL caps

**From Domain Concepts Document**:
- The 5 Defenses table - shows which can be purchased
- "Toughness: NO - Only via Advantages/Powers"

**Key Insights**:
- All defenses except Toughness can be purchased
- Common pattern: Buy defenses to reach PL caps (Dodge+Toughness ≤ PL×2, etc.)
- Toughness improved through Defensive Roll advantage or Protection powers
- Defense purchases independent of ability values

**Formula**:
```
Defense Total = Base (from ability) + Purchased Ranks
Cost = Purchased Ranks × 1 pp
```

---

## Source Material

**Referenced During Exploration**:
- Handbook page 26 - Defense cost (1 pp/rank)
- Handbook pages 110-111 - Defense descriptions
- Handbook pages 51-54 - Character examples showing defense purchases
- Domain concepts - Toughness special rule





