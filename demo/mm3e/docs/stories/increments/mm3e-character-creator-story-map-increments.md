# Story Map Increments: MM3E Online Character Creator

**Navigation:** [📋 Story Map](../map/mm3e-character-creator-story-map.md)

**File Name**: `mm3e-character-creator-story-map-increments.md`
**Location**: `demo/mm3e/docs/stories/increments/mm3e-character-creator-story-map-increments.md`

> **CRITICAL MARKDOWN FORMATTING**: All tree structure lines MUST end with TWO SPACES (  ) for proper line breaks. Without two spaces, markdown will wrap lines together into one long line, breaking the visual tree structure.

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## 🚀 **Value Increment 1: Minimal Playable Character (Walking Skeleton) - NOW**

**Relative Size**: Compared to typical character sheet web applications, this represents the bare minimum end-to-end flow to create and persist a legal M&M 3E character.

**End-to-End Flow**: User can select power level → configure 8 abilities → system calculates 5 defenses → purchase defense ranks → save character → load saved character. This is a THIN but COMPLETE vertical slice through the entire character creation workflow.

**Discovery Status**: ✅ **EXHAUSTIVE DECOMPOSITION COMPLETE** (100% stories identified)

**Epics and Features**:

🎯 **Establish Character Foundation** (PARTIAL - 3 of 5 features)  
│  
├─ [⚙️ **Enter Basic Identity**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Enter%20Basic%20Identity/%E2%9A%99%EF%B8%8F%20Enter%20Basic%20Identity%20-%20Feature%20Overview.md)   
│  ├─ 📝 User enters character name  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system validates uniqueness against saved characters  
│  └─ 📝 User enters identity fields  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - hero identity and description with basic text validation  
│  
├─ [⚙️ **Select Power Level**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Select%20Power%20Level/%E2%9A%99%EF%B8%8F%20Select%20Power%20Level%20-%20Feature%20Overview.md)   
│  ├─ 📝 System displays power level options  
│  │ &nbsp;&nbsp;&nbsp; - PL 8, 10, 12, 14 in dropdown  
│  ├─ 📝 User selects power level  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system calculates starting power points (PL × 15)  
│  ├─ 📝 System displays point budget  
│  │ &nbsp;&nbsp;&nbsp; - showing total available points  
│  ├─ 📝 System displays power level caps summary  
│  │ &nbsp;&nbsp;&nbsp; - 6 cap types: skill mod, attack+effect, 3 defense pairs  
│  └─ 📝 System stores selected power level  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - as character foundation  
│  
└─ [⚙️ **Configure Abilities**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Configure%20Abilities/%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)   
   ├─ 📝 User sets ability rank for any of 8 abilities  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system calculates point cost (rank × 2)  
   ├─ 📝 System displays all 8 abilities with current ranks  
   │ &nbsp;&nbsp;&nbsp; - STR, STA, AGL, DEX, FGT, INT, AWE, PRE  
   ├─ 📝 System calculates total ability points spent  
   │ &nbsp;&nbsp;&nbsp; - sum of all ability costs  
   ├─ 📝 System updates remaining point budget  
   │ &nbsp;&nbsp;&nbsp; - total points - spent points  
   └─ 📝 System updates dependent defenses when linked ability changes  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- AGL→Dodge, FGT→Parry, STA→Fortitude+Toughness, AWE→Will  

🎯 **Establish Character Foundation** (PARTIAL - continued)  
│  
├─ [⚙️ **Calculate Defenses**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Calculate%20Defenses/%E2%9A%99%EF%B8%8F%20Calculate%20Defenses%20-%20Feature%20Overview.md)   
│  ├─ 📝 System calculates active defenses from abilities  
│  │ &nbsp;&nbsp;&nbsp; - Dodge (10 + Agility), Parry (10 + Fighting)  
│  ├─ 📝 System calculates resistance defenses from abilities  
│  │ &nbsp;&nbsp;&nbsp; - Fortitude (Stamina), Will (Awareness), Toughness (Stamina)  
│  └─ 📝 System displays all 5 defense values  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - showing base calculation breakdown  
│  
└─ [⚙️ **Purchase Defense Ranks**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Purchase%20Defense%20Ranks/%E2%9A%99%EF%B8%8F%20Purchase%20Defense%20Ranks%20-%20Feature%20Overview.md)   
   └─ 📝 User purchases additional defense ranks  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system adds to base value (Dodge, Parry, Fortitude, Will only), deducts cost (1 pp/rank), prevents Toughness purchase  

