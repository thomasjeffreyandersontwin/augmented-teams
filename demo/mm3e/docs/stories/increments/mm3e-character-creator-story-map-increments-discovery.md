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
**Discovery Status**: ✅ EXHAUSTIVE DECOMPOSITION COMPLETE

│
├─ 🎯 **Create Character** (PARTIAL - 4 of 8 features)
│  │
│  ├─ ⚙️ **Establish Identity** (5 stories)
│  │  ├─ 📝 User enters identity text fields
│  │  │   - and system saves name, real name, concept, description, and player name
│  │  ├─ 📝 User enters identity numeric fields
│  │  │   - and system saves age, height, and weight
│  │  ├─ 📝 User selects gender
│  │  │   - and system saves selection
│  │  ├─ 📝 User selects power level
│  │  │   - and system calculates and displays total point budget
│  │  └─ 📝 User clears identity field
│  │     - and system removes value and updates display
│  │
│  ├─ ⚙️ **Allocate Abilities** (7 stories)
│  │  ├─ 📝 User increases ability rank from current value
│  │  │   - and system calculates incremental cost (2 points/rank) and updates budget
│  │  ├─ 📝 User decreases ability rank from current value
│  │  │   - and system refunds points (2 points/rank) and updates budget
│  │  ├─ 📝 User sets ability to negative rank
│  │  │   - and system refunds points and applies negative modifier
│  │  ├─ 📝 System displays ability modifier
│  │  │   - Calculates (rank - 10) ÷ 2 rounded down
│  │  ├─ 📝 System updates defense values when ability affecting defense changes
│  │  │   - Updates dodge (Agility), toughness (Stamina), parry (Fighting), fortitude (Stamina), will (Awareness)
│  │  ├─ 📝 System updates skill modifiers when ability affecting skills changes
│  │  │   - Recalculates totals for skills linked to changed ability
│  │  └─ 📝 System updates attack bonuses when ability affecting attacks changes
│  │     - Updates close attack (Fighting, Strength damage), ranged attack (Dexterity)
│  │
│  ├─ ⚙️ **Purchase Skills** (7 stories)
│  │  ├─ 📝 User adds ranks to untrained skill
│  │  │   - and system calculates cost (0.5 points/rank) and displays total modifier
│  │  ├─ 📝 User adds ranks to trained-only skill
│  │  │   - and system validates minimum 1 rank and calculates cost (1 point/rank) and displays total modifier
│  │  ├─ 📝 User decreases skill ranks to zero on untrained skill
│  │  │   - and system refunds points and updates total
│  │  ├─ 📝 User decreases skill ranks to zero on trained-only skill
│  │  │   - and system refunds points and removes skill from display
│  │  ├─ 📝 System calculates skill total modifier
│  │  │   - Adds ability modifier + skill ranks
│  │  ├─ 📝 System groups skills by ability category
│  │  │   - Displays skills organized under their linked abilities
│  │  └─ 📝 User filters skills by training status or search term
│  │     - and system displays matching skills
│  │
│  └─ ⚙️ **Select Advantages** (14 stories)
│     ├─ 📝 User selects advantage without prerequisites
│     │   - and system adds to sheet and deducts flat cost
│     ├─ 📝 User selects ranked advantage without prerequisites
│     │   - and system prompts for rank selection and deducts cost per rank
│     ├─ 📝 User selects advantage with ability score prerequisite
│     │   - and system validates minimum ability rank and adds if valid
│     ├─ 📝 User selects advantage with skill rank prerequisite
│     │   - and system validates minimum skill rank and adds if valid
│     ├─ 📝 User selects advantage with other advantage prerequisite
│     │   - and system validates character has required advantage and adds if valid
│     ├─ 📝 User selects advantage with power prerequisite
│     │   - and system validates character has required power and adds if valid
│     ├─ 📝 User selects advantage with multiple prerequisites (AND logic)
│     │   - and system validates all requirements met and adds if valid
│     ├─ 📝 User selects advantage with alternative prerequisites (OR logic)
│     │   - and system validates at least one requirement met and adds if valid
│     ├─ 📝 User removes advantage from character
│     │   - and system refunds cost and updates budget
│     ├─ 📝 User removes ranked advantage from character
│     │   - and system prompts for removal confirmation and refunds cost based on ranks
│     ├─ 📝 User removes advantage that is prerequisite for another
│     │   - and system flags dependent advantages and prevents removal
│     ├─ 📝 User searches advantages by name
│     │   - and system filters displayed advantages
│     ├─ 📝 User filters advantages by category
│     │   - and system displays advantages matching category with category-specific effects
│     └─ 📝 System displays advantage cost
│        - Shows flat cost or per-rank cost based on advantage type
│
├─ 🎯 **Validate Character** (PARTIAL - 2 of 5 features)
│  │
│  ├─ ⚙️ **Validate Point Expenditure** (5 stories)
│  │  ├─ 📝 System validates total points at or under budget
│  │  │   - Flags overspend errors when total exceeds budget
│  │  ├─ 📝 System validates ability points at or under budget
│  │  │   - Flags overspend in abilities category with category-specific UI
│  │  ├─ 📝 System validates skill points at or under budget
│  │  │   - Flags overspend in skills category with category-specific UI
│  │  ├─ 📝 System validates advantage points at or under budget
│  │  │   - Flags overspend in advantages category with category-specific UI
│  │  └─ 📝 System calculates unspent points by category
│  │     - and displays remaining points for abilities, skills, and advantages
│  │
│  └─ ⚙️ **Validate Prerequisites** (6 stories)
│     ├─ 📝 System validates ability score prerequisites for advantages
│     │   - Checks minimum ability rank required
│     ├─ 📝 System validates skill rank prerequisites for advantages
│     │   - Checks minimum skill rank required
│     ├─ 📝 System validates other advantage prerequisites for advantages
│     │   - Checks character has required advantage
│     ├─ 📝 System validates power prerequisites for advantages
│     │   - Checks character has required power
│     ├─ 📝 System validates multiple prerequisites with AND logic
│     │   - Checks all requirements met
│     └─ 📝 System validates alternative prerequisites with OR logic
│        - Checks at least one requirement met
│
└─ 🎯 **Persist Character Data** (PARTIAL - 2 of 4 features)
   │
   ├─ ⚙️ **Save Character** (5 stories)
   │  ├─ 📝 User saves character to cloud storage
   │  │   - and system validates data completeness and creates or updates record
   │  ├─ 📝 System auto-saves character during editing
   │  │   - Saves draft every 2 minutes without user action
   │  ├─ 📝 User saves character revision with version note
   │  │   - and system creates version history entry with timestamp and note
   │  ├─ 📝 User saves character with validation errors
   │  │   - and system prevents save and displays error list
   │  └─ 📝 System indicates save status to user
   │     - Displays "Saving...", "Saved", or "Error" status
   │
   └─ ⚙️ **Load Character** (4 stories)
      ├─ 📝 User loads character from storage or version history
      │   - and system populates all character fields
      ├─ 📝 System recalculates derived values when loading character
      │   - Recalculates ability modifiers, skill totals, defense values
      ├─ 📝 System validates loaded character data integrity
      │   - Checks for missing or corrupted fields and flags errors
      └─ 📝 User loads character with invalid data
         - and system displays error message and offers repair options

