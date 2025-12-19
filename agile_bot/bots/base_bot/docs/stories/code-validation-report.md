# Validation Report - Code

**Generated:** 2025-12-19 10:31:45
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model against **40 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\actions\action.py`
  - `src\actions\action_factory.py`
  - `src\actions\action_scope.py`
  - `src\actions\action_state_manager.py`
  - `src\actions\actions.py`
  - `src\actions\activity_tracker.py`
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
  - `src\actions\context_data_injector.py`
  - `src\actions\guardrails.py`
  - `src\actions\render\evidence.py`
  - `src\actions\render\render_action.py`
  - `src\actions\render\render_config_loader.py`
  - `src\actions\render\render_instruction_formatter.py`
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
  - `src\actions\validate\background_validation_handler.py`
  - `src\actions\validate\file_discovery.py`
  - `src\actions\validate\file_link_builder.py`
  - `src\actions\validate\knowledge_graph.py`
  - `src\actions\validate\path_resolver.py`
  - `src\actions\validate\rule.py`
  - `src\actions\validate\rule_filter.py`
  - `src\actions\validate\rule_loader.py`
  - `src\actions\validate\rules.py`
  - `src\actions\validate\scanner_status_formatter.py`
  - `src\actions\validate\story_graph.py`
  - `src\actions\validate\validate_action.py`
  - `src\actions\validate\validation_executor.py`
  - `src\actions\validate\validation_report_builder.py`
  - `src\actions\validate\validation_report_formatter.py`
  - `src\actions\validate\validation_report_writer.py`
  - `src\actions\validate\validation_scanner_status_builder.py`
  - `src\actions\validate\validation_scope.py`
  - `src\actions\validate\validation_stats.py`
  - `src\actions\validate\validation_violations_builder.py`
  - `src\actions\validate\violation_formatter.py`
  - `src\actions\workflow_status_builder.py`
  - `src\bot\behavior.py`
  - `src\bot\behaviors.py`
  - `src\bot\bot.py`
  - `src\bot\bot_paths.py`
  - `src\bot\instructions.py`
  - `src\bot\merged_instructions.py`
  - `src\bot\reminders.py`
  - `src\bot\trigger_words.py`
  - `src\bot\workspace.py`
  - `src\cli\base_bot_cli.py`
  - `src\cli\behavior_matcher.py`
  - `src\cli\bot_matcher.py`
  - `src\cli\cli_command_router.py`
  - `src\cli\cli_executor.py`
  - `src\cli\cli_generator.py`
  - `src\cli\cli_help_generator.py`
  - `src\cli\cli_parameter_parser.py`
  - `src\cli\cli_script_generator.py`
  - `src\cli\cursor_command_generator.py`
  - `src\cli\description_extractor.py`
  - `src\cli\parameter_info_builder.py`
  - `src\cli\trigger_domain.py`
  - `src\cli\trigger_router.py`
  - `src\cli\trigger_router_entry.py`
  - `src\mcp\behavior_tool_generator.py`
  - `src\mcp\bot_tool_generator.py`
  - `src\mcp\mcp_code_generator.py`
  - `src\mcp\mcp_config_generator.py`
  - `src\mcp\mcp_server.py`
  - `src\mcp\mcp_server_generator.py`
  - `src\mcp\mcp_tool_registrar.py`
  - `src\mcp\server_deployer.py`
  - `src\mcp\server_restart.py`
  - `src\story_graph\domain.py`
  - `src\story_graph\nodes.py`
  - **Total:** 92 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 34 | Scanners ran without errors |
| 🟩 Clean Rules | 24 | No violations found |
| 🟨 Rules with Warnings | 7 | Found 27 warning violation(s) |
| 🟥 Rules with Errors | 1 | Found 1 error violation(s) |
| [i] No Scanner | 6 | Rule has no scanner configured |

**Total Rules:** 40
- **Rules with Scanners:** 34
  - 🟩 **Executed Successfully:** 34
- [i] **Rules without Scanners:** 6

### 🟩 Successfully Executed Scanners

- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 6 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟨 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-unnecessary-parameter-passing-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟨 **[Provide Meaningful Context](#provide-meaningful-context)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟨 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟨 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#delegate-to-lowest-level-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Remove Bad Comments](#remove-bad-comments)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#remove-bad-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Enforce Encapsulation](#enforce-encapsulation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Follow Open Closed Principle](#follow-open-closed-principle)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.open_closed_principle_scanner.OpenClosedPrincipleScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Maintain Test Quality](#maintain-test-quality)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
- 🟩 **[Maintain Vertical Density](#maintain-vertical-density)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟩 **[Minimize Mutable State](#minimize-mutable-state)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.minimize_mutable_state_scanner.MinimizeMutableStateScanner`
- 🟩 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟩 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟩 **[Test Boundary Behavior](#test-boundary-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_boundary_behavior_scanner.TestBoundaryBehaviorScanner`
- 🟩 **[Test One Concept Per Test](#test-one-concept-per-test)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.one_concept_per_test_scanner.OneConceptPerTestScanner`
- 🟩 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟩 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟩 **[Use Domain Language](#use-domain-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟩 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_handling_scanner.ExceptionHandlingScanner`
- 🟩 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Use Natural English](#use-natural-english)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.natural_english_code_scanner.NaturalEnglishCodeScanner`
- 🟩 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Enforce Team Formatting Consensus](#enforce-team-formatting-consensus)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Handle Backward Compatibility](#handle-backward-compatibility)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Practice Test Driven Development](#practice-test-driven-development)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Write Good Comments](#write-good-comments)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 1 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 14 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** Function signatures should be simple and intention-revealing. Prefer 0-2 parameters; use objects for more complex needs.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 6 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - 2 WARNING(S) - [View Details](#avoid-unnecessary-parameter-passing-violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 2 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 1 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="remove-bad-comments">Remove Bad Comments</span> - 1 WARNING(S) - [View Details](#remove-bad-comments-violations)
**Description:** CRITICAL: Some comments actively harm readability. Delete commented-out code (it's in git), remove misleading or outdated comments, and eliminate redundant noise.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.bad_comments_scanner.BadCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 1 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data, and follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code should represent domain concepts directly. Domain models should match code. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="follow-open-closed-principle">Follow Open Closed Principle</span> - CLEAN (0 violations)
**Description:** Open for extension, closed for modification. Design for extension without modification, depend on interfaces/abstractions not concrete types, and use composition over inheritance.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.open_closed_principle_scanner.OpenClosedPrincipleScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must be organized by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must hide calculation timing. Properties hide when calculations occur—they may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the value was calculated.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="keep-functions-single-responsibility">Keep Functions Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Functions should do one thing and do it well, with no hidden side effects. Each function must have a single, well-defined responsibility.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-test-quality">Maintain Test Quality</span> - CLEAN (0 violations)
**Description:** CRITICAL: Tests should be as clean as production code. Keep tests readable and maintainable, use descriptive test names, and follow FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-vertical-density">Maintain Vertical Density</span> - CLEAN (0 violations)
**Description:** Related code should be visually close. Group related concepts together, declare variables close to usage, and keep files under 500 lines when possible.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="minimize-mutable-state">Minimize Mutable State</span> - CLEAN (0 violations)
**Description:** CRITICAL: Prefer immutable data structures and pure functions. Use immutable data structures by default, create new objects instead of mutating, and make immutability explicit in type system.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.minimize_mutable_state_scanner.MinimizeMutableStateScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 20 more rules*

## Violations Found

**Total Violations:** 30
- **File-by-File Violations:** 30
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 6 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:156): Line 156: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:27): Line 27: Variable truthiness check detected (if not is_absolute:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\file_link_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_link_builder.py:52): Line 52: Variable truthiness check detected (if line_number:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:42): Line 42: Variable truthiness check detected (if has_scope_in_params:). Assume variable exists - let code fail fast if missing.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:247): Line 247: None check guard clause detected. Assume variables are initialized - let code fail fast if None.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:251): Line 251: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

