# Validation Report - Exploration

**Generated:** 2025-12-23 21:32:24
**Project:** base_bot
**Behavior:** exploration
**Action:** validate

## Summary

Validated content against **14 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟥 Overall Status: CRITICAL ISSUES

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 11 | Scanners ran without errors |
| 🟩 Clean Rules | 8 | No violations found |
| 🟥 Load Failed | 3 | Scanner could not be loaded |

**Total Rules:** 14
- **Rules with Scanners:** 14
  - 🟩 **Executed Successfully:** 11
  - 🟥 **Load Failed:** 3

### 🟩 Successfully Executed Scanners

- 🟨 **[Stories Developed And Tested In Days](#stories-developed-and-tested-in-days)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#stories-developed-and-tested-in-days-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
- 🟨 **[Scenarios On Story Docs](#scenarios-on-story-docs)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#scenarios-on-story-docs-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_on_story_docs_scanner.ScenariosOnStoryDocsScanner`
- 🟨 **[Map Sequential Spine Vs Optional Paths](#map-sequential-spine-vs-optional-paths)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟩 **[Given Uses State Language](#given-uses-state-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.given_state_not_actions_scanner.GivenStateNotActionsScanner`
- 🟩 **[Maintain Verb Noun Consistency](#maintain-verb-noun-consistency)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Scenarios Cover All Cases](#scenarios-cover-all-cases)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_cover_all_cases_scanner.ScenariosCoverAllCasesScanner`
- 🟩 **[Story Names Must Follow Verb Noun Format](#story-names-must-follow-verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Use Active Behavioral Language](#use-active-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Use Background For Common Setup](#use-background-for-common-setup)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.background_common_setup_scanner.BackgroundCommonSetupScanner`
- 🟩 **[Use Scenario Outline When Needed](#use-scenario-outline-when-needed)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.scenario_outline_scanner.ScenarioOutlineScanner`
- 🟩 **[Use Verb Noun Format For Story Elements](#use-verb-noun-format-for-story-elements)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`

### 🟥 Scanner Load Failures

- 🟥 **[Behavioral Ac At Story Level](#behavioral-ac-at-story-level)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.actions.validate.scanners.behavioral_ac_scanner.BehavioralACScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.actions.validate.scanners.behavioral_ac_scanner.BehavioralACScanner`
- 🟥 **[Enumerate All Ac Permutations](#enumerate-all-ac-permutations)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.actions.validate.scanners.enumerate_ac_permutations_scanner.EnumerateACPermutationsScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.actions.validate.scanners.enumerate_ac_permutations_scanner.EnumerateACPermutationsScanner`
- 🟥 **[Present Ac Consolidation](#present-ac-consolidation)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.actions.validate.scanners.ac_consolidation_scanner.ACConsolidationScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.actions.validate.scanners.ac_consolidation_scanner.ACConsolidationScanner`

## Validation Rules Checked

### 🟥 Rule: <span id="behavioral-ac-at-story-level">Behavioral Ac At Story Level</span> - FAILED
**Description:** Behavioral AC belongs at story level, written in story-graph.json (main epics section). Use When/Then format (NO Given clauses - save for scenarios). Each acceptance criteria is a SINGLE string containing one WHEN/THEN pair. AND can be part of the same acceptance criteria, but THEN and its AND must be together in the same string.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.behavioral_ac_scanner.BehavioralACScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.actions.validate.scanners.behavioral_ac_scanner.BehavioralACScanner`

### 🟥 Rule: <span id="enumerate-all-ac-permutations">Enumerate All Ac Permutations</span> - FAILED
**Description:** Enumerate ALL acceptance criteria permutations. Apply exhaustive logic decomposition at AC level.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.enumerate_ac_permutations_scanner.EnumerateACPermutationsScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.actions.validate.scanners.enumerate_ac_permutations_scanner.EnumerateACPermutationsScanner`

### 🟥 Rule: <span id="present-ac-consolidation">Present Ac Consolidation</span> - FAILED
**Description:** Present AC consolidation review BEFORE finalizing. Identify similar ACs, ask domain expert questions, wait for user confirmation.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.ac_consolidation_scanner.ACConsolidationScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.actions.validate.scanners.ac_consolidation_scanner.ACConsolidationScanner`

### 🟩 Rule: <span id="given-uses-state-language">Given Uses State Language</span> - CLEAN (0 violations)
**Description:** Given statements must use state-oriented language (not action-oriented). Given describes STATE, not actions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.given_state_not_actions_scanner.GivenStateNotActionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-verb-noun-consistency">Maintain Verb Noun Consistency</span> - CLEAN (0 violations)
**Description:** Maintain verb-noun consistency from epic to feature to story to scenario
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="scenarios-cover-all-cases">Scenarios Cover All Cases</span> - CLEAN (0 violations)
**Description:** Scenarios must cover happy path, edge cases, and error cases based on acceptance criteria.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_cover_all_cases_scanner.ScenariosCoverAllCasesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="story-names-must-follow-verb-noun-format">Story Names Must Follow Verb Noun Format</span> - CLEAN (0 violations)
**Description:** CRITICAL: Story names MUST follow Verb-Noun format (e.g., 'Move To Mob Leaders Turn', 'Determines Target from Strategy', 'Initiate Mob Attack'), and include italicized description showing component interactions (e.g., '*Combat Tracker moves to any mob member's turn, auto moves to mob leader's turn*'). The story name should be concise and action-oriented, while the description shows the component-to-component interactions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-active-behavioral-language">Use Active Behavioral Language</span> - CLEAN (0 violations)
**Description:** Use active behavioral language with action verbs. Describe behaviors, not tasks or capabilities.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-background-for-common-setup">Use Background For Common Setup</span> - CLEAN (0 violations)
**Description:** Use Background for repeated Given steps across 3+ scenarios. Background contains only Given/And steps (no When/Then).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.background_common_setup_scanner.BackgroundCommonSetupScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-scenario-outline-when-needed">Use Scenario Outline When Needed</span> - CLEAN (0 violations)
**Description:** Use Scenario Outline with Examples when story warrants concrete data: formulas need validation, domain has named entities, parameter variations exist.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.scenario_outline_scanner.ScenarioOutlineScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-verb-noun-format-for-story-elements">Use Verb Noun Format For Story Elements</span> - CLEAN (0 violations)
**Description:** Use verb-noun format for all story elements (epic names, feature names, story titles)
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="map-sequential-spine-vs-optional-paths">Map Sequential Spine Vs Optional Paths</span> - 5 VIOLATION(S) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="scenarios-on-story-docs">Scenarios On Story Docs</span> - 9 VIOLATION(S) - [View Details](#scenarios-on-story-docs-violations)
**Description:** CRITICAL SCOPE: Scenarios work on STORY documents (📝 *.md files), NOT feature documents. NEVER creates feature specification documents.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_on_story_docs_scanner.ScenariosOnStoryDocsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="stories-developed-and-tested-in-days">Stories Developed And Tested In Days</span> - 19 VIOLATION(S) - [View Details](#stories-developed-and-tested-in-days-violations)
**Description:** Write stories that can be developed and tested in a matter of days
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
**Execution Status:** EXECUTION_SUCCESS

## Violations Found

**Total Violations:** 33
- **File-by-File Violations:** 33
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="map-sequential-spine-vs-optional-paths-violations">Map Sequential Spine Vs Optional Paths: 5 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[2].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[2].sequential_order): Story "Enter Confirm Results" has sequential_order 2, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].sequential_order): Story "Provide Context For Instructions" has sequential_order 7, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

#### <span id="scenarios-on-story-docs-violations">Scenarios On Story Docs: 9 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].name): Story "Provide Context For Instructions" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].name): Story "Provide Story Scope Context For Instructions" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].name): Story "Provide File Scope Context For Instructions" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].name): Story "Store Scope Context" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].name): Story "Get Instructions and Display" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].name): Story "Submit Action and Display Results" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].name): Story "Confirm Action and Display Results" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].name): Story "Advance To Next Action" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].name): Story "Loop Back To Display State" has no scenarios or scenario_outlines in story-graph.json - scenarios should be in JSON (scenarios or scenario_outlines fields)

#### <span id="stories-developed-and-tested-in-days-violations">Stories Developed And Tested In Days: 19 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[0].name): Sub-epic "Initialize and Display Session" has 1 1 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria): Story "Show Available Behaviors and Actions" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].name): Sub-epic "Navigate Workflow" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[0].acceptance_criteria): Story "Navigate To Behavior" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[1].acceptance_criteria): Story "Navigate To Action" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[2].acceptance_criteria): Story "Enter Confirm Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].name): Sub-epic "Help" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[0].acceptance_criteria): Story "Request Help" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[1].acceptance_criteria): Story "Request Status" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[2].acceptance_criteria): Story "Show Action Parameter Help" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].acceptance_criteria): Story "Provide Context For Instructions" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].acceptance_criteria): Story "Provide Story Scope Context For Instructions" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].acceptance_criteria): Story "Provide File Scope Context For Instructions" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].acceptance_criteria): Story "Store Scope Context" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].acceptance_criteria): Story "Get Instructions and Display" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].acceptance_criteria): Story "Submit Action and Display Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].acceptance_criteria): Story "Confirm Action and Display Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].acceptance_criteria): Story "Advance To Next Action" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].acceptance_criteria): Story "Loop Back To Display State" has 3 3 acceptance criteria (should be 4-10)

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
*... and 254 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\exploration-validation-report-2025-12-23_21-32-21.md`