**Total Stories**: 53 stories (exhaustively discovered)

**Discovery Refinement Notes**:
- 🔍 **Complex Story**: "Select Advantages" feature has 14 stories covering 80+ advantages with varying prerequisite patterns - may benefit from splitting into sub-features during exploration
- 🔍 **Ambiguous**: "System updates defense values when ability affecting defense changes" - needs clarity on which abilities affect which defenses (documented: Agility→Dodge, Stamina→Toughness/Fortitude, Fighting→Parry, Awareness→Will)
- 🔍 **Complex Story**: "User selects advantage with multiple prerequisites (AND logic)" and "OR logic" variants - need clear examples of AND vs OR prerequisite patterns during exploration
- 🔍 **Ambiguous**: "User filters advantages by category" - needs catalog of advantage categories and category-specific effect rules
- 🔍 **Integration Point**: "System recalculates derived values when loading character" - cascades to multiple systems (abilities→skills→attacks→defenses), needs careful coordination
- ⚠️ **Prerequisite Dependency**: "User removes advantage that is prerequisite for another" - complex dependency checking logic, may need additional stories for multi-level dependencies

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

| Increment | Priority | Features | Stories | Relative Size | Discovery Status |
|-----------|----------|----------|---------|---------------|------------------|
| Core Character Creation | NOW | 8 features (partial) | 53 | Medium (baseline) | ✅ Exhaustive |
| Powers & Combat | NEXT | 9 features | ~83 | Larger (complex) | Pending |
| Equipment & Export | NEXT | 8 features | ~42 | Smaller (catalog) | Pending |
| User Experience Polish | LATER | 6 features | ~32 | Smaller (UI) | Pending |
| **TOTAL** | | **31 features** | **~210 stories** | | |

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
- Sections Referenced (Shaping): 
  - Chapter 1: Character Creation (pages 16-28) - Overall workflow
  - Chapter 2: Abilities (pages 29-33) - Point costs and calculations
  - Chapter 3: Skills (pages 34-63) - Skill system and training rules
  - Chapter 4: Advantages (pages 64-77) - Prerequisites and ranked advantages
  - Chapter 5: Powers (pages 78-147) - Power effects, extras, flaws
  - Chapter 6: Gadgets & Gear (pages 148-167) - Equipment system
  - Chapter 7: Combat (pages 168-187) - Attack calculations and PL limits
