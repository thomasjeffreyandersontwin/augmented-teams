# 📝 User enters character concept

## Story Information
**Feature**: Establish Identity
**Epic**: Create Character
**Status**: Scenarios Added

---

## Story Description

User enters character concept - and system saves concept to character

---

## Acceptance Criteria Reference
**Source**: Feature document - ⚙️ Establish Identity - Feature Overview.md

- AC1: When user enters character concept, then system saves concept to character

---

## Background

**Given** character creation screen is displayed
**And** the Establish Identity section is displayed
**And** the character concept field is available

---

## Scenarios

### Scenario 1: Enter character concept successfully (happy path)

**Purpose**: User enters character concept and system saves it

**Given** the character concept field is empty
**When** user types "Street-smart vigilante with fire powers" into the concept field
**Then** system saves "Street-smart vigilante with fire powers" as the character concept
**And** the concept displays "Street-smart vigilante with fire powers" in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 2: Update existing character concept

**Purpose**: User changes previously entered character concept

**Given** the character concept field contains "Street-smart vigilante with fire powers"
**When** user changes the concept to "Genius inventor with high-tech armor"
**Then** system saves "Genius inventor with high-tech armor" as the new character concept
**And** the concept displays "Genius inventor with high-tech armor" in the field
**And** the previous value is replaced

**Acceptance Criteria Covered**: AC1

---

### Scenario 3: Clear character concept (empty entry)

**Purpose**: User removes character concept by deleting all text

**Given** the character concept field contains "Street-smart vigilante with fire powers"
**When** user deletes all text from the character concept field
**Then** system saves empty value for character concept
**And** the character concept field displays as empty

**Acceptance Criteria Covered**: AC1

---

### Scenario 4: Enter short character concept

**Purpose**: System accepts brief, concise character concepts

**Given** the character concept field is empty
**When** user types "Speedster" as the character concept
**Then** system saves "Speedster" as the character concept
**And** the concept displays "Speedster" in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 5: Enter detailed character concept

**Purpose**: System accepts comprehensive, detailed character concepts

**Given** the character concept field is empty
**When** user types "Reformed criminal with superhuman strength who protects the innocent from the same criminal organizations he once worked for"
**Then** system saves the entire detailed concept to the character
**And** the concept displays the full text in the field
**And** the field provides appropriate display handling for longer text

**Acceptance Criteria Covered**: AC1

---

### Scenario 6: Enter character concept with special characters

**Purpose**: System accepts concepts with punctuation and special characters

**Given** the character concept field is empty
**When** user types "Tech-genius & inventor (with attitude!)" into the concept field
**Then** system saves "Tech-genius & inventor (with attitude!)" exactly as entered
**And** the concept displays with all punctuation and special characters preserved

**Acceptance Criteria Covered**: AC1

---

### Scenario 7: Enter character concept with unicode characters

**Purpose**: System accepts concepts with international and unicode characters

**Given** the character concept field is empty
**When** user types "Místico guardián del bosque encantado" into the concept field
**Then** system saves "Místico guardián del bosque encantado" exactly as entered
**And** the concept displays with all unicode characters and accents preserved

**Acceptance Criteria Covered**: AC1

---

### Scenario 8: Enter character concept with leading and trailing whitespace

**Purpose**: System handles whitespace in concept entries

**Given** the character concept field is empty
**When** user types "  Fire-wielding hero  " with leading and trailing spaces
**Then** system saves the text with whitespace trimmed or preserved based on business rules
**And** the concept displays consistently in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 9: Enter character concept with only whitespace

**Purpose**: System handles whitespace-only entries

**Given** the character concept field is empty
**When** user types only spaces "     " into the concept field
**Then** system saves the whitespace or treats as empty based on business rules
**And** the concept field displays appropriately
**And** system may validate or warn if whitespace-only is invalid

**Acceptance Criteria Covered**: AC1

---

### Scenario 10: Enter character concept with numbers

**Purpose**: System accepts concepts containing numeric values

**Given** the character concept field is empty
**When** user types "1 of 12 experimental super-soldiers" into the concept field
**Then** system saves "1 of 12 experimental super-soldiers" as the character concept
**And** the concept displays with numbers preserved

**Acceptance Criteria Covered**: AC1

---

### Scenario 11: Enter archetype-based character concept

**Purpose**: User enters a classic superhero archetype as concept

**Given** the character concept field is empty
**When** user types "Paragon" into the concept field
**Then** system saves "Paragon" as the character concept
**And** the concept displays "Paragon" in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 12: Enter power-focused character concept

**Purpose**: User describes character primarily by powers

**Given** the character concept field is empty
**When** user types "Telekinetic with telepathy and mind control" into the concept field
**Then** system saves "Telekinetic with telepathy and mind control" as the character concept
**And** the concept displays the power-focused description in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 13: Enter origin-focused character concept

