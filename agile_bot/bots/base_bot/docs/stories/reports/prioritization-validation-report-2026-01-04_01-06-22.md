# Validation Report - Prioritization

**Generated:** 2026-01-04 01:06:22
**Project:** base_bot
**Behavior:** prioritization
**Action:** validate

## Summary

Validated content against **5 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 2 | Scanners ran without errors |
| 🟩 Clean Rules | 1 | No violations found |
| [i] No Scanner | 3 | Rule has no scanner configured |

**Total Rules:** 5
- **Rules with Scanners:** 2
  - 🟩 **Executed Successfully:** 2
- [i] **Rules without Scanners:** 3

### 🟩 Successfully Executed Scanners

- 🟨 **[Map Sequential Spine Vs Optional Paths](#map-sequential-spine-vs-optional-paths)** - 30 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟩 **[Design Vertical Slice Increments](#design-vertical-slice-increments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_slice_scanner.VerticalSliceScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Apply Quality Tradeoffs For Minimal Spine](#apply-quality-tradeoffs-for-minimal-spine)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Identify Marketable Increments](#identify-marketable-increments)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Prioritize Architectural Risk Validation](#prioritize-architectural-risk-validation)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="design-vertical-slice-increments">Design Vertical Slice Increments</span> - CLEAN (0 violations)
**Description:** Create increments that are vertical slices that deliver end-to-end working flows across multiple features/epics, NOT horizontal layers that complete one feature/epic at a time. Each increment must demonstrate complete working flow from start to finish.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.vertical_slice_scanner.VerticalSliceScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="apply-quality-tradeoffs-for-minimal-spine">Apply Quality Tradeoffs For Minimal Spine</span> - NO SCANNER
**Description:** Apply quality trade-offs to create thin slicing spine and later increments. Decide what quality the spine will have, what parts will be manual, what logic can be excluded, and how to prioritize adding quality in later increments.
**Scanner:** Not configured

### [i] Rule: <span id="identify-marketable-increments">Identify Marketable Increments</span> - NO SCANNER
**Description:** Identify marketable increments of value during prioritization. Name increments with business value terms that stakeholders understand, not technical implementation terms.
**Scanner:** Not configured

### 🟨 Rule: <span id="map-sequential-spine-vs-optional-paths">Map Sequential Spine Vs Optional Paths</span> - 30 VIOLATION(S) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
**Description:** When mapping stories, carefully distinguish between sequential spine (essential path) and optional paths, alternate routes, or additional functionality that is not strictly essential. Sequential stories form the mandatory flow; optional stories are alternatives, enhancements, or non-essential features.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.spine_optional_scanner.SpineOptionalScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="prioritize-architectural-risk-validation">Prioritize Architectural Risk Validation</span> - NO SCANNER
**Description:** Prioritize early increments to validate architectural risks and technology decisions. Build risky integrations, test unfamiliar technologies, and validate solution feasibility early to avoid late-stage surprises.
**Scanner:** Not configured

## Violations Found

**Total Violations:** 30
- **File-by-File Violations:** 30
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="map-sequential-spine-vs-optional-paths-violations">Map Sequential Spine Vs Optional Paths: 30 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics%5B0%5D.sub_epics%5B0%5D.story_groups%5B0%5D.stories%5B0%5D.sequential_order): Story "Generate Bot Tools" has sequential_order 0.5, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics%5B1%5D.sub_epics%5B1%5D.story_groups%5B0%5D.stories%5B0%5D.sequential_order): Story "Bootstrap Workspace" has sequential_order 0.5, but expected 1 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics%5B1%5D.sub_epics%5B2%5D.story_groups%5B0%5D.stories%5B0%5D.sequential_order): Story "Route to Default Behavior Action" has sequential_order 7, but expected 1 (gap in sequence)
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
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[2].story_groups[0].stories[5].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics%5B2%5D.sub_epics%5B2%5D.story_groups%5B0%5D.stories%5B5%5D.sequential_order): Story "proactively Validate knowledge against rules" has sequential_order 1, but expected 2 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[3].story_groups[0].stories[9].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics%5B2%5D.sub_epics%5B3%5D.story_groups%5B0%5D.stories%5B9%5D.sequential_order): Story "Inject Render Instructions And Configs" has sequential_order 6, but expected 7 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[4].story_groups[0].stories[3].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics%5B2%5D.sub_epics%5B4%5D.story_groups%5B0%5D.stories%5B3%5D.sequential_order): Story "Discovers Scanners" has sequential_order 1, but expected 2 (gap in sequence)
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- <span style="color: orange;">[!]</span> **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

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
`c:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\prioritization-validation-report-2026-01-04_01-06-22.md`

