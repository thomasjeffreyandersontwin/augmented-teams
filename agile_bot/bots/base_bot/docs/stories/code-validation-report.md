# Validation Report - Code

**Generated:** 2025-12-18 16:54:30
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model against **55 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\bot\bot.py`
  - **Total:** 1 src file(s)

## Scanner Execution Status

### 🔴 Overall Status: VIOLATIONS FOUND

| Status | Count | Description |
|--------|-------|-------------|
| 🟢 Executed Successfully | 49 | Scanners ran without errors |
| 🟢 Clean Rules | 42 | No violations found |
| 🔴 Rules with Errors | 1 | Found 1 error violation(s) |
| ⚪ No Scanner | 6 | Rule has no scanner configured |

**Total Rules:** 55
- **Rules with Scanners:** 49
  - ✅ **Executed Successfully:** 49
- ⚪ **Rules without Scanners:** 6

### ✅ Successfully Executed Scanners

- 🟡 **[Maintain Verb Noun Consistency](#maintain-verb-noun-consistency)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-verb-noun-consistency-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟡 **[Story Names Must Follow Verb Noun Format](#story-names-must-follow-verb-noun-format)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#story-names-must-follow-verb-noun-format-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟡 **[Use Verb Noun Format For Story Elements](#use-verb-noun-format-for-story-elements)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-verb-noun-format-for-story-elements-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟡 **[Stories Developed And Tested In Days](#stories-developed-and-tested-in-days)** - 13 violation(s) (EXECUTION_SUCCESS) - [View Details](#stories-developed-and-tested-in-days-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
- 🟡 **[Map Sequential Spine Vs Optional Paths](#map-sequential-spine-vs-optional-paths)** - 10 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟡 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#delegate-to-lowest-level-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🔴 **[Separate Concerns](#separate-concerns)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#separate-concerns-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.separate_concerns_scanner.SeparateConcernsScanner`
- 🟢 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟢 **[Avoid Technical Abstractions](#avoid-technical-abstractions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_abstraction_code_scanner.TechnicalAbstractionCodeScanner`
- 🟢 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟢 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟢 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟢 **[Eliminate Duplication](#eliminate-duplication)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟢 **[Encapsulate Through Properties](#encapsulate-through-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.property_encapsulation_code_scanner.PropertyEncapsulationCodeScanner`
- 🟢 **[Enforce Encapsulation](#enforce-encapsulation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟢 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟢 **[Follow Open Closed Principle](#follow-open-closed-principle)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.open_closed_principle_scanner.OpenClosedPrincipleScanner`
- 🟢 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟢 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟢 **[Isolate Error Handling](#isolate-error-handling)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.error_handling_isolation_scanner.ErrorHandlingIsolationScanner`
- 🟢 **[Isolate Third Party Code](#isolate-third-party-code)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.third_party_isolation_scanner.ThirdPartyIsolationScanner`
- 🟢 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟢 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟢 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟢 **[Maintain Abstraction Levels](#maintain-abstraction-levels)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.abstraction_levels_scanner.AbstractionLevelsScanner`
- 🟢 **[Maintain Test Quality](#maintain-test-quality)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
- 🟢 **[Maintain Vertical Density](#maintain-vertical-density)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟢 **[Minimize Mutable State](#minimize-mutable-state)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.minimize_mutable_state_scanner.MinimizeMutableStateScanner`
- 🟢 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟢 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟢 **[Prefer Code Over Comments](#prefer-code-over-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟢 **[Prefer Objects Over Primitives](#prefer-objects-over-primitives)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.primitive_vs_object_scanner.PrimitiveVsObjectScanner`
- 🟢 **[Provide Meaningful Context](#provide-meaningful-context)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟢 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟢 **[Remove Bad Comments](#remove-bad-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
- 🟢 **[Simplify Control Flow](#simplify-control-flow)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟢 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟢 **[Test Boundary Behavior](#test-boundary-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_boundary_behavior_scanner.TestBoundaryBehaviorScanner`
- 🟢 **[Test One Concept Per Test](#test-one-concept-per-test)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.one_concept_per_test_scanner.OneConceptPerTestScanner`
- 🟢 **[Use Active Behavioral Language](#use-active-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟢 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟢 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟢 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟢 **[Use Domain Language](#use-domain-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟢 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_handling_scanner.ExceptionHandlingScanner`
- 🟢 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟢 **[Use Intention Revealing Names](#use-intention-revealing-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.intention_revealing_names_scanner.IntentionRevealingNamesScanner`
- 🟢 **[Use Natural English](#use-natural-english)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.natural_english_code_scanner.NaturalEnglishCodeScanner`
- 🟢 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`

### ⚪ Rules Without Scanners

- ⚪ **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- ⚪ **[Enforce Team Formatting Consensus](#enforce-team-formatting-consensus)** - No scanner configured
- ⚪ **[Handle Backward Compatibility](#handle-backward-compatibility)** - No scanner configured
- ⚪ **[Practice Test Driven Development](#practice-test-driven-development)** - No scanner configured
- ⚪ **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured
- ⚪ **[Write Good Comments](#write-good-comments)** - No scanner configured

## Validation Rules Checked

### 🔴 Rule: <span id="separate-concerns">Separate Concerns</span> - 1 ERROR(S) - [View Details](#separate-concerns-violations)
**Description:** CRITICAL: Separate pure logic from side effects and infrastructure. Keep pure calculations separate from I/O, isolate business logic from infrastructure, and separate queries from commands.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.separate_concerns_scanner.SeparateConcernsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - CLEAN (0 violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="avoid-technical-abstractions">Avoid Technical Abstractions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must stay at the domain level, even if concrete. Don't separate technical details from domain concepts—they should be the same (class vs object vs file—all represent the same domain concept).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_abstraction_code_scanner.TechnicalAbstractionCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - CLEAN (0 violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - CLEAN (0 violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="encapsulate-through-properties">Encapsulate Through Properties</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must encapsulate state and behavior through properties. Properties control access to object state, hide internal representation, and allow objects to manage their own data. Objects expose properties representing what they are or contain, not raw data access methods.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.property_encapsulation_code_scanner.PropertyEncapsulationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data, and follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code should represent domain concepts directly. Domain models should match code. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="follow-open-closed-principle">Follow Open Closed Principle</span> - CLEAN (0 violations)
**Description:** Open for extension, closed for modification. Design for extension without modification, depend on interfaces/abstractions not concrete types, and use composition over inheritance.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.open_closed_principle_scanner.OpenClosedPrincipleScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must be organized by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must hide calculation timing. Properties hide when calculations occur—they may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the value was calculated.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="isolate-error-handling">Isolate Error Handling</span> - CLEAN (0 violations)
**Description:** Keep error handling separate from business logic. Extract try/catch blocks into dedicated functions and handle errors at appropriate abstraction levels.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.error_handling_isolation_scanner.ErrorHandlingIsolationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="isolate-third-party-code">Isolate Third Party Code</span> - CLEAN (0 violations)
**Description:** CRITICAL: Don't let external APIs spread through your codebase. Wrap third-party APIs behind your interfaces, create learning tests for external dependencies, and isolate boundary code from business logic.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.third_party_isolation_scanner.ThirdPartyIsolationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="keep-functions-single-responsibility">Keep Functions Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Functions should do one thing and do it well, with no hidden side effects. Each function must have a single, well-defined responsibility.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - CLEAN (0 violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="maintain-abstraction-levels">Maintain Abstraction Levels</span> - CLEAN (0 violations)
**Description:** Code should flow from high-level concepts down to details. Follow 'newspaper metaphor' (high-level first), keep related functions close together, and step down one abstraction level at a time.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.abstraction_levels_scanner.AbstractionLevelsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟢 Rule: <span id="maintain-test-quality">Maintain Test Quality</span> - CLEAN (0 violations)
**Description:** CRITICAL: Tests should be as clean as production code. Keep tests readable and maintainable, use descriptive test names, and follow FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 35 more rules*

## Violations Found

**Total Violations:** 82
- **File-by-File Violations:** 82
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="maintain-verb-noun-consistency-violations">Maintain Verb Noun Consistency: 19 violation(s)</span>

- 🔴 **ERROR** - [`epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].domain_concepts[1]): Unknown name "Specific Bot" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].domain_concepts[1]): Unknown name "Specific Bot" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[0]): Unknown name "Router" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[2]): Unknown name "Workflow State" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[0]): Unknown name "Router" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[2]): Unknown name "Workflow State" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].sub_epics[3].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].domain_concepts[0]): Unknown name "Behavior" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].domain_concepts[0]): Unknown name "Behavior Workflow" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].domain_concepts[0]): Unknown name "Behavior Workflow" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "GatherContextAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Guardrails" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "PlanningAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Guardrails" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "BuildKnowledgeAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "RenderOutputAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Renderer" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[2]): Unknown name "Template" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "ValidateRulesAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[2]): Unknown name "CorrectBotAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")

