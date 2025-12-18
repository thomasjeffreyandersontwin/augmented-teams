# Validation Report - Code

**Generated:** 2025-12-18 15:54:09
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model against **55 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\actions\action.py`
  - `src\actions\action_scope.py`
  - `src\actions\actions.py`
  - `src\actions\activity_tracker.py`
  - `src\actions\base_action_config.py`
  - `src\actions\build\build_action.py`
  - `src\actions\build\build_scope.py`
  - `src\actions\build\knowledge.py`
  - `src\actions\build\knowledge_graph_spec.py`
  - `src\actions\build\knowledge_graph_template.py`
  - `src\actions\clarify\clarify_action.py`
  - `src\actions\clarify\evidence.py`
  - `src\actions\clarify\key_questions.py`
  - `src\actions\clarify\recommended_activities.py`
  - `src\actions\clarify\required_context.py`
  - `src\actions\clarify\requirements_clarifications.py`
  - `src\actions\content.py`
  - `src\actions\guardrails.py`
  - `src\actions\render\evidence.py`
  - `src\actions\render\render_action.py`
  - `src\actions\render\render_spec.py`
  - `src\actions\render\synchronizer.py`
  - `src\actions\render\template.py`
  - `src\actions\strategy\assumptions.py`
  - `src\actions\strategy\json_persistent.py`
  - `src\actions\strategy\recommended_activities.py`
  - `src\actions\strategy\strategy.py`
  - `src\actions\strategy\strategy_action.py`
  - `src\actions\strategy\strategy_criteria.py`
  - `src\actions\strategy\strategy_criterias.py`
  - `src\actions\strategy\strategy_decision.py`
  - `src\actions\validate\knowledge_graph.py`
  - `src\actions\validate\rule.py`
  - `src\actions\validate\rules.py`
  - `src\actions\validate\story_graph.py`
  - `src\actions\validate\validate_action.py`
  - `src\actions\validate\validation_report_writer.py`
  - `src\actions\validate\validation_scope.py`
  - `src\bot\behavior.py`
  - `src\bot\behavior_config.py`
  - `src\bot\behaviors.py`
  - `src\bot\bot.py`
  - `src\bot\bot_config.py`
  - `src\bot\bot_paths.py`
  - `src\bot\instructions.py`
  - `src\bot\merged_instructions.py`
  - `src\bot\trigger_words.py`
  - `src\bot\workspace.py`
  - `src\cli\base_bot_cli.py`
  - `src\cli\cli_generator.py`
  - `src\cli\trigger_router.py`
  - `src\cli\trigger_router_entry.py`
  - `src\mcp\behavior_tool_generator.py`
  - `src\mcp\bot_tool_generator.py`
  - `src\mcp\mcp_server.py`
  - `src\mcp\mcp_server_generator.py`
  - `src\mcp\server_deployer.py`
  - `src\mcp\server_restart.py`
  - `src\utils.py`
  - **Total:** 59 src file(s)

## Scanner Execution Status

### 🔴 Overall Status: VIOLATIONS FOUND

| Status | Count | Description |
|--------|-------|-------------|
| 🟢 Executed Successfully | 49 | Scanners ran without errors |
| 🟢 Clean Rules | 20 | No violations found |
| 🟡 Rules with Warnings | 15 | Found 410 warning violation(s) |
| 🔴 Rules with Errors | 6 | Found 317 error violation(s) |
| ⚪ No Scanner | 6 | Rule has no scanner configured |

**Total Rules:** 55
- **Rules with Scanners:** 49
  - ✅ **Executed Successfully:** 49
- ⚪ **Rules without Scanners:** 6

### ✅ Successfully Executed Scanners

- 🔴 **[Place Imports At Top](#place-imports-at-top)** - 88 violation(s) (EXECUTION_SUCCESS) - [View Details](#place-imports-at-top-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🔴 **[Separate Concerns](#separate-concerns)** - 86 violation(s) (EXECUTION_SUCCESS) - [View Details](#separate-concerns-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.separate_concerns_scanner.SeparateConcernsScanner`
- 🟡 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 73 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟡 **[Encapsulate Through Properties](#encapsulate-through-properties)** - 72 violation(s) (EXECUTION_SUCCESS) - [View Details](#encapsulate-through-properties-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.property_encapsulation_code_scanner.PropertyEncapsulationCodeScanner`
- 🟡 **[Provide Meaningful Context](#provide-meaningful-context)** - 66 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🔴 **[Eliminate Duplication](#eliminate-duplication)** - 64 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🔴 **[Remove Bad Comments](#remove-bad-comments)** - 64 violation(s) (EXECUTION_SUCCESS) - [View Details](#remove-bad-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
- 🟡 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 48 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟡 **[Prefer Objects Over Primitives](#prefer-objects-over-primitives)** - 46 violation(s) (EXECUTION_SUCCESS) - [View Details](#prefer-objects-over-primitives-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.primitive_vs_object_scanner.PrimitiveVsObjectScanner`
- 🟡 **[Maintain Vertical Density](#maintain-vertical-density)** - 39 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟡 **[Simplify Control Flow](#simplify-control-flow)** - 39 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟡 **[Maintain Abstraction Levels](#maintain-abstraction-levels)** - 25 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-abstraction-levels-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.abstraction_levels_scanner.AbstractionLevelsScanner`
- 🟡 **[Maintain Verb Noun Consistency](#maintain-verb-noun-consistency)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-verb-noun-consistency-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟡 **[Story Names Must Follow Verb Noun Format](#story-names-must-follow-verb-noun-format)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#story-names-must-follow-verb-noun-format-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🟡 **[Use Verb Noun Format For Story Elements](#use-verb-noun-format-for-story-elements)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-verb-noun-format-for-story-elements-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.verb_noun_scanner.VerbNounScanner`
- 🔴 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟡 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 13 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟡 **[Stories Developed And Tested In Days](#stories-developed-and-tested-in-days)** - 13 violation(s) (EXECUTION_SUCCESS) - [View Details](#stories-developed-and-tested-in-days-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.story_sizing_scanner.StorySizingScanner`
- 🟡 **[Map Sequential Spine Vs Optional Paths](#map-sequential-spine-vs-optional-paths)** - 10 violation(s) (EXECUTION_SUCCESS) - [View Details](#map-sequential-spine-vs-optional-paths-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.spine_optional_scanner.SpineOptionalScanner`
- 🟡 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟡 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 8 violation(s) (EXECUTION_SUCCESS) - [View Details](#delegate-to-lowest-level-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟡 **[Use Domain Language](#use-domain-language)** - 6 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟡 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟡 **[Isolate Error Handling](#isolate-error-handling)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#isolate-error-handling-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.error_handling_isolation_scanner.ErrorHandlingIsolationScanner`
- 🟡 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟡 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-unnecessary-parameter-passing-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟡 **[Isolate Third Party Code](#isolate-third-party-code)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#isolate-third-party-code-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.third_party_isolation_scanner.ThirdPartyIsolationScanner`
- 🔴 **[Maintain Test Quality](#maintain-test-quality)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-test-quality-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
- 🟡 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-explicit-dependencies-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟢 **[Avoid Technical Abstractions](#avoid-technical-abstractions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.technical_abstraction_code_scanner.TechnicalAbstractionCodeScanner`
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
- 🟢 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟢 **[Minimize Mutable State](#minimize-mutable-state)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.minimize_mutable_state_scanner.MinimizeMutableStateScanner`
- 🟢 **[Prefer Code Over Comments](#prefer-code-over-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟢 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟢 **[Test Boundary Behavior](#test-boundary-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_boundary_behavior_scanner.TestBoundaryBehaviorScanner`
- 🟢 **[Test One Concept Per Test](#test-one-concept-per-test)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.one_concept_per_test_scanner.OneConceptPerTestScanner`
- 🟢 **[Use Active Behavioral Language](#use-active-behavioral-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.active_language_scanner.ActiveLanguageScanner`
- 🟢 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟢 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟢 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_handling_scanner.ExceptionHandlingScanner`
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

### 🔴 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - 88 ERROR(S) - [View Details](#place-imports-at-top-violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🔴 Rule: <span id="separate-concerns">Separate Concerns</span> - 86 ERROR(S) - [View Details](#separate-concerns-violations)
**Description:** CRITICAL: Separate pure logic from side effects and infrastructure. Keep pure calculations separate from I/O, isolate business logic from infrastructure, and separate queries from commands.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.separate_concerns_scanner.SeparateConcernsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🔴 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 64 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🔴 Rule: <span id="remove-bad-comments">Remove Bad Comments</span> - 64 ERROR(S) - [View Details](#remove-bad-comments-violations)
**Description:** CRITICAL: Some comments actively harm readability. Delete commented-out code (it's in git), remove misleading or outdated comments, and eliminate redundant noise.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🔴 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 14 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🔴 Rule: <span id="maintain-test-quality">Maintain Test Quality</span> - 1 ERROR(S) - [View Details](#maintain-test-quality-violations)
**Description:** CRITICAL: Tests should be as clean as production code. Keep tests readable and maintainable, use descriptive test names, and follow FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 73 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="encapsulate-through-properties">Encapsulate Through Properties</span> - 72 WARNING(S) - [View Details](#encapsulate-through-properties-violations)
**Description:** CRITICAL: Code must encapsulate state and behavior through properties. Properties control access to object state, hide internal representation, and allow objects to manage their own data. Objects expose properties representing what they are or contain, not raw data access methods.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.property_encapsulation_code_scanner.PropertyEncapsulationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 66 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 48 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="prefer-objects-over-primitives">Prefer Objects Over Primitives</span> - 46 WARNING(S) - [View Details](#prefer-objects-over-primitives-violations)
**Description:** CRITICAL: Prefer passing objects to objects and returning objects. Work with primitives inside methods, not between objects. Primitives are acceptable only at presentation boundaries (user interfaces, command-line interfaces, serialization for display), but all internal object-to-object communication including APIs should use domain objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.primitive_vs_object_scanner.PrimitiveVsObjectScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 39 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="maintain-abstraction-levels">Maintain Abstraction Levels</span> - 25 WARNING(S) - [View Details](#maintain-abstraction-levels-violations)
**Description:** Code should flow from high-level concepts down to details. Follow 'newspaper metaphor' (high-level first), keep related functions close together, and step down one abstraction level at a time.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.abstraction_levels_scanner.AbstractionLevelsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 13 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 9 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="use-domain-language">Use Domain Language</span> - 6 WARNING(S) - [View Details](#use-domain-language-violations)
**Description:** CRITICAL: Code must use domain-specific language, not generic terms. Objects should expose properties representing what they contain (e.g., recommended_trades), not methods that 'generate' or 'calculate' things.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 5 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="isolate-error-handling">Isolate Error Handling</span> - 3 WARNING(S) - [View Details](#isolate-error-handling-violations)
**Description:** Keep error handling separate from business logic. Extract try/catch blocks into dedicated functions and handle errors at appropriate abstraction levels.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.error_handling_isolation_scanner.ErrorHandlingIsolationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 3 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** Function signatures should be simple and intention-revealing. Prefer 0-2 parameters; use objects for more complex needs.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟡 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - 1 WARNING(S) - [View Details](#avoid-unnecessary-parameter-passing-violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 35 more rules*

## Violations Found

**Total Violations:** 855
- **File-by-File Violations:** 804
- **Cross-File Violations:** 51

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

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 73 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:77): Line 77: Variable truthiness check detected (if next_action:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:84): Line 84: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:291): Line 291: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:295): Line 295: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:15): Line 15: Variable truthiness check detected (if workspace_path:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:20): Line 20: Variable truthiness check detected (if bot_directory:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\bot\merged_instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/merged_instructions.py:30): Line 30: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\bot\workspace.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/workspace.py:34): Line 34: File existence check detected. Let file operations fail if file missing - handle errors centrally.
- 🟡 **WARNING** - [`src\bot\workspace.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/workspace.py:40): Line 40: File existence check detected. Let file operations fail if file missing - handle errors centrally.
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:12): Line 12: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:71): Line 71: Variable truthiness check detected (if not target_bot:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:83): Line 83: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:88): Line 88: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:93): Line 93: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:98): Line 98: Variable truthiness check detected (if route:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\mcp\behavior_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:28): Line 28: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\bot_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/bot_tool_generator.py:37): Line 37: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:120): Line 120: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:123): Line 123: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:137): Line 137: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:167): Line 167: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:189): Line 189: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:192): Line 192: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:207): Line 207: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:216): Line 216: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:289): Line 289: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:343): Line 343: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:391): Line 391: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:394): Line 394: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:403): Line 403: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:409): Line 409: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:423): Line 423: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:603): Line 603: File existence check detected. Let file operations fail if file missing - handle errors centrally.
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:728): Line 728: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:65): Line 65: Variable truthiness check detected (if not pids:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:54): Line 54: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:130): Line 130: Variable truthiness check detected (if not scope_config:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:28): Line 28: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:196): Line 196: Variable truthiness check detected (if not current_behavior:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:322): Line 322: Variable truthiness check detected (if next_action:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:227): Line 227: Variable truthiness check detected (if not behavior_obj:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:410): Line 410: Variable truthiness check detected (if context_instructions:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:127): Line 127: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:158): Line 158: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:188): Line 188: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:191): Line 191: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:195): Line 195: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:204): Line 204: File existence check detected. Let file operations fail if file missing - handle errors centrally.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:251): Line 251: Variable truthiness check detected (if current_action_obj:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:271): Line 271: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:340): Line 340: File existence check detected. Let file operations fail if file missing - handle errors centrally.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:457): Line 457: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:38): Line 38: Variable truthiness check detected (if outputs:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:40): Line 40: Variable truthiness check detected (if duration:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\base_action_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/base_action_config.py:24): Line 24: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:64): Line 64: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:75): Line 75: Variable truthiness check detected (if not template_filename:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:84): Line 84: Variable truthiness check detected (if not template_filename:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:13): Line 13: Variable truthiness check detected (if config_file:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:23): Line 23: Variable truthiness check detected (if scanner_path:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:165): Line 165: Variable truthiness check detected (if violations_cross_file:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:136): Line 136: Variable truthiness check detected (if not rules:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:161): Line 161: Variable truthiness check detected (if not formatted_sections:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:71): Line 71: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:72): Line 72: Variable truthiness check detected (if not violations:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:661): Line 661: Variable truthiness check detected (if has_errors:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:663): Line 663: Variable truthiness check detected (if has_warnings:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:73): Line 73: Variable truthiness check detected (if files_list:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:87): Line 87: File existence check detected. Let file operations fail if file missing - handle errors centrally.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:187): Line 187: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:160): Line 160: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:195): Line 195: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:171): Line 171: Variable truthiness check detected (if files:). Assume variable exists - let code fail fast if missing.

