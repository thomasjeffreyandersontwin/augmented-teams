# 📝 System calculates total ability points spent

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [⚙️ Feature Overview](./%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Configure Abilities  
**Status:** Scenarios Complete

---

## Story Description

System calculates total ability points spent - sum of all ability costs

---

## Acceptance Criteria Reference

**Source**: Configure Abilities - Feature Overview.md

### Covered Acceptance Criteria:
- **Calculate Total**: System recalculates total when any ability changes using Σ(rank × 2) for all 8
- **Calculation Examples**: Various ability combinations with correct totals
- **Display Format**: Shows total in abilities section header with breakdown

---

## Background

**Given** character is being created  
**And** Power Level 10 is selected (150 starting points)  
**And** abilities configuration screen is displayed

---

## Scenarios

### Scenario 1: Calculate total with all abilities at zero

**Purpose**: Default state has zero total cost

**Given** all 8 abilities are at rank 0  
**When** system calculates total ability points  
**Then** total equals 0 points  
**And** system displays "Ability Points: 0 / 150"  
**And** no points are deducted from budget

**Acceptance Criteria Covered**: Calculate Total, Zero baseline

---

### Scenario 2: Calculate total with single ability set

**Purpose**: Single ability cost contributes to total

**Given** all abilities are at rank 0  
**And** Strength is set to rank 5  
**When** system calculates total ability points  
**Then** total equals 10 points (5 × 2)  
**And** system displays "Ability Points: 10 / 150"  
**And** calculation shows: STR: 10pp, Total: 10pp

**Acceptance Criteria Covered**: Calculate Total, Display Format

---

### Scenario 3: Calculate total with multiple abilities set

**Purpose**: Multiple ability costs are summed correctly

**Given** Strength is set to rank 5 (10 pp)  
**And** Stamina is set to rank 3 (6 pp)  
**And** all other abilities are at rank 0  
**When** system calculates total ability points  
**Then** total equals 16 points (10 + 6)  
**And** system displays "Ability Points: 16 / 150"  
**And** breakdown shows: "STR: 10pp, STA: 6pp, Total: 16pp"

**Acceptance Criteria Covered**: Calculate Total, Calculation Examples, Display Format

---

### Scenario 4: Calculate total with all abilities at same rank

**Purpose**: Symmetrical build calculates correctly

**Given** all 8 abilities are set to rank 2  
**When** system calculates total ability points  
**Then** total equals 32 points (8 abilities × 2 ranks × 2 pp/rank)  
**And** system displays "Ability Points: 32 / 150"  
**And** each ability contributes 4 pp to total

**Acceptance Criteria Covered**: Calculate Total, Calculation Examples

---

### Scenario 5: Calculate total with negative rank (refund)

**Purpose**: Negative ranks reduce total (refund points)

**Given** Strength is set to rank 5 (10 pp)  
**And** Dexterity is set to rank -2 (-4 pp)  
**And** all other abilities are at rank 0  
**When** system calculates total ability points  
**Then** total equals 6 points (10 + (-4))  
**And** system displays "Ability Points: 6 / 150"  
**And** breakdown shows: "STR: 10pp, DEX: -4pp, Total: 6pp"

**Acceptance Criteria Covered**: Calculate Total, Calculation Examples with negative ranks

---

### Scenario 6: Recalculate total when ability changes

**Purpose**: Total updates in real-time when abilities modified

**Given** STR=5 (10pp), STA=3 (6pp), total=16pp  
**When** user changes Agility from 0 to 4  
**Then** system recalculates total immediately  
**And** new total equals 24 points (10 + 6 + 8)  
**And** system displays "Ability Points: 24 / 150"  
**And** total updates within 100ms

**Acceptance Criteria Covered**: Calculate Total, Real-time recalculation

---

### Scenario 7: Display total with breakdown

**Purpose**: User can see how total is distributed across abilities

**Given** STR=6 (12pp), FGT=8 (16pp), AWE=5 (10pp)  
**When** system displays total  
**Then** abilities section shows total as "Ability Points: 38 / 150"  
**And** breakdown displays:  
**And** "STR: 12pp"  
**And** "FGT: 16pp"  
**And** "AWE: 10pp"  
**And** "Others: 0pp"  
**And** "Total: 38pp"

**Acceptance Criteria Covered**: Display Format

---

## Scenario Outline: Calculate total for various ability combinations

**Purpose**: Verify total calculation formula across different character builds

**Given** abilities are configured with specified ranks  
**When** system calculates total ability points  
**Then** total equals <total> points

**Examples**:

| STR | STA | AGL | DEX | FGT | INT | AWE | PRE | calculation                     | total | build type    |
|-----|-----|-----|-----|-----|-----|-----|-----|---------------------------------|-------|---------------|
| 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0                               | 0     | All default   |
| 5   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 5×2                             | 10    | Single ability|
| 5   | 3   | 0   | 0   | 0   | 0   | 0   | 0   | (5×2)+(3×2)                     | 16    | Two abilities |
| 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 8×(2×2)                         | 32    | All equal     |
| 10  | 8   | 6   | 4   | 8   | 2   | 4   | 4   | (10+8+6+4+8+2+4+4)×2            | 92    | Physical hero |
| 2   | 4   | 4   | 3   | 3   | 8   | 10  | 6   | (2+4+4+3+3+8+10+6)×2            | 80    | Mental hero   |
| -2  | 0   | 0   | -1  | 0   | 0   | 0   | 0   | (-2×2)+(-1×2)                   | -6    | Below average |
| 12  | 12  | 2   | 0   | 6   | 0   | 2   | 4   | (12+12+2+0+6+0+2+4)×2           | 76    | Powerhouse    |
| 20  | 20  | 20  | 20  | 20  | 20  | 20  | 20  | 8×(20×2)                        | 320   | Maximum ranks |

**Acceptance Criteria Covered**: Calculate Total, Calculation Examples, Formula validation

---

## Scenario Outline: Verify aggregation formula

**Purpose**: Validate total = Σ(rank × 2) for all 8 abilities

**Given** abilities have the specified ranks  
**When** system calculates total  
**Then** total equals sum of (rank × 2) for each ability  
**And** formula verification: <str_cost> + <sta_cost> + <agl_cost> + <dex_cost> + <fgt_cost> + <int_cost> + <awe_cost> + <pre_cost> = <total>

**Examples**:

| str | sta | agl | dex | fgt | int | awe | pre | str_cost | sta_cost | agl_cost | dex_cost | fgt_cost | int_cost | awe_cost | pre_cost | total |
|-----|-----|-----|-----|-----|-----|-----|-----|----------|----------|----------|----------|----------|----------|----------|----------|-------|
| 5   | 3   | 0   | 0   | 0   | 0   | 0   | 0   | 10       | 6        | 0        | 0        | 0        | 0        | 0        | 0        | 16    |
| 8   | 6   | 4   | 3   | 7   | 2   | 5   | 3   | 16       | 12       | 8        | 6        | 14       | 4        | 10       | 6        | 76    |
| 10  | 10  | 10  | 10  | 10  | 10  | 10  | 10  | 20       | 20       | 20       | 20       | 20       | 20       | 20       | 20       | 160   |

**Acceptance Criteria Covered**: Calculate Total formula (Σ(rank × 2)), Detailed calculation breakdown

---

## Source Material

**Inherited From**: Story Map → Configure Abilities Feature Overview

**Referenced During Specification**:
- M&M 3E Handbook, Page 26: Basic Trait Costs table - "Ability: 2 per ability rank"
- Domain Concepts Document: Total Ability Cost formula: `Total = Σ(rank × 2)` for all 8 abilities
- Feature Overview: Calculation Examples section with concrete test cases
- Formula confirmed: Total Ability Points = sum of (ability_rank × 2) for STR, STA, AGL, DEX, FGT, INT, AWE, PRE





