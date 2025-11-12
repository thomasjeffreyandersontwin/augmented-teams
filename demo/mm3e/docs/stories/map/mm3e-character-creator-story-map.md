# Story Map: MM3E Online Character Creator

**File Name**: `mm3e-character-creator-story-map.md`
**Location**: `demo/mm3e/docs/stories/map/mm3e-character-creator-story-map.md`

## System Purpose
An online character creator for Mutants & Masterminds 3rd Edition that guides users through building superhero characters according to game rules, calculating point costs automatically, validating prerequisites, and exporting characters for gameplay use.

---

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Story Map Structure

🎯 **Create Character** (8 features, ~75 stories)
│   *Relative Size: Similar to D&D character builder complexity*
│
├─ ⚙️ **Establish Identity** (~8 stories)
│  ├─ 📝 User enters character name
│  │   - and system saves to character sheet
│  ├─ 📝 User enters character concept
│  │   - and system saves as descriptor
│  ├─ 📝 User selects power level
│  │   - and system calculates and displays total point budget
│  └─ 📝 ~5 more stories
│
├─ ⚙️ **Allocate Abilities** (~12 stories)
│  ├─ 📝 User increases ability rank
│  │   - and system calculates point cost and updates budget
│  ├─ 📝 User decreases ability rank
│  │   - and system refunds points and updates budget
│  ├─ 📝 System updates dependent values when ability changes
│  │   - Updates skills, attacks, damage, and defenses
│  └─ 📝 ~9 more stories
│
├─ ⚙️ **Purchase Skills** (~15 stories)
│  ├─ 📝 User adds ranks to untrained skill
│  │   - and system calculates cost and displays total modifier
│  ├─ 📝 User adds ranks to trained-only skill
│  │   - and system validates training requirement
│  ├─ 📝 User adds ranks to ability-based skill
│  │   - and system applies ability modifier to total
│  └─ 📝 ~12 more stories
│
├─ ⚙️ **Select Advantages** (~14 stories)
│  ├─ 📝 User selects advantage without prerequisites
│  │   - and system adds to sheet and deducts cost
│  ├─ 📝 User selects ranked advantage
│  │   - and system prompts for rank selection
│  ├─ 📝 System validates advantage prerequisites
│  │   - Checks ability, skill, power, or other advantage requirements
│  └─ 📝 ~11 more stories
│
├─ ⚙️ **Build Powers** (~18 stories)
│  ├─ 📝 User selects base power effect
│  │   - and system displays base cost and available modifiers
│  ├─ 📝 User adds extra to power
│  │   - and system increases power cost
│  ├─ 📝 User adds flaw to power
│  │   - and system decreases power cost
│  └─ 📝 ~15 more stories
│
├─ ⚙️ **Calculate Defenses** (~6 stories)
│  ├─ 📝 System calculates dodge defense
│  │   - Based on ability modifier and purchased ranks
│  ├─ 📝 System calculates toughness defense
│  │   - Based on ability modifier only
│  ├─ 📝 User purchases defense ranks
│  │   - and system updates defense value and point cost
│  └─ 📝 ~3 more stories
│
└─ ⚙️ ~2 more features

---

🎯 **Manage Attacks** (6 features, ~45 stories)
│   *Relative Size: Complex combat calculation system*
│
├─ ⚙️ **Create Standard Attacks** (~8 stories)
│  ├─ 📝 User creates close combat attack
│  │   - and system calculates attack bonus from ability
│  ├─ 📝 User creates ranged combat attack
│  │   - and system calculates attack bonus from ability
│  ├─ 📝 User sets attack damage value
│  │   - and system validates against power level limits
│  └─ 📝 ~5 more stories
│
├─ ⚙️ **Create Power Attacks** (~9 stories)
│  ├─ 📝 User creates attack from damaging power
│  │   - and system derives attack bonus and damage from power
│  ├─ 📝 User creates attack from affliction power
│  │   - and system sets resistance check and conditions
│  ├─ 📝 System validates power attack against PL limits
│  │   - Checks attack + damage vs trade-off rules
│  └─ 📝 ~6 more stories
│
├─ ⚙️ **Apply Attack Modifiers** (~7 stories)
│  ├─ 📝 User applies circumstance modifier
│  │   - and system adjusts attack bonus
│  ├─ 📝 User applies power attack trade-off
│  │   - and system decreases attack, increases damage
│  └─ 📝 ~5 more stories
│
└─ ⚙️ ~3 more features

