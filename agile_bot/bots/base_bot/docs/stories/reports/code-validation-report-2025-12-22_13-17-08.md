# Validation Report - Code

**Generated:** 2025-12-22 13:17:18
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 11 code file(s) against **32 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `solution-domain-model-description.md`
  - `story-graph.json`
  - `story-map-increments.md`
- **Code Files Scanned:**
  - `src\cli\cli_code_visitor.py`
  - `src\cli\cli_help_generator.py`
  - `src\cli\cli_help_renderer.py`
  - `src\cli\command_renderer.py`
  - `src\cli\cursor_command_generator.py`
  - `src\cli\cursor_help_renderer.py`
  - `src\cli\help_renderer.py`
  - `src\cli\mcp_code_visitor.py`
  - `src\generator\orchestrator.py`
  - `src\generator\visitor.py`
  - `src\mcp\mcp_code_generator.py`
  - **Total:** 11 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 23 | No violations found |
| 🟨 Rules with Warnings | 3 | Found 6 warning violation(s) |
| 🟥 Rules with Errors | 2 | Found 39 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 37 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#chain-dependencies-properly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#delegate-to-lowest-level-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Use Domain Language](#use-domain-language)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟩 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
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

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 37 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 2 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - 4 WARNING(S) - [View Details](#chain-dependencies-properly-violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 1 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-domain-language">Use Domain Language</span> - 1 WARNING(S) - [View Details](#use-domain-language-violations)
**Description:** CRITICAL: Code must use domain-specific language, not generic terms. NEVER use Dict[str, Any], List[str], or generic 'data'/'config'/'parameters' - use typed domain objects. Objects should expose properties representing what they contain (e.g., recommended_trades), not methods that 'generate' or 'calculate' things.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
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

**Total Violations:** 49
- **File-by-File Violations:** 17
- **Cross-File Violations:** 32

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="chain-dependencies-properly-violations">Chain Dependencies Properly: 4 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:14): Method "visit_header" in Test class [CliCodeVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:14) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.bot_name = bot_name
    
    def visit_header(self, bot_name: str) -> None:
        pass
    
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:14): Method "visit_header" in Test class [CursorCommandVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:14) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.output_lines = output_lines
    
    def visit_header(self, bot_name: str) -> None:
        pass
    
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:12): Method "visit_header" in Test class [CursorHelpVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:12) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.formatter = formatter
    
    def visit_header(self, bot_name: str) -> None:
        name = bot_name if bot_name is not None else self.bot_name
        print(f"## Available Cursor Commands for {name}:")
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\mcp_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:20): Method "visit_header" in Test class [MCPCodeVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:20) takes parameter "bot_name" that is already injected in __init__. Use self.bot_name instead.

```python
        self.server_file_path = None
    
    def visit_header(self, bot_name: str) -> None:
        for behavior in self.behaviors:
            trigger_words = self._load_trigger_words(behavior)
    # ... (truncated)
```

