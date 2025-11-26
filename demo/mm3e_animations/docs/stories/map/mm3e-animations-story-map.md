# Story Map: MM3e Animations Module

**Navigation:** [📊 Increments](../increments/mm3e-animations-story-map-increments.md)

**File Name**: `mm3e-animations-story-map.md`
**Location**: `mm3e_animations/docs/stories/map/mm3e-animations-story-map.md`

> **CRITICAL MARKDOWN FORMATTING**: All tree structure lines MUST end with TWO SPACES (  ) for proper line breaks. Without two spaces, markdown will wrap lines together into one long line, breaking the visual tree structure.

> **CRITICAL HIERARCHY FORMATTING**: The epic hierarchy section MUST use tree structure characters to show hierarchy:
> - Use `│` (vertical line) for continuing branches
> - Use `├─` (branch) for items that have siblings below them
> - Use `└─` (end branch) for the last item in a group
> - Epic format: `🎯 **Epic Name** (X features, ~Y stories)  `
> - Feature format: `├─ ⚙️ **Feature Name** (~Z stories)  ` or `└─ ⚙️ **Feature Name** (~Z stories)  ` for last feature
> - Story format (when present): `│  ├─ 📝 Story: [Verb-Noun Name]  ` followed by `│  │  *[Component interaction description]*  ` on the next line, or `│  └─ 📝 Story: [Verb-Noun Name]  ` for last story
> - **MANDATORY STORY NAMING FORMAT**: All story names MUST follow Actor-Verb-Noun format:
>   - Story name: Concise Verb-Noun format (e.g., "Create Mob from Selected Tokens", "Display Mob Grouping in Combat Tracker", "Execute Mob Attack with Strategy")
>   - Description: Italicized component interaction description showing component-to-component interactions (e.g., "*GM selects multiple minion tokens on canvas and Mob manager creates mob with selected tokens and assigns random leader*")

## System Purpose
Provides descriptor-based animation system for Mutants and Masterminds 3rd Edition powers in Foundry VTT, enabling automatic and manual animation playback based on power descriptors, range types, area shapes, and effects. Focuses on flexible domain model supporting reusable animation components that can be easily extended.

---

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Story Map Structure

🎯 **Build Animation from Components** (2 features, ~12 stories)  
│  
├─ ⚙️ **Assemble Animation from Base Templates** (~6 stories)  
│  ├─ 📝 Story: Receive Power Characteristics  
│  │  *Power Item Analyzer extracts descriptor, range, area, effect from power item and passes to Animation Builder*  
│  ├─ 📝 Story: Request Base Templates  
│  │  *Animation Builder constructs lookup key from descriptor+range+area+effect and requests templates from Descriptor Association*  
│  ├─ 📝 Story: Instantiate Cast Template  
│  │  *Animation Builder instantiates cast template with caster token location*  
│  ├─ 📝 Story: Instantiate Project Template  
│  │  *Animation Builder instantiates project template from caster to target for ranged powers*  
│  ├─ 📝 Story: Instantiate Affect Template  
│  │  *Animation Builder instantiates affect template at target/area location*  
│  └─ 📝 Story: Combine Templates into Sequence  
│     *Animation Builder combines all instantiated templates into single animation sequence with proper timing*  
│  
└─ ⚙️ **Parameterize Animation Components** (~6 stories)  
   ├─ 📝 Story: Receive Component Template  
   │  *Animation Builder receives animation component template from Descriptor Association*  
   ├─ 📝 Story: Apply Animation File Path  
   │  *Animation Builder applies animation file path parameter to component template*  
   ├─ 📝 Story: Apply Duration Parameter  
   │  *Animation Builder applies duration parameter to component template*  
   ├─ 📝 Story: Apply Sound File  
   │  *Animation Builder applies sound file parameter if specified in template*  
   ├─ 📝 Story: Apply Motion Effects  
   │  *Animation Builder applies motion effects parameter if specified in template*  
   └─ 📝 Story: Create Configured Component  
      *Animation Builder creates configured component instance from parameterized template*  

