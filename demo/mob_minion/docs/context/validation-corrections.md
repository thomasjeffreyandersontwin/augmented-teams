# Story Graph Validation Corrections - Mob Minion

## All Violations Fixed

### Changes Applied

**1. Epic Name Fixed**
- **Before**: "Explore Foundry API" (wrong verb form)
- **After**: "Map Foundry API" (action-oriented verb)
- **Rationale**: "Map" is an action verb showing what is being done, not just exploration

**2. Data Access Stories Transformed to Show Value**

| Before (No Value) | After (Clear Outcome) | Rationale |
|-------------------|----------------------|-----------|
| "Query Token Properties" | "Retrieve Token Selection State" | Shows specific outcome - getting selection state |
| "Access Actor Data" | "Load Actor Statistics" | Specifies what data and clear loading action |
| "Retrieve Actor Stats" | "Evaluate Actor Combat Capabilities" | Outcome-focused - evaluating capabilities for strategy use |
| "Access Combat Tracker" | "Register Combatant In Tracker" | Complete action - registering entity in system |
| "Query Available Targets" | "Identify Valid Combat Targets" | Clear purpose - identifying valid targets for strategy |

**3. Generic/Implementation Stories Made Specific**

| Before (Generic/Implementation) | After (Specific/Testable) | Rationale |
|---------------------------------|---------------------------|-----------|
| "Execute Action" | "Determine Attack Feasibility" | Specific testable outcome - can attack or not |
| "Calculate Range" | Merged into "Determine Attack Feasibility" | Implementation detail merged into testable story |
| "Move Minion To Target" | Removed | Implementation step - movement is part of attack execution stories |

**4. User Changes**
- Changed "Foundry API" users to "Mob System" to reflect that the mob system integrates with Foundry, not that Foundry API is the actor

**5. Story Count Updates**
- Map Combat System: 3 → 2 stories (merged Calculate Range)
- Execute Mob Actions: 6 → 5 stories (removed Move Minion)
- Total: ~17 stories (within 15-20 target range)

## Verification Against Rules

### ✓ Verb-Noun Format
- All epics, sub-epics, and stories use proper verb-noun format
- Action verbs used consistently: Map, Retrieve, Load, Evaluate, Register, Determine, Identify, Set
- No actors in names (documented separately in users field)

### ✓ Active Business Language
- All stories use active voice with clear actors
- Business/system behavior focus, not technical implementation
- System stories properly marked with story_type: "system"

### ✓ Outcome-Oriented Language
- Stories focus on outcomes and artifacts
- "Retrieve Token Selection State" not "Access Tokens"
- "Evaluate Actor Combat Capabilities" not "Query Actor Data"
- "Determine Attack Feasibility" not "Calculate Range"

### ✓ Valuable
- All stories deliver independent value with clear outcomes
- "Retrieve Token Selection State" → value: know which tokens are selected
- "Register Combatant In Tracker" → value: combatant tracked in Foundry
- "Determine Attack Feasibility" → value: know if attack is possible

### ✓ Small and Testable
- All stories are complete interactions that can be tested independently
- Implementation steps removed or merged
- Each story has clear acceptance criteria potential
- Stories follow user/system journey, not implementation order

### ✓ User and System Behavior
- System integration stories properly marked as story_type: "system"
- User stories show GM actions with system responses
- Complete flows: user action → system response

## Summary

**Status: ALL VIOLATIONS RESOLVED ✓**

- 10 violations identified
- 10 violations corrected
- 0 remaining issues
- Story graph ready for validation approval

The story graph now follows all shaping rules with:
- Clear value proposition for each story
- Proper verb-noun format throughout
- Outcome-oriented language
- Testable, independent stories
- System integration stories properly identified
- Total story count: ~17 (within 15-20 target)


