# Validation Report - Shape

**Generated:** 2025-12-30 16:25:24
**Project:** mob_minion
**Behavior:** shape
**Action:** validate

## Summary

Validated story map and domain model against **8 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 4 | Scanners ran without errors |
| 🟩 Clean Rules | 1 | No violations found |
| [i] No Scanner | 4 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 4
  - 🟩 **Executed Successfully:** 4
- [i] **Rules without Scanners:** 4

### 🟩 Successfully Executed Scanners

- 🟨 **[Active Business And Behavioral Language](#active-business-and-behavioral-language)** - 16 violation(s) (EXECUTION_SUCCESS) - [View Details](#active-business-and-behavioral-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟨 **[Verb Noun Format](#verb-noun-format)** - 16 violation(s) (EXECUTION_SUCCESS) - [View Details](#verb-noun-format-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
- 🟨 **[Small And Testable](#small-and-testable)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#small-and-testable-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟩 **[Outcome Oriented Language](#outcome-oriented-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Lightweight And Precise](#lightweight-and-precise)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Valuable](#valuable)** - No scanner configured
- <span style="color: gray;">[i]</span> **[User And System Behavior](#user-and-system-behavior)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Story Map Existing Code](#story-map-existing-code)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="outcome-oriented-language">Outcome Oriented Language</span> - CLEAN (0 violations)
**Description:** Use outcome-oriented language over mechanism-oriented language. Focus on what is created or achieved, not how it's shown or communicated.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.communication_verb_scanner.CommunicationVerbScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="active-business-and-behavioral-language">Active Business And Behavioral Language</span> - 16 VIOLATION(S) - [View Details](#active-business-and-behavioral-language-violations)
**Description:** Use active business language focused on user/system behavior. Describe what actors do with clear action verbs, not technical implementation or passive constructions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="lightweight-and-precise">Lightweight And Precise</span> - NO SCANNER
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
**Scanner:** Not configured

### 🟨 Rule: <span id="small-and-testable">Small And Testable</span> - 2 VIOLATION(S) - [View Details](#small-and-testable-violations)
**Description:** Stories must be testable as complete interactions and deliverable independently. Balance testability with maintaining value and behavioral focus - stories should be small enough to test but large enough to matter.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="story-map-existing-code">Story Map Existing Code</span> - NO SCANNER
**Description:** When creating story maps from code, start with the outermost layer (entry points), analyze operations, create epics from higher-order goals, and lay out the story journey.
**Scanner:** Not configured

### [i] Rule: <span id="user-and-system-behavior">User And System Behavior</span> - NO SCANNER
**Description:** Stories should capture both user and system behavior. User-facing stories show user actions with system responses. System stories capture system-to-system interactions and should be marked with story_type: 'system'. NOTE: This rule only applies when strategy decisions in planning.json specify flow_scope_and_granularity as 'Integration boundary level' or 'Intra-system level', OR drill_down_approach includes 'Dig deep on system interactions' or 'Dig deep on architectural pieces'. Check {project_area}/docs/stories/planning.json for these decisions.
**Scanner:** Not configured

### [i] Rule: <span id="valuable">Valuable</span> - NO SCANNER
**Description:** Stories must deliver independent value as complete functional accomplishments. Balance value with testability - stories should be valuable enough to matter but small enough to deliver quickly. Not just data access or isolated operations.
**Scanner:** Not configured

### 🟨 Rule: <span id="verb-noun-format">Verb Noun Format</span> - 16 VIOLATION(S) - [View Details](#verb-noun-format-violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

## Violations Found

**Total Violations:** 34
- **File-by-File Violations:** 34
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="verb-noun-format-violations">Verb Noun Format: 16 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].name): Epic name "Map Foundry API" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[0].name): Sub_epic name "Map Token System" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[0].story_groups[0].stories[1].name): Story name "Update Token State" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[1].name): Sub_epic name "Map Actor System" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[1].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[1].story_groups[0].stories[0].name): Story name "Load Actor Statistics" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[2].name): Sub_epic name "Map Combat System" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[2].story_groups[0].stories[0].name): Story name "Register Combatant In Tracker" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[3].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[3].name): Sub_epic name "Map Targeting System" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[3].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[3].story_groups[0].stories[1].name): Story name "Set Target" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[0].story_groups[0].stories[1].name): Story name "Group Minions Into Mob" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].story_groups[0].stories[0].name): Story name "Add Minions To Mob" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].story_groups[0].stories[1].name): Story name "Remove Minions From Mob" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].name): Sub_epic name "Spawn Mob" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].story_groups[0].stories[0].name): Story name "Spawn Mob From Template" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].story_groups[0].stories[1].name): Story name "Spawn Mob From Actors" contains actor prefix (e.g., "Customer") - use verb-noun format without actor
- <span style="color: red;">[X]</span> **ERROR** - [`epics[3].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[3].sub_epics[1].name): Sub_epic name "Coordinate Attack" contains actor prefix (e.g., "Customer") - use verb-noun format without actor

#### <span id="active-business-and-behavioral-language-violations">Active Business And Behavioral Language: 16 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].name): Epic name "Map Foundry API" has actor "Map" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Foundry API"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[0].name): Sub_epic name "Map Token System" has actor "Map" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Token System"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[0].story_groups[0].stories[1].name): Story name "Update Token State" has actor "Update" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Token State"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[1].name): Sub_epic name "Map Actor System" has actor "Map" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Actor System"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[1].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[1].story_groups[0].stories[0].name): Story name "Load Actor Statistics" has actor "Load" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Actor Statistics"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[2].name): Sub_epic name "Map Combat System" has actor "Map" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Combat System"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[2].story_groups[0].stories[0].name): Story name "Register Combatant In Tracker" has actor "Register" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Combatant In Tracker"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[3].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[3].name): Sub_epic name "Map Targeting System" has actor "Map" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Targeting System"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[3].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[3].story_groups[0].stories[1].name): Story name "Set Target" has actor "Set" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Target"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[0].story_groups[0].stories[1].name): Story name "Group Minions Into Mob" has actor "Group" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Minions Into Mob"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].story_groups[0].stories[0].name): Story name "Add Minions To Mob" has actor "Add" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Minions To Mob"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].story_groups[0].stories[1].name): Story name "Remove Minions From Mob" has actor "Remove" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Minions From Mob"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].name): Sub_epic name "Spawn Mob" has actor "Spawn" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Mob"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].story_groups[0].stories[0].name): Story name "Spawn Mob From Template" has actor "Spawn" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Mob From Template"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].story_groups[0].stories[1].name): Story name "Spawn Mob From Actors" has actor "Spawn" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Mob From Actors"
- <span style="color: red;">[X]</span> **ERROR** - [`epics[3].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[3].sub_epics[1].name): Sub_epic name "Coordinate Attack" has actor "Coordinate" in the name - actor should be in "users" field, not in name. Use Verb-Noun format: "Attack"

#### <span id="small-and-testable-violations">Small And Testable: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Set Target`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Set Target): Story "Set Target" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Apply Strategy Criteria`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Apply Strategy Criteria): Story "Apply Strategy Criteria" appears to be an implementation operation - should be a step within a story that describes user/system outcome

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
*... and 54 more instructions*

## Report Location

This report was automatically generated and saved to:
`demo\mob_minion\docs\stories\reports\shape-validation-report-2025-12-30_16-25-22.md`

