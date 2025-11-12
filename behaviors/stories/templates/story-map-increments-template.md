# Story Map with Increments: [Product/Feature Name]

**File Name**: `[product-name]-story-map-increments.md` (e.g., `mm3-character-builder-story-map-increments.md`)
**Location**: `docs/stories/increments/[product-name]-story-map-increments.md`
**Created During**: Shape Phase (`/story-shape`) - organizes stories by increments
**Purpose**: Organize stories by Value Increments (can include story counts during Shape, finalized during Discovery)
**Note**: Individual increment docs (`increment-[name].md`) created in `docs/stories/increments/` during Discovery Phase (`/story-discovery`)

## System Purpose
[Brief description of the system purpose and user goals]

---

## Legend
- 🚀 **Value Increment** - Deliverable chunk of value
- 🎯 **Epic** - High-level capability
- 📂 **Sub-Epic** - Sub-capability (when epic has > 9 features)
- ⚙️ **Feature** - Cohesive set of functionality
- 📝 **Story** - Small increment of behavior

---

## Marketable Value Increments

🚀 **Value Increment 1: [Name] - NOW**
│   *Priority: NOW (deliver first)*
│   *Relative Size: [Compared to: Previous similar work]*
│   *Story Count: X stories (all listed)*
│
├─ 🎯 **[Verb] [Noun]** (X features, Y stories)
│  │
│  └─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (X stories)
│     ├─ 📝 User [verb] [noun]
│     │   - and system [immediate response]
│     ├─ 📝 User [verb] [noun]
│     │   - and system [immediate response]
│     ├─ 📝 System [verb] [noun] when [trigger]
│     │   - [Cascading effect description]
│     └─ 📝 User [verb] [noun]
│        - and system [immediate response]
│
└─ 🎯 **[Verb] [Noun]** (X features, Y stories)
   │
   └─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (X stories)
      ├─ 📝 User [verb] [noun]
      │   - and system [immediate response]
      ├─ 📝 User [verb] [noun]
      │   - and system [immediate response]
      └─ 📝 System [verb] [noun] when [trigger]

---

🚀 **Value Increment 2: [Name] - NEXT**
│   *Priority: NEXT*
│   *Relative Size: [Compared to: Previous similar work]*
│   *Story Count: ~X stories*
│
└─ 🎯 **[Verb] [Noun]** (PARTIAL - [what's included])
   │
   └─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~X stories)
      │   *Note: [Any important notes]*
      └─ (~X stories - not yet identified)

---

🚀 **Value Increment 3: [Name] - LATER**
│   *Priority: LATER*
│   *Relative Size: [Compared to: Previous similar work]*
│   *Story Count: ~X stories*
│
└─ 🎯 **[Verb] [Noun]** (REMAINING)
   │
   └─ ⚙️ **[Verb] [Noun]** *[optional clarifier]* (~X stories)
      └─ (~X stories - not yet identified)

---

## Notes

### Format
- **Increment(s) in Focus**: ALL stories must be listed explicitly (no ~X stories notation) for increment(s) being discovered
- **Other Increments**: Use story counts (~X stories) for increments not yet in focus
- **NO separate increment docs**: This single file contains all increments
- **NO Status field**: Do not add "Status: DISCOVERY" lines
- **NO Estimates by AI**: Estimates require human entry during actual discovery sessions
- **Priority Labels**: NOW / NEXT / LATER (not High/Medium/Low)
- **Partial Epics/Features**: Increments can contain partial epics or features
- **Naming**: All levels use [Verb] [Noun] *[optional clarifier]* format
- **Tree Characters**: Use │ ├─ └─ to show hierarchy
- **Emojis**: Visual indicators for quick scanning (🚀 🎯 📂 ⚙️ 📝)
- **Relative Sizing**: Compare each increment to previously delivered similar work

### Story Format (CRITICAL)
- **Story Title**: "User [verb] [noun]" or "System [verb] [noun] when [trigger]"
- **Single "and" clause**: "- and system [immediate response]" (shows user action + system response = ONE story)
- **NO extra notes**: NO examples, NO data lists in story map (save details for exploration)
- **NO separate system stories**: User action + immediate system response = ONE story, not two
- **System stories**: Only for system-to-system communication (e.g., "Payment service validates with fraud detection service")

### Discovery Decomposition Principles
- **Same logic, different data → ONE story**: Consolidate when UI/validation/calculation logic is identical
- **Different formulas/rules/algorithms → SEPARATE stories**: Split when business logic differs
- **Enumerate ALL permutations**: Identify every different path through requirements
- **Cascading updates**: Make cascading recalculation its own story when it updates multiple dependent values
- **Seek significant differences**: Look for differences in business logic, state management, rules, data structure
- **Ask "What fundamentally different code must be built?"**: If different classes/functions/algorithms needed, it's a different story

### Exploration Acceptance Criteria Principles
- **AC Location**: ALL acceptance criteria belong in FEATURE documents, NOT in story documents
- **Domain AC**: Feature-level concepts, constraints, relationships (in feature document)
- **Behavioral AC**: Story-level When/Then statements (in feature document under each story)
- **AC Format**: Use "When...then..." format (NO "Given" clauses - save for specifications)
- **Story Documents**: Contain only story description and reference to feature document for AC
- **Feature Document**: Contains all Domain AC and Behavioral AC for all stories in that feature
