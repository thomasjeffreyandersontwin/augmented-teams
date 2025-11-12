# Story Map Increments: MM3E Online Character Creator

**File Name**: `mm3e-character-creator-story-map-increments.md`
**Location**: `demo/mm3e/docs/stories/increments/mm3e-character-creator-story-map-increments.md`

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Value Increment 1: Core Character Creation - NOW
**Priority**: NOW
**Relative Size**: Compared to basic D&D character builder (medium complexity)
**Description**: Minimum viable character creator allowing users to establish identity, allocate points to abilities/skills/advantages, and save basic characters.

│
├─ 🎯 **Create Character** (PARTIAL - 4 of 8 features)
│  │
│  ├─ ⚙️ **Establish Identity** (~8 stories)
│  │  ├─ 📝 User enters character name
│  │  │   - and system saves to character sheet
│  │  ├─ 📝 User enters character concept
│  │  │   - and system saves as descriptor
│  │  ├─ 📝 User selects power level
│  │  │   - and system calculates and displays total point budget
│  │  └─ 📝 ~5 more stories
│  │
│  ├─ ⚙️ **Allocate Abilities** (~12 stories)
│  │  ├─ 📝 User increases ability rank
│  │  │   - and system calculates point cost and updates budget
│  │  ├─ 📝 User decreases ability rank
│  │  │   - and system refunds points and updates budget
│  │  ├─ 📝 System updates dependent values when ability changes
│  │  │   - Updates skills, attacks, damage, and defenses
│  │  └─ 📝 ~9 more stories
│  │
│  ├─ ⚙️ **Purchase Skills** (~15 stories)
│  │  ├─ 📝 User adds ranks to untrained skill
│  │  │   - and system calculates cost and displays total modifier
│  │  ├─ 📝 User adds ranks to trained-only skill
│  │  │   - and system validates training requirement
│  │  ├─ 📝 User adds ranks to ability-based skill
│  │  │   - and system applies ability modifier to total
│  │  └─ 📝 ~12 more stories
│  │
│  └─ ⚙️ **Select Advantages** (~14 stories)
│     ├─ 📝 User selects advantage without prerequisites
│     │   - and system adds to sheet and deducts cost
│     ├─ 📝 User selects ranked advantage
│     │   - and system prompts for rank selection
│     ├─ 📝 System validates advantage prerequisites
│     │   - Checks ability, skill, power, or other advantage requirements
│     └─ 📝 ~11 more stories
│
├─ 🎯 **Validate Character** (PARTIAL - 2 of 5 features)
│  │
│  ├─ ⚙️ **Validate Point Expenditure** (~6 stories)
│  │  ├─ 📝 System validates total points at or under budget
│  │  │   - Flags overspend errors to user
│  │  ├─ 📝 System validates point allocation per category
│  │  │   - Checks abilities, skills, advantages, powers, defenses
│  │  ├─ 📝 System calculates unspent points
│  │  │   - and displays available points by category
│  │  └─ 📝 ~3 more stories
│  │
│  └─ ⚙️ **Validate Prerequisites** (~6 stories)
│     ├─ 📝 System validates advantage prerequisites
│     │   - Checks required abilities, skills, powers, advantages
│     ├─ 📝 System validates power prerequisites
│     │   - Checks required effects or descriptors
│     └─ 📝 ~4 more stories
│
└─ 🎯 **Persist Character Data** (PARTIAL - 2 of 4 features)
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
   └─ ⚙️ **Load Character** (~5 stories)
      ├─ 📝 User loads character from storage
      │   - and system populates all character fields
      ├─ 📝 User loads character from previous version
      │   - and system restores historical state
      └─ 📝 ~3 more stories

**Total Stories**: ~72 stories

---

## Value Increment 2: Powers & Combat - NEXT
**Priority**: NEXT
**Relative Size**: Compared to Increment 1 (slightly larger - complex power system)
**Description**: Add power building system and attack management, enabling users to create powered characters with combat capabilities.

│
├─ 🎯 **Create Character** (PARTIAL - 2 of 8 features, completing epic)
│  │
│  ├─ ⚙️ **Build Powers** (~18 stories)
│  │  ├─ 📝 User selects base power effect
│  │  │   - and system displays base cost and available modifiers
│  │  ├─ 📝 User adds extra to power
│  │  │   - and system increases power cost
│  │  ├─ 📝 User adds flaw to power
│  │  │   - and system decreases power cost
│  │  └─ 📝 ~15 more stories
│  │
│  └─ ⚙️ **Calculate Defenses** (~6 stories)
│     ├─ 📝 System calculates dodge defense
│     │   - Based on ability modifier and purchased ranks
│     ├─ 📝 System calculates toughness defense
│     │   - Based on ability modifier only
│     ├─ 📝 User purchases defense ranks
│     │   - and system updates defense value and point cost
│     └─ 📝 ~3 more stories
│
├─ 🎯 **Manage Attacks** (6 features, ~45 stories)
│  │
│  ├─ ⚙️ **Create Standard Attacks** (~8 stories)
│  │  ├─ 📝 User creates close combat attack
│  │  │   - and system calculates attack bonus from ability
│  │  ├─ 📝 User creates ranged combat attack
│  │  │   - and system calculates attack bonus from ability
│  │  ├─ 📝 User sets attack damage value
│  │  │   - and system validates against power level limits
│  │  └─ 📝 ~5 more stories
│  │
│  ├─ ⚙️ **Create Power Attacks** (~9 stories)
│  │  ├─ 📝 User creates attack from damaging power
│  │  │   - and system derives attack bonus and damage from power
│  │  ├─ 📝 User creates attack from affliction power
│  │  │   - and system sets resistance check and conditions
│  │  ├─ 📝 System validates power attack against PL limits
│  │  │   - Checks attack + damage vs trade-off rules
│  │  └─ 📝 ~6 more stories
│  │
│  ├─ ⚙️ **Apply Attack Modifiers** (~7 stories)
│  │  ├─ 📝 User applies circumstance modifier
│  │  │   - and system adjusts attack bonus
│  │  ├─ 📝 User applies power attack trade-off
│  │  │   - and system decreases attack, increases damage
│  │  └─ 📝 ~5 more stories
│  │
│  └─ ⚙️ ~3 more features
│
└─ 🎯 **Validate Character** (PARTIAL - 1 of 5 features, continuing epic)
   │
   └─ ⚙️ **Validate Power Level Limits** (~7 stories)
      ├─ 📝 System validates attack + damage vs PL cap
      │   - Flags attacks exceeding PL × 2
      ├─ 📝 System validates dodge + toughness vs PL cap
      │   - Flags defenses exceeding PL × 2
      ├─ 📝 System validates ability scores vs PL
      │   - Flags abilities exceeding PL + 10
      └─ 📝 ~4 more stories

