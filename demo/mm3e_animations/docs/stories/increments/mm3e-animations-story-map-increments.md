# Story Map Increments: MM3e Animations Module

**Navigation:** [📋 Story Map](../map/mm3e-animations-story-map.md)

**File Name**: `mm3e-animations-story-map-increments.md`
**Location**: `mm3e_animations/docs/stories/increments/mm3e-animations-story-map-increments.md`

> **CRITICAL MARKDOWN FORMATTING**: All tree structure lines MUST end with TWO SPACES (  ) for proper line breaks. Without two spaces, markdown will wrap lines together into one long line, breaking the visual tree structure.

## Increment Planning Philosophy

**🎯 VERTICAL SLICES - NOT Horizontal Layers**

Each increment should deliver a **thin end-to-end working flow** across multiple features/epics, NOT complete one feature/epic at a time.

- ✅ **DO**: Include PARTIAL features from MULTIPLE epics in each increment
- ✅ **DO**: Ensure each increment demonstrates complete flow: input → process → validate → persist → display
- ✅ **DO**: Layer complexity across increments (simple first, then add users/scenarios/edge cases)
- ❌ **DON'T**: Complete entire Epic A, then Epic B, then Epic C
- ❌ **DON'T**: Build increments that can't demonstrate working end-to-end flow

**Layering Strategy:**
- **Increment 1**: Simplest user + simplest scenario + happy path → Full end-to-end
- **Increment 2**: Add complexity (more options, validations) + Additional users → Full end-to-end  
- **Increment 3**: Add edge cases + Error handling + Advanced features → Full end-to-end

## Legend
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Increment 1: Core Animation System

**Priority:** NOW  
**Relative Size:** Large  
**Approach:** Build core domain model with Animation Builder, Descriptor Association, and basic component types. Implement integration with MM3e attack system for hit/miss conditions. Focus on getting domain model right for extensibility.  
**Focus:** Establish flexible domain model supporting component-based animation assembly. Implement basic integration points with MM3e system, targeting, and sequencer. Support hit and miss conditions.

### Stories Included

🎯 **Build Animation from Components**  
│  
├─ ⚙️ **Assemble Animation from Base Templates**  
│  ├─ 📝 Receive Power Characteristics  
│  ├─ 📝 Request Base Templates  
│  ├─ 📝 Instantiate Cast Template  
│  ├─ 📝 Instantiate Project Template  
│  ├─ 📝 Instantiate Affect Template  
│  └─ 📝 Combine Templates into Sequence  
│  
🎯 **Launch Animation on Attack**  
│  
├─ ⚙️ **Trigger Animation on Attack Hit**  
│  ├─ 📝 Receive Attack Rolled Hook  
│  ├─ 📝 Extract Power Item  
│  ├─ 📝 Extract Target Token  
│  ├─ 📝 Request Hit Animation  
│  ├─ 📝 Assemble Hit Animation  
│  └─ 📝 Execute Animation  
│  
🎯 **Associate Descriptors with Animations**  
│  
├─ ⚙️ **Lookup Animation Components by Descriptor**  
│  ├─ 📝 Construct Lookup Key  
│  ├─ 📝 Request Configuration  
│  └─ 📝 Return Component Configuration  
│  
🎯 **Analyze Power Items**  
│  
└─ ⚙️ **Extract Power Characteristics from Item**  
   ├─ 📝 Receive Power Item  
   ├─ 📝 Extract Descriptor  
   ├─ 📝 Determine Range Type  
   └─ 📝 Return Power Characteristics  

---

## Source Material

**Shape phase:**
- Primary source: Legacy mm3e-animations module codebase (mm3e-effects-section.mjs, 21,190 lines)
- Sections referenced: PowerItem class, DescriptorSequence class, BaseEffectSection class, animation lookup chain, sequencer integration
- Date generated: 2024-12-19
- Context note: Legacy system analysis for new foundry-mm3 system migration. Focus on component integration and domain model flexibility. Restructured to show proper granularity: 4 epics, 7 features, 40 stories showing deeper component-level interactions.
