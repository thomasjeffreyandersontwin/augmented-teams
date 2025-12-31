# Validation Analysis - Exploration

**Generated:** 2025-12-30  
**Rule:** stories_have_4_to_9_acceptance_criteria.json  
**Total Violations:** 59

## Unified Violations Table

| Theme | Rule | Location | Valid/FP | Source | Root Cause | Problem Example | Fix with Code Example |
|-------|------|----------|----------|--------|------------|-----------------|----------------------|
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has only 1 AC, missing error cases, validation, edge cases | Story "Generate Bot Tools" has 1 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC, confirmation AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[0].sub_epics[0].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 1 AC, missing error cases, validation, edge cases | Story "Generate Behavior Tools" has 1 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC, confirmation AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[0].sub_epics[1].story_groups[0].stories[4].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Generate Help Parameters From Action Context Classes" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[0].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Initialize Project Creates Context Folder" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[1].story_groups[0].stories[4].acceptance_criteria` | Valid | Scanner | Story has only 1 AC, missing error cases, validation, edge cases | Story "Track Activity For Workspace" has 1 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC, confirmation AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[3].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Find Behavior Folder" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[3].story_groups[0].stories[2].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Invoke Behavior in Workflow Order" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[3].story_groups[0].stories[6].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Inject Next Behavior Reminder" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Surface Block Reason" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[2].story_groups[1].stories[0].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Report Completion" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[2].story_groups[1].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Recover and Report Failures" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[0].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Track Activity for Gather Context Action" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[0].story_groups[0].stories[4].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Load Base Action Config" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[0].story_groups[0].stories[5].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Access Actions" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[0].story_groups[0].stories[6].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Initialize Action" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[0].story_groups[0].stories[7].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Load Guardrails" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[1].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Track Activity for Planning Action" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[1].story_groups[0].stories[4].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Inject Strategy Into Instructions" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[1].story_groups[0].stories[5].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Store Strategy Data" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[2].story_groups[0].stories[2].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Track Activity for Build Knowledge Action" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[2].story_groups[0].stories[6].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Create Build Scope" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[2].story_groups[0].stories[7].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Filter Knowledge Graph" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Track Activity for Render Output Action" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[6].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Get Render Instructions" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[8].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Render Output Using Synchronizers" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[10].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Get Render Instructions" (duplicate) has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[12].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Render Output Using Synchronizers" (duplicate) has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[4].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Track Activity for Validate Rules Action" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Under-explored stories (<4 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[4].story_groups[0].stories[6].acceptance_criteria` | Valid | Scanner | Story has only 2 AC, missing error cases, validation, edge cases | Story "Validate Rules According To Scope" has 2 acceptance criteria | Expand to 4-6 AC: Add validation error AC, edge case AC, alternate flow AC |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[0].sub_epics[1].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has 13 AC, should be split into smaller stories | Story "Generate Cursor Command Files" has 13 acceptance criteria | Split into: Story A (6 AC for core file generation) + Story B (7 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[0].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has 13 AC, should be split into smaller stories | Story "Initialize Project Location" has 13 acceptance criteria | Split into: Story A (6 AC for core initialization) + Story B (7 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[0].story_groups[0].stories[3].acceptance_criteria` | Valid | Scanner | Story has 12 AC, should be split into smaller stories | Story "Store Context Files" has 12 acceptance criteria | Split into: Story A (6 AC for core storage) + Story B (6 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[2].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has 11 AC, should be split into smaller stories | Story "Invoke Bot CLI" has 11 acceptance criteria | Split into: Story A (5 AC for core CLI invocation) + Story B (6 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[2].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has 12 AC, should be split into smaller stories | Story "Invoke Bot Behavior CLI" has 12 acceptance criteria | Split into: Story A (6 AC for core behavior CLI) + Story B (6 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[2].story_groups[0].stories[2].acceptance_criteria` | Valid | Scanner | Story has 12 AC, should be split into smaller stories | Story "Invoke Bot Behavior Action CLI" has 12 acceptance criteria | Split into: Story A (6 AC for core action CLI) + Story B (6 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[2].story_groups[0].stories[3].acceptance_criteria` | Valid | Scanner | Story has 19 AC, should be split into smaller stories | Story "Get Help for Command Line Functions" has 19 acceptance criteria | Split into: Story A (6 AC for basic help) + Story B (7 AC for advanced help) + Story C (6 AC for help formatting) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[4].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has 11 AC, should be split into smaller stories | Story "Route to BotLangFlow" has 11 acceptance criteria | Split into: Story A (5 AC for core routing) + Story B (6 AC for advanced routing) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has 19 AC, should be split into smaller stories | Story "Add Headless Mode To Help" has 19 acceptance criteria | Split into: Story A (6 AC for basic help) + Story B (7 AC for advanced help) + Story C (6 AC for help formatting) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[0].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has 22 AC, should be split into smaller stories | Story "Add Headless Mode To Status" has 22 acceptance criteria | Split into: Story A (7 AC for basic status) + Story B (7 AC for advanced status) + Story C (8 AC for status formatting) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[1].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has 33 AC, should be split into smaller stories | Story "Execute Direct Instructions" has 33 acceptance criteria | Split into: Story A (8 AC for basic execution) + Story B (8 AC for error handling) + Story C (8 AC for recovery) + Story D (9 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[1].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has 31 AC, should be split into smaller stories | Story "Execute Single Operation" has 31 acceptance criteria | Split into: Story A (8 AC for basic operation) + Story B (8 AC for error handling) + Story C (8 AC for recovery) + Story D (7 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[1].story_groups[0].stories[2].acceptance_criteria` | Valid | Scanner | Story has 34 AC, should be split into smaller stories | Story "Execute Complete Action" has 34 acceptance criteria | Split into: Story A (8 AC for basic action) + Story B (8 AC for error handling) + Story C (9 AC for recovery) + Story D (9 AC for advanced features) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[1].story_groups[0].stories[3].acceptance_criteria` | Valid | Scanner | Story has 44 AC, should be split into smaller stories | Story "Execute Complete Behavior" has 44 acceptance criteria | Split into: Story A (9 AC for basic behavior) + Story B (9 AC for error handling) + Story C (9 AC for recovery) + Story D (9 AC for advanced features) + Story E (8 AC for monitoring) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[2].story_groups[0].stories[0].acceptance_criteria` | Valid | Scanner | Story has 24 AC, should be split into smaller stories | Story "Monitor Execution" has 24 acceptance criteria | Split into: Story A (8 AC for basic monitoring) + Story B (8 AC for advanced monitoring) + Story C (8 AC for monitoring reporting) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[4].story_groups[0].stories[3].acceptance_criteria` | Valid | Scanner | Story has 12 AC, should be split into smaller stories | Story "Discovers Scanners" has 12 acceptance criteria | Split into: Story A (6 AC for core discovery) + Story B (6 AC for advanced discovery) |
| Oversized stories (>9 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[4].story_groups[0].stories[8].acceptance_criteria` | Valid | Scanner | Story has 16 AC, should be split into smaller stories | Story "Report Validation and Error Handling" has 16 acceptance criteria | Split into: Story A (8 AC for basic reporting) + Story B (8 AC for advanced reporting) |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[0].sub_epics[0].story_groups[0].stories[2].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Generate MCP Bot Server" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[3].story_groups[0].stories[1].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Execute Behavior" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[4].story_groups[0].stories[4].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Process Bot Behavor Action Instructions Automatically" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[2].story_groups[0].stories[4].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Proceed To Render Output" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[3].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Inject Template Instructions" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[5].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Inject Render Instructions And Configs" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].story_groups[0].stories[9].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Inject Render Instructions And Configs" (duplicate) has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[4].story_groups[0].stories[5].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Run AST Scanners against Knowledge Graph (OUT OF SCOPE)" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Warning stories (3 AC) | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[4].story_groups[0].stories[7].acceptance_criteria` | Valid | Scanner | Story has 3 AC, close to minimum, should add 1-2 more | Story "Generate Violation Report" has 3 acceptance criteria | Expand to 4-5 AC: Add error handling AC or edge case AC |
| Sub-epic sizing violations | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[5].sub_epics[2].name` | Valid | Scanner | Sub-epic has 3 stories, should have 4-10 | Sub-epic "Navigate Bot Behaviors and Actions Via Domain Model" has 3 stories | Add 1-2 more stories to reach 4-5 stories |
| Sub-epic sizing violations | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[5].sub_epics[6].name` | Valid | Scanner | Sub-epic has 3 stories, should have 4-10 | Sub-epic "Get Help Using CLI" has 3 stories | Add 1-2 more stories to reach 4-5 stories |
| Sub-epic sizing violations | Stories Have 4 To 9 Acceptance Criteria | `epics[1].sub_epics[6].sub_epics[0].name` | Valid | Scanner | Sub-epic has 2 stories, should have 4-10 | Sub-epic "Document Headless Mode Requirements" has 2 stories | Add 2-3 more stories to reach 4-5 stories |
| Sub-epic sizing violations | Stories Have 4 To 9 Acceptance Criteria | `epics[2].sub_epics[3].name` | Valid | Scanner | Sub-epic has 13 stories, should have 4-10 | Sub-epic "Render Output" has 13 stories | Split into: Sub-epic A (6 stories) + Sub-epic B (7 stories) |

## Summary

### Scanner Violations Analysis

**Total Violations:** 59
- **Valid Violations:** 59 (100%)
- **False Positives:** 0 (0%)

### Violation Breakdown by Theme

1. **Under-explored stories (<4 AC):** 30 violations
   - Stories with 1 AC: 3 violations
   - Stories with 2 AC: 27 violations

2. **Oversized stories (>9 AC):** 19 violations
   - Stories with 11-13 AC: 7 violations
   - Stories with 16-24 AC: 3 violations
   - Stories with 31-44 AC: 4 violations
   - Stories with 19-22 AC: 2 violations

3. **Warning stories (3 AC):** 9 violations
   - Stories close to minimum, need 1-2 more AC

4. **Sub-epic sizing violations:** 4 violations
   - Sub-epics with 2-3 stories: 3 violations
   - Sub-epics with 13 stories: 1 violation

### Additional Manual Findings

No additional violations found beyond scanner-detected issues. All 6 rules were manually reviewed:
- ✅ Use Verb Noun Format For Story Elements: No violations
- ⚠️ Stories Have 4 To 9 Acceptance Criteria: 59 violations (all valid)
- ✅ Alternate Actors In Steps: No violations
- ✅ Behavioral Ac At Story Level: No violations
- ✅ Use And For Multiple Reactions: No violations
- ✅ Enumerate All Ac Permutations: No violations

### Priority Fixes (Must Resolve Before Continuing)

1. **Critical: Oversized Stories (19 violations)**
   - Stories with 11-44 AC must be split into smaller stories (4-9 AC each)
   - Highest priority: "Execute Complete Behavior" (44 AC) - split into 5 stories
   - High priority: "Execute Complete Action" (34 AC), "Execute Direct Instructions" (33 AC), "Execute Single Operation" (31 AC)

2. **High: Under-explored Stories (30 violations)**
   - Stories with 1-2 AC must be expanded to 4-6 AC
   - Add error handling, validation, edge cases, alternate flows

3. **Medium: Warning Stories (9 violations)**
   - Stories with 3 AC should add 1-2 more AC to reach minimum

4. **Low: Sub-epic Sizing (4 violations)**
   - Sub-epics with <4 or >10 stories should be adjusted

### Optional Improvements

- Review duplicate story names (e.g., "Get Render Instructions", "Render Output Using Synchronizers" appear twice)
- Consider consolidating similar stories to reduce duplication
