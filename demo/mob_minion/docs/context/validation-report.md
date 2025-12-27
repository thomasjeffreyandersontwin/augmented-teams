# Story Graph Validation Report - Mob Minion

## Unified Violations Table

| Theme | Rule | Location | Valid/FP | Source | Root Cause | Problem Example | Fix with Code Example |
|-------|------|----------|----------|--------|------------|-----------------|----------------------|
| No value | Valuable | epics[0].sub_epics[0].story_groups[0].stories[0] | Valid | Manual | Data access without outcome | `"Query Token Properties"` | `"Retrieve Token Selection State"` - includes clear outcome |
| No value | Valuable | epics[0].sub_epics[1].story_groups[0].stories[0] | Valid | Manual | Data access without outcome | `"Access Actor Data"` | `"Load Actor Statistics"` - specifies what data and purpose |
| No value | Valuable | epics[0].sub_epics[1].story_groups[0].stories[1] | Valid | Manual | Data access without outcome | `"Retrieve Actor Stats"` | `"Evaluate Actor Combat Capabilities"` - outcome-focused |
| No value | Valuable | epics[0].sub_epics[2].story_groups[0].stories[0] | Valid | Manual | Data access without outcome | `"Access Combat Tracker"` | `"Register Combatant In Tracker"` - clear action and outcome |
| No value | Valuable | epics[0].sub_epics[3].story_groups[0].stories[0] | Valid | Manual | Data access without outcome | `"Query Available Targets"` | `"Identify Valid Combat Targets"` - complete action with purpose |
| Too generic | Verb-Noun Format | epics[0].sub_epics[2].story_groups[0].stories[1] | Valid | Manual | Generic verb without specificity | `"Execute Action"` | `"Initiate Attack Action"` or `"Trigger Mob Action"` - specific |
| Implementation step | Small and Testable | epics[0].sub_epics[2].story_groups[0].stories[2] | Valid | Manual | Implementation detail, not testable story | `"Calculate Range"` | `"Determine Attack Feasibility"` - testable outcome |
| Implementation step | Small and Testable | epics[3].sub_epics[1].story_groups[1].stories[0] | Valid | Manual | Implementation step within larger action | `"Move Minion To Target"` | Merge into parent attack stories or `"Position Minion For Attack"` |
| Verb naming | Verb-Noun Format | epics[0] | Valid | Manual | Wrong verb form (explore vs process/map) | `"Explore Foundry API"` | `"Map Foundry API"` - action verb |
| Too generic | Verb-Noun Format | epics[1].sub_epics[2] | Valid | Manual | Noun-only without specific action | `"Spawn Mob"` | `"Create Mob From Template"` or keep as epic, stories are specific |

## Summary

### Scanner Violations
No automated scanner was run - manual review only.

### Manual Findings
**Total Violations: 10**

**Priority Fixes (Must Resolve):**

1. **Data Access Without Value (5 violations)**
   - Stories that only query/access/retrieve data without clear outcome or purpose
   - Location: Foundry API exploration epic stories
   - Pattern: "Query X", "Access Y", "Retrieve Z"
   - Fix: Transform into stories with clear outcomes

2. **Generic/Implementation Details (3 violations)**
   - Stories too generic or representing implementation steps rather than testable behaviors
   - Location: Combat system and mob action stories  
   - Pattern: "Execute Action", "Calculate Range", "Move Minion"
   - Fix: Make specific or merge into parent stories

3. **Naming Issues (2 violations)**
   - Wrong verb forms or non-specific naming
   - Location: Epic and sub-epic names
   - Pattern: "Explore" instead of action verb, noun-only sub-epic
   - Fix: Use proper verb-noun format with action verbs

**Optional Improvements:**
- Consider whether "Foundry API" exploration epic should have more specific outcomes since this is a shaping phase
- Verify all stories follow user journey flow rather than technical implementation order

## Recurring Themes

1. **API Exploration Stories Lack Clear Value** - The Foundry API exploration stories focus on accessing/querying data without showing what happens with that data or what outcome is achieved

2. **Implementation Steps Elevated to Stories** - Some stories represent technical implementation steps (calculate, move) rather than complete testable behaviors

3. **Generic Naming** - Some stories use generic verbs without specificity about what specifically is being done

## Recommendations

**Before proceeding:**
1. Rewrite all API exploration stories to show clear outcomes and value
2. Either merge implementation steps into parent stories or rewrite as complete behaviors  
3. Fix verb forms and naming to be specific and action-oriented
4. Verify stories can be tested independently with clear acceptance criteria

**Alternative Approach for API Exploration:**
Since this is shaping phase and API exploration is foundational, consider whether these should be:
- Technical spike stories (story_type: 'technical') with clear deliverables
- Or reframed as integration stories showing system-to-system interactions with outcomes

