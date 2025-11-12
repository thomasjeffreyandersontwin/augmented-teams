# 🎯 [Epic Name] - Epic Overview

**File Name**: `🎯 [Epic Name] - Epic Overview.md`

## Epic Purpose

[Brief description of the epic and its business purpose across multiple features]

---

## Domain AC (Epic Level)

**Epic-level Domain AC defines concepts SHARED across features in this epic.**

**Only include concepts that:**
- Are used by MULTIPLE features in this epic
- Would be duplicated if kept at feature level
- Represent core business objects for this epic's domain

**Do NOT include:**
- Concepts specific to single features (keep at feature level)
- Concepts used across ALL epics (elevate to solution level in story map)

---

### Core Domain Concepts (Shared Across Epic)

**[Shared Business Concept]:** (Used by multiple features in this epic)
- What it IS (definition in business terms)
- Key attributes, components, relationships
- Constraints and rules governing the concept
- **Used by features**: [Feature 1], [Feature 2], [Feature 3]

**Example - Create Character Epic**:
- **Ability**: Fundamental attribute of character (8 core abilities)
  - Range: 0-20 ranks (10 is average human)
  - Cost: 2 points per rank
  - Modifier: (Rank - 10) ÷ 2 rounded down
  - **Used by features**: Allocate Abilities, Purchase Skills, Calculate Defenses

- **Skill**: Trained capability based on Ability
  - Types: Untrained (0.5 pts/rank), Trained-only (1 pt/rank)
  - Total Modifier: Ability modifier + Skill ranks
  - **Used by features**: Purchase Skills, Validate Prerequisites

---

## Features in This Epic

### ⚙️ [Feature Name] ([X] stories)
**Purpose**: [Brief feature purpose]
**Domain AC**: See `⚙️ [Feature Name] - Feature Overview.md`

### ⚙️ [Feature Name] ([X] stories)
**Purpose**: [Brief feature purpose]
**Domain AC**: See `⚙️ [Feature Name] - Feature Overview.md`

---

## Notes

[Any epic-level notes, patterns, or considerations]

---

## Source Material

**Inherited From**: Story Map
- See story map "Source Material" section for primary source
- Additional references specific to this epic
