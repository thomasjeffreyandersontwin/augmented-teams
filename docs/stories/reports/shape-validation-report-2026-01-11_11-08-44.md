# Validation Report - Shape

**Generated:** 2026-01-11 11:08:47
**Project:** augmented-teams
**Behavior:** shape
**Action:** validate

## Summary

Validated content against **8 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: ALL CLEAN

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 4 | Scanners ran without errors |
| 🟩 Clean Rules | 4 | No violations found |
| [i] No Scanner | 4 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 4
  - 🟩 **Executed Successfully:** 4
- [i] **Rules without Scanners:** 4

### 🟩 Successfully Executed Scanners

- 🟩 **[Active Business And Behavioral Language](#active-business-and-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Outcome Oriented Language](#outcome-oriented-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
- 🟩 **[Small And Testable](#small-and-testable)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟩 **[Verb Noun Format](#verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Lightweight And Precise](#lightweight-and-precise)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Valuable](#valuable)** - No scanner configured
- <span style="color: gray;">[i]</span> **[User And System Behavior](#user-and-system-behavior)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Story Map Existing Code](#story-map-existing-code)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="active-business-and-behavioral-language">Active Business And Behavioral Language</span> - CLEAN (0 violations)
**Description:** Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="outcome-oriented-language">Outcome Oriented Language</span> - CLEAN (0 violations)
**Description:** Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="small-and-testable">Small And Testable</span> - CLEAN (0 violations)
**Description:** Stories must be testable as complete interactions and deliverable independently. Balance testability with maintaining value and behavioral focus - stories should be small enough to test but large enough to matter.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="verb-noun-format">Verb Noun Format</span> - CLEAN (0 violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="lightweight-and-precise">Lightweight And Precise</span> - NO SCANNER
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
**Scanner:** Not configured

### [i] Rule: <span id="story-map-existing-code">Story Map Existing Code</span> - NO SCANNER
**Description:** When creating story maps from code, start with the outermost layer (entry points), analyze operations, create epics from higher-order goals, and lay out the story journey.
**Scanner:** Not configured

### [i] Rule: <span id="user-and-system-behavior">User And System Behavior</span> - NO SCANNER
**Description:** Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'. NOTE: This rule only applies when strategy decisions in planning.json specify flow_scope_and_granularity as 'Integration boundary level' or 'Intra-system level', OR drill_down_approach includes 'Dig deep on system interactions' or 'Dig deep on architectural pieces'. Check {project_area}/docs/stories/planning.json for these decisions.
**Scanner:** Not configured

### [i] Rule: <span id="valuable">Valuable</span> - NO SCANNER
**Description:** Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
**Scanner:** Not configured

## Violations Found

🟩 **No violations found.** All rules passed validation.

## Validation Instructions

The following validation steps were performed:

1. validate base instructions
2. 
=== SCANNER EXECUTION STATUS ===
3. Successfully Executed: 4
4. Load Failed: 0
5. Execution Failed: 0
6. No Scanner: 4
7. 
8. All scanners executed successfully.
9. === END SCANNER STATUS ===

10. 
Validation report: [docs\stories\reports\shape-validation-report-2026-01-11_11-08-44.md](vscode://file/C:/dev/augmented-teams/docs/stories/reports/shape-validation-report-2026-01-11_11-08-44.md)

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\docs\stories\reports\shape-validation-report-2026-01-11_11-08-44.md`