**Purpose**: User describes character primarily by origin story

**Given** the character concept field is empty
**When** user types "Alien warrior stranded on Earth" into the concept field
**Then** system saves "Alien warrior stranded on Earth" as the character concept
**And** the concept displays the origin-focused description in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 14: Enter role-focused character concept

**Purpose**: User describes character primarily by team role or function

**Given** the character concept field is empty
**When** user types "Team leader and tactical strategist" into the concept field
**Then** system saves "Team leader and tactical strategist" as the character concept
**And** the concept displays the role-focused description in the field

**Acceptance Criteria Covered**: AC1

---

### Scenario 15: Multiple rapid updates to character concept

**Purpose**: System handles quick successive changes correctly

**Given** the character concept field is empty
**When** user types "Speedster"
**And** immediately changes it to "Speedster with lightning powers"
**And** immediately changes it to "Time-manipulating speedster"
**Then** system saves "Time-manipulating speedster" as the final character concept
**And** the concept displays "Time-manipulating speedster" in the field
**And** all intermediate states are handled correctly without data loss

**Acceptance Criteria Covered**: AC1

---

## Scenario Coverage Summary

### Happy Path Coverage
- ✅ Enter character concept successfully (Scenario 1)
- ✅ Update existing concept (Scenario 2)
- ✅ Clear concept (Scenario 3)

### Edge Cases Coverage
- ✅ Short/brief concept (Scenario 4)
- ✅ Detailed/long concept (Scenario 5)
- ✅ Special characters and punctuation (Scenario 6)
- ✅ Unicode and international characters (Scenario 7)
- ✅ Leading/trailing whitespace (Scenario 8)
- ✅ Whitespace-only entry (Scenario 9)
- ✅ Concepts with numbers (Scenario 10)
- ✅ Archetype-based concepts (Scenario 11)
- ✅ Power-focused concepts (Scenario 12)
- ✅ Origin-focused concepts (Scenario 13)
- ✅ Role-focused concepts (Scenario 14)
- ✅ Rapid successive updates (Scenario 15)

### Acceptance Criteria Coverage
- ✅ AC1: Enter character concept - All 15 scenarios

**Total Scenarios**: 15 (3 happy path + 12 edge cases)

---

## Notes

### Business Rules to Clarify
- **Whitespace Handling**: Should leading/trailing whitespace be trimmed or preserved?
- **Whitespace-Only**: Should whitespace-only entries be treated as empty or invalid?
- **Maximum Length**: What is the character limit for concepts? (Tested ~130 chars in Scenario 5)
- **Required Field**: Is character concept required, or can it be left empty?
- **Format Guidance**: Should UI provide examples of concept types (archetype, powers, origin, role)?

### Character Concept Patterns
Character concepts in M&M3e typically fall into categories:
- **Archetype**: "Paragon", "Powerhouse", "Gadgeteer", "Mystic"
- **Power-Based**: "Telekinetic martial artist", "Fire controller"
- **Origin-Based**: "Mutant outcast", "Alien refugee", "Magic user"
- **Role-Based**: "Team leader", "Mentor", "Strategist"
- **Combined**: "Street-smart vigilante with fire powers" (role + powers)

### Related Stories
- **User enters identity text fields** - Consolidated story covering all text fields including concept
- **User enters character name** - Character name often reflects concept
- **User clears identity field** - Explicit clear action (different from backspace/delete)

---

## Source Material

**Inherited From**: Story Map → Feature Document
- Primary Source: Mutants & Masterminds 3rd Edition - Hero's Handbook
- Chapter 1: Character Creation (pages 16-28) - Character concept guidance
- Page 18: "Concept" section describes character in one sentence or phrase

**Exploration Phase**:
- Scenarios generated: November 12, 2025
- Edge cases derived from standard text input patterns
- Concept pattern categories from Hero's Handbook examples (Archetype, Power, Origin, Role)
- Unicode support for international player base

---

## Implementation Guidance

### Character Concept Field
- **Field Type**: Single-line text input (or multi-line for longer concepts)
- **Validation**: Accept standard text, special characters, and unicode
- **Display**: Show full concept with appropriate overflow handling
- **Save Timing**: Auto-save on blur or after brief typing delay
- **Placeholder**: "Describe your character in a phrase (e.g., 'Genius inventor with high-tech armor')"

### UI Enhancements
- **Examples/Help Text**: Show common concept patterns (Archetype, Powers, Origin, Role)
- **Character Counter**: Optional display showing concept length
- **Inspiration**: Link to archetype examples from Hero's Handbook

### Special Considerations
- **Concept Guides Builds**: Character concept often informs power and skill selections
- **Campaign Fit**: Concept should fit game master's campaign setting
- **Flexibility**: Allow players to update concept as character develops
- **Empty Concepts**: Allow empty during creation (player may define concept during play)

