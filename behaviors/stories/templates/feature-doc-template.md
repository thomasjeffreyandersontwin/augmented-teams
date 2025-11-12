# ⚙️ [Feature Name] - Feature Overview

**File Name**: `⚙️ [Feature Name] - Feature Overview.md`

**Epic:** [Epic Name]

## Feature Purpose

[Brief description of the feature and its business purpose]

---

## Domain AC (Feature Level)

**Domain AC is hierarchical - shared concepts should move UP to appropriate level:**
- **Solution-level**: Core concepts used across ALL epics → In story map document
- **Epic-level**: Concepts shared across features in epic → In epic document
- **Sub-Epic-level**: Concepts shared across features in sub-epic → In sub-epic document (if epic has sub-epics)
- **Feature-level**: Concepts specific to THIS feature → In this document

**For this feature:**
1. **Check higher levels first**: Does sub-epic, epic, or solution document already define shared concepts?
2. **Reference higher-level concepts**: Link to higher-level Domain AC if concepts already defined
3. **Define feature-specific concepts**: Only concepts unique to this feature

**Structure like a domain map** (see `behaviors/ddd/ddd-rule.mdc`):
1. **Core Domain Concepts** (nouns) - WHAT business objects exist (reference higher levels)
2. **Domain Behaviors** (verbs) - WHAT operations happen on concepts
3. **Domain Rules** - Business rules, formulas, validation patterns specific to this feature

**If domain map exists** (e.g., `<solution-folder>/<system-name>-domain-map.txt`), **extract relevant concepts.**

---

### Shared Domain Concepts (Reference Higher Levels)

**From Solution-level Domain AC** (if in story map):
- Reference: See story map Domain AC section for Character, User, and other system-wide concepts

**From Epic-level Domain AC** (if in epic document):
- Reference: See `🎯 [Epic Name] - Epic Overview.md` for concepts shared across features in this epic

**From Sub-Epic-level Domain AC** (if in sub-epic document):
- Reference: See `📂 [Sub-Epic Name] - Sub-Epic Overview.md` for concepts shared across features in this sub-epic

---

### Feature-Specific Domain Concepts

**[Primary Business Concept]:** (The main thing this feature operates on)
- What it IS (definition in business terms)
- Key attributes/components
- Constraints or rules
- Relationships to other concepts

**[Related Concept]:**
- What it IS
- How it relates to primary concept
- Key characteristics

**Example - Character Persistence**:
- **Character**: Player-created hero in game system
  - Composed of: Abilities, Skills, Advantages, Powers, Defenses, Attacks, Equipment
  - Has point budget based on Power Level (15 × PL)
  - Can be in draft or complete state
  
- **Ability**: Fundamental attribute of character (Strength, Agility, etc.)
  - Range: 0-20 ranks
  - Cost: 2 points per rank
  - Affects: Skills, Defenses, Attack bonuses
  
- **Skill**: Trained capability
  - Types: Untrained (0.5 pts/rank), Trained-only (1 pt/rank)
  - Based on linked Ability
  - Total modifier = Ability modifier + Skill ranks

---

### Domain Behaviors

**[Behavior Name]:** (Operation on domain concepts)
- What it does to which concepts
- When it happens
- Business rules governing it

**Example**:
- **Save**: Persist Character to storage
  - Operations: Create (new), Update (existing), Save As Revision (versioned copy)
  - Always saves complete Character (all components)
  - Validation warnings don't prevent save ("Warn, Don't Prevent")

---

### Domain Rules

- [Business rule or formula]
- [Validation pattern]
- [Constraint]

**NOT like this (operations first, no business concepts)**:
- ❌ Starting with "Save Operation" without defining what's being saved
- ❌ "API Contract", "Endpoint", "Data Structure" (technical terms)
- ❌ Missing core concepts like Character, Ability, Skill

---

## Stories ([X] total)

### 1. **[Story Title]** - 📝 [Verb] [Noun]

**Story Description**: [Brief description with user action and system response]

#### Acceptance Criteria

##### [AC Group Name]
- **When** [condition/action], **then** [outcome/response]
- **When** [condition/action], **then** [outcome/response]

##### [AC Group Name]
- **When** [condition/action], **then** [outcome/response]

---

### 2. **[Story Title]** - 📝 [Verb] [Noun]

**Story Description**: [Brief description]

#### Acceptance Criteria

##### [AC Group Name]
- **When** [condition/action], **then** [outcome/response]

---

**[CRITICAL]**: All notes, consolidation decisions, domain rules, and source material go BELOW all acceptance criteria

---

## Notes

[Any additional notes about the feature, implementation considerations, or clarifications]

**Consolidation Applied**:
- [Notes about what was consolidated and why]

---

## Consolidation Decisions

**Consolidated (Same Logic):**
- ✅ [What was consolidated and why]
- ✅ [Another consolidation decision]

**Separated (Different Logic):**
- ❌ [What was kept separate and why]
- ❌ [Another separation decision]

**Result**: [X] stories with exhaustive AC decomposition

---

## Domain Rules Referenced

**From [Source]:**
- [Reference to source material sections]
- [Key formulas or rules]

**Discovery Refinements Applied:**
- [Consolidation decisions]
- [Logic patterns identified]
- [Key elaborations from discovery phase]

---

## Source Material

**Inherited From**: Story Map (Discovery Refinements)
- Primary Source: [Document name and location]
- Sections Referenced: [Chapter/page references]
- Discovery Refinements: [Key elaborations from discovery phase]

