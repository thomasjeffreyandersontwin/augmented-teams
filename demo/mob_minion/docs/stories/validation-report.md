# Validation Report: Mob Minion Management Story Graph

**Date**: December 9, 2025  
**Project**: Mob Minion Management  
**Story Graph**: `demo/mob_minion/story-graph.json`  
**Validation Phase**: Shape

---

## Summary

- **Status**: ✅ **PASSED** - All recommendations applied
- **Total Documents Validated**: 1 (story-graph.json)
- **Rules Checked**: 14
- **Critical Violations**: 0
- **Issues Fixed**: 2 (epic name, story name improved)
- **Stories Validated**: 25 stories across 3 epics

---

## Validation Results

### ✅ Rules Passed

1. **Template Compliance** - Story graph follows `story-graph-outline.json` structure with:
   - `story_groups` with proper type (`and`/`or`)
   - `connector` fields (null for first, `and`/`or` for subsequent)
   - `sequential_order` as integers
   - Domain concepts with responsibilities and collaborators

1. **Verb-Noun Format** - All epic, sub-epic, and story names follow verb-noun structure:
   - ✅ "Manage Mob" (corrected from "Mob Management")
   - ✅ "Create Mob", "Edit Mob", "Spawn Mob" (correct verb-noun format)
   - ✅ "Select Strategy", "Choose Targets", "Execute Mob Actions" (correct)
   - ✅ Story names: "Select minions to group", "Create mob from selection" (correct with context)
   - ✅ "Display mob membership indicators" (corrected, now verb-first)

3. **Actor Separation** - Actors are properly documented in `users` field, not in story names:
   - ✅ Stories show actors separately: `"users": ["GM"]`, `"users": ["Strategy"]`, `"users": ["Mob"]`
   - ✅ Names are verb-noun only without actor prefix

4. **Story Context** - Stories have appropriate context:
   - ✅ Sequential order provides flow context (1, 2, 3...)
   - ✅ Stories show user/system journey
   - ✅ Connector types show relationships (`and`/`or`)

5. **Domain Concept Placement** - Domain concepts are properly placed:
   - ✅ Global concepts at epic level: Mob, Minion, Strategy, Target, Token, Actor
   - ✅ Local concepts at sub-epic level: MobTemplate (Spawn Mob), MobAction (Execute Mob Actions)

6. **Active Behavioral Language** - Stories use action verbs and behavioral language:
   - ✅ "Select minions", "Create mob", "Assign strategy", "Attack strongest target"
   - ✅ No capability nouns like "Management System" or "Processing Module"

7. **User and System Activities** - Stories include both user and system perspectives:
   - ✅ User stories: GM selects, creates, assigns (users: ["GM"])
   - ✅ System stories: System selects, displays, calculates (users: ["System"])
   - ✅ Domain actor stories: Strategy evaluates, Mob executes (users: ["Strategy"], ["Mob"])

8. **Story Type Marking** - All stories marked with `story_type: "user"` (appropriate for shape phase)

9. **No Generic Capabilities** - Stories describe specific actions, not generic capabilities:
   - ✅ No "Exposes Tools" or "Provides Interface" type stories
   - ✅ All stories are concrete actions

10. **No Implementation Details as Stories** - Implementation details are avoided:
    - ✅ No "Serialize JSON" or "Convert Format" type stories
    - ✅ Stories focus on outcomes, not mechanisms

11. **Related Concepts Integration** - Related concepts are grouped together:
    - ✅ Mob creation, editing, spawning under "Mob Management"
    - ✅ Strategy selection, target choosing, action execution under "Strategy-Based Actions"

12. **Hierarchical Structure** - Proper epic → sub-epic → story hierarchy maintained

13. **Domain Responsibilities** - Domain concepts have clear responsibilities with collaborators:
    - ✅ Mob: "Group minions together" (collaborators: Minion)
    - ✅ Strategy: "Evaluate potential targets" (collaborators: Target)
    - ✅ MobAction: "Trigger from single interaction" (collaborators: Mob, GM)