🎯 **Manage Characters** (PARTIAL - 2 of 5 features)  
│  
├─ [⚙️ **Save Character**](../map/%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Save%20Character/%E2%9A%99%EF%B8%8F%20Save%20Character%20-%20Feature%20Overview.md)   
│  ├─ 📝 User saves new character to cloud storage  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system creates new record  
│  ├─ 📝 User saves existing character to cloud storage  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system updates record  
│  ├─ 📝 System displays save status  
│  │ &nbsp;&nbsp;&nbsp; - "Saving...", "Saved", with timestamp  
│  └─ 📝 System handles save errors gracefully  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - network errors, auth errors with retry option  
│  
└─ [⚙️ **Load Character**](../map/%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Load%20Character/%E2%9A%99%EF%B8%8F%20Load%20Character%20-%20Feature%20Overview.md)   
   ├─ 📝 User loads saved character from list  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system fetches character data  
   ├─ 📝 System restores all ability ranks  
   │ &nbsp;&nbsp;&nbsp; - repopulating 8 ability fields  
   ├─ 📝 System recalculates all derived values  
   │ &nbsp;&nbsp;&nbsp; - defenses, point totals, budget  
   └─ 📝 System validates loaded data integrity  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- checking for corrupt or missing data, displaying errors if found  

**Total Stories**: **24 stories** across 7 partial features (100% identified, +2 from estimate)

**Consolidation Decisions Applied**:
- **Abilities**: Consolidated cost calculation (same formula: rank × 2 for all 8 abilities)
- **Defenses**: Consolidated by type - Active (Dodge, Parry) vs Resistance (Fortitude, Will, Toughness)
- **Defense Purchases**: Single story covers all 4 purchasable defenses + Toughness prevention
- **Save Operations**: Split into create vs update (different database operations)
- **Identity Fields**: Consolidated hero identity + description (same validation pattern)

**Why This Increment**: Delivers minimal end-to-end capability. User can create a valid character with PL, all 8 abilities, all 5 defenses with purchasing, and PERSIST it (create/update/load). Everything calculated correctly with dependencies. Can demo complete walking skeleton flow.

---

## 🚀 **Value Increment 2: Add Skills and Basic Validation - NEXT**

**Relative Size**: Similar to adding a secondary attribute system to a character builder. Adds skill purchasing and introduces validation warnings.

**End-to-End Flow**: Builds on Increment 1. User can now purchase skills → system calculates bonuses from abilities → validates skill modifiers against PL caps → displays warnings (but allows save). Adds BREADTH (skills) and DEPTH (validation) to existing end-to-end flow.

**Epics and Features**:

🎯 **Build Character Skills** (PARTIAL - 2 of 4 features)  
│  
├─ ⚙️ **Purchase Skill Ranks** (6 of ~8 stories)  
│  ├─ 📝 User increases skill rank  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system calculates point cost (0.5 per rank)  
│  ├─ 📝 System calculates skill bonus from linked ability  
│  ├─ 📝 System displays skill total (ability + skill rank)  
│  ├─ 📝 User decreases skill rank  
│  ├─ 📝 System calculates total skill points spent  
│  └─ 📝 System updates remaining point budget  
│  
└─ ⚙️ **Update Skills When Ability Changes** (3 of ~5 stories)  
   ├─ 📝 System recalculates all linked skill bonuses when ability changes  
   ├─ 📝 System displays updated skill totals in real-time  
   └─ 📝 System updates validation warnings when skill modifiers change  

