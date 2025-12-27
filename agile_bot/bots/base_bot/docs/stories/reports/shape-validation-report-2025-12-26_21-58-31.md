# Validation Report - Shape

**Generated:** 2025-12-26 21:58:31
**Project:** base_bot
**Behavior:** shape
**Action:** validate

## Summary

Validated content against **8 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
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

- 🟨 **[Small And Testable](#small-and-testable)** - 20 violation(s) (EXECUTION_SUCCESS) - [View Details](#small-and-testable-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟨 **[Verb Noun Format](#verb-noun-format)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#verb-noun-format-violations)
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

### 🟨 Rule: <span id="small-and-testable">Small And Testable</span> - 20 VIOLATION(S) - [View Details](#small-and-testable-violations)
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

### 🟨 Rule: <span id="verb-noun-format">Verb Noun Format</span> - 2 VIOLATION(S) - [View Details](#verb-noun-format-violations)
**Description:** Use verb-noun format consistently across all hierarchy levels. Actor --> verb noun [qualifiers]. Actor is documented separately, NOT in the name. Focus on specific actions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

## Violations Found

**Total Violations:** 22
- **File-by-File Violations:** 22
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="verb-noun-format-violations">Verb Noun Format: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[5].sub_epics[2].story_groups[0].stories[3].name): Story name "Re-execute Current Operation Using CLI" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[2].story_groups[0].stories[5].name): Story name "proactively Validate knowledge against rules" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")

#### <span id="small-and-testable-violations">Small And Testable: 20 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Generate Bot Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Bot Tools): Story "Generate Bot Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Behavior Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Behavior Tools): Story "Generate Behavior Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate MCP Bot Server`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate MCP Bot Server): Story "Generate MCP Bot Server" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Behavior Action Tools`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Behavior Action Tools): Story "Generate Behavior Action Tools" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate BOT CLI code`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate BOT CLI code): Story "Generate BOT CLI code" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Command Files`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Cursor Command Files): Story "Generate Cursor Command Files" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Help): Story "Generate Help" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Awareness Files`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Cursor Awareness Files): Story "Generate Cursor Awareness Files" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help Parameters From Action Context Classes`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Help Parameters From Action Context Classes): Story "Generate Help Parameters From Action Context Classes" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate REPL Command Definitions`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate REPL Command Definitions): Story "Generate REPL Command Definitions" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate CLI Entry Point`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate CLI Entry Point): Story "Generate CLI Entry Point" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Cursor Commands`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Cursor Commands): Story "Generate Cursor Commands" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Help Documentation`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Help Documentation): Story "Generate Help Documentation" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Context Files`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Store Context Files): Story "Store Context Files" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Set Scope Through CLI Using String Parameters`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Set Scope Through CLI Using String Parameters): Story "Set Scope Through CLI Using String Parameters" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Clarification Data`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Store Clarification Data): Story "Store Clarification Data" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Save Final Assumptions and Decisions`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Save Final Assumptions and Decisions): Story "Save Final Assumptions and Decisions" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Store Strategy Data`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Store Strategy Data): Story "Store Strategy Data" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Create Build Scope`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Create Build Scope): Story "Create Build Scope" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Generate Violation Report`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/Generate Violation Report): Story "Generate Violation Report" appears to be an implementation operation - should be a step within a story that describes user/system outcome

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
*... and 53 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\shape-validation-report-2025-12-26_21-58-31.md`

