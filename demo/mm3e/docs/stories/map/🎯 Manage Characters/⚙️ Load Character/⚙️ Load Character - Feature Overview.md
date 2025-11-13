# ⚙️ Load Character - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Manage Characters  
**Feature:** ⚙️ Load Character  
**Stories:** 4 stories

---

## Feature Purpose

Enable user to load previously saved character from cloud storage, restoring all character data and recalculating all derived values (defenses from abilities, point totals, budget). Validates data integrity and handles corrupted/missing data gracefully.

---

## Domain AC (Feature Level)

### Shared Concepts (from Solution Level)
- **Character**: The superhero being loaded
- **User**: The player owning the character
- **Cloud Storage**: Persistent storage backend

### Feature-Specific Domain Concepts

**Saved Character** (feature-scoped):
- **Definition**: Character record stored in cloud with storage ID
- **Data Includes**: PL, abilities, defenses, purchased ranks, points, warnings, metadata (name, timestamps)
- **Selection**: User picks from character list (shows name, PL, last modified)

**Character Restoration** (feature-scoped):
- **Fetch**: Retrieve character data from storage by ID
- **Deserialize**: Parse stored data into character object
- **Restore**: Repopulate UI fields with stored values
- **Recalculate**: Recompute derived values (defenses, totals, budget)
- **Validate**: Check data integrity

**Derived Values Recalculation** (feature-scoped):
- **Defenses**: Recalculate from abilities (in case formulas changed)
- **Point Totals**: Recalculate spent points by category
- **Remaining Budget**: Recalculate (PL × 15 - spent)
- **PL Caps**: Recalculate and re-validate warnings
- **Rationale**: Don't trust stored derived values - always recalculate from source data

**Data Integrity** (feature-scoped):
- **Valid**: All required fields present, data types correct
- **Corrupt**: Missing fields, invalid data types, parsing errors
- **Incomplete**: Optional fields missing (acceptable)
- **Validation**: Check before restoring to UI

### Domain Behaviors

**Load from Storage**:
- User selects character from list
- Fetch character data by storage ID
- Deserialize JSON/data format
- Check integrity

**Restore Character State**:
- Repopulate all 8 ability rank fields
- Restore PL selection
- Restore character name, identity, description
- Restore purchased defense ranks
- Load persisted validation warnings

**Recalculate Everything**:
- Recalculate defenses from abilities
- Recalculate point totals (abilities, defenses)
- Recalculate remaining budget
- Re-run PL cap validations
- Update all displays

**Validate Integrity**:
- Check required fields present (character name, PL)
- Check data types valid (ranks are numbers, etc.)
- If corrupt, display error and prevent load
- If incomplete (missing optional), allow load with defaults

### Domain Rules