🎯 **Validate Character** (PARTIAL - 3 of 5 features)  
│  
├─ ⚙️ **Calculate Point Totals** (4 of ~6 stories)  
│  ├─ 📝 System calculates total points spent  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and displays by category (abilities, skills, defenses)  
│  ├─ 📝 System displays remaining unspent points  
│  ├─ 📝 System updates point totals in real-time  
│  └─ 📝 System displays point budget progress indicator  
│  
├─ ⚙️ **Validate Power Level Caps** (3 of ~7 stories)  
│  ├─ 📝 System validates skill modifiers ≤ PL + 10  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and displays warning if exceeded  
│  ├─ 📝 System validates Dodge + Toughness ≤ PL × 2  
│  └─ 📝 System validates Fortitude + Will ≤ PL × 2  
│  
└─ ⚙️ **Allow Save Despite Warnings** (2 of ~3 stories)  
   ├─ 📝 System allows save with validation warnings present  
   │ &nbsp;&nbsp;&nbsp; - displaying "Warn Don't Prevent" message  
   └─ 📝 System saves warnings with character for review  

🎯 **Manage Characters** (PARTIAL - enhancement)  
│  
└─ [⚙️ **Save Character**](../map/%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Save%20Character/%E2%9A%99%EF%B8%8F%20Save%20Character%20-%20Feature%20Overview.md)   
   └─ 📝 System saves validation warnings with character  

**Total Estimated Stories**: ~19 stories across 5 partial features  
**Why This Increment**: Adds skills (major M&M component) and validation. Still end-to-end - user can create character with abilities AND skills, see validation warnings, save with warnings. Builds on walking skeleton.

---

## 🚀 **Value Increment 3: Add Advantages and Enhanced Validation - NEXT**

**Relative Size**: Similar complexity to skills. Adds minor benefits system and completes validation coverage.

**End-to-End Flow**: Builds on Increments 1 & 2. User can now select advantages (with prerequisites) → system validates all PL caps → displays comprehensive validation → saves complete character state. Adds MORE BREADTH (advantages) and MORE DEPTH (complete validation).

**Epics and Features**:

