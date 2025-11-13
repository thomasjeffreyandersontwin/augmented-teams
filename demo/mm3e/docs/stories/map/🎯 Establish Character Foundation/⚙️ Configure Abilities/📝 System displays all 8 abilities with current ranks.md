# 📝 System displays all 8 abilities with current ranks

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [⚙️ Feature Overview](./%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Configure Abilities  
**Status:** Scenarios Complete

---

## Story Description

System displays all 8 abilities with current ranks - STR, STA, AGL, DEX, FGT, INT, AWE, PRE

---

## Acceptance Criteria Reference

**Source**: Configure Abilities - Feature Overview.md

### Covered Acceptance Criteria:
- **Display All Abilities**: System shows all 8 abilities in standard order
- **Ability Details**: Shows abbreviation, full name, current rank, cost
- **Visual Organization**: Groups abilities logically (physical, reflexes, combat, mental)
- **Real-time Updates**: Display updates immediately when ability changes

---

## Background

**Given** character is being created  
**And** Power Level 10 is selected (150 starting points)  
**And** abilities configuration screen is displayed

---

## Scenarios

### Scenario 1: Display all 8 abilities at default ranks

**Purpose**: Initial display shows all 8 abilities at average (rank 0)

**When** abilities section renders  
**Then** system displays all 8 abilities in standard order: STR, STA, AGL, DEX, FGT, INT, AWE, PRE  
**And** each ability shows abbreviation, full name, and current rank  
**And** all abilities display rank as "0 (Average)"  
**And** all abilities display cost as "0 pp"  
**And** rank adjustment controls are displayed for each ability

**Acceptance Criteria Covered**: Display All Abilities, Ability Details

---

### Scenario 2: Display abilities grouped by category

**Purpose**: Abilities are organized into logical groups for easier navigation

**When** abilities section renders  
**Then** system organizes abilities into groups:  
**And** Physical group contains: Strength, Stamina  
**And** Reflexes group contains: Agility, Dexterity  
**And** Combat group contains: Fighting  
**And** Mental group contains: Intellect, Awareness, Presence  
**And** each group is visually distinct with header

**Acceptance Criteria Covered**: Visual Organization

---

### Scenario 3: Display ability with positive rank

**Purpose**: Ability above average shows rank and calculated cost

**Given** Strength has been set to rank 8  
**When** abilities section renders  
**Then** system displays Strength as:  
**And** abbreviation: "STR"  
**And** full name: "Strength"  
**And** rank: "8"  
**And** cost: "16 pp" (8 × 2)  
**And** rank description: "(Superhuman)"

**Acceptance Criteria Covered**: Ability Details

---

### Scenario 4: Display ability with negative rank

**Purpose**: Ability below average shows negative rank with warning styling

**Given** Dexterity has been set to rank -2  
**When** abilities section renders  
**Then** system displays Dexterity as:  
**And** abbreviation: "DEX"  
**And** full name: "Dexterity"  
**And** rank: "-2"  
**And** rank is displayed in warning color/style  
**And** cost: "-4 pp" (refund shown)  
**And** rank description: "(Below Average)"

**Acceptance Criteria Covered**: Ability Details, Warning styling for negative ranks

---

### Scenario 5: Display ability with rank zero

**Purpose**: Average ability shows zero with "Average" designation

**Given** Intellect is at rank 0  
**When** abilities section renders  
**Then** system displays Intellect as:  
**And** abbreviation: "INT"  
**And** full name: "Intellect"  
**And** rank: "0 (Average)"  
**And** cost: "0 pp"  
**And** no warning styling applied

**Acceptance Criteria Covered**: Ability Details, Zero rank handling

---

### Scenario 6: Display ability tooltip on hover

**Purpose**: User can see ability description and uses by hovering

**Given** abilities are displayed  
**When** user hovers over "Strength" name  
**Then** system displays tooltip containing:  
**And** description: "Physical power, lifting, damage"  
**And** primary use: "Athletics skill"  
**And** example: "Lifting heavy objects, breaking things"

**Acceptance Criteria Covered**: Ability Details, Tooltip functionality

---

### Scenario 7: Update display when ability changes

**Purpose**: Display updates immediately when user modifies ability rank

**Given** all abilities are displayed at rank 0  
**And** Agility is visible on screen  
**When** user changes Agility rank from 0 to 6  
**Then** system updates Agility display immediately  
**And** new rank "6" is displayed  
**And** new cost "12 pp" is displayed  
**And** update occurs within 100ms (real-time)  
**And** no page refresh required

**Acceptance Criteria Covered**: Real-time Updates

---

### Scenario 8: Display total ability points spent

**Purpose**: Summary shows aggregate points spent on all abilities

**Given** STR=5 (10pp), STA=3 (6pp), all others=0  
**When** abilities section is displayed  
**Then** system shows total ability points at bottom of section  
**And** total displays as "Ability Points: 16 / 150"  
**And** breakdown shows: "STR: 10pp, STA: 6pp, Total: 16pp"

**Acceptance Criteria Covered**: Visual Organization, Display total

---

## Scenario Outline: Display all 8 abilities with example builds

**Purpose**: Verify display works correctly for different character builds

**Given** abilities are configured according to <build>  
**When** abilities section renders  
**Then** system displays all 8 abilities with their ranks and costs  
**And** total ability points spent is <total>

**Examples**:

| build           | STR | STA | AGL | DEX | FGT | INT | AWE | PRE | total | description              |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-------|--------------------------|
| Default         | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 0     | All average              |
| Detective       | 2   | 2   | 5   | 3   | 8   | 4   | 6   | 3   | 66    | The Rook (handbook p51)  |
| Powerhouse      | 12  | 12  | 2   | 0   | 6   | 0   | 2   | 4   | 76    | Princess (handbook p54)  |
| Balanced Hero   | 4   | 4   | 4   | 4   | 4   | 4   | 4   | 4   | 64    | All abilities equal      |
| Physical Focus  | 10  | 8   | 6   | 4   | 8   | 0   | 2   | 0   | 76    | Strength-based           |
| Mental Focus    | 0   | 2   | 2   | 2   | 2   | 8   | 10  | 6   | 64    | Intelligence-based       |
| Below Average   | -2  | 0   | 0   | -1  | 0   | 0   | 0   | 0   | -6    | Some below average       |

**Acceptance Criteria Covered**: Display All Abilities, Ability Details, Example character builds from handbook

---

## Scenario Outline: Display ability rank descriptions

**Purpose**: Verify rank descriptions match handbook scale

**When** ability is set to <rank>  
**Then** system displays rank description as "<description>"

**Examples**:

| rank | description       | meaning                  |
|------|-------------------|--------------------------|
| -5   | Far Below Average | Minimum rank             |
| -2   | Below Average     | Deficient                |
| 0    | Average           | Normal human             |
| 2    | Above Average     | Better than most         |
| 4    | Exceptional       | Remarkable               |
| 6    | Peak Human        | Olympic-level            |
| 8    | Superhuman        | Beyond human limits      |
| 10   | Superhuman        | Typical PL 10 hero       |
| 15   | Superhuman        | Very powerful            |
| 20   | Cosmic-level      | Maximum rank             |

**Acceptance Criteria Covered**: Ability Details, Rank scale from handbook

---

## Source Material

**Inherited From**: Story Map → Configure Abilities Feature Overview

**Referenced During Specification**:
- M&M 3E Handbook, Pages 108-109: Ability descriptions and what each ability represents
- M&M 3E Handbook, Page 108: Rank scale descriptions (-5 to 20 with meanings)
- M&M 3E Handbook, Pages 51-54: Character examples (The Rook, Princess) used in Scenario Outline
- Domain Concepts Document: The 8 Abilities table with abbreviations and primary uses