1. **Recalculation Rule**: ALWAYS recalculate derived values on load (never trust stored derived values)
2. **Integrity Validation**: Check data before restoring to UI (prevent corrupt data display)
3. **Partial Load**: If optional fields missing, use defaults (don't fail entire load)
4. **Cascade Trigger**: Loading abilities triggers defense recalculation (same as manual ability entry)
5. **Warning Restoration**: Load and display any persisted validation warnings

---

## Stories and Acceptance Criteria

### 📝 Story 1: User loads saved character from list

**Story Description**: User loads saved character from list - and system fetches character data

#### Acceptance Criteria

**Character Selection**:
- When user views character list, then system displays saved characters (name, PL, last modified)
- When user selects character from list, then system initiates load operation
- When load initiated, then system displays "Loading..." indicator

**Fetch Operation**:
- When character selected, then system fetches character data from storage using storage ID
- When fetch initiated, then system sends GET request to storage API
- When storage returns data, then system deserializes character data
- When fetch completes, then system proceeds to restoration

**Fetch Errors**:
- When character not found in storage (404), then system displays "Character not found" error
- When fetch fails due to network error, then system displays "Load failed: Network error" with Retry option
- When auth error occurs (401), then system prompts re-authentication
- When fetch error occurs, then system keeps current character (doesn't clear)

---

### 📝 Story 2: System restores all ability ranks

**Story Description**: System restores all ability ranks - repopulating 8 ability fields

#### Acceptance Criteria

**Restore Ability Ranks**:
- When character data loaded, then system restores all 8 ability ranks (STR, STA, AGL, DEX, FGT, INT, AWE, PRE)
- When ability ranks restored, then system populates ability rank fields with stored values
- When rank field populated, then system displays restored rank

**Restore Examples**:
- When loaded character has STR=5, STA=3, then system sets STR field to 5 and STA field to 3
- When loaded character has Agility=10, then system sets Agility field to 10
- When loaded character has negative rank (INT=-1), then system restores negative value

**UI Population**:
- When all 8 ranks restored, then system displays all abilities with restored values
- When abilities populated, then system marks restoration as complete
- When abilities restored, then system enables editing (user can modify after load)

---

### 📝 Story 3: System recalculates all derived values

**Story Description**: System recalculates all derived values - defenses, point totals, budget

#### Acceptance Criteria

**Recalculate Defenses**:
- When ability ranks restored, then system recalculates all 5 defense base values from abilities
- When Agility restored, then system recalculates Dodge (10 + Agility)
- When Fighting restored, then system recalculates Parry (10 + Fighting)
- When Stamina restored, then system recalculates Fortitude and Toughness (both from Stamina)
- When Awareness restored, then system recalculates Will (Awareness)

**Add Purchased Ranks**:
- When defense bases calculated, then system adds any purchased ranks to bases
- When Dodge base=15 and 2 purchased ranks, then Dodge total = 17
- When purchased ranks restored, then system displays total defense values

**Recalculate Point Totals**:
- When abilities restored, then system recalculates total ability points (Σ(rank × 2))
- When defense purchases restored, then system recalculates total defense points
- When all traits restored, then system calculates total points spent across all categories

**Recalculate Budget**:
- When total spent recalculated, then system calculates remaining (PL × 15 - spent)
- When budget calculated, then system displays spent/total
- When spent > total, then system displays overspend warning

**PL Cap Validation**:
- When all values restored and recalculated, then system re-runs all 6 PL cap validations
- When any caps exceeded, then system displays warnings (saved warnings may differ from current)
- When validations complete, then character fully restored and ready for use

---

### 📝 Story 4: System validates loaded data integrity

**Story Description**: System validates loaded data integrity - checking for corrupt or missing data, displaying errors if found

#### Acceptance Criteria

**Required Field Validation**:
- When character data loaded, then system checks required fields present (character name, PL, abilities)
- When required field missing, then system displays "Character data corrupt: missing [field]" error
- When required fields valid, then system proceeds with restoration

**Data Type Validation**:
- When loading character, then system validates ability ranks are numbers
- When loading character, then system validates PL is number in valid range (1-20)
- When data type invalid, then system displays "Character data corrupt: invalid [field] value" error
- When data types valid, then system proceeds with restoration

**Corruption Handling**:
- When multiple fields corrupt, then system displays all corruption errors together
- When critical corruption detected (can't parse), then system prevents load and keeps current character
- When minor corruption (optional field invalid), then system loads with defaults for corrupt fields

**Missing Optional Fields**:
- When hero identity missing, then system defaults to empty string (allows)
- When description missing, then system defaults to empty string (allows)
- When purchased defense ranks missing, then system defaults to 0 for all (allows)
- When optional field missing, then system logs warning but completes load

**Integrity Success**:
- When all validation passes, then system marks character as "validated ✓"
- When integrity confirmed, then system proceeds to full restoration and recalculation
- When character fully loaded, then system displays "Character Loaded Successfully"

---

## Consolidation Decisions

**Why 4 stories**:
- **Story 1**: Fetch from storage - network operation
- **Story 2**: Restore ability ranks - repopulate UI fields (explicit because abilities are foundation)
- **Story 3**: Recalculate derived values - complex calculation cascade (defenses, totals, budget, validations)
- **Story 4**: Validate integrity - data validation (corrupt, missing, invalid types)
- **Rationale**: Each represents distinct concern (fetch, restore, calculate, validate)

**Why NOT 1 story**:
- Fetch, restore, recalculate, and validate are DIFFERENT operations
- Different failure modes (network vs corrupt data vs calculation error)
- Different user feedback needs (fetch status vs validation errors)
- **Different logic** → Keep separate for clarity

**AC Consolidation**:
- All 8 ability restorations consolidated (same UI population pattern)
- All 5 defense recalculations consolidated (same cascade trigger)
- All validation checks consolidated (same integrity concern)
- Point total recalculations consolidated (single aggregation pass)

---

## Domain Rules Referenced

**From Load/Restore Logic**:
- Always recalculate derived values (defenses from abilities)
- Never trust stored derived values (formulas may have changed)
- Validate before restoring (prevent corrupt data in UI)
- Use defaults for missing optional fields

**From M&M 3E Handbook**:
- Same defense formulas as Configure Abilities (pages 110-111)
- Same point cost formulas (page 26)
- Character integrity not defined by handbook (implementation decision)

**Technical Pattern**:
```
Load Flow:
  1. Fetch(storage_id) → character_data
  2. Validate(character_data) → valid/corrupt
  3. Restore(character_data) → populate UI
  4. Recalculate() → defenses, totals, budget
  5. Display() → show character
```

---

## Source Material

**Referenced During Exploration**:
- Domain concepts - Save/Load Philosophy section
- Domain concepts - Dependencies & Cascading Updates (same cascade on load as on manual entry)
- User requirement - Data integrity validation before restoration





