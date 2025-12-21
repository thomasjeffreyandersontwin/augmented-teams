# Validation Report - Tests

**Generated:** 2025-12-20 15:39:35
**Project:** base_bot
**Behavior:** tests
**Action:** validate

## Summary

Validated story map and domain model and 1 test file(s) against **27 validation rules**.

## Content Validated

- **Rendered Outputs:**
  - `story-graph.json`
- **Test Files Scanned:**
  - `test\test_invoke_cli.py`
  - **Total:** 1 test file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 23 | Scanners ran without errors |
| 🟩 Clean Rules | 17 | No violations found |
| 🟨 Rules with Warnings | 2 | Found 23 warning violation(s) |
| 🟥 Rules with Errors | 4 | Found 99 error violation(s) |
| [i] No Scanner | 4 | Rule has no scanner configured |

**Total Rules:** 27
- **Rules with Scanners:** 23
  - 🟩 **Executed Successfully:** 23
- [i] **Rules without Scanners:** 4

### 🟩 Successfully Executed Scanners

- 🟥 **[Self Documenting Tests](#self-documenting-tests)** - 87 violation(s) (EXECUTION_SUCCESS) - [View Details](#self-documenting-tests-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Match Specification Scenarios](#match-specification-scenarios)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#match-specification-scenarios-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.specification_match_scanner.SpecificationMatchScanner`
- 🟨 **[Use Exact Variable Names](#use-exact-variable-names)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-exact-variable-names-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
- 🟥 **[Place Imports At Top](#place-imports-at-top)** - 7 violation(s) (EXECUTION_SUCCESS) - [View Details](#place-imports-at-top-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟥 **[Test Observable Behavior](#test-observable-behavior)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#test-observable-behavior-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
- 🟥 **[Call Production Code Directly](#call-production-code-directly)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#call-production-code-directly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.real_implementations_scanner.RealImplementationsScanner`
- 🟩 **[Business Readable Test Names](#business-readable-test-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.business_readable_test_names_scanner.BusinessReadableTestNamesScanner`
- 🟩 **[Consistent Vocabulary](#consistent-vocabulary)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
- 🟩 **[Cover All Behavior Paths](#cover-all-behavior-paths)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.cover_all_paths_scanner.CoverAllPathsScanner`
- 🟩 **[Create Parameterized Tests For Scenarios](#create-parameterized-tests-for-scenarios)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.parameterized_tests_scanner.ParameterizedTestsScanner`
- 🟩 **[Define Fixtures In Test File](#define-fixtures-in-test-file)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.fixture_placement_scanner.FixturePlacementScanner`
- 🟩 **[Helper Extraction And Reuse](#helper-extraction-and-reuse)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟩 **[Mock Only Boundaries](#mock-only-boundaries)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.mock_boundaries_scanner.MockBoundariesScanner`
- 🟩 **[No Fallbacks In Tests](#no-fallbacks-in-tests)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.no_fallbacks_scanner.NoFallbacksScanner`
- 🟩 **[No Guard Clauses In Tests](#no-guard-clauses-in-tests)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
- 🟩 **[Production Code Explicit Dependencies](#production-code-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Production Code Single Responsibility](#production-code-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Production Code Small Functions](#production-code-small-functions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟩 **[Ubiquitous Language](#ubiquitous-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner`
- 🟩 **[Use Ascii Only](#use-ascii-only)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.ascii_only_scanner.AsciiOnlyScanner`
- 🟩 **[Use Class Based Organization](#use-class-based-organization)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
- 🟩 **[Use Descriptive Function Names](#use-descriptive-function-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.descriptive_function_names_scanner.DescriptiveFunctionNamesScanner`
- 🟩 **[Use Given When Then Helpers](#use-given-when-then-helpers)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.given_when_then_helpers_scanner.GivenWhenThenHelpersScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Bug Fix Test First](#bug-fix-test-first)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Design Api Through Failing Tests](#design-api-through-failing-tests)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Pytest Bdd Orchestrator Pattern](#pytest-bdd-orchestrator-pattern)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Test Driven Development](#test-driven-development)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="self-documenting-tests">Self Documenting Tests</span> - 87 ERROR(S) - [View Details](#self-documenting-tests-violations)
**Description:** Tests are self-documenting through code structure. Do NOT add verbose comments explaining that tests will fail or what API is needed. The imports, constructor calls, method calls, and assertions clearly show the expected API design. Let the code speak for itself.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - 7 ERROR(S) - [View Details](#place-imports-at-top-violations)
**Description:** Place all import statements at the top of the test file, after module docstrings and comments, but before any executable code. This improves readability and makes test dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="test-observable-behavior">Test Observable Behavior</span> - 3 ERROR(S) - [View Details](#test-observable-behavior-violations)
**Description:** Test observable behavior, not implementation details. Verify public API behavior and visible state changes. Don't assert on private methods, internal flags, or how the code works internally. Test WHAT happens, not HOW it happens. This makes tests resilient to refactoring.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="call-production-code-directly">Call Production Code Directly</span> - 2 ERROR(S) - [View Details](#call-production-code-directly-violations)
**Description:** Call production code directly - tests drive production code creation through RED-GREEN-REFACTOR. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries (file I/O, network, APIs) when necessary. Separate business logic from side effects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.real_implementations_scanner.RealImplementationsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="match-specification-scenarios">Match Specification Scenarios</span> - 14 WARNING(S) - [View Details](#match-specification-scenarios-violations)
**Description:** CRITICAL: Test variables, test methods, test assertiosn etc must match specification scenarios . Test names and steps describe the behavior from specification. Assertions verify exactly what the scenario states - no more, no less. Use exact variable names and terminology from specification.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.specification_match_scanner.SpecificationMatchScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-exact-variable-names">Use Exact Variable Names</span> - 9 WARNING(S) - [View Details](#use-exact-variable-names-violations)
**Description:** Use exact variable names from specification scenarios. When specification mentions specific variables (agent_name, workspace_root, config_path), use those exact names in tests and production code. Consistency in naming makes tests match specification exactly.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="business-readable-test-names">Business Readable Test Names</span> - CLEAN (0 violations)
**Description:** Test names must read like plain English stories. Use domain language stakeholders understand, not technical jargon. Test names should read naturally when spoken aloud. Describe WHAT happens (behavior), not HOW it works (implementation). Principle adapted from BDD Rule 1 (Business Readable Language) for Given When Then story-based testing.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.business_readable_test_names_scanner.BusinessReadableTestNamesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="consistent-vocabulary">Consistent Vocabulary</span> - CLEAN (0 violations)
**Description:** Use ONE word per concept across entire test suite. Pick consistent vocabulary for common operations: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Inconsistent vocabulary confuses readers and makes codebase harder to navigate. From Clean Code Rule 2.2 and BDD Rule 1.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="cover-all-behavior-paths">Cover All Behavior Paths</span> - CLEAN (0 violations)
**Description:** Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent and can run in any order. From BDD Rule 3 (Comprehensive and Brief Coverage).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.cover_all_paths_scanner.CoverAllPathsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="create-parameterized-tests-for-scenarios">Create Parameterized Tests For Scenarios</span> - CLEAN (0 violations)
**Description:** If scenarios have tests in stories (Examples tables with multiple test cases), then create parameterized tests using @pytest.mark.parametrize. Each row in the Examples table becomes a test case. Don't write single test methods that only test one example - iterate over all examples from the scenario file.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.parameterized_tests_scanner.ParameterizedTestsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="define-fixtures-in-test-file">Define Fixtures In Test File</span> - CLEAN (0 violations)
**Description:** Define fixtures in the test file, not in separate conftest.py. Use pytest fixtures for shared setup. Truly reusable fixtures (file operations, location helpers) belong in agents/base/src/conftest.py.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.fixture_placement_scanner.FixturePlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="helper-extraction-and-reuse">Helper Extraction And Reuse</span> - CLEAN (0 violations)
**Description:** Extract duplicate test setup to reusable helper functions and factory functions. Keep test bodies focused on specific behavior being tested. Balance shared context with test-specific setup.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="mock-only-boundaries">Mock Only Boundaries</span> - CLEAN (0 violations)
**Description:** Mock ONLY at architectural boundaries: external APIs, network calls, uncontrollable services. DON'T mock internal business logic, classes under test, or file operations (use temp files). Mocking internal code defeats the purpose of tests. From BDD Rule 8.2 (Proper Mocking).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.mock_boundaries_scanner.MockBoundariesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="no-fallbacks-in-tests">No Fallbacks In Tests</span> - CLEAN (0 violations)
**Description:** Tests must fail if a fallback or default branch is executed. Every assertion should cover the explicitly intended path so that regressions do not hide behind fallback/default handling.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.no_fallbacks_scanner.NoFallbacksScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="no-guard-clauses-in-tests">No Guard Clauses In Tests</span> - CLEAN (0 violations)
**Description:** CRITICAL: Tests must NEVER contain guard clauses that check variable values, file existence, type checks, or any defensive conditionals. We control the test setup and MUST assume the code we write in tests works correctly. If test setup is wrong, we WANT the test to fail immediately - guard clauses hide problems and reduce our ability to know if tests are actually working. Guard clauses assume the code we wrote won't work, which defeats the purpose of testing. Write tests that assume positive outcomes - if you need different behavior, write a different test.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="production-code-explicit-dependencies">Production Code Explicit Dependencies</span> - CLEAN (0 violations)
**Description:** PRODUCTION CODE RULE: Make dependencies explicit through constructor injection. Pass all external dependencies (file systems, APIs, services) as constructor parameters. No hidden global state or singleton access. Tests should easily inject test doubles when needed. Follow user's rule: 'Maximize use of constructor injection - objects should have external dependencies passed in at construction time'.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="production-code-single-responsibility">Production Code Single Responsibility</span> - CLEAN (0 violations)
**Description:** PRODUCTION CODE RULE: Each function/method should do ONE thing and do it well. No hidden side effects. Name reveals complete behavior. Keep functions under 20 lines. Extract multiple concerns into separate functions. Tests should verify single responsibility - if test needs multiple unrelated assertions, function probably does too much.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="production-code-small-functions">Production Code Small Functions</span> - CLEAN (0 violations)
**Description:** PRODUCTION CODE RULE: Keep functions under 20 lines. Each function should be one level of abstraction. Extract complex logic into named helper functions. Use guard clauses to reduce nesting. Keep nesting under 2-3 levels. Tests for small functions are easier to write and understand.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="ubiquitous-language">Ubiquitous Language</span> - CLEAN (0 violations)
**Description:** Use Ubiquitous Language (DDD): The SAME language EVERYWHERE - domain model, stories, acceptance criteria, scenarios, AND code. Class names = domain entities/nouns (GatherContextAction, BotConfig, Guardrails). Method names = domain responsibilities/verbs (inject_questions_and_evidence, load_and_merge_instructions). Do NOT reinvent with generic technical terms (execute, process, handle, manager, service). You may refine for finer detail, but ALWAYS preserve domain terminology.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-ascii-only">Use Ascii Only</span> - CLEAN (0 violations)
**Description:** All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters in test code, assertions, print statements, or output messages. Use plain ASCII alternatives like [PASS], [ERROR], [FAIL].
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.ascii_only_scanner.AsciiOnlyScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 7 more rules*

## Violations Found

**Total Violations:** 122
- **File-by-File Violations:** 122
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="call-production-code-directly-violations">Call Production Code Directly: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:431): Line 431 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:674): Line 674 uses fake/stub implementation - tests should call real production code directly

#### <span id="match-specification-scenarios-violations">Match Specification Scenarios: 14 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:573): Test method [test_trigger_bot_only_no_behavior_or_action_specified](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:573) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger bot only (no behavior or action specified)
        GIVEN: user types mess...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:598): Test method [test_trigger_bot_and_behavior_no_action_specified](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:598) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger bot and behavior (no action specified)
        GIVEN: user types message ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:618): Test method [test_trigger_bot_behavior_and_action_explicitly](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:618) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger bot, behavior, and action explicitly
        GIVEN: user types message co...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:639): Test method [test_trigger_close_current_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:639) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Trigger close current action
        GIVEN: user types message containing close t...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:693): Test method [test_cli_returns_generic_description_for_unknown_command](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:693) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: CLI returns generic description when parameter description cannot be inferred
   ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:803): Test method [test_priority_property_returns_configured_priority_or_zero](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:803) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Priority property returns configured priority or zero
        GIVEN: BehaviorConf...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:824): Test method [test_matches_returns_true_when_text_matches_any_pattern](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:824) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches returns true when text matches any pattern
        GIVEN: BehaviorConfig ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:841): Test method [test_matches_returns_false_when_no_patterns_match](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:841) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches returns false when no patterns match
        GIVEN: BehaviorConfig with p...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:858): Test method [test_matches_returns_false_when_no_triggers_configured](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:858) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches returns false when no triggers configured
        GIVEN: BehaviorConfig w...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:875): Test method [test_matches_works_with_list_trigger_format](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:875) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches works with list trigger format
        GIVEN: BehaviorConfig with list tr...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:892): Test method [test_matches_checks_all_patterns_until_match_found](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:892) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches checks all patterns until match found
        GIVEN: BehaviorConfig with ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:909): Test method [test_matches_handles_regex_patterns](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:909) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches handles regex patterns
        GIVEN: BehaviorConfig with regex pattern '...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:926): Test method [test_matches_is_case_insensitive](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:926) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches is case insensitive
        GIVEN: BehaviorConfig with pattern 'TEST'
   ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:943): Test method [test_matches_handles_invalid_regex_patterns_by_falling_back_to_literal](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:943) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Matches handles invalid regex patterns by falling back to literal
        GIVEN: ...

#### <span id="place-imports-at-top-violations">Place Imports At Top: 7 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:26`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:26:26): Import statement found at line 26 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:30`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:30:30): Import statement found at line 30 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:33`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:33:33): Import statement found at line 33 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:34`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:34:34): Import statement found at line 34 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:719`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:719:719): Import statement found at line 719 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:720`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:720:720): Import statement found at line 720 after non-import code. Move all imports to the top of the file.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py:721`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:721:721): Import statement found at line 721 after non-import code. Move all imports to the top of the file.

#### <span id="self-documenting-tests-violations">Self Documenting Tests: 87 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:54): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:74): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:89): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:103): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:113): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:120): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:131): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:138): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:149): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:161): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:173): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:201): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:223): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:237): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:241): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:252): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:271): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:280): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:300): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:310): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:316): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:322): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:328): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:336): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:343): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:364): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:401): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:434): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:473): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:482): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:486): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:491): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:504): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:516): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:526): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:538): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:545): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:562): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:571): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:574): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:599): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:619): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:640): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:672): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:681): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:691): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:694): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:725): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:735): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:742): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:749): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:755): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:760): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:765): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:770): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:779): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:782): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:793): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:804): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:822): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:825): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:842): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:859): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:876): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:893): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:910): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:927): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:944): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:36): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:38): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:245): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:247): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:282): Useless comment: "# Create or update behavior.json file with trigger words (RE" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:290): Useless comment: "# Update trigger_words in behavior.json (router reads from b" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:556): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:558): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:566): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:568): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:667): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:669): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:715): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:717): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:774): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:776): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:961): Useless comment: "# ==========================================================" - delete it or improve the code instead
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:963): Useless comment: "# ==========================================================" - delete it or improve the code instead

#### <span id="test-observable-behavior-violations">Test Observable Behavior: 3 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:182): Line 182 tests internal implementation (mocks/spies) - tests should focus on observable behavior, not internal calls
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:185): Line 185 tests internal implementation (mocks/spies) - tests should focus on observable behavior, not internal calls
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:354): Line 354 tests internal implementation (mocks/spies) - tests should focus on observable behavior, not internal calls

#### <span id="use-exact-variable-names-violations">Use Exact Variable Names: 9 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:815): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:836): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:853): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:870): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:887): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:904): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:921): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:938): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_invoke_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_invoke_cli.py:955): Variable "result" uses generic name - use exact domain concept name from scenario/AC

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
*... and 252 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\tests-validation-report.md`
