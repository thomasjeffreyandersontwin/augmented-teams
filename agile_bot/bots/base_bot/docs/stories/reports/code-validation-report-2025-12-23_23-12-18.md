# Validation Report - Code

**Generated:** 2025-12-23 23:14:58
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 10 code file(s) against **32 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\actions\action_context.py`
  - `src\actions\build\build_scope.py`
  - `src\actions\rules\rules.py`
  - `src\cli\cli_context_builder.py`
  - `src\cli\cli_parser_generator.py`
  - `src\cli\type_hint_converter.py`
  - `test\test_build_knowledge.py`
  - `test\test_decide_strategy_criteria_action.py`
  - `test\test_invoke_cli.py`
  - `test\test_validate_knowledge_and_content_against_rules.py`
  - **Total:** 10 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: NEEDS ATTENTION

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 14 | No violations found |
| 🟨 Rules with Warnings | 10 | Found 81 warning violation(s) |
| 🟥 Rules with Errors | 5 | Found 629 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 589 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 27 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟥 **[Place Imports At Top](#place-imports-at-top)** - 23 violation(s) (EXECUTION_SUCCESS) - [View Details](#place-imports-at-top-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟨 **[Provide Meaningful Context](#provide-meaningful-context)** - 16 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 15 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 10 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 8 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟨 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#classify-exceptions-by-caller-needs-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟨 **[Enforce Encapsulation](#enforce-encapsulation)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-encapsulation-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟨 **[Use Domain Language](#use-domain-language)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟥 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-resource-oriented-design-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟩 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟩 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟩 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_handling_scanner.ExceptionHandlingScanner`
- 🟩 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Use Natural English](#use-natural-english)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.natural_english_code_scanner.NaturalEnglishCodeScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 589 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - 23 ERROR(S) - [View Details](#place-imports-at-top-violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 15 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 1 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="use-resource-oriented-design">Use Resource Oriented Design</span> - 1 ERROR(S) - [View Details](#use-resource-oriented-design-violations)
**Description:** CRITICAL: Code must use resource-oriented, object-oriented design. Use object-oriented classes (singular or collection) with responsibilities that encapsulate logic over manager/doer/loader patterns. Maximize encapsulation through collaborator relationships.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 27 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 16 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 14 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 10 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 5 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** CRITICAL: Function signatures must be simple and intention-revealing. Prefer 0-2 parameters. NEVER pass Dict[str, Any] or List[str] for complex data - create typed objects instead. Examples: parameters dict → ParametersObject, files dict → FilesCollection, exclude list → ExcludePatterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 4 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - 2 WARNING(S) - [View Details](#classify-exceptions-by-caller-needs-violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - 1 WARNING(S) - [View Details](#enforce-encapsulation-violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 1 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-domain-language">Use Domain Language</span> - 1 WARNING(S) - [View Details](#use-domain-language-violations)
**Description:** CRITICAL: Code must use domain-specific language, not generic terms. NEVER use Dict[str, Any], List[str], or generic 'data'/'config'/'parameters' - use typed domain objects. Objects should expose properties representing what they contain (e.g., recommended_trades), not methods that 'generate' or 'calculate' things.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - CLEAN (0 violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="delegate-to-lowest-level">Delegate To Lowest Level</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code should represent domain concepts directly. Domain models should match code. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must be organized by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 12 more rules*

## Violations Found

**Total Violations:** 718
- **File-by-File Violations:** 706
- **Cross-File Violations:** 12

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 10 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:32): Line 32: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

    ```python
        @classmethod
        def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
            if not data:
                return cls()
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:145): Line 145: Variable truthiness check detected (if changed:). Assume variable exists - let code fail fast if missing.

    ```python
            for file_type, file_list in files.items():
                changed = [f for f in file_list if f.stat().st_mtime > last_report_time]
                if changed:
                    changed_files[file_type] = changed
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:776): Line 776: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
        when_create_test_files_parameter, when_create_code_files_parameter, when_create_empty_parameters
        """
        if scope is not None:
            return _convert_scope_config_to_unified_format(scope) if scope else {}
        elif test_files is not None:
            # Handle both single Path and list of Paths
            if isinstance(test_files, (list, tuple)):
                return {'test': [str(f) for f in test_files]}
            else:
                return {'test': str(test_files)}
        elif code_files is not None:
            return {'src': [str(f) for f in code_files]}
        else:
            return {}
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1101): Line 1101: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
        
        # Convert legacy dict parameters to typed context if needed
        if context is not None:
            return action.do_execute(context)
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1104): Line 1104: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
            return action.do_execute(context)
        
        if parameters is None:
            return action.do_execute(ValidateActionContext())
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1235): Line 1235: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
            Tuple of (file_path, parameters_dict) or (None, bad_example)
        """
        if bad_example is None:
            return given_test_file_for_scanner_type(directory, scanner_class_path, behavior)
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:232): Line 232: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
            """
            route = self._create_router_and_match(trigger_message, current_behavior, current_action)
            if route is None:
                return None, None
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1412): Line 1412: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
        from agile_bot.bots.base_bot.src.actions.scoping_parameter import ScopingParameter
        scope = {'type': scope_type}
        if scope_value is not None:
            scope['value'] = scope_value
        scoping_param = ScopingParameter(scope)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:98): Line 98: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
            Tuple of (assumptions, criteria)
        """
        if assumptions is None:
            assumptions = ['Stories follow user story format', 'Acceptance criteria are testable']
        if criteria is None:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:100): Line 100: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
        if assumptions is None:
            assumptions = ['Stories follow user story format', 'Acceptance criteria are testable']
        if criteria is None:
            criteria = {'scope': ['Component', 'System', 'Solution']}
        return assumptions, criteria
    ```

#### <span id="classify-exceptions-by-caller-needs-violations">Classify Exceptions By Caller Needs: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:927): Line 927 defines component-based exception - exceptions should be classified by how caller handles them, not by component
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:929): Line 929 defines component-based exception - exceptions should be classified by how caller handles them, not by component

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 4 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1138): Duplicate code detected: functions test_scenario_map_location, test_scenario_map_location have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1149): Duplicate code detected: functions test_scenario_outline_map_location, test_scenario_outline_map_location have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1160): Duplicate code detected: functions test_from_bot_loads_story_graph, test_from_bot_loads_story_graph have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1171): Duplicate code detected: functions test_from_bot_with_path, test_from_bot_with_path have identical bodies - extract to shared function

#### <span id="enforce-encapsulation-violations">Enforce Encapsulation: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:586): Method "test_trigger_bot_only_no_behavior_or_action_specified" in Test class [TestDetectTriggerWordsThroughExtension](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:586) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2717): Class "TestValidateRulesAccordingToScope" is 734 lines - should be under 300 lines (extract related methods into separate classes)

```python
# ============================================================================