🎯 **Configure Advantages** (ALL - 4 of 4 features)  
│  
├─ ⚙️ **Select Standard Advantages** (6 stories)  
│  ├─ 📝 User selects advantage  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system adds to character and deducts 1 point  
│  ├─ 📝 System displays advantage list organized by type  
│  ├─ 📝 User searches advantages by name  
│  ├─ 📝 User filters advantages by type (Combat, Fortune, General, Skill)  
│  ├─ 📝 System calculates total advantage points spent  
│  └─ 📝 System displays advantage descriptions  
│  
├─ ⚙️ **Select Ranked Advantages** (5 stories)  
│  ├─ 📝 User selects ranked advantage  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system prompts for rank count  
│  ├─ 📝 System calculates cost (1 point per rank)  
│  ├─ 📝 User adjusts advantage ranks  
│  ├─ 📝 System displays examples of ranked advantages (Equipment, Benefit)  
│  └─ 📝 User removes ranked advantage  
│  
├─ ⚙️ **Validate Prerequisites** (3 stories)  
│  ├─ 📝 System validates advantage prerequisites  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and displays warning if not met  
│  ├─ 📝 System displays prerequisite requirements before selection  
│  └─ 📝 System allows selection despite unmet prerequisites (warn don't prevent)  
│  
└─ ⚙️ **Manage Advantage List** (3 stories)  
   ├─ 📝 User removes advantage  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system refunds points  
   ├─ 📝 System updates point budget when removing advantage  
   └─ 📝 User views selected advantages summary  

🎯 **Build Character Skills** (PARTIAL - 1 of 4 features)  
│  
└─ ⚙️ **Manage Skill Organization** (6 stories)  
   ├─ 📝 System groups skills by linked ability  
   ├─ 📝 User searches skills by name  
   ├─ 📝 User filters trained vs untrained skills  
   ├─ 📝 System displays skill count by category  
   ├─ 📝 User sorts skills alphabetically or by bonus  
   └─ 📝 System displays untrained use indicators  

🎯 **Validate Character** (PARTIAL - completing remaining)  
│  
├─ ⚙️ **Calculate Point Totals** (2 more of ~6 stories)  
│  ├─ 📝 System includes advantages in point breakdown  
│  └─ 📝 System displays all categories (abilities, skills, advantages, defenses)  
│  
├─ ⚙️ **Validate Power Level Caps** (4 more of ~7 stories)  
│  ├─ 📝 System validates Parry + Toughness ≤ PL × 2  
│  ├─ 📝 System displays all PL cap validations together  
│  ├─ 📝 System highlights exceeded caps in red  
│  └─ 📝 System explains PL cap formulas in tooltips  
│  
├─ ⚙️ **Validate Point Budget** (3 of ~5 stories)  
│  ├─ 📝 System validates total spent ≤ starting points  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and displays overspend warning if exceeded  
│  ├─ 📝 System displays overspend amount  
│  └─ 📝 System allows save despite overspend (warn don't prevent)  
│  
└─ ⚙️ **Display Validation Warnings** (4 stories)  
   ├─ 📝 System displays validation warnings  
   │ &nbsp;&nbsp;&nbsp; - grouped by category (PL caps, budget, prerequisites)  
   ├─ 📝 System displays warning count badge  
   ├─ 📝 User expands/collapses warning categories  
   └─ 📝 System clears warnings when issues resolved  

**Total Estimated Stories**: ~36 stories across 9 partial features  
**Why This Increment**: Completes non-power character creation. User can create full character with abilities, skills, advantages, see all validation, save complete state. Still end-to-end. Can play "non-powered" hero archetypes (Crime Fighter, Martial Artist).

---

## 🚀 **Value Increment 4: Add Powers (Complex System) - NEXT**

**Relative Size**: Largest increment due to power system complexity (effects, modifiers, arrays). Comparable to adding spell/ability systems in other RPGs.

**End-to-End Flow**: Builds on Increments 1-3. User can now create power effects → apply modifiers → validate effect ranks → save powered characters. Adds MOST COMPLEXITY but still end-to-end flow.

**Epics and Features**:

🎯 **Build Character Powers** (ALL - 6 of 6 features)  
│  
├─ ⚙️ **Select Power Effects** (7 stories)  
│  ├─ 📝 User selects base power effect  
│  ├─ 📝 User sets effect rank  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system calculates base cost (cost per rank × rank)  
│  ├─ 📝 System displays effect catalog organized by type  
│  ├─ 📝 User searches effects by name  
│  ├─ 📝 System displays effect descriptions and examples  
│  ├─ 📝 System calculates total power points spent  
│  └─ 📝 System updates remaining point budget  
│  
├─ ⚙️ **Apply Power Extras** (6 stories)  
│  ├─ 📝 User adds Extra modifier to effect  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system increases cost per rank  
│  ├─ 📝 System recalculates effect total cost  
│  ├─ 📝 System displays available Extras for effect type  
│  ├─ 📝 User removes Extra modifier  
│  ├─ 📝 System validates Extra compatibility with effect  
│  └─ 📝 System displays Extra descriptions  
│  
├─ ⚙️ **Apply Power Flaws** (6 stories)  
│  ├─ 📝 User adds Flaw modifier to effect  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system decreases cost per rank  
│  ├─ 📝 System recalculates effect total cost  
│  ├─ 📝 System displays available Flaws for effect type  
│  ├─ 📝 User removes Flaw modifier  
│  ├─ 📝 System validates Flaw compatibility with effect  
│  └─ 📝 System displays Flaw descriptions  
│  
├─ ⚙️ **Create Power Arrays** (6 stories)  
│  ├─ 📝 User creates power array  
│  ├─ 📝 User adds alternate effect to array  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system charges 1 point per alternate  
│  ├─ 📝 System calculates array total cost (base + alternates)  
│  ├─ 📝 User removes alternate effect  
│  ├─ 📝 System validates alternate effects ≤ base effect cost  
│  └─ 📝 System displays array structure visually  
│  
├─ ⚙️ **Validate Power Limits** (5 stories)  
│  ├─ 📝 System validates effect rank against PL caps  
│  ├─ 📝 System validates attack effect rank ≤ PL  
│  ├─ 📝 System validates resistance effect rank ≤ PL  
│  ├─ 📝 System displays power validation warnings  
│  └─ 📝 System allows save despite power warnings (warn don't prevent)  
│  
└─ ⚙️ **Manage Power List** (5 stories)  
   ├─ 📝 User removes power effect  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system refunds points  
   ├─ 📝 System updates point budget when removing power  
   ├─ 📝 User duplicates power effect  
   ├─ 📝 User renames custom powers  
   └─ 📝 System displays powers organized by category  

🎯 **Validate Character** (PARTIAL - enhancement)  
│  
├─ ⚙️ **Calculate Point Totals** (1 more story)  
│  └─ 📝 System includes powers in point breakdown  
│  
└─ ⚙️ **Validate Power Level Caps** (1 more story)  
   └─ 📝 System validates Attack bonus + Effect rank ≤ PL × 2  

**Total Estimated Stories**: ~36 stories across 7 partial features  
**Why This Increment**: Completes full character creation system. User can create ANY M&M 3E character including powered heroes. Still end-to-end - create, configure, validate, save. Most complex increment but builds on solid foundation from Increments 1-3.

---

## 🚀 **Value Increment 5: Add Complications and Character Management - LATER**

**Relative Size**: Smaller increment focused on rounding out character creation and list management.

**End-to-End Flow**: Adds complications (earn hero points) and completes character management (list, delete, duplicate, auto-save).

**Epics and Features**:

🎯 **Establish Character Foundation** (REMAINING - 1 of 5 features)  
│  
└─ [⚙️ **Enter Basic Identity**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Enter%20Basic%20Identity/%E2%9A%99%EF%B8%8F%20Enter%20Basic%20Identity%20-%20Feature%20Overview.md)   
   ├─ 📝 User enters real name  
   └─ 📝 User enters character description  

🎯 **Establish Character Foundation** (REMAINING - 1 of 5 features)  
│  
└─ [⚙️ **Purchase Defense Ranks**](../map/%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Purchase%20Defense%20Ranks/%E2%9A%99%EF%B8%8F%20Purchase%20Defense%20Ranks%20-%20Feature%20Overview.md)   
   ├─ 📝 System displays defense purchase cost  
   └─ 📝 User resets defense ranks to base value  

🎯 **Configure Complications** (ALL - 3 of 3 features)  
│  
├─ ⚙️ **Select Complication Types** (5 stories)  
│  ├─ 📝 User selects complication type  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system prompts for description  
│  ├─ 📝 System displays complication type list (Motivation, Identity, Relationship, etc.)  
│  ├─ 📝 User enters complication description  
│  ├─ 📝 System displays complication examples  
│  └─ 📝 User selects multiple complications  
│  
├─ ⚙️ **Manage Complication List** (4 stories)  
│  ├─ 📝 User removes complication  
│  ├─ 📝 User edits complication description  
│  ├─ 📝 System displays complication count (recommend 2+)  
│  └─ 📝 System displays selected complications summary  
│  
└─ ⚙️ **Display Complication Reminders** (3 stories)  
   ├─ 📝 System displays complication reminders on character sheet  
   ├─ 📝 System highlights complications during gameplay  
   └─ 📝 User views complication descriptions in tooltips  

🎯 **Build Character Skills** (REMAINING - 1 of 4 features)  
│  
└─ ⚙️ **Validate Skill Limits** (6 stories)  
   ├─ 📝 System validates skill modifier against PL cap (PL + 10)  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and displays warning if exceeded  
   ├─ 📝 System displays skill cap formula in tooltip  
   ├─ 📝 System highlights skills exceeding cap  
   ├─ 📝 System validates skills when PL changes  
   ├─ 📝 System validates skills when abilities change  
   └─ 📝 System allows exceeding cap with warning (warn don't prevent)  

🎯 **Validate Character** (REMAINING - 1 of 5 features)  
│  
└─ ⚙️ **Validate Point Budget** (2 more of ~5 stories)  
   ├─ 📝 System displays point budget history  
   └─ 📝 System shows point allocation suggestions when under budget  

🎯 **Manage Characters** (REMAINING - 3 of 5 features)  
│  
├─ [⚙️ **Save Character**](../map/%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Save%20Character/%E2%9A%99%EF%B8%8F%20Save%20Character%20-%20Feature%20Overview.md)   
│  └─ 📝 System auto-saves periodically  
│  
├─ [⚙️ **Load Character**](../map/%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Load%20Character/%E2%9A%99%EF%B8%8F%20Load%20Character%20-%20Feature%20Overview.md)   
│  ├─ 📝 System displays load errors  
│  └─ 📝 System restores UI state from saved character  
│  
├─ ⚙️ **List Characters** (5 stories)  
│  ├─ 📝 User views character list  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system displays name, PL, and last modified  
│  ├─ 📝 User sorts character list  
│  ├─ 📝 User filters character list by PL  
│  ├─ 📝 User searches characters by name  
│  └─ 📝 System displays character count  
│  
├─ ⚙️ **Delete Character** (4 stories)  
│  ├─ 📝 User deletes character  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system confirms before removing  
│  ├─ 📝 System displays delete confirmation dialog  
│  ├─ 📝 System removes character from list  
│  └─ 📝 System handles delete errors gracefully  
│  
└─ ⚙️ **Duplicate Character** (4 stories)  
   ├─ 📝 User duplicates character  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system creates copy with "(Copy)" suffix  
   ├─ 📝 System generates unique name for duplicate  
   ├─ 📝 System copies all character data  
   └─ 📝 System opens duplicated character for editing  

**Total Estimated Stories**: ~38 stories across 11 partial features  
**Why This Increment**: Rounds out character creation and management. Adds complications for hero point earning. Completes list/delete/duplicate operations. Auto-save for convenience.

---

## 🚀 **Value Increment 6: Export and Gameplay Support - LATER**

**Relative Size**: Adds PDF export and session-time gameplay tracking features.

**End-to-End Flow**: Export characters to PDF matching handbook format. Track hero points, conditions, damage during gameplay.

**Epics and Features**:

🎯 **Export Characters** (ALL - 4 of 4 features)  
│  
├─ ⚙️ **Export Character Sheet** (6 stories)  
│  ├─ 📝 User exports character to PDF  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system generates formatted sheet matching handbook layout  
│  ├─ 📝 System formats abilities section  
│  ├─ 📝 System formats skills section  
│  ├─ 📝 System formats powers section  
│  ├─ 📝 System formats complications section  
│  └─ 📝 System includes all calculated values  
│  
├─ ⚙️ **Print Character Sheet** (5 stories)  
│  ├─ 📝 User prints character sheet  
│  ├─ 📝 System formats for print layout  
│  ├─ 📝 System includes print-friendly styling  
│  ├─ 📝 User previews before printing  
│  └─ 📝 System handles multi-page characters  
│  
├─ ⚙️ **Share Character** (4 stories)  
│  ├─ 📝 User generates share link  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system creates public URL  
│  ├─ 📝 System displays shareable link  
│  ├─ 📝 User copies link to clipboard  
│  └─ 📝 System displays shared character as read-only  
│  
└─ ⚙️ **Import Character** (3 stories)  
   ├─ 📝 User imports character from file  
   ├─ 📝 System validates import data  
   └─ 📝 System adds imported character to list  

🎯 **Support Gameplay** (ALL - 4 of 4 features)  
│  
├─ ⚙️ **Track Hero Points** (5 stories)  
│  ├─ 📝 User adjusts hero points  
│  ├─ 📝 System displays current hero points  
│  ├─ 📝 User resets hero points to maximum (1 per session)  
│  ├─ 📝 System tracks hero point usage history  
│  └─ 📝 User adds notes to hero point changes  
│  
├─ ⚙️ **Track Conditions** (6 stories)  
│  ├─ 📝 User applies condition to character  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system displays condition effects  
│  ├─ 📝 User removes condition  
│  ├─ 📝 System displays active conditions list  
│  ├─ 📝 System calculates penalties from conditions  
│  ├─ 📝 User adds custom condition  
│  └─ 📝 System validates condition compatibility  
│  
├─ ⚙️ **Track Damage** (5 stories)  
│  ├─ 📝 User records damage penalty  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system applies to relevant checks  
│  ├─ 📝 User clears damage penalties  
│  ├─ 📝 System displays current damage level  
│  ├─ 📝 System calculates effects on abilities  
│  └─ 📝 User applies recovery  
│  
└─ ⚙️ **Roll Checks** (4 stories)  
   ├─ 📝 User rolls d20 for check  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system adds modifiers and displays total  
   ├─ 📝 System displays roll breakdown  
   ├─ 📝 User selects check type (skill, attack, save)  
   └─ 📝 System highlights critical success or failure  

**Total Estimated Stories**: ~38 stories across 8 features  
**Why This Increment**: Completes system with export/print (for table play) and gameplay tracking (for online sessions). Both are "nice to have" after core creation system is solid.

---

## Source Material

**Primary Source**: M&M 3E Heroes Handbook (demo/mm3e/HeroesHandbook.pdf)
- Location: Extracted to `demo/mm3e/docs/mm3e-handbook-reference.txt` (27,362 lines, 321 pages)
- Domain Concepts: Documented in `demo/mm3e/docs/mm3e-domain-concepts.md`
- Key Sections Referenced:
  - Chapter 2: Secret Origins (Character Creation) - Pages 23-54
  - Chapter 3: Abilities - Pages 107-112
  - Chapter 4: Skills - Pages 113-131
  - Chapter 5: Advantages - Pages 132-142
  - Chapter 6: Powers - Pages 143+
  - Basic Trait Costs Table - Page 26
  - Power Level Limits - Pages 26-27
  - Character Examples (The Rook, Princess) - Pages 51-54
- Date Generated: Thursday, November 13, 2025

**Increment Design Philosophy**:
This increment organization follows **Principle 1.7.1: End-to-End Value Increments (Vertical Slices)**. Each increment delivers a COMPLETE end-to-end flow (thin but working) rather than completing one feature at a time (horizontal layers). 

- **Increment 1**: Minimal playable - PL, abilities, defenses, save/load (walking skeleton)
- **Increment 2**: Add skills and validation (build on skeleton, add breadth+depth)
- **Increment 3**: Add advantages and complete validation (more breadth+depth)
- **Increment 4**: Add powers (most complex, but still builds on solid foundation)
- **Increment 5**: Round out with complications and management
- **Increment 6**: Export and gameplay support

Each increment touches multiple epics/features and delivers independently usable/demonstrable capability.

**Discovery Refinements**: Friday, November 13, 2025
- **Increment in Focus**: Increment 1 - Minimal Playable Character (Walking Skeleton)
- **Additional Sections Referenced**: 
  - Chapter 3: Abilities (pages 107-112) - All 8 ability definitions and dependencies
  - Defense mechanics (pages 110-111) - Active vs Resistance defense formulas
  - Point costs table (page 26) - Confirmed ability cost (2 pp/rank), defense cost (1 pp/rank)
- **Areas Elaborated**: 
  - All 7 features in Increment 1 exhaustively decomposed (24 stories total)
  - Ability-to-defense dependency mappings documented
  - Defense calculation patterns identified (active: 10+ability, resistance: ability only)
  - Save/load operations split into create vs update flows
- **Consolidation Decisions**:
  - Consolidated: Ability cost calculations (same formula for all 8)
  - Consolidated: Defense calculations by type (active vs resistance patterns)
  - Consolidated: Defense rank purchasing (same operation for all 4 purchasable)
  - Consolidated: Identity fields with same validation pattern
  - Split: Save create vs update (different database operations)
  - Confirmed: Active defenses (Dodge, Parry) = 10 + ability (opponent rolls against)
  - Confirmed: Resistance defenses (Fortitude, Will, Toughness) = ability only (you roll with them + d20)

**Context for Exploration**: When writing acceptance criteria for Increment 1, reference:
- Defense formulas and active vs resistance distinction
- Ability-to-defense cascade mappings (which abilities update which defenses)
- Point budget calculations (PL × 15 total, 2 pp/ability rank, 1 pp/defense rank)
- "Warn don't prevent" philosophy for validation (allow saves despite warnings)
- Toughness special rule (cannot purchase ranks, only improved via advantages/powers)