**Total Stories**: ~83 stories

---

## Value Increment 3: Equipment & Export - NEXT
**Priority**: NEXT
**Relative Size**: Compared to Increment 1 (smaller - mostly catalog-driven)
**Description**: Add equipment system and character export capabilities, enabling users to equip characters and share them with others.

│
├─ 🎯 **Manage Equipment** (7 features, ~35 stories)
│  │
│  ├─ ⚙️ **Select Standard Equipment** (~6 stories)
│  │  ├─ 📝 User selects equipment from catalog
│  │  │   - and system deducts equipment points
│  │  ├─ 📝 User removes equipment from character
│  │  │   - and system refunds equipment points
│  │  └─ 📝 ~4 more stories
│  │
│  ├─ ⚙️ **Create Custom Equipment** (~7 stories)
│  │  ├─ 📝 User defines custom equipment properties
│  │  │   - and system calculates equipment point cost
│  │  ├─ 📝 User adds features to custom equipment
│  │  │   - and system updates total cost
│  │  └─ 📝 ~5 more stories
│  │
│  └─ ⚙️ ~5 more features
│
└─ 🎯 **Persist Character Data** (PARTIAL - 1 of 4 features, completing epic)
   │
   └─ ⚙️ **Export Character** (~7 stories)
      ├─ 📝 User exports character as PDF
      │   - and system generates formatted character sheet
      ├─ 📝 User exports character as JSON
      │   - and system serializes all character data
      ├─ 📝 User exports character for virtual tabletop
      │   - and system formats for specific VTT platform
      └─ 📝 ~4 more stories

**Total Stories**: ~42 stories

---

## Value Increment 4: User Experience Polish - LATER
**Priority**: LATER
**Relative Size**: Compared to Increment 1 (smaller - UI enhancements)
**Description**: Enhance user experience with guidance, navigation, and progress visualization features.

│
└─ 🎯 **Support User Experience** (6 features, ~32 stories)
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

**Total Stories**: ~32 stories

---

## Increment Summary

| Increment | Priority | Features | Stories | Relative Size |
|-----------|----------|----------|---------|---------------|
| Core Character Creation | NOW | 8 features (partial) | ~72 | Medium (baseline) |
| Powers & Combat | NEXT | 9 features | ~83 | Larger (complex) |
| Equipment & Export | NEXT | 8 features | ~42 | Smaller (catalog) |
| User Experience Polish | LATER | 6 features | ~32 | Smaller (UI) |
| **TOTAL** | | **31 features** | **~229 stories** | |

---

## Notes

### Increment Planning Principles
- **Partial Epics**: Increments can contain partial epics/features
- **Delivery Priority**: NOW = immediate value, NEXT = planned, LATER = future consideration
- **Relative Sizing**: Compare against similar previously delivered work or baseline increment
- **Story Counts**: Use (~X stories) for unexplored areas during shaping
- **Exhaustive Discovery**: Full story enumeration happens during Discovery phase for increment in focus

### Value Increment Rationale
1. **Core Character Creation (NOW)**: Establishes foundation - users can create, save, and validate basic characters
2. **Powers & Combat (NEXT)**: Adds superhero differentiation - users can build unique powered heroes
3. **Equipment & Export (NEXT)**: Enables sharing and gameplay integration - users can equip and export characters
4. **User Experience Polish (LATER)**: Enhances usability - users get better guidance and visualization

---

## Source Material

**Primary Source**: Mutants & Masterminds 3rd Edition - Hero's Handbook
- Location: `demo/mm3e/HeroesHandbook.pdf`
- Sections Referenced: 
  - Chapter 1: Character Creation (pages 16-28) - Overall workflow
  - Chapter 2: Abilities (pages 29-33) - Point costs and calculations
  - Chapter 3: Skills (pages 34-63) - Skill system and training rules
  - Chapter 4: Advantages (pages 64-77) - Prerequisites and ranked advantages
  - Chapter 5: Powers (pages 78-147) - Power effects, extras, flaws
  - Chapter 6: Gadgets & Gear (pages 148-167) - Equipment system
  - Chapter 7: Combat (pages 168-187) - Attack calculations and PL limits
- Date Generated: November 12, 2025

**Context for Discovery**: When proceeding to Discovery phase, reference the same source material (Hero's Handbook PDF) and sections to elaborate stories. Prioritize Increment 1 (Core Character Creation) for exhaustive decomposition. Focus on:
- Detailed point cost formulas and edge cases
- Validation rules for each character element
- Prerequisite checking algorithms
- User interaction flows and error handling

