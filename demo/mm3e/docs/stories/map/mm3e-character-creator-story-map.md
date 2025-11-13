# Story Map: MM3E Online Character Creator

**Navigation:** [📊 Increments](../increments/mm3e-character-creator-story-map-increments.md)

**File Name**: `mm3e-character-creator-story-map.md`
**Location**: `demo/mm3e/docs/stories/map/mm3e-character-creator-story-map.md`

> **CRITICAL MARKDOWN FORMATTING**: All tree structure lines MUST end with TWO SPACES (  ) for proper line breaks. Without two spaces, markdown will wrap lines together into one long line, breaking the visual tree structure.

## System Purpose

Enable players to create, manage, and share superhero characters for Mutants & Masterminds 3E tabletop RPG sessions. The system guides users through character creation following M&M 3E rules (handbook pages 23-54), validates character legality with "warn don't prevent" philosophy, manages point budgets with real-time calculations, and provides tools for character management during gameplay.

---

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Story Map Structure

🎯 **Establish Character Foundation** (5 features, ~30 stories)  
│  
├─ [⚙️ **Enter Basic Identity**](./%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Enter%20Basic%20Identity/%E2%9A%99%EF%B8%8F%20Enter%20Basic%20Identity%20-%20Feature%20Overview.md)  
│  ├─ 📝 User enters character name  
│  └─ 📝 User enters identity fields  
├─ │  
├─ [⚙️ **Select Power Level**](./%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Select%20Power%20Level/%E2%9A%99%EF%B8%8F%20Select%20Power%20Level%20-%20Feature%20Overview.md)  
│  ├─ 📝 System displays power level options  
│  ├─ 📝 User selects power level  
│  ├─ 📝 System displays point budget  
│  ├─ 📝 System displays power level caps summary  
│  └─ 📝 System stores selected power level  
├─ │  
├─ [⚙️ **Configure Abilities**](./%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Configure%20Abilities/%E2%9A%99%EF%B8%8F%20Configure%20Abilities%20-%20Feature%20Overview.md)   
│  ├─ 📝 User sets ability rank for any of 8 abilities  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system calculates point cost (rank × 2)  
│  ├─ 📝 System displays all 8 abilities with current ranks  
│  │ &nbsp;&nbsp;&nbsp; - STR, STA, AGL, DEX, FGT, INT, AWE, PRE  
│  ├─ 📝 System calculates total ability points spent  
│  │ &nbsp;&nbsp;&nbsp; - sum of all ability costs  
│  ├─ 📝 System updates remaining point budget  
│  │ &nbsp;&nbsp;&nbsp; - total points - spent points  
│  └─ 📝 System updates dependent defenses when linked ability changes  
│ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - AGL→Dodge, FGT→Parry, STA→Fortitude+Toughness, AWE→Will  
│  
├─ [⚙️ **Calculate Defenses**](./%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Calculate%20Defenses/%E2%9A%99%EF%B8%8F%20Calculate%20Defenses%20-%20Feature%20Overview.md)  
│  ├─ 📝 System calculates active defenses from abilities  
│  ├─ 📝 System calculates resistance defenses from abilities  
│  └─ 📝 System displays all 5 defense values  
├─ │  
└─ [⚙️ **Purchase Defense Ranks**](./%F0%9F%8E%AF%20Establish%20Character%20Foundation/%E2%9A%99%EF%B8%8F%20Purchase%20Defense%20Ranks/%E2%9A%99%EF%B8%8F%20Purchase%20Defense%20Ranks%20-%20Feature%20Overview.md)   
   └─ 📝 User purchases additional defense ranks  
       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system adds to base value (Dodge, Parry, Fortitude, Will only), deducts cost (1 pp/rank), prevents Toughness purchase  

🎯 **Build Character Skills** (4 features, ~25 stories)  
│  
├─ ⚙️ **Purchase Skill Ranks** (6 stories)  
│  ├─ 📝 User increases skill rank  
│  ├─ 📝 System calculates skill bonus from linked ability  
│  ├─ 📝 System displays skill total (ability + skill rank)  
│  ├─ 📝 User decreases skill rank  
│  ├─ 📝 System calculates total skill points spent  
│  └─ 📝 System updates remaining point budget  
├─ │  
├─ ⚙️ **Manage Skill Organization** (~6 stories)  
│  ├─ 📝 System groups skills by linked ability  
│  ├─ 📝 User searches skills by name  
│  ├─ 📝 User filters trained vs untrained skills  
│  └─ 📝 ~3 more stories  
│  
├─ ⚙️ **Validate Skill Limits** (~6 stories)  
│  ├─ 📝 System validates skill modifier against PL cap (PL + 10)  
│  │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and displays warning if exceeded  
│  └─ 📝 ~5 more stories  
│  
└─ ⚙️ **Update Skills When Ability Changes** (~5 stories)  
   ├─ 📝 System recalculates all linked skill bonuses when ability changes  
   └─ 📝 ~4 more stories  

