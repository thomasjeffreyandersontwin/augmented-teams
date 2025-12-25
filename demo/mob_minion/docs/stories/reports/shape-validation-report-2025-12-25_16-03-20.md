# Validation Report - Shape

**Generated:** 2025-12-25 16:03:22
**Project:** mob_minion
**Behavior:** shape
**Action:** validate

## Summary

Validated content against **8 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 3 | Scanners ran without errors |
| 🟩 Clean Rules | 2 | No violations found |
| [i] No Scanner | 5 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 3
  - 🟩 **Executed Successfully:** 3
- [i] **Rules without Scanners:** 5

### 🟩 Successfully Executed Scanners

- 🟨 **[Small And Testable](#small-and-testable)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#small-and-testable-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟩 **[Outcome Oriented Language](#outcome-oriented-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
- 🟩 **[Verb Noun Format](#verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Active Business And Behavioral Language](#active-business-and-behavioral-language)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Lightweight And Precise](#lightweight-and-precise)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Valuable](#valuable)** - No scanner configured
- <span style="color: gray;">[i]</span> **[User And System Behavior](#user-and-system-behavior)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Story Map Existing Code](#story-map-existing-code)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="outcome-oriented-language">Outcome Oriented Language</span> - CLEAN (0 violations)
**Description:** Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="verb-noun-format">Verb Noun Format</span> - CLEAN (0 violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="active-business-and-behavioral-language">Active Business And Behavioral Language</span> - NO SCANNER
**Description:** Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
**Scanner:** Not configured

### [i] Rule: <span id="lightweight-and-precise">Lightweight And Precise</span> - NO SCANNER
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
**Scanner:** Not configured

### 🟨 Rule: <span id="small-and-testable">Small And Testable</span> - 2 VIOLATION(S) - [View Details](#small-and-testable-violations)
**Description:** Stories must be testable as complete interactions and deliverable independently. Balance testability with maintaining value and behavioral focus - stories should be small enough to test but large enough to matter.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="story-map-existing-code">Story Map Existing Code</span> - NO SCANNER
**Description:** When creating story maps from code, start with the outermost layer (entry points), analyze operations and domain concepts, create epics from higher-order goals, and lay out the story journey.
**Scanner:** Not configured

### [i] Rule: <span id="user-and-system-behavior">User And System Behavior</span> - NO SCANNER
**Description:** Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'. NOTE: This rule only applies when strategy decisions in planning.json specify flow_scope_and_granularity as 'Integration boundary level' or 'Intra-system level', OR drill_down_approach includes 'Dig deep on system interactions' or 'Dig deep on architectural pieces'. Check {project_area}/docs/stories/planning.json for these decisions.
**Scanner:** Not configured

### [i] Rule: <span id="valuable">Valuable</span> - NO SCANNER
**Description:** Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
**Scanner:** Not configured

## Violations Found

**Total Violations:** 2
- **File-by-File Violations:** 2
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="small-and-testable-violations">Small And Testable: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Create Mobs`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Create Mobs): Story "Create Mobs" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Configure Mob Strategy`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Configure Mob Strategy): Story "Configure Mob Strategy" appears to be an implementation operation - should be a step within a story that describes user/system outcome

## Validation Instructions

The following validation steps were performed:

1. ## Step 1: Scanner Violation Review
2. 
3. {{scanner_output}}
4. 
5. Carefully review all scanner-reported violations as follows:
6. 1. For each violation message, locate the corresponding element in the knowledge graph.
7. 2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
8. 3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
9. 4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
10. 5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
*... and 52 more instructions*

## Report Location

This report was automatically generated and saved to:
`demo\mob_minion\docs\stories\reports\shape-validation-report-2025-12-25_16-03-20.md`

