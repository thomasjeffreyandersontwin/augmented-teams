# ⚙️ Enter Basic Identity - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Establish Character Foundation  
**Feature:** ⚙️ Enter Basic Identity  
**Stories:** 2 stories

---

## Feature Purpose

Enable user to establish the fundamental identity information for a new M&M 3E character, including character name (with uniqueness validation) and basic identity fields (hero identity and description). This is the absolute first step in character creation - without this, no character exists.

---

## Domain AC (Feature Level)

### Shared Concepts (from Solution Level)
- **Character**: The superhero being created (defined at solution level)
- **User**: The player creating the character (defined at solution level)

### Feature-Specific Domain Concepts

**Character Identity** (feature-scoped):
- **Character Name**: Unique identifier for the character across user's character list
  - Must be unique within user's saved characters
  - Text field, required
  - Used for character selection, display in lists
- **Hero Identity**: Public superhero name/alias the character uses
  - Text field, optional
  - May differ from character name
  - Example: Character Name "Batman", Hero Identity "Bruce Wayne"
- **Description**: Free-text narrative about the character
  - Text field, optional
  - Used for player notes, background, appearance details

### Domain Behaviors

**Validate Uniqueness**:
- Check character name against list of user's existing saved characters
- Case-insensitive comparison
- Prevent duplicate character names within user's collection

**Validate Text Fields**:
- Basic text validation (not empty for required fields)
- No special character restrictions (superhero names can have symbols, punctuation)
- Length limits reasonable (e.g., 100 chars for names, 1000+ for description)

### Domain Rules

1. **Uniqueness Rule**: Character name must be unique within user's character collection
   - Formula: `COUNT(characters WHERE LOWER(name) = LOWER(input_name)) = 0`
   - If violated: Display warning "Character with this name already exists"
   
2. **Required Fields**: Character name is required (minimum for character existence)
   - Hero identity and description are optional (can be added later)

3. **Identity Independence**: Hero identity is independent of character name
   - Players can use either field for either purpose (no enforced semantics)
   - Flexibility supports different player preferences

---

## Stories and Acceptance Criteria

### 📝 Story 1: User enters character name

**Story Description**: User enters character name - and system validates uniqueness against saved characters

#### Acceptance Criteria

**Basic Input**:
- When user types character name into name field, then system captures text value
- When user clears name field, then system displays "Name required" indicator
- When name field is empty, then system disables character creation proceed action

**Uniqueness Validation**:
- When user enters name that matches existing character (case-insensitive), then system displays "Character with this name already exists" warning
- When user enters unique name, then system clears any previous uniqueness warnings
- When uniqueness check completes successfully, then system enables character creation to proceed

**Real-time Feedback**:
- When user types in name field, then system performs uniqueness check after 500ms pause (debounce)
- When uniqueness check is in progress, then system displays checking indicator
- When name field loses focus, then system performs final uniqueness validation

---

### 📝 Story 2: User enters identity fields

**Story Description**: User enters identity fields - hero identity and description with basic text validation

####  Acceptance Criteria

**Hero Identity Input**:
- When user types hero identity into identity field, then system captures text value
- When user leaves hero identity blank, then system allows (optional field)
- When hero identity exceeds 100 characters, then system displays character count warning

**Description Input**:
- When user types character description, then system captures multi-line text value
- When user leaves description blank, then system allows (optional field)
- When description is edited, then system preserves line breaks and formatting
- When description exceeds 2000 characters, then system displays character count warning

**Field Validation**:
- When user enters text in any identity field, then system validates against length limits
- When validation passes, then system stores field values
- When validation fails on optional fields, then system displays warning but allows proceeding

---

## Consolidation Decisions

**Why 2 stories (not 3)**:
- **Consolidated**: Hero identity and description use same validation logic (basic text, optional, length checks)
- **Separate**: Character name has unique validation (uniqueness check + required) - different business logic

**AC Consolidation**:
- All text input uses same capture mechanism (consolidated behavioral pattern)
- Uniqueness check is separate concern (only for character name)
- Optional field handling consolidated (same pattern for hero identity and description)

---

## Domain Rules Referenced

**From M&M 3E Handbook**:
- Character sheet layout (page 52) - shows Name, Identity fields
- No specific M&M 3E rules govern character naming (house rules/GM discretion)
- Identity fields are freeform for creative freedom

**From User Requirements**:
- "Warn don't prevent" philosophy: Validation warns but doesn't block
- Character name uniqueness prevents confusion in character lists

---

## Source Material

**Referenced During Exploration**:
- `demo/mm3e/docs/mm3e-domain-concepts.md` - Character identity field definitions
- Handbook pages 52-54 - Character sheet examples showing identity field usage
- User requirement - Uniqueness validation for character name

**Formulas Applied**:
- Uniqueness check: `COUNT(characters WHERE LOWER(name) = LOWER(input)) = 0`
- Length validation: `LENGTH(field) ≤ max_length`