- Date Generated: November 12, 2025

**Discovery Refinements**: November 12, 2025
- **Increment in Focus**: Increment 1 - Core Character Creation (NOW)
- **Additional Sections Referenced**:
  - Chapter 2: Abilities (pages 29-33) - Detailed ability modifier calculations, negative ranks, cascade update patterns
  - Chapter 3: Skills (pages 34-63) - Trained vs untrained skill distinctions, cost formulas (0.5 vs 1.0 points/rank), skill grouping by abilities
  - Chapter 4: Advantages (pages 64-77) - Exhaustive prerequisite types (ability, skill, advantage, power), AND/OR logic patterns, ranked advantages
  - Chapter 1: Character Creation (pages 16-28) - Point budget formula (15 × PL), category-based point tracking, validation rules
- **Areas Elaborated**:
  - **Establish Identity**: Consolidated text/numeric fields (5 stories from initial 10)
  - **Allocate Abilities**: Consolidated cascades by TYPE (defense, skills, attacks) resulting in 7 stories
  - **Purchase Skills**: Enumerated untrained vs trained-only permutations, cost formulas, removal behaviors (7 stories)
  - **Select Advantages**: Exhaustive prerequisite permutations across 80+ advantages (14 stories covering all validation paths)
  - **Validate Point Expenditure**: Separated category validation for UI work, consolidated calculation logic (5 stories)
  - **Validate Prerequisites**: All prerequisite types and boolean logic patterns (6 stories)
  - **Save/Load Character**: Consolidated create/update paths, version history patterns (5 + 4 stories)
- **Consolidation Decisions Applied**:
  - ✅ Consolidated same-logic fields (text inputs, numeric inputs, calculations)
  - ✅ Separated different formulas (untrained 0.5 vs trained 1.0 point costs)
  - ✅ Separated different algorithms (prerequisite types, cascade targets)
  - ✅ Kept category-specific UI work separate (validation displays per category)
  - **Result**: 53 stories (down from initial estimate of ~72)

**Context for Exploration**: When writing acceptance criteria, reference sections above for:
- Point cost formulas: 2 pts/rank (abilities), 0.5 pts/rank (untrained skills), 1 pt/rank (trained skills)
- Power level budget: 15 × PL
- Ability modifier: (rank - 10) ÷ 2 rounded down
- Cascade patterns: Defense updates, skill modifier updates, attack bonus updates
- Prerequisite validation algorithms for each type
- Category-based point tracking and validation display patterns

