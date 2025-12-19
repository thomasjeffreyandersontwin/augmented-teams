# Validation Report - Code

**Generated:** 2025-12-18 21:18:15
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model against **48 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\actions\render\evidence.py`
  - `src\actions\render\render_action.py`
  - `src\actions\render\render_spec.py`
  - `src\actions\render\synchronizer.py`
  - `src\actions\render\template.py`
  - **Total:** 5 src file(s)

## Scanner Execution Status

### 🔴 Overall Status: VIOLATIONS FOUND

| Status | Count | Description |
|--------|-------|-------------|
| 🟢 Executed Successfully | 42 | Scanners ran without errors |
| 🟢 Clean Rules | 31 | No violations found |
| 🟡 Rules with Warnings | 7 | Found 14 warning violation(s) |
| 🔴 Rules with Errors | 2 | Found 10 error violation(s) |
| ⚪ No Scanner | 6 | Rule has no scanner configured |

**Total Rules:** 48
- **Rules with Scanners:** 42
  - ✅ **Executed Successfully:** 42
- ⚪ **Rules without Scanners:** 6

### ✅ Successfully Executed Scanners

- 🔴 **[Separate Concerns](#separate-concerns)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#separate-concerns-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.separate_concerns_scanner.SeparateConcernsScanner`
- 🟡 **[Remove Bad Comments](#remove-bad-comments)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#remove-bad-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
- 🟡 **[Maintain Abstraction Levels](#maintain-abstraction-levels)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-abstraction-levels-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.abstraction_levels_scanner.AbstractionLevelsScanner`
- 🟡 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#delegate-to-lowest-level-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟡 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟡 **[Provide Meaningful Context](#provide-meaningful-context)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟡 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🔴 **[Eliminate Duplication](#eliminate-duplication)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟡 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟡 **[Maintain Vertical Density](#maintain-vertical-density)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟡 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟢 **[Avoid Technical Abstractions](#avoid-technical-abstractions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_abstraction_code_scanner.TechnicalAbstractionCodeScanner`
- 🟢 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟢 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟢 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
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
- 🟢 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟢 **[Maintain Test Quality](#maintain-test-quality)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
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
- 🟢 **[Simplify Control Flow](#simplify-control-flow)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟢 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟢 **[Test Boundary Behavior](#test-boundary-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_boundary_behavior_scanner.TestBoundaryBehaviorScanner`
- 🟢 **[Test One Concept Per Test](#test-one-concept-per-test)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.one_concept_per_test_scanner.OneConceptPerTestScanner`
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

### 🔴 Rule: <span id="separate-concerns">Separate Concerns</span> - 9 ERROR(S) - [View Details](#separate-concerns-violations)
**Description:** CRITICAL: Separate pure logic from side effects and infrastructure. Keep pure calculations separate from I/O, isolate business logic from infrastructure, and separate queries from commands.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.separate_concerns_scanner.SeparateConcernsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🔴 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 1 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="remove-bad-comments">Remove Bad Comments</span> - 4 WARNING(S) - [View Details](#remove-bad-comments-violations)
**Description:** CRITICAL: Some comments actively harm readability. Delete commented-out code (it's in git), remove misleading or outdated comments, and eliminate redundant noise.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="maintain-abstraction-levels">Maintain Abstraction Levels</span> - 3 WARNING(S) - [View Details](#maintain-abstraction-levels-violations)
**Description:** Code should flow from high-level concepts down to details. Follow 'newspaper metaphor' (high-level first), keep related functions close together, and step down one abstraction level at a time.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.abstraction_levels_scanner.AbstractionLevelsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 2 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 2 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 1 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 1 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 1 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
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

*... and 28 more rules*

## Violations Found

**Total Violations:** 27
- **File-by-File Violations:** 27
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 1 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:13): Line 13: Variable truthiness check detected (if config_file:). Assume variable exists - let code fail fast if missing.

#### <span id="delegate-to-lowest-level-violations">Delegate To Lowest Level: 2 violation(s)</span>

- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:125): Method "templates" in Test class [RenderOutputAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:125) iterates through "_render_specs" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:133): Method "synchronizers" in Test class [RenderOutputAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:133) iterates through "_render_specs" instead of delegating to collection class. Delegate to collection class instead.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 1 violation(s)</span>

- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:428): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_format_executed_synchronizers:428-432):
    ```python
    parts = []
    parts.append('**Synchronizers Already Executed:**')
    parts.append('')
    parts.append('The following render configurations have been automatically executed via synchronizers:')
    parts.append('')
    ```

  Location (_format_template_instructions:459-463):
    ```python
    parts = []
    parts.append('**Template-Based Render Configurations Requiring AI Handling:**')
    parts.append('')
    parts.append('The following render configurations use templates and require AI assistance to...
    ```

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 1 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:14): Class "RenderOutputAction" is 493 lines - should be under 300 lines (extract related methods into separate classes)

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 2 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:31): Function "do_execute" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:9): Function "__init__" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