#### <span id="delegate-to-lowest-level-violations">Delegate To Lowest Level: 1 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\mcp_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:21): Method "visit_header" in Test class [MCPCodeVisitor](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:21) iterates through "behaviors" instead of delegating to collection class. Delegate to collection class instead.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 5 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\generator\visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/generator/visitor.py:7): Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header, visit_footer have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:14): Duplicate code detected: functions visit_header, visit_behavior, visit_action, visit_action_help_section_header have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:14): Duplicate code detected: functions visit_header, visit_behavior, visit_action_help_section_header have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/help_renderer.py:13): Duplicate code detected: functions render_header, _format_behavior_command, _format_behavior_title, _format_action_command have identical bodies - extract to shared function
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\mcp_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:33): Duplicate code detected: functions visit_action, visit_action_help_section_header have identical bodies - extract to shared function

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 3 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:31): Function "_create_python_cli_script" is 82 lines - consider improving vertical density by declaring variables near usage

    ```python
            self._create_powershell_script()
        
        def _create_python_cli_script(self) -> Path:
            bot_dir = self.workspace_root / self.bot_location
            src_dir = bot_dir / 'src'
            src_dir.mkdir(parents=True, exist_ok=True)
            cli_file = src_dir / f'{self.bot_name}_cli.py'
            cli_code = f'''#!/usr/bin/env python3
    """
    {self.bot_name.title().replace('_', ' ')} CLI Entry Point
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\mcp_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:98): Function "_build_server_code" is 66 lines - consider improving vertical density by declaring variables near usage

    ```python
            return server_file
        
        def _build_server_code(self, base_tools_code: str, behavior_tools_code: str) -> str:
            return f'''"""
    {self.bot_name.title().replace('_', ' ')} MCP Server Entry Point
    
    Runnable MCP server for {self.bot_name} using FastMCP with statically generated tools.
    """
    from pathlib import Path
    import sys
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cursor_command_generator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_command_generator.py:160): Function "_build_rules_command" is 65 lines - consider improving vertical density by declaring variables near usage

    ```python
        
    
        def _build_rules_command(self, python_command: str, behavior_name: str) -> str:
            if behavior_name == 'code':
                examples = [
                    f"# Write new production code following rules",
                    f"{python_command} --behavior {behavior_name} --action rules --message \"Help me write a new ValidationContext class that encapsulates validation parameters\"",
                    "",
                    f"# Refactor existing code to follow rules",
                    f"{python_command} --behavior {behavior_name} --action rules --message \"Refactor the _execute_scanner method to reduce parameters from 10 to 3\"",
        # ... (truncated)
    ```

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\cli\command_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/command_renderer.py:57): Function "_build_example_params" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            self.output_lines.append(f"  # {example_cmd}")
        
        def _build_example_params(self, params: List[str]) -> List[str]:
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
            return example_params
        # ... (truncated)
    ```

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_code_visitor.py:85): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\mcp_code_visitor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/mcp_code_visitor.py:139): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def main():
        """Main entry point for {self.bot_name} MCP server.
    
        Environment variables are bootstrapped before import:
        - BOT_DIRECTORY: Self-detected from script location
        - WORKING_AREA: Read from bot_config.json (or overridden by mcp.json env)
        
        All subsequent code reads from these environment variables.
        """
        bot_directory = get_bot_directory()
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\generator\orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/generator/orchestrator.py:27): Function "generate_help" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 32 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\generator\orchestrator.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/generator/orchestrator.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (orchestrator.py:_visit_behavior (lines 40-50)):
    ```python
    behavior_name = behavior.name
    behavior_description = self.data_collector.get_behavior_description(behavior_name)
    actions = self.data_collector.get_behavior_actions(behavior)
    additional_options = self._get_additional_options(behavior_name)
    context = BehaviorHelpContext(bot_name=self.bot_name, behavio...
    ```

  Location 2 (mcp_code_generator.py:generate_server_entry_point (lines 17-22)):
    ```python
    workspace_root = self.bot_directory.parent.parent.parent.parent.parent
    formatter = CliTerminalFormatter()
    description_extractor = DescriptionExtractor(self.bot_name, self.bot_directory, formatter)
    data_collector = ActionDataCollector(bot, self.bot_name, self.bot_directory, description_extractor)
    mcp...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-21)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 21-25)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-21)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    ```

  Location 2 (help_renderer.py:render_behavior_section (lines 38-42)):
    ```python
    print(f'\n{self._format_behavior_title(context)}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(self._format_behavior_command(context, action_list))
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-22)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-26)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-22)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (help_renderer.py:render_behavior_section (lines 39-43)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(self._format_behavior_command(context, action_list))
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-23)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-27)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-24)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-28)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 22-29)):
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

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 26-33)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-22)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 21-26)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-22)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    ```

  Location 2 (help_renderer.py:render_behavior_section (lines 38-43)):
    ```python
    print(f'\n{self._format_behavior_title(context)}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(self._format_behavior_command(context, action_list))
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-23)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-27)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-24)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-28)):
    ```python
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-28)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additi...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-32)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 21-29)):
    ```python
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, descript...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 25-33)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-23)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 21-27)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-24)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-28)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-28)):
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

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-32)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 20-29)):
    ```python
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additi...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 24-33)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-24)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 21-28)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-28)):
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

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-32)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-29)):
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
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    print(f'action:   {action_list}')
    print('context:  Optional context or file path')
    if context.additional_options:
        print('           Additional options:')
        for option, description in context.additio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 19-29)):
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

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 23-33)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-28)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 21-32)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:18): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 18-29)):
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

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 22-33)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:17): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_behavior (lines 17-29)):
    ```python
    print(f'\n## {context.bot_name}-{context.behavior_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'python {self.cli_script_path} --behavior {context.behavior_name} --action <{action_list}> [context]')
    print()
    print(f'action:   {action_...
    ```

  Location 2 (cursor_help_renderer.py:visit_behavior (lines 21-33)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:32): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_action (lines 32-38)):
    ```python
    print(f'### {context.action_name}\n')
    print(f'{context.action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    ```

  Location 2 (cursor_help_renderer.py:visit_action (lines 36-42)):
    ```python
    print(f'### {context.action_name}\n')
    print(f'{context.action_description}\n')
    print('```')
    print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:33): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_action (lines 33-39)):
    ```python
    print(f'{context.action_description}\n')
    print('```')
    print(f'python {self.cli_script_path} --behavior <behavior> --action {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    print('```\n')
    ```

  Location 2 (cursor_help_renderer.py:visit_action (lines 37-43)):
    ```python
    print(f'{context.action_description}\n')
    print('```')
    print(f'/{context.bot_name}-<behavior> {context.action_name} [parameters]')
    if context.parameters:
        print()
        self._print_parameters(context)
    print('```\n')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:32): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:visit_action (lines 32-39)):
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

  Location 2 (cursor_help_renderer.py:visit_action (lines 36-43)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cli_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_help_renderer.py:42): Duplicate code detected across files - extract to shared function.

  Location 1 (cli_help_renderer.py:_print_parameters (lines 42-47)):
    ```python
    param_desc = context.parameter_descriptions.get(param, 'Optional parameter')
    if '\n' in param_desc:
        self._print_multiline_parameter(param, param_desc)
    else:
        print(f'{param}:   {param_desc}')
    ```

  Location 2 (cursor_help_renderer.py:_print_parameters (lines 46-51)):
    ```python
    param_desc = context.parameter_descriptions.get(param, 'Optional parameter')
    if '\n' in param_desc:
        self._print_multiline_parameter(param, param_desc)
    else:
        print(f'{param}:   {param_desc}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cursor_help_renderer.py:visit_behavior (lines 21-25)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    ```

  Location 2 (help_renderer.py:render_behavior_section (lines 38-42)):
    ```python
    print(f'\n{self._format_behavior_title(context)}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(self._format_behavior_command(context, action_list))
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (cursor_help_renderer.py:visit_behavior (lines 22-26)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```

  Location 2 (help_renderer.py:render_behavior_section (lines 39-43)):
    ```python
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(self._format_behavior_command(context, action_list))
    print()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\cli\cursor_help_renderer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cursor_help_renderer.py:21): Duplicate code detected across files - extract to shared function.

  Location 1 (cursor_help_renderer.py:visit_behavior (lines 21-26)):
    ```python
    print(f'\n## {cmd_name}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(f'/{cmd_name} <{action_list}> <context>')
    print()
    ```

  Location 2 (help_renderer.py:render_behavior_section (lines 38-43)):
    ```python
    print(f'\n{self._format_behavior_title(context)}\n')
    print(f'{context.behavior_description}\n')
    print('```')
    action_list = '|'.join(context.actions)
    print(self._format_behavior_command(context, action_list))
    print()
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
*... and 253 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-22_13-17-08.md`