---

🎯 **Validate Character** (5 features, ~28 stories)
│   *Relative Size: Rules validation engine*
│
├─ ⚙️ **Validate Point Expenditure** (~6 stories)
│  ├─ 📝 System validates total points at or under budget
│  │   - Flags overspend errors to user
│  ├─ 📝 System validates point allocation per category
│  │   - Checks abilities, skills, advantages, powers, defenses
│  ├─ 📝 System calculates unspent points
│  │   - and displays available points by category
│  └─ 📝 ~3 more stories
│
├─ ⚙️ **Validate Power Level Limits** (~7 stories)
│  ├─ 📝 System validates attack + damage vs PL cap
│  │   - Flags attacks exceeding PL × 2
│  ├─ 📝 System validates dodge + toughness vs PL cap
│  │   - Flags defenses exceeding PL × 2
│  ├─ 📝 System validates ability scores vs PL
│  │   - Flags abilities exceeding PL + 10
│  └─ 📝 ~4 more stories
│
├─ ⚙️ **Validate Prerequisites** (~6 stories)
│  ├─ 📝 System validates advantage prerequisites
│  │   - Checks required abilities, skills, powers, advantages
│  ├─ 📝 System validates power prerequisites
│  │   - Checks required effects or descriptors
│  └─ 📝 ~4 more stories
│
└─ ⚙️ ~2 more features

---

🎯 **Manage Equipment** (7 features, ~35 stories)
│   *Relative Size: Item catalog and inventory system*
│
├─ ⚙️ **Select Standard Equipment** (~6 stories)
│  ├─ 📝 User selects equipment from catalog
│  │   - and system deducts equipment points
│  ├─ 📝 User removes equipment from character
│  │   - and system refunds equipment points
│  └─ 📝 ~4 more stories
│
├─ ⚙️ **Create Custom Equipment** (~7 stories)
│  ├─ 📝 User defines custom equipment properties
│  │   - and system calculates equipment point cost
│  ├─ 📝 User adds features to custom equipment
│  │   - and system updates total cost
│  └─ 📝 ~5 more stories
│
└─ ⚙️ ~5 more features

---

🎯 **Persist Character Data** (4 features, ~22 stories)
│   *Relative Size: Standard CRUD with export formats*
│
├─ ⚙️ **Save Character** (~6 stories)
│  ├─ 📝 User saves character to cloud storage
│  │   - and system validates data before saving
│  ├─ 📝 System auto-saves character during editing
│  │   - Saves draft every N minutes
│  ├─ 📝 User saves character revision
│  │   - and system creates version history entry
│  └─ 📝 ~3 more stories
│
├─ ⚙️ **Load Character** (~5 stories)
│  ├─ 📝 User loads character from storage
│  │   - and system populates all character fields
│  ├─ 📝 User loads character from previous version
│  │   - and system restores historical state
│  └─ 📝 ~3 more stories
│
├─ ⚙️ **Export Character** (~7 stories)
│  ├─ 📝 User exports character as PDF
│  │   - and system generates formatted character sheet
│  ├─ 📝 User exports character as JSON
│  │   - and system serializes all character data
│  ├─ 📝 User exports character for virtual tabletop
│  │   - and system formats for specific VTT platform
│  └─ 📝 ~4 more stories
│
└─ ⚙️ ~1 more feature

---

🎯 **Support User Experience** (6 features, ~32 stories)
│   *Relative Size: Standard UI/UX patterns*
│
├─ ⚙️ **Provide Rule Guidance** (~6 stories)
│  ├─ 📝 User views tooltip for game term
│  │   - and system displays definition and examples
│  ├─ 📝 User accesses help panel for section
│  │   - and system shows relevant rules text
│  └─ 📝 ~4 more stories
│
├─ ⚙️ **Navigate Character Sections** (~5 stories)
│  ├─ 📝 User switches between character tabs
│  │   - and system saves current section state
│  ├─ 📝 User uses quick navigation menu
│  │   - and system jumps to requested section
│  └─ 📝 ~3 more stories
│
├─ ⚙️ **Visualize Character Progress** (~6 stories)
│  ├─ 📝 System displays point budget visualization
│  │   - Shows spent vs available by category
│  ├─ 📝 System displays completion indicators
│  │   - Shows required vs completed sections
│  └─ 📝 ~4 more stories
│
└─ ⚙️ ~3 more features

