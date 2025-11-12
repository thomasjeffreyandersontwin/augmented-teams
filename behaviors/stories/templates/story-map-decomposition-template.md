# Story Map: [Product/Feature Name]

**File Name**: `[product-name]-story-map.md` (e.g., `mm3-character-builder-story-map.md`)
**Location**: `docs/stories/map/[product-name]-story-map.md`
**Note**: Epic/feature folder structure created later by `/story-arrange` command

## System Purpose
[Brief description of the system purpose and user goals]

---

## Legend
- 🎯 **Epic** - High-level capability
- 🎯 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior (3-12d)

---

## Story Map Structure

🎯 **[Verb] [Noun]** *[optional clarifier]* (8 features, ~Y stories)
│   *Relative Size: [Compared to: Previous similar work]*
│
├─ 🎯 **[Verb] [Noun]** *[optional clarifier]* (6 features, ~X stories)
│  │
│  ├─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~9 stories)
│  │  ├─ 📝 User [verb] [noun]
│  │  │   - and system [immediate response]
│  │  ├─ 📝 User [verb] [noun]
│  │  │   - and system [immediate response]
│  │  ├─ 📝 System [verb] [noun] when [trigger]
│  │  └─ 📝 ~6 more stories
│  │
│  ├─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~X stories)
│  └─ ⚙️ ~4 more features
│
└─ 🎯 **[Verb] [Noun]** *[optional clarifier]* (5 features, ~X stories)
   │
   ├─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~8 stories)
   │  ├─ 📝 User [verb] [noun]
   │  │   - and system [immediate response]
   │  ├─ 📝 User [verb] [noun]
   │  │   - and system [immediate response]
   │  └─ 📝 ~6 more stories
   │
   ├─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~X stories)
   └─ ⚙️ ~3 more features

---

🎯 **[Verb] [Noun]** *[optional clarifier]* (4 features, ~Y stories)
│   *Relative Size: [Compared to: Previous similar work]*
│
├─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~7 stories)
│  ├─ 📝 User [verb] [noun]
│  │   - and system [immediate response]
│  ├─ 📝 System [verb] [noun] when [trigger]
│  └─ 📝 ~5 more stories
│
├─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~X stories)
└─ ⚙️ ~2 more features

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
- **Example Pattern - Features**: Epic (8 features) → show 2-3 examples → "~5 more features"
- **Example Pattern - Stories**: Feature (~9 stories) → show 3 examples → "~6 more stories"
- **Extrapolate scope**: Enough to estimate but not exhaustive
- **Save exhaustive decomposition for Discovery**: Full permutation enumeration happens in Discovery phase
