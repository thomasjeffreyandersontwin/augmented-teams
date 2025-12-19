# Validation Report - Code

**Generated:** 2025-12-19 18:46:06
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 7 code file(s) against **33 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\cli\cli_generator.py`
  - `src\cli\cli_help_generator.py`
  - `src\cli\cli_help_renderer.py`
  - `src\cli\cursor_command_generator.py`
  - `src\cli\cursor_help_renderer.py`
  - `src\cli\help_renderer.py`
  - `src\cli\unified_help_generator.py`
  - **Total:** 7 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 31 | Scanners ran without errors |
| 🟩 Clean Rules | 27 | No violations found |
| 🟨 Rules with Warnings | 3 | Found 13 warning violation(s) |
| 🟥 Rules with Errors | 1 | Found 25 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 33
- **Rules with Scanners:** 31
  - 🟩 **Executed Successfully:** 31
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 25 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 6 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟩 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟩 **[Enforce Encapsulation](#enforce-encapsulation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟩 **[Maintain Test Quality](#maintain-test-quality)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
- 🟩 **[Maintain Vertical Density](#maintain-vertical-density)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟩 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Provide Meaningful Context](#provide-meaningful-context)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟩 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟩 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
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
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 25 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 6 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** Function signatures should be simple and intention-revealing. Prefer 0-2 parameters; use objects for more complex needs.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 4 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 3 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - CLEAN (0 violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - CLEAN (0 violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="delegate-to-lowest-level">Delegate To Lowest Level</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data, and follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code should represent domain concepts directly. Domain models should match code. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must be organized by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-business-logic-behind-properties">Hide Business Logic Behind Properties</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide business logic behind properties. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must hide calculations. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
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

### 🟩 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - CLEAN (0 violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-test-quality">Maintain Test Quality</span> - CLEAN (0 violations)
**Description:** CRITICAL: Tests should be as clean as production code. Keep tests readable and maintainable, use descriptive test names, and follow FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-vertical-density">Maintain Vertical Density</span> - CLEAN (0 violations)
**Description:** Related code should be visually close. Group related concepts together, declare variables close to usage, and keep files under 500 lines when possible.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - CLEAN (0 violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 13 more rules*

## Violations Found

**Total Violations:** 38
- **File-by-File Violations:** 13
- **Cross-File Violations:** 25

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:12): Method "render_header" in Test class [CursorHelpRenderer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:12) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:20): Method "render_behavior_section" in Test class [CursorHelpRenderer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:20) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:42): Method "render_action_help" in Test class [CursorHelpRenderer](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:42) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 4 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\unified_help_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/unified_help_generator.py:82): Function "_get_action_parameters" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\unified_help_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/unified_help_generator.py:99): Function "_get_parameter_descriptions" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:38): Function "render_action_help" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:42): Function "render_action_help" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 6 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Function "render_behavior_section" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:38): Function "render_action_help" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:20): Function "render_behavior_section" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:42): Function "render_action_help" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:14): Function "render_behavior_section" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:24): Function "render_action_help" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 25 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 19-23)):
    ```python
    print(f'\n## {bot_name}-{behavior_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 23-27)):
    ```python
    print(f'## {cmd_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 20-24)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 24-28)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 21-25)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 25-29)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 22-26)):
    ```python
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 26-30)):
    ```python
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:24): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 24-31)):
    ```python
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options.items():
            print(f'           {option}  {description}')
    print('```\n')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 28-35)):
    ```python
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options.items():
            print(f'           {option}  {description}')
    print('```\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 19-24)):
    ```python
    print(f'\n## {bot_name}-{behavior_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 23-28)):
    ```python
    print(f'## {cmd_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 20-25)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 24-29)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 21-26)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 25-30)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:23): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 23-31)):
    ```python
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additiona...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 27-35)):
    ```python
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options.items():
            print(f'           {option}...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 19-25)):
    ```python
    print(f'\n## {bot_name}-{behavior_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 23-29)):
    ```python
    print(f'## {cmd_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 20-26)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 24-30)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 21-30)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional option...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 25-34)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 22-31)):
    ```python
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for ...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 26-35)):
    ```python
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options.items():
       ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 19-26)):
    ```python
    print(f'\n## {bot_name}-{behavior_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional contex...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 23-30)):
    ```python
    print(f'## {cmd_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 20-30)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        ...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 24-34)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 21-31)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional option...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 26-35)):
    ```python
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options.items():
       ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 21-31)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional option...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 25-35)):
    ```python
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option, description in additional_options...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 19-30)):
    ```python
    print(f'\n## {bot_name}-{behavior_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional contex...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 23-34)):
    ```python
    print(f'## {cmd_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 20-31)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        ...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 24-35)):
    ```python
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional options:')
        for option...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_behavior_section (lines 19-31)):
    ```python
    print(f'\n## {bot_name}-{behavior_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'python {self.cli_script_path} --behavior {behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional contex...
    ```

  Location 2 (cursor_help_renderer.py:render_behavior_section (lines 23-35)):
    ```python
    print(f'## {cmd_name}\n')
    print(f'{behavior_description}\n')
    print('```')
    action_list = '|'.join(actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if additional_options:
        print('           Additional...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:46): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_action_help (lines 46-54)):
    ```python
    param_desc = parameter_descriptions.get(param, 'Optional parameter')
    if '\n' in param_desc:
        lines = param_desc.split('\n')
        print(f'{param}:   {lines[0]}')
        for line in lines[1:]:
            print(f'    {line}')
    else:
        print(f'{param}:   {param_desc}')
    ```

  Location 2 (cursor_help_renderer.py:render_action_help (lines 50-58)):
    ```python
    param_desc = parameter_descriptions.get(param, 'Optional parameter')
    if '\n' in param_desc:
        lines = param_desc.split('\n')
        print(f'{param}:   {lines[0]}')
        for line in lines[1:]:
            print(f'    {line}')
    else:
        print(f'{param}:   {param_desc}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:48): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_action_help (lines 48-54)):
    ```python
    lines = param_desc.split('\n')
    print(f'{param}:   {lines[0]}')
    for line in lines[1:]:
        print(f'    {line}')
    ```

  Location 2 (cursor_help_renderer.py:render_action_help (lines 52-58)):
    ```python
    lines = param_desc.split('\n')
    print(f'{param}:   {lines[0]}')
    for line in lines[1:]:
        print(f'    {line}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_action_help (lines 40-54)):
    ```python
    print(f'### {action_name}\n')
    print(f'{action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {action_name} [parameters]')
    if parameters:
        print()
        for param in parameters:
            param_desc = parameter_descriptions.get(param, 'Optional param...
    ```

  Location 2 (cursor_help_renderer.py:render_action_help (lines 44-58)):
    ```python
    print(f'### {action_name}\n')
    print(f'{action_description}\n')
    print('```')
    print(f'/{bot_name}-<behavior> {action_name} [parameters]')
    if parameters:
        print()
        for param in parameters:
            param_desc = parameter_descriptions.get(param, 'Optional parameter')
            if '\n' in param_desc:
    ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:41): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_action_help (lines 41-55)):
    ```python
    print(f'{action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {action_name} [parameters]')
    if parameters:
        print()
        for param in parameters:
            param_desc = parameter_descriptions.get(param, 'Optional parameter')
            if '\n' in para...
    ```

  Location 2 (cursor_help_renderer.py:render_action_help (lines 45-59)):
    ```python
    print(f'{action_description}\n')
    print('```')
    print(f'/{bot_name}-<behavior> {action_name} [parameters]')
    if parameters:
        print()
        for param in parameters:
            param_desc = parameter_descriptions.get(param, 'Optional parameter')
            if '\n' in param_desc:
                lines = param_desc...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:render_action_help (lines 40-55)):
    ```python
    print(f'### {action_name}\n')
    print(f'{action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {action_name} [parameters]')
    if parameters:
        print()
        for param in parameters:
            param_desc = parameter_descriptions.get(param, 'Optional param...
    ```

  Location 2 (cursor_help_renderer.py:render_action_help (lines 44-59)):
    ```python
    print(f'### {action_name}\n')
    print(f'{action_description}\n')
    print('```')
    print(f'/{bot_name}-<behavior> {action_name} [parameters]')
    if parameters:
        print()
        for param in parameters:
            param_desc = parameter_descriptions.get(param, 'Optional parameter')
            if '\n' in param_desc:
    ...
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
*... and 250 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\code-validation-report.md`