---

## Notes

### Format (Shaping Phase)
- **Hierarchy**: 🎯 Epic → 📂 Sub-Epic → ⚙️ Feature → 📝 Story
- **Naming**: All levels use [Verb] [Noun] *[optional clarifier]* format
- **Story Counts**: Use (~X stories) for unexplored areas
- **Detail Level**: Only 10-20% of stories identified (critical/unique/architecturally significant)
- **Tree Characters**: Use │ ├─ └─ to show hierarchy
- **Emojis**: Visual indicators for quick scanning (NO "Epic:", "Feature:", "Story:" prefixes)
- **Estimates and Status**: Added in Discovery phase
- **NO Acceptance Criteria**: Added later in Explore phase

### Story Format (CRITICAL)
- **Story Title**: "User [verb] [noun]" or "System [verb] [noun] when [trigger]"
- **Single "and" clause**: "- and system [immediate response]" (shows user action + system response = ONE story)
- **NO extra notes during Shaping**: NO examples, NO data lists (save details for discovery/exploration)
- **NO separate system stories**: User action + immediate system response = ONE story, not two
- **Remaining Stories Format**: When showing example stories, add final line: "└─ 📝 ~X more stories" (shows approximate remaining count)
- **Remaining Features Format**: When showing example features within epic/sub-epic, add final line: "└─ ⚙️ ~X more features" (shows approximate remaining count)

### Shaping Decomposition Approach
- **Light touch**: Only decompose 10-20% of stories (critical/unique/architecturally significant)
- **Story counts**: Use (~X stories) at feature level, show approximate remaining at story level
- **Representative samples**: Show 2-3 example features/stories, then add "~X more features/stories" line
- **Extrapolate scope**: Enough to estimate but not exhaustive
- **Save exhaustive decomposition for Discovery**: Full permutation enumeration happens in Discovery phase


---

## Source Material

**Primary Source**: Mutants & Masterminds 3rd Edition - Hero's Handbook
- Location: `demo/mm3e/HeroesHandbook.pdf`
- Sections Referenced (Shaping): 
  - Chapter 1: Character Creation (pages 16-28)
  - Chapter 2: Abilities (pages 29-33)
  - Chapter 3: Skills (pages 34-63)
  - Chapter 4: Advantages (pages 64-77)
  - Chapter 5: Powers (pages 78-147)
  - Chapter 6: Gadgets & Gear (pages 148-167)
  - Chapter 7: Combat (pages 168-187)
- Date Generated: November 12, 2025

**Discovery Refinements**: November 12, 2025
- **Increment in Focus**: Increment 1 - Core Character Creation (NOW)
- **Additional Sections Referenced**:
  - Chapter 2: Abilities (pages 29-33) - Detailed ability modifier calculations, negative ranks, cascade update patterns
  - Chapter 3: Skills (pages 34-63) - Trained vs untrained skill distinctions, cost formulas (0.5 vs 1.0 points/rank), skill grouping by abilities
  - Chapter 4: Advantages (pages 64-77) - Exhaustive prerequisite types (ability, skill, advantage, power), AND/OR logic patterns, ranked advantages
  - Chapter 1: Character Creation (pages 16-28) - Point budget formula (15 × PL), category-based point tracking, validation rules
- **Areas Elaborated**: 
  - Increment 1 features fully decomposed (53 stories across 8 features)
  - Consolidation applied based on logic similarity (text fields, calculations, cascade patterns)
  - Separated by different algorithms (prerequisite types, cost formulas, UI patterns)
- **Consolidation Rationale**:
  - Same logic, different data → CONSOLIDATED (e.g., text input fields, unspent point calculations)
  - Different formulas/algorithms → SEPARATE (e.g., untrained vs trained skills, prerequisite types)
  - Category-specific UI work → SEPARATE (e.g., validation displays per category)

**Context for Exploration**: When writing acceptance criteria, reference sections above for domain rules and behavioral details. Key formulas documented in Discovery Refinements.

