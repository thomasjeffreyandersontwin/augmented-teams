# Validation Report - Domain

**Generated:** 2025-12-29 13:26:17
**Project:** base_bot
**Behavior:** domain
**Action:** validate

## Summary

Validated content against **8 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: ALL CLEAN

| Status | Count | Description |
|--------|-------|-------------|
| [i] No Scanner | 8 | Rule has no scanner configured |

**Total Rules:** 8
- **Rules with Scanners:** 0
  - 🟩 **Executed Successfully:** 0
- [i] **Rules without Scanners:** 8

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Integrate And Organize Concepts](#integrate-and-organize-concepts)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Module For Folder Structure](#use-module-for-folder-structure)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Domain Language](#use-domain-language)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Favor Code Representation](#favor-code-representation)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Scope Concepts Correctly](#scope-concepts-correctly)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Natural English](#use-natural-english)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Use Resource Oriented Design](#use-resource-oriented-design)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Shape Relationships From Story Map](#shape-relationships-from-story-map)** - No scanner configured

## Validation Rules Checked

### [i] Rule: <span id="favor-code-representation">Favor Code Representation</span> - NO SCANNER
**Description:** Keep domain model tightly aligned to code it represents, use actual class names and method signatures, not prose descriptions. Show collaborators as types, not descriptions. Avoid over conceptualization.
**Scanner:** Not configured

### [i] Rule: <span id="integrate-and-organize-concepts">Integrate And Organize Concepts</span> - NO SCANNER
**Description:** Integrate related capabilities under parent concepts and organize by business domain. Avoid noun redundancy by nesting related capabilities together, group by business capabilities not technical layers.
**Scanner:** Not configured

### [i] Rule: <span id="scope-concepts-correctly">Scope Concepts Correctly</span> - NO SCANNER
**Description:** Scope domain concepts correctly - place at the most specific level where relevant and ensure they represent complete functional capabilities. Use 'local' scope for single sub-epic concepts, 'global' for shared concepts. Concepts should be complete functional units, not fragments.
**Scanner:** Not configured

### [i] Rule: <span id="shape-relationships-from-story-map">Shape Relationships From Story Map</span> - NO SCANNER
**Description:** Shape domain concept relationships from the story map. Collaborators should come from stories showing how concepts work together to accomplish user goals.
**Scanner:** Not configured

### [i] Rule: <span id="use-domain-language">Use Domain Language</span> - NO SCANNER
**Description:** Use domain-specific language rooted in core business concepts. Avoid generic terms, technical patterns (Manager, Service, Handler, Factory), and capability verbs (Exposes, Provides, Contains). Name concepts and responsibilities using the ubiquitous language of the business domain.
**Scanner:** Not configured

### [i] Rule: <span id="use-module-for-folder-structure">Use Module For Folder Structure</span> - NO SCANNER
**Description:** Use module field to map domain concepts to source code folder structure. Module names MUST exactly match folder paths where they exist using dot notation for nesting.
**Scanner:** Not configured

### [i] Rule: <span id="use-natural-english">Use Natural English</span> - NO SCANNER
**Description:** Use natural English for responsibility names. Responsibilities should read like natural language method calls, using proper grammar and clear intent.
**Scanner:** Not configured

### [i] Rule: <span id="use-resource-oriented-design">Use Resource Oriented Design</span> - NO SCANNER
**Description:** Use resource-oriented design where concepts represent resources with properties and behaviors. Focus on what the resource IS and HAS, not implementation operations.
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
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\domain-validation-report-2025-12-29_13-26-17.md`