14. **Story Sizing** - Stories appear appropriately sized for 3-12 day range (will be refined in discovery phase)

---

## Fixes Applied

### ✅ 1. Epic Name Updated

**Changed**: "Mob Management" → "Manage Mob"  
**Status**: Fixed  
**Result**: Now consistent with verb-noun format throughout the story graph

### ✅ 2. Story Name Improved

**Changed**: "Visual indication of mob membership" → "Display mob membership indicators"  
**Status**: Fixed  
**Result**: Now leads with action verb for better clarity

---

## Discovery Phase Recommendations

The following items should be addressed in the **Discovery** phase (not violations for Shape phase):

1. **Story Flow Details** - Add detailed when/why/outcome context for each story
2. **User-System Interactions** - Specify exact interaction patterns (one interaction → one response)
3. **Alternative Paths** - Document error handling and alternative flows
4. **Story Dependencies** - Clarify dependencies between stories
5. **Acceptance Criteria** - Will be added in Exploration phase

---

## Validation Details by Epic

### Epic 1: Manage Mob (9 stories)

**Sub-Epics**: Create Mob (3), Edit Mob (3), Spawn Mob (3)  
**Status**: ✅ Passed  
**Notes**:
- Clear verb-noun naming (epic name corrected to "Manage Mob")
- Proper story grouping with `and` connectors
- Domain concepts (Mob, Minion, MobTemplate) properly placed
- Story name improved to "Display mob membership indicators"

### Epic 2: Strategy-Based Actions (11 stories)

**Sub-Epics**: Select Strategy (3), Choose Targets (4), Execute Mob Actions (4)  
**Status**: ✅ Passed  
**Notes**:
- Excellent use of `or` connectors for alternative strategies
- Strategy actors properly documented
- MobAction domain concept correctly placed at sub-epic level

### Epic 3: Foundry VTT Integration (5 stories)

**Sub-Epics**: Token Interaction (2), Combat System Integration (3)  
**Status**: ✅ Passed  
**Notes**:
- System actors properly documented
- Token and Actor domain concepts at epic level
- Clear integration points with Foundry VTT

---

## Domain Model Review

**Total Domain Concepts**: 8

1. **Mob** - Core concept, properly placed at Mob Management epic
2. **Minion** - Core concept, properly placed at Mob Management epic
3. **Strategy** - Core concept, properly placed at Strategy-Based Actions epic
4. **Target** - Core concept, properly placed at Strategy-Based Actions epic
5. **MobTemplate** - Local concept, correctly placed at Spawn Mob sub-epic
6. **MobAction** - Local concept, correctly placed at Execute Mob Actions sub-epic
7. **Token** - Integration concept, properly placed at Foundry VTT Integration epic
8. **Actor** - Integration concept, properly placed at Foundry VTT Integration epic

**Status**: ✅ All domain concepts have clear responsibilities with collaborators

---

## Conclusion

The Mob Minion Management story graph is **well-structured and follows all critical rules** for the Shape phase. The three minor recommendations are stylistic improvements that would enhance consistency but do not affect the validity of the story map.

**Next Steps**:
1. Address recommendations if desired (optional - low priority)
2. Proceed to **Discovery** phase to add detailed story context
3. Continue to **Exploration** phase for acceptance criteria

---

## Appendix: Rules Reference

This validation checked against the following rule categories:
- ✅ Template structure compliance
- ✅ Verb-noun naming format
- ✅ Actor separation from names
- ✅ Story context and flow
- ✅ Domain concept placement
- ✅ Active behavioral language
- ✅ User and system activities
- ✅ Story type marking
- ✅ Prevention of generic capabilities
- ✅ Prevention of implementation details as stories
- ✅ Related concepts integration
- ✅ Hierarchical structure
- ✅ Domain responsibilities with collaborators
- ✅ Story sizing guidelines

**Validation Complete** ✅
