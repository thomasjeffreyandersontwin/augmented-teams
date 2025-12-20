# Validation Report - Prioritization

**Generated:** 2025-12-20 01:09:33
**Project:** mob_minion
**Behavior:** prioritization
**Action:** validate

## Summary

Validated content against **11 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `solution-domain-model-description.md`
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 8 | Scanners ran without errors |
| 🟩 Clean Rules | 6 | No violations found |
| [i] No Scanner | 3 | Rule has no scanner configured |

**Total Rules:** 11
- **Rules with Scanners:** 8
  - 🟩 **Executed Successfully:** 8
- [i] **Rules without Scanners:** 3

### 🟩 Successfully Executed Scanners

- 🟨 **[Map Sequential Spine Vs Optional Paths](#map-sequential-spine-vs-optional-paths)** - 12 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟨 **[Stories Developed And Tested In Days](#stories-developed-and-tested-in-days)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#stories-developed-and-tested-in-days-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
- 🟩 **[Design Vertical Slice Increments](#design-vertical-slice-increments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_slice_scanner.VerticalSliceScanner`
- 🟩 **[Folder Structure Matches Hierarchy](#folder-structure-matches-hierarchy)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.increment_folder_structure_scanner.IncrementFolderStructureScanner`
- 🟩 **[Maintain Verb Noun Consistency](#maintain-verb-noun-consistency)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Story Names Must Follow Verb Noun Format](#story-names-must-follow-verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Use Active Behavioral Language](#use-active-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Use Verb Noun Format For Story Elements](#use-verb-noun-format-for-story-elements)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Apply Quality Tradeoffs For Minimal Spine](#apply-quality-tradeoffs-for-minimal-spine)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Archive Not Delete](#archive-not-delete)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Identify Marketable Increments](#identify-marketable-increments)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="design-vertical-slice-increments">Design Vertical Slice Increments</span> - CLEAN (0 violations)
**Description:** CRITICAL: Increments MUST be designed as vertical slices that deliver end-to-end working flows across multiple features/epics, NOT horizontal layers that complete one feature/epic at a time. Each increment must demonstrate complete working flow from start to finish.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_slice_scanner.VerticalSliceScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="folder-structure-matches-hierarchy">Folder Structure Matches Hierarchy</span> - CLEAN (0 violations)
**Description:** Folder structure must exactly match story map hierarchy. Epic/feature folders created inside docs/stories/ directory.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.increment_folder_structure_scanner.IncrementFolderStructureScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-verb-noun-consistency">Maintain Verb Noun Consistency</span> - CLEAN (0 violations)
**Description:** Maintain verb-noun consistency from epic to feature to story to scenario
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="story-names-must-follow-verb-noun-format">Story Names Must Follow Verb Noun Format</span> - CLEAN (0 violations)
**Description:** CRITICAL: Story names MUST follow Verb-Noun format (e.g., 'Move To Mob Leaders Turn', 'Determines Target from Strategy', 'Initiate Mob Attack'), and include italicized description showing component interactions (e.g., '*Combat Tracker moves to any mob member's turn, auto moves to mob leader's turn*'). The story name should be concise and action-oriented, while the description shows the component-to-component interactions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-active-behavioral-language">Use Active Behavioral Language</span> - CLEAN (0 violations)
**Description:** Use active behavioral language with action verbs. Describe behaviors, not tasks or capabilities.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-verb-noun-format-for-story-elements">Use Verb Noun Format For Story Elements</span> - CLEAN (0 violations)
**Description:** Use verb-noun format for all story elements (epic names, feature names, story titles)
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="apply-quality-tradeoffs-for-minimal-spine">Apply Quality Tradeoffs For Minimal Spine</span> - NO SCANNER
**Description:** Apply quality trade-offs to create thin slicing spine and later increments. Decide what quality the spine will have, what parts will be manual, what logic can be excluded, and how to prioritize adding quality in later increments.
**Scanner:** Not configured

### [i] Rule: <span id="archive-not-delete">Archive Not Delete</span> - NO SCANNER
**Description:** NEVER delete files or folders. Archive obsolete items to map/z_archive/[timestamp]/ instead.
**Scanner:** Not configured

### [i] Rule: <span id="identify-marketable-increments">Identify Marketable Increments</span> - NO SCANNER
**Description:** Identify marketable increments of value during prioritization, creating increment-organized view of the story map with delivery priorities and relative sizing.
**Scanner:** Not configured

### 🟨 Rule: <span id="map-sequential-spine-vs-optional-paths">Map Sequential Spine Vs Optional Paths</span> - 12 VIOLATION(S) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="stories-developed-and-tested-in-days">Stories Developed And Tested In Days</span> - 9 VIOLATION(S) - [View Details](#stories-developed-and-tested-in-days-violations)
**Description:** Write stories that can be developed and tested in a matter of days
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
**Execution Status:** EXECUTION_SUCCESS

## Violations Found

**Total Violations:** 21
- **File-by-File Violations:** 21
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="map-sequential-spine-vs-optional-paths-violations">Map Sequential Spine Vs Optional Paths: 12 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

#### <span id="stories-developed-and-tested-in-days-violations">Stories Developed And Tested In Days: 9 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[0].name): Sub-epic "Form Mob" has 3 3 stories (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[1].name): Sub-epic "Expand Mob" has 2 2 stories (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[2].name): Sub-epic "Reduce Mob" has 2 2 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].name): Sub-epic "Coordinate Attack" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].name): Sub-epic "Resolve Attack" has 3 3 stories (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[2].sub_epics[0].name): Sub-epic "Define Mob Template" has 2 2 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[2].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[2].sub_epics[1].name): Sub-epic "Spawn From Template" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[3].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[3].sub_epics[0].name): Sub-epic "Choose Pathfinding Algorithm" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[3].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[3].sub_epics[2].name): Sub-epic "Execute Mob Movement" has 3 3 stories (should be 4-10)

## Validation Instructions

The following validation steps were performed:

1. **MANDATORY: Before validating any content, you MUST load and review the project's context files:**
2. 1. Load `{project_area}/docs/stories/clarification.json` - Contains key questions and evidence (generated file)
3. 2. Load `{project_area}/docs/stories/planning.json` - Contains assumptions and decisions (generated file)
4. 3. Load `{project_area}/docs/context/input.txt` (or similar) - Original input/source material if needed for validation (original context)
5. 
6. **CRITICAL: File locations:**
7. - **Generated files:** `{project_area}/docs/stories/clarification.json`, `{project_area}/docs/stories/planning.json`
8. - **Original input:** `{project_area}/docs/context/input.txt` and other original context files
9. 
10. These files contain critical requirements, decisions, and context that MUST be checked against during validation.
*... and 248 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\demo\mob_minion\docs\stories\prioritization-validation-report.md`