#### <span id="maintain-abstraction-levels-violations">Maintain Abstraction Levels: 3 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:31): Function "do_execute" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:205): Function "_execute_synchronizer" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:9): Function "__init__" mixes high-level operations with low-level details - extract low-level details to separate functions

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 1 violation(s)</span>

- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:205): Function "_execute_synchronizer" is 61 lines - consider improving vertical density by declaring variables near usage

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 2 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:302): Line 302 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:31): Line 31 uses numbered variable "10" - use meaningful descriptive name

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 1 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:213): Commented-out old code found (lines 213-213) - complete refactoring by deleting old code

#### <span id="remove-bad-comments-violations">Remove Bad Comments: 4 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:32): Line 32 has commented-out code - delete it (it's in git history if needed)
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:228): Line 228 has commented-out code - delete it (it's in git history if needed)
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:231): Line 231 has commented-out code - delete it (it's in git history if needed)
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:335): Line 335 has commented-out code - delete it (it's in git history if needed)

#### <span id="separate-concerns-violations">Separate Concerns: 9 violation(s)</span>

- 🔴 **ERROR** - [`src\actions\render\evidence.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/evidence.py:23): Function "_load_evidence" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.

    ```python
            self._load_evidence()
        
        def _load_evidence(self):
            """Load evidence from evidence.json."""
            evidence_file = self._guardrails_dir / 'evidence.json'
            evidence_data = read_json_file(evidence_file)
            self._evidence_list = evidence_data.get('evidence', [])
        
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:31): Function "do_execute" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.

    ```python
            raise AttributeError("action_name is read-only for RenderOutputAction")
        
        def do_execute(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
            # Load render-specific data (render_instructions and render_configs)
            render_instructions = self._load_render_instructions()
            render_configs = self._load_render_configs()
            
            # Execute synchronizers automatically
            executed_configs = []
            template_configs = []
            
            for render_config in render_configs:
                config = render_config.get('config', {})
                
                if 'synchronizer' in config:
                    # Execute synchronizer automatically
                    try:
                        result = self._execute_synchronizer(render_config)
                        executed_configs.append({
                            'config': render_config,
                            'result': result,
                            'status': 'executed'
                        })
                        logger.info(f"Executed synchronizer for {config.get('name', 'unknown')}: {result.get('output_path', 'N/A')}")
                    except Exception as e:
                        logger.error(f"Failed to execute synchronizer for {config.get('name', 'unknown')}: {e}")
                        executed_configs.append({
                            'config': render_config,
                            'error': str(e),
                            'status': 'failed'
                        })
                else:
                    # Template-based config - include in instructions for AI to handle
                    template_configs.append(render_config)
            
            # Use MergedInstructions to merge base and render instructions
            merged_instructions = MergedInstructions(
                base_instructions=self.instructions.get('base_instructions', []),
                render_instructions=render_instructions
            )
            instructions = merged_instructions.merge()
            
            # Inject render-specific data into instructions
            # Pass executed_configs so AI knows what was already done
            self._inject_render_data(instructions, render_instructions, template_configs, executed_configs)
            
            # Add execution results to return data
            return {
                'instructions': instructions,
                'executed_configs': executed_configs,
        # ... (truncated)
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:86): Function "_load_render_instructions" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.

    ```python
            return self.behavior.folder / 'content' / 'render'
        
        def _load_render_instructions(self) -> Dict[str, Any]:
            """Load render instructions.json - REQUIRED if render folder exists."""
            render_folder = self._find_render_folder()
            
            # If render folder doesn't exist, return empty dict (no render needed)
            if not render_folder.exists() or not render_folder.is_dir():
                return {}
            
            # If render folder exists, instructions.json is MANDATORY
            instructions_path = render_folder / 'instructions.json'
            if not instructions_path.exists():
                raise FileNotFoundError(
                    f"Render folder exists at {render_folder} but instructions.json is missing. "
                    f"instructions.json is mandatory when render folder exists."
                )
            
            return read_json_file(instructions_path)
        
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:104): Function "_load_render_specs" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.

    ```python
            return read_json_file(instructions_path)
        
        def _load_render_specs(self):
            render_folder = self._find_render_folder()
            
            # Guard: Only load specs if render folder exists
            if not render_folder.exists() or not render_folder.is_dir():
                return
            
            render_json_files = [f for f in render_folder.glob('*.json')]
            
            for render_json_file in render_json_files:
                config_data = read_json_file(render_json_file)
                render_spec = RenderSpec(config_data, render_folder, self.behavior.bot_paths, render_json_file)
                self._render_specs.append(render_spec)
        
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:138): Function "_load_render_configs" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.

    ```python
            return synchronizers
        
        def _load_render_configs(self) -> List[Dict[str, Any]]:
            render_folder = self._find_render_folder()
            render_configs = []
            
            # Guard: Only load configs if render folder exists
            if not render_folder.exists() or not render_folder.is_dir():
                return render_configs
            
            render_json_files = [f for f in render_folder.glob('*.json')]
            
            for render_json_file in render_json_files:
                render_config = self._load_single_render_config(render_json_file)
                render_configs.append(render_config)
            
            return render_configs
        
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:154): Function "_load_single_render_config" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.

    ```python
            return render_configs
        
        def _load_single_render_config(self, render_json_file: Path) -> Dict[str, Any]:
            config = read_json_file(render_json_file)
            
            config_entry = {
                'file': str(render_json_file.relative_to(self.behavior.bot_paths.bot_directory)),
                'config': config
            }
            
            if 'synchronizer' in config:
                self._verify_synchronizer_class(config['synchronizer'])
            elif 'template' in config:
                template_content = self._load_template_file(config['template'])
                config_entry['template'] = template_content
            
            return config_entry
        
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:205): Function "_execute_synchronizer" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.

    ```python
                raise ValueError(f'Synchronizer class {synchronizer_class_path} does not have required methods')
        
        def _execute_synchronizer(self, render_config: Dict[str, Any]) -> Dict[str, Any]:
            """Execute a synchronizer from render config."""
            config = render_config.get('config', {})
            synchronizer_path = config.get('synchronizer')
            
            if not synchronizer_path:
                raise ValueError("No synchronizer specified in config")
            
            # Import synchronizer class dynamically
            synchronizer_class = self._import_synchronizer_class(synchronizer_path)
            
            # Instantiate synchronizer
            synchronizer_instance = synchronizer_class()
            
            # Resolve input and output paths
            workspace_dir = self.working_dir
            input_file = config.get('input', 'story-graph.json')
            output_file = config.get('output', 'output.md')
            config_path = config.get('path', 'docs/stories')
            
            # Resolve input path (relative to workspace)
            input_path = workspace_dir / config_path / input_file
            if not input_path.exists():
                # Try docs/stories as fallback
                input_path = workspace_dir / 'docs' / 'stories' / input_file
            
            # Resolve output path (relative to workspace)
            # Handle template variables in output filename
            output_file_resolved = output_file
            if '{solution_name_slug}' in output_file:
                # Try to get solution name from story-graph.json if it exists
                try:
                    if input_path.exists():
                        story_graph_data = read_json_file(input_path)
                        solution_name = story_graph_data.get('solution_name', 'solution')
                        solution_name_slug = solution_name.lower().replace(' ', '-')
                        output_file_resolved = output_file.replace('{solution_name_slug}', solution_name_slug)
                except Exception:
                    # If we can't resolve, use a default
                    output_file_resolved = output_file.replace('{solution_name_slug}', 'solution')
            
            output_path = workspace_dir / config_path / output_file_resolved
            
            # Prepare kwargs from config
            kwargs = {}
            if 'renderer_command' in config:
                kwargs['renderer_command'] = config['renderer_command']
            if 'force_outline' in config:
        # ... (truncated)
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:297): Function "_load_template_file" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.

    ```python
            return synchronizer_class
        
        def _load_template_file(self, template_path: str) -> str:
            render_folder = self._find_render_folder()
            templates_dir = render_folder / 'templates'
            
            if template_path.startswith('templates/'):
                template_path = template_path[10:]
            
            template_file = templates_dir / template_path
            return template_file.read_text(encoding='utf-8')
        
    ```
- 🔴 **ERROR** - [`src\actions\render\template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/template.py:27): Function "_load_template" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.

    ```python
            self._load_template()
        
        def _load_template(self):
            """Load template content from file."""
            if not self._template_path.exists():
                raise FileNotFoundError(
                    f'Template file not found: {self._template_path}'
                )
            
            self._content = self._template_path.read_text(encoding='utf-8')
        
    ```

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
*... and 257 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\code-validation-report.md`
