# Validation Report - Shape

**Generated:** 2025-12-20 01:03:37
**Project:** mob_minion
**Behavior:** shape
**Action:** validate

## Summary

Validated content against **27 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `solution-domain-model-description.md`
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 14 | Scanners ran without errors |
| 🟩 Clean Rules | 11 | No violations found |
| [i] No Scanner | 13 | Rule has no scanner configured |

**Total Rules:** 27
- **Rules with Scanners:** 14
  - 🟩 **Executed Successfully:** 14
- [i] **Rules without Scanners:** 13

### 🟩 Successfully Executed Scanners

- 🟨 **[Enforce Specificity In Stories](#enforce-specificity-in-stories)** - 10 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-specificity-in-stories-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.specificity_scanner.SpecificityScanner`
- 🟨 **[Prevent Implementation Details As Stories](#prevent-implementation-details-as-stories)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#prevent-implementation-details-as-stories-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.implementation_details_scanner.ImplementationDetailsScanner`
- 🟨 **[Avoid Technical Implementation Language](#avoid-technical-implementation-language)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-technical-implementation-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_language_scanner.TechnicalLanguageScanner`
- 🟩 **[Avoid Noun Redundancy](#avoid-noun-redundancy)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.noun_redundancy_scanner.NounRedundancyScanner`
- 🟩 **[Avoid Technical Abstractions](#avoid-technical-abstractions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_abstraction_scanner.TechnicalAbstractionScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_scanner.CodeRepresentationScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_scanner.DomainGroupingScanner`
- 🟩 **[Prevent Generic Capabilities](#prevent-generic-capabilities)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.generic_capability_scanner.GenericCapabilityScanner`
- 🟩 **[Use Active Behavioral Language](#use-active-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟩 **[Use Domain Language](#use-domain-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_scanner.DomainLanguageScanner`
- 🟩 **[Use Natural English](#use-natural-english)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.natural_english_scanner.NaturalEnglishScanner`
- 🟩 **[Use Outcome Verbs Not Communication Verbs](#use-outcome-verbs-not-communication-verbs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.communication_verb_scanner.CommunicationVerbScanner`
- 🟩 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_design_scanner.ResourceOrientedDesignScanner`
- 🟩 **[Use Verb Noun Format](#use-verb-noun-format)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Avoid Technical Stories](#avoid-technical-stories)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Balance Fine Grained Testable Stories](#balance-fine-grained-testable-stories)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Create Lightweight Precise Docs](#create-lightweight-precise-docs)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Enforce Behavioral Journey Flow](#enforce-behavioral-journey-flow)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Enforce Functional Accomplishment](#enforce-functional-accomplishment)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Extract Story Map From Code](#extract-story-map-from-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Focus Real Actions On Domain Concepts](#focus-real-actions-on-domain-concepts)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Focus User And System Activities](#focus-user-and-system-activities)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Identify System Stories](#identify-system-stories)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Maximize Integration Of Related Concepts](#maximize-integration-of-related-concepts)** - No scanner configured
- *... and 3 more rules without scanners*

## Validation Rules Checked

### 🟩 Rule: <span id="avoid-noun-redundancy">Avoid Noun Redundancy</span> - CLEAN (0 violations)
**Description:** When shaping stories, avoid noun redundancy in domain and concept names
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.noun_redundancy_scanner.NounRedundancyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-technical-abstractions">Avoid Technical Abstractions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Domain concepts must stay at the domain level, even if concrete. Don't separate technical details from domain concepts—they should be the same (class vs object vs file—all represent the same domain concept).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_abstraction_scanner.TechnicalAbstractionScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Domain models must represent code as closely as possible. Code should represent domain concepts. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_scanner.CodeRepresentationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Domain concepts must be grouped by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_scanner.DomainGroupingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="prevent-generic-capabilities">Prevent Generic Capabilities</span> - CLEAN (0 violations)
**Description:** CRITICAL: Stories must describe specific actions with actors, not generic capabilities. Reject stories that describe what system IS (capabilities) vs what system DOES (behaviors).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.generic_capability_scanner.GenericCapabilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-active-behavioral-language">Use Active Behavioral Language</span> - CLEAN (0 violations)
**Description:** Use active behavioral language with action verbs. Describe behaviors, not tasks or capabilities.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-domain-language">Use Domain Language</span> - CLEAN (0 violations)
**Description:** CRITICAL: Domain concepts must use domain-specific language, not generic terms. Objects should expose properties representing what they contain (e.g., recommended_trades), not methods that 'generate' or 'calculate' things. If field-level variables are needed for clarity, show them with dot notation (class.field).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_scanner.DomainLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-natural-english">Use Natural English</span> - CLEAN (0 violations)
**Description:** CRITICAL: Domain concepts must use natural English for plural, singular, and cardinality. Collections add 's' to concept name. Use 'many' for accessing collections, 'may' for optional, 'will' for required. Don't use brackets or technical notation like '0..1' or '1..*'.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.natural_english_scanner.NaturalEnglishScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-outcome-verbs-not-communication-verbs">Use Outcome Verbs Not Communication Verbs</span> - CLEAN (0 violations)
**Description:** Use Outcome Verbs, Not Communication Verbs
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.communication_verb_scanner.CommunicationVerbScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-resource-oriented-design">Use Resource Oriented Design</span> - CLEAN (0 violations)
**Description:** CRITICAL: Domain concepts must use resource-oriented, object-oriented design. Use object-oriented classes (singular or collection) with responsibilities that encapsulate logic over manager/doer/loader patterns. Maximize encapsulation through collaborator relationships.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_design_scanner.ResourceOrientedDesignScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-verb-noun-format">Use Verb Noun Format</span> - CLEAN (0 violations)
**Description:** Use verb-noun format consistently for all story elements (epics, features, stories, scenarios). Maintain consistency across hierarchy levels.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-technical-implementation-language">Avoid Technical Implementation Language</span> - 1 VIOLATION(S) - [View Details](#avoid-technical-implementation-language-violations)
**Description:** When shaping stories, avoid technical implementation language in user-facing story elements
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_language_scanner.TechnicalLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="avoid-technical-stories">Avoid Technical Stories</span> - NO SCANNER
**Description:** Technical stories represent implementation tasks that do not describe system behavior. They are normally avoided in favor of user stories and system stories. When technical stories are necessary, they should be marked with story_type: 'technical' and kept minimal.
**Scanner:** Not configured

### [i] Rule: <span id="balance-fine-grained-testable-stories">Balance Fine Grained Testable Stories</span> - NO SCANNER
**Description:** Balance fine-grained stories with testable and valuable independent units. Stories must deliver value and be independently testable.
**Scanner:** Not configured

### [i] Rule: <span id="create-lightweight-precise-docs">Create Lightweight Precise Docs</span> - NO SCANNER
**Description:** Create lightweight but precise documentation during shaping. Focus on structure and scope, not detailed specifications.
**Scanner:** Not configured

### [i] Rule: <span id="enforce-behavioral-journey-flow">Enforce Behavioral Journey Flow</span> - NO SCANNER
**Description:** Stories must show user/system journey flow with context (when/why), not just list operations. Order by user journey, not technical sequence.
**Scanner:** Not configured

### [i] Rule: <span id="enforce-functional-accomplishment">Enforce Functional Accomplishment</span> - NO SCANNER
**Description:** CRITICAL: Stories must represent complete functional accomplishments, not data access operations or implementation steps. Stories must deliver value independently.
**Scanner:** Not configured

### 🟨 Rule: <span id="enforce-specificity-in-stories">Enforce Specificity In Stories</span> - 10 VIOLATION(S) - [View Details](#enforce-specificity-in-stories-violations)
**Description:** CRITICAL: Stories must be specific about what, when, why, and who. Generic operations like 'Add Sub-Epic' or 'Read Epics' are insufficient - stories must include context and specificity.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.specificity_scanner.SpecificityScanner`
**Execution Status:** EXECUTION_SUCCESS

### [i] Rule: <span id="extract-story-map-from-code">Extract Story Map From Code</span> - NO SCANNER
**Description:** When creating story maps from code, start with the outermost layer (entry points), analyze operations and domain concepts, create epics from higher-order goals, and lay out the story journey.
**Scanner:** Not configured

### [i] Rule: <span id="focus-real-actions-on-domain-concepts">Focus Real Actions On Domain Concepts</span> - NO SCANNER
**Description:** When shaping stories, stories must describe REAL ACTIONS that users or other actors (even system or technical actors) can perform, not capabilities or structural descriptions. Organize by lifecycle flow (Load, Read, Edit, Render, Synchronize, Search, Save). CRITICAL: Actor names must NOT appear in Epic/Sub-Epic/Story names - names are Verb-Noun only.
**Scanner:** Not configured

*... and 7 more rules*

## Violations Found

**Total Violations:** 13
- **File-by-File Violations:** 13
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-technical-implementation-language-violations">Avoid Technical Implementation Language: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Configure Strategy`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Configure Strategy): Story element "Configure Strategy" uses technical implementation verb "configure" - use business language focusing on user experience

#### <span id="enforce-specificity-in-stories-violations">Enforce Specificity In Stories: 10 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[0].name): Sub_epic name "Form Mob" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[1].name): Sub_epic name "Expand Mob" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[0].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[0].sub_epics[2].name): Sub_epic name "Reduce Mob" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[0].name): Sub_epic name "Configure Strategy" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[0].story_groups[1].stories[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[0].story_groups[1].stories[2].name): Story name "Defend leader" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[1].name): Sub_epic name "Coordinate Attack" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[1].sub_epics[2].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[1].sub_epics[2].name): Sub_epic name "Resolve Attack" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[0].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[2].sub_epics[0].story_groups[0].stories[1].name): Story name "Save template" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[0].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[2].sub_epics[1].story_groups[0].stories[0].name): Story name "Select template" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")
- <span style="color: red;">[X]</span> **ERROR** - [`epics[2].sub_epics[1].story_groups[0].stories[1].name`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/epics[2].sub_epics[1].story_groups[0].stories[1].name): Story name "Instantiate mob" is too generic - add context (e.g., "Process Order Payment" not "Process Payment")

#### <span id="prevent-implementation-details-as-stories-violations">Prevent Implementation Details As Stories: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`Configure Strategy`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Configure Strategy): Story "Configure Strategy" appears to be an implementation operation - should be a step within a story that describes user/system outcome
- <span style="color: red;">[X]</span> **ERROR** - [`Save template`](vscode://file/C:/dev/augmented-teams/demo/mob_minion/Save template): Story "Save template" appears to be an implementation operation - should be a step within a story that describes user/system outcome

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
*... and 249 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\demo\mob_minion\docs\stories\shape-validation-report.md`
