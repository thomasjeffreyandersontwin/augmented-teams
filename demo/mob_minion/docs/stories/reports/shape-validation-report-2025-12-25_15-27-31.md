# Validation Report - Shape

**Generated:** 2025-12-25 15:27:34
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
| 🟩 Clean Rules | 1 | No violations found |
| [i] No Scanner | 5 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 3
  - 🟩 **Executed Successfully:** 3
- [i] **Rules without Scanners:** 5

### 🟩 Successfully Executed Scanners

- 🟨 **[Small And Testable](#small-and-testable)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#small-and-testable-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟨 **[Verb Noun Format](#verb-noun-format)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#verb-noun-format-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Outcome Oriented Language](#outcome-oriented-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`

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
**Description:** Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'.
**Scanner:** Not configured

### [i] Rule: <span id="valuable">Valuable</span> - NO SCANNER
**Description:** Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
**Scanner:** Not configured

### 🟨 Rule: <span id="verb-noun-format">Verb Noun Format</span> - 1 VIOLATION(S) - [View Details](#verb-noun-format-violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

## Violations Found

**Total Violations:** 3
- **File-by-File Violations:** 3
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="verb-noun-format-violations">Verb Noun Format: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].name): Sub_epic name "Strategy Types" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")

#### <span id="small-and-testable-violations">Small And Testable: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Create Mobs`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Create Mobs): Story "Create Mobs" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Configure Mob Strategy`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Configure Mob Strategy): Story "Configure Mob Strategy" appears to be an implementation operation - should be a step within a story that describes user/system outcome

## Validation Instructions

The following validation steps were performed:

1. Review previous clarification and strategy data, then validate the content against behavior-specific rules to identify violations and ensure compliance.
2. 
3. **Your task:**
4. 1. Examine the content to be validated (stories, code files, test files, scenarios, etc.)
5. 2. Check content against behavior-specific validation rules
6. 3. Identify any violations with specific examples
7. 4. Verify content incorporates all requirements from clarification and strategy data
8. 5. Present the validation results to the user for review and final confirmation.
9. **Format:**
10. **Rules {rule} Status:** Pass | Violations Found [count] | Suggested Corrections [how to fix violation]
*... and 16 more instructions*

## Report Location

This report was automatically generated and saved to:
`demo\mob_minion\docs\stories\reports\shape-validation-report-2025-12-25_15-27-31.md`

