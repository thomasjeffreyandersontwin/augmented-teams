# Validation Report - Scenarios

**Generated:** 2025-12-29 13:45:40
**Project:** base_bot
**Behavior:** scenarios
**Action:** validate

## Summary

Validated content against **10 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: ALL CLEAN

| Status | Count | Description |
|--------|-------|-------------|
| [i] No Scanner | 10 | Rule has no scanner configured |

**Total Rules:** 10
- **Rules with Scanners:** 0
  - 🟩 **Executed Successfully:** 0
- [i] **Rules without Scanners:** 10

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Given Describes State Not Actions](#given-describes-state-not-actions)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Background For Common Setup](#use-background-for-common-setup)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Scenario Steps Start With Scenario Specific Given](#scenario-steps-start-with-scenario-specific-given)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Scenarios Cover All Cases](#scenarios-cover-all-cases)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Scenario Outline When Needed](#use-scenario-outline-when-needed)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Write Plain English Scenarios](#write-plain-english-scenarios)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Scenarios On Story Docs](#scenarios-on-story-docs)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Map Table Columns To Scenario Parameters](#map-table-columns-to-scenario-parameters)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Domain Rich Language In Testing Tables](#use-domain-rich-language-in-testing-tables)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Specify Constants And Stub Values](#specify-constants-and-stub-values)** - No scanner configured

## Validation Rules Checked

### [i] Rule: <span id="given-describes-state-not-actions">Given Describes State Not Actions</span> - NO SCANNER
**Description:** Given statements describe STATE/PRECONDITIONS, not actions or functionality. Given = what exists before test. When = first action. Then = expected behavior. Example: Given user is logged in (state), not Given user logs in (action).
**Scanner:** Not configured

### [i] Rule: <span id="map-table-columns-to-scenario-parameters">Map Table Columns To Scenario Parameters</span> - NO SCANNER
**Description:** Map all table columns to scenario parameters bidirectionally. Every column header maps to a Background/When/Then parameter, and every parameter appears as a column. Example: '{payment_system}' parameter → 'Payment System' column.
**Scanner:** Not configured

### [i] Rule: <span id="scenario-steps-start-with-scenario-specific-given">Scenario Steps Start With Scenario Specific Given</span> - NO SCANNER
**Description:** Each scenario's Steps start with Given for scenario-specific setup. Background is auto-applied first. Scenario Steps contain setup for THIS scenario only. Example: Background has common setup; Scenario Given has test-specific paths/data.
**Scanner:** Not configured

### [i] Rule: <span id="scenarios-cover-all-cases">Scenarios Cover All Cases</span> - NO SCANNER
**Description:** Scenarios must cover happy path, edge cases, and error cases based on acceptance criteria. Example: Valid input → success; Boundary value → validates; Invalid input → error message.
**Scanner:** Not configured

### [i] Rule: <span id="scenarios-on-story-docs">Scenarios On Story Docs</span> - NO SCANNER
**Description:** Scenarios must be in story-graph.json (in scenarios or scenario_outlines fields), NOT in separate markdown files. NEVER create feature specification documents. Example: story-graph.json epics[].stories[].scenarios[], not docs/stories/scenarios.md.
**Scanner:** Not configured

### [i] Rule: <span id="specify-constants-and-stub-values">Specify Constants And Stub Values</span> - NO SCANNER
**Description:** Specify constants where known, use actual values instead of placeholders. Describe stub return values in Givens. Don't parameterize stubbed inputs. Example: 'payment_rules/common/' (constant) not '{rules_path}' (placeholder).
**Scanner:** Not configured

### [i] Rule: <span id="use-background-for-common-setup">Use Background For Common Setup</span> - NO SCANNER
**Description:** Use Background for repeated Given steps across 3+ scenarios. Background contains only Given/And steps (no When/Then). Example: Background: Given user is logged in And character sheet exists (used by 5 scenarios).
**Scanner:** Not configured

### [i] Rule: <span id="use-domain-rich-language-in-testing-tables">Use Domain Rich Language In Testing Tables</span> - NO SCANNER
**Description:** Use domain-rich language in testing tables. Replace generic JSON with concrete, descriptive language tied to domain concepts. Real data and examples for all inputs/outputs. Example: 'Payment with amount -50.00 (negative)' not '{"payment": {"amount": -50}}'.
**Scanner:** Not configured

### [i] Rule: <span id="use-scenario-outline-when-needed">Use Scenario Outline When Needed</span> - NO SCANNER
**Description:** Use Scenario Outline with Examples when story warrants concrete data: formulas need validation, domain has named entities, parameter variations exist. Example: Calculate ability modifier with Examples table Rank 10→0, Rank 12→+1, Rank 14→+2.
**Scanner:** Not configured

### [i] Rule: <span id="write-plain-english-scenarios">Write Plain English Scenarios</span> - NO SCANNER
**Description:** Write scenarios in plain English. NO variables, NO placeholders, NO Scenario Outlines, NO Examples tables at initial scenario writing stage. Example: 'Given user has typed request message start shaping' not 'Given user has typed <request_message>'.
**Scanner:** Not configured

## Violations Found

🟩 **No violations found.** All rules passed validation.

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
*... and 49 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\scenarios-validation-report-2025-12-29_13-45-40.md`

