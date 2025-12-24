# Validation Report - Scenarios

**Generated:** 2025-12-23 22:41:42
**Project:** base_bot
**Behavior:** scenarios
**Action:** validate

## Summary

Validated content against **25 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 22 | Scanners ran without errors |
| 🟩 Clean Rules | 18 | No violations found |
| [i] No Scanner | 3 | Rule has no scanner configured |

**Total Rules:** 25
- **Rules with Scanners:** 22
  - 🟩 **Executed Successfully:** 22
- [i] **Rules without Scanners:** 3

### 🟩 Successfully Executed Scanners

- 🟨 **[Stories Developed And Tested In Days Copy](#stories-developed-and-tested-in-days copy)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#stories-developed-and-tested-in-days copy-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
- 🟨 **[Stories Developed And Tested In Days](#stories-developed-and-tested-in-days)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#stories-developed-and-tested-in-days-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
- 🟨 **[Map Sequential Spine Vs Optional Paths Copy](#map-sequential-spine-vs-optional-paths copy)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths copy-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟨 **[Map Sequential Spine Vs Optional Paths](#map-sequential-spine-vs-optional-paths)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟩 **[Given Describes Preconditions Not Functionality](#given-describes-preconditions-not-functionality)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.given_precondition_scanner.GivenPreconditionScanner`
- 🟩 **[Given Describes State Not Actions](#given-describes-state-not-actions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.given_state_not_actions_scanner.GivenStateNotActionsScanner`
- 🟩 **[Given Uses State Language](#given-uses-state-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.given_state_not_actions_scanner.GivenStateNotActionsScanner`
- 🟩 **[Maintain Verb Noun Consistency Copy](#maintain-verb-noun-consistency copy)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Maintain Verb Noun Consistency](#maintain-verb-noun-consistency)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Scenario Steps Start With Scenario Specific Given](#scenario-steps-start-with-scenario-specific-given)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.scenario_specific_given_scanner.ScenarioSpecificGivenScanner`
- 🟩 **[Scenarios Cover All Cases](#scenarios-cover-all-cases)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_cover_all_cases_scanner.ScenariosCoverAllCasesScanner`
- 🟩 **[Scenarios On Story Docs](#scenarios-on-story-docs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_on_story_docs_scanner.ScenariosOnStoryDocsScanner`
- 🟩 **[Stories Follow Invest Principles](#stories-follow-invest-principles)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.invest_principles_scanner.InvestPrinciplesScanner`
- 🟩 **[Story Filename Matches Story Name](#story-filename-matches-story-name)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_filename_scanner.StoryFilenameScanner`
- 🟩 **[Story Names Must Follow Verb Noun Format Copy](#story-names-must-follow-verb-noun-format copy)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Story Names Must Follow Verb Noun Format](#story-names-must-follow-verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Use Active Behavioral Language Copy](#use-active-behavioral-language copy)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Use Active Behavioral Language](#use-active-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Use Background For Common Setup](#use-background-for-common-setup)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.background_common_setup_scanner.BackgroundCommonSetupScanner`
- 🟩 **[Use Verb Noun Format For Story Elements Copy](#use-verb-noun-format-for-story-elements copy)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Use Verb Noun Format For Story Elements](#use-verb-noun-format-for-story-elements)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟩 **[Write Plain English Scenarios](#write-plain-english-scenarios)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.plain_english_scenarios_scanner.PlainEnglishScenariosScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Map Table Columns To Scenario Parameters](#map-table-columns-to-scenario-parameters)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Specify Constants And Stub Values](#specify-constants-and-stub-values)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Domain Rich Language In Testing Tables](#use-domain-rich-language-in-testing-tables)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="given-describes-preconditions-not-functionality">Given Describes Preconditions Not Functionality</span> - CLEAN (0 violations)
**Description:** CRITICAL: Given statements describe PRECONDITIONS (what exists before the test), NOT the functionality being tested. If you're describing WHAT the system does or HOW it behaves, that belongs in Then statements, not Given.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.given_precondition_scanner.GivenPreconditionScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="given-describes-state-not-actions">Given Describes State Not Actions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Given statements describe STATE/CONFIGURATION, never actions or events. The first action in a scenario is ALWAYS a When, never a Given. Given sets up preconditions, When triggers the behavior being tested.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.given_state_not_actions_scanner.GivenStateNotActionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="given-uses-state-language">Given Uses State Language</span> - CLEAN (0 violations)
**Description:** Given statements must use state-oriented language (not action-oriented). Given describes STATE, not actions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.given_state_not_actions_scanner.GivenStateNotActionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-verb-noun-consistency copy">Maintain Verb Noun Consistency Copy</span> - CLEAN (0 violations)
**Description:** Maintain verb-noun consistency from epic to feature to story to scenario
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-verb-noun-consistency">Maintain Verb Noun Consistency</span> - CLEAN (0 violations)
**Description:** Maintain verb-noun consistency from epic to feature to story to scenario
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="scenario-steps-start-with-scenario-specific-given">Scenario Steps Start With Scenario Specific Given</span> - CLEAN (0 violations)
**Description:** CRITICAL: Each scenario's Steps section starts with Given steps for scenario-specific setup. Background steps are automatically applied before scenario Steps. Scenario Steps should contain setup specific to THIS scenario only, not common setup that belongs in Background.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.scenario_specific_given_scanner.ScenarioSpecificGivenScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="scenarios-cover-all-cases">Scenarios Cover All Cases</span> - CLEAN (0 violations)
**Description:** Scenarios must cover happy path, edge cases, and error cases based on acceptance criteria.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_cover_all_cases_scanner.ScenariosCoverAllCasesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="scenarios-on-story-docs">Scenarios On Story Docs</span> - CLEAN (0 violations)
**Description:** CRITICAL SCOPE: Scenarios must be in story-graph.json (in scenarios or scenario_outlines fields), NOT in separate markdown files. NEVER creates feature specification documents.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_on_story_docs_scanner.ScenariosOnStoryDocsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="stories-follow-invest-principles">Stories Follow Invest Principles</span> - CLEAN (0 violations)
**Description:** Ensure stories follow INVEST principles (Independent, Negotiable, Valuable, Estimable, Small, Testable)
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.invest_principles_scanner.InvestPrinciplesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="story-filename-matches-story-name">Story Filename Matches Story Name</span> - CLEAN (0 violations)
**Description:** CRITICAL: Story filenames must match the story name exactly (no actor prefix). Actor information belongs in story description or acceptance criteria, NOT in the filename.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.story_filename_scanner.StoryFilenameScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="story-names-must-follow-verb-noun-format copy">Story Names Must Follow Verb Noun Format Copy</span> - CLEAN (0 violations)
**Description:** CRITICAL: Story names MUST follow Verb-Noun format (e.g., 'Move To Mob Leaders Turn', 'Determines Target from Strategy', 'Initiate Mob Attack'), and include italicized description showing component interactions (e.g., '*Combat Tracker moves to any mob member's turn, auto moves to mob leader's turn*'). The story name should be concise and action-oriented, while the description shows the component-to-component interactions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="story-names-must-follow-verb-noun-format">Story Names Must Follow Verb Noun Format</span> - CLEAN (0 violations)
**Description:** CRITICAL: Story names MUST follow Verb-Noun format (e.g., 'Move To Mob Leaders Turn', 'Determines Target from Strategy', 'Initiate Mob Attack'), and include italicized description showing component interactions (e.g., '*Combat Tracker moves to any mob member's turn, auto moves to mob leader's turn*'). The story name should be concise and action-oriented, while the description shows the component-to-component interactions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-active-behavioral-language copy">Use Active Behavioral Language Copy</span> - CLEAN (0 violations)
**Description:** Use active behavioral language with action verbs. Describe behaviors, not tasks or capabilities.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-active-behavioral-language">Use Active Behavioral Language</span> - CLEAN (0 violations)
**Description:** Use active behavioral language with action verbs. Describe behaviors, not tasks or capabilities.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-background-for-common-setup">Use Background For Common Setup</span> - CLEAN (0 violations)
**Description:** CRITICAL: Background section is ONLY for common setup steps shared across 3+ scenarios. DO NOT include scenario-specific setup here. Background contains only Given/And steps (no When/Then). Scenario-specific setup goes in scenario Steps as Given steps, not in Background.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.background_common_setup_scanner.BackgroundCommonSetupScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-verb-noun-format-for-story-elements copy">Use Verb Noun Format For Story Elements Copy</span> - CLEAN (0 violations)
**Description:** Use verb-noun format for all story elements (epic names, feature names, story titles)
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-verb-noun-format-for-story-elements">Use Verb Noun Format For Story Elements</span> - CLEAN (0 violations)
**Description:** Use verb-noun format for all story elements (epic names, feature names, story titles)
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="write-plain-english-scenarios">Write Plain English Scenarios</span> - CLEAN (0 violations)
**Description:** Write scenarios in plain English. NO variables, NO placeholders, NO Scenario Outlines, NO Examples tables at this stage.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.plain_english_scenarios_scanner.PlainEnglishScenariosScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="map-sequential-spine-vs-optional-paths copy">Map Sequential Spine Vs Optional Paths Copy</span> - 5 VIOLATION(S) - [View Details](#map-sequential-spine-vs-optional-paths copy-violations)
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="map-sequential-spine-vs-optional-paths">Map Sequential Spine Vs Optional Paths</span> - 5 VIOLATION(S) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 5 more rules*

## Violations Found

**Total Violations:** 38
- **File-by-File Violations:** 38
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="map-sequential-spine-vs-optional-paths copy-violations">Map Sequential Spine Vs Optional Paths Copy: 5 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[0].sequential_order): Story "Navigate To Behavior" has sequential_order 3, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].sequential_order): Story "Provide Context For Instructions" has sequential_order 7, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

#### <span id="map-sequential-spine-vs-optional-paths-violations">Map Sequential Spine Vs Optional Paths: 5 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].story_groups[0].stories[0].sequential_order): Story "Navigate To Behavior" has sequential_order 3, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[0].sequential_order): Story "Provide Context For Instructions" has sequential_order 7, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

#### <span id="stories-developed-and-tested-in-days copy-violations">Stories Developed And Tested In Days Copy: 14 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[0].name): Sub-epic "Initialize and Display Session" has 1 1 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria): Story "Show Available Behaviors and Actions" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].name): Sub-epic "Navigate Workflow" has 2 2 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].name): Sub-epic "Help" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[0].acceptance_criteria): Story "Request Help" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[2].acceptance_criteria): Story "Show Current Behavior Action Help" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].acceptance_criteria): Story "Provide Story Scope Context For Instructions" has 2 2 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].acceptance_criteria): Story "Provide File Scope Context For Instructions" has 2 2 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].acceptance_criteria): Story "Store Scope Context" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].acceptance_criteria): Story "Get Instructions and Display" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].acceptance_criteria): Story "Submit Action and Display Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].acceptance_criteria): Story "Confirm Action and Display Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].acceptance_criteria): Story "Advance To Next Action" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].acceptance_criteria): Story "Loop Back To Display State" has 1 1 acceptance criteria (should be 4-10)

#### <span id="stories-developed-and-tested-in-days-violations">Stories Developed And Tested In Days: 14 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[0].name): Sub-epic "Initialize and Display Session" has 1 1 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria): Story "Show Available Behaviors and Actions" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[1].name): Sub-epic "Navigate Workflow" has 2 2 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].name): Sub-epic "Help" has 3 3 stories (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[0].acceptance_criteria): Story "Request Help" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[2].story_groups[0].stories[2].acceptance_criteria): Story "Show Current Behavior Action Help" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[1].acceptance_criteria): Story "Provide Story Scope Context For Instructions" has 2 2 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[2].acceptance_criteria): Story "Provide File Scope Context For Instructions" has 2 2 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[3].acceptance_criteria): Story "Store Scope Context" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[4].acceptance_criteria): Story "Get Instructions and Display" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[5].acceptance_criteria): Story "Submit Action and Display Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[6].acceptance_criteria): Story "Confirm Action and Display Results" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[7].acceptance_criteria): Story "Advance To Next Action" has 3 3 acceptance criteria (should be 4-10)
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].sub_epics[3].story_groups[0].stories[8].acceptance_criteria): Story "Loop Back To Display State" has 1 1 acceptance criteria (should be 4-10)

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
*... and 250 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\scenarios-validation-report-2025-12-23_22-41-40.md`

