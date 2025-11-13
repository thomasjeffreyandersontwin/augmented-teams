# ⚙️ Save Character - Feature Overview

**Navigation:** [📋 Story Map](../../mm3e-character-creator-story-map.md) | [📊 Increments](../../../increments/mm3e-character-creator-story-map-increments.md)

**Epic:** 🎯 Manage Characters  
**Feature:** ⚙️ Save Character  
**Stories:** 4 stories

---

## Feature Purpose

Enable user to persist character data to cloud storage, supporting both creation of new characters and updates to existing characters. Implements "warn don't prevent" philosophy - saves allowed even with validation warnings. Provides status feedback and graceful error handling for network/auth failures.

---

## Domain AC (Feature Level)

### Shared Concepts (from Solution Level)
- **Character**: The superhero being created/edited
- **User**: The player owning the character
- **Cloud Storage**: Persistent storage backend (implementation TBD)

### Feature-Specific Domain Concepts

**Character Persistence State** (feature-scoped):
- **New Character**: Character that has never been saved (no storage ID)
  - Operation: CREATE
  - Result: New record in storage with generated ID
- **Existing Character**: Character that was previously saved (has storage ID)
  - Operation: UPDATE
  - Result: Existing record overwritten with current data

**Save Operation Types** (feature-scoped):
- **Create**: Insert new character record
  - Precondition: Character has no storage ID
  - Action: POST to storage API, generate ID
  - Result: Character assigned storage ID
- **Update**: Overwrite existing character record
  - Precondition: Character has storage ID
  - Action: PUT to storage API with ID
  - Result: Existing record updated

**Save Status** (feature-scoped):
- **Saving**: Operation in progress (async)
- **Saved**: Operation completed successfully (with timestamp)
- **Error**: Operation failed (with error details)

**"Warn Don't Prevent" Philosophy** (feature-scoped - CRITICAL):
- Validation warnings do NOT block save operations
- Character can be saved even if:
  - Points overspent
  - PL caps exceeded
  - Prerequisites not met
  - Required fields empty (except character name)
- Warnings persisted WITH character for later review
- GM/player decide if "illegal" character acceptable

### Domain Behaviors

**Determine Operation Type**:
- Check if character has storage ID
- If no ID → CREATE
- If has ID → UPDATE
- Single code path (upsert pattern)

**Persist Character Data**:
- Serialize all character data (PL, abilities, defenses, points, warnings)
- Send to cloud storage
- Receive confirmation or error
- Update character with storage ID (if create)

**Display Status**:
- Show "Saving..." while operation in progress
- Show "Saved ✓" with timestamp when complete
- Show error message if operation fails

