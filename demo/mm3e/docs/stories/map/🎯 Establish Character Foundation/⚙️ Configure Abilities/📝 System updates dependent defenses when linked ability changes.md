# 📝 System updates dependent defenses when linked ability changes

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [⚙️ Feature Overview](./%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Configure Abilities  
**Status:** Scenarios Complete

---

## Story Description

System updates dependent defenses when linked ability changes - AGL→Dodge, FGT→Parry, STA→Fortitude+Toughness, AWE→Will

---

## Acceptance Criteria Reference

**Source**: Configure Abilities - Feature Overview.md

### Covered Acceptance Criteria:
- **Agility → Dodge**: Dodge = 10 + Agility (active defense)
- **Fighting → Parry**: Parry = 10 + Fighting (active defense)
- **Stamina → Fortitude + Toughness**: Fortitude = Stamina, Toughness = Stamina (resistance defenses)
- **Awareness → Will**: Will = Awareness (resistance defense)
- **No Cascade**: STR, DEX, INT, PRE do NOT update any defenses
- **Synchronous Updates**: Defense updates occur immediately in same cycle

---

## Background

**Given** character is being created  
**And** Power Level 10 is selected  
**And** abilities configuration screen is displayed  
**And** all abilities are at rank 0 (defenses at base values)  
**And** defense values are visible on screen

---

## Scenarios

### Scenario 1: Update Dodge when Agility changes

**Purpose**: Agility directly affects Dodge defense (active defense formula)

**Given** Agility is at rank 0 (Dodge base = 10)  
**When** user sets Agility to rank 5  
**Then** system immediately recalculates Dodge as 15 (10 + 5)  
**And** Dodge display updates to show 15  
**And** defense update occurs in same cycle as ability update  
**And** user sees both Agility and Dodge change simultaneously

**Acceptance Criteria Covered**: Agility → Dodge cascade, Synchronous Updates

---

### Scenario 2: Update Parry when Fighting changes

**Purpose**: Fighting directly affects Parry defense (active defense formula)

**Given** Fighting is at rank 0 (Parry base = 10)  
**When** user sets Fighting to rank 8  
**Then** system immediately recalculates Parry as 18 (10 + 8)  
**And** Parry display updates to show 18  
**And** defense update occurs in same cycle as ability update  
**And** user sees both Fighting and Parry change simultaneously

**Acceptance Criteria Covered**: Fighting → Parry cascade, Synchronous Updates

---

### Scenario 3: Update Fortitude and Toughness when Stamina changes

**Purpose**: Stamina affects TWO defenses (resistance defense formula)

**Given** Stamina is at rank 0 (Fortitude = 0, Toughness = 0)  
**When** user sets Stamina to rank 3  
**Then** system immediately recalculates Fortitude as 3 (equals Stamina)  
**And** system immediately recalculates Toughness as 3 (equals Stamina)  
**And** Fortitude display updates to show 3  
**And** Toughness display updates to show 3  
**And** both defenses update together in same cycle  
**And** user sees Stamina, Fortitude, and Toughness all change simultaneously

**Acceptance Criteria Covered**: Stamina → Fortitude + Toughness cascade, Synchronous Updates

---

### Scenario 4: Update Will when Awareness changes

**Purpose**: Awareness directly affects Will defense (resistance defense formula)

**Given** Awareness is at rank 0 (Will = 0)  
**When** user sets Awareness to rank 2  
**Then** system immediately recalculates Will as 2 (equals Awareness)  
**And** Will display updates to show 2  
**And** defense update occurs in same cycle as ability update  
**And** user sees both Awareness and Will change simultaneously

**Acceptance Criteria Covered**: Awareness → Will cascade, Synchronous Updates

---

### Scenario 5: No defense update when Strength changes

**Purpose**: Strength does not affect any defenses

**Given** all defenses are at base values  
**And** Strength is at rank 0  
**When** user sets Strength to rank 10  
**Then** system does NOT update Dodge  
**And** system does NOT update Parry  
**And** system does NOT update Fortitude  
**And** system does NOT update Toughness  
**And** system does NOT update Will  
**And** all defenses remain at base values

**Acceptance Criteria Covered**: No Cascade for non-defense-linked abilities

---

### Scenario 6: No defense update when Dexterity changes

**Purpose**: Dexterity does not affect any defenses

**Given** all defenses are at base values  
**And** Dexterity is at rank 0  
**When** user sets Dexterity to rank 6  
**Then** system does NOT update any defenses  
**And** all defenses remain at base values

**Acceptance Criteria Covered**: No Cascade for DEX

---

### Scenario 7: No defense update when Intellect changes

**Purpose**: Intellect does not affect any defenses

**Given** all defenses are at base values  
**And** Intellect is at rank 0  
**When** user sets Intellect to rank 8  
**Then** system does NOT update any defenses  
**And** all defenses remain at base values

**Acceptance Criteria Covered**: No Cascade for INT

---

### Scenario 8: No defense update when Presence changes

**Purpose**: Presence does not affect any defenses

**Given** all defenses are at base values  
**And** Presence is at rank 0  
**When** user sets Presence to rank 4  
**Then** system does NOT update any defenses  
**And** all defenses remain at base values

**Acceptance Criteria Covered**: No Cascade for PRE

---

### Scenario 9: Cascade updates when ability decreased

**Purpose**: Defense decreases when linked ability decreases

**Given** Agility is set to rank 8 (Dodge = 18)  
**When** user changes Agility from 8 to 3  
**Then** system recalculates Dodge as 13 (10 + 3)  
**And** Dodge display updates from 18 to 13  
**And** update is immediate

**Acceptance Criteria Covered**: Cascade on decrease, Synchronous Updates

---

### Scenario 10: Cascade updates when ability reset to zero

**Purpose**: Defense returns to base when ability reset

**Given** Fighting is set to rank 10 (Parry = 20)  
**When** user resets Fighting to rank 0  
**Then** system recalculates Parry as 10 (10 + 0)  
**And** Parry display updates to show base value 10  
**And** update is immediate

**Acceptance Criteria Covered**: Cascade on reset

---

## Scenario Outline: Agility to Dodge cascade at various ranks

**Purpose**: Validate Dodge = 10 + Agility formula across rank range

**Given** Agility is being set  
**When** user sets Agility to <agility_rank>  
**Then** system calculates Dodge as <dodge_value> (10 + <agility_rank>)  
**And** Dodge display shows <dodge_value>

**Examples**:

| agility_rank | dodge_value | formula      | scenario            |
|--------------|-------------|--------------|---------------------|
| 0            | 10          | 10 + 0       | Base (average)      |
| 3            | 13          | 10 + 3       | Above average       |
| 5            | 15          | 10 + 5       | Peak human          |
| 8            | 18          | 10 + 8       | Superhuman          |
| 10           | 20          | 10 + 10      | Typical PL 10       |
| 15           | 25          | 10 + 15      | High superhuman     |
| 20           | 30          | 10 + 20      | Maximum rank        |
| -2           | 8           | 10 + (-2)    | Below average       |

**Acceptance Criteria Covered**: Agility → Dodge formula validation, Active defense +10 base

---

## Scenario Outline: Fighting to Parry cascade at various ranks

**Purpose**: Validate Parry = 10 + Fighting formula across rank range

**Given** Fighting is being set  
**When** user sets Fighting to <fighting_rank>  
**Then** system calculates Parry as <parry_value> (10 + <fighting_rank>)  
**And** Parry display shows <parry_value>

**Examples**:

| fighting_rank | parry_value | formula      | scenario            |
|---------------|-------------|--------------|---------------------|
| 0             | 10          | 10 + 0       | Base (average)      |
| 4             | 14          | 10 + 4       | Trained fighter     |
| 8             | 18          | 10 + 8       | Expert combatant    |
| 10            | 20          | 10 + 10      | Typical PL 10       |
| 12            | 22          | 10 + 12      | Master fighter      |
| 20            | 30          | 10 + 20      | Maximum rank        |
| -1            | 9           | 10 + (-1)    | Poor combatant      |

**Acceptance Criteria Covered**: Fighting → Parry formula validation, Active defense +10 base

---

## Scenario Outline: Stamina to Fortitude and Toughness cascade

**Purpose**: Validate Stamina affects BOTH Fortitude and Toughness with same value

**Given** Stamina is being set  
**When** user sets Stamina to <stamina_rank>  
**Then** system calculates Fortitude as <defense_value> (equals Stamina)  
**And** system calculates Toughness as <defense_value> (equals Stamina)  
**And** both Fortitude and Toughness display show <defense_value>

**Examples**:

| stamina_rank | defense_value | formula        | scenario                |
|--------------|---------------|----------------|-------------------------|
| 0            | 0             | STA (no +10)   | Base (average)          |
| 3            | 3             | STA (no +10)   | Above average           |
| 8            | 8             | STA (no +10)   | Superhuman              |
| 10           | 10            | STA (no +10)   | Typical PL 10           |
| 12           | 12            | STA (no +10)   | Powerhouse (Princess)   |
| 20           | 20            | STA (no +10)   | Maximum rank            |
| -2           | -2            | STA (no +10)   | Below average (fragile) |

**Acceptance Criteria Covered**: Stamina → Fortitude + Toughness formula, Resistance defense (no +10 base), Dual defense update

---

## Scenario Outline: Awareness to Will cascade at various ranks

**Purpose**: Validate Will = Awareness formula across rank range

**Given** Awareness is being set  
**When** user sets Awareness to <awareness_rank>  
**Then** system calculates Will as <will_value> (equals Awareness)  
**And** Will display shows <will_value>

**Examples**:

| awareness_rank | will_value | formula      | scenario              |
|----------------|------------|--------------|-----------------------|
| 0              | 0          | AWE (no +10) | Base (average)        |
| 2              | 2          | AWE (no +10) | Alert                 |
| 5              | 5          | AWE (no +10) | Very perceptive       |
| 8              | 8          | AWE (no +10) | Superhuman senses     |
| 10             | 10         | AWE (no +10) | Typical PL 10         |
| 15             | 15         | AWE (no +10) | Cosmic awareness      |
| -3             | -3         | AWE (no +10) | Oblivious             |

**Acceptance Criteria Covered**: Awareness → Will formula validation, Resistance defense (no +10 base)

---

## Scenario Outline: Complete cascade mapping for all 8 abilities

**Purpose**: Comprehensive test showing which abilities affect which defenses

**Given** ability <ability> is being set to rank <rank>  
**When** user sets <ability> to <rank>  
**Then** <dodge_change> occurs to Dodge  
**And** <parry_change> occurs to Parry  
**And** <fortitude_change> occurs to Fortitude  
**And** <toughness_change> occurs to Toughness  
**And** <will_change> occurs to Will

**Examples**:

| ability | rank | dodge_change        | parry_change        | fortitude_change  | toughness_change  | will_change       | cascade pattern                 |
|---------|------|---------------------|---------------------|-------------------|-------------------|-------------------|---------------------------------|
| STR     | 5    | no change           | no change           | no change         | no change         | no change         | No defense impact               |
| STA     | 8    | no change           | no change           | updates to 8      | updates to 8      | no change         | Affects 2 defenses              |
| AGL     | 6    | updates to 16       | no change           | no change         | no change         | no change         | Affects Dodge only              |
| DEX     | 4    | no change           | no change           | no change         | no change         | no change         | No defense impact               |
| FGT     | 10   | no change           | updates to 20       | no change         | no change         | no change         | Affects Parry only              |
| INT     | 7    | no change           | no change           | no change         | no change         | no change         | No defense impact               |
| AWE     | 5    | no change           | no change           | no change         | no change         | updates to 5      | Affects Will only               |
| PRE     | 6    | no change           | no change           | no change         | no change         | no change         | No defense impact               |

**Acceptance Criteria Covered**: All 4 cascade patterns, All 4 non-cascade abilities, Complete mapping

---

## Source Material

**Inherited From**: Story Map → Configure Abilities Feature Overview

**Referenced During Specification**:
- M&M 3E Handbook, Page 110: "Your Dodge defense is 10 + your Agility rank"
- M&M 3E Handbook, Page 110: "Your Parry defense is 10 + your Fighting rank"
- M&M 3E Handbook, Page 111: "Your Fortitude defense equals your Stamina rank"
- M&M 3E Handbook, Page 111: "Your Toughness equals your Stamina rank"
- M&M 3E Handbook, Page 111: "Your Will defense equals your Awareness rank"
- Domain Concepts Document: Cascading Dependencies section with complete ability-to-defense mappings
- Feature Overview: Defense calculation formulas confirming active (+10 base) vs resistance (no +10)

**Key Insight from Handbook**: Active defenses (Dodge, Parry) add +10 base because opponent rolls against them. Resistance defenses (Fortitude, Will, Toughness) have no +10 because you roll with them + d20.