#### <span id="map-sequential-spine-vs-optional-paths-violations">Map Sequential Spine Vs Optional Paths: 10 violation(s)</span>

- 🔴 **ERROR** - [`epics[0].sub_epics[0].story_groups[0].stories[0].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].story_groups[0].stories[0].sequential_order): Story "Generate Bot Tools" has sequential_order 0.5, but expected 1 (gap in sequence)
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🔴 **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[1].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[1].sequential_order): Story "Initialize Project Creates Context Folder" has sequential_order 1.5, but expected 2 (gap in sequence)
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🔴 **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[7].sequential_order`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[7].sequential_order): Story "Load And Merge Behavior Action Instructions" has sequential_order 3, but expected 4 (gap in sequence)
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements
- 🟡 **WARNING** - ``: All stories in story group have sequential_order - consider marking some as optional if they are alternatives or enhancements

#### <span id="stories-developed-and-tested-in-days-violations">Stories Developed And Tested In Days: 13 violation(s)</span>

- 🔴 **ERROR** - [`epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].story_groups[0].stories[0].acceptance_criteria): Story "Generate Bot Tools" has 2 2 acceptance criteria (should be 4-10)
- 🔴 **ERROR** - [`epics[0].sub_epics[0].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[0].story_groups[0].stories[1].acceptance_criteria): Story "Generate Behavior Tools" has 2 2 acceptance criteria (should be 4-10)
- 🔴 **ERROR** - [`epics[0].sub_epics[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[1].name): Sub-epic "Generate CLI" has 2 2 stories (should be 4-10)
- 🔴 **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[0].acceptance_criteria): Story "Initialize Project Location" has 16 16 acceptance criteria (should be 4-10)
- 🔴 **ERROR** - [`epics[1].sub_epics[0].story_groups[0].stories[3].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[0].story_groups[0].stories[3].acceptance_criteria): Story "Store Context Files" has 16 16 acceptance criteria (should be 4-10)
- 🟡 **WARNING** - [`epics[1].sub_epics[1].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[1].story_groups[0].stories[1].acceptance_criteria): Story "Load And Merge Behavior Action Instructions" has 3 3 acceptance criteria (should be 4-10)
- 🔴 **ERROR** - [`epics[1].sub_epics[2].story_groups[0].stories[3].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[2].story_groups[0].stories[3].acceptance_criteria): Story "Get Help for Command Line Functions" has 19 19 acceptance criteria (should be 4-10)
- 🟡 **WARNING** - [`epics[1].sub_epics[3].story_groups[0].stories[0].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[0].acceptance_criteria): Story "Find Behavior Folder" has 3 3 acceptance criteria (should be 4-10)
- 🟡 **WARNING** - [`epics[1].sub_epics[3].story_groups[0].stories[2].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[2].acceptance_criteria): Story "Invoke Behavior in Workflow Order" has 3 3 acceptance criteria (should be 4-10)
- 🔴 **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[3].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[3].acceptance_criteria): Story "Invoke Behavior Actions in Workflow Order" has 14 14 acceptance criteria (should be 4-10)
- 🟡 **WARNING** - [`epics[1].sub_epics[3].story_groups[0].stories[4].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[4].acceptance_criteria): Story "Invoke Behavior Actions in Workflow Order" has 11 11 acceptance criteria (should be 4-10)
- 🔴 **ERROR** - [`epics[1].sub_epics[3].story_groups[0].stories[5].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].story_groups[0].stories[5].acceptance_criteria): Story "Close Current Action" has 14 14 acceptance criteria (should be 4-10)
- 🟡 **WARNING** - [`epics[2].sub_epics[0].story_groups[0].stories[1].acceptance_criteria`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].story_groups[0].stories[1].acceptance_criteria): Story "Track Activity for Gather Context Action" has 3 3 acceptance criteria (should be 4-10)

