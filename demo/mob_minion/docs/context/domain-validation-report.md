# Domain Model Validation Report - Mob Minion

## Unified Violations Table

| Theme | Rule | Location | Valid/FP | Source | Root Cause | Problem Example | Fix with Code Example |
|-------|------|----------|----------|--------|------------|-----------------|----------------------|
| Capability verbs | Use Domain Language | epics[0].sub_epics[1].domain_concepts[0].responsibilities[1] | Valid | Manual | Using capability verb instead of domain action | `"Provides combat capabilities"` | `"Evaluates combat capabilities"` |
| Capability verbs | Use Domain Language | epics[0].sub_epics[1].domain_concepts[0].responsibilities[2] | Valid | Manual | Using capability verb instead of domain action | `"Exposes HP and power level"` | `"Tracks HP and power level"` |

## Summary

### Scanner Violations
No automated scanner was run - manual review only.

### Manual Findings
**Total Violations: 2**

**Priority Fixes:**

1. **Capability Verb Usage (2 violations)**
   - Location: Actor concept in Map Actor System
   - Pattern: Using "Provides" and "Exposes" - these are capability/interface verbs, not domain behaviors
   - Fix: Replace with domain-specific action verbs

**Violations Details:**

1. **Actor.responsibilities[1]**: "Provides combat capabilities"
   - Issue: "Provides" is a capability verb indicating what the concept exposes, not what it does
   - Fix: "Evaluates combat capabilities" - shows the actor actively evaluating its own capabilities

2. **Actor.responsibilities[2]**: "Exposes HP and power level"
   - Issue: "Exposes" is an API/interface term, not domain language
   - Fix: "Tracks HP and power level" - shows the actor managing its own state

### Positive Findings

**Well-Formed Concepts (Examples):**
- ✓ Token: "Represents minion on game map" - clear domain language
- ✓ Mob: "Coordinates minion actions" - specific domain behavior
- ✓ Strategy: "Defines targeting behavior" - clear purpose
- ✓ Attack: "Executes coordinated action" - action-oriented

**Good Practices Followed:**
- Domain concepts properly scoped (local to sub-epics, global at epic level where shared)
- Natural English in most responsibilities
- Clear collaborator relationships derived from stories
- Resource-oriented design (concepts represent domain resources)
- Avoids technical patterns (no Manager, Service, Handler, Factory suffixes)

### Optional Improvements

**None identified** - domain model is generally well-structured with only 2 minor violations to fix.

## Recommendations

**Before proceeding:**
1. Fix the 2 capability verb violations in Actor concept
2. All other domain concepts are compliant

The domain model accurately represents the mob minion system with clear concepts, responsibilities, and relationships.