🎯 **Configure Advantages** (4 features, ~20 stories)  
│  
├─ ⚙️ **Select Standard Advantages** (6 stories)  
│  ├─ 📝 User selects advantage  
│  ├─ 📝 System displays advantage list organized by type  
│  ├─ 📝 User searches advantages by name  
│  ├─ 📝 User filters advantages by type (Combat, Fortune, General, Skill)  
│  ├─ 📝 System calculates total advantage points spent  
│  └─ 📝 System displays advantage descriptions  
├─ │  
├─ ⚙️ **Select Ranked Advantages** (5 stories)  
│  ├─ 📝 User selects ranked advantage  
│  ├─ 📝 System calculates cost (1 point per rank)  
│  ├─ 📝 User adjusts advantage ranks  
│  ├─ 📝 System displays examples of ranked advantages (Equipment, Benefit)  
│  └─ 📝 User removes ranked advantage  
├─ │  
├─ ⚙️ **Validate Prerequisites** (3 stories)  
│  ├─ 📝 System validates advantage prerequisites  
│  ├─ 📝 System displays prerequisite requirements before selection  
│  └─ 📝 System allows selection despite unmet prerequisites (warn don't prevent)  
├─ │  
└─ ⚙️ **Manage Advantage List** (~4 stories)  
   ├─ 📝 User removes advantage  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system refunds points  
   └─ 📝 ~3 more stories  

🎯 **Build Character Powers** (6 features, ~35 stories)  
│  
├─ ⚙️ **Select Power Effects** (7 stories)  
│  ├─ 📝 User selects base power effect  
│  ├─ 📝 User sets effect rank  
│  ├─ 📝 System displays effect catalog organized by type  
│  ├─ 📝 User searches effects by name  
│  ├─ 📝 System displays effect descriptions and examples  
│  ├─ 📝 System calculates total power points spent  
│  └─ 📝 System updates remaining point budget  
├─ │  
├─ ⚙️ **Apply Power Extras** (6 stories)  
│  ├─ 📝 User adds Extra modifier to effect  
│  ├─ 📝 System recalculates effect total cost  
│  ├─ 📝 System displays available Extras for effect type  
│  ├─ 📝 User removes Extra modifier  
│  ├─ 📝 System validates Extra compatibility with effect  
│  └─ 📝 System displays Extra descriptions  
├─ │  
├─ ⚙️ **Apply Power Flaws** (6 stories)  
│  ├─ 📝 User adds Flaw modifier to effect  
│  ├─ 📝 System recalculates effect total cost  
│  ├─ 📝 System displays available Flaws for effect type  
│  ├─ 📝 User removes Flaw modifier  
│  ├─ 📝 System validates Flaw compatibility with effect  
│  └─ 📝 System displays Flaw descriptions  
├─ │  
├─ ⚙️ **Create Power Arrays** (6 stories)  
│  ├─ 📝 User creates power array  
│  ├─ 📝 User adds alternate effect to array  
│  ├─ 📝 System calculates array total cost (base + alternates)  
│  ├─ 📝 User removes alternate effect  
│  ├─ 📝 System validates alternate effects ≤ base effect cost  
│  └─ 📝 System displays array structure visually  
├─ │  
├─ ⚙️ **Validate Power Limits** (5 stories)  
│  ├─ 📝 System validates effect rank against PL caps  
│  ├─ 📝 System validates attack effect rank ≤ PL  
│  ├─ 📝 System validates resistance effect rank ≤ PL  
│  ├─ 📝 System displays power validation warnings  
│  └─ 📝 System allows save despite power warnings (warn don't prevent)  
├─ │  
└─ ⚙️ **Manage Power List** (~5 stories)  
   ├─ 📝 User removes power effect  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system refunds points  
   └─ 📝 ~4 more stories  

🎯 **Validate Character** (5 features, ~25 stories)  
│  
├─ ⚙️ **Calculate Point Totals** (1 stories)  
│  └─ 📝 System includes powers in point breakdown  
├─ │  
├─ ⚙️ **Validate Power Level Caps** (4 stories)  
│  ├─ 📝 System validates Parry + Toughness ≤ PL × 2  
│  ├─ 📝 System displays all PL cap validations together  
│  ├─ 📝 System highlights exceeded caps in red  
│  └─ 📝 System explains PL cap formulas in tooltips  
├─ │  
├─ ⚙️ **Validate Point Budget** (3 stories)  
│  ├─ 📝 System validates total spent ≤ starting points  
│  ├─ 📝 System displays overspend amount  
│  └─ 📝 System allows save despite overspend (warn don't prevent)  
├─ │  
├─ ⚙️ **Display Validation Warnings** (~4 stories)  
│  ├─ 📝 System displays validation warnings  
│  │ &nbsp;&nbsp;&nbsp; - grouped by category (PL caps, budget, prerequisites)  
│  └─ 📝 ~3 more stories  
│  
└─ ⚙️ **Allow Save Despite Warnings** (~3 stories)  
   ├─ 📝 System allows save with validation warnings present  
   │ &nbsp;&nbsp;&nbsp; - displaying "Warn Don't Prevent" message  
   └─ 📝 ~2 more stories  

🎯 **Manage Characters** (5 features, ~22 stories)  
│  
├─ [⚙️ **Save Character**](./%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Save%20Character/%E2%9A%99%EF%B8%8F%20Save%20Character%20-%20Feature%20Overview.md)  
│  └─ 📝 System auto-saves periodically  
├─ │  
├─ [⚙️ **Load Character**](./%F0%9F%8E%AF%20Manage%20Characters/%E2%9A%99%EF%B8%8F%20Load%20Character/%E2%9A%99%EF%B8%8F%20Load%20Character%20-%20Feature%20Overview.md)  
│  ├─ 📝 System displays load errors  
│  └─ 📝 System restores UI state from saved character  
├─ │  
├─ ⚙️ **List Characters** (5 stories)  
│  ├─ 📝 User views character list  
│  ├─ 📝 User sorts character list  
│  ├─ 📝 User filters character list by PL  
│  ├─ 📝 User searches characters by name  
│  └─ 📝 System displays character count  
├─ │  
├─ ⚙️ **Delete Character** (4 stories)  
│  ├─ 📝 User deletes character  
│  ├─ 📝 System displays delete confirmation dialog  
│  ├─ 📝 System removes character from list  
│  └─ 📝 System handles delete errors gracefully  
├─ │  
└─ ⚙️ **Duplicate Character** (~4 stories)  
   ├─ 📝 User duplicates character  
   │ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- and system creates copy with "(Copy)" suffix  
   └─ 📝 ~3 more stories  

🎯 **Configure Complications** (3 features, ~12 stories)  
│  
├─ ⚙️ **Select Complication Types** (5 stories)  
│  ├─ 📝 User selects complication type  
│  ├─ 📝 System displays complication type list (Motivation, Identity, Relationship, etc.)  
│  ├─ 📝 User enters complication description  
│  ├─ 📝 System displays complication examples  
│  └─ 📝 User selects multiple complications  
├─ │  
├─ ⚙️ **Manage Complication List** (4 stories)  
│  ├─ 📝 User removes complication  
│  ├─ 📝 User edits complication description  
│  ├─ 📝 System displays complication count (recommend 2+)  
│  └─ 📝 System displays selected complications summary  
├─ │  
└─ ⚙️ **Display Complication Reminders** (~3 stories)  
   ├─ 📝 System displays complication reminders during character use  
   └─ 📝 ~2 more stories  

🎯 **Export Characters** (4 features, ~18 stories)  
│  
├─ ⚙️ **Export Character Sheet** (6 stories)  
│  ├─ 📝 User exports character to PDF  
│  ├─ 📝 System formats abilities section  
│  ├─ 📝 System formats skills section  
│  ├─ 📝 System formats powers section  
│  ├─ 📝 System formats complications section  
│  └─ 📝 System includes all calculated values  
├─ │  
├─ ⚙️ **Print Character Sheet** (5 stories)  
│  ├─ 📝 User prints character sheet  
│  ├─ 📝 System formats for print layout  
│  ├─ 📝 System includes print-friendly styling  
│  ├─ 📝 User previews before printing  
│  └─ 📝 System handles multi-page characters  
├─ │  
├─ ⚙️ **Share Character** (4 stories)  
│  ├─ 📝 User generates share link  
│  ├─ 📝 System displays shareable link  
│  ├─ 📝 User copies link to clipboard  
│  └─ 📝 System displays shared character as read-only  
├─ │  
└─ ⚙️ **Import Character** (~3 stories)  
   ├─ 📝 User imports character from file  
   └─ 📝 ~2 more stories  

🎯 **Support Gameplay** (4 features, ~20 stories)  
│  
├─ ⚙️ **Track Hero Points** (5 stories)  
│  ├─ 📝 User adjusts hero points  
│  ├─ 📝 System displays current hero points  
│  ├─ 📝 User resets hero points to maximum (1 per session)  
│  ├─ 📝 System tracks hero point usage history  
│  └─ 📝 User adds notes to hero point changes  
├─ │  
├─ ⚙️ **Track Conditions** (6 stories)  
│  ├─ 📝 User applies condition to character  
│  ├─ 📝 User removes condition  
│  ├─ 📝 System displays active conditions list  
│  ├─ 📝 System calculates penalties from conditions  
│  ├─ 📝 User adds custom condition  
│  └─ 📝 System validates condition compatibility  
├─ │  
├─ ⚙️ **Track Damage** (5 stories)  
│  ├─ 📝 User records damage penalty  
│  ├─ 📝 User clears damage penalties  
│  ├─ 📝 System displays current damage level  
│  ├─ 📝 System calculates effects on abilities  
│  └─ 📝 User applies recovery  
├─ │  
└─ ⚙️ **Roll Checks** (4 stories)  
   ├─ 📝 User rolls d20 for check  
   ├─ 📝 System displays roll breakdown  
   ├─ 📝 User selects check type (skill, attack, save)  
   └─ 📝 System highlights critical success or failure  
└─ │  

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

**Discovery Refinements**: Thursday, November 13, 2025
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
