# Validation Report - Discovery

**Generated:** 2026-01-12 19:32:34
**Project:** agile_bot
**Behavior:** discovery
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

- 🟨 **[Enumerate All Stories Explicitly](#enumerate-all-stories-explicitly)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#enumerate-all-stories-explicitly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.enumerate_stories_scanner.EnumerateStoriesScanner`
- 🟩 **[Ensure Vertical Slices](#ensure-vertical-slices)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_slice_scanner.VerticalSliceScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Consolidate Superficial Stories](#consolidate-superficial-stories)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Expand System Technology Stories](#expand-system-technology-stories)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Review And Expand Stories](#review-and-expand-stories)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="ensure-vertical-slices">Ensure Vertical Slices</span> - CLEAN (0 violations)
**Description:** Ensure increments remain vertical slices (end-to-end flows across multiple epics/features, NOT horizontal layers). Each increment must deliver a complete working flow.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.vertical_slice_scanner.VerticalSliceScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="consolidate-superficial-stories">Consolidate Superficial Stories</span> - NO SCANNER
**Description:** Consolidate similar stories that differ superficially. When multiple stories use the same logic and only differ in data values or enumeration, combine them into a single parameterized story.
**Scanner:** Not configured

### 🟨 Rule: <span id="enumerate-all-stories-explicitly">Enumerate All Stories Explicitly</span> - 3 VIOLATION(S) - [View Details](#enumerate-all-stories-explicitly-violations)
**Description:** Enumerate ALL stories for increment(s) in focus explicitly (no ~X stories notation). Use story counts (~X stories) only for other increments. When applying new approach (System stories, component interactions), MUST expand existing stories into component-level stories.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.enumerate_stories_scanner.EnumerateStoriesScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="expand-system-technology-stories">Expand System Technology Stories</span> - NO SCANNER
**Description:** Review and expand stories based on new approach granularity. When planning decisions specify 'System stories' or detailed component interactions, MUST break down existing stories into component-interaction stories. The story count WILL increase.
**Scanner:** Not configured

### [i] Rule: <span id="review-and-expand-stories">Review And Expand Stories</span> - NO SCANNER
**Description:** Review and expand stories based on new approach granularity. When planning decisions specify 'System stories' or detailed component interactions, MUST break down existing stories into component-interaction stories. The story count WILL increase.
**Scanner:** Not configured

## Violations Found

**Total Violations:** 3
- **File-by-File Violations:** 3
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="enumerate-all-stories-explicitly-violations">Enumerate All Stories Explicitly: 3 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].name.sub_epics[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/epics%5B1%5D.name.sub_epics%5B1%5D): Sub-epic "Invoke Bot Directly" has no story_groups - all stories must be explicitly enumerated
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].name.sub_epics[3]`](vscode://file/C:/dev/augmented-teams/agile_bot/epics%5B1%5D.name.sub_epics%5B3%5D): Sub-epic "Invoke Bot Through Panel" has no story_groups - all stories must be explicitly enumerated
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].name.sub_epics[4]`](vscode://file/C:/dev/augmented-teams/agile_bot/epics%5B1%5D.name.sub_epics%5B4%5D): Sub-epic "Invoke Bot Through REPL" has no story_groups - all stories must be explicitly enumerated

## Validation Instructions

The following validation steps were performed:

1. 
=== SCANNER EXECUTION STATUS ===
2. Successfully Executed: 2
3. Load Failed: 0
4. Execution Failed: 0
5. No Scanner: 3
6. 
7. All scanners executed successfully.
8. === END SCANNER STATUS ===

9. Based on code scanner diagnostics, edit the story graph to fix violations:
10. Rule enumerate_all_stories_explicitly.json: 3 file-by-file, 0 cross-file violations
*... and 2 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\docs\stories\reports\discovery-validation-report-2026-01-12_19-32-34.md`

