# 📝 User sets ability rank for any of 8 abilities

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [⚙️ Feature Overview](./%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Configure Abilities  
**Status:** Scenarios Complete

---

## Story Description

User sets ability rank for any of 8 abilities - and system calculates point cost (rank × 2)

---

## Acceptance Criteria Reference

**Source**: Configure Abilities - Feature Overview.md

### Covered Acceptance Criteria:
- **Set Rank**: User can set rank for any of 8 abilities (STR, STA, AGL, DEX, FGT, INT, AWE, PRE)
- **Cost Calculation**: System calculates cost using formula: Cost = Rank × 2
- **Immediate Application**: System deducts/adds points to budget immediately
- **Storage**: System stores new rank value with character

---

## Background

**Given** character is being created  
**And** Power Level 10 is selected (150 starting points)  
**And** abilities configuration screen is displayed  
**And** all 8 abilities are at rank 0 (average/default)

---

## Scenarios

### Scenario 1: Set positive ability rank

**Purpose**: User increases ability from default to positive rank

**When** user sets Strength rank to 5  
**Then** system calculates cost as 10 points (5 × 2)  
**And** system deducts 10 points from remaining budget  
**And** system displays Strength rank as 5  
**And** system stores Strength rank value with character  
**And** remaining budget shows "10 / 150 points spent"

**Acceptance Criteria Covered**: Set Rank, Cost Calculation, Immediate Application, Storage

---

### Scenario 2: Set ability rank to zero

**Purpose**: Ability at average level has zero cost

**When** user sets Intellect rank to 0  
**Then** system calculates cost as 0 points (0 × 2)  
**And** system does not deduct any points from budget  
**And** system displays Intellect as "0 (Average)"  
**And** remaining budget remains unchanged

**Acceptance Criteria Covered**: Cost Calculation, Immediate Application

---

### Scenario 3: Set negative ability rank (below average)

**Purpose**: User sets ability below average, receiving point refund

**When** user sets Dexterity rank to -2  
**Then** system calculates cost as -4 points (-2 × 2)  
**And** system adds 4 points to remaining budget (refund)  
**And** system displays Dexterity rank as "-2" in warning style  
**And** remaining budget increases by 4 points

**Acceptance Criteria Covered**: Set Rank, Cost Calculation, Immediate Application

---

### Scenario 4: Change existing ability rank (increase)

**Purpose**: User modifies previously set ability rank upward

**Given** Agility is already set to rank 3 (6 points spent)  
**And** 6 points have been deducted from budget  
**When** user changes Agility rank from 3 to 8  
**Then** system recalculates cost as 16 points (8 × 2)  
**And** system deducts additional 10 points from budget (16 total - 6 previous)  
**And** system updates Agility display to rank 8  
**And** remaining budget reflects new total spent

**Acceptance Criteria Covered**: Set Rank, Cost Calculation, Immediate Application

---

### Scenario 5: Change existing ability rank (decrease)

**Purpose**: User reduces previously set ability rank, receiving partial refund

**Given** Fighting is already set to rank 10 (20 points spent)  
**And** 20 points have been deducted from budget  
**When** user changes Fighting rank from 10 to 6  
**Then** system recalculates cost as 12 points (6 × 2)  
**And** system refunds 8 points to budget (20 previous - 12 new)  
**And** system updates Fighting display to rank 6  
**And** remaining budget increases by 8 points

**Acceptance Criteria Covered**: Set Rank, Cost Calculation, Immediate Application

---

### Scenario 6: Set ability to minimum rank

**Purpose**: Test boundary condition at minimum ability rank

**When** user sets Presence rank to -5  
**Then** system calculates cost as -10 points (-5 × 2)  
**And** system adds 10 points to remaining budget  
**And** system displays Presence as "-5 (Far Below Average)" in warning style  
**And** system allows setting minimum rank

**Acceptance Criteria Covered**: Set Rank, Cost Calculation, Boundary Condition

---

### Scenario 7: Set ability to maximum rank

**Purpose**: Test boundary condition at maximum ability rank

**When** user sets Stamina rank to 20  
**Then** system calculates cost as 40 points (20 × 2)  
**And** system deducts 40 points from remaining budget  
**And** system displays Stamina as "20 (Cosmic-level)"  
**And** system allows setting maximum rank

**Acceptance Criteria Covered**: Set Rank, Cost Calculation, Boundary Condition

---

## Scenario Outline: Set ability rank for all 8 abilities

**Purpose**: Verify cost formula works identically for all 8 abilities

**Given** character abilities are all at rank 0  
**When** user sets <ability> rank to <rank>  
**Then** system calculates cost as <cost> points (<rank> × 2)  
**And** system deducts <cost> points from remaining budget  
**And** system displays <ability> rank as <rank>  
**And** remaining budget shows "<cost> / 150 points spent"

**Examples**:

| ability    | rank | cost | description                           |
|------------|------|------|---------------------------------------|
| STR        | 5    | 10   | Strength - physical power             |
| STA        | 8    | 16   | Stamina - endurance (affects 2 defenses) |
| AGL        | 6    | 12   | Agility - balance (affects Dodge)     |
| DEX        | 4    | 8    | Dexterity - accuracy                  |
| FGT        | 7    | 14   | Fighting - combat (affects Parry)     |
| INT        | 3    | 6    | Intellect - reasoning                 |
| AWE        | 5    | 10   | Awareness - perception (affects Will) |
| PRE        | 6    | 12   | Presence - charisma                   |

**Acceptance Criteria Covered**: Set Rank for all 8 abilities, Cost Calculation formula consistency

---

## Scenario Outline: Ability rank cost formula validation

**Purpose**: Validate cost calculation formula across full rank range

**Given** ability is at rank 0  
**When** user sets ability rank to <rank>  
**Then** system calculates cost as <cost> points  
**And** budget calculation is <cost> = <rank> × 2

**Examples**:

| rank | cost | calculation | scenario           |
|------|------|-------------|-------------------|
| -5   | -10  | -5 × 2      | Min rank (refund) |
| -2   | -4   | -2 × 2      | Below average     |
| 0    | 0    | 0 × 2       | Average (free)    |
| 1    | 2    | 1 × 2       | Above average     |
| 3    | 6    | 3 × 2       | Exceptional       |
| 5    | 10   | 5 × 2       | Peak human        |
| 8    | 16   | 8 × 2       | Low superhuman    |
| 10   | 20   | 10 × 2      | PL 10 typical     |
| 15   | 30   | 15 × 2      | High superhuman   |
| 20   | 40   | 20 × 2      | Max rank (cosmic) |

**Acceptance Criteria Covered**: Cost Calculation formula, Edge cases (min/max), Negative ranks, Zero rank

---

## Source Material

**Inherited From**: Story Map → Configure Abilities Feature Overview

**Referenced During Specification**:
- M&M 3E Handbook, Page 26: "Ability: 2 per ability rank" (cost formula)
- M&M 3E Handbook, Pages 107-112: Ability descriptions and rank scale
- M&M 3E Handbook, Page 108: Rank scale from -5 (far below average) to 20 (cosmic)
- Domain Concepts Document: The 8 Abilities table with abbreviations

**Formula Confirmed**: Cost = Rank × 2 power points





