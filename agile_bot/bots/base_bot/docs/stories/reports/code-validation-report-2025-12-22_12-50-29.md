# Validation Report - Code

**Generated:** 2025-12-22 12:50:30
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 4 code file(s) against **32 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `solution-domain-model-description.md`
  - `story-graph.json`
  - `story-map-increments.md`
- **Code Files Scanned:**
  - `src\cli\cli_code_visitor.py`
  - `src\cli\cli_help_renderer.py`
  - `src\cli\command_renderer.py`
  - `src\cli\cursor_help_renderer.py`
  - **Total:** 4 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 25 | No violations found |
| 🟨 Rules with Warnings | 2 | Found 4 warning violation(s) |
| 🟥 Rules with Errors | 2 | Found 51 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 26 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 25 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
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
- 🟩 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟩 **[Provide Meaningful Context](#provide-meaningful-context)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟩 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟩 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
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

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 26 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 25 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 3 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 1 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
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
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
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

### 🟩 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - CLEAN (0 violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="prefer-object-model-over-config">Prefer Object Model Over Config</span> - CLEAN (0 violations)
**Description:** Use existing object model to access information instead of directly accessing configuration files
**Scanner:** `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - CLEAN (0 violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 12 more rules*

## Violations Found

**Total Violations:** 56
- **File-by-File Violations:** 31
- **Cross-File Violations:** 25

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:16): Method "visit_header" in Test class [CursorCommandVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:16) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.output_lines = output_lines
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - not used for command files."""
        pass
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:13): Method "visit_header" in Test class [CursorHelpVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:13) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.formatter = formatter
    
    def visit_header(self, bot_name: str) -> None:
        name = bot_name if bot_name is not None else self.bot_name
        print(f"## Available Cursor Commands for {name}:")
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:16): Method "visit_header" in Test class [CliCodeVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:16) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.bot_name = bot_name
    
    def visit_header(self, bot_name: str) -> None:
        """Visit header - not used for code generation."""
        pass
    # ... (truncated)
```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 1 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:38): Function "_create_python_cli_script" is 83 lines - consider improving vertical density by declaring variables near usage

    ```python
            self._create_powershell_script()
        
        def _create_python_cli_script(self) -> Path:
            """Create Python CLI script file."""
            bot_dir = self.workspace_root / self.bot_location
            src_dir = bot_dir / 'src'
            src_dir.mkdir(parents=True, exist_ok=True)
            cli_file = src_dir / f'{self.bot_name}_cli.py'
            cli_code = f'''#!/usr/bin/env python3
    """
        # ... (truncated)
    ```

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:65): Function "_build_example_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            self.output_lines.append(f"  # {example_cmd}")
        
        def _build_example_params(self, params: List[str]) -> List[str]:
            """Build example parameter strings."""
            example_params = []
            for param in params:
                param_name = param.split()[0]
                if '<dict>' in param:
                    example_params.append(f"{param_name} '{{\"key\": \"value\"}}'")
                elif '<list>' in param:
                    example_params.append(f'{param_name} "value1" "value2"')
                elif '<flag>' in param:
                    example_params.append(param_name)
                else:
                    example_params.append(f'{param_name} "value"')
        # ... (truncated)
    ```

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 26 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:8): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class CursorCommandVisitor(CliVisitor):
        """Visitor that renders cursor command files."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_header(self, bot_name: str) -> None:
            """Visit header - not used for command files."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:21): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_behavior(self, context: BehaviorHelpContext) -> None:
            """Visit a behavior - not used for command files (handled separately)."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:25): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_action(self, context: ActionHelpContext) -> None:
            """Visit an action and add its help to output."""
            short_desc = self._extract_short_description(context)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:40): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _extract_short_description(self, context: ActionHelpContext) -> str:
            """Extract short description from action description."""
            if not context.action_description:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:46): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _append_parameter_help(self, context: ActionHelpContext) -> None:
            """Append parameter help to output lines."""
            for param in context.parameters:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:55): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _append_example_command(self, context: ActionHelpContext) -> None:
            """Append example command with parameters."""
            example_params = self._build_example_params(context.parameters[:2])
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:66): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _build_example_params(self, params: List[str]) -> List[str]:
            """Build example parameter strings."""
            example_params = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:81): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_action_help_section_header(self) -> None:
            """Visit action help section header - not used for command files."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:85): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_footer(self) -> None:
            """Visit footer - add common patterns."""
            scope_epic = "{'type': 'epic', 'value': ['Epic Name']}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:6): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class CliHelpVisitor(CliVisitor):
        """Visitor for generating CLI help output."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:43): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _print_parameters(self, context: ActionHelpContext) -> None:
            """Print parameter descriptions."""
            for param in context.parameters:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:52): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _print_multiline_parameter(self, param: str, param_desc: str) -> None:
            """Print multiline parameter description."""
            lines = param_desc.split('\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:7): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class CursorHelpVisitor(CliVisitor):
        """Visitor for generating cursor help output."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:47): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _print_parameters(self, context: ActionHelpContext) -> None:
            """Print parameter descriptions."""
            for param in context.parameters:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:56): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _print_multiline_parameter(self, param: str, param_desc: str) -> None:
            """Print multiline parameter description."""
            lines = param_desc.split('\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:9): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class CliCodeVisitor(CliVisitor):
        """Visitor for generating CLI code files (Python, shell, PowerShell scripts)."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_header(self, bot_name: str) -> None:
            """Visit header - not used for code generation."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:21): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_behavior(self, context: BehaviorHelpContext) -> None:
            """Visit a behavior - not used for code generation."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:25): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_action(self, context: ActionHelpContext) -> None:
            """Visit an action - not used for code generation."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_action_help_section_header(self) -> None:
            """Visit action help section header - not used for code generation."""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def visit_footer(self) -> None:
            """Visit footer - create all CLI code files."""
            self._create_python_cli_script()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _create_python_cli_script(self) -> Path:
            """Create Python CLI script file."""
            bot_dir = self.workspace_root / self.bot_location
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:93): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def main():
        """Main CLI entry point.
    
        Environment variables are bootstrapped before import:
        - BOT_DIRECTORY: Self-detected from script location
        - WORKING_AREA: Read from bot_config.json (or pre-set by user)
        
        All subsequent code reads from these environment variables.
        """
        bot_directory = get_bot_directory()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:123): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _create_shell_script(self) -> Path:
            """Create shell script wrapper file."""
            bot_dir = self.workspace_root / self.bot_location
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:132): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _create_powershell_script(self) -> Path:
            """Create PowerShell script wrapper file."""
            bot_dir = self.workspace_root / self.bot_location
    ```

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 25 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-22)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-26)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-23)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-27)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-24)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-28)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 21-25)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 25-29)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:23): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 23-30)):
    ```python
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additional_options.items():
            print(f'           {option}  {description}')
    print('```\n')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 27-34)):
    ```python
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additional_options.items():
            print(f'           {option}  {description}')
    print('```\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-23)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-27)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-24)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-28)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-25)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-29)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 21-29)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additi...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 25-33)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 22-30)):
    ```python
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, descript...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 26-34)):
    ```python
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additional_options.items():
            print(f'   ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-24)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-28)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-25)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-29)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-29)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('    ...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-33)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in co...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 21-30)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additi...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 25-34)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-25)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-29)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-29)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if ...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-33)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-30)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('    ...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 25-34)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-30)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('    ...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-34)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in co...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-29)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-33)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        pr...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-30)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if ...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-34)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-30)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-34)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        pr...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:33): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_action (lines 33-39)):
    ```python
    print(f'### {context.action_name}\n')
    print(f'{context.action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    ```

  Location 2 (cursor_help_renderer.py:visit_action (lines 37-43)):
    ```python
    print(f'### {context.action_name}\n')
    print(f'{context.action_description}\n')
    print('```')
    print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_action (lines 34-40)):
    ```python
    print(f'{context.action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    print('```\n')
    ```

  Location 2 (cursor_help_renderer.py:visit_action (lines 38-44)):
    ```python
    print(f'{context.action_description}\n')
    print('```')
    print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    print('```\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:33): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_action (lines 33-40)):
    ```python
    print(f'### {context.action_name}\n')
    print(f'{context.action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    print('```\n')
    ```

  Location 2 (cursor_help_renderer.py:visit_action (lines 37-44)):
    ```python
    print(f'### {context.action_name}\n')
    print(f'{context.action_description}\n')
    print('```')
    print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    print('```\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:44): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:_print_parameters (lines 44-49)):
    ```python
    param_desc = context.parameter_descriptions.get(param, 'Optional parameter')
    if '\n' in param_desc:
        self._print_multiline_parameter(param, param_desc)
    else:
        print(f'{param}:   {param_desc}')
    ```

  Location 2 (cursor_help_renderer.py:_print_parameters (lines 48-53)):
    ```python
    param_desc = context.parameter_descriptions.get(param, 'Optional parameter')
    if '\n' in param_desc:
        self._print_multiline_parameter(param, param_desc)
    else:
        print(f'{param}:   {param_desc}')
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
*... and 251 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-22_12-50-29.md`