#### <span id="avoid-unnecessary-parameter-passing-violations">Avoid Unnecessary Parameter Passing: 1 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:263): Line 263: Passing self._behavior_name as parameter to _behavior_to_directory(). Access it directly in the method through self._behavior_name instead.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 9 violation(s)</span>

- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:249): Method "_load_bot_triggers" in Test class [TriggerRouter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:249) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:269): Method "_load_behavior_triggers" in Test class [TriggerRouter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:269) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:306): Method "_load_action_triggers" in Test class [TriggerRouter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:306) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:36): Method "_create_action_instance" in Test class [Actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:36) takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.
- 🟡 **WARNING** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:21): Method "track_start" in Test class [ActivityTracker](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:21) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- 🟡 **WARNING** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:30): Method "track_completion" in Test class [ActivityTracker](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:30) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- 🟡 **WARNING** - [`src\actions\clarify\requirements_clarifications.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/requirements_clarifications.py:40): Method "load_all" in Test class [RequirementsClarifications](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/requirements_clarifications.py:40) takes parameter "bot_paths" that is already injected in __init__. Use self.bot_paths instead.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_decision.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_decision.py:47): Method "load_all" in Test class [StrategyDecision](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_decision.py:47) takes parameter "bot_paths" that is already injected in __init__. Use self.bot_paths instead.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:24): Method "_behavior_to_directory" in Test class [ValidationScope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:24) takes parameter "behavior_name" that is already injected in __init__. Use self.behavior_name instead.

#### <span id="delegate-to-lowest-level-violations">Delegate To Lowest Level: 8 violation(s)</span>

- 🔵 **INFO** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:78): Method "find_by_name" in Test class [Behaviors](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:78) iterates through "_behaviors" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:93): Method "__iter__" in Test class [Behaviors](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:93) iterates through "_behaviors" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\bot\bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py:37): Method "__init__" in Test class [Bot](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot.py:37) iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:115): Method "find_by_name" in Test class [Actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:115) iterates through "_actions" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:121): Method "find_by_order" in Test class [Actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:121) iterates through "_actions" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:136): Method "__iter__" in Test class [Actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:136) iterates through "_actions" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:125): Method "templates" in Test class [RenderOutputAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:125) iterates through "_render_specs" instead of delegating to collection class. Delegate to collection class instead.
- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:133): Method "synchronizers" in Test class [RenderOutputAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:133) iterates through "_render_specs" instead of delegating to collection class. Delegate to collection class instead.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 13 violation(s)</span>

- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:134): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (close_current_action:134-139):
    ```python
    if self.bot.behaviors.first:
        self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
        current_behavior = self.bot.behaviors.current
    else:
        raise ValueError('No behaviors available')
    ```

  Location (_route_to_current_behavior_and_action:191-196):
    ```python
    if self.bot.behaviors.first:
        self.bot.behaviors.navigate_to(self.bot.behaviors.first.name)
        current_behavior = self.bot.behaviors.current
    else:
        raise ValueError('No behaviors available')
    ```
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:181): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_route_to_behavior:181-186):
    ```python
    action = behavior_obj.actions.forward_to_current()
    if action is None:
        raise ValueError(f"No current action found for behavior '{behavior_name}'")
    result_data = action.execute()
    result = self._crea...
    ```

  Location (_route_to_current_behavior_and_action:199-204):
    ```python
    action = current_behavior.actions.forward_to_current()
    if action is None:
        raise ValueError(f'No current action found for behavior {current_behavior.name}')
    result_data = action.execute()
    result = ...
    ```
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:291): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (help_behaviors_and_actions:291-301):
    ```python
    if line.startswith('**CRITICAL: YOU MUST DISPLAY') or line.startswith('**YOU MUST DISPLAY'):
        continue
    try:
        sys.stdout.buffer.write((line + '\n').encode('utf-8'))
        sys.stdout.buffer.flush()
    ...
    ```

  Location (help_cursor_commands:487-497):
    ```python
    if line.startswith('**CRITICAL: YOU MUST DISPLAY') or line.startswith('**YOU MUST DISPLAY'):
        continue
    try:
        sys.stdout.buffer.write((line + '\n').encode('utf-8'))
        sys.stdout.buffer.flush()
    ...
    ```
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:262): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_load_bot_triggers:262-267):
    ```python
    content = trigger_file.read_text(encoding='utf-8')
    data = json.loads(content)
    return data.get('patterns', [])
    ```

  Location (_load_patterns_from_file:379-384):
    ```python
    content = file_path.read_text(encoding='utf-8')
    data = json.loads(content)
    return data.get('patterns', [])
    ```
- 🔴 **ERROR** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:146): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_get_increment_story_names:146-153):
    ```python
    if increment.get('priority') == priority:
        stories = increment.get('stories', [])
        for story in stories:
            if isinstance(story, dict):
                story_names.add(story['name'])
            el...
    ```

  Location (_get_increment_story_names_by_name:162-169):
    ```python
    if increment.get('name') == increment_name:
        stories = increment.get('stories', [])
        for story in stories:
            if isinstance(story, dict):
                story_names.add(story['name'])
            ...
    ```
- 🔴 **ERROR** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:147): Duplicate code blocks detected (3 locations) - extract to helper function.

  Location (_get_increment_story_names:147-153):
    ```python
    stories = increment.get('stories', [])
    for story in stories:
        if isinstance(story, dict):
            story_names.add(story['name'])
        elif isinstance(story, str):
            story_names.add(story)
    ```

  Location (_get_increment_story_names_by_name:163-169):
    ```python
    stories = increment.get('stories', [])
    for story in stories:
        if isinstance(story, dict):
            story_names.add(story['name'])
        elif isinstance(story, str):
            story_names.add(story)
    ```

  Location (_extract_story_names_from_epic:188-194):
    ```python
    stories = group.get('stories', [])
    for story in stories:
        if isinstance(story, dict):
            story_names.add(story['name'])
        elif isinstance(story, str):
            story_names.add(story)
    ```
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:107): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_inject_clarification_data:107-123):
    ```python
    from agile_bot.bots.base_bot.src.actions.clarify.requirements_clarifications import RequirementsClarifications
    bot_paths = self.behavior.bot_paths
    clarification_data = RequirementsClarifications.load_...
    ```

  Location (_inject_strategy_data:126-142):
    ```python
    from agile_bot.bots.base_bot.src.actions.strategy.strategy_decision import StrategyDecision
    bot_paths = self.behavior.bot_paths
    strategy_data = StrategyDecision.load_all(bot_paths)
    if not strategy_dat...
    ```
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:194): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (close_current:194-212):
    ```python
    current_action_obj = self.current
    if current_action_obj is None:
        return
    workspace_dir = self.behavior.bot_paths.workspace_directory
    state_file = workspace_dir / 'behavior_action_state.json'
    expect...
    ```

  Location (save_state:331-348):
    ```python
    if self.current is None or self.behavior.bot_paths is None:
        return
    workspace_dir = self.behavior.bot_paths.workspace_directory
    state_file = workspace_dir / 'behavior_action_state.json'
    expected_be...
    ```
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:33): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_load_config:33-46):
    ```python
    config_files = list(self._kg_dir.glob('*.json'))
    if not config_files:
        self._config_data = {'path': 'docs/stories', 'output': 'story-graph.json', 'template': None}
        self._config_path = None
        ...
    ```

  Location (_load_config:23-31):
    ```python
    self._config_data = {'path': 'docs/stories', 'output': 'story-graph.json', 'template': None}
    self._config_path = None
    return
    ```
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:30): Duplicate code detected: functions schema, template_content have identical bodies - extract to shared function
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:381): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_format_render_configs:381-388):
    ```python
    instructions = config.get('instructions', '')
    if isinstance(instructions, str):
        formatted_parts.append(f'   - Instructions: {instructions}')
    elif isinstance(instructions, list):
        formatted_part...
    ```

  Location (_format_template_instructions:463-470):
    ```python
    instructions = config.get('instructions', '')
    if isinstance(instructions, str):
        parts.append(f'   - Instructions: {instructions}')
    elif isinstance(instructions, list):
        parts.append(f'   - Inst...
    ```
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:418): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_format_executed_synchronizers:418-422):
    ```python
    parts = []
    parts.append('**Synchronizers Already Executed:**')
    parts.append('')
    parts.append('The following render configurations have been automatically executed via synchronizers:')
    parts.append('')
    ```

  Location (_format_template_instructions:449-453):
    ```python
    parts = []
    parts.append('**Template-Based Render Configurations Requiring AI Handling:**')
    parts.append('')
    parts.append('The following render configurations use templates and require AI assistance to...
    ```
- 🔴 **ERROR** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:235): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (formatted_text:235-243):
    ```python
    desc = example.get('description', '')
    content = example.get('content', '')
    if isinstance(content, list):
        content = '\n'.join(content)
    if desc:
        formatted.append(f'- {desc}: {content}')
    else:
      ...
    ```

  Location (formatted_text:249-257):
    ```python
    desc = example.get('description', '')
    content = example.get('content', '')
    if isinstance(content, list):
        content = '\n'.join(content)
    if desc:
        formatted.append(f'- {desc}: {content}')
    else:
      ...
    ```

#### <span id="encapsulate-through-properties-violations">Encapsulate Through Properties: 72 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:52): Method "folder" in Test class [Behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:52) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\behavior_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior_config.py:46): Method "base_actions_path" in Test class [BehaviorConfig](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior_config.py:46) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:47): Method "workspace_directory" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:47) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:51): Method "bot_directory" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:51) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:55): Method "base_actions_directory" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:55) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:59): Method "python_workspace_root" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:59) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:63): Method "documentation_path" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:63) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:66): Method "find_repo_root" in Test class [BotPaths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:66) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/instructions.py:24): Method "behavior_instructions" in Test class [Instructions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/instructions.py:24) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\merged_instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/merged_instructions.py:19): Method "base_instructions" in Test class [MergedInstructions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/merged_instructions.py:19) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\bot\merged_instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/merged_instructions.py:23): Method "render_instructions" in Test class [MergedInstructions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/merged_instructions.py:23) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:162): Method "get_tool_catalog" in Test class [ServerDeployer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:162) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:115): Method "get_tool_catalog" in Test class [ServerDeployer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:115) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:71): Method "scope" in Test class [ActionScope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:71) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:91): Method "action_name" in Test class [Action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:91) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:417): Method "tracker" in Test class [Action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:417) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:425): Method "working_dir" in Test class [Action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:425) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:429): Method "bot_dir" in Test class [Action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:429) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:267): Method "forward_to_current" in Test class [Actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:267) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:15): Method "workspace_dir" in Test class [ActivityTracker](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:15) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:32): Method "knowledge" in Test class [BuildKnowledgeAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:32) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:36): Method "knowledge_graph_spec" in Test class [BuildKnowledgeAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:36) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:40): Method "knowledge_graph_template" in Test class [BuildKnowledgeAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:40) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:60): Method "knowledge_graph" in Test class [KnowledgeGraphSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:60) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:92): Method "template" in Test class [KnowledgeGraphSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:92) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:96): Method "config_data" in Test class [KnowledgeGraphSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:96) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:100): Method "config_path" in Test class [KnowledgeGraphSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:100) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:31): Method "schema" in Test class [KnowledgeGraphTemplate](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:31) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:35): Method "template_content" in Test class [KnowledgeGraphTemplate](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:35) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:39): Method "template_path" in Test class [KnowledgeGraphTemplate](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:39) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\clarify\clarify_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py:24): Method "required_context" in Test class [ClarifyContextAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py:24) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\clarify\clarify_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py:28): Method "key_questions" in Test class [ClarifyContextAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py:28) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\clarify\clarify_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py:32): Method "evidence" in Test class [ClarifyContextAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/clarify_action.py:32) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\clarify\evidence.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/evidence.py:21): Method "evidence_list" in Test class [Evidence](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/evidence.py:21) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\clarify\key_questions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/key_questions.py:21): Method "questions" in Test class [KeyQuestions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/key_questions.py:21) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\clarify\recommended_activities.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/recommended_activities.py:20): Method "recommended_activities" in Test class [RecommendedActivities](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/recommended_activities.py:20) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\evidence.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/evidence.py:31): Method "evidence_list" in Test class [Evidence](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/evidence.py:31) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:120): Method "render_specs" in Test class [RenderOutputAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:120) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:39): Method "input" in Test class [RenderSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:39) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:43): Method "output" in Test class [RenderSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:43) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:47): Method "template" in Test class [RenderSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:47) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:51): Method "synchronizer" in Test class [RenderSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:51) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:55): Method "instructions" in Test class [RenderSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:55) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:59): Method "config_data" in Test class [RenderSpec](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:59) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\synchronizer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/synchronizer.py:27): Method "synchronizer_class_path" in Test class [Synchronizer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/synchronizer.py:27) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/template.py:42): Method "content" in Test class [Template](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/template.py:42) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\render\template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/template.py:47): Method "template_path" in Test class [Template](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/template.py:47) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\assumptions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/assumptions.py:19): Method "assumptions" in Test class [Assumptions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/assumptions.py:19) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\recommended_activities.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/recommended_activities.py:19): Method "recommended_activities" in Test class [RecommendedActivities](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/recommended_activities.py:19) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:24): Method "strategy" in Test class [StrategyAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:24) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:28): Method "strategy_criteria" in Test class [StrategyAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:28) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:32): Method "typical_assumptions" in Test class [StrategyAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:32) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:36): Method "recommended_activities" in Test class [StrategyAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:36) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_criteria.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criteria.py:12): Method "question" in Test class [StrategyCriteria](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criteria.py:12) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_criteria.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criteria.py:20): Method "options" in Test class [StrategyCriteria](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criteria.py:20) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_criteria.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criteria.py:28): Method "outcome" in Test class [StrategyCriteria](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criteria.py:28) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\strategy\strategy_criterias.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criterias.py:23): Method "strategy_criterias" in Test class [StrategyCriterias](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criterias.py:23) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\knowledge_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/knowledge_graph.py:20): Method "content" in Test class [KnowledgeGraph](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/knowledge_graph.py:20) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\knowledge_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/knowledge_graph.py:24): Method "path" in Test class [KnowledgeGraph](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/knowledge_graph.py:24) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:42): Method "name" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:42) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:46): Method "rule_file" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:46) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:50): Method "behavior_name" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:50) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:60): Method "scanner_class" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:60) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:76): Method "rule_content" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:76) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:88): Method "scanner_load_error" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:88) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:92): Method "scanner_execution_status" in Test class [Rule](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:92) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:118): Method "violations" in Test class [Rules](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:118) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\story_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:51): Method "knowledge_graph_spec" in Test class [StoryGraph](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:51) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\story_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:55): Method "content" in Test class [StoryGraph](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:55) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\story_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:59): Method "path" in Test class [StoryGraph](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:59) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:47): Method "rules" in Test class [ValidateRulesAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:47) returns mutable reference. Return defensive copy or use property.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:58): Method "scope" in Test class [ValidationScope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:58) returns mutable reference. Return defensive copy or use property.

#### <span id="isolate-error-handling-violations">Isolate Error Handling: 3 violation(s)</span>

- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:244): Function "help_behaviors_and_actions" has 3 try-except blocks - extract error handling to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:381): Function "help_cursor_commands" has 3 try-except blocks - extract error handling to separate functions
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:883): Function "_create_file_link" has 3 try-except blocks - extract error handling to separate functions

#### <span id="isolate-third-party-code-violations">Isolate Third Party Code: 1 violation(s)</span>

- 🔵 **INFO** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:87): Line 87 imports third-party library directly - wrap third-party APIs behind your own interfaces

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 13 violation(s)</span>

- 🔵 **INFO** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:16): Class "Behaviors" has 19 methods - consider if it has multiple responsibilities and should be split.
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:16): Class "CliTerminalFormatter" has low cohesion (LCOM=1.00) - methods don't share many attributes, suggesting multiple responsibilities. Consider splitting into separate classes.
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:99): Class "BaseBotCli" is 897 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:8): Class "CliGenerator" is 348 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:16): Class "TriggerRouter" is 369 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:9): Class "MCPServerGenerator" is 890 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:16): Class "Action" is 549 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:13): Class "Actions" is 461 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:14): Class "RenderOutputAction" is 490 lines - should be under 300 lines (extract related methods into separate classes)
- 🔵 **INFO** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:6): Class "Rule" has 23 methods - consider if it has multiple responsibilities and should be split.
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:10): Class "Rules" is 311 lines - should be under 300 lines (extract related methods into separate classes)
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:31): Class "ValidateRulesAction" has low cohesion (LCOM=0.87) - methods don't share many attributes, suggesting multiple responsibilities. Consider splitting into separate classes.
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:170): Class "ValidationReportWriter" is 831 lines - should be under 300 lines (extract related methods into separate classes)

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 48 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:19): Function "__init__" is 25 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:17): Function "__init__" is 33 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:186): Function "load_state" is 32 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:131): Function "close_current_action" is 23 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:244): Function "help_behaviors_and_actions" is 55 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:381): Function "help_cursor_commands" is 99 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:666): Function "parse_arguments" is 21 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:805): Function "main" is 60 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:23): Function "generate_cli_code" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:42): Function "match_trigger" is 33 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\behavior_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:14): Function "invoke" is 29 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\behavior_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:63): Function "create_behavior_tools" is 25 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\bot_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/bot_tool_generator.py:13): Function "invoke" is 38 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\mcp_server.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server.py:22): Function "invoke_tool" is 23 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:115): Function "register_bot_tool" is 28 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:184): Function "register_close_current_action_tool" is 43 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:338): Function "register_restart_server_tool" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:379): Function "register_behavior_tool" is 50 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:38): Function "__init__" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:76): Function "deploy_server" is 25 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:16): Function "find_mcp_server_processes" has high cognitive complexity (18) - should be under 15. Reduce nesting and extract complex logic.
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:48): Function "terminate_processes" is 30 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:132): Function "restart_mcp_server" is 29 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:73): Function "get_story_names" is 52 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:17): Function "__init__" is 33 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:170): Function "get_workflow_status_breadcrumbs" is 130 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:438): Function "execute" is 23 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:146): Function "navigate_to" is 32 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:187): Function "close_current" is 46 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:364): Function "load_state" is 50 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\base_action_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/base_action_config.py:10): Function "__init__" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:46): Function "do_execute" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:31): Function "do_execute" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:9): Function "__init__" is 21 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:7): Function "__init__" is 22 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:112): Function "scan" is 49 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:222): Function "formatted_text" is 53 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:134): Function "formatted_rules" is 24 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:166): Function "validate" is 93 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\story_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:15): Function "__init__" is 29 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:49): Function "do_execute" is 70 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:174): Function "injectValidationInstructions" is 52 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:67): Function "on_file_scanned" is 24 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:100): Function "on_scanner_complete" is 27 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:176): Function "write" is 23 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:651): Function "sort_key" has high cognitive complexity (17) - should be under 15. Reduce nesting and extract complex logic.
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:60): Function "files" is 57 lines - should be under 20 lines (extract complex logic to helper functions)
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:129): Function "all_files" is 61 lines - should be under 20 lines (extract complex logic to helper functions)

#### <span id="maintain-abstraction-levels-violations">Maintain Abstraction Levels: 25 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:186): Function "load_state" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\bot\workspace.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/workspace.py:31): Function "get_base_actions_directory" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:123): Function "run" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:131): Function "close_current_action" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:244): Function "help_behaviors_and_actions" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:381): Function "help_cursor_commands" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:503): Function "_group_commands" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:536): Function "_get_behavior_description" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:666): Function "parse_arguments" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:805): Function "main" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:872): Function "_execute_and_output" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:226): Function "_generate_cursor_commands" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:92): Function "register_all_tools" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:76): Function "deploy_server" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:111): Function "get_tool_catalog" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:132): Function "restart_mcp_server" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:26): Function "_build_scope" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:73): Function "get_story_names" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:73): Function "template_filename" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:31): Function "do_execute" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:205): Function "_execute_synchronizer" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:9): Function "__init__" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:166): Function "validate" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:174): Function "injectValidationInstructions" mixes high-level operations with low-level details - extract low-level details to separate functions
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:22): Function "__init__" mixes high-level operations with low-level details - extract low-level details to separate functions

#### <span id="maintain-test-quality-violations">Maintain Test Quality: 1 violation(s)</span>

- 🔴 **ERROR** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:136): Line 136 uses global state - tests should be independent, not share state

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 39 violation(s)</span>

- 🔵 **INFO** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:244): Function "help_behaviors_and_actions" is 62 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:381): Function "help_cursor_commands" is 121 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:536): Function "_get_behavior_description" is 57 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:717): Function "_parse_action_parameters" is 87 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:805): Function "main" is 66 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:872): Function "_execute_and_output" is 56 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:61): Function "_generate_python_cli_script" is 99 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:226): Function "_generate_cursor_commands" is 59 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:42): Function "match_trigger" is 60 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:184): Function "register_close_current_action_tool" is 99 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:284): Function "register_confirm_out_of_order_tool" is 53 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:379): Function "register_behavior_tool" is 71 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:460): Function "_execute_entry_workflow" is 76 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:613): Function "generate_server_entry_point" is 81 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:753): Function "_generate_workspace_rules_file" is 146 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:111): Function "get_tool_catalog" is 52 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:48): Function "terminate_processes" is 51 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:132): Function "restart_mcp_server" is 54 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:73): Function "get_story_names" is 67 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:170): Function "get_workflow_status_breadcrumbs" is 178 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:438): Function "execute" is 69 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:508): Function "_inject_reminders_if_final" is 54 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:36): Function "_create_action_instance" is 67 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:187): Function "close_current" is 77 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:364): Function "load_state" is 59 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:205): Function "_execute_synchronizer" is 61 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:447): Function "_format_template_instructions" is 54 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:112): Function "scan" is 73 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:222): Function "formatted_text" is 59 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:166): Function "validate" is 155 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:49): Function "do_execute" is 77 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:174): Function "injectValidationInstructions" is 100 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:356): Function "_build_scanner_status" is 175 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:532): Function "_build_status_summary" is 73 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:606): Function "_build_validation_rules" is 134 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:795): Function "_build_violations_by_type" is 60 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:919): Function "_extract_test_info" is 52 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:60): Function "files" is 68 lines - consider improving vertical density by declaring variables near usage
- 🔵 **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:129): Function "all_files" is 70 lines - consider improving vertical density by declaring variables near usage

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 14 violation(s)</span>

- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:149): Except block only contains pass at line 149 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:162): Except block only contains pass at line 162 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:177): Except block only contains pass at line 177 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:41): Except block only contains pass at line 41 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:547): Except block only contains pass at line 547 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:632): Except block only contains pass at line 632 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:301): Except block only contains pass at line 301 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:589): Except block only contains pass at line 589 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:406): Except block only contains pass at line 406 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:368): Except block only contains pass at line 368 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:276): Except block only contains pass at line 276 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:291): Except block only contains pass at line 291 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:326): Except block only contains pass at line 326 - exceptions must be logged or rethrown, never swallowed
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:324): Except block only contains pass at line 324 - exceptions must be logged or rethrown, never swallowed

#### <span id="place-imports-at-top-violations">Place Imports At Top: 88 violation(s)</span>

- 🔴 **ERROR** - [`src\bot\behavior.py:15`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:15:15): Import statement found at line 15 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\bot\behaviors.py:11`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:11:11): Import statement found at line 11 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\bot\behaviors.py:21`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:21:21): Import statement found at line 21 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\bot\behaviors.py:22`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:22:22): Import statement found at line 22 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\bot\behaviors.py:45`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:45:45): Import statement found at line 45 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\bot\behaviors.py:260`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:260:260): Import statement found at line 260 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\bot\bot_paths.py:9`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:9:9): Import statement found at line 9 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:274`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:274:274): Import statement found at line 274 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:323`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:323:323): Import statement found at line 323 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:335`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:335:335): Import statement found at line 335 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:383`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:383:383): Import statement found at line 383 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:429`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:429:429): Import statement found at line 429 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:473`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:473:473): Import statement found at line 473 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:588`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:588:588): Import statement found at line 588 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:845`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:845:845): Import statement found at line 845 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py:940`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:940:940): Import statement found at line 940 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\cli_generator.py:86`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:86:86): Import statement found at line 86 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\cli_generator.py:87`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:87:87): Import statement found at line 87 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\cli_generator.py:88`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:88:88): Import statement found at line 88 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\cli_generator.py:89`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:89:89): Import statement found at line 89 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\cli_generator.py:122`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:122:122): Import statement found at line 122 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\cli\cli_generator.py:123`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:123:123): Import statement found at line 123 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\behavior_tool_generator.py:15`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:15:15): Import statement found at line 15 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\behavior_tool_generator.py:16`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:16:16): Import statement found at line 16 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\behavior_tool_generator.py:60`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:60:60): Import statement found at line 60 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\bot_tool_generator.py:14`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/bot_tool_generator.py:14:14): Import statement found at line 14 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\bot_tool_generator.py:15`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/bot_tool_generator.py:15:15): Import statement found at line 15 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\bot_tool_generator.py:24`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/bot_tool_generator.py:24:24): Import statement found at line 24 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:73`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:73:73): Import statement found at line 73 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:141`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:141:141): Import statement found at line 141 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:171`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:171:171): Import statement found at line 171 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:292`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:292:292): Import statement found at line 292 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:303`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:303:303): Import statement found at line 303 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:304`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:304:304): Import statement found at line 304 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:347`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:347:347): Import statement found at line 347 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:364`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:364:364): Import statement found at line 364 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:412`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:412:412): Import statement found at line 412 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:426`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:426:426): Import statement found at line 426 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:457`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:457:457): Import statement found at line 457 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:472`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:472:472): Import statement found at line 472 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:574`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:574:574): Import statement found at line 574 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:624`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:624:624): Import statement found at line 624 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:625`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:625:625): Import statement found at line 625 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:626`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:626:626): Import statement found at line 626 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:627`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:627:627): Import statement found at line 627 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:657`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:657:657): Import statement found at line 657 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:661`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:661:661): Import statement found at line 661 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py:800`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:800:800): Import statement found at line 800 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\server_deployer.py:53`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:53:53): Import statement found at line 53 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\mcp\server_deployer.py:87`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:87:87): Import statement found at line 87 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:8`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:8:8): Import statement found at line 8 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:13`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:13:13): Import statement found at line 13 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:34`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:34:34): Import statement found at line 34 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:67`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:67:67): Import statement found at line 67 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:107`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:107:107): Import statement found at line 107 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:126`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:126:126): Import statement found at line 126 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:204`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:204:204): Import statement found at line 204 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:445`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:445:445): Import statement found at line 445 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:446`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:446:446): Import statement found at line 446 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\action.py:520`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:520:520): Import statement found at line 520 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\actions.py:9`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:9:9): Import statement found at line 9 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\actions.py:10`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:10:10): Import statement found at line 10 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\actions.py:38`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:38:38): Import statement found at line 38 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\actions.py:39`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:39:39): Import statement found at line 39 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\actions.py:40`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:40:40): Import statement found at line 40 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\actions.py:91`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:91:91): Import statement found at line 91 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge.py:6`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge.py:6:6): Import statement found at line 6 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge.py:7`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge.py:7:7): Import statement found at line 7 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py:6`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:6:6): Import statement found at line 6 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py:7`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:7:7): Import statement found at line 7 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py:8`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:8:8): Import statement found at line 8 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py:51`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:51:51): Import statement found at line 51 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py:87`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:87:87): Import statement found at line 87 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rule.py:34`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:34:34): Import statement found at line 34 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rule.py:104`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:104:104): Import statement found at line 104 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rule.py:105`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:105:105): Import statement found at line 105 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:7`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:7:7): Import statement found at line 7 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:35`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:35:35): Import statement found at line 35 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:49`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:49:49): Import statement found at line 49 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:65`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:65:65): Import statement found at line 65 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:181`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:181:181): Import statement found at line 181 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:182`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:182:182): Import statement found at line 182 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:183`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:183:183): Import statement found at line 183 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\rules.py:189`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:189:189): Import statement found at line 189 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\story_graph.py:9`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:9:9): Import statement found at line 9 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\validate_action.py:56`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:56:56): Import statement found at line 56 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\validation_report_writer.py:196`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:196:196): Import statement found at line 196 after non-import code. Move all imports to the top of the file.
- 🔴 **ERROR** - [`src\actions\validate\validation_scope.py:96`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:96:96): Import statement found at line 96 after non-import code. Move all imports to the top of the file.

#### <span id="prefer-objects-over-primitives-violations">Prefer Objects Over Primitives: 46 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:77): Function "find_by_name" takes primitive "behavior_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:96): Function "check_exists" takes primitive "behavior_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:99): Function "navigate_to" takes primitive "behavior_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:116): Function "_inject_next_behavior_reminder" takes primitive "action_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\bot\workspace.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/workspace.py:55): Function "get_behavior_folder" takes primitive "bot_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:155): Function "_route_to_action" takes primitive "behavior_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:155): Function "_route_to_action" takes primitive "action_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:607): Function "_extract_placeholder_name" takes primitive "cmd_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:650): Function "_get_behavior_actions" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:658): Function "_is_action_method" takes primitive "attr_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:929): Function "_handle_list_command" takes primitive "behavior_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:209): Function "_get_behaviors_from_config" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:345): Function "_load_bot_trigger_patterns" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:249): Function "_load_bot_triggers" takes primitive "bot_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:249): Function "_load_bot_triggers" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:306): Function "_load_action_triggers" takes primitive "bot_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:306): Function "_load_action_triggers" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:345): Function "_extract_behavior_name" takes primitive "dir_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:356): Function "_extract_action_name" takes primitive "dir_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:367): Function "_load_patterns_from_file" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\behavior_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:63): Function "create_behavior_tools" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:82): Function "_get_bot_behaviors" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:568): Function "_load_trigger_words_from_behavior_folder" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:695): Function "generate_cursor_mcp_config" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:727): Function "generate_server" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:741): Function "generate_awareness_files" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:164): Function "_load_trigger_words" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:16): Function "find_mcp_server_processes" takes primitive "bot_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:16): Function "find_mcp_server_processes" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:48): Function "terminate_processes" returns "dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:157): Function "_get_increment_story_names_by_name" takes primitive "increment_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:173): Function "_get_epic_story_names" takes primitive "epic_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:349): Function "_get_default_breadcrumbs" returns "list" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:114): Function "find_by_name" takes primitive "action_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:146): Function "navigate_to" takes primitive "action_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:456): Function "is_action_completed" takes primitive "action_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\actions\clarify\requirements_clarifications.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/requirements_clarifications.py:40): Function "load_all" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\strategy\json_persistent.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/json_persistent.py:22): Function "load" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\strategy\strategy_decision.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_decision.py:47): Function "load_all" returns "Dict" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:33): Function "_load_scanner" returns "tuple" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:31): Function "_load_rules" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:48): Function "_load_bot_rules" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:64): Function "_load_behavior_rules" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:98): Function "find_by_name" takes primitive "rule_name: str" - consider passing domain object instead
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:163): Function "get_action_instructions" returns "List" - consider returning domain object instead
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:347): Function "_rule_name_to_anchor" takes primitive "rule_name: str" - consider passing domain object instead

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 66 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:42): Line 42 uses numbered variable "999" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:36): Line 36 uses numbered variable "999" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:270): Line 270 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:1): Line 1 uses numbered variable "python3" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:90): Line 90 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:329): Line 329 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:331): Line 331 uses numbered variable "80" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:332): Line 332 uses numbered variable "77" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:713): Line 713 uses numbered variable "ps1" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:853): Line 853 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:855): Line 855 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:864): Line 864 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:866): Line 866 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:911): Line 911 uses numbered variable "cp1252" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:941): Line 941 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:943): Line 943 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:947): Line 947 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:949): Line 949 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:950): Line 950 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:67): Line 67 uses numbered variable "python3" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:176): Line 176 uses numbered variable "python3" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:188): Line 188 uses numbered variable "ps1" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:20): Line 20 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:23): Line 23 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:24): Line 24 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:25): Line 25 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:26): Line 26 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:27): Line 27 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:28): Line 28 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:29): Line 29 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:30): Line 30 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:33): Line 33 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:34): Line 34 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:35): Line 35 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:36): Line 36 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:37): Line 37 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:38): Line 38 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:39): Line 39 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:40): Line 40 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:43): Line 43 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:44): Line 44 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:45): Line 45 uses numbered variable "033" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:63): Line 63 uses numbered variable "win32" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:64): Line 64 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:118): Line 118 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:291): Line 291 uses numbered variable "u2713" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:292): Line 292 uses numbered variable "u27A4" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:293): Line 293 uses numbered variable "u2610" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:355): Line 355 uses numbered variable "u2610" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:463): Line 463 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:465): Line 465 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:471): Line 471 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:473): Line 473 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:479): Line 479 uses numbered variable "70" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:302): Line 302 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\render\render_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_spec.py:31): Line 31 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:521): Line 521 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:526): Line 526 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:527): Line 527 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:672): Line 672 uses numbered variable "20" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:735): Line 735 uses numbered variable "20" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:736): Line 736 uses numbered variable "20" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:866): Line 866 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:868): Line 868 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:869): Line 869 uses numbered variable "10" - use meaningful descriptive name
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:245): Line 245 uses numbered variable "10" - use meaningful descriptive name

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 5 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:28): Commented-out old code found (lines 28-28) - complete refactoring by deleting old code
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:406): Commented-out old code found (lines 406-407) - complete refactoring by deleting old code
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:175): Commented-out old code found (lines 175-175) - complete refactoring by deleting old code
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:90): Commented-out old code found (lines 90-90) - complete refactoring by deleting old code
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:213): Commented-out old code found (lines 213-213) - complete refactoring by deleting old code

#### <span id="remove-bad-comments-violations">Remove Bad Comments: 64 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\workspace.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/workspace.py:36): Line 36 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:113): Line 113 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:295): Line 295 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:477): Line 477 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:491): Line 491 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:836): Line 836 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:840): Line 840 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:952): Line 952 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:20): Line 20 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:41): Line 41 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:44): Line 44 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:114): Line 114 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:119): Line 119 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:135): Line 135 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:166): Line 166 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:171): Line 171 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:175): Line 175 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:201): Line 201 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:268): Line 268 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:274): Line 274 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:322): Line 322 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:37): Line 37 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\cli\trigger_router_entry.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router_entry.py:27): Line 27 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\behavior_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:66): Line 66 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:17): Line 17 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:226): Line 226 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:399): Line 399 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:474): Line 474 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:654): Line 654 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:673): Line 673 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:706): Line 706 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:759): Line 759 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:771): Line 771 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:775): Line 775 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:854): Line 854 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:48): Line 48 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:101): Line 101 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:31): Line 31 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:37): Line 37 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:187): Line 187 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:266): Line 266 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:280): Line 280 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:289): Line 289 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:505): Line 505 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\base_action_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/base_action_config.py:35): Line 35 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:47): Line 47 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:24): Line 24 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:53): Line 53 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:32): Line 32 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:228): Line 228 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:231): Line 231 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:335): Line 335 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:183): Line 183 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:231): Line 231 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:289): Line 289 has commented-out code - call production code directly, even if API doesn't exist yet
- 🔴 **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:717): Line contains HTML markup in comment - remove HTML, use plain text
- 🔴 **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:807): Line contains HTML markup in comment - remove HTML, use plain text
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:7): Line 7 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:63): Line 63 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:80): Line 80 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:90): Line 90 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:149): Line 149 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:175): Line 175 has commented-out code - call production code directly, even if API doesn't exist yet
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:212): Line 212 has commented-out code - call production code directly, even if API doesn't exist yet

#### <span id="separate-concerns-violations">Separate Concerns: 86 violation(s)</span>

- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:19): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:57): Function "does_requested_action_match_current" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:17): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:109): Function "close_current" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:166): Function "save_state" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:186): Function "load_state" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:225): Function "initialize_state" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\behavior_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior_config.py:9): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\bot_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_config.py:8): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:13): Function "__init__" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:34): Function "_load_documentation_path" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:131): Function "close_current_action" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:307): Function "_get_action_description" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:381): Function "help_cursor_commands" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:536): Function "_get_behavior_description" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:607): Function "_extract_placeholder_name" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:955): Function "_get_breadcrumbs_from_action" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:23): Function "generate_cli_code" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:61): Function "_generate_python_cli_script" mixes incompatible responsibilities: Computation, I/O. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:161): Function "_generate_shell_script" mixes incompatible responsibilities: Computation, I/O. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:186): Function "_generate_powershell_script" mixes incompatible responsibilities: Computation, I/O. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:226): Function "_generate_cursor_commands" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:309): Function "_update_bot_registry" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:345): Function "_load_bot_trigger_patterns" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:19): Function "__init__" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:42): Function "match_trigger" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:103): Function "_match_bot_from_registry" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:232): Function "_load_bot_registry" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:249): Function "_load_bot_triggers" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:269): Function "_load_behavior_triggers" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:306): Function "_load_action_triggers" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:367): Function "_load_patterns_from_file" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\behavior_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/behavior_tool_generator.py:55): Function "__init__" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:52): Function "create_server_instance" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:184): Function "register_close_current_action_tool" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:284): Function "register_confirm_out_of_order_tool" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:379): Function "register_behavior_tool" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:568): Function "_load_trigger_words_from_behavior_folder" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:594): Function "generate_bot_config_file" mixes incompatible responsibilities: Computation, I/O. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:613): Function "generate_server_entry_point" mixes incompatible responsibilities: Computation, I/O. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:753): Function "_generate_workspace_rules_file" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:111): Function "get_tool_catalog" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\mcp\server_deployer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_deployer.py:164): Function "_load_trigger_words" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:17): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:106): Function "_inject_clarification_data" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:125): Function "_inject_strategy_data" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:170): Function "get_workflow_status_breadcrumbs" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:14): Function "__init__" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:36): Function "_create_action_instance" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:146): Function "navigate_to" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:187): Function "close_current" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:330): Function "save_state" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:364): Function "load_state" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:424): Function "_save_completed_action" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:456): Function "is_action_completed" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\base_action_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/base_action_config.py:10): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_spec.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_spec.py:21): Function "_load_config" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:14): Function "_load_template" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\clarify\evidence.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/evidence.py:13): Function "_load_evidence" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\clarify\key_questions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/key_questions.py:13): Function "_load_questions" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\clarify\recommended_activities.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/recommended_activities.py:13): Function "_load_recommended_activities" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\evidence.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/evidence.py:23): Function "_load_evidence" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:31): Function "do_execute" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:86): Function "_load_render_instructions" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:104): Function "_load_render_specs" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:138): Function "_load_render_configs" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:154): Function "_load_single_render_config" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:205): Function "_execute_synchronizer" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:297): Function "_load_template_file" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\render\template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/template.py:27): Function "_load_template" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\strategy\assumptions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/assumptions.py:12): Function "_load_assumptions" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\strategy\recommended_activities.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/recommended_activities.py:12): Function "_load_recommended_activities" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\strategy\strategy_criterias.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_criterias.py:13): Function "_load_strategy_criterias" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\knowledge_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/knowledge_graph.py:13): Function "_load" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:7): Function "__init__" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:33): Function "_load_scanner" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:31): Function "_load_rules" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:98): Function "find_by_name" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:105): Function "__iter__" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:134): Function "formatted_rules" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\story_graph.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/story_graph.py:15): Function "__init__" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:127): Function "inject_common_bot_rules" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:140): Function "inject_behavior_specific_and_bot_rules" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:163): Function "get_action_instructions" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:36): Function "start" mixes incompatible responsibilities: Computation, I/O, Transformation. Separate I/O from Computation - pure logic should be separate from side effects.
- 🔴 **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:176): Function "write" mixes incompatible responsibilities: I/O, Transformation. Separate I/O from Transformation - pure logic should be separate from side effects.

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 39 violation(s)</span>

- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:17): Function "__init__" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:186): Function "load_state" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:244): Function "help_behaviors_and_actions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:307): Function "_get_action_description" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:381): Function "help_cursor_commands" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:503): Function "_group_commands" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:536): Function "_get_behavior_description" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:607): Function "_extract_placeholder_name" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:717): Function "_parse_action_parameters" has nesting depth of 10 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:805): Function "main" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:872): Function "_execute_and_output" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:269): Function "_load_behavior_triggers" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:306): Function "_load_action_triggers" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:753): Function "_generate_workspace_rules_file" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\mcp\server_restart.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/server_restart.py:16): Function "find_mcp_server_processes" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:26): Function "_build_scope" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:141): Function "_get_increment_story_names" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:157): Function "_get_increment_story_names_by_name" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\action_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_scope.py:184): Function "_extract_story_names_from_epic" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action.py:170): Function "get_workflow_status_breadcrumbs" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:146): Function "navigate_to" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:295): Function "_get_next_behavior_reminder" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:364): Function "load_state" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:365): Function "_format_render_configs" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:447): Function "_format_template_instructions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:222): Function "formatted_text" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:64): Function "_load_behavior_rules" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:166): Function "validate" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:174): Function "injectValidationInstructions" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:331): Function "_get_relative_path" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:356): Function "_build_scanner_status" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:532): Function "_build_status_summary" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:606): Function "_build_validation_rules" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:771): Function "_organize_violations" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:795): Function "_build_violations_by_type" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:883): Function "_create_file_link" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:651): Function "sort_key" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:60): Function "files" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- 🟡 **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:129): Function "all_files" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 3 violation(s)</span>

- 🟡 **WARNING** - [`src\actions\activity_tracker.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/activity_tracker.py:30): Function "track_completion" has 6 parameters - consider using parameter object or reducing parameters
- 🟡 **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:166): Function "validate" has 6 parameters - consider using parameter object or reducing parameters
- 🟡 **WARNING** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:532): Function "_build_status_summary" has 12 parameters - consider using parameter object or reducing parameters