#### <span id="avoid-unnecessary-parameter-passing-violations">Avoid Unnecessary Parameter Passing: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\actions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/actions.py:114): Instance property "self.current" is extracted to variable "current_action_obj" and passed to internal method "_mark_action_completed". Access via self.current directly instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\build\build_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/build/build_action.py:51): Instance property "self.knowledge_graph_spec.knowledge_graph" is extracted to variable "story_graph" and passed to internal method "_add_update_instructions". Access via self.knowledge_graph_spec.knowledge_graph directly instead.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rule_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule_loader.py:20): Method "_load_rules_from_glob" in Test class [RuleLoader](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule_loader.py:20) takes parameter "behavior" that is already injected in __init__. Use self.behavior instead.

#### <span id="delegate-to-lowest-level-violations">Delegate To Lowest Level: 1 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\file_discovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_discovery.py:21): Method "should_include_file" in Test class [FileDiscovery](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/file_discovery.py:21) iterates through "exclude_patterns" instead of delegating to collection class. Delegate to collection class instead.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\story_graph\nodes.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/story_graph/nodes.py:230): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (from_dict:230-234):
    ```python
    sequential_order = float(data.get('sequential_order', index + 1))
    scenario = cls(name=data.get('name', ''), sequential_order=sequential_order, type=data.get('type', ''), background=data.get('backgroun...
    ```

  Location (from_dict:273-277):
    ```python
    sequential_order = float(data.get('sequential_order', index + 1))
    scenario_outline = cls(name=data.get('name', ''), sequential_order=sequential_order, type=data.get('type', ''), background=data.get('b...
    ```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 1 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:29): Function "categorize_scanner_rules" has deep nesting (depth=5) - should be under 4 levels. Extract nested logic to helper functions.

    ```python
            return lines
    
        def categorize_scanner_rules(self, validation_rules: List[Dict[str, Any]]) -> Dict:
            """Categorize rules by execution status."""
            executed_rules = []
            load_failed_rules = []
            execution_failed_rules = []
            no_scanner_rules = []
            for rule_dict in validation_rules:
                category = self._get_rule_category(rule_dict)
                if category == 'executed':
                    executed_rules.append(self._build_executed_rule_entry(rule_dict))
                elif category == 'load_failed':
                    load_failed_rules.append(self._build_failed_rule_entry(rule_dict))
                elif category == 'execution_failed':
                    execution_failed_rules.append(self._build_failed_rule_entry(rule_dict))
                elif category == 'no_scanner':
                    no_scanner_rules.append(self._get_rule_file(rule_dict))
            return {'executed': executed_rules, 'load_failed': load_failed_rules, 'execution_failed': execution_failed_rules, 'no_scanner': no_scanner_rules}
    
    ```

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:6): Line 6 contains magic number - replace with named constant
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:8): Line 8 contains magic number - replace with named constant

#### <span id="remove-bad-comments-violations">Remove Bad Comments: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:143): Line 143 has commented-out code - delete it (it's in git history if needed)

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\scanner_status_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/scanner_status_formatter.py:29): Function "categorize_scanner_rules" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 14 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\workflow_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/workflow_status_builder.py:115): Function "_build_current_behavior_section" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_instruction_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_formatter.py:33): Function "_update_instructions_dict" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:143): Function "_execute_file_by_file_scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rule.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rule.py:155): Function "_execute_cross_file_scan" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:176): Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:192): Function "_execute_scanner" has 10 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:212): Function "_process_rule" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:224): Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/rules.py:229): Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_executor.py:81): Function "_process_scanner_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:38): Function "_categorize_rule_by_status" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:241): Function "_get_rule_status_display" has vague parameter name "info" - use descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scanner_status_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scanner_status_builder.py:255): Function "_format_rule_scanner_info" has vague parameter name "info" - use descriptive name
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\parameter_info_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/parameter_info_builder.py:24): Function "add_param_detail" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

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
*... and 256 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\code-validation-report.md`
