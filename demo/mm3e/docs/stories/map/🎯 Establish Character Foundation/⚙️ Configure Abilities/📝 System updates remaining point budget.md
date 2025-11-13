# 📝 System updates remaining point budget

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [⚙️ Feature Overview](./%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Configure Abilities  
**Status:** Scenarios Complete

---

## Story Description

System updates remaining point budget - total points - spent points

---

## Acceptance Criteria Reference

**Source**: Configure Abilities - Feature Overview.md

### Covered Acceptance Criteria:
- **Budget Calculation**: Remaining = Total - Spent (across all categories)
- **Budget Display**: Shows "Spent / Total" format with color coding
- **Overspend Warning**: Allows continuing when spent > total (warn, don't prevent)
- **Real-time Updates**: Budget updates immediately (<100ms) when abilities change

---

## Background

**Given** character is being created  
**And** Power Level 10 is selected (150 total points)  
**And** abilities configuration screen is displayed

---

## Scenarios

### Scenario 1: Display initial budget with no points spent

**Purpose**: Starting budget shows all points available

**Given** no abilities have been configured (all at rank 0)  
**When** budget display is rendered  
**Then** system shows "0 / 150 points spent"  
**And** remaining budget is 150 points  
**And** budget is displayed in normal color  
**And** progress bar shows 0% filled

**Acceptance Criteria Covered**: Budget Display, Initial state

---

### Scenario 2: Update budget when ability points spent

**Purpose**: Budget decreases as ability points are allocated

**Given** budget shows "0 / 150"  
**When** user sets Strength to rank 5 (10 points)  
**Then** system recalculates remaining budget  
**And** budget updates to "10 / 150 points spent"  
**And** remaining budget is 140 points  
**And** budget is displayed in normal color  
**And** progress bar shows 7% filled (10/150)

**Acceptance Criteria Covered**: Budget Calculation, Budget Display, Real-time Updates

---

### Scenario 3: Update budget in real-time with multiple changes

**Purpose**: Budget reflects each change immediately

**Given** budget shows "10 / 150" (STR=5)  
**When** user sets Agility to rank 4 (8 points)  
**Then** budget immediately updates to "18 / 150 points spent"  
**And** update occurs within 100ms  
**When** user sets Intellect to rank 6 (12 points)  
**Then** budget immediately updates to "30 / 150 points spent"  
**And** update occurs within 100ms

**Acceptance Criteria Covered**: Real-time Updates, Multiple changes

---

### Scenario 4: Update budget when points refunded (negative rank)

**Purpose**: Budget increases when ability set below average

**Given** budget shows "20 / 150" (STR=10)  
**When** user sets Dexterity to rank -2 (-4 points refund)  
**Then** system recalculates budget with refund  
**And** budget updates to "16 / 150 points spent"  
**And** remaining budget increases to 134 points

**Acceptance Criteria Covered**: Budget Calculation with negative ranks

---

### Scenario 5: Display budget at fully used (zero remaining)

**Purpose**: Budget shows "fully used" when all points allocated

**Given** total spent equals 150 points  
**When** budget display is rendered  
**Then** system shows "150 / 150 points spent"  
**And** remaining budget is 0 points  
**And** budget displays "Budget Fully Used" indicator  
**And** progress bar shows 100% filled  
**And** no warning color (this is valid state)

**Acceptance Criteria Covered**: Budget Display, Zero remaining

---

### Scenario 6: Display overspend warning

**Purpose**: User can overspend with warning (warn, don't prevent philosophy)

**Given** budget shows "150 / 150" (fully used)  
**When** user sets Presence to rank 3 (6 more points)  
**Then** system allows the change  
**And** budget updates to "156 / 150 points spent"  
**And** remaining budget shows -6 points  
**And** system displays "Over Budget by 6 points" in warning color  
**And** progress bar shows 104% filled (overfilled)  
**But** system does NOT prevent saving character

**Acceptance Criteria Covered**: Overspend Warning, Warn don't prevent philosophy

---

### Scenario 7: Display budget with progress bar visualization

**Purpose**: Visual progress bar helps user see budget usage at a glance

**Given** budget shows "75 / 150 points spent"  
**When** budget display is rendered  
**Then** system displays progress bar showing 50% filled  
**And** filled portion is in normal color  
**And** unfilled portion shows remaining capacity  
**And** current/total numbers displayed alongside bar

**Acceptance Criteria Covered**: Budget Display with visual progress

---

## Scenario Outline: Budget calculation across spending levels

**Purpose**: Verify budget formula (Total - Spent = Remaining) across range

**Given** Power Level 10 provides 150 total points  
**And** abilities cost <spent> points  
**When** system calculates remaining budget  
**Then** remaining equals <remaining> points  
**And** budget displays as "<spent> / 150 points spent"  
**And** budget color is <color>

**Examples**:

| spent | remaining | percentage | color   | state                |
|-------|-----------|------------|---------|----------------------|
| 0     | 150       | 0%         | normal  | No points used       |
| 30    | 120       | 20%        | normal  | Light usage          |
| 75    | 75        | 50%        | normal  | Half used            |
| 120   | 30        | 80%        | normal  | Mostly used          |
| 145   | 5         | 97%        | normal  | Nearly full          |
| 150   | 0         | 100%       | normal  | Fully used (valid)   |
| 156   | -6        | 104%       | warning | 6 points overspent   |
| 170   | -20       | 113%       | warning | 20 points overspent  |

**Acceptance Criteria Covered**: Budget Calculation, Budget Display, Color coding, Overspend handling

---

## Scenario Outline: Real-time budget updates

**Purpose**: Verify budget updates immediately when abilities change

**Given** budget shows "<initial_spent> / 150"  
**When** user changes ability from rank <old_rank> to <new_rank>  
**Then** cost changes by <cost_delta> points  
**And** budget immediately updates to "<new_spent> / 150"  
**And** update occurs within 100ms

**Examples**:

| initial_spent | old_rank | new_rank | cost_delta | new_spent | scenario             |
|---------------|----------|----------|------------|-----------|----------------------|
| 0             | 0        | 5        | +10        | 10        | First ability set    |
| 10            | 5        | 8        | +6         | 16        | Increase existing    |
| 16            | 8        | 3        | -10        | 6         | Decrease existing    |
| 6             | 3        | 0        | -6         | 0         | Reset to average     |
| 0             | 0        | -2       | -4         | -4        | Set below average    |
| 150           | 0        | 3        | +6         | 156       | Overspend            |

**Acceptance Criteria Covered**: Real-time Updates, Budget recalculation on changes

---

## Scenario Outline: Multi-category budget tracking

**Purpose**: Budget tracks spending across all categories (abilities shown here)

**Given** Power Level 10 provides 150 total points  
**And** ability points spent = <ability_cost>  
**And** other category points spent = <other_cost>  
**When** system calculates remaining budget  
**Then** total spent = <total_spent>  
**And** remaining = 150 - <total_spent>  
**And** budget displays "<total_spent> / 150 points spent"

**Examples**:

| ability_cost | other_cost | total_spent | remaining | scenario                    |
|--------------|------------|-------------|-----------|----------------------------|
| 40           | 0          | 40          | 110       | Only abilities configured  |
| 40           | 20         | 60          | 90        | Abilities + skills         |
| 40           | 50         | 90          | 60        | Abilities + skills + adv   |
| 40           | 110        | 150         | 0         | Fully allocated            |
| 40           | 120        | 160         | -10       | Overspent by 10            |

**Acceptance Criteria Covered**: Budget Calculation across categories, Total tracking

---

## Source Material

**Inherited From**: Story Map → Configure Abilities Feature Overview

**Referenced During Specification**:
- M&M 3E Handbook, Page 26: Power Level limits table - PL 10 = 150 starting points
- Domain Concepts Document: Point Budget formula: `Remaining = Total - Spent`
- Domain Concepts Document: "Warn, Don't Prevent" validation philosophy
- Feature Overview: Budget calculation and overspend handling rules
- Formula: Remaining Budget = Total Points - Spent Points (across ALL categories)