#### <span id="use-domain-language-violations">Use Domain Language: 6 violation(s)</span>

- 🟡 **WARNING** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:23): Function "generate_cli_code" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:594): Function "generate_bot_config_file" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:613): Function "generate_server_entry_point" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:695): Function "generate_cursor_mcp_config" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:727): Function "generate_server" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").
- 🟡 **WARNING** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:741): Function "generate_awareness_files" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

#### <span id="use-explicit-dependencies-violations">Use Explicit Dependencies: 1 violation(s)</span>

- 🟡 **WARNING** - [`src\utils.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/utils.py:136): Global variable usage detected - dependencies should be explicit (passed as parameters)

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 51 violation(s)</span>

- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:21): Duplicate code detected across files: __init__() in behavior.py (lines 21-26) matches __init__() in behavior_config.py (lines 13-18) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:22): Duplicate code detected across files: __init__() in behavior.py (lines 22-32) matches __init__() in behavior_config.py (lines 14-24) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:23): Duplicate code detected across files: __init__() in behavior.py (lines 23-34) matches __init__() in behavior_config.py (lines 15-26) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:34): Duplicate code detected across files: __init__() in behavior.py (lines 34-39) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:34): Duplicate code detected across files: __init__() in behavior.py (lines 34-39) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:36): Duplicate code detected across files: __init__() in behavior.py (lines 36-40) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:36): Duplicate code detected across files: __init__() in behavior.py (lines 36-40) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:37): Duplicate code detected across files: __init__() in behavior.py (lines 37-41) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:37): Duplicate code detected across files: __init__() in behavior.py (lines 37-41) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:38): Duplicate code detected across files: __init__() in behavior.py (lines 38-42) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:38): Duplicate code detected across files: __init__() in behavior.py (lines 38-42) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:39): Duplicate code detected across files: __init__() in behavior.py (lines 39-44) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:39): Duplicate code detected across files: __init__() in behavior.py (lines 39-44) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:40): Duplicate code detected across files: __init__() in behavior.py (lines 40-45) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:40): Duplicate code detected across files: __init__() in behavior.py (lines 40-45) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:41): Duplicate code detected across files: __init__() in behavior.py (lines 41-46) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:41): Duplicate code detected across files: __init__() in behavior.py (lines 41-46) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:42): Duplicate code detected across files: __init__() in behavior.py (lines 42-47) matches __init__() in bot.py (lines 29-34) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:42): Duplicate code detected across files: __init__() in behavior.py (lines 42-47) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:44): Duplicate code detected across files: __init__() in behavior.py (lines 44-48) matches __init__() in bot.py (lines 30-36) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:21): Duplicate code detected across files: __init__() in behavior.py (lines 21-32) matches __init__() in behavior_config.py (lines 13-24) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:22): Duplicate code detected across files: __init__() in behavior.py (lines 22-34) matches __init__() in behavior_config.py (lines 14-26) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:34): Duplicate code detected across files: __init__() in behavior.py (lines 34-40) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:36): Duplicate code detected across files: __init__() in behavior.py (lines 36-41) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:37): Duplicate code detected across files: __init__() in behavior.py (lines 37-42) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:38): Duplicate code detected across files: __init__() in behavior.py (lines 38-44) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:39): Duplicate code detected across files: __init__() in behavior.py (lines 39-45) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:40): Duplicate code detected across files: __init__() in behavior.py (lines 40-46) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:41): Duplicate code detected across files: __init__() in behavior.py (lines 41-47) matches sort_key() in validation_report_writer.py (lines 652-657) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behavior.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behavior.py:21): Duplicate code detected across files: __init__() in behavior.py (lines 21-34) matches __init__() in behavior_config.py (lines 13-26) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:133): Duplicate code detected across files: _inject_next_behavior_reminder() in behaviors.py (lines 133-139) matches _inject_reminders_if_final() in action.py (lines 554-559) - extract to shared function
- 🔴 **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:133): Duplicate code detected across files: _inject_next_behavior_reminder() in behaviors.py (lines 133-139) matches _inject_reminders_if_final() in action.py (lines 554-561) - extract to shared function
- 🔴 **ERROR** - [`src\bot\bot_paths.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/bot_paths.py:37): Duplicate code detected across files: _load_documentation_path() in bot_paths.py (lines 37-42) matches _load_trigger_words_from_behavior_folder() in mcp_server_generator.py (lines 584-590) - extract to shared function
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:134): Duplicate code detected across files: close_current_action() in base_bot_cli.py (lines 134-139) matches invoke() in bot_tool_generator.py (lines 27-32) - extract to shared function
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:134): Duplicate code detected across files: close_current_action() in base_bot_cli.py (lines 134-139) matches register_bot_tool() in mcp_server_generator.py (lines 127-132) - extract to shared function
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:191): Duplicate code detected across files: _route_to_current_behavior_and_action() in base_bot_cli.py (lines 191-196) matches invoke() in bot_tool_generator.py (lines 27-32) - extract to shared function
- 🔴 **ERROR** - [`src\cli\base_bot_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/base_bot_cli.py:191): Duplicate code detected across files: _route_to_current_behavior_and_action() in base_bot_cli.py (lines 191-196) matches register_bot_tool() in mcp_server_generator.py (lines 127-132) - extract to shared function
- 🔴 **ERROR** - [`src\cli\cli_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_generator.py:215): Duplicate code detected across files: _discover_behaviors_from_folders() in cli_generator.py (lines 215-224) matches _discover_behaviors_from_folders() in server_deployer.py (lines 65-74) - extract to shared function
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:262): Duplicate code detected across files: _load_bot_triggers() in trigger_router.py (lines 262-267) matches _load_trigger_words_from_behavior_folder() in mcp_server_generator.py (lines 584-590) - extract to shared function
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:262): Duplicate code detected across files: _load_bot_triggers() in trigger_router.py (lines 262-267) matches _load_trigger_words() in server_deployer.py (lines 173-178) - extract to shared function
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:379): Duplicate code detected across files: _load_patterns_from_file() in trigger_router.py (lines 379-384) matches _load_trigger_words_from_behavior_folder() in mcp_server_generator.py (lines 584-590) - extract to shared function
- 🔴 **ERROR** - [`src\cli\trigger_router.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/trigger_router.py:379): Duplicate code detected across files: _load_patterns_from_file() in trigger_router.py (lines 379-384) matches _load_trigger_words() in server_deployer.py (lines 173-178) - extract to shared function
- 🔴 **ERROR** - [`src\mcp\bot_tool_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/bot_tool_generator.py:27): Duplicate code detected across files: invoke() in bot_tool_generator.py (lines 27-32) matches register_bot_tool() in mcp_server_generator.py (lines 127-132) - extract to shared function
- 🔴 **ERROR** - [`src\mcp\mcp_server_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/mcp/mcp_server_generator.py:584): Duplicate code detected across files: _load_trigger_words_from_behavior_folder() in mcp_server_generator.py (lines 584-590) matches _load_trigger_words() in server_deployer.py (lines 173-178) - extract to shared function
- 🔴 **ERROR** - [`src\actions\build\knowledge_graph_template.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/knowledge_graph_template.py:8): Duplicate code detected across files: __init__() in knowledge_graph_template.py (lines 8-12) matches __init__() in validation_scope.py (lines 12-16) - extract to shared function
- 🔴 **ERROR** - [`src\actions\clarify\requirements_clarifications.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/requirements_clarifications.py:13): Duplicate code detected across files: __init__() in requirements_clarifications.py (lines 13-17) matches __init__() in strategy_decision.py (lines 12-16) - extract to shared function
- 🔴 **ERROR** - [`src\actions\clarify\requirements_clarifications.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/clarify/requirements_clarifications.py:22): Duplicate code detected across files: save() in requirements_clarifications.py (lines 22-37) matches save() in strategy_decision.py (lines 28-44) - extract to shared function
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:217): Duplicate code detected across files: _execute_synchronizer() in render_action.py (lines 217-223) matches sort_key() in validation_report_writer.py (lines 652-656) - extract to shared function
- 🔴 **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:217): Duplicate code detected across files: _execute_synchronizer() in render_action.py (lines 217-223) matches sort_key() in validation_report_writer.py (lines 653-657) - extract to shared function
- 🔴 **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:212): Duplicate code detected across files: injectValidationInstructions() in validate_action.py (lines 212-216) matches _build_scanner_status() in validation_report_writer.py (lines 357-365) - extract to shared function
- 🔴 **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:212): Duplicate code detected across files: injectValidationInstructions() in validate_action.py (lines 212-216) matches _build_scanner_status() in validation_report_writer.py (lines 370-376) - extract to shared function

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
*... and 275 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\code-validation-report.md`