🎯 **Launch Animation on Attack** (3 features, ~19 stories)  
│  
├─ ⚙️ **Trigger Animation on Attack Hit** (~6 stories)  
│  ├─ 📝 Story: Receive Attack Rolled Hook  
│  │  *Animation Trigger listens to attackRolled hook and receives hook event with hit condition*  
│  ├─ 📝 Story: Extract Power Item  
│  │  *Animation Trigger extracts power item reference from attack data*  
│  ├─ 📝 Story: Extract Target Token  
│  │  *Animation Trigger extracts target token reference from attack data*  
│  ├─ 📝 Story: Request Hit Animation  
│  │  *Animation Trigger requests hit animation from Animation Builder with power characteristics and hit condition*  
│  ├─ 📝 Story: Assemble Hit Animation  
│  │  *Animation Builder assembles animation with hit condition and passes sequence to Sequencer Integration*  
│  └─ 📝 Story: Execute Animation  
│     *Sequencer Integration executes animation at target location showing hit effect*  
│  
├─ ⚙️ **Trigger Animation on Attack Miss** (~6 stories)  
│  ├─ 📝 Story: Receive Miss Hook Event  
│  │  *Animation Trigger receives attackRolled hook with miss condition*  
│  ├─ 📝 Story: Request Miss Animation  
│  │  *Animation Trigger requests miss animation from Animation Builder*  
│  ├─ 📝 Story: Assemble Miss Animation  
│  │  *Animation Builder assembles animation with miss condition*  
│  ├─ 📝 Story: Modify Projection for Miss  
│  │  *Animation Builder modifies projection component to stop short of target or fizzle*  
│  ├─ 📝 Story: Add Fizzle Effect  
│  │  *Animation Builder adds fizzle effect at projection end point*  
│  └─ 📝 Story: Execute Miss Animation  
│     *Sequencer Integration executes miss animation showing projection that doesn't reach target*  
│  
└─ ⚙️ **Launch Animation from Chat Button** (~7 stories)  
   ├─ 📝 Story: Add Run Animation Button  
   │  *Chat Attack System renders attack message and adds Run Animation button to message*  
   ├─ 📝 Story: Handle Button Click  
   │  *Player clicks Run Animation button and Chat Attack System receives click event*  
   ├─ 📝 Story: Extract Power Item ID  
   │  *Chat Attack System extracts power item ID from message data*  
   ├─ 📝 Story: Extract Target Token ID  
   │  *Chat Attack System extracts target token ID from message data*  
   ├─ 📝 Story: Extract Attack Condition  
   │  *Chat Attack System extracts attack condition from message*  
   ├─ 📝 Story: Request Animation from Trigger  
   │  *Chat Attack System requests animation from Animation Trigger with extracted data*  
   └─ 📝 Story: Process Manual Trigger  
      *Animation Trigger processes request same as automatic trigger and launches animation*  

🎯 **Associate Descriptors with Animations** (2 features, ~10 stories)  
│  
├─ ⚙️ **Lookup Animation Components by Descriptor** (~5 stories)  
│  ├─ 📝 Story: Construct Lookup Key  
│  │  *Animation Builder constructs lookup key from descriptor+range+area+effect*  
│  ├─ 📝 Story: Request Configuration  
│  │  *Animation Builder requests component configuration from Descriptor Registry using lookup key*  
│  ├─ 📝 Story: Lookup Descriptor Mapping  
│  │  *Descriptor Registry looks up descriptor mapping using provided key*  
│  ├─ 📝 Story: Return Component Configuration  
│  │  *Descriptor Registry returns component configuration (cast, project, affect templates)*  
│  └─ 📝 Story: Use Configuration for Assembly  
│     *Animation Builder uses returned configuration to assemble animation*  
│  
└─ ⚙️ **Register New Descriptor Configuration** (~5 stories)  
   ├─ 📝 Story: Receive Registration Request  
   │  *Descriptor Registry receives registration request with descriptor name and component configuration*  
   ├─ 📝 Story: Validate Configuration Structure  
   │  *Descriptor Registry validates configuration structure is correct format*  
   ├─ 📝 Story: Verify Component References  
   │  *Descriptor Registry verifies component references exist in Component Library*  
   ├─ 📝 Story: Store Descriptor Mapping  
   │  *Descriptor Registry stores descriptor-to-component mapping*  
   └─ 📝 Story: Make Descriptor Available  
      *New descriptor becomes available for animation lookup*  

🎯 **Analyze Power Items** (1 feature, ~6 stories)  
│  
└─ ⚙️ **Extract Power Characteristics from Item** (~6 stories)  
   ├─ 📝 Story: Receive Power Item  
   │  *Power Item Analyzer receives MM3e power item*  
   ├─ 📝 Story: Extract Descriptor  
   │  *Power Item Analyzer reads descriptor from item.system.descriptors*  
   ├─ 📝 Story: Determine Range Type  
   │  *Power Item Analyzer determines range type (Melee/Range/Personal) from item.system.range or attack.defenseType*  
   ├─ 📝 Story: Determine Area Shape  
   │  *Power Item Analyzer determines area shape if present (Burst/Cone/Line) from item.system.extras*  
   ├─ 📝 Story: Determine Effect Type  
   │  *Power Item Analyzer determines effect type (Damage/Affliction/etc) from item.system.effects*  
   └─ 📝 Story: Return Power Characteristics  
      *Power Item Analyzer returns Power Characteristics object with extracted data*  

---

## Source Material

**Shape phase:**
- Primary source: Legacy mm3e-animations module codebase (mm3e-effects-section.mjs, 21,190 lines)
- Sections referenced: PowerItem class, DescriptorSequence class, BaseEffectSection class, animation lookup chain, sequencer integration
- Date generated: 2024-12-19
- Context note: Legacy system analysis for new foundry-mm3 system migration. Focus on component integration and domain model flexibility. Restructured to show proper granularity: 4 epics, 7 features, 40 stories showing deeper component-level interactions.