**Handle Errors**:
- Network errors: Offer retry
- Auth errors: Prompt re-authentication
- Validation errors from server: Display but allow (warn don't prevent)

### Domain Rules

1. **Upsert Pattern**: Create and Update use same logic, differentiated by storage ID existence
2. **Warn Don't Prevent**: Validation warnings NEVER block save - Handbook doesn't require legal characters
3. **Data Completeness**: Save ALL character data (PL, abilities, defenses, purchased ranks, points spent/total, validation warnings)
4. **Storage ID Assignment**: New characters receive ID from storage on create (not client-generated)
5. **Timestamp**: Each save records timestamp for "last modified" tracking
6. **Error Recovery**: Save errors allow retry (network issues transient)

---

## Stories and Acceptance Criteria

### 📝 Story 1: User saves new character to cloud storage

**Story Description**: User saves new character to cloud storage - and system creates new record

#### Acceptance Criteria

**Create Operation**:
- When user saves character that has no storage ID, then system creates new character record in storage
- When create operation initiated, then system sends character data to storage API (POST)
- When storage returns success, then system receives generated storage ID
- When ID received, then system stores ID with character (marks as existing)

**Data Persisted**:
- When creating character, then system includes: character name, hero identity, description, power level, all 8 ability ranks, all 5 defense values, purchased defense ranks, points spent/total, any validation warnings
- When character has incomplete data, then system saves partial character (allows work-in-progress)
- When character has validation warnings, then system saves warnings WITH character data

**Success Confirmation**:
- When create succeeds, then system displays "Character Created ✓" message
- When create succeeds, then system records save timestamp
- When character created, then subsequent saves become updates (has ID now)

---

### 📝 Story 2: User saves existing character to cloud storage

**Story Description**: User saves existing character to cloud storage - and system updates record

#### Acceptance Criteria

**Update Operation**:
- When user saves character that has storage ID, then system updates existing record in storage
- When update operation initiated, then system sends character data to storage API (PUT with ID)
- When storage returns success, then system confirms record updated
- When update confirmed, then system keeps existing storage ID (unchanged)

**Data Persisted**:
- When updating character, then system includes ALL current character data (same fields as create)
- When character data changed since last save, then system overwrites with current values
- When validation warnings changed, then system updates warnings in stored record

**Success Confirmation**:
- When update succeeds, then system displays "Saved ✓" message with timestamp
- When update succeeds, then system records new save timestamp (replaces old)
- When character updated, then system marks as "no unsaved changes"

---

### 📝 Story 3: System displays save status

**Story Description**: System displays save status - "Saving...", "Saved", with timestamp

#### Acceptance Criteria

**Saving Status**:
- When save operation begins, then system displays "Saving..." indicator (spinner or progress)
- When save in progress, then system disables save button (prevent double-save)
- When save takes > 2 seconds, then system displays "Still saving..." (user reassurance)

**Saved Status**:
- When save operation completes successfully, then system displays "Saved ✓" message
- When save succeeded, then system shows timestamp of save (e.g., "Saved at 10:30 PM")
- When saved status displayed, then system shows for 3 seconds then fades to subtle indicator

**Status Persistence**:
- When character has unsaved changes, then system shows "Unsaved changes" indicator
- When character just saved, then system shows "All changes saved" indicator
- When user makes edit after save, then system changes status to "Unsaved changes"

---

### 📝 Story 4: System handles save errors gracefully

**Story Description**: System handles save errors gracefully - network errors, auth errors with retry option

#### Acceptance Criteria

**Network Errors**:
- When save fails due to network error, then system displays "Save failed: Network error" message
- When network error occurs, then system offers "Retry" button
- When user clicks Retry, then system reattempts save operation
- When network error persists after 3 retries, then system suggests "Save will retry automatically when connection restored"

**Authentication Errors**:
- When save fails due to auth error (401/403), then system displays "Save failed: Please log in again"
- When auth error occurs, then system prompts user to re-authenticate
- When user re-authenticates successfully, then system automatically retries save
- When auth error persists, then system keeps character data in memory (not lost)

**Storage Errors**:
- When save fails due to storage error (500), then system displays "Save failed: Server error"
- When storage error occurs, then system offers "Retry" button
- When storage error persists, then system logs error details for debugging

**Error Recovery**:
- When any save error occurs, then system keeps character data in memory (never lost)
- When error resolved, then user can retry save without losing work
- When multiple errors occur, then system displays most recent error only

**"Warn Don't Prevent" for Validation**:
- When character has validation warnings (overspent, PL caps exceeded), then system ALLOWS save (doesn't treat as error)
- When saving character with warnings, then system includes warnings in saved data
- When validation error returned from server, then system treats as warning (not blocking error)

---

## Consolidation Decisions

**Why 4 stories (not 2 with create/update combined)**:
- **Story 1**: Create new character - distinct operation (POST, ID generation)
- **Story 2**: Update existing character - distinct operation (PUT, ID required)
- **Story 3**: Status display - separate UI concern (spans both create and update)
- **Story 4**: Error handling - separate concern (network, auth, storage errors)
- **Rationale**: Create and update are DIFFERENT database operations (POST vs PUT), not same logic

**Why NOT 1 story**:
- User confirmed: "I think this is two stories" (create vs update)
- Different HTTP operations (POST vs PUT)
- Different storage outcomes (generate ID vs use existing ID)
- **Different logic** → Keep separate

**AC Consolidation**:
- Status display consolidated (same UI for create and update)
- Error handling consolidated (same recovery flows for create and update)
- Both operations include same data fields (consolidated data model)

---

## Domain Rules Referenced

**From User Requirements**:
- "Warn don't prevent" philosophy: Validation warnings never block saves
- "Persistence is same logic regardless of manual or automatic" - Upsert pattern with operation detection
- Save errors should allow retry, keep data in memory

**From M&M 3E Context**:
- No handbook rules about character persistence (GM discretion)
- Characters saved as-is, including "illegal" builds
- Player/GM responsibility to follow or ignore rules

**Technical Pattern**:
- Upsert: Check ID existence → CREATE if absent, UPDATE if present
- HTTP: POST for create (returns ID), PUT for update (uses ID)
- Timestamps: Record save time for "last modified" tracking

**Formula**:
```
If character.storage_id exists:
  Operation = UPDATE (PUT)
Else:
  Operation = CREATE (POST)
  Result includes new storage_id
```

---

## Source Material

**Referenced During Exploration**:
- User requirement - "Warn don't prevent" philosophy
- User requirement - Create vs update are two stories
- Domain concepts - Save/Load Philosophy section