class TestValidateRulesAccordingToScope:
    """Story: Validate Rules According to Scope - Tests that validate only processes stories within specified scope."""

    @staticmethod
    def create_comprehensive_story_graph() -> Dict[str, Any]:
        """Create a comprehensive story graph with multiple epics, sub-epics, stories, and increments."""
        return {
            "epics": [
    # ... (truncated)
```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 27 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:35): Function "generate_parsers_for_bot" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            self._generated_lines: List[str] = []
        
        def generate_parsers_for_bot(self, bot) -> str:
            self._generated_lines = []
            self._add_header()
            self._add_imports()
            
            # Collect all unique context classes
            context_classes_seen = set()
            action_mappings = []
            
            for behavior in bot.behaviors:
                for action in behavior.actions:
                    context_class = action.context_class
                    action_name = action.action_name
                    
                    if context_class not in context_classes_seen:
                        context_classes_seen.add(context_class)
                        self._generate_parser_function(context_class)
                    
                    # Record mapping
                    action_mappings.append((behavior.name, action_name, context_class.__name__))
            
            self._add_blank_line()
            self._generate_context_builder_functions()
            self._add_blank_line()
            self._generate_action_parser_mapping(action_mappings)
            
            return '\n'.join(self._generated_lines)
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:66): Function "from_parameters" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        
        @classmethod
        def from_parameters(cls, parameters: Dict[str, Any], behavior, bot_paths, callbacks: Optional[ValidationCallbacks] = None) -> 'ValidationContext':
            from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
            from agile_bot.bots.base_bot.src.bot.behavior import Behavior
            
            if isinstance(behavior, str):
                behavior = Behavior(name=behavior, bot_paths=bot_paths)
            
            scope = None
            if 'scope' in parameters and parameters['scope']:
                scope_dict = parameters['scope']
                if isinstance(scope_dict, dict):
                    scope_type_str = scope_dict.get('type', 'all')
                    scope_type = ScopeType(scope_type_str)
                    scope = Scope(
                        type=scope_type,
                        value=scope_dict.get('value', []),
                        exclude=scope_dict.get('exclude', []),
                        skiprule=scope_dict.get('skiprule', [])
                    )
            
            # Handle both all_files and force_full (backward compatibility)
            all_files = parameters.get('all_files', False) or parameters.get('force_full', False)
            
            context = ValidateActionContext(
                scope=scope,
                background=parameters.get('background'),
                skip_cross_file=parameters.get('skip_cross_file', False),
                all_files=all_files
            )
            
            return cls.from_action_context(behavior, context, callbacks)
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:106): Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return rules_instance._rule_filter.filter_files(self.files, self.exclude)
    
        def get_last_report_timestamp(self) -> float:
            logger = logging.getLogger(__name__)
            docs_path = self.bot_paths.documentation_path
            reports_dir = self.bot_paths.workspace_directory / docs_path / 'reports'
            logger.info(f'Looking for previous reports in: {reports_dir}')
            if not reports_dir.exists():
                logger.info('Reports directory does not exist - returning 0.0')
                return 0.0
            
            report_files = list(reports_dir.glob(f'{self.behavior.name}-validation-status-*.md'))
            logger.info(f'Found {len(report_files)} report files')
            if not report_files:
                logger.info('No report files found - returning 0.0')
                return 0.0
            
            current_time = time.time()
            previous_run_files = [f for f in report_files if (current_time - f.stat().st_mtime) > 10]
            logger.info(f'Found {len(previous_run_files)} previous run files (excluding files < 10 seconds old)')
            
            if not previous_run_files:
                logger.info('No previous run files found - returning 0.0')
                return 0.0
            
            most_recent = max(previous_run_files, key=lambda p: p.stat().st_mtime)
            logger.info(f'Most recent previous report: {most_recent.name} (timestamp: {most_recent.stat().st_mtime})')
            return most_recent.stat().st_mtime
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:234): Function "then_domain_terms_extracted_correctly" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def then_domain_terms_extracted_correctly(extracted_terms: Set[str], expected_terms: Set[str]):
        """Then: Domain terms extracted correctly from story graph.
        
        Verifies extracted terms match expected, including compound terms.
        
        Args:
            extracted_terms: Set of extracted domain terms
            expected_terms: Set of expected domain terms
        """
        # Verify all expected terms are present (or at least their components)
        missing_terms = []
        for expected_term in expected_terms:
            # Check if term itself is present
            if expected_term in extracted_terms:
                continue
            # Check if words from term are present (for compound terms)
            words = expected_term.lower().replace('_', ' ').split()
            if not any(word in extracted_terms for word in words):
                missing_terms.append(expected_term)
        
        assert len(missing_terms) == 0, (
            f"Missing expected domain terms: {missing_terms}. "
            f"Extracted terms: {sorted(list(extracted_terms))[:20]}"
        )
        
        # Verify compound terms (snake_case versions) are extracted
        has_compound_terms = any('_' in term for term in extracted_terms)
        assert has_compound_terms or len(expected_terms) == 0, (
            "Expected compound terms (snake_case) to be extracted, but none found. "
            f"Extracted terms: {sorted(list(extracted_terms))[:20]}"
        )
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:267): Function "given_spy_scanner_for_unified_architecture" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def given_spy_scanner_for_unified_architecture():
        """Given: Spy scanner that records calls for unified architecture testing.
        
        Returns a spy scanner class that records:
        - received_files: List of files received
        - called_is_test_file: Whether _is_test_file() was called
        
        Returns:
            Tuple of (spy_scanner_class, spy_instance)
        """
        from agile_bot.bots.base_bot.src.scanners.code_scanner import CodeScanner
        from typing import List, Dict, Any, Optional
        
        class SpyScanner(CodeScanner):
            def __init__(self):
                super().__init__()
                self.received_files = []
                self.called_is_test_file = False
            
            def scan(self, knowledge_graph: Dict[str, Any], rule_obj: Any = None,
                    test_files: Optional[List[Path]] = None,
                    code_files: Optional[List[Path]] = None) -> List[Dict[str, Any]]:
                """Record files received."""
                if test_files:
                    self.received_files.extend(test_files)
                if code_files:
                    self.received_files.extend(code_files)
                return []
            
            def _is_test_file(self, file_path: Path) -> bool:
                """Record that this method was called."""
                self.called_is_test_file = True
                return super()._is_test_file(file_path) if hasattr(super(), '_is_test_file') else False
        
        spy_instance = SpyScanner()
        return SpyScanner, spy_instance
    
    
    
    
    
    
        action.track_activity_on_start()
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:445): Function "then_stories_match" has high cognitive complexity (18) - should be under 15. Reduce nesting and extract complex logic.

    ```python
    
    
    def then_stories_match(expected: set, stories_to_check, present: bool = None):
        """
        Consolidated function for matching stories.
        Replaces: then_expected_story_names_contain_stories, then_expected_story_names_equal
        
        Args:
            expected: Expected set of story names
            stories_to_check: Stories to check (set or list)
            present: If True, checks stories are present; if False, checks stories are absent;
                     if None and stories_to_check is a set, checks equality
        
        Returns:
            None (asserts on failure)
        """
        if isinstance(stories_to_check, set) and present is None:
            # Equality check (then_expected_story_names_equal)
            assert expected == stories_to_check, f"Expected {stories_to_check}, got {expected}"
        else:
            # Containment check (then_expected_story_names_contain_stories)
            stories_list = list(stories_to_check) if not isinstance(stories_to_check, list) else stories_to_check
            should_be_present = present if present is not None else True
            for story in stories_list:
                if should_be_present:
                    assert story in expected, f"Expected '{story}' to be in expected set: {expected}"
                else:
                    assert story not in expected, f"Expected '{story}' NOT to be in expected set: {expected}"
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:534): Function "then_scanner_detects_violations_with_message" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def then_scanner_detects_violations_with_message(violations: list, scanner_class_path: str, message: str):
        """Then: Scanner detects violations with message.
        
        Consolidates: then_scanner_detects_violations_with_expected_message(violations, scanner_class_path, expected_violation_message)
        
        Args:
            violations: List of violation dictionaries
            scanner_class_path: Path to scanner class
            message: Expected violation message
        """
        assert len(violations) > 0, f"Scanner {scanner_class_path} should detect violations in bad example"
        
        # For SpecificationMatchScanner, it may detect multiple types of violations
        # Check if expected message is in any violation, or if violations are detected (for flexible matching)
        if 'specification_match' in scanner_class_path.lower() and message == 'scenario format':
            # SpecificationMatchScanner detects various violations - if it detects any, that's acceptable
            # The test file has violations that the scanner correctly identifies
            assert len(violations) > 0, f"Scanner {scanner_class_path} should detect violations"
            return  # Accept any violations for this scanner
        
        # Check that at least one violation contains expected message
        violation_messages = []
        for v in violations:
            assert 'violation_message' in v, f"Violation must contain 'violation_message' key: {v}"
            violation_messages.append(v['violation_message'])
        assert any(message.lower() in msg.lower() for msg in violation_messages), (
            f"Expected violation message '{message}' not found in violations: {violation_messages}"
        )
        
        # Validate violation structure
        for violation in violations:
            assert validate_violation_structure(violation, ['rule', 'violation_message', 'severity']), (
                f"Violation missing required fields: {violation}"
            )
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:574): Function "given_rule_file_created" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def given_rule_file_created(bot_directory: Path, behavior: str, rule_filename: str, rule_content: dict = None, **params):
        """
        Consolidated function for creating rule files.
        Replaces: given_behavior_rule_file_created, given_scenarios_rule_created,
        given_test_scope_verification_rule_created, given_validation_rule_for_verb_noun_format,
        given_validation_rules_created
        
        Args:
            bot_directory: Bot directory path
            behavior: Behavior name (required for behavior rules)
            rule_filename: Name of the rule file
            rule_content: Content of the rule file (dict)
            **params: Additional parameters:
                - rule_type: Type of rule ('behavior', 'scenarios', 'test_scope_verification',
                              'validation', 'verb_noun_format')
                - rules_dir_name: Directory name ('3_rules' or 'rules', default: '3_rules')
        
        Returns:
            Path to created rule file
        """
        rule_type = params.get('rule_type', 'behavior')
        rules_dir_name = params.get('rules_dir_name', '3_rules')
        
        if rule_type == 'behavior':
            if not behavior:
                raise ValueError("behavior parameter required for behavior rule")
            if rule_content is None:
                raise ValueError("rule_content parameter required")
            rules_dir = bot_directory / 'behaviors' / behavior / rules_dir_name
            rules_dir.mkdir(parents=True, exist_ok=True)
            rule_file = rules_dir / rule_filename
            rule_file.write_text(json.dumps(rule_content, indent=2), encoding='utf-8')
            return rule_file
        
        elif rule_type == 'scenarios':
            behavior_name = behavior or 'scenarios'
            rules_dir = bot_directory / 'behaviors' / behavior_name / '3_rules'
            rules_dir.mkdir(parents=True, exist_ok=True)
            rule_file = rules_dir / 'test_scenarios_rule.json'
            default_content = {
                "description": "Stories must have scenarios",
                "scanner": "agile_bot.bots.base_bot.src.actions.validate.scanners.scenarios_on_story_docs_scanner.ScenariosOnStoryDocsScanner"
            }
            rule_file.write_text(json.dumps(default_content, indent=2), encoding='utf-8')
            return rule_file
        
        elif rule_type == 'test_scope_verification':
            rule_content = {
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1051): Function "given_test_file_for_scanner_type" is 33 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        return None
    
    def given_test_file_for_scanner_type(workspace_directory: Path, scanner_class_path: str, behavior: str):
        """Given: Test file for scanner type."""
        test_file = workspace_directory / 'test_code.py'
        test_file.parent.mkdir(parents=True, exist_ok=True)
        bad_example = None
        
        # For test scanners, create a test file with violations
        if 'tests' in behavior:
            test_file = workspace_directory / 'test_place_order.py'
            test_file.parent.mkdir(parents=True, exist_ok=True)
            bad_example = _create_test_files_for_test_scanners(test_file, scanner_class_path)
        
        # For code scanners, create a test Python file with violations
        if bad_example is None and 'code' in behavior:
            # Use a filename that doesn't start with 'test_' to avoid being skipped by scanners
            # that skip test files (e.g., IntentionRevealingNamesScanner)
            test_file = workspace_directory / 'code_sample.py'
            test_file.parent.mkdir(parents=True, exist_ok=True)
            # _create_code_file_for_scanner_type writes the file and returns dict with code_files
            bad_example = _create_code_file_for_scanner_type(test_file, scanner_class_path)
            # If no match found, create a default file with violations
            if bad_example is None:
                # Create a default code file with common violations
                default_content = '''class Order:
        def process(self):
            return self.customer.get_order().get_items().add(item)
        
        def another_method(self):
            obj = SomeClass()
            return obj.method1().method2().method3()
    
    '''
                given_file_created(workspace_directory, 'code_sample.py', default_content, file_type='text')
                bad_example = {'code_files': [str(test_file)]}
            # Extract test_file from bad_example if needed
            elif bad_example and 'code_files' in bad_example:
                test_file = Path(bad_example['code_files'][0])
        
        return test_file, bad_example
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1096): Function "when_action_executes_and_returns_result" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def when_action_executes_and_returns_result(action: ValidateRulesAction, parameters: dict = None, context: 'ValidateActionContext' = None):
        """When: Action executes and returns result with typed context."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
        
        # Convert legacy dict parameters to typed context if needed
        if context is not None:
            return action.do_execute(context)
        
        if parameters is None:
            return action.do_execute(ValidateActionContext())
        
        # Convert dict to typed context
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type = ScopeType(scope_dict.get('type', 'all'))
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
                    exclude=scope_dict.get('exclude', []),
                    skiprule=scope_dict.get('skiprule', [])
                )
        
        typed_context = ValidateActionContext(
            scope=scope,
            background=parameters.get('background'),
            skip_cross_file=parameters.get('skip_cross_file', False),
            force_full=parameters.get('force_full', False)
        )
        return action.do_execute(typed_context)
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1255): Function "when_execute_scanner_based_on_type" is 32 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def when_execute_scanner_based_on_type(scanner_instance, bad_example: dict, rule_obj):
        """When: Execute scanner based on type.
        
        NEW DOMAIN MODEL: Use rule.scan() instead of calling scanner directly.
        """
        # Extract knowledge graph and files from bad_example
        kg = _extract_knowledge_graph_from_bad_example(bad_example)
        test_files = _extract_test_files_from_bad_example(bad_example)
        code_files = []
        if bad_example and 'code_files' in bad_example:
            code_files = [Path(cf) for cf in bad_example['code_files']]
        
        # Use rule.scan() which handles scanner instantiation and calling
        files_dict = {}
        if test_files:
            files_dict['test'] = [Path(tf) for tf in test_files]
        if code_files:
            files_dict['src'] = code_files
        
        # Call rule.scan() which returns scanner_results dict
        scanner_results = rule_obj.scan(kg, files=files_dict if files_dict else None)
        
        # Extract violations from scanner_results
        # rule.scan() returns a dict with scanner_results structure:
        # - For single-pass scanners: {'violations': [...]}
        # - For two-pass scanners: {'file_by_file': {'violations': [...]}, 'cross_file': {'violations': [...]}}
        violations = []
        if 'violations' in scanner_results:
            violations = scanner_results['violations']
        elif 'file_by_file' in scanner_results:
            violations = scanner_results.get('file_by_file', {}).get('violations', [])
            violations.extend(scanner_results.get('cross_file', {}).get('violations', []))
        
        # Also check rule's internal violation storage (rule.scan() stores violations internally)
        # Use the properties to access violations
        if not violations:
            violations = rule_obj.file_by_file_violations or []
            if rule_obj.cross_file_violations:
                violations.extend(rule_obj.cross_file_violations)
        
        return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1321): Function "given_bot_setup" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def given_bot_setup(bot_directory: Path, workspace_directory: Path, rules: dict = None, knowledge_graph: dict = None, **params):
        """
        Consolidated function for bot setup with rules and/or knowledge graph.
        Replaces: given_test_bot_setup_with_rules, given_knowledge_graph_and_test_bot_setup
        
        Args:
            bot_directory: Bot directory path
            workspace_directory: Workspace directory path
            rules: Dict with 'repo_root', 'rule_file_paths', 'rule_file_content' (for test_bot_setup_with_rules)
                   OR dict with 'repo_root', 'rule_file_path', 'rule_file_content' (for knowledge_graph_and_test_bot_setup)
            knowledge_graph: Knowledge graph dict (optional, for knowledge_graph_and_test_bot_setup)
            **params: Additional parameters (repo_root, etc.)
        
        Returns:
            test_bot_dir Path (if rules only) or (kg_file, test_bot_dir) tuple (if knowledge_graph provided)
        """
        repo_root = params.get('repo_root') or (rules.get('repo_root') if rules else None)
        if not repo_root:
            raise ValueError("repo_root parameter required (via rules dict or params)")
        
        bootstrap_env(bot_directory, workspace_directory)
        
        if knowledge_graph is not None:
            # Knowledge graph and test bot setup
            rule_file_path = rules.get('rule_file_path') if rules else params.get('rule_file_path')
            rule_file_content = rules.get('rule_file_content') if rules else params.get('rule_file_content')
            if rule_file_path and rule_file_content:
                setup_test_rules(repo_root, [rule_file_path], [rule_file_content])
            test_bot_dir = given_test_bot_directory_created(repo_root)
            # Create story graph in the workspace directory
            test_workspace_directory = test_bot_dir.parent / 'workspace'
            kg_file = given_file_created(test_workspace_directory / 'docs' / 'stories', 'story-graph.json', knowledge_graph)
            return kg_file, test_bot_dir
        else:
            # Test bot setup with rules only
            rule_file_paths = rules.get('rule_file_paths') if rules else params.get('rule_file_paths', [])
            rule_file_content = rules.get('rule_file_content') if rules else params.get('rule_file_content', [])
            test_bot_dir = given_test_bot_directory_created(repo_root)
            if rule_file_paths and rule_file_content:
                setup_test_rules(repo_root, rule_file_paths, rule_file_content)
            return test_bot_dir
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1414): Function "given_setup" is 112 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for VALIDATE setup.
        Replaces: given_validation_setup, given_story_graph_and_test_file_with_violations_setup,
        given_test_file_and_naming_rule_setup, given_story_graph_test_file_and_rules_setup,
        given_test_file_and_naming_rule_with_rule_id_setup, given_comprehensive_story_graph_setup_for_scope_test,
        given_test_file_scope_verification_setup, given_test_file_scope_setup_with_rule,
        given_multiple_test_files_scope_setup_with_rule
        
        Args:
            setup_type: Type of setup ('validation', 'story_graph_and_test_file_with_violations',
                        'test_file_and_naming_rule', 'story_graph_test_file_and_rules',
                        'test_file_and_naming_rule_with_rule_id', 'comprehensive_story_graph_for_scope',
                        'test_file_scope_verification', 'test_file_scope_with_rule',
                        'multiple_test_files_scope_with_rule')
            bot_directory: Bot directory path
            **setup_params: Additional parameters (workspace_directory, behavior, violations, rule_type,
                          create_method, etc.)
        
        Returns:
            Varies by setup_type:
            - 'validation': None (just sets up environment)
            - 'story_graph_and_test_file_with_violations': test_file Path
            - 'test_file_and_naming_rule': test_file Path
            - 'story_graph_test_file_and_rules': test_file Path
            - 'test_file_and_naming_rule_with_rule_id': test_file Path
            - 'comprehensive_story_graph_for_scope': (story_graph, story_graph_path)
            - 'test_file_scope_verification': (story_graph, story_graph_path)
            - 'test_file_scope_with_rule': (story_graph, story_graph_path, test_file)
            - 'multiple_test_files_scope_with_rule': (story_graph, story_graph_path, test_file1, test_file2)
        """
        workspace_directory = setup_params.get('workspace_directory')
        behavior = setup_params.get('behavior', 'tests')
        violations = setup_params.get('violations', False)
        rule_type = setup_params.get('rule_type')
        create_method = setup_params.get('create_method')
        
        if setup_type == 'validation':
            # General validation setup - just bootstrap environment
            if workspace_directory:
                bootstrap_env(bot_directory, workspace_directory)
            return None
        
        elif setup_type == 'story_graph_and_test_file_with_violations':
            verb_noun_rule_content = given_rule_content_dict('verb_noun')
            given_story_graph_with_content(workspace_directory, {
                'epics': [{'name': 'Bad Epic Name'}]  # Violation: noun-only format
            })
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1719): Function "then_content_to_validate_has_workspace_location" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        return validation_rules
    
    def then_content_to_validate_has_workspace_location(instructions: dict, workspace_directory: Path):
        """Then: Content to validate has workspace location."""
        assert 'content_to_validate' in instructions, (
            f"Expected 'content_to_validate' in instructions, but got keys: {instructions.keys()}"
        )
        content_info = instructions['content_to_validate']
        # content_to_validate can be None if not set
        if content_info is None:
            # If None, that's acceptable - some tests don't require content_to_validate
            return None
        # Explicitly check for project_location (implementation always uses project_location)
        assert 'project_location' in content_info, (
            "content_to_validate should contain project_location"
        )
        project_location_value = content_info['project_location']
        assert str(workspace_directory) in str(project_location_value), (
            f"project_location should point to the workspace directory, got: {project_location_value}"
        )
        assert 'rendered_outputs' in content_info, (
            "content_to_validate should contain rendered_outputs list"
        )
        return content_info
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1751): Function "then_report_path_is_valid" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        )
    
    def then_report_path_is_valid(content_info: dict, workspace_directory: Path):
        """Then: Report path is valid."""
        # content_info can be None - skip check if None
        if content_info is None:
            return
        assert 'report_path' in content_info, (
            "content_to_validate should contain report_path where validation report should be saved"
        )
        report_path = content_info['report_path']
        assert report_path.endswith('validation-report.md'), (
            f"report_path should point to validation-report.md, got: {report_path}"
        )
        assert str(workspace_directory) in report_path or 'docs' in report_path, (
            f"report_path should be in workspace directory, got: {report_path}"
        )
        report_path_obj = Path(report_path)
        expected_docs_dir = workspace_directory / 'docs' / 'stories'
        assert report_path_obj.parent == expected_docs_dir, (
            f"report_path parent should be docs/stories directory, got: {report_path_obj.parent}"
        )
        assert report_path_obj.name == 'validation-report.md', (
            f"report_path filename should be validation-report.md, got: {report_path_obj.name}"
        )
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1862): Function "when_extract_violations_from_validation_rules" is 27 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def when_extract_violations_from_validation_rules(validation_rules: list):
        """When: Extract violations from validation rules."""
        all_violations = []
        for rule_data in validation_rules:
            assert 'scanner_results' in rule_data, f"Rule data must contain 'scanner_results' key: {rule_data}"
            scanner_results = rule_data['scanner_results']
            # Handle both old format (direct 'violations' key) and new format ('file_by_file'/'cross_file')
            if 'violations' in scanner_results:
                violations = scanner_results['violations']
                if violations:  # Only extend if violations list is not empty
                    all_violations.extend(violations)
            elif 'file_by_file' in scanner_results:
                # New format: violations are nested under 'file_by_file' and 'cross_file'
                file_by_file = scanner_results.get('file_by_file', {})
                cross_file = scanner_results.get('cross_file', {})
                if 'violations' in file_by_file:
                    violations = file_by_file['violations']
                    if violations:  # Only extend if violations list is not empty
                        all_violations.extend(violations)
                if 'violations' in cross_file:
                    violations = cross_file['violations']
                    if violations:  # Only extend if violations list is not empty
                        all_violations.extend(violations)
            elif scanner_results:  # If scanner_results exists but doesn't match expected format, log it
                # Empty dict is OK (no scanner or no violations), but if it has content, it's unexpected
                if scanner_results != {}:
                    raise AssertionError(f"Scanner results must contain 'violations' key or 'file_by_file'/'cross_file' keys: {scanner_results}")
        return all_violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1907): Function "when_action_executes_with_scope_parameters" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def when_action_executes_with_scope_parameters(action: ValidateRulesAction, parameters: dict):
        """When: Action executes with scope parameters."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
        
        # Convert dict to typed context
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type = ScopeType(scope_dict.get('type', 'all'))
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
                    exclude=scope_dict.get('exclude', []),
                    skiprule=scope_dict.get('skiprule', [])
                )
        # Handle 'test' key from when_parameters_created (for test files)
        elif 'test' in parameters:
            test_files = parameters['test']
            if isinstance(test_files, str):
                test_files = [test_files]
            scope = Scope(type=ScopeType.FILES, value=test_files)
        # Handle 'src' key from when_parameters_created (for source files)
        elif 'src' in parameters:
            src_files = parameters['src']
            if isinstance(src_files, str):
                src_files = [src_files]
            scope = Scope(type=ScopeType.FILES, value=src_files)
        
        typed_context = ValidateActionContext(
            scope=scope,
            background=parameters.get('background'),
            skip_cross_file=parameters.get('skip_cross_file', False),
            force_full=parameters.get('force_full', False)
        )
        return action.do_execute(typed_context)
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1983): Function "when_validate_code_files_action_created" is 27 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def when_validate_code_files_action_created(bot_name: str, behavior: str, bot_directory: Path, workspace_directory: Path = None):
        """When: ValidateRulesAction created (ValidateCodeFilesAction was removed, use ValidateRulesAction instead)."""
        from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
        from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
        from agile_bot.bots.base_bot.src.bot.bot import Behavior
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json, bootstrap_env
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        
        # Use provided workspace_directory or create default
        if workspace_directory is None:
            workspace_directory = bot_directory.parent / 'workspace'
        workspace_directory.mkdir(parents=True, exist_ok=True)
        bootstrap_env(bot_directory, workspace_directory)
        
        # Ensure behavior.json exists
        create_actions_workflow_json(bot_directory, behavior)
        
        # Create minimal guardrails files
        create_minimal_guardrails_files(bot_directory, behavior, bot_name)
        
        # Create minimal story graph (required for validation)
        docs_stories_dir = workspace_directory / 'docs' / 'stories'
        docs_stories_dir.mkdir(parents=True, exist_ok=True)
        story_graph_path = docs_stories_dir / 'story-graph.json'
        minimal_story_graph = {"epics": []}
        story_graph_path.write_text(json.dumps(minimal_story_graph, indent=2), encoding='utf-8')
        
        # Create Behavior object - pass workspace_path so reports go to correct location
        bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
        behavior_obj = Behavior(name=behavior, bot_paths=bot_paths)
        
        # Create action - Use ValidateRulesAction (ValidateCodeFilesAction was removed)
        # Action signature: behavior, action_config (action_name is derived from class name)
        return ValidateRulesAction(
            behavior=behavior_obj,
            action_config=None
        )
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2022): Function "when_validate_code_files_action_executes" is 29 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def when_validate_code_files_action_executes(action, parameters: dict):
        """When: ValidateRulesAction executes with parameters (ValidateCodeFilesAction was removed)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
        
        # Convert dict to typed context
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type = ScopeType(scope_dict.get('type', 'all'))
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
                    exclude=scope_dict.get('exclude', []),
                    skiprule=scope_dict.get('skiprule', [])
                )
        # Handle 'src' key from when_parameters_created (for source files)
        elif 'src' in parameters:
            src_files = parameters['src']
            if isinstance(src_files, str):
                src_files = [src_files]
            scope = Scope(type=ScopeType.FILES, value=src_files)
        # Handle 'test' key from when_parameters_created (for test files)
        elif 'test' in parameters:
            test_files = parameters['test']
            if isinstance(test_files, str):
                test_files = [test_files]
            scope = Scope(type=ScopeType.FILES, value=test_files)
        
        # For tests, default to synchronous (background=False) so reports are written before assertions
        typed_context = ValidateActionContext(
            scope=scope,
            background=parameters.get('background', False),  # Default to synchronous for tests
            skip_cross_file=parameters.get('skip_cross_file', False),
            force_full=parameters.get('force_full', False)
        )
        return action.do_execute(typed_context)
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5403): Function "test_formatted_rules_digest_returns_compact_format" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            assert len(rules) >= 1
            
        def test_formatted_rules_digest_returns_compact_format(self, bot_directory, workspace_directory):
            """
            SCENARIO: formatted_rules_digest returns compact format
            GIVEN: behavior has 2 rules defined
            WHEN: formatted_rules_digest is called
            THEN: returns name + description format (not full examples)
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
            from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
            from agile_bot.bots.base_bot.src.bot.behavior import Behavior
            from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
            
            # Given: Setup behavior with multiple rules
            bootstrap_env(bot_directory, workspace_directory)
            create_actions_workflow_json(bot_directory, 'code')
            rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
            rules_dir.mkdir(parents=True, exist_ok=True)
            (rules_dir / 'rule_one.json').write_text(json.dumps({
                'description': 'First rule description',
                'examples': [{'do': {'description': 'Do this', 'content': ['example code']}}]
            }), encoding='utf-8')
            (rules_dir / 'rule_two.json').write_text(json.dumps({
                'description': 'Second rule description',
                'examples': []
            }), encoding='utf-8')
            
            bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
            behavior = Behavior('code', bot_paths)
            rules = Rules(behavior=behavior, bot_paths=bot_paths)
            
            # When: Get digest
            digest = rules.formatted_rules_digest()
            
            # Then: Digest is compact (contains descriptions but not examples)
            assert 'Rules to follow' in digest
            assert 'First rule description' in digest
            assert 'Second rule description' in digest
            # Should NOT contain example content
            assert 'example code' not in digest
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5443): Function "test_rules_action_includes_message_in_context" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            assert 'example code' not in digest
    
        def test_rules_action_includes_message_in_context(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules action includes user message in context
            GIVEN: behavior is 'code' and message is 'help me refactor'
            WHEN: rules action executes with message
            THEN: instructions include user message
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
            from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
            from agile_bot.bots.base_bot.src.bot.behavior import Behavior
            from agile_bot.bots.base_bot.src.actions.rules.rules_action import RulesAction
            from agile_bot.bots.base_bot.src.actions.action_context import RulesActionContext
            
            # Given: Setup behavior
            bootstrap_env(bot_directory, workspace_directory)
            create_actions_workflow_json(bot_directory, 'code')
            rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
            rules_dir.mkdir(parents=True, exist_ok=True)
            (rules_dir / 'test_rule.json').write_text(json.dumps({
                'description': 'Test rule',
                'examples': []
            }), encoding='utf-8')
            
            bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
            behavior = Behavior('code', bot_paths)
            action = RulesAction(behavior=behavior)
            
            # When: Execute with message
            context = RulesActionContext(message='help me refactor this function')
            result = action.do_execute(context)
            
            # Then: Message is in instructions
            instructions = result['instructions']
            base_instructions = instructions.get('base_instructions', [])
            instructions_text = '\n'.join(str(i) for i in base_instructions)
            assert 'help me refactor' in instructions_text
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5480): Function "test_rules_action_outputs_to_ai_context_only" is 26 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            assert 'help me refactor' in instructions_text
    
        def test_rules_action_outputs_to_ai_context_only(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules action outputs digest to AI context only (not display)
            GIVEN: behavior has rules defined
            WHEN: rules action executes
            THEN: digest appears in base_instructions but NOT display_content
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
            from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
            from agile_bot.bots.base_bot.src.bot.behavior import Behavior
            from agile_bot.bots.base_bot.src.actions.rules.rules_action import RulesAction
            from agile_bot.bots.base_bot.src.actions.action_context import RulesActionContext
            
            # Given: Setup behavior with rules
            bootstrap_env(bot_directory, workspace_directory)
            create_actions_workflow_json(bot_directory, 'code')
            rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
            rules_dir.mkdir(parents=True, exist_ok=True)
            (rules_dir / 'my_rule.json').write_text(json.dumps({
                'description': 'My unique rule description',
                'examples': []
            }), encoding='utf-8')
            
            bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
            behavior = Behavior('code', bot_paths)
            action = RulesAction(behavior=behavior)
            
            # When: Execute rules action
            context = RulesActionContext()
            result = action.do_execute(context)
            
            # Then: Digest in AI context only
            instructions = result['instructions']
            display_content = instructions.get('display_content', [])
            base_instructions = instructions.get('base_instructions', [])
            
            display_text = '\n'.join(display_content)
            instructions_text = '\n'.join(str(i) for i in base_instructions)
            
            # Rules go to AI context ONLY, not display
            assert 'My unique rule description' in instructions_text
            assert 'My unique rule description' not in display_text
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:276): Function "given_setup" is 34 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            verify_workflow_saves_completed_action(bot_directory, workspace_directory, 'build')
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for BUILD KNOWLEDGE setup.
        Replaces: given_knowledge_graph_setup, given_knowledge_graph_setup_complete,
        given_knowledge_graph_config_and_template_created, given_knowledge_graph_directory_structure_created,
        given_knowledge_graph_directory_for_prioritization, given_environment_and_knowledge_graph_setup
        
        Args:
            setup_type: Type of setup ('knowledge_graph', 'knowledge_graph_complete', 'config_and_template',
                        'directory_structure', 'directory_for_prioritization', 'environment_and_kg')
            bot_directory: Bot directory path
            **setup_params: Additional parameters (behavior, template_name, workspace_directory, kg_dir)
        
        Returns:
            kg_dir Path or tuple depending on setup_type
        """
        behavior = setup_params.get('behavior', 'build')
        workspace_directory = setup_params.get('workspace_directory')
        template_name = setup_params.get('template_name', 'story-graph-outline.json')
        kg_dir = setup_params.get('kg_dir')
        
        # Create kg_dir if not provided
        if kg_dir is None:
            behavior_dir = bot_directory / 'behaviors' / behavior
            kg_dir = behavior_dir / 'content' / 'knowledge_graph'
            kg_dir.mkdir(parents=True, exist_ok=True)
        
        if setup_type == 'knowledge_graph' or setup_type == 'directory_structure':
            return kg_dir
        elif setup_type == 'knowledge_graph_complete':
            given_file_created(kg_dir, 'build_story_graph_outline.json', {'template': template_name})
            given_file_created(kg_dir, template_name, {'template': 'knowledge_graph', 'structure': {}})
            return kg_dir
        elif setup_type == 'config_and_template':
            config_file = kg_dir / 'build_story_graph_outline.json'
            config_file.write_text(
                json.dumps({
                    'name': 'build_story_graph_outline',
                    'path': 'docs/stories/',
                    'template': 'story-graph-outline.json',
                    'output': 'story-graph.json'
                }),
                encoding='utf-8'
            )
            template_file = kg_dir / 'story-graph-outline.json'
            template_file.write_text(
                json.dumps({
                    '_explanation': {},
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:448): Function "then_location_matches" is 27 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    
    
    def then_location_matches(item, type=None, field=None):
        """
        Consolidated function for checking map location correctness.
        Replaces: then_epic_map_location_correct, then_sub_epic_map_location_correct,
        then_story_map_location_correct, then_scenario_map_location_correct,
        then_scenario_outline_map_location_correct
        
        Args:
            item: Epic, SubEpic, Story, Scenario, or ScenarioOutline instance
            type: Type hint ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline') - auto-detected if None
            field: Optional field name to check (e.g., 'sequential_order', 'sizing')
        """
        # Auto-detect type if not provided
        if type is None:
            from agile_bot.bots.base_bot.src.scanners.story_map import Epic, SubEpic, Story, Scenario, ScenarioOutline
            if isinstance(item, Epic):
                type = 'epic'
            elif isinstance(item, SubEpic):
                type = 'sub_epic'
            elif isinstance(item, Story):
                type = 'story'
            elif isinstance(item, Scenario):
                type = 'scenario'
            elif isinstance(item, ScenarioOutline):
                type = 'scenario_outline'
        
        # Expected locations based on type
        expected_locations = {
            'epic': {
                None: "epics[0].name",
                'sequential_order': "epics[0].sequential_order"
            },
            'sub_epic': {
                None: "epics[0].sub_epics[0].name"
            },
            'story': {
                None: "epics[0].sub_epics[0].story_groups[0].stories[0].name",
                'sizing': "epics[0].sub_epics[0].story_groups[0].stories[0].sizing"
            },
            'scenario': {
                None: "epics[0].sub_epics[0].story_groups[0].stories[0].scenarios[0].name"
            },
            'scenario_outline': {
                None: "epics[0].sub_epics[0].story_groups[0].stories[0].scenario_outlines[0].name"
            }
        }
        
        # Check default location (name)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1424): Function "then_story_graph_contains_story" has high cognitive complexity (16) - should be under 15. Reduce nesting and extract complex logic.

    ```python
    
    
    def then_story_graph_contains_story(filtered_graph, story_name):
        """Then: Story graph contains story."""
        story_names = []
        for epic in filtered_graph.get('epics', []):
            for sub_epic in epic.get('sub_epics', []):
                for story_group in sub_epic.get('story_groups', []):
                    for story in story_group.get('stories', []):
                        if isinstance(story, dict):
                            story_names.append(story.get('name'))
                        else:
                            story_names.append(story)
        assert story_name in story_names
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:36): Function "when_action_executes_with_parameters" is 38 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
    # ============================================================================
    
    def when_action_executes_with_parameters(action, parameters: dict):
        """When: Action executes with parameters (converts dict to typed context).
        
        Determines the appropriate context type based on the action class.
        """
        from agile_bot.bots.base_bot.src.actions.action_context import StrategyActionContext, ValidateActionContext, Scope, ScopeType
        from agile_bot.bots.base_bot.src.actions.strategy.strategy_action import StrategyAction
        from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
        
        if isinstance(action, StrategyAction):
            # Strategy action context
            context = StrategyActionContext(
                decisions_made=parameters.get('decisions_made'),
                assumptions_made=parameters.get('assumptions_made')
            )
        elif isinstance(action, ValidateRulesAction):
            # Validate action context - convert test_files to scope
            scope = None
            if 'test_files' in parameters:
                test_files = parameters.get('test_files')
                if isinstance(test_files, (str, type(None).__class__)):
                    file_paths = [str(test_files)] if test_files else []
                else:
                    file_paths = [str(f) for f in test_files] if test_files else []
                scope = Scope(type=ScopeType.FILES, value=file_paths)
            elif 'scope' in parameters:
                scope_dict = parameters.get('scope', {})
                if isinstance(scope_dict, dict):
                    scope = Scope(
                        type=ScopeType(scope_dict.get('type', 'all')),
                        value=scope_dict.get('value', []),
                        exclude=scope_dict.get('exclude', []),
                        skiprule=scope_dict.get('skiprule', [])
                    )
            context = ValidateActionContext(
                scope=scope,
                background=parameters.get('background', False),
                skip_cross_file=parameters.get('skip_cross_file', False),
                force_full=parameters.get('force_full', False)
            )
        else:
            # Fallback - use the action's default context class
            context = action.context_class()
        
        return action.do_execute(context)
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:217): Function "then_strategy_json_contains_behavior_data" has high cyclomatic complexity (11) - should be under 10. Extract decision logic to helper functions.

    ```python
        assert strategy_data['shape']['strategy_criteria']['decisions_made']['drill_down'] == expected_drill_down
    
    def then_strategy_json_contains_behavior_data(strategy_file: Path, behavior: str, expected_decisions: dict = None, expected_assumptions: list = None):
        """Then step: strategy.json contains behavior data."""
        strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
        assert behavior in strategy_data
        if expected_decisions:
            # New structure: strategy_criteria has 'criteria' and 'decisions_made'
            assert 'strategy_criteria' in strategy_data[behavior]
            assert 'decisions_made' in strategy_data[behavior]['strategy_criteria']
            for key, value in expected_decisions.items():
                assert strategy_data[behavior]['strategy_criteria']['decisions_made'][key] == value
        if expected_assumptions:
            # New structure: assumptions has 'typical_assumptions' and 'assumptions_made'
            assert 'assumptions' in strategy_data[behavior]
            assert 'assumptions_made' in strategy_data[behavior]['assumptions']
            assert strategy_data[behavior]['assumptions']['assumptions_made'] == expected_assumptions
        return strategy_data
    
    ```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 8 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:574): Function "given_rule_file_created" is 72 lines - consider improving vertical density by declaring variables near usage

    ```python
    
    
    def given_rule_file_created(bot_directory: Path, behavior: str, rule_filename: str, rule_content: dict = None, **params):
        """
        Consolidated function for creating rule files.
        Replaces: given_behavior_rule_file_created, given_scenarios_rule_created,
        given_test_scope_verification_rule_created, given_validation_rule_for_verb_noun_format,
        given_validation_rules_created
        
        Args:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:854): Function "_create_code_file_for_scanner_type" is 196 lines - consider improving vertical density by declaring variables near usage

    ```python
        return None
    
    def _create_code_file_for_scanner_type(test_file: Path, scanner_class_path: str):
        """Helper: Create code file for specific scanner type."""
        scanner_lower = scanner_class_path.lower()
        scanner_file_contents = {
            'useless_comments': '''def get_name(self):
        """Get the name.
        
        
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1414): Function "given_setup" is 179 lines - consider improving vertical density by declaring variables near usage

    ```python
    
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for VALIDATE setup.
        Replaces: given_validation_setup, given_story_graph_and_test_file_with_violations_setup,
        given_test_file_and_naming_rule_setup, given_story_graph_test_file_and_rules_setup,
        given_test_file_and_naming_rule_with_rule_id_setup, given_comprehensive_story_graph_setup_for_scope_test,
        given_test_file_scope_verification_setup, given_test_file_scope_setup_with_rule,
        given_multiple_test_files_scope_setup_with_rule
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2721): Function "create_comprehensive_story_graph" is 272 lines - consider improving vertical density by declaring variables near usage

    ```python
    
        @staticmethod
        def create_comprehensive_story_graph() -> Dict[str, Any]:
            """Create a comprehensive story graph with multiple epics, sub-epics, stories, and increments."""
            return {
                "epics": [
                    {
                        "name": "Manage Mobs",
                        "sequential_order": 1,
                        "sub_epics": [
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:151): Function "simple_story_graph" is 71 lines - consider improving vertical density by declaring variables near usage

    ```python
    
    @pytest.fixture
    def simple_story_graph():
        return {
            "epics": [
                {
                    "name": "Build Knowledge",
                    "sequential_order": 1,
                    "sub_epics": [
                        {
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:276): Function "given_setup" is 61 lines - consider improving vertical density by declaring variables near usage

    ```python
            verify_workflow_saves_completed_action(bot_directory, workspace_directory, 'build')
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for BUILD KNOWLEDGE setup.
        Replaces: given_knowledge_graph_setup, given_knowledge_graph_setup_complete,
        given_knowledge_graph_config_and_template_created, given_knowledge_graph_directory_structure_created,
        given_knowledge_graph_directory_for_prioritization, given_environment_and_knowledge_graph_setup
        
        Args:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:448): Function "then_location_matches" is 60 lines - consider improving vertical density by declaring variables near usage

    ```python
    
    
    def then_location_matches(item, type=None, field=None):
        """
        Consolidated function for checking map location correctness.
        Replaces: then_epic_map_location_correct, then_sub_epic_map_location_correct,
        then_story_map_location_correct, then_scenario_map_location_correct,
        then_scenario_outline_map_location_correct
        
        Args:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1332): Function "given_story_graph_with_epics_and_increments" is 74 lines - consider improving vertical density by declaring variables near usage

    ```python
    # ============================================================================
    
    def given_story_graph_with_epics_and_increments():
        """Given: Story graph with epics and increments."""
        return {
            'epics': [
                {
                    'name': 'Epic A',
                    'sub_epics': [
                        {
        # ... (truncated)
    ```

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2244): Except block only contains pass at line 2244 - exceptions must be logged or rethrown, never swallowed

    ```python
            try:
                file_path.unlink()
            except Exception:
                pass  # Ignore cleanup errors
    
    ```

#### <span id="place-imports-at-top-violations">Place Imports At Top: 23 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:49): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        given_scanner_spy
    )
    from agile_bot.bots.base_bot.test.test_perform_behavior_action import given_action_config, given_action_config_with_order, then_result_matches
    from agile_bot.bots.base_bot.test.test_build_knowledge import (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:50): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    )
    from agile_bot.bots.base_bot.test.test_perform_behavior_action import given_action_config, given_action_config_with_order, then_result_matches
    from agile_bot.bots.base_bot.test.test_build_knowledge import (
        given_test_bot_directory_created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:53): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        given_test_bot_directory_created
    )
    from agile_bot.bots.base_bot.test.test_decide_strategy_criteria_action import (
        when_action_executes_with_parameters
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:56): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        when_action_executes_with_parameters
    )
    from agile_bot.bots.base_bot.test.test_invoke_mcp import (
        given_base_actions_setup
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:59): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        given_base_actions_setup
    )
    from agile_bot.bots.base_bot.src.bot.bot import Behavior
    from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:60): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    )
    from agile_bot.bots.base_bot.src.bot.bot import Behavior
    from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:61): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    from agile_bot.bots.base_bot.src.bot.bot import Behavior
    from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    from agile_bot.bots.base_bot.src.scanners.code_scanner import CodeScanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:62): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    from agile_bot.bots.base_bot.src.scanners.code_scanner import CodeScanner
    from agile_bot.bots.base_bot.src.scanners.test_scanner import TestScanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:63): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    from agile_bot.bots.base_bot.src.scanners.code_scanner import CodeScanner
    from agile_bot.bots.base_bot.src.scanners.test_scanner import TestScanner
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2116): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    
    
    from agile_bot.bots.base_bot.test.test_helpers import create_validation_rules
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3833): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    # ============================================================================
    
    from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
    from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3834): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    
    from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
    from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
    from agile_bot.bots.base_bot.src.scanners.scanner_loader import ScannerLoader
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3835): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    from agile_bot.bots.base_bot.src.actions.rules.rules import Rules
    from agile_bot.bots.base_bot.src.actions.validate.validation_scope import ValidationScope
    from agile_bot.bots.base_bot.src.scanners.scanner_loader import ScannerLoader
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:26): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        create_base_actions_structure
    )
    from agile_bot.bots.base_bot.test.test_helpers import (
        bootstrap_env, create_behavior_action_instructions,
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:30): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        then_route_matches_expected, then_cli_result_matches_expected
    )
    from agile_bot.bots.base_bot.test.test_helpers import (
        create_base_action_instructions
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:33): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        create_base_action_instructions
    )
    from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    from agile_bot.bots.base_bot.src.cli.cli_parameter_parser import CliParameterParser
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:34): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    )
    from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    from agile_bot.bots.base_bot.src.cli.cli_parameter_parser import CliParameterParser
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:735): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    # ============================================================================
    
    from unittest.mock import Mock
    from agile_bot.bots.base_bot.src.ext.trigger_words import TriggerWords
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:736): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    
    from unittest.mock import Mock
    from agile_bot.bots.base_bot.src.ext.trigger_words import TriggerWords
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior  # BehaviorConfig merged into Behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:737): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    from unittest.mock import Mock
    from agile_bot.bots.base_bot.src.ext.trigger_words import TriggerWords
    from agile_bot.bots.base_bot.src.bot.behavior import Behavior  # BehaviorConfig merged into Behavior
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:18): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        StoryMap, Epic, SubEpic, StoryGroup, Story, Scenario, ScenarioOutline
    )
    from agile_bot.bots.base_bot.test.test_helpers import (
        bootstrap_env,
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:46): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        when_action_executes
    )
    from agile_bot.bots.base_bot.test.test_execute_behavior_actions import (
        verify_action_tracks_start,
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:24): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
        when_action_injects
    )
    from agile_bot.bots.base_bot.test.test_execute_behavior_actions import (
        verify_action_tracks_start,
    ```

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 16 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:248): Line 248 uses numbered variable "s1" - use meaningful descriptive name

    ```python
            import re
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:897): Line 897 contains magic number - replace with named constant

    ```python
            'meaningful_context': '''def process():
        if status == 200:
            return data
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1704): Line 1704 contains magic number - replace with named constant

    ```python
        assert 'clarification.json' in instructions_text or 'clarification' in instructions_text.lower(), (
            f"base_instructions should contain the action instructions mentioning clarification.json. Got: {instructions_text[:500]}"
        )
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1785): Line 1785 contains magic number - replace with named constant

    ```python
               'save.*validation' in instructions_text, (
            f"base_instructions should include instruction to save/write validation report. Got: {instructions_text[:500]}"
        )
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4122): Line 4122 uses numbered variable "expected_name1" - use meaningful descriptive name

    ```python
    
    def then_rule_names_include(rule_names: list, expected_name1: str, expected_name2: str):
        """Then: Rule names include expected names."""
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4122): Line 4122 uses numbered variable "expected_name2" - use meaningful descriptive name

    ```python
    
    def then_rule_names_include(rule_names: list, expected_name1: str, expected_name2: str):
        """Then: Rule names include expected names."""
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5062): Line 5062 uses numbered variable "old_report1" - use meaningful descriptive name

    ```python
    
    def then_old_reports_still_exist(old_report1, old_report2):
        assert old_report1.exists(), f"Old report {old_report1} should still exist"
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5062): Line 5062 uses numbered variable "old_report2" - use meaningful descriptive name

    ```python
    
    def then_old_reports_still_exist(old_report1, old_report2):
        assert old_report1.exists(), f"Old report {old_report1} should still exist"
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4947): Line 4947 uses numbered variable "unchanged_file1" - use meaningful descriptive name

    ```python
        
        unchanged_file1 = src_dir / 'unchanged1.py'
        unchanged_file1.write_text('def unchanged1(): pass')
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4953): Line 4953 uses numbered variable "unchanged_file2" - use meaningful descriptive name

    ```python
        
        unchanged_file2 = src_dir / 'unchanged2.py'
        unchanged_file2.write_text('def unchanged2(): pass')
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3785): Line 3785 uses numbered variable "source_file1" - use meaningful descriptive name

    ```python
            ], file_type='text')
            source_file1, source_file2 = source_files[0], source_files[1]
            given_environment_bootstrapped_with_story_graph(bot_directory, workspace_directory)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3785): Line 3785 uses numbered variable "source_file2" - use meaningful descriptive name

    ```python
            ], file_type='text')
            source_file1, source_file2 = source_files[0], source_files[1]
            given_environment_bootstrapped_with_story_graph(bot_directory, workspace_directory)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4862): Line 4862 uses numbered variable "unchanged_file1" - use meaningful descriptive name

    ```python
            
            changed_file, unchanged_file1, unchanged_file2 = given_changed_and_unchanged_files(workspace_directory)
            given_previous_validation_report_exists(workspace_directory, bot_name, unchanged_file1, unchanged_file2)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4862): Line 4862 uses numbered variable "unchanged_file2" - use meaningful descriptive name

    ```python
            
            changed_file, unchanged_file1, unchanged_file2 = given_changed_and_unchanged_files(workspace_directory)
            given_previous_validation_report_exists(workspace_directory, bot_name, unchanged_file1, unchanged_file2)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4892): Line 4892 uses numbered variable "old_report1" - use meaningful descriptive name

    ```python
            
            old_report1 = given_previous_timestamped_report_exists(workspace_directory, bot_name, '2025-01-01_10-00-00')
            old_report2 = given_previous_timestamped_report_exists(workspace_directory, bot_name, '2025-01-02_10-00-00')
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4893): Line 4893 uses numbered variable "old_report2" - use meaningful descriptive name

    ```python
            old_report1 = given_previous_timestamped_report_exists(workspace_directory, bot_name, '2025-01-01_10-00-00')
            old_report2 = given_previous_timestamped_report_exists(workspace_directory, bot_name, '2025-01-02_10-00-00')
            
    ```

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 4 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:77): Fallback/legacy support code found (comment at line 77, code at line 78) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:148): Fallback/legacy support code found (comment at line 148, code at line 149) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:191): Fallback/legacy support code found (comment at line 191, code at line 192) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:202): Fallback/legacy support code found (comment at line 202, code at line 203) - complete refactoring by removing old pattern support

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 14 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\type_hint_converter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/type_hint_converter.py:4): Function "to_cli_type" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
        
        @staticmethod
        def to_cli_type(field_type) -> str:
            type_str = str(field_type)
            if 'Dict' in type_str:
                return 'dict'
            elif 'List' in type_str:
                return 'list'
            elif 'bool' in type_str:
                return 'flag'
            elif 'Scope' in type_str:
                return 'dict'
            return 'str'
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:379): Function "_validate_rule_structure" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def _validate_rule_structure(rule):
        """Helper: Validate individual rule structure.
        
        Accepts Rule objects or dicts (for backward compatibility with validated rules).
        """
        from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
        
        # Handle Rule objects (new format)
        if isinstance(rule, Rule):
            assert hasattr(rule, 'rule_file'), f"Rule object must have 'rule_file' attribute"
            assert hasattr(rule, 'rule_content'), f"Rule object must have 'rule_content' attribute"
            rule_file = str(rule.rule_file)
            rule_content = rule.rule_content
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:574): Function "given_rule_file_created" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def given_rule_file_created(bot_directory: Path, behavior: str, rule_filename: str, rule_content: dict = None, **params):
        """
        Consolidated function for creating rule files.
        Replaces: given_behavior_rule_file_created, given_scenarios_rule_created,
        given_test_scope_verification_rule_created, given_validation_rule_for_verb_noun_format,
        given_validation_rules_created
        
        Args:
            bot_directory: Bot directory path
            behavior: Behavior name (required for behavior rules)
            rule_filename: Name of the rule file
            rule_content: Content of the rule file (dict)
            **params: Additional parameters:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1414): Function "given_setup" has nesting depth of 9 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for VALIDATE setup.
        Replaces: given_validation_setup, given_story_graph_and_test_file_with_violations_setup,
        given_test_file_and_naming_rule_setup, given_story_graph_test_file_and_rules_setup,
        given_test_file_and_naming_rule_with_rule_id_setup, given_comprehensive_story_graph_setup_for_scope_test,
        given_test_file_scope_verification_setup, given_test_file_scope_setup_with_rule,
        given_multiple_test_files_scope_setup_with_rule
        
        Args:
            setup_type: Type of setup ('validation', 'story_graph_and_test_file_with_violations',
                        'test_file_and_naming_rule', 'story_graph_test_file_and_rules',
                        'test_file_and_naming_rule_with_rule_id', 'comprehensive_story_graph_for_scope',
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1862): Function "when_extract_violations_from_validation_rules" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def when_extract_violations_from_validation_rules(validation_rules: list):
        """When: Extract violations from validation rules."""
        all_violations = []
        for rule_data in validation_rules:
            assert 'scanner_results' in rule_data, f"Rule data must contain 'scanner_results' key: {rule_data}"
            scanner_results = rule_data['scanner_results']
            # Handle both old format (direct 'violations' key) and new format ('file_by_file'/'cross_file')
            if 'violations' in scanner_results:
                violations = scanner_results['violations']
                if violations:  # Only extend if violations list is not empty
                    all_violations.extend(violations)
            elif 'file_by_file' in scanner_results:
                # New format: violations are nested under 'file_by_file' and 'cross_file'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1907): Function "when_action_executes_with_scope_parameters" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def when_action_executes_with_scope_parameters(action: ValidateRulesAction, parameters: dict):
        """When: Action executes with scope parameters."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
        
        # Convert dict to typed context
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type = ScopeType(scope_dict.get('type', 'all'))
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2022): Function "when_validate_code_files_action_executes" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def when_validate_code_files_action_executes(action, parameters: dict):
        """When: ValidateRulesAction executes with parameters (ValidateCodeFilesAction was removed)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
        
        # Convert dict to typed context
        scope = None
        if 'scope' in parameters and parameters['scope']:
            scope_dict = parameters['scope']
            if isinstance(scope_dict, dict):
                scope_type = ScopeType(scope_dict.get('type', 'all'))
                scope = Scope(
                    type=scope_type,
                    value=scope_dict.get('value', []),
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3020): Function "_handle_increment_priorities_scope" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
        
        @staticmethod
        def _handle_increment_priorities_scope(scope_config: Dict[str, Any], story_graph: Dict[str, Any], expected_names: Set[str]):
            """Helper: Handle increment_priorities scope configuration."""
            if 'increment_priorities' in scope_config:
                priorities = scope_config['increment_priorities']
                if not isinstance(priorities, list):
                    priorities = [priorities]
                for priority in priorities:
                    for increment in story_graph.get('increments', []):
                        inc_priority = increment.get('priority', 999)
                        if isinstance(inc_priority, str):
                            priority_map = {'NOW': 1, 'LATER': 2, 'SOON': 1, 'NEXT': 2}
                            inc_priority = priority_map.get(inc_priority.upper(), 999)
                        if inc_priority == priority:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3036): Function "_handle_epic_names_scope" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
        
        @staticmethod
        def _handle_epic_names_scope(scope_config: Dict[str, Any], story_graph: Dict[str, Any], expected_names: Set[str]):
            """Helper: Handle epic_names scope configuration."""
            if 'epic_names' in scope_config:
                epic_names_list = scope_config['epic_names']
                if not isinstance(epic_names_list, list):
                    epic_names_list = [epic_names_list]
                for epic_name in epic_names_list:
                    for epic in story_graph.get('epics', []):
                        if epic.get('name') == epic_name:
                            TestValidateRulesAccordingToScope._extract_story_names_from_epic(epic, expected_names)
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3071): Function "_extract_story_names_from_epic" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
        @staticmethod
        def _extract_story_names_from_epic(epic_data: Dict[str, Any], story_names: Set[str]) -> None:
            """Recursively extract story names from epic/sub_epic structure."""
            for story in epic_data.get('stories', []):
                if isinstance(story, dict) and 'name' in story:
                    story_names.add(story['name'])
                elif isinstance(story, str):
                    story_names.add(story)
            
            for story_group in epic_data.get('story_groups', []):
                for story in story_group.get('stories', []):
                    if isinstance(story, dict) and 'name' in story:
                        story_names.add(story['name'])
                    elif isinstance(story, str):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:276): Function "given_setup" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            verify_workflow_saves_completed_action(bot_directory, workspace_directory, 'build')
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for BUILD KNOWLEDGE setup.
        Replaces: given_knowledge_graph_setup, given_knowledge_graph_setup_complete,
        given_knowledge_graph_config_and_template_created, given_knowledge_graph_directory_structure_created,
        given_knowledge_graph_directory_for_prioritization, given_environment_and_knowledge_graph_setup
        
        Args:
            setup_type: Type of setup ('knowledge_graph', 'knowledge_graph_complete', 'config_and_template',
                        'directory_structure', 'directory_for_prioritization', 'environment_and_kg')
            bot_directory: Bot directory path
            **setup_params: Additional parameters (behavior, template_name, workspace_directory, kg_dir)
        
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:448): Function "then_location_matches" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def then_location_matches(item, type=None, field=None):
        """
        Consolidated function for checking map location correctness.
        Replaces: then_epic_map_location_correct, then_sub_epic_map_location_correct,
        then_story_map_location_correct, then_scenario_map_location_correct,
        then_scenario_outline_map_location_correct
        
        Args:
            item: Epic, SubEpic, Story, Scenario, or ScenarioOutline instance
            type: Type hint ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline') - auto-detected if None
            field: Optional field name to check (e.g., 'sequential_order', 'sizing')
        """
        # Auto-detect type if not provided
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1424): Function "then_story_graph_contains_story" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    
    
    def then_story_graph_contains_story(filtered_graph, story_name):
        """Then: Story graph contains story."""
        story_names = []
        for epic in filtered_graph.get('epics', []):
            for sub_epic in epic.get('sub_epics', []):
                for story_group in sub_epic.get('story_groups', []):
                    for story in story_group.get('stories', []):
                        if isinstance(story, dict):
                            story_names.append(story.get('name'))
                        else:
                            story_names.append(story)
        assert story_name in story_names
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:36): Function "when_action_executes_with_parameters" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
    # ============================================================================
    
    def when_action_executes_with_parameters(action, parameters: dict):
        """When: Action executes with parameters (converts dict to typed context).
        
        Determines the appropriate context type based on the action class.
        """
        from agile_bot.bots.base_bot.src.actions.action_context import StrategyActionContext, ValidateActionContext, Scope, ScopeType
        from agile_bot.bots.base_bot.src.actions.strategy.strategy_action import StrategyAction
        from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
        
        if isinstance(action, StrategyAction):
            # Strategy action context
            context = StrategyActionContext(
                decisions_made=parameters.get('decisions_made'),
        # ... (truncated)
    ```

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 589 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:86): Useless comment: "# Handle both all_files and force_full (backward compatibili" - delete it or improve the code instead

    ```python
                    )
            
            # Handle both all_files and force_full (backward compatibility)
            all_files = parameters.get('all_files', False) or parameters.get('force_full', False)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:71): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    # Backward-compatible alias for given_file_created
    def given_test_file_created_with_content(directory: Path, filename: str, content: str) -> Path:
        """Alias for given_file_created - creates test file with content."""
        return given_file_created(directory, filename, content, file_type='text')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:80): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_unified_scanner_base_class():
        """Given: Unified Scanner base class exists."""
        from agile_bot.bots.base_bot.src.scanners.scanner import Scanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:86): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_with_combined_files(test_files: List[Path], code_files: List[Path], bot_directory: Path, behavior: str = 'tests'):
        """Given: Rule that combines test_files and code_files.
        
        Creates a Rule instance and verifies it combines files before passing to scanner.
        
        Args:
            test_files: List of test file paths
            code_files: List of code file paths
            bot_directory: Bot directory path
            behavior: Behavior name (default: 'tests')
            
        Returns:
            Tuple of (rule, all_files) where all_files is the combined list
        """
        from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:125): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_scanner_scans_files(scanner, files: List[Path], knowledge_graph: Dict[str, Any], rule_obj: Any = None):
        """When: Scanner scans files using unified scan_file() method.
        
        Calls scanner.scan() with files parameter (unified architecture).
        For now, works with current architecture (test_files/code_files) but prepares for unified.
        
        Args:
            scanner: Scanner instance
            files: List of file paths to scan (test files, code files, or both)
            knowledge_graph: Knowledge graph dict
            rule_obj: Optional rule object
            
        Returns:
            List of violations
        """
        from pathlib import Path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:168): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_received_all_files(scanner_spy, expected_files: List[Path]):
        """Then: Scanner received all files (no filtering by type).
        
        Verifies scanner received all files, not filtered.
        
        Args:
            scanner_spy: Spy scanner that records received files
            expected_files: List of expected file paths
        """
        received_files = getattr(scanner_spy, 'received_files', [])
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:187): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_did_not_check_file_type(scanner_spy):
        """Then: Scanner did not check file type internally.
        
        Verifies no _is_test_file() calls were made.
        
        Args:
            scanner_spy: Spy scanner that records method calls
        """
        called_is_test_file = getattr(scanner_spy, 'called_is_test_file', False)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:202): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_domain_concepts_in_story_graph(concepts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Given: Story graph with domain_concepts.
        
        Creates a test knowledge graph with domain_concepts structure.
        
        Args:
            concepts: List of domain concept dicts, e.g.:
                [{'name': 'Game Master', 'responsibilities': [{'name': 'Manage Mobs'}], 'collaborators': ['Mob Manager']}]
                
        Returns:
            Knowledge graph dict with domain_concepts
        """
        knowledge_graph = {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:235): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_domain_terms_extracted_correctly(extracted_terms: Set[str], expected_terms: Set[str]):
        """Then: Domain terms extracted correctly from story graph.
        
        Verifies extracted terms match expected, including compound terms.
        
        Args:
            extracted_terms: Set of extracted domain terms
            expected_terms: Set of expected domain terms
        """
        # Verify all expected terms are present (or at least their components)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:268): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_spy_scanner_for_unified_architecture():
        """Given: Spy scanner that records calls for unified architecture testing.
        
        Returns a spy scanner class that records:
        - received_files: List of files received
        - called_is_test_file: Whether _is_test_file() was called
        
        Returns:
            Tuple of (spy_scanner_class, spy_instance)
        """
        from agile_bot.bots.base_bot.src.scanners.code_scanner import CodeScanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:297): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
            
            def _is_test_file(self, file_path: Path) -> bool:
                """Record that this method was called."""
                self.called_is_test_file = True
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:327): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_workflow_state_with_all_actions_completed(workspace_directory: Path, bot_name: str, behavior: str, current_action: str):
        """Given: Workflow state with all actions completed."""
        return create_workflow_state_file(
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:344): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_workflow_completion_checked(behavior: str, state_file: Path):
        """
        Consolidated function for checking workflow completion status.
        Replaces: when_check_workflow_completion_status
        
        Args:
            behavior: Behavior name
            state_file: Path to state file
        
        Returns:
            Boolean indicating if workflow is complete
        """
        import json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:366): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_workflow_completion_matches(is_complete: bool, expected: bool = True):
        """
        Consolidated function for verifying workflow completion status.
        Replaces: then_behavior_workflow_is_complete
        
        Args:
            is_complete: Actual completion status
            expected: Expected completion status (default: True)
        """
        assert is_complete == expected, f"Expected workflow completion to be {expected}, got {is_complete}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:380): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _validate_rule_structure(rule):
        """Helper: Validate individual rule structure.
        
        Accepts Rule objects or dicts (for backward compatibility with validated rules).
        """
        from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:421): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_violations_match_scope(violated_stories: set, expected_stories: set, expected_violations: set):
        """Then: Violations match expected scope and stories.
        
        Consolidates: then_violations_match_expected_scope_and_stories(violated_story_names, expected_stories_in_scope_set, expected_violations_set)
        
        Args:
            violated_stories: Set of story names that have violations
            expected_stories: Set of story names expected to be in scope (optional - if empty, scope check is skipped)
            expected_violations: Set of story names expected to have violations
        """
        if expected_stories:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:446): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_stories_match(expected: set, stories_to_check, present: bool = None):
        """
        Consolidated function for matching stories.
        Replaces: then_expected_story_names_contain_stories, then_expected_story_names_equal
        
        Args:
            expected: Expected set of story names
            stories_to_check: Stories to check (set or list)
            present: If True, checks stories are present; if False, checks stories are absent;
                     if None and stories_to_check is a set, checks equality
        
        Returns:
            None (asserts on failure)
        """
        if isinstance(stories_to_check, set) and present is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:474): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_violations_detected_in_file(violations: list, file: Path):
        """Then: Violations detected in file.
        
        Consolidates: then_violations_detected_in_test_file(all_violations, test_file)
        
        Args:
            violations: List of violation dictionaries
            file: Path to the file that should have violations
        """
        assert len(violations) > 0, f"Should detect violations in file: {file}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:496): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_violations_count_is(violations: list, count: int = None):
        """Then: Violations count is.
        
        Consolidates: then_violations_detected_in_test_files_count(all_violations, expected_count)
        
        Args:
            violations: List of violation dictionaries
            count: Expected count of violations. If None, just checks that violations exist.
        """
        if count is not None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:513): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_violations_found_in_files(violations: list, files: list):
        """Then: Violations found in files.
        
        Consolidates: then_violations_found_in_test_files(all_violations, test_files)
        
        Args:
            violations: List of violation dictionaries
            files: List of file paths that should have violations
        """
        assert len(violations) > 0, "Should detect violations in files"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:535): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_detects_violations_with_message(violations: list, scanner_class_path: str, message: str):
        """Then: Scanner detects violations with message.
        
        Consolidates: then_scanner_detects_violations_with_expected_message(violations, scanner_class_path, expected_violation_message)
        
        Args:
            violations: List of violation dictionaries
            scanner_class_path: Path to scanner class
            message: Expected violation message
        """
        assert len(violations) > 0, f"Scanner {scanner_class_path} should detect violations in bad example"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:575): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_file_created(bot_directory: Path, behavior: str, rule_filename: str, rule_content: dict = None, **params):
        """
        Consolidated function for creating rule files.
        Replaces: given_behavior_rule_file_created, given_scenarios_rule_created,
        given_test_scope_verification_rule_created, given_validation_rule_for_verb_noun_format,
        given_validation_rules_created
        
        Args:
            bot_directory: Bot directory path
            behavior: Behavior name (required for behavior rules)
            rule_filename: Name of the rule file
            rule_content: Content of the rule file (dict)
            **params: Additional parameters:
                - rule_type: Type of rule ('behavior', 'scenarios', 'test_scope_verification',
                              'validation', 'verb_noun_format')
                - rules_dir_name: Directory name ('3_rules' or 'rules', default: '3_rules')
        
        Returns:
            Path to created rule file
        """
        rule_type = params.get('rule_type', 'behavior')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:653): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_object_for_scanner(rule_filename: str, scanner_class_path: str, behavior_name: str):
        """Given: Rule object for scanner."""
        from pathlib import Path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:668): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_created_for_test_bot(test_bot_dir: Path, behavior_name: str, bot_name: str):
        """Given: Behavior created for test bot."""
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:687): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _extract_test_files_from_bad_example(bad_example: dict):
        """Helper: Extract test files list from bad_example."""
        test_files_to_scan = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:697): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _extract_knowledge_graph_from_bad_example(bad_example: dict):
        """Helper: Extract knowledge graph from bad_example."""
        if 'knowledge_graph' in bad_example:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:704): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _scan_files_via_scan_method(scanner_instance: TestScanner, bad_example: dict, rule_obj: Rule):
        """Helper: Try scanning via scan() method."""
        test_files_list = None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:739): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _convert_scope_config_to_unified_format(scope_config: dict) -> dict:
        """Convert old scope_config format to new unified scope format."""
        if not scope_config:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:771): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_parameters_created(scope=None, test_files=None, code_files=None):
        """
        Consolidated function for creating parameters.
        Replaces: when_create_parameters_from_scope_config, when_create_test_file_parameter,
        when_create_test_files_parameter, when_create_code_files_parameter, when_create_empty_parameters
        """
        if scope is not None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:793): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_action_and_extract_violations(action, parameters: dict):
        """When: Execute action and extract violations."""
        result = when_action_executes_with_scope_parameters(action, parameters)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:807): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_test_file_for_class_based_scanner(test_file: Path):
        """Helper: Create test file for class-based scanner."""
        test_file.write_text('''class TestGenTools:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:819): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_test_file_for_test_quality_scanner(test_file: Path):
        """Helper: Create test file for test quality scanner."""
        test_file.write_text('''def test_1():
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:831): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_test_file_for_specification_match_scanner(test_file: Path):
        """Helper: Create test file for specification match scanner."""
        test_file.write_text('''def test_agent_init(self):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:845): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_test_files_for_test_scanners(test_file: Path, scanner_class_path: str):
        """Helper: Create test files for test scanners."""
        if 'class_based' in scanner_class_path.lower():
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:855): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_code_file_for_scanner_type(test_file: Path, scanner_class_path: str):
        """Helper: Create code file for specific scanner type."""
        scanner_lower = scanner_class_path.lower()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1052): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_file_for_scanner_type(workspace_directory: Path, scanner_class_path: str, behavior: str):
        """Given: Test file for scanner type."""
        test_file = workspace_directory / 'test_code.py'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1097): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_executes_and_returns_result(action: ValidateRulesAction, parameters: dict = None, context: 'ValidateActionContext' = None):
        """When: Action executes and returns result with typed context."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1132): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_executes_and_raises_file_not_found_error(action: ValidateRulesAction):
        """When: Action executes and raises FileNotFoundError."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1139): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_executes_and_raises_json_error(action: ValidateRulesAction):
        """When: Action executes and raises JSON error."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1154): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scanner_test_setup(bot_directory: Path, workspace_directory: Path, scanner_class_path: str, behavior: str):
        """
        Consolidated function for scanner test setup.
        Replaces: when_setup_scanner_test_environment
        
        Args:
            bot_directory: Bot directory path
            workspace_directory: Workspace directory path
            scanner_class_path: Path to scanner class
            behavior: Behavior name
        
        Returns:
            Tuple of (scanner_class, rule_obj)
        """
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1175): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_setup_for_file_not_found_test(bot_directory: Path, workspace_directory: Path):
        """Given: Environment setup for file not found test."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1184): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_setup_for_invalid_json_test(bot_directory: Path, workspace_directory: Path):
        """Given: Environment setup for invalid JSON test."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1195): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_test_file_scope_verification(action, test_file: Path, story_graph: dict):
        """When: Execute test file scope verification.
        
        Verifies that test_files parameter is passed correctly through action execution.
        The action.do_execute() already passes test_files to scanners via ValidationContext.
        """
        parameters = when_parameters_created(test_files=test_file)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1208): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_action_and_extract_violated_story_names_with_conversion(action, parameters: dict, story_graph: dict, test_case: dict, extract_story_names_method, extract_epic_method):
        """When: Execute action and extract violated story names with conversion."""
        result = when_action_executes_and_returns_result(action, parameters=parameters)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1222): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_file_created_if_needed(directory: Path, scanner_class_path: str, behavior: str, bad_example):
        """
        Consolidated function for creating test files if needed for scanner.
        Replaces: when_create_test_file_if_needed_for_scanner
        
        Args:
            directory: Directory where file should be created
            scanner_class_path: Path to scanner class
            behavior: Behavior name
            bad_example: Bad example content (string, dict, or None)
        
        Returns:
            Tuple of (file_path, parameters_dict) or (None, bad_example)
        """
        if bad_example is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1256): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_scanner_based_on_type(scanner_instance, bad_example: dict, rule_obj):
        """When: Execute scanner based on type.
        
        NEW DOMAIN MODEL: Use rule.scan() instead of calling scanner directly.
        """
        # Extract knowledge graph and files from bad_example
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1299): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_base_action_instructions_and_behavior_rule_setup(bot_directory: Path, workspace_directory: Path):
        """Given: Base action instructions and behavior rule setup."""
        instructions_file = given_action_config(bot_directory, 'validate')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1312): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_and_action_for_report_path_test(bot_directory: Path, workspace_directory: Path):
        """Given: Environment and action for report path test."""
        docs_dir = given_directory_created(workspace_directory, directory_type='docs_stories', return_path=True)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1322): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_bot_setup(bot_directory: Path, workspace_directory: Path, rules: dict = None, knowledge_graph: dict = None, **params):
        """
        Consolidated function for bot setup with rules and/or knowledge graph.
        Replaces: given_test_bot_setup_with_rules, given_knowledge_graph_and_test_bot_setup
        
        Args:
            bot_directory: Bot directory path
            workspace_directory: Workspace directory path
            rules: Dict with 'repo_root', 'rule_file_paths', 'rule_file_content' (for test_bot_setup_with_rules)
                   OR dict with 'repo_root', 'rule_file_path', 'rule_file_content' (for knowledge_graph_and_test_bot_setup)
            knowledge_graph: Knowledge graph dict (optional, for knowledge_graph_and_test_bot_setup)
            **params: Additional parameters (repo_root, etc.)
        
        Returns:
            test_bot_dir Path (if rules only) or (kg_file, test_bot_dir) tuple (if knowledge_graph provided)
        """
        repo_root = params.get('repo_root') or (rules.get('repo_root') if rules else None)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1367): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_validate_code_files_action_with_test_files(bot_name: str, behavior: str, bot_directory: Path, test_files: list):
        """When: Execute validate code files action with test files."""
        action = when_validate_code_files_action_created(bot_name, behavior, bot_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1376): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_validate_code_files_action_with_single_test_file(bot_name: str, behavior: str, bot_directory: Path, test_file: Path):
        """When: Execute validate code files action with single test file."""
        action = when_validate_code_files_action_created(bot_name, behavior, bot_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1383): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_content_dict(rule_type: str = None):
        """
        Consolidated function for creating rule content dictionaries.
        Replaces: given_verb_noun_rule_content
        
        Args:
            rule_type: Type of rule content ('verb_noun' or None for default verb_noun)
        
        Returns:
            Rule content dictionary
        """
        if rule_type is None or rule_type == 'verb_noun':
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1415): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for VALIDATE setup.
        Replaces: given_validation_setup, given_story_graph_and_test_file_with_violations_setup,
        given_test_file_and_naming_rule_setup, given_story_graph_test_file_and_rules_setup,
        given_test_file_and_naming_rule_with_rule_id_setup, given_comprehensive_story_graph_setup_for_scope_test,
        given_test_file_scope_verification_setup, given_test_file_scope_setup_with_rule,
        given_multiple_test_files_scope_setup_with_rule
        
        Args:
            setup_type: Type of setup ('validation', 'story_graph_and_test_file_with_violations',
                        'test_file_and_naming_rule', 'story_graph_test_file_and_rules',
                        'test_file_and_naming_rule_with_rule_id', 'comprehensive_story_graph_for_scope',
                        'test_file_scope_verification', 'test_file_scope_with_rule',
                        'multiple_test_files_scope_with_rule')
            bot_directory: Bot directory path
            **setup_params: Additional parameters (workspace_directory, behavior, violations, rule_type,
                          create_method, etc.)
        
        Returns:
            Varies by setup_type:
            - 'validation': None (just sets up environment)
            - 'story_graph_and_test_file_with_violations': test_file Path
            - 'test_file_and_naming_rule': test_file Path
            - 'story_graph_test_file_and_rules': test_file Path
            - 'test_file_and_naming_rule_with_rule_id': test_file Path
            - 'comprehensive_story_graph_for_scope': (story_graph, story_graph_path)
            - 'test_file_scope_verification': (story_graph, story_graph_path)
            - 'test_file_scope_with_rule': (story_graph, story_graph_path, test_file)
            - 'multiple_test_files_scope_with_rule': (story_graph, story_graph_path, test_file1, test_file2)
        """
        workspace_directory = setup_params.get('workspace_directory')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1596): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_validate_code_files_action_with_code_files(bot_name: str, behavior: str, bot_directory: Path, code_files: list, workspace_directory: Path = None):
        """When: Execute validate code files action with code files."""
        action = when_validate_code_files_action_created(bot_name, behavior, bot_directory, workspace_directory=workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1605): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_test_file_scope_validation(action, test_file: Path, story_graph_path: Path):
        """When: Execute test file scope validation."""
        parameters = when_parameters_created(test_files=test_file)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1614): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_multiple_test_files_scope_validation(action, test_file1: Path, test_file2: Path, story_graph_path: Path):
        """When: Execute multiple test files scope validation."""
        parameters = when_parameters_created(test_files=[test_file1, test_file2])
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1624): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_file_scope_verification_complete_setup(bot_directory: Path, workspace_directory: Path):
        """Given: Test file scope verification complete setup."""
        story_graph, story_graph_path = given_setup('test_file_scope_verification', bot_directory, workspace_directory=workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1643): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_result_contains_instructions_with_content_to_validate(result: dict):
        """Then: Result contains instructions with content_to_validate."""
        assert 'instructions' in result, "Result should contain 'instructions' key"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1653): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_content_to_validate_has_report_path(instructions_or_content_info: dict, expected_docs_dir: Path):
        """Then: Instructions have report_path.
        
        Note: report_path is at the top level of instructions dict, not inside content_to_validate.
        This function accepts either the full instructions dict or content_info for backwards compatibility.
        """
        # Report path is at top level of instructions, not inside content_to_validate
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1669): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_injects_behavior_specific_and_bot_rules(action: ValidateRulesAction):
        """When: Action gets action instructions."""
        return action.get_action_instructions()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1674): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rules_data_has_valid_action_instructions(rules_data: list):
        """Then: Rules data has valid action instructions."""
        assert isinstance(rules_data, list), (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1684): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_result_contains_instructions(result: dict):
        """Then: Result contains instructions."""
        assert 'instructions' in result, "Result should contain 'instructions' key"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1689): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_base_instructions_are_valid_list(instructions: dict):
        """Then: Base instructions are valid list."""
        assert 'base_instructions' in instructions, (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1701): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_base_instructions_contain_clarification_reference(base_instructions_list: list):
        """Then: Base instructions contain clarification reference."""
        instructions_text = ' '.join(base_instructions_list)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1708): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_validation_rules_are_valid_list(instructions: dict):
        """Then: Validation rules are valid list."""
        assert 'validation_rules' in instructions, (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1720): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_content_to_validate_has_workspace_location(instructions: dict, workspace_directory: Path):
        """Then: Content to validate has workspace location."""
        assert 'content_to_validate' in instructions, (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1743): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_instructions_specify_action_and_behavior(instructions: dict, expected_action: str, expected_behavior: str):
        """Then: Instructions specify action and behavior."""
        assert instructions.get('action') == expected_action, (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1752): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_report_path_is_valid(content_info: dict, workspace_directory: Path):
        """Then: Report path is valid."""
        # content_info can be None - skip check if None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1777): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_base_instructions_include_save_report_instruction(instructions: dict):
        """Then: Base instructions include save report instruction."""
        base_instructions_list = instructions['base_instructions']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1790): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_specific_rule_exists(bot_directory: Path, behavior: str, rule_name: str, rule_content: dict):
        """Given: Behavior-specific rule exists."""
        behavior_dir = bot_directory / 'behaviors' / behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1801): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_story_graph_file_exists_minimal(workspace_directory: Path):
        """Given: Minimal story graph file exists."""
        docs_dir = workspace_directory / 'docs' / 'stories'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1813): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_instructions_file_exists_and_has_content(instructions_file: Path):
        """Then: Instructions file exists and has content."""
        assert instructions_file.exists(), f"Instructions file should exist at {instructions_file}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1821): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_action_finds_instructions_file(action: ValidateRulesAction, expected_instructions_file: Path):
        """Then: Action finds instructions file."""
        action_base_actions_dir = action.base_actions_dir
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1830): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_common_rule_created(bot_directory: Path, rule_name: str, rule_content: dict, behavior_name: str = None):
        """Given: Common rule created.
        
        Uses consolidated given_file_created internally.
        
        Args:
            bot_directory: Bot directory path
            rule_name: Name of the rule file
            rule_content: Rule content dictionary
            behavior_name: Behavior name (if None, creates in bot_directory/rules, otherwise in behaviors/behavior_name/rules)
        """
        from agile_bot.bots.base_bot.test.test_helpers import given_file_created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1849): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_story_graph_saved_to_workspace(workspace_directory: Path, story_graph: dict):
        """Given: Story graph saved to workspace."""
        docs_stories_dir = given_directory_created(workspace_directory, directory_type='docs_stories')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1857): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_add_scope_to_story_graph(story_graph_path: Path, story_graph: dict, scope_config: dict):
        """When: Add scope to story graph."""
        story_graph['_validation_scope'] = scope_config
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1863): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_extract_violations_from_validation_rules(validation_rules: list):
        """When: Extract violations from validation rules."""
        all_violations = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1893): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_file_with_content(workspace_directory: Path, filename: str, content: str):
        """Given: Test file with content."""
        test_file = workspace_directory / filename
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1900): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_rule_created(bot_directory: Path, behavior: str, rule_name: str, rule_content: dict):
        """Given: Behavior rule created.
        
        Uses consolidated given_rule_file_created internally.
        """
        return given_rule_file_created(bot_directory, behavior, rule_name, rule_content, rule_type='behavior', rules_dir_name='3_rules')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1908): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_executes_with_scope_parameters(action: ValidateRulesAction, parameters: dict):
        """When: Action executes with scope parameters."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1955): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_file_created(workspace_directory: Path, filename: str, content: str):
        """Given: Test file created in test directory (using test_base_bot structure).
        
        Uses consolidated given_file_created internally.
        """
        from agile_bot.bots.base_bot.test.test_helpers import given_file_created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1965): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_source_file_created(workspace_directory: Path, filename: str, content: str):
        """Given: Source file created in src directory (using test_base_bot structure).
        
        Uses consolidated given_file_created internally.
        """
        from agile_bot.bots.base_bot.test.test_helpers import given_file_created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1975): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_bootstrapped_with_story_graph(bot_directory: Path, workspace_directory: Path, story_graph: dict = None):
        """Given: Environment bootstrapped with story graph."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1984): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_validate_code_files_action_created(bot_name: str, behavior: str, bot_directory: Path, workspace_directory: Path = None):
        """When: ValidateRulesAction created (ValidateCodeFilesAction was removed, use ValidateRulesAction instead)."""
        from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2023): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_validate_code_files_action_executes(action, parameters: dict):
        """When: ValidateRulesAction executes with parameters (ValidateCodeFilesAction was removed)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext, Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2062): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_result_has_violations_or_instructions(result: dict, expected_message: str = None):
        """Then: Result has violations or instructions."""
        assert 'violations' in result or 'instructions' in result, (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2069): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_common_rule_file_created(bot_directory: Path, rule_name: str, rule_content: dict):
        """Given: Common rule file created.
        
        Uses consolidated given_file_created internally.
        """
        from agile_bot.bots.base_bot.test.test_helpers import given_file_created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2079): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_story_graph_with_content(workspace_directory: Path, story_graph_content: dict):
        """Given: Story graph with content."""
        story_graph_path = workspace_directory / 'docs' / 'stories' / 'story-graph.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2087): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_json_created(bot_directory: Path, behavior: str, actions: list):
        """Given: Behavior.json file created."""
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2097): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_file_unchanged(file_path: Path, **checks):
        """
        Consolidated function for checking file hasn't changed.
        Replaces: then_story_graph_not_modified_with_test_files
        
        Args:
            file_path: Path to file to check
            **checks: Optional checks like 'exclude_keys' (list of keys that should not be present)
        """
        if 'exclude_keys' in checks:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2123): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def create_test_rule_file(repo_root: Path, rule_path: str, rule_content: Dict[str, Any]) -> Path:
        """
        Helper: Create a test-specific rule.json file at specified path.
        Used for creating rule files defined in Examples tables.
        """
        full_path = repo_root / rule_path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2133): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def load_existing_rule_file(repo_root: Path, rule_path: str) -> Optional[Dict[str, Any]]:
        """
        Helper: Load an existing rule file from the codebase.
        """
        full_path = repo_root / rule_path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2143): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _validate_scanner_class(scanner_class, scanner_module_path: str):
        """Helper: Validate scanner class structure."""
        if not isinstance(scanner_class, type):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2151): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def load_scanner_class(scanner_module_path: str):
        """
        Helper: Load an existing scanner class from the codebase.
        Validates that the class inherits from Scanner base class.
        Returns (scanner_class, error_message) tuple.
        If scanner doesn't exist or doesn't inherit from Scanner, returns (None, error_message).
        """
        from agile_bot.bots.base_bot.src.scanners.scanner_loader import ScannerLoader
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2170): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def setup_test_rules(repo_root: Path, rule_paths: List[str], rule_contents: List[Dict[str, Any]]) -> List[Path]:
        """
        Helper: Create test rule files in filesystem from Examples table data.
        This ONLY creates the files - does NOT load them or discover scanners.
        The test should call ValidateRulesAction methods to do the actual loading.
        
        Files are created under repo_root (which uses tmp_path fixture) so they auto-cleanup.
        
        
        """
        created_files = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2205): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def validate_violation_structure(violation: Dict[str, Any], expected_fields: List[str]) -> bool:
        """Validate violation has required fields."""
        return all(field in violation for field in expected_fields)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2233): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    @pytest.fixture
    def cleanup_test_files():
        """
        Fixture: Track and cleanup test files created during tests.
        Since repo_root and bot_directory use tmp_path, they auto-cleanup,
        but this ensures any files created outside those directories are tracked.
        """
        created_files = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2252): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestTrackActivityForValidateRulesAction:
        """Story: Track Activity for Validate Rules Action - Tests activity tracking for validate."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2255): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_track_activity_when_validate_action_starts(self, bot_directory, workspace_directory):
            """
            SCENARIO: Track activity when validate action starts
            GIVEN: behavior is 'exploration' and action is 'validate'
            WHEN: validate action starts execution
            THEN: Activity logger creates entry with timestamp and action_state
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2272): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_track_activity_when_validate_action_completes(self, bot_directory, workspace_directory):
            """
            SCENARIO: Track activity when validate action completes
            GIVEN: validate action started at timestamp
            WHEN: validate action finishes execution
            THEN: Activity logger creates completion entry with outputs and duration
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2305): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_track_multiple_validate_invocations_across_behaviors(self, bot_directory, workspace_directory):
            """
            SCENARIO: Track multiple validate invocations across behaviors
            GIVEN: activity log contains entries for shape and exploration validate
            WHEN: both entries are present
            THEN: activity log distinguishes same action in different behaviors
            """
            # Given: Activity log with multiple validate entries (in workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2336): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_activity_log_maintains_chronological_order(self, bot_directory, workspace_directory):
            """
            SCENARIO: Activity Log Maintains Chronological Order
            GIVEN: activity log contains 10 previous action entries
            WHEN: validate entry is appended
            THEN: New entry appears at end of log in chronological order
            """
            # Given: Activity log with 10 entries (in workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2366): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestInvokeCompleteValidationWorkflow:
        """Story: Invoke Complete Validation Workflow - Tests workflow completion at terminal action."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2369): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_marks_workflow_as_complete(self, bot_directory, workspace_directory):
            """
            SCENARIO: validate marks workflow as complete
            GIVEN: validate action is complete
            AND: validate is terminal action (next_action=null)
            WHEN: validate finalizes
            THEN: Workflow is marked as complete (no next action)
            """
            # Given: Terminal action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2386): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_does_not_inject_next_action_instructions(self, bot_directory, workspace_directory):
            """
            SCENARIO: validate does NOT inject next action instructions
            GIVEN: validate action is complete
            AND: validate is terminal action
            WHEN: validate finalizes
            THEN: No next action instructions injected
            """
            # Given: Terminal action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2405): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_workflow_state_shows_all_actions_completed(self, bot_directory, workspace_directory):
            """
            SCENARIO: Workflow state shows all actions completed
            GIVEN: validate completes as final action
            WHEN: Action tracks completion
            THEN: Activity log records the completion
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2426): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_activity_log_records_full_workflow_completion(self, bot_directory, workspace_directory):
            """
            SCENARIO: Activity log records full workflow completion
            GIVEN: validate completes at timestamp
            WHEN: Activity logger records completion
            THEN: Activity log shows validate completed and workflow finished
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2447): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_workflow_does_not_transition_after_validate(self, bot_directory, workspace_directory):
            """
            SCENARIO: Workflow does NOT transition after validate
            GIVEN: validate action is complete
            AND: validate is terminal action
            WHEN: validate provides next action instructions
            THEN: No next action instructions (empty string indicates terminal action)
            """
            # Given: Terminal action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2465): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_behavior_workflow_completes_at_terminal_action(self, bot_directory, workspace_directory):
            """
            SCENARIO: Behavior workflow completes at terminal action
            GIVEN: exploration behavior has completed all 5 workflow actions
            WHEN: validate (terminal) is marked complete
            THEN: Exploration behavior workflow is complete
            """
            # Given: Workflow state with all actions completed
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2483): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _verify_action_setup_and_execution(self, bot_directory, workspace_directory):
            """Helper: Set up action and execute, returning action and result."""
            instructions_file = given_base_action_instructions_and_behavior_rule_setup(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2492): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _verify_instructions_structure(self, action_result, workspace_directory):
            """Helper: Verify instructions structure contains required fields."""
            instructions = then_result_contains_instructions(action_result)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2504): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_returns_instructions_with_rules_as_context(self, bot_directory, workspace_directory):
            """
            SCENARIO: validate returns instructions with rules as supporting context
            GIVEN: validate action has base instructions and validation rules
            WHEN: validate action executes
            THEN: Return value contains base_instructions (primary) and validation_rules (context)
            AND: Return value contains content_to_validate information
            """
            action, action_result = self._verify_action_setup_and_execution(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2517): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_provides_report_path_for_saving_validation_report(self, bot_directory, workspace_directory):
            """
            SCENARIO: validate provides report_path for saving validation report
            GIVEN: validate action executes
            AND: workspace directory has docs/stories/ folder
            WHEN: Action identifies content to validate
            THEN: Action includes report_path in content_to_validate
            AND: report_path points to {workspace_area}/docs/stories/validation-report.md
            AND: base_instructions include instruction to save report to report_path
            AND: AI receives clear instruction to write validation report to file
            """
            # Given: Base action instructions exist with save report instruction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2547): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestDiscoversScanners:
        """Story: Discovers Scanners - Tests scanner discovery from rule files."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2584): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_scanner_discovery_extracts_metadata_and_registers_scanners(self, repo_root, bot_directory, workspace_directory, rule_file_paths, rule_file_content, expected_scanner_count):
            """
            SCENARIO: Scanner discovery extracts metadata and registers scanners
            GIVEN: Rule files exist at specified paths
            AND: Rule files contain scanner configurations
            WHEN: Scanner discovery is executed via ValidateRulesAction
            THEN: Scanners are discovered and registered in catalog
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2607): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestRunScannersAgainstKnowledgeGraph:
        """Story: Run Scanners Against Knowledge Graph - Tests scanner execution against knowledge graph."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2654): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_scanners_detect_violations_in_knowledge_graph(self, repo_root, bot_directory, workspace_directory, rule_file_path, rule_file_content, knowledge_graph, expected_has_violations):
            """
            SCENARIO: Scanners detect violations in knowledge graph
            GIVEN: Knowledge graph contains problems
            AND: Rule file is specified
            WHEN: Scanners are executed against knowledge graph
            THEN: Violations are detected at expected line numbers
            
            Tests all examples from scenario file - parameterized test.
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2680): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestHandleValidateRulesExceptions:
        """Story: Handle Validate Rules Exceptions - Tests exception handling for validate action."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2683): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_raises_exception_when_story_graph_not_found(self, bot_directory, workspace_directory, tmp_path):
            """
            SCENARIO: ValidateRulesAction raises exception when story graph not found
            GIVEN: Story graph file doesn't exist
            WHEN: validate action executes
            THEN: FileNotFoundError is raised with appropriate message
            """
            # Given: Story graph file doesn't exist
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2698): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_raises_exception_when_story_graph_invalid_json(self, bot_directory, workspace_directory, tmp_path):
            """
            SCENARIO: ValidateRulesAction raises exception when story graph has syntax error
            GIVEN: Story graph file exists but contains invalid JSON
            WHEN: validate action executes
            THEN: JSONDecodeError or ValueError is raised
            """
            # Given: Story graph file exists but contains invalid JSON
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2718): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestValidateRulesAccordingToScope:
        """Story: Validate Rules According to Scope - Tests that validate only processes stories within specified scope."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2722): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def create_comprehensive_story_graph() -> Dict[str, Any]:
            """Create a comprehensive story graph with multiple epics, sub-epics, stories, and increments."""
            return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2996): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def extract_story_names_from_violations(violations: List[Dict[str, Any]]) -> Set[str]:
            """Extract story names from violation messages."""
            story_names = set()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3011): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _handle_story_names_scope(scope_config: Dict[str, Any], expected_names: Set[str]):
            """Helper: Handle story_names scope configuration."""
            if 'story_names' in scope_config:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3021): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _handle_increment_priorities_scope(scope_config: Dict[str, Any], story_graph: Dict[str, Any], expected_names: Set[str]):
            """Helper: Handle increment_priorities scope configuration."""
            if 'increment_priorities' in scope_config:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3037): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _handle_epic_names_scope(scope_config: Dict[str, Any], story_graph: Dict[str, Any], expected_names: Set[str]):
            """Helper: Handle epic_names scope configuration."""
            if 'epic_names' in scope_config:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3049): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def get_expected_story_names_for_scope(scope_config: Dict[str, Any], story_graph: Dict[str, Any]) -> Set[str]:
            """Calculate expected story names in scope based on scope configuration."""
            expected_names = set()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3060): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _extract_story_names_from_increment(increment_data: Dict[str, Any], story_names: Set[str]) -> None:
            """Recursively extract story names from increment structure."""
            for story in increment_data.get('stories', []):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3072): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _extract_story_names_from_epic(epic_data: Dict[str, Any], story_names: Set[str]) -> None:
            """Recursively extract story names from epic/sub_epic structure."""
            for story in epic_data.get('stories', []):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3316): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @pytest.mark.parametrize("test_case", SCOPE_TEST_CASES, ids=[tc["test_name"] for tc in SCOPE_TEST_CASES])
        def test_validate_respects_scope(self, test_case: Dict[str, Any], tmp_path: Path, bot_directory, workspace_directory):
            """
            SCENARIO: Validate that validate only processes stories within specified scope.
            
            Tests various scope configurations:
            - Single story
            - Multiple stories
            - Single epic
            - Multiple epics
            - Single sub-epic
            - Multiple sub-epics from different epics
            - Single increment
            - Multiple increments
            - Epic with many sub-epics
            - Combined scope criteria
            - Validate all
            - Default to all stories
            """
            # Setup
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3357): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_scope_extraction(self, bot_directory, workspace_directory):
            """Test that scope extraction functions work correctly."""
            # Given: Comprehensive story graph
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3397): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_with_test_file_scope_parameter(self, bot_directory, workspace_directory):
            """
            SCENARIO: Validate test file using test_file scope parameter
            GIVEN: A test file exists with violations
            AND: A rule with TestScanner exists
            WHEN: validate is called with test_file scope parameter
            THEN: TestScanner instances scan the test file
            AND: Violations are detected in the test file
            AND: test_file is not added to the knowledge graph (one-off validation)
            """
            # Given: Test file exists with violations and rule with TestScanner exists
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3415): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_with_test_files_scope_parameter(self, bot_directory, workspace_directory):
            """
            SCENARIO: Validate multiple test files using test_files scope parameter
            GIVEN: Multiple test files exist with violations
            AND: A rule with TestScanner exists
            WHEN: validate is called with test_files scope parameter (plural)
            THEN: TestScanner instances scan all test files
            AND: Violations are detected in all test files
            AND: test_files are passed through scope parameters correctly
            """
            # Given: Multiple test files exist with violations and rule with TestScanner exists
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3433): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_validate_verifies_test_files_passed_to_scanner(self, bot_directory, workspace_directory):
            """
            SCENARIO: Verify that test files from scope parameters are actually passed to TestScanner
            GIVEN: A test file exists
            AND: A spy TestScanner that records knowledge_graph it receives
            WHEN: validate is called with test_file scope parameter
            THEN: TestScanner receives knowledge_graph with test_files populated
            AND: test_files contains the test file from scope parameter
            """
            # Given: Test file exists and spy TestScanner that records knowledge_graph
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3461): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestRunAllScanners:
        """Story: Test All Scanners - Comprehensive tests for all scanner implementations."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3647): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_scanner_detects_violations(self, repo_root, bot_directory, workspace_directory, scanner_class_path, behavior, bad_example, expected_violation_message):
            """
            SCENARIO: Scanner detects violations in bad examples
            GIVEN: Scanner class path, behavior, bad example, and expected violation message
            WHEN: Scanner is executed against bad example
            THEN: Scanner detects violation with expected message
            
            Tests all scanners with real examples - parameterized test.
            """
            # Bootstrap environment
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3683): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestRunScannersAgainstTestCode:
        """Story: Run Scanners Against Test Code - Validates generated test files."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3686): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_accepts_test_files_parameter(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction accepts test files via test_files parameter"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3715): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_validates_each_file_from_parameters(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction validates each file provided via test_files parameter"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3728): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_merges_violations_from_knowledge_graph_and_files(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction merges violations from knowledge graph validation and code file validation"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3741): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_works_for_tests_behavior(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction works for tests behavior (test files)"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3767): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestRunScannersAgainstCode:
        """Story: Run Scanners Against Code - Validates generated source files."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3770): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_accepts_code_files_parameter(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction accepts source files via code_files parameter"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3795): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_works_for_code_behavior(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction works for code behavior (source files)"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3814): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_code_files_action_returns_early_when_no_files_provided(self, bot_directory, workspace_directory):
            """Scenario: ValidateCodeFilesAction returns knowledge graph results when no files provided"""
            
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3842): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rules_exist_for_behavior(bot_directory: Path, behavior: str):
        """Given: Rules exist for behavior."""
        rules_dir = bot_directory / 'rules'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3854): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rules_with_scanner_paths_exist(bot_directory: Path, behavior: str):
        """Given: Rules with scanner paths exist."""
        behavior_rules_dir = bot_directory / 'behaviors' / behavior / 'rules'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3866): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_validation_parameters_with_scope():
        """Given: Validation parameters with scope."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3874): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_with_scanner_path(bot_directory: Path, behavior: str):
        """Given: Rule with scanner path."""
        from agile_bot.bots.base_bot.src.actions.rules.rule import Rule
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3888): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scanner_loader_with_bot_name(bot_name: str):
        """Given: ScannerLoader with bot_name."""
        return ScannerLoader(bot_name=bot_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3893): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scanner_class_that_inherits_from_scanner():
        """Given: Scanner class that inherits from Scanner."""
        from agile_bot.bots.base_bot.src.scanners.scanner import Scanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3902): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_action_uses_rules_collection(action: ValidateRulesAction):
        """Then: Action uses Rules collection to load rules."""
        # Verify action uses Rules collection by checking if it loads rules
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3908): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_action_uses_rule_class_properties(action: ValidateRulesAction):
        """Then: Action uses Rule class properties."""
        # Verify action accesses rule properties through Rule class
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3918): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_action_uses_scanner_loader_service(action: ValidateRulesAction):
        """Then: Action uses ScannerLoader service."""
        # Verify action uses ScannerLoader by checking internal structure
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3924): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_action_uses_validation_scope_class(action: ValidateRulesAction, parameters: dict):
        """Then: Action uses ValidationScope class."""
        # Verify action uses ValidationScope by checking if it creates scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3932): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rule_uses_scanner_loader_service(rule):
        """Then: Rule uses ScannerLoader service."""
        # Verify rule uses ScannerLoader by checking if scanner is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3938): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_loader_tries_multiple_paths(scanner_loader: ScannerLoader, scanner_name: str):
        """Then: ScannerLoader tries multiple path locations."""
        # Verify ScannerLoader tries multiple paths (implementation detail)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3945): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_loader_validates_inheritance(scanner_loader: ScannerLoader, scanner_class):
        """Then: ScannerLoader validates inheritance from Scanner."""
        from agile_bot.bots.base_bot.src.scanners.scanner import Scanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3952): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_with_bot_paths(bot_directory, workspace_directory, bot_name, behavior_name):
        """Given: Behavior with bot_paths."""
        from agile_bot.bots.base_bot.test.test_helpers import bootstrap_env, create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3968): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_file_created_in_dir(rule_dir: Path, rule_name: str, rule_data: dict):
        """Given: Rule file created in specific directory.
        
        Uses consolidated given_file_created internally.
        Note: This is a specialized helper for creating rule files when you already have the rule_dir.
        For most cases, use the consolidated given_rule_file_created() function instead.
        """
        from agile_bot.bots.base_bot.test.test_helpers import given_file_created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3980): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rules_instantiated_with_behavior(behavior, bot_paths):
        """When: Rules instantiated with behavior."""
        return Rules(behavior=behavior, bot_paths=bot_paths)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3985): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rules_find_by_name(rules: Rules, rule_name: str):
        """When: find_by_name() called."""
        return rules.find_by_name(rule_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3990): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rules_iterate(rules: Rules):
        """When: iterate() called."""
        return iter(rules)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3995): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_instantiated_from_file(rule_file: Path):
        """When: Rule instantiated with file path."""
        # Rule requires behavior_name and bot_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4003): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_instantiated_from_content(rule_content: dict):
        """When: Rule instantiated with rule_content."""
        # Rule requires rule_file_path, behavior_name, bot_name even for embedded rules
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4012): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_validation_scope_instantiated(parameters: dict):
        """When: ValidationScope instantiated with parameters."""
        return ValidationScope(parameters)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4017): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_scanner_loader_loads_scanner(scanner_loader: ScannerLoader, scanner_path: str, bot_name: str = None):
        """When: load_scanner() called."""
        # ScannerLoader.load_scanner only takes scanner_module_path, bot_name is set in constructor
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4023): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rules_collection_contains_rules(rules: Rules, expected_count: int):
        """Then: Rules collection contains expected number of rules."""
        rule_list = list(rules)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4029): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rule_is_not_none(rule):
        """Then: Rule is not None."""
        assert rule is not None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4034): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rule_is_none(rule):
        """Then: Rule is None."""
        assert rule is None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4039): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rule_name_is(rule: Rule, expected_name: str):
        """Then: Rule name is expected."""
        assert rule.name == expected_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4044): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_validation_scope_contains(validation_scope: ValidationScope, expected_key: str, expected_value):
        """Then: ValidationScope contains expected key-value."""
        assert expected_key in validation_scope.scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4050): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_class_is_not_none(scanner_class):
        """Then: Scanner class is not None."""
        assert scanner_class is not None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4055): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_class_is_none(scanner_class):
        """Then: Scanner class is None."""
        assert scanner_class is None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4060): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_bot_rules_directory_created(bot_directory: Path):
        """Given: Bot rules directory created."""
        bot_rules_dir = bot_directory / 'rules'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4067): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_rules_directory_created(bot_directory: Path, behavior_name: str):
        """Given: Behavior rules directory created."""
        behavior_rules_dir = bot_directory / 'behaviors' / behavior_name / 'rules'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4074): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_without_bot_paths(bot_name: str, behavior_name: str, bot_directory: Path = None):
        """Given: Behavior without bot_paths."""
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4092): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rules_instantiation_raises_value_error_for_missing_bot_paths(behavior):
        """When: Rules instantiation raises ValueError for missing bot_paths."""
        with pytest.raises(ValueError, match='bot_paths is required'):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4098): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rules_instantiation_raises_value_error_for_missing_behavior():
        """When: Rules instantiation raises ValueError for missing behavior."""
        with pytest.raises(ValueError, match='Either behavior or bot_config must be provided'):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4104): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rules_iterator_has_count(iterator, expected_count: int):
        """Then: Rules iterator has expected count."""
        rule_list = list(iterator)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4110): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rules_iterator_includes_both_rule_types(iterator, bot_rule_name: str, behavior_rule_name: str):
        """Then: Rules iterator includes both rule types."""
        rule_list = list(iterator)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4118): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_names_extracted_from_list(rule_list):
        """When: Rule names extracted from list."""
        return [rule.name for rule in rule_list]
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4123): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rule_names_include(rule_names: list, expected_name1: str, expected_name2: str):
        """Then: Rule names include expected names."""
        assert expected_name1 in rule_names
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4129): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_rules_directory_created(tmp_path: Path):
        """Given: Test rules directory created."""
        rule_dir = tmp_path / 'rules'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4136): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_rule_data_with_optional_scanner(rule_name: str, scanner_config):
        """Given: Rule data with optional scanner."""
        rule_data = {'name': rule_name}
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4144): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_scanner_accessed(rule):
        """When: Rule scanner property accessed."""
        return rule.scanner
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4149): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_scanner_class_accessed(rule):
        """When: Rule scanner_class property accessed."""
        return rule.scanner_class
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4154): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_properties_match_expected(scanner, scanner_class, scanner_result):
        """Then: Scanner properties match expected."""
        if scanner_result is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4164): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_description_accessed(rule):
        """When: Rule description property accessed."""
        return rule.description
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4169): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_examples_accessed(rule):
        """When: Rule examples property accessed."""
        return rule.examples
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4174): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_instruction_accessed(rule):
        """When: Rule instruction property accessed."""
        return rule.instruction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4179): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_behavior_name_accessed(rule):
        """When: Rule behavior_name property accessed."""
        return rule.behavior_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4184): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_rule_properties_are_accessible(description, examples, instruction, behavior_name):
        """Then: Rule properties are accessible."""
        assert description is not None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4192): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_validation_scope_contains_all_expected(validation_scope: ValidationScope, expected_scope_contains: dict):
        """Then: ValidationScope contains all expected key-value pairs."""
        for key, value in expected_scope_contains.items():
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4198): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_nonexistent_rule_file_path(tmp_path: Path):
        """Given: Nonexistent rule file path."""
        return tmp_path / 'nonexistent_rule.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4203): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_rule_instantiation_raises_file_not_found_error(rule_file: Path):
        """When: Rule instantiation raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4209): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_complete_rule_data():
        """Given: Complete rule data."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4220): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scanner_loader_created():
        """Given: ScannerLoader created."""
        return ScannerLoader()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4225): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_valid_scanner_module_path():
        """Given: Valid scanner module path."""
        return 'agile_bot.bots.base_bot.src.actions.validate.scanners.code_scanner.CodeScanner'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4230): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scanner_name_for_test():
        """Given: Scanner name for test."""
        return 'code_scanner'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4235): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_bot_name_for_test():
        """Given: Bot name for test."""
        return 'story_bot'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4240): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_invalid_scanner_path():
        """Given: Invalid scanner path."""
        return 'pathlib.Path'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4245): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_nonexistent_scanner_path():
        """Given: Nonexistent scanner path."""
        return 'nonexistent.module.NonexistentScanner'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4250): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scanner_name_without_full_path():
        """Given: Scanner name without full module path."""
        return 'code_scanner'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4255): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_class_may_be_none_or_not_none(scanner_class):
        """Then: Scanner class may be None or not None."""
        assert scanner_class is None or scanner_class is not None
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4260): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_scanner_loader_loads_scanner_with_error(scanner_loader: ScannerLoader, scanner_path: str):
        """When: ScannerLoader load_scanner_with_error() called."""
        return scanner_loader.load_scanner_with_error(scanner_path)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4265): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scanner_loader_returns_error_tuple(result):
        """Then: ScannerLoader returns error tuple."""
        assert isinstance(result, tuple)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4277): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestLoadRulesCollection:
        """Story: Load Rules Collection (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4280): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_rules_loads_both_bot_level_and_behavior_specific_rules_when_instantiated_with_behavior(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules loads both bot-level and behavior-specific rules when instantiated with behavior
            GIVEN: Behavior with bot rules directory and behavior rules directory with rule files, and bot_paths
            WHEN: Rules instantiated with behavior and bot_paths
            THEN: Rules collection contains both bot-level and behavior-specific rules
            """
            # Given: Behavior with bot rules and behavior rules
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4310): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestFindRuleByName:
        """Story: Find Rule By Name (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4313): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_find_by_name_returns_rule_when_rule_exists(self, bot_directory, workspace_directory):
            """
            SCENARIO: Find by name returns rule when rule exists
            GIVEN: Rules collection with rule named 'test_rule'
            WHEN: find_by_name('test_rule') called
            THEN: Returns Rule object
            """
            # Given: Rules collection with rule
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4337): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_find_by_name_returns_none_when_rule_does_not_exist(self, bot_directory, workspace_directory):
            """
            SCENARIO: Find by name returns none when rule does not exist
            GIVEN: Rules collection without 'nonexistent_rule'
            WHEN: find_by_name('nonexistent_rule') called
            THEN: Returns None
            """
            # Given: Rules collection without 'nonexistent_rule'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4356): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_find_by_name_searches_both_bot_level_and_behavior_specific_rules(self, bot_directory, workspace_directory):
            """
            SCENARIO: Find by name searches both bot-level and behavior-specific rules
            GIVEN: Rules collection with bot-level and behavior-specific rules
            WHEN: find_by_name() called
            THEN: Searches both rule sets
            """
            # Given: Rules collection with both rule types
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4387): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestIterateRules:
        """Story: Iterate Rules (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4390): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_iterate_returns_all_rules_in_collection(self, bot_directory, workspace_directory):
            """
            SCENARIO: Iterate returns all rules in collection
            GIVEN: Rules collection with multiple rules
            WHEN: iterate() called
            THEN: Returns iterator with all rules
            """
            # Given: Rules collection with multiple rules
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4414): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_iterate_returns_empty_iterator_when_no_rules_loaded(self, bot_directory, workspace_directory):
            """
            SCENARIO: Iterate returns empty iterator when no rules loaded
            GIVEN: Rules collection with no rules
            WHEN: iterate() called
            THEN: Returns empty iterator
            """
            # Given: Rules collection with no rules
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4433): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_iterate_includes_both_bot_level_and_behavior_specific_rules(self, bot_directory, workspace_directory):
            """
            SCENARIO: Iterate includes both bot-level and behavior-specific rules
            GIVEN: Rules collection with bot-level and behavior-specific rules
            WHEN: iterate() called
            THEN: Iterator includes all rules from both sources
            """
            # Given: Rules collection with both rule types
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4460): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestLoadRuleFromFile:
        """Story: Load Rule From File (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4463): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_rule_loads_from_json_file_path(self, tmp_path):
            """
            SCENARIO: Rule loads from JSON file path
            GIVEN: Rule JSON file exists
            WHEN: Rule instantiated with file path
            THEN: Rule loads content from file
            """
            # Given: Rule JSON file exists
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4482): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_rule_loads_embedded_rule_from_validation_rules_json(self, tmp_path):
            """
            SCENARIO: Rule loads embedded rule from validation_rules.json
            GIVEN: validation_rules.json with embedded rule data
            WHEN: Rule instantiated with rule_content parameter
            THEN: Rule loads from provided content
            """
            # Given: Embedded rule data
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4499): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_rule_extracts_name_from_file_path(self, tmp_path):
            """
            SCENARIO: Rule extracts name from file path
            GIVEN: Rule file 'test_rule.json'
            WHEN: Rule instantiated
            THEN: Rule name property returns 'test_rule'
            """
            # Given: Rule file
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4516): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_rule_extracts_name_from_embedded_rule_data(self, tmp_path):
            """
            SCENARIO: Rule extracts name from embedded rule data
            GIVEN: Embedded rule data with name 'embedded_rule'
            WHEN: Rule instantiated with rule_content
            THEN: Rule name property returns 'embedded_rule'
            """
            # Given: Embedded rule data
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4535): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestLoadScannerForRule:
        """Story: Load Scanner For Rule (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4546): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_rule_scanner_properties_return_scanner_instance_or_none(self, scanner_config, scanner_result, scanner_class_result):
            """
            SCENARIO: Rule scanner properties return scanner instance or None
            GIVEN: Rule with different scanner configurations
            WHEN: scanner and scanner_class properties accessed
            THEN: Returns scanner instance and class type when loaded, None when not configured or not found
            """
            # Given: Rule with scanner configuration
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4565): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestGetRuleProperties:
        """Story: Get Rule Properties (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4568): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_rule_provides_access_to_config_properties(self, tmp_path):
            """
            SCENARIO: Rule provides access to config properties
            GIVEN: Rule loaded with complete rule config (description, examples, instruction, behavior_name)
            WHEN: Rule properties accessed (description, examples, instruction, behavior_name)
            THEN: All config properties are accessible
            """
            # Given: Rule loaded with complete config
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4589): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestCreateValidationScope:
        """Story: Create Validation Scope (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4604): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_validation_scope_created_with_different_parameter_combinations(self, parameters, expected_scope_contains):
            """
            SCENARIO: Validation scope created with different parameter combinations
            GIVEN: Parameters dict with scope configuration
            WHEN: ValidationScope instantiated with parameters
            THEN: ValidationScope scope property returns expected configuration
            """
            # Given: Parameters dict
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4619): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestLoadScannerClass:
        """Story: Load Scanner Class (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4622): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scanner_loader_loads_scanner_from_exact_module_path(self):
            """
            SCENARIO: Scanner loader loads scanner from exact module path
            GIVEN: Valid scanner module path
            WHEN: load_scanner() called with exact path
            THEN: Returns scanner class
            """
            # Given: Valid scanner module path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4639): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scanner_loader_loads_scanner_from_base_bot_scanners_directory(self):
            """
            SCENARIO: Scanner loader loads scanner from base_bot scanners directory
            GIVEN: Scanner name 'story_scanner'
            WHEN: load_scanner() called
            THEN: Tries base_bot/src/scanners/story_scanner.py
            """
            # Given: Scanner name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4656): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scanner_loader_loads_scanner_from_bot_specific_scanners_directory(self):
            """
            SCENARIO: Scanner loader loads scanner from bot-specific scanners directory
            GIVEN: Bot name 'story_bot' and scanner name
            WHEN: load_scanner() called
            THEN: Tries bot's src/scanners directory
            """
            # Given: Bot name and scanner name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4674): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scanner_loader_validates_scanner_inherits_from_scanner_base_class(self):
            """
            SCENARIO: Scanner loader validates scanner inherits from Scanner base class
            GIVEN: Scanner class that doesn't inherit from Scanner
            WHEN: load_scanner() called
            THEN: Returns None (validation fails)
            """
            # Given: Invalid scanner path (class that doesn't inherit from Scanner)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4697): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestInjectValidationRulesForValidateRulesAction:
        """Story: Inject Validation Rules for Validate Rules Action (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4700): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_action_uses_rules_collection_to_load_rules(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action uses Rules collection to load rules
            GIVEN: ValidateRulesAction with Behavior
            WHEN: Action executes
            THEN: Action uses Rules collection to load rules
            """
            # Given: Environment bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4716): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_action_uses_rule_class_to_access_rule_properties(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action uses Rule class to access rule properties
            GIVEN: ValidateRulesAction with loaded rules
            WHEN: Action accesses rule properties
            THEN: Uses Rule class properties
            """
            # Given: Environment bootstrapped with rules
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4733): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_action_uses_scanner_loader_to_load_scanner_classes(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action uses ScannerLoader to load scanner classes
            GIVEN: ValidateRulesAction with rules containing scanner paths
            WHEN: Action loads scanners
            THEN: Uses ScannerLoader service
            """
            # Given: Environment bootstrapped with rules containing scanner paths
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4750): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_action_uses_validation_scope_to_define_validation_scope(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action uses ValidationScope to define validation scope
            GIVEN: ValidateRulesAction with file paths or story graph
            WHEN: Action creates validation scope
            THEN: Uses ValidationScope class
            """
            # Given: Environment bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4768): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestLoadScannerClasses:
        """Story: Load Scanner Classes (Updated Existing Story) (Sub-epic: Validate Knowledge & Content Against Rules)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4771): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_action_uses_scanner_loader_service_to_load_scanner_classes(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action uses ScannerLoader service to load scanner classes
            GIVEN: Rule with scanner path
            WHEN: Scanner needs to be loaded
            THEN: Uses ScannerLoader service
            """
            # Given: Rule with scanner path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4787): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scanner_loader_loads_scanner_from_multiple_possible_paths(self):
            """
            SCENARIO: ScannerLoader loads scanner from multiple possible paths
            GIVEN: ScannerLoader with bot_name
            WHEN: load_scanner() called with scanner name
            THEN: Tries multiple path locations
            """
            # Given: ScannerLoader with bot_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4804): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scanner_loader_validates_scanner_inherits_from_scanner_base_class(self):
            """
            SCENARIO: ScannerLoader validates scanner inherits from Scanner base class
            GIVEN: ScannerLoader with scanner class
            WHEN: Scanner loaded
            THEN: Validates inheritance from Scanner
            """
            # Given: ScannerLoader with scanner class
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4997): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_execute_validate_code_files_action_with_files(bot_name, behavior, bot_directory, files):
        """Execute validation with files using ValidateRulesAction (ValidateCodeFilesAction was removed)."""
        from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5173): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestValidationWithAllParameterCombinations:
        """Tests for ValidationContext with all parameter combinations.
        
        Note: These tests pass behavior as a string to from_parameters which converts it to a Behavior object.
        The Behavior requires behavior.json to exist, so we use create_actions_workflow_json.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5370): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestInjectRulesIntoAIChatMessage:
        """Story: Inject Rules Into AI Chat Message - Load and format behavior rules for AI context."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5373): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_rules_action_loads_rules_for_behavior(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules action loads rules for behavior
            GIVEN: behavior is 'code' with rules defined
            WHEN: rules action executes
            THEN: rules are loaded from behavior rules directory
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5404): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
            
        def test_formatted_rules_digest_returns_compact_format(self, bot_directory, workspace_directory):
            """
            SCENARIO: formatted_rules_digest returns compact format
            GIVEN: behavior has 2 rules defined
            WHEN: formatted_rules_digest is called
            THEN: returns name + description format (not full examples)
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5444): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_rules_action_includes_message_in_context(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules action includes user message in context
            GIVEN: behavior is 'code' and message is 'help me refactor'
            WHEN: rules action executes with message
            THEN: instructions include user message
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5481): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_rules_action_outputs_to_ai_context_only(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules action outputs digest to AI context only (not display)
            GIVEN: behavior has rules defined
            WHEN: rules action executes
            THEN: digest appears in base_instructions but NOT display_content
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5524): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_rules_action_is_not_workflow_action(self, bot_directory, workspace_directory):
            """
            SCENARIO: Rules action is not part of workflow
            GIVEN: rules action is initialized
            WHEN: action properties are checked
            THEN: workflow property is False
            """
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:65): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    from agile_bot.bots.base_bot.src.scanners.test_scanner import TestScanner
    
    # ============================================================================
    # HELPER FUNCTIONS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:67): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:75): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # UNIFIED SCANNER ARCHITECTURE HELPERS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:77): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # UNIFIED SCANNER ARCHITECTURE HELPERS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:102): Useless comment: "# Create a rule file for testing" - delete it or improve the code instead

    ```python
        from pathlib import Path
        
        # Create a rule file for testing
        rule_file = bot_directory / 'behaviors' / behavior / '3_rules' / 'test_rule.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:672): Useless comment: "# Create behavior folder and behavior.json" - delete it or improve the code instead

    ```python
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
        # Create behavior folder and behavior.json
        create_actions_workflow_json(test_bot_dir, behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:865): Useless comment: "# Load state from file" - delete it or improve the code instead

    ```python
        return self.name
    
    # Load state from file
    def load_state(self):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1047): Useless comment: "# Return dict with code_files, using the actual file path" - delete it or improve the code instead

    ```python
            else:
                test_file.write_text(content, encoding='utf-8')
            # Return dict with code_files, using the actual file path
            return {'code_files': [str(test_file)]}
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1073): Useless comment: "# Create a default code file with common violations" - delete it or improve the code instead

    ```python
            # If no match found, create a default file with violations
            if bad_example is None:
                # Create a default code file with common violations
                default_content = '''class Order:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1240): Useless comment: "# Create a Python file with the bad example code (don't use " - delete it or improve the code instead

    ```python
        # If bad_example is a string (code), create a file from it
        if isinstance(bad_example, str):
            # Create a Python file with the bad example code (don't use "test" in name to avoid scanner skipping it)
            code_file = directory / 'bad_example_code.py'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1350): Useless comment: "# Create story graph in the workspace directory" - delete it or improve the code instead

    ```python
                setup_test_rules(repo_root, [rule_file_path], [rule_file_content])
            test_bot_dir = given_test_bot_directory_created(repo_root)
            # Create story graph in the workspace directory
            test_workspace_directory = test_bot_dir.parent / 'workspace'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1530): Useless comment: "# Create scenarios behavior.json and guardrails files (requi" - delete it or improve the code instead

    ```python
            docs_stories_dir = given_directory_created(workspace_directory, directory_type='docs_stories')
            story_graph_path = given_file_created(docs_stories_dir, 'story-graph.json', story_graph)
            # Create scenarios behavior.json and guardrails files (required for Behavior initialization)
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1947): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS FOR VALIDATE CODE FILES ACTION TESTS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1949): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS FOR VALIDATE CODE FILES ACTION TESTS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2000): Useless comment: "# Create minimal guardrails files" - delete it or improve the code instead

    ```python
        create_actions_workflow_json(bot_directory, behavior)
        
        # Create minimal guardrails files
        create_minimal_guardrails_files(bot_directory, behavior, bot_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2003): Useless comment: "# Create minimal story graph (required for validation)" - delete it or improve the code instead

    ```python
        create_minimal_guardrails_files(bot_directory, behavior, bot_name)
        
        # Create minimal story graph (required for validation)
        docs_stories_dir = workspace_directory / 'docs' / 'stories'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2118): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    from agile_bot.bots.base_bot.test.test_helpers import create_validation_rules
    
    # ============================================================================
    # SCANNER AND RULE LOADING HELPERS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2120): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # SCANNER AND RULE LOADING HELPERS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2185): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
        return created_files
    
    # ============================================================================
    # COMMON VALIDATORS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2187): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # COMMON VALIDATORS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2225): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
            return False
    
    # ============================================================================
    # FIXTURES
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2227): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # FIXTURES
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2247): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
                pass  # Ignore cleanup errors
    
    # ============================================================================
    # STORY: Track Activity for Validate Rules Action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2249): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Track Activity for Validate Rules Action
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2361): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Complete Validate Rules Action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2363): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Complete Validate Rules Action
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2542): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Discovers Scanners
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2544): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Discovers Scanners
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2602): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Run Scanners Against Knowledge Graph
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2604): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Run Scanners Against Knowledge Graph
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2675): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Handle Validate Rules Exceptions
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2677): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Handle Validate Rules Exceptions
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2713): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Validate Rules According to Scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2715): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Validate Rules According to Scope
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3445): Useless comment: "# Create a spy TestScanner that records what knowledge_graph" - delete it or improve the code instead

    ```python
            story_graph, story_graph_path, test_file, rule_file, action = given_test_file_scope_verification_complete_setup(bot_directory, workspace_directory)
            
            # Create a spy TestScanner that records what knowledge_graph it receives
            received_knowledge_graphs, SpyTestScanner = given_scanner_spy(scanner_type='test', record='knowledge_graph')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3456): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Test All Scanners
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3458): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Test All Scanners
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3678): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Run Scanners Against Test Code
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3680): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Run Scanners Against Test Code
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3762): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Run Scanners Against Code
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3764): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Run Scanners Against Code
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3829): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS - Domain Classes (Stories 9-16: Rules, Rule, ValidationScope, ScannerLoader)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3831): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Domain Classes (Stories 9-16: Rules, Rule, ValidationScope, ScannerLoader)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3837): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    from agile_bot.bots.base_bot.src.scanners.scanner_loader import ScannerLoader
    
    # ============================================================================
    # HELPER FUNCTIONS - Inject Validation Rules Story
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3839): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Inject Validation Rules Story
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3956): Useless comment: "# Create behavior folder and behavior.json" - delete it or improve the code instead

    ```python
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        bootstrap_env(bot_directory, workspace_directory)
        # Create behavior folder and behavior.json
        create_actions_workflow_json(bot_directory, behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4272): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # TEST CLASSES - Domain Classes (Stories 9-16: Rules, Rule, ValidationScope, ScannerLoader)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4274): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # TEST CLASSES - Domain Classes (Stories 9-16: Rules, Rule, ValidationScope, ScannerLoader)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4291): Useless comment: "# Create bot-level rule" - delete it or improve the code instead

    ```python
            behavior, bot_paths = given_behavior_with_bot_paths(bot_directory, workspace_directory, bot_name, behavior_name)
            
            # Create bot-level rule
            bot_rules_dir = given_bot_rules_directory_created(bot_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4692): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
        # test_scanner_loader_returns_none_when_scanner_class_not_found removed - exception handling test
        
    # ============================================================================
    # STORY: Inject Validation Rules for Validate Rules Action (Updated Existing Story)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4694): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Inject Validation Rules for Validate Rules Action (Updated Existing Story)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4824): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Perform Incremental Validation
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4826): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Perform Incremental Validation
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4901): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS - Incremental Validation
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4903): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Incremental Validation
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5009): Useless comment: "# Create Behavior object" - delete it or improve the code instead

    ```python
        create_minimal_guardrails_files(bot_directory, behavior, bot_name)
        
        # Create Behavior object
        bot_paths = BotPaths(bot_directory=bot_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5014): Useless comment: "# Create typed context with files scope" - delete it or improve the code instead

    ```python
        action = ValidateRulesAction(behavior=behavior_obj)
        
        # Create typed context with files scope
        file_paths = [str(f) for f in files]
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5137): Useless comment: "# Create behavior.json first" - delete it or improve the code instead

    ```python
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
            
            # Create behavior.json first
            create_actions_workflow_json(bot_directory, 'code')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5140): Useless comment: "# Create story graph" - delete it or improve the code instead

    ```python
            create_actions_workflow_json(bot_directory, 'code')
            
            # Create story graph
            given_environment_bootstrapped_with_story_graph(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5157): Useless comment: "# Create behavior.json first" - delete it or improve the code instead

    ```python
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
            
            # Create behavior.json first
            create_actions_workflow_json(bot_directory, 'code')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5160): Useless comment: "# Create story graph" - delete it or improve the code instead

    ```python
            create_actions_workflow_json(bot_directory, 'code')
            
            # Create story graph
            given_environment_bootstrapped_with_story_graph(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5364): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Inject Rules Into AI Chat Message
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5367): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # STORY: Inject Rules Into AI Chat Message
    # Epic: Validate with Rules
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TriggerTestSetup:
        """Helper class to set up bot with trigger words for testing."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:54): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def setup_bot(self):
            """Set up bot with all behaviors and actions."""
            workspace_root = self.bot_directory.parent.parent.parent
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:74): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _setup_behavior_folders_and_knowledge_graphs(self, workspace_root: Path):
            """Set up behavior folders with behavior.json files and knowledge graph configs."""
            from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:89): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _create_knowledge_graph_config(self, behavior_dir: Path):
            """Create knowledge graph folder and config files for a behavior."""
            kg_dir = behavior_dir / 'content' / 'knowledge_graph'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _create_story_graph_file(self):
            """Create story graph file in workspace for validate action."""
            stories_dir = self.workspace_directory / 'docs' / 'stories'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:113): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def add_bot_triggers(self, patterns: list):
            """Add bot-level trigger words."""
            # workspace_root is bot_directory's parent.parent.parent (tmp_path)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:120): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def add_behavior_triggers(self, behavior_patterns: dict):
            """Add behavior-level trigger words.
            
            
            """
            # workspace_root is bot_directory's parent.parent.parent (tmp_path)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:131): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def add_action_triggers(self, behavior: str, action: str, patterns: list):
            """Add action-level trigger words."""
            # workspace_root is bot_directory's parent.parent.parent (tmp_path)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:138): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def add_all_action_triggers(self, template: str):
            """Add action triggers for all behavior/action combinations using template.
            
            
            """
            for behavior in self.behaviors:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:149): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def create_workflow_state(self, current_behavior: str, current_action: str):
            """Create workflow state file."""
            return create_workflow_state_file(
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:161): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    class TriggerRouterTestHelper:
        
        """Helper class for testing trigger routing and CLI execution."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:173): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _create_router_and_match(self, trigger_message: str, current_behavior: str = None, current_action: str = None):
            """Helper: Create router and match trigger."""
            # Patch get_python_workspace_root() to return the test's tmp_path where triggers are created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:201): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _create_cli_and_execute(self, route: dict, trigger_message: str):
            """Helper: Create CLI instance and execute route."""
            from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:225): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def match_and_execute(self, trigger_message: str, current_behavior: str = None, current_action: str = None):
            """Match trigger and execute via CLI.
            
            Creates fresh router and CLI instances for each call to avoid state leakage.
            
            
            """
            route = self._create_router_and_match(trigger_message, current_behavior, current_action)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:239): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def assert_route(self, route, expected_bot: str, expected_behavior: str, expected_action: str, expected_type: str):
            """Assert route matches expected values."""
            then_route_matches_expected(route, expected_bot, expected_behavior, expected_action, expected_type)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:243): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def assert_cli_result(self, result, expected_behavior: str, expected_action: str):
            """Assert CLI result matches expected values."""
            then_cli_result_matches_expected(result, expected_behavior, expected_action)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:254): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def create_base_action_instructions_duplicate_removed(bot_directory: Path, action: str) -> Path:
        """Helper: Create base action instructions file in bot directory.
        
        Action folders no longer use numbered prefixes.
        """
        from agile_bot.bots.base_bot.test.test_helpers import get_test_base_actions_dir
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:273): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def create_bot_trigger_words(workspace: Path, bot_name: str, patterns: list) -> Path:
        """Helper: Create bot-level trigger words file."""
        trigger_dir = workspace / 'agile_bot' / 'bots' / bot_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:282): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def create_behavior_trigger_words(workspace: Path, bot_name: str, behavior: str, patterns: list) -> Path:
        """Helper: Create behavior-level trigger words in behavior.json (new format)."""
        bot_dir = workspace / 'agile_bot' / 'bots' / bot_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:302): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def create_action_trigger_words(workspace: Path, bot_name: str, behavior: str, action: str, patterns: list) -> Path:
        """Helper: Create action-level trigger words file."""
        action_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:312): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_verify_route_and_result_for_bot_only(setup, helper, behavior, action, route, result, trigger_message):
        """Then: Verify route and result for bot-only trigger."""
        helper.assert_route(route, setup.bot_name, behavior, action, 'bot_only')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:318): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_verify_route_and_result_for_bot_and_behavior(setup, helper, behavior, action, route, result, trigger_message):
        """Then: Verify route and result for bot and behavior trigger."""
        helper.assert_route(route, setup.bot_name, behavior, action, 'bot_and_behavior')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:324): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_verify_route_and_result_for_explicit_action(setup, helper, behavior, action, route, result):
        """Then: Verify route and result for explicit action trigger."""
        helper.assert_route(route, setup.bot_name, behavior, action, 'bot_behavior_action')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:330): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_verify_close_trigger_route_and_result(setup, route, result):
        """Then: Verify close trigger route and result."""
        assert route is not None, f"Failed for {setup.bot_name}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:338): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_setup_action_triggers_for_all_behaviors(setup, action_trigger_templates: dict):
        """When: Setup action triggers for all behaviors."""
        for behavior in setup.behaviors:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:345): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_trigger_router_helper_and_message(setup, trigger_message: str):
        """Given step: Create trigger router helper and set trigger message."""
        # Bootstrap environment before creating helper (required for BotPaths)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:366): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_all_combinations_tested(cli, behaviors, actions, **params):
        """
        Consolidated function for testing all behavior/action combinations.
        Replaces: when_test_all_behavior_action_combinations
        
        Args:
            cli: CLI instance or setup object
            behaviors: List of behaviors to test
            actions: List of actions to test
            **params: Additional parameters:
                - setup: Setup object (if cli is not a setup object)
                - helper: Trigger router helper
                - trigger_message: Trigger message to test
                - verify_func: Verification function
                - current_behavior: Current behavior (if None, tests all)
                - current_action: Current action (if None, tests all)
        """
        setup = params.get('setup', cli)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:403): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_triggers_dict(behavior=None, triggers=None):
        """
        Consolidated function for creating behavior triggers dictionary.
        Replaces: given_standard_behavior_triggers_dict
        
        Args:
            behavior: Behavior name (if None, returns all standard behaviors)
            triggers: Custom triggers dict (if None, uses standard triggers)
        
        Returns:
            Dictionary mapping behavior names to trigger strings
        """
        if triggers is not None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:436): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for INVOKE CLI setup.
        Replaces: given_bot_setup_with_triggers, given_bot_setup_with_behavior_triggers
        
        Args:
            setup_type: Type of setup ('bot_with_triggers')
            bot_directory: Bot directory path
            **setup_params: Additional parameters:
                - workspace_directory: Workspace directory path (required)
                - behaviors: List of behavior names (optional, defaults to standard behaviors)
                - triggers: Dict of triggers (for 'bot_with_triggers' setup_type)
                - behavior_triggers: Dict mapping behavior names to trigger patterns
        
        Returns:
            TriggerTestSetup object
        """
        workspace_directory = setup_params.get('workspace_directory')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:475): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_action_trigger_templates_dict():
        """Given: Action trigger templates dictionary."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:484): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_bot_setup_with_action_triggers(bot_directory: Path, workspace_directory: Path, action_trigger_templates: dict):
        """Given: Bot setup with action triggers."""
        return TriggerTestSetup(bot_directory, workspace_directory).setup_bot()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:488): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_cli_created_with_mock_bot(mock_bot):
        """When: CLI created with mock bot."""
        from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:493): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_triggers_dictionary():
        """Given step: Create behavior triggers dictionary."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:506): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_test_all_behaviors_with_triggers(setup, helper, behavior_triggers: dict, verify_func):
        """When step: Test all behaviors with their triggers."""
        for behavior, trigger_message in behavior_triggers.items():
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:518): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_action_trigger_templates_dictionary():
        """Given step: Create action trigger templates dictionary."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:528): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_test_all_behaviors_with_action_templates(setup, helper, action_trigger_templates: dict, verify_func):
        """When step: Test all behaviors with action trigger templates."""
        for behavior in setup.behaviors:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:540): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_base_action_instructions(bot_directory: Path):
        """Helper: Create base action instructions in bot directory."""
        actions = ['initialize_workspace', 'gather_context', 'decide_planning_criteria', 
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:547): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def setup_bot_for_testing(workspace_root: Path, bot_name: str, behaviors: list):
        """Helper: Set up complete bot structure for testing.
        
        
        """
        bot_dir = workspace_root / 'agile_bot' / 'bots' / bot_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:564): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    @pytest.fixture
    def workspace_root(tmp_path):
        """Fixture: Temporary workspace directory."""
        workspace = tmp_path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:573): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestDetectTriggerWordsThroughExtension:
        """Story: Detect Trigger Words Through Extension (Sub-epic: Invoke CLI)"""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:576): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_trigger_bot_only_no_behavior_or_action_specified(self, bot_directory, workspace_directory):
            """
            SCENARIO: Trigger bot only (no behavior or action specified)
            GIVEN: user types message containing trigger words
            AND: bot is at specific behavior and action from workflow state
            WHEN: Extension intercepts user message
            THEN: Extension identifies target bot from trigger patterns
            AND: Extension routes to bot using current behavior and action from state
            AND: CLI executes current behavior and action
            """
            # Arrange: Set up bot with bot-level triggers
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:601): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_trigger_bot_and_behavior_no_action_specified(self, bot_directory, workspace_directory):
            """
            SCENARIO: Trigger bot and behavior (no action specified)
            GIVEN: user types message containing behavior-specific trigger words
            AND: behavior is at specific action from workflow state
            WHEN: Extension intercepts user message
            THEN: Extension identifies bot and behavior from trigger patterns
            AND: Extension routes to behavior using current action from state
            AND: CLI executes behavior with current action
            """
            # Arrange: Set up bot with behavior-level triggers
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:621): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_trigger_bot_behavior_and_action_explicitly(self, bot_directory, workspace_directory):
            """
            SCENARIO: Trigger bot, behavior, and action explicitly
            GIVEN: user types message containing action-specific trigger words
            WHEN: Extension intercepts user message
            THEN: Extension identifies bot, behavior, and action from trigger patterns
            AND: Extension routes directly to specified action
            AND: CLI executes specified action
            """
            # Arrange: Set up bot with action-level triggers for all combinations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:642): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_trigger_close_current_action(self, bot_directory, workspace_directory):
            """
            SCENARIO: Trigger close current action
            GIVEN: user types message containing close trigger words
            AND: bot is at specific behavior and action from workflow state
            WHEN: Extension intercepts user message
            THEN: Extension identifies close action from trigger patterns
            AND: Extension routes to close_current_action
            AND: CLI closes current action and advances workflow
            """
            # Arrange: Set up bot with close trigger words
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:674): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_mock_bot_created(tmp_path: Path, bot_name: str = 'test_bot'):
        """Given: Mock bot created with proper Path attributes including bot_paths."""
        from unittest.mock import Mock
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:697): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_cli_infers_parameter_description_for_unknown_command(cli):
        """When: CLI infers parameter description for unknown command."""
        from agile_bot.bots.base_bot.src.cli.base_bot_cli import BaseBotCli
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:707): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestCLIExceptions:
        """Tests for CLI exception handling - no fallbacks."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:710): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_cli_returns_generic_description_for_unknown_command(self, tmp_path):
            """
            SCENARIO: CLI returns generic description when parameter description cannot be inferred
            GIVEN: Mock bot is created
            WHEN: CLI is created with mock bot
            AND: Inferring parameter description for unknown command
            THEN: Generic description is returned (graceful fallback)
            """
            # Given: Mock bot is created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:741): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_config_with_trigger_patterns(patterns: list, priority: int = 0):
        """Given: Behavior with trigger patterns (BehaviorConfig merged into Behavior)."""
        behavior_config = Mock(spec=Behavior)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:751): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_config_with_list_triggers(patterns: list):
        """Given: Behavior with list trigger words (BehaviorConfig merged into Behavior)."""
        behavior_config = Mock(spec=Behavior)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:758): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_config_with_no_triggers():
        """Given: Behavior with no trigger words (BehaviorConfig merged into Behavior)."""
        behavior_config = Mock(spec=Behavior)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:765): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_trigger_words_instantiated(behavior_config, behavior=None):
        """When: TriggerWords instantiated."""
        # TriggerWords only takes behavior_config, not behavior parameter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:771): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_matches_called(trigger_words: TriggerWords, text: str):
        """When: matches() called."""
        return trigger_words.matches(text)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:776): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_priority_accessed(trigger_words: TriggerWords):
        """When: priority property accessed."""
        return trigger_words.priority
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:781): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_priority_is(result: int, expected: int):
        """Then: Priority is expected value."""
        assert result == expected
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:786): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_matches_returns(result: bool, expected: bool):
        """Then: Matches returns expected value."""
        assert result == expected
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:795): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestGetTriggerPriority:
        """Story: Get Trigger Priority (Sub-epic: Invoke CLI)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:798): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
    def given_behavior_config_from_trigger_config(trigger_config):
        """Given: BehaviorConfig from trigger configuration."""
        if isinstance(trigger_config, dict):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:809): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestGetTriggerPriority:
        """Story: Get Trigger Priority (Sub-epic: Invoke CLI)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:820): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_priority_property_returns_configured_priority_or_zero(self, trigger_config, expected_priority):
            """
            SCENARIO: Priority property returns configured priority or zero
            GIVEN: BehaviorConfig with different trigger configurations
            WHEN: priority property accessed
            THEN: Returns configured priority when available, otherwise returns 0
            """
            # Given: BehaviorConfig with trigger configuration
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:838): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestMatchTextAgainstTriggers:
        """Story: Match Text Against Triggers (Sub-epic: Invoke CLI)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:841): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_returns_true_when_text_matches_any_pattern(self):
            """
            SCENARIO: Matches returns true when text matches any pattern
            GIVEN: BehaviorConfig with multiple patterns ['test', 'pattern', 'xyz']
            WHEN: matches() called with text 'This is a test'
            THEN: Returns True
            """
            # Given: BehaviorConfig with multiple patterns
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:858): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_returns_false_when_no_patterns_match(self):
            """
            SCENARIO: Matches returns false when no patterns match
            GIVEN: BehaviorConfig with patterns ['xyz', 'abc']
            WHEN: matches() called with text 'This is a test'
            THEN: Returns False
            """
            # Given: BehaviorConfig with patterns
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:875): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_returns_false_when_no_triggers_configured(self):
            """
            SCENARIO: Matches returns false when no triggers configured
            GIVEN: BehaviorConfig with no triggers
            WHEN: matches() called with text 'This is a test'
            THEN: Returns False
            """
            # Given: BehaviorConfig with no triggers
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:892): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_works_with_list_trigger_format(self):
            """
            SCENARIO: Matches works with list trigger format
            GIVEN: BehaviorConfig with list triggers ['test', 'pattern']
            WHEN: matches() called with text 'This is a test'
            THEN: Returns True
            """
            # Given: BehaviorConfig with list triggers
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:909): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_checks_all_patterns_until_match_found(self):
            """
            SCENARIO: Matches checks all patterns until match found
            GIVEN: BehaviorConfig with patterns ['xyz', 'abc', 'test']
            WHEN: matches() called with text 'This is a test'
            THEN: Returns True (third pattern matches)
            """
            # Given: BehaviorConfig with patterns
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:926): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_handles_regex_patterns(self):
            """
            SCENARIO: Matches handles regex patterns
            GIVEN: BehaviorConfig with regex pattern 'test.*pattern'
            WHEN: matches() called with text 'test this pattern'
            THEN: Returns True
            """
            # Given: BehaviorConfig with regex pattern
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:943): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_is_case_insensitive(self):
            """
            SCENARIO: Matches is case insensitive
            GIVEN: BehaviorConfig with pattern 'TEST'
            WHEN: matches() called with text 'this is a test'
            THEN: Returns True (case insensitive)
            """
            # Given: BehaviorConfig with pattern
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:960): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_matches_handles_invalid_regex_patterns_by_falling_back_to_literal(self):
            """
            SCENARIO: Matches handles invalid regex patterns by falling back to literal
            GIVEN: BehaviorConfig with invalid regex pattern '['
            WHEN: matches() called with text 'This contains [ bracket'
            THEN: Returns True (fallback to literal matching)
            """
            # Given: BehaviorConfig with invalid regex pattern
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1013): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def simulate_cli_invocation(cli_args_list):
        """Simulate CLI invocation and return args plus parsed params dict for tests.
        
        The new CliParameterParser returns (args, remaining_args_list), but tests 
        expect a params dict. This helper builds a params dict for backward compatibility.
        """
        original_argv = sys.argv
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1408): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_action_with_context_class(action_class):
        """Given: An action class with its declared context_class."""
        from agile_bot.bots.base_bot.src.actions.action_context import ActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1414): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_scope_config_for_files(file_paths: list, exclude_patterns: list = None):
        """Given: A typed Scope targeting specific files."""
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1424): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_validate_action_context(scope=None, skip_cross_file=False):
        """Given: A typed ValidateActionContext with optional parameters."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1433): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_context_built_from_cli_args(cli_args: list):
        """When: CLI arguments are parsed and context is built."""
        from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1446): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_parser_generator_generates_for_action(action_class):
        """When: Parser generator creates parser code for action's context class."""
        from agile_bot.bots.base_bot.src.cli.cli_parser_generator import CliParserGenerator
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1457): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_context_is_typed_with_values(context, expected_type, **expected_values):
        """Then: Context is of expected type with expected attribute values."""
        assert isinstance(context, expected_type), f"Expected {expected_type}, got {type(context)}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1465): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_generated_parser_has_arguments(parser_code: str, expected_args: list):
        """Then: Generated parser code includes expected CLI arguments."""
        for arg in expected_args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1471): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scope_is_typed_config(scope, expected_type, expected_value: list):
        """Then: Scope is a typed Scope with expected type and value."""
        from agile_bot.bots.base_bot.src.actions.action_context import Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1483): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestCliTypeSafeActionContext:
        """Story: CLI Passes Typed ActionContext to Actions
        
        When CLI receives parameters, it builds a typed ActionContext
        and passes it to the action's execute() method.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1490): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_validate_action_declares_typed_context_class(self):
            """
            SCENARIO: ValidateRulesAction declares ValidateActionContext as its context_class
            GIVEN: ValidateRulesAction class
            WHEN: Inspecting its context_class attribute
            THEN: context_class is ValidateActionContext
            """
            from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1506): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_build_action_declares_scope_context_class(self):
            """
            SCENARIO: BuildKnowledgeAction declares ScopeActionContext as its context_class
            GIVEN: BuildKnowledgeAction class
            WHEN: Inspecting its context_class attribute
            THEN: context_class is ScopeActionContext
            """
            from agile_bot.bots.base_bot.src.actions.build.build_action import BuildKnowledgeAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1522): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_clarify_action_declares_clarify_context_class(self):
            """
            SCENARIO: ClarifyContextAction declares ClarifyActionContext as its context_class
            GIVEN: ClarifyContextAction class
            WHEN: Inspecting its context_class attribute
            THEN: context_class is ClarifyActionContext
            """
            from agile_bot.bots.base_bot.src.actions.clarify.clarify_action import ClarifyContextAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1538): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_strategy_action_declares_strategy_context_class(self):
            """
            SCENARIO: StrategyAction declares StrategyActionContext as its context_class
            GIVEN: StrategyAction class
            WHEN: Inspecting its context_class attribute
            THEN: context_class is StrategyActionContext
            """
            from agile_bot.bots.base_bot.src.actions.strategy.strategy_action import StrategyAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1555): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestCliContextBuilderParsesTypedContext:
        """Story: CliContextBuilder Parses CLI Args into Typed Context
        
        When CLI arguments are parsed, CliContextBuilder creates a typed
        ActionContext with proper attribute values.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1562): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_context_builder_creates_validate_context_from_cli_args(self):
            """
            SCENARIO: CliContextBuilder creates ValidateActionContext from CLI args
            GIVEN: CLI args with --skip-cross-file flag
            WHEN: Context is built from CLI args
            THEN: Context is ValidateActionContext with skip_cross_file=True
            """
            from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1580): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_context_builder_creates_typed_scope_config(self):
            """
            SCENARIO: CliContextBuilder creates typed Scope from JSON scope arg
            GIVEN: CLI args with --scope as JSON for files
            WHEN: Context is built from CLI args
            THEN: Context.scope is Scope with type=FILES and value list
            """
            from agile_bot.bots.base_bot.src.actions.action_context import (
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1601): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_context_builder_handles_all_validate_parameters(self):
            """
            SCENARIO: CliContextBuilder handles all ValidateActionContext parameters
            GIVEN: CLI args with scope, skip-cross-file, and all-files
            WHEN: Context is built from CLI args
            THEN: All parameters are correctly set in typed context
            """
            from agile_bot.bots.base_bot.src.actions.action_context import ValidateActionContext
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1628): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestCliParserGeneratorCreatesActionParsers:
        """Story: CLI Parser Generator Creates Type-Safe Parsers
        
        When parser generator runs, it creates argument parsers
        that match each action's context_class fields.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1635): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_parser_generator_creates_validate_parser_with_correct_args(self):
            """
            SCENARIO: Parser generator creates parser for ValidateActionContext
            GIVEN: ValidateRulesAction with ValidateActionContext
            WHEN: Parser generator generates parser code
            THEN: Generated code includes --scope, --skip-cross-file, --all-files args
            """
            from agile_bot.bots.base_bot.src.actions.validate.validate_action import ValidateRulesAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1656): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_parser_generator_creates_scope_parser_for_build_action(self):
            """
            SCENARIO: Parser generator creates parser for ScopeActionContext
            GIVEN: BuildKnowledgeAction with ScopeActionContext
            WHEN: Parser generator generates parser code
            THEN: Generated code includes --scope arg
            """
            from agile_bot.bots.base_bot.src.actions.build.build_action import BuildKnowledgeAction
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:36): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    from agile_bot.bots.base_bot.src.cli.cli_parameter_parser import CliParameterParser
    
    # ============================================================================
    # HELPER CLASSES
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:38): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER CLASSES
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:247): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:249): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:284): Useless comment: "# Create or update behavior.json file with trigger words (RE" - delete it or improve the code instead

    ```python
        """Helper: Create behavior-level trigger words in behavior.json (new format)."""
        bot_dir = workspace / 'agile_bot' / 'bots' / bot_name
        # Create or update behavior.json file with trigger words (REQUIRED after refactor)
        behavior_dir = bot_dir / 'behaviors' / behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:292): Useless comment: "# Update trigger_words in behavior.json (router reads from b" - delete it or improve the code instead

    ```python
        behavior_data = json.loads(behavior_file.read_text())
        
        # Update trigger_words in behavior.json (router reads from behavior.json now)
        behavior_data['trigger_words'] = {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:558): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # FIXTURES
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:560): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # FIXTURES
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:568): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
        return workspace
    
    # ============================================================================
    # TEST CLASSES - Detect Trigger Words Through Extension
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:570): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # TEST CLASSES - Detect Trigger Words Through Extension
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:669): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # EXCEPTION HANDLING TESTS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:671): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # EXCEPTION HANDLING TESTS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:687): Useless comment: "# Create the CLI script path that CliHelpGenerator expects" - delete it or improve the code instead

    ```python
        mock_bot.bot_paths = mock_bot_paths
        
        # Create the CLI script path that CliHelpGenerator expects
        src_dir = bot_dir / 'src'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:731): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS - Domain Classes (Stories 1-2: TriggerWords)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:733): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Domain Classes (Stories 1-2: TriggerWords)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:790): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # TEST CLASSES - Domain Classes (Stories 1-2: TriggerWords)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:792): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # TEST CLASSES - Domain Classes (Stories 1-2: TriggerWords)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:977): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # CLI PARAMETER PARSING TESTS (Infrastructure)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:979): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # CLI PARAMETER PARSING TESTS (Infrastructure)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1403): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS - CLI Type Safety (Typed ActionContext)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1405): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - CLI Type Safety (Typed ActionContext)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1478): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # TEST CLASSES - CLI Type Safety (Typed ActionContext)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:1480): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # TEST CLASSES - CLI Type Safety (Typed ActionContext)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:55): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def _create_behavior(bot_directory: Path, bot_name: str, behavior_name: str, workspace_directory: Path = None):
        """Create a real Behavior object for testing."""
        from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:75): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_bot_directory_created(repo_root_or_tmp_path, bot_name: str = 'test_story_bot'):
        """Given: Test bot directory created."""
        test_bot_dir = repo_root_or_tmp_path / 'agile_bot' / 'bots' / bot_name
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:83): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_build_outputs():
        """Given: Build knowledge action outputs."""
        return {'knowledge_items_count': 12, 'file_path': 'knowledge.json'}
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:87): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_build_duration():
        """Given: Build knowledge action duration."""
        return 420
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:91): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_base_and_behavior_instructions_setup(bot_directory, workspace_directory, bot_name, behavior, action):
        """Given: Base and behavior-specific instructions setup."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:113): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_base_instructions_only_setup(bot_directory, workspace_directory, bot_dir, behavior, action):
        """Given: Base instructions only setup (no behavior-specific instructions)."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:129): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_base_instructions_text_extracted(instructions):
        """Given: Base instructions text extracted from instructions dict."""
        return '\n'.join(instructions.get('base_instructions', []))
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:133): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_story_map_created(bot=None, test_instance=None, bot_directory=None):
        """
        Consolidated function for creating story map.
        Replaces: when_story_map_created_from_bot, when_story_map_created_from_mock_bot
        
        Args:
            bot: Bot instance (if provided, use directly)
            test_instance: Test instance (if bot not provided, use to create mock bot)
            bot_directory: Bot directory (if bot not provided, use with test_instance)
        """
        if bot is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:234): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestTrackActivityForBuildKnowledgeAction:
        """Story: Track Activity for Build Knowledge Action - Tests activity tracking for build."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:256): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestProceedToRenderOutput:
        """Story: Proceed To Render Output - Tests transition to render_output action."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:259): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_seamless_transition_from_build_to_validate(self, bot_directory, workspace_directory):
            """
            SCENARIO: Seamless Transition From Build Knowledge To Validate Rules
            """
            # Given: Bot directory and workspace directory are set up
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:268): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_workflow_state_captures_build_completion(self, bot_directory, workspace_directory):
            """
            SCENARIO: Workflow State Captures Build Knowledge Completion
            """
            # Given: Bot directory and workspace directory are set up
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:277): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_setup(setup_type, bot_directory, **setup_params):
        """
        Consolidated function for BUILD KNOWLEDGE setup.
        Replaces: given_knowledge_graph_setup, given_knowledge_graph_setup_complete,
        given_knowledge_graph_config_and_template_created, given_knowledge_graph_directory_structure_created,
        given_knowledge_graph_directory_for_prioritization, given_environment_and_knowledge_graph_setup
        
        Args:
            setup_type: Type of setup ('knowledge_graph', 'knowledge_graph_complete', 'config_and_template',
                        'directory_structure', 'directory_for_prioritization', 'environment_and_kg')
            bot_directory: Bot directory path
            **setup_params: Additional parameters (behavior, template_name, workspace_directory, kg_dir)
        
        Returns:
            kg_dir Path or tuple depending on setup_type
        """
        behavior = setup_params.get('behavior', 'build')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:341): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    # Backward-compatible aliases for consolidated functions
    def given_knowledge_graph_directory_structure_created(bot_directory, behavior='build'):
        """Alias for given_setup('directory_structure', ...) - backward compatibility."""
        return given_setup('directory_structure', bot_directory, behavior=behavior)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:346): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_knowledge_graph_config_and_template_created(kg_dir):
        """Alias for given_setup('config_and_template', ...) - backward compatibility."""
        # This one needs the bot_directory, so we work backward from kg_dir
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:369): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_base_instructions_copied_to_bot_directory(bot_directory: Path, action_name: str) -> Path:
        """Given: Base instructions copied to bot directory."""
        from agile_bot.bots.base_bot.test.test_helpers import get_base_actions_dir, get_test_base_actions_dir
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:390): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_behavior_specific_instructions_created(bot_directory: Path, behavior: str, action: str, kg_dir: Path) -> Path:
        """Given: Behavior-specific instructions created."""
        behavior_instructions_file = kg_dir / 'instructions.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:407): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_base_instructions_present(merged_instructions: dict):
        """Then: Base instructions present."""
        base_instructions_list = merged_instructions['base_instructions']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:416): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_behavior_instructions_present(merged_instructions: dict):
        """Then: Behavior instructions present."""
        behavior_instructions_list = merged_instructions['behavior_instructions']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:423): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_behavior_instructions_contain_action(merged_instructions: dict, behavior: str, action: str):
        """Then: Behavior instructions contain action."""
        behavior_instructions_list = merged_instructions['behavior_instructions']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:437): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_nodes_match_expected_structure(nodes):
        """Then: Nodes match expected structure."""
        assert len(nodes) == 4
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:449): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_location_matches(item, type=None, field=None):
        """
        Consolidated function for checking map location correctness.
        Replaces: then_epic_map_location_correct, then_sub_epic_map_location_correct,
        then_story_map_location_correct, then_scenario_map_location_correct,
        then_scenario_outline_map_location_correct
        
        Args:
            item: Epic, SubEpic, Story, Scenario, or ScenarioOutline instance
            type: Type hint ('epic', 'sub_epic', 'story', 'scenario', 'scenario_outline') - auto-detected if None
            field: Optional field name to check (e.g., 'sequential_order', 'sizing')
        """
        # Auto-detect type if not provided
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:518): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_map_matches(story_map, epic=None):
        """
        Consolidated function for checking story map matches expected epic.
        Replaces: then_story_map_contains_test_epic, then_epics_contain_single_build_epic, then_epics_match
        
        Args:
            story_map: StoryMap instance or epics list
            epic: Epic name to check for. None = check for single epic (defaults to "Test Epic" for story_map, "Build Knowledge" for epics list)
        
        Returns:
            The epic if checking epics list, None otherwise
        """
        # Handle both story_map and epics list
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:564): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_instructions_indicate_updating_existing_file(instructions: dict, expected_output: str):
        """Then: Instructions indicate updating existing file."""
        assert 'knowledge_graph_config' in instructions
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:571): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_variables_for_exploration() -> tuple[str, str]:
        """Given: Test variables for exploration behavior."""
        bot_name = 'story_bot'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:578): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_variables_for_shape_build() -> tuple[str, str, str]:
        """Given: Test variables for shape build."""
        bot_name = 'test_bot'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:590): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_template_variables_test_setup(bot_directory: Path, workspace_directory: Path) -> tuple:
        """Given: Complete setup for template variables test.
        
        Sets up all prerequisites for testing template variable replacement:
        - Test variables (bot_name, behavior, action)
        - Environment bootstrap
        - Base instructions
        - Knowledge graph directory structure
        - Behavior-specific instructions
        - Behavior main instructions
        - Knowledge graph config and template
        - Knowledge graph template with schema
        - Validation rules
        
        
        """
        bot_name, behavior, action = given_test_variables_for_shape_build()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:637): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_test_variables_for_prioritization() -> tuple[str, str]:
        """Given: Test variables for prioritization behavior."""
        bot_name = 'story_bot'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:654): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_graph_updated_with_increments(instructions: dict, story_graph_path: Path):
        """Then: Story graph updated with increments."""
        assert story_graph_path.exists()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:666): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_epic_children_retrieved(parent, return_both=False):
        """
        Consolidated function for retrieving children from epic/sub-epic/story-group.
        Replaces: when_sub_epic_and_story_group_retrieved, when_epic_children_retrieved,
        when_sub_epic_children_retrieved, when_story_group_stories_retrieved
        
        Args:
            parent: Epic, SubEpic, or StoryGroup instance
            return_both: If True and parent is Epic, returns (sub_epic, story_group) tuple
        
        Returns:
            List of children, or (sub_epic, story_group) tuple if return_both=True
        """
        if return_both and hasattr(parent, 'children') and len(parent.children) > 0:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:688): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_children_contain_single_sub_epic(children, expected_name: str = "Load Story Graph"):
        """Then: Children contain single sub epic."""
        assert len(children) == 1
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:696): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_children_contain_single_story_group(children):
        """Then: Children contain single story group."""
        assert len(children) == 1
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:703): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_stories_contain_single_story(stories, expected_name: str = "Load Story Graph Into Memory"):
        """Then: Stories contain single story."""
        assert len(stories) == 1
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:713): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_has_expected_properties(story):
        """Then: Story has expected properties."""
        assert story.name == "Load Story Graph Into Memory"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:723): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_story_scenarios_retrieved(story):
        """When: Story scenarios retrieved."""
        return story.scenarios
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:728): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scenarios_contain_expected_scenarios(scenarios):
        """Then: Scenarios contain expected scenarios."""
        assert len(scenarios) == 2
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:740): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scenario_has_expected_properties(scenario):
        """Then: Scenario has expected properties."""
        assert scenario.name == "Story graph file exists"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:751): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_story_scenario_outlines_retrieved(story):
        """When: Story scenario outlines retrieved."""
        return story.scenario_outlines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:756): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scenario_outlines_contain_expected_outline(scenario_outlines):
        """Then: Scenario outlines contain expected outline."""
        assert len(scenario_outlines) == 1
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:765): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_scenario_outline_has_expected_examples(scenario_outline):
        """Then: Scenario outline has expected examples."""
        assert len(scenario_outline.examples_columns) == 2
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:778): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_build_scope_instantiated(parameters: dict, bot_paths=None):
        """When: BuildScope instantiated with parameters."""
        from agile_bot.bots.base_bot.src.actions.build.build_scope import BuildScope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:784): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_build_scope_contains(build_scope, expected_key: str, expected_value):
        """Then: BuildScope contains expected key-value."""
        assert expected_key in build_scope.scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:790): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_build_scope_contains_all_expected(build_scope, expected_scope_contains: dict):
        """Then: BuildScope contains all expected key-value pairs."""
        for key, value in expected_scope_contains.items():
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:796): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_action_uses_build_scope_class(action: BuildKnowledgeAction, parameters: dict):
        """Then: Action uses BuildScope class (converts dict to typed context)."""
        from agile_bot.bots.base_bot.src.actions.action_context import ScopeActionContext, Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:821): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_build_parameters_with_scope(scope_type='all', scope_value=None):
        """Given: Build parameters with scope."""
        if scope_type == 'all':
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:828): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_build_parameters_with_story_names(story_names):
        """Given: Build parameters with story names."""
        if isinstance(story_names, str):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:835): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_build_parameters_with_increment_priorities(priorities):
        """Given: Build parameters with increment priorities."""
        if isinstance(priorities, int):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:842): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_build_parameters_with_epic_names(epic_names):
        """Given: Build parameters with epic names."""
        if isinstance(epic_names, str):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:853): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestInjectKnowledgeGraphTemplateForBuildKnowledge:
        """Story: Inject Knowledge Graph Template for Build Knowledge - Tests template injection."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:856): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_action_injects_knowledge_graph_template(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action Injects Knowledge Graph Template
            """
            bot_name, behavior = given_test_variables_for_exploration()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:876): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_action_loads_and_merges_instructions(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action Loads And Merges Instructions
            GIVEN: Base and behavior-specific instructions exist
            WHEN: Action method is invoked
            THEN: Instructions are loaded from both locations and merged
            """
            bot_name, behavior, action = given_test_variables_for_shape_build()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:893): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_all_template_variables_are_replaced_in_instructions(self, bot_directory, workspace_directory):
            """
            SCENARIO: All Template Variables Are Replaced In Instructions
            GIVEN: Base instructions with {{rules}}, {{schema}}, {{description}}, {{instructions}} placeholders
            WHEN: Action loads and merges instructions with all injections
            THEN: All template variables are replaced with actual content
            """
            bot_name, behavior, action, kg_dir = given_template_variables_test_setup(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:917): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestUpdateExistingKnowledgeGraph:
        """Story: Update Existing Knowledge Graph - Tests that build updates existing story-graph.json instead of creating a new file."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:920): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_behavior_updates_existing_story_graph_json(self, bot_directory, workspace_directory):
            """
            Test that prioritization behavior updates existing story-graph.json by adding increments array,
            rather than creating a separate story-graph-increments.json file.
            """
            bot_name, behavior = given_test_variables_for_prioritization()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:956): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestLoadStoryGraphIntoMemory:
        """Story: Load Story Graph Into Memory - Tests loading story graph and creating StoryMap object model."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:960): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _create_mock_bot(bot_directory: Path):
            """Helper: Create MockBot instance for testing StoryMap.from_bot().
            
            Used by: test_from_bot_loads_story_graph, test_from_bot_raises_when_file_not_found
            """
            class MockBot:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:971): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_map_loads_epics(self, story_map):
            """
            SCENARIO: Story Map Loads Epics
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:981): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_epic_has_sub_epics(self, story_map):
            """
            SCENARIO: Epic Has Sub Epics
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:993): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_sub_epic_has_story_groups(self, story_map):
            """
            SCENARIO: Sub Epic Has Story Groups
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1006): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_group_has_stories(self, story_map):
            """
            SCENARIO: Story Group Has Stories
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1019): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_has_properties(self, story_map):
            """
            SCENARIO: Story Has Properties
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1029): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_has_scenarios(self, story_map):
            """
            SCENARIO: Story Has Scenarios
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1040): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_has_properties(self, story_map):
            """
            SCENARIO: Scenario Has Properties
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1051): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_default_test_method(self, story_map):
            """
            SCENARIO: Scenario Default Test Method
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1062): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_has_scenario_outlines(self, story_map):
            """
            SCENARIO: Story Has Scenario Outlines
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1073): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_outline_has_examples(self, story_map):
            """
            SCENARIO: Scenario Outline Has Examples
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1084): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_default_test_class(self, story_map):
            """
            SCENARIO: Story Default Test Class
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1094): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_story_map_walk_traverses_all_nodes(self, story_map):
            """
            SCENARIO: Story Map Walk Traverses All Nodes
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1106): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_map_location_for_epic(self, story_map):
            """
            SCENARIO: Map Location For Epic
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1117): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_map_location_for_sub_epic(self, story_map):
            """
            SCENARIO: Map Location For Sub Epic
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1128): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_map_location_for_story(self, story_map):
            """
            SCENARIO: Map Location For Story
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1139): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_map_location(self, story_map):
            """
            SCENARIO: Scenario Map Location
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1150): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_outline_map_location(self, story_map):
            """
            SCENARIO: Scenario Outline Map Location
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1161): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_from_bot_loads_story_graph(self, tmp_path):
            """
            SCENARIO: From Bot Loads Story Graph
            """
            bot_directory = given_test_bot_directory_created(tmp_path)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1172): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_from_bot_with_path(self, tmp_path):
            """
            SCENARIO: From Bot With Path
            """
            # Given: Bot directory, docs directory, and story graph file are created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1188): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_map_location(self, story_map):
            """
            SCENARIO: Scenario Map Location
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1199): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_scenario_outline_map_location(self, story_map):
            """
            SCENARIO: Scenario Outline Map Location
            """
            # Given: Story map is loaded
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1210): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_from_bot_loads_story_graph(self, tmp_path):
            """
            SCENARIO: From Bot Loads Story Graph
            """
            bot_directory = given_test_bot_directory_created(tmp_path)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1221): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_from_bot_with_path(self, tmp_path):
            """
            SCENARIO: From Bot With Path
            """
            # Given: Bot directory, docs directory, and story graph file are created
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1244): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestCreateBuildScope:
        """Story: Create Build Scope (Sub-epic: Build Knowledge)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1267): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        ])
        def test_build_scope_created_with_different_parameter_combinations(self, parameters, expected_scope_contains):
            """
            SCENARIO: Build scope created with different parameter combinations
            GIVEN: Parameters dict with scope configuration
            WHEN: BuildScope instantiated with parameters
            THEN: BuildScope scope property returns expected configuration
            """
            # Given: Parameters dict
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1281): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_build_scope_defaults_to_all_when_no_parameters(self):
            """
            SCENARIO: Build scope defaults to 'all' when no parameters provided
            GIVEN: Empty parameters dict
            WHEN: BuildScope instantiated
            THEN: Scope defaults to 'all'
            """
            # Given: Empty parameters
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1297): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_action_uses_build_scope_to_define_build_scope(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action uses BuildScope to define build scope
            GIVEN: BuildKnowledgeAction with parameters
            WHEN: Action executes with scope parameters
            THEN: Uses BuildScope class and includes scope in instructions
            """
            # Given: Environment bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1333): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_story_graph_with_epics_and_increments():
        """Given: Story graph with epics and increments."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1409): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_scoping_parameter_filters_story_graph(scope_type, scope_value, story_graph):
        """When: ScopingParameter filters story graph."""
        from agile_bot.bots.base_bot.src.actions.scoping_parameter import ScopingParameter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1419): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_graph_contains_epic(filtered_graph, epic_name):
        """Then: Story graph contains epic."""
        epic_names = [epic.get('name') for epic in filtered_graph.get('epics', [])]
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1425): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_graph_contains_story(filtered_graph, story_name):
        """Then: Story graph contains story."""
        story_names = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1439): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_graph_contains_increment(filtered_graph, increment_name):
        """Then: Story graph contains increment."""
        increment_names = [inc.get('name') for inc in filtered_graph.get('increments', [])]
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1445): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_graph_contains_all_epics(filtered_graph, expected_count):
        """Then: Story graph contains all epics."""
        assert len(filtered_graph.get('epics', [])) == expected_count
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1450): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_story_graph_contains_all_increments(filtered_graph, expected_count):
        """Then: Story graph contains all increments."""
        assert len(filtered_graph.get('increments', [])) == expected_count
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1459): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestFilterKnowledgeGraph:
        """Story: Filter Knowledge Graph (Sub-epic: Build Knowledge)"""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1462): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_filter_returns_all_when_scope_is_all(self):
            """
            SCENARIO: Filter returns all when scope is all
            GIVEN: Story graph with multiple epics and increments
            WHEN: ScopingParameter filters with scope type 'all'
            THEN: Story graph contains all epics and increments
            """
            # Given: Story graph with epics and increments
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1479): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_filter_by_story_names_returns_matching_stories(self):
            """
            SCENARIO: Filter by story names returns matching stories
            GIVEN: Story graph with multiple stories
            WHEN: ScopingParameter filters with story names
            THEN: Story graph contains only matching stories and their parent epics
            """
            # Given: Story graph with stories
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1497): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_filter_by_epic_names_returns_matching_epics(self):
            """
            SCENARIO: Filter by epic names returns matching epics
            GIVEN: Story graph with multiple epics
            WHEN: ScopingParameter filters with epic names
            THEN: Story graph contains only matching epics and their increments
            """
            # Given: Story graph with epics
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1515): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_filter_by_increment_priorities_returns_matching_increments(self):
            """
            SCENARIO: Filter by increment priorities returns matching increments
            GIVEN: Story graph with increments having different priorities
            WHEN: ScopingParameter filters with increment priorities
            THEN: Story graph contains only matching increments and their stories
            """
            # Given: Story graph with increments
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1533): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def test_filter_by_increment_names_returns_matching_increments(self):
            """
            SCENARIO: Filter by increment names returns matching increments
            GIVEN: Story graph with increments having different names
            WHEN: ScopingParameter filters with increment names
            THEN: Story graph contains only matching increments and their stories
            """
            # Given: Story graph with increments
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:97): Useless comment: "# Create guardrails files (required for behavior loading)" - delete it or improve the code instead

    ```python
        given_behavior_specific_instructions_created(bot_directory, behavior, action, kg_dir)
        given_setup('config_and_template', bot_directory, kg_dir=kg_dir)
        # Create guardrails files (required for behavior loading)
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:100): Useless comment: "# Create behavior.json with actions_workflow that includes b" - delete it or improve the code instead

    ```python
        from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
        create_minimal_guardrails_files(bot_directory, behavior, bot_name)
        # Create behavior.json with actions_workflow that includes behavior instructions
        from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:229): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Track Activity for Build Knowledge Action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:231): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Track Activity for Build Knowledge Action
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:251): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Proceed To Render Output
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:253): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Proceed To Render Output
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:612): Useless comment: "# Create instructions.json via behavior config" - delete it or improve the code instead

    ```python
        given_behavior_specific_instructions_created(bot_directory, behavior, action, kg_dir)
        from agile_bot.bots.base_bot.test.test_perform_behavior_action import given_behavior_config
        # Create instructions.json via behavior config
        behavior_dir = bot_directory / 'behaviors' / behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:773): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS - Build Scope (Story: Create Build Scope)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:775): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Build Scope (Story: Create Build Scope)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:848): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Inject Knowledge Graph Template for Build Knowledge
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:850): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Inject Knowledge Graph Template for Build Knowledge
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:866): Useless comment: "# Create guardrails files (required for strategy data inject" - delete it or improve the code instead

    ```python
            given_file_created(kg_dir, template_name, {'template': 'knowledge_graph', 'structure': {}})
            
            # Create guardrails files (required for strategy data injection)
            from agile_bot.bots.base_bot.test.test_execute_behavior_actions import create_minimal_guardrails_files
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:901): Useless comment: "# Create a mock behavior object for the action" - delete it or improve the code instead

    ```python
            bot_name, behavior, action, kg_dir = given_template_variables_test_setup(bot_directory, workspace_directory)
            
            # Create a mock behavior object for the action
            behavior_obj = _create_behavior(bot_directory, bot_name, behavior)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:912): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Update Existing Knowledge Graph
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:914): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Update Existing Knowledge Graph
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:951): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Load Story Graph Into Memory
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:953): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Load Story Graph Into Memory
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1239): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Create Build Scope (Sub-epic: Build Knowledge)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1241): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Create Build Scope (Sub-epic: Build Knowledge)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1308): Useless comment: "# Create behavior setup" - delete it or improve the code instead

    ```python
            behavior_name = 'exploration'
            
            # Create behavior setup
            from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1314): Useless comment: "# Create knowledge graph directory and config" - delete it or improve the code instead

    ```python
            create_minimal_guardrails_files(bot_directory, behavior_name, bot_name)
            
            # Create knowledge graph directory and config
            kg_dir = given_directory_created(bot_directory, directory_type='knowledge_graph', behavior=behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1318): Useless comment: "# Create behavior and action" - delete it or improve the code instead

    ```python
            given_setup('config_and_template', bot_directory, kg_dir=kg_dir)
            
            # Create behavior and action
            behavior = _create_behavior(bot_directory, bot_name, behavior_name, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1328): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # HELPER FUNCTIONS - Filter Knowledge Graph (Story: Filter Knowledge Graph)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1330): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Filter Knowledge Graph (Story: Filter Knowledge Graph)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1454): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Filter Knowledge Graph (Sub-epic: Build Knowledge)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_build_knowledge.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_build_knowledge.py:1456): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Filter Knowledge Graph (Sub-epic: Build Knowledge)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_executes_with_parameters(action, parameters: dict):
        """When: Action executes with parameters (converts dict to typed context).
        
        Determines the appropriate context type based on the action class.
        """
        from agile_bot.bots.base_bot.src.actions.action_context import StrategyActionContext, ValidateActionContext, Scope, ScopeType
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:87): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_strategy_assumptions_and_criteria(assumptions=None, criteria=None):
        """
        Consolidated function for strategy assumptions and criteria.
        Replaces: given_strategy_assumptions_and_criteria_dict
        
        Args:
            assumptions: List of assumptions (if None, returns default)
            criteria: Dict of criteria (if None, returns default)
        
        Returns:
            Tuple of (assumptions, criteria)
        """
        if assumptions is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:105): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_strategy_parameters_with_decisions_and_assumptions():
        """Given: Strategy parameters with decisions and assumptions."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:118): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_strategy_parameters_for_shape_behavior():
        """Given: Strategy parameters for shape behavior."""
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:125): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_discovery_strategy_decisions_and_assumptions():
        """Given: Discovery strategy decisions and assumptions."""
        decisions = {'scope': 'Component level'}
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:131): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_expected_strategy_decisions_and_assumptions():
        """Given: Expected strategy decisions and assumptions."""
        decisions = {'drill_down': 'Dig deep on system interactions'}
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:142): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_strategy_guardrails_exist(bot_directory: Path, behavior: str, assumptions: list, criteria: dict):
        """Given step: Strategy guardrails exist."""
        create_strategy_guardrails(bot_directory, behavior, assumptions, criteria)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:146): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_strategy_json_exists_with_data(workspace_directory: Path, behavior: str, decisions_made: dict, assumptions_made: list, bot_paths: BotPaths = None):
        """Given step: strategy.json exists with data for behavior."""
        if bot_paths is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:173): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def when_action_injects_strategy_criteria_and_assumptions(action: StrategyAction):
        """When step: Action injects decision criteria and assumptions."""
        # Call do_execute to get instructions with planning criteria injected
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:189): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_strategy_json_file_exists(workspace_directory: Path, bot_paths: BotPaths = None):
        """Then step: strategy.json file exists."""
        if bot_paths is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:200): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_strategy_json_file_does_not_exist(workspace_directory: Path, bot_paths: BotPaths = None):
        """Then step: strategy.json file does not exist."""
        if bot_paths is None:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:210): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_strategy_data_contains_discovery_scope(strategy_data: dict, expected_scope: str):
        """Then: Strategy data contains discovery scope."""
        assert strategy_data['discovery']['strategy_criteria']['decisions_made']['scope'] == expected_scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:214): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_strategy_data_contains_shape_drill_down(strategy_data: dict, expected_drill_down: str):
        """Then: Strategy data contains shape drill down."""
        assert strategy_data['shape']['strategy_criteria']['decisions_made']['drill_down'] == expected_drill_down
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:218): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_strategy_json_contains_behavior_data(strategy_file: Path, behavior: str, expected_decisions: dict = None, expected_assumptions: list = None):
        """Then step: strategy.json contains behavior data."""
        strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:235): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def then_strategy_json_preserves_existing_behaviors(strategy_file: Path, existing_behaviors: list):
        """Then step: strategy.json preserves existing behavior data."""
        strategy_data = json.loads(strategy_file.read_text(encoding='utf-8'))
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:243): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_bootstrapped_with_strategy_guardrails(bot_directory: Path, workspace_directory: Path):
        """Given: Environment bootstrapped with strategy guardrails."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:275): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_bootstrapped_and_strategy_action_initialized(bot_directory: Path, workspace_directory: Path):
        """Given: Environment bootstrapped and strategy action initialized."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:283): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_action_and_strategy_parameters(bot_directory: Path, workspace_directory: Path):
        """Given: Environment, action and strategy parameters."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:292): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_with_existing_strategy_and_action(bot_directory: Path, workspace_directory: Path):
        """Given: Environment with existing strategy and action."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:303): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def given_environment_action_and_empty_strategy_parameters(bot_directory: Path, workspace_directory: Path):
        """Given: Environment, action and empty strategy parameters."""
        bootstrap_env(bot_directory, workspace_directory)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:315): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestTrackActivityForStrategyAction:
        """Story: Track Activity for Strategy Action - Tests activity tracking for decide_strategy."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:342): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestProceedToBuildKnowledge:
        """Story: Proceed To Build Knowledge - Tests transition to build_knowledge action."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:362): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestInjectStrategyIntoInstructions:
        """Story: Inject Strategy Into Instructions - Tests strategy injection."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:365): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_action_injects_decision_criteria_and_assumptions(self, bot_directory, workspace_directory):
            """
            SCENARIO: Action Injects Decision Criteria And Assumptions
            """
            # Given: Environment is bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:385): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TestStoreStrategyData:
        """Story: Store Strategy Data - Tests that strategy data is saved to strategy.json."""
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:388): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_save_strategy_data_when_parameters_provided(self, bot_directory, workspace_directory):
            """
            SCENARIO: Save strategy data when parameters are provided
            GIVEN: strategy action is initialized
            AND: parameters contain decisions_made and assumptions_made
            WHEN: do_execute is called with these parameters
            THEN: strategy.json file is created in docs/stories/ folder
            AND: file contains behavior section with decisions_made and assumptions_made
            """
            # Given: Environment is bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:408): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_preserve_existing_strategy_data_when_saving(self, bot_directory, workspace_directory):
            """
            SCENARIO: Preserve existing strategy data when saving
            GIVEN: strategy.json already exists with data for 'discovery' behavior
            AND: strategy action is initialized for 'shape' behavior
            WHEN: do_execute is called with parameters
            THEN: strategy.json contains both 'discovery' and 'shape' sections
            AND: existing 'discovery' data is preserved
            """
            # Given: Environment is bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:428): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def test_skip_saving_when_no_strategy_parameters_provided(self, bot_directory, workspace_directory):
            """
            SCENARIO: Skip saving when no strategy parameters are provided
            GIVEN: strategy action is initialized
            AND: parameters do not contain decisions_made or assumptions_made
            WHEN: do_execute is called with empty or unrelated parameters
            THEN: strategy.json file is not created
            """
            # Given: Environment is bootstrapped
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:32): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # Use fixtures from conftest.py (bot_directory, workspace_directory)
    
    # ============================================================================
    # HELPER FUNCTIONS - Sub-Epic Level (Used across multiple test classes)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:34): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # HELPER FUNCTIONS - Sub-Epic Level (Used across multiple test classes)
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:82): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
        return action.do_execute(context)
    
    # ============================================================================
    # GIVEN/WHEN/THEN HELPER FUNCTIONS
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:84): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # GIVEN/WHEN/THEN HELPER FUNCTIONS
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:178): Useless comment: "# Return just the strategy criteria portion for testing" - delete it or improve the code instead

    ```python
        result = action.do_execute(StrategyActionContext())
        instructions = result.get('instructions', {})
        # Return just the strategy criteria portion for testing
        return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:310): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
        return action, parameters, bot_paths
    
    # ============================================================================
    # STORY: Track Activity for Strategy Action
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:312): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Track Activity for Strategy Action
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:337): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Proceed To Build Knowledge
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:339): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Proceed To Build Knowledge
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:357): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Inject Strategy Criteria Into Instructions
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:359): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Inject Strategy Criteria Into Instructions
    # ============================================================================
    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:380): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    
    
    # ============================================================================
    # STORY: Store Planning Data
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_decide_strategy_criteria_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_decide_strategy_criteria_action.py:382): Useless comment: "# ==========================================================" - delete it or improve the code instead

    ```python
    # ============================================================================
    # STORY: Store Planning Data
    # ============================================================================
    
    ```

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 5 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:294): Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                return data
    
        def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            execution_status = rule.scanner_execution_status or 'SUCCESS'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:310): Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'
    
        def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
            scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:330): Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                raise
    
        def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
            scanner_path = rule.scanner_path
            if not scanner_path:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:342): Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)
    
        def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
            if isinstance(context, ValidationContext):
                return self._execute_validation(context)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:347): Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))
    
        def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
            return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())
    
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_parser_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parser_generator.py:252): Function "generate_parsers_for_story_bot" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 11 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1109): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:when_action_executes_and_returns_result (lines 1109-1118)):
    ```python
    scope_dict = parameters['scope']
    if isinstance(scope_dict, dict):
        scope_type = ScopeType(scope_dict.get('type', 'all'))
        scope = Scope(type=scope_type, value=scope_dict.get('value', []), exclude=scope_dict.get('exclude', []), skiprule=scope_dict.get('skiprule', []))
    ```

  Location 2 (test_build_knowledge.py:then_action_uses_build_scope_class (lines 801-809)):
    ```python
    scope_dict = parameters['scope']
    if isinstance(scope_dict, dict):
        scope_type = ScopeType(scope_dict.get('type', 'all'))
        scope = Scope(type=scope_type, value=scope_dict.get('value', []), exclude=scope_dict.get('exclude', []))
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1445): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:given_setup (lines 1445-1449)):
    ```python
    workspace_directory = setup_params.get('workspace_directory')
    behavior = setup_params.get('behavior', 'tests')
    violations = setup_params.get('violations', False)
    rule_type = setup_params.get('rule_type')
    create_method = setup_params.get('create_method')
    ```

  Location 2 (test_invoke_cli.py:when_all_combinations_tested (lines 382-386)):
    ```python
    setup = params.get('setup', cli)
    helper = params.get('helper')
    trigger_message = params.get('trigger_message', '')
    verify_func = params.get('verify_func')
    current_behavior = params.get('current_behavior')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1445): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:given_setup (lines 1445-1449)):
    ```python
    workspace_directory = setup_params.get('workspace_directory')
    behavior = setup_params.get('behavior', 'tests')
    violations = setup_params.get('violations', False)
    rule_type = setup_params.get('rule_type')
    create_method = setup_params.get('create_method')
    ```

  Location 2 (test_invoke_cli.py:when_all_combinations_tested (lines 383-387)):
    ```python
    helper = params.get('helper')
    trigger_message = params.get('trigger_message', '')
    verify_func = params.get('verify_func')
    current_behavior = params.get('current_behavior')
    current_action = params.get('current_action')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1792): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:given_behavior_specific_rule_exists (lines 1792-1797)):
    ```python
    rules_dir = behavior_dir / '3_rules'
    rules_dir.mkdir(parents=True, exist_ok=True)
    rule_file = rules_dir / rule_name
    rule_file.write_text(json.dumps(rule_content), encoding='utf-8')
    return rule_file
    ```

  Location 2 (test_invoke_cli.py:given_mock_bot_created (lines 688-693)):
    ```python
    src_dir = bot_dir / 'src'
    src_dir.mkdir(parents=True, exist_ok=True)
    cli_script = src_dir / f'{bot_name}_cli.py'
    cli_script.write_text('# Mock CLI script', encoding='utf-8')
    return mock_bot
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:1802): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:given_story_graph_file_exists_minimal (lines 1802-1809)):
    ```python
    docs_dir = workspace_directory / 'docs' / 'stories'
    docs_dir.mkdir(parents=True, exist_ok=True)
    story_graph_file = docs_dir / 'story-graph.json'
    story_graph_file.write_text(json.dumps({'epics': [], 'stories': []}), encoding='utf-8')
    return story_graph_file
    ```

  Location 2 (test_invoke_cli.py:given_mock_bot_created (lines 688-693)):
    ```python
    src_dir = bot_dir / 'src'
    src_dir.mkdir(parents=True, exist_ok=True)
    cli_script = src_dir / f'{bot_name}_cli.py'
    cli_script.write_text('# Mock CLI script', encoding='utf-8')
    return mock_bot
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2004): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:when_validate_code_files_action_created (lines 2004-2008)):
    ```python
    docs_stories_dir = workspace_directory / 'docs' / 'stories'
    docs_stories_dir.mkdir(parents=True, exist_ok=True)
    story_graph_path = docs_stories_dir / 'story-graph.json'
    minimal_story_graph = {'epics': []}
    story_graph_path.write_text(json.dumps(minimal_story_graph, indent=2), encoding='utf-8')
    ```

  Location 2 (test_invoke_cli.py:create_base_action_instructions_duplicate_removed (lines 262-269)):
    ```python
    base_dir = base_actions_dir / action
    base_dir.mkdir(parents=True, exist_ok=True)
    instructions_file = base_dir / 'instructions.json'
    instructions_data = {'actionName': action, 'instructions': [f'Base {action} instructions']}
    instructions_file.write_text(json.dumps(instructions_data), encoding='utf-8'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2004): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:when_validate_code_files_action_created (lines 2004-2008)):
    ```python
    docs_stories_dir = workspace_directory / 'docs' / 'stories'
    docs_stories_dir.mkdir(parents=True, exist_ok=True)
    story_graph_path = docs_stories_dir / 'story-graph.json'
    minimal_story_graph = {'epics': []}
    story_graph_path.write_text(json.dumps(minimal_story_graph, indent=2), encoding='utf-8')
    ```

  Location 2 (test_invoke_cli.py:create_bot_trigger_words (lines 274-278)):
    ```python
    trigger_dir = workspace / 'agile_bot' / 'bots' / bot_name
    trigger_dir.mkdir(parents=True, exist_ok=True)
    trigger_file = trigger_dir / 'trigger_words.json'
    trigger_data = {'patterns': patterns}
    trigger_file.write_text(json.dumps(trigger_data), encoding='utf-8')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2004): Duplicate code detected across files - extract to shared function.

  Location 1 (test_validate_knowledge_and_content_against_rules.py:when_validate_code_files_action_created (lines 2004-2008)):
    ```python
    docs_stories_dir = workspace_directory / 'docs' / 'stories'
    docs_stories_dir.mkdir(parents=True, exist_ok=True)
    story_graph_path = docs_stories_dir / 'story-graph.json'
    minimal_story_graph = {'epics': []}
    story_graph_path.write_text(json.dumps(minimal_story_graph, indent=2), encoding='utf-8')
    ```

  Location 2 (test_invoke_cli.py:create_action_trigger_words (lines 303-307)):
    ```python
    action_dir = workspace / 'agile_bot' / 'bots' / bot_name / 'behaviors' / behavior / action
    action_dir.mkdir(parents=True, exist_ok=True)
    trigger_file = action_dir / 'trigger_words.json'
    trigger_data = {'patterns': patterns}
    trigger_file.write_text(json.dumps(trigger_data), encoding='utf-8')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:263): Duplicate code detected across files - extract to shared function.

  Location 1 (test_invoke_cli.py:create_base_action_instructions_duplicate_removed (lines 263-270)):
    ```python
    base_dir.mkdir(parents=True, exist_ok=True)
    instructions_file = base_dir / 'instructions.json'
    instructions_data = {'actionName': action, 'instructions': [f'Base {action} instructions']}
    instructions_file.write_text(json.dumps(instructions_data), encoding='utf-8')
    return instructions_file
    ```

  Location 2 (test_decide_strategy_criteria_action.py:given_strategy_json_exists_with_data (lines 153-170)):
    ```python
    stories_folder.mkdir(parents=True, exist_ok=True)
    strategy_file = stories_folder / 'strategy.json'
    existing_data = {behavior: {'strategy_criteria': {'criteria': {}, 'decisions_made': decisions_made}, 'assumptions': {'typical_assumptions': [], 'assumptions_made': assumptions_made}, 'recommended_activ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:275): Duplicate code detected across files - extract to shared function.

  Location 1 (test_invoke_cli.py:create_bot_trigger_words (lines 275-279)):
    ```python
    trigger_dir.mkdir(parents=True, exist_ok=True)
    trigger_file = trigger_dir / 'trigger_words.json'
    trigger_data = {'patterns': patterns}
    trigger_file.write_text(json.dumps(trigger_data), encoding='utf-8')
    return trigger_file
    ```

  Location 2 (test_decide_strategy_criteria_action.py:given_strategy_json_exists_with_data (lines 153-170)):
    ```python
    stories_folder.mkdir(parents=True, exist_ok=True)
    strategy_file = stories_folder / 'strategy.json'
    existing_data = {behavior: {'strategy_criteria': {'criteria': {}, 'decisions_made': decisions_made}, 'assumptions': {'typical_assumptions': [], 'assumptions_made': assumptions_made}, 'recommended_activ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:304): Duplicate code detected across files - extract to shared function.

  Location 1 (test_invoke_cli.py:create_action_trigger_words (lines 304-308)):
    ```python
    action_dir.mkdir(parents=True, exist_ok=True)
    trigger_file = action_dir / 'trigger_words.json'
    trigger_data = {'patterns': patterns}
    trigger_file.write_text(json.dumps(trigger_data), encoding='utf-8')
    return trigger_file
    ```

  Location 2 (test_decide_strategy_criteria_action.py:given_strategy_json_exists_with_data (lines 153-170)):
    ```python
    stories_folder.mkdir(parents=True, exist_ok=True)
    strategy_file = stories_folder / 'strategy.json'
    existing_data = {behavior: {'strategy_criteria': {'criteria': {}, 'decisions_made': decisions_made}, 'assumptions': {'typical_assumptions': [], 'assumptions_made': assumptions_made}, 'recommended_activ...
    ```

#### <span id="use-resource-oriented-design-violations">Use Resource Oriented Design: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_context_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_context_builder.py:22): Class "CliContextBuilder" uses manager/doer/loader pattern but is not owned by a domain object. Use resource-oriented design instead (e.g., make it a property of a domain object like "CliContext").

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
*... and 262 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-23_23-12-18.md`