#### <span id="story-names-must-follow-verb-noun-format-violations">Story Names Must Follow Verb Noun Format: 19 violation(s)</span>

- 🔴 **ERROR** - [`epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].domain_concepts[1]): Unknown name "Specific Bot" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].domain_concepts[1]): Unknown name "Specific Bot" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[0]): Unknown name "Router" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[2]): Unknown name "Workflow State" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[0]): Unknown name "Router" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[2]): Unknown name "Workflow State" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].sub_epics[3].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].domain_concepts[0]): Unknown name "Behavior" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].domain_concepts[0]): Unknown name "Behavior Workflow" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].domain_concepts[0]): Unknown name "Behavior Workflow" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "GatherContextAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Guardrails" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "PlanningAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Guardrails" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "BuildKnowledgeAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "RenderOutputAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Renderer" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[2]): Unknown name "Template" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "ValidateRulesAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[2]): Unknown name "CorrectBotAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")

#### <span id="use-verb-noun-format-for-story-elements-violations">Use Verb Noun Format For Story Elements: 19 violation(s)</span>

- 🔴 **ERROR** - [`epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].domain_concepts[1]): Unknown name "Specific Bot" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].domain_concepts[1]): Unknown name "Specific Bot" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[0]): Unknown name "Router" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[2]): Unknown name "Workflow State" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[0]): Unknown name "Router" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].domain_concepts[2]): Unknown name "Workflow State" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[1].sub_epics[3].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[3].domain_concepts[0]): Unknown name "Behavior" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].domain_concepts[0]): Unknown name "Behavior Workflow" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].domain_concepts[0]): Unknown name "Behavior Workflow" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "GatherContextAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Guardrails" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "PlanningAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Guardrails" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "BuildKnowledgeAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "RenderOutputAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[1]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[1]): Unknown name "Renderer" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[2]): Unknown name "Template" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[0]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[0]): Unknown name "ValidateRulesAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")
- 🔴 **ERROR** - [`epics[2].sub_epics[0].domain_concepts[2]`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[2].sub_epics[0].domain_concepts[2]): Unknown name "CorrectBotAction" appears to be noun-only - use verb-noun format (e.g., "Places Order" not "Order Management")

#### <span id="delegate-to-lowest-level-violations">Delegate To Lowest Level: 1 violation(s)</span>

- 🔵 **INFO** - [`src\bot\bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py:43): Method "__init__" in Test class [Bot](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py:43) iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

#### <span id="separate-concerns-violations">Separate Concerns: 1 violation(s)</span>

- 🔴 **ERROR** - [`src\bot\bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py:27): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.

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
*... and 253 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\code-validation-report.md`
