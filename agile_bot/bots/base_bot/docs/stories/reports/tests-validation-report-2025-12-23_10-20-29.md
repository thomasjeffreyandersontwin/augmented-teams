# Validation Report - Tests

**Generated:** 2025-12-23 10:20:29
**Project:** base_bot
**Behavior:** tests
**Action:** validate

## Summary

Validated content against **27 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: HEALTHY

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 24 | Scanners ran without errors |
| 🟩 Clean Rules | 23 | No violations found |
| [i] No Scanner | 3 | Rule has no scanner configured |

**Total Rules:** 27
- **Rules with Scanners:** 24
  - 🟩 **Executed Successfully:** 24
- [i] **Rules without Scanners:** 3

### 🟩 Successfully Executed Scanners

- 🟨 **[Create Parameterized Tests For Scenarios](#create-parameterized-tests-for-scenarios)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#create-parameterized-tests-for-scenarios-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.parameterized_tests_scanner.ParameterizedTestsScanner`
- 🟩 **[Business Readable Test Names](#business-readable-test-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.business_readable_test_names_scanner.BusinessReadableTestNamesScanner`
- 🟩 **[Call Production Code Directly](#call-production-code-directly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.real_implementations_scanner.RealImplementationsScanner`
- 🟩 **[Consistent Vocabulary](#consistent-vocabulary)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
- 🟩 **[Cover All Behavior Paths](#cover-all-behavior-paths)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.cover_all_paths_scanner.CoverAllPathsScanner`
- 🟩 **[Define Fixtures In Test File](#define-fixtures-in-test-file)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.fixture_placement_scanner.FixturePlacementScanner`
- 🟩 **[Helper Extraction And Reuse](#helper-extraction-and-reuse)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟩 **[Maintain Test Quality](#maintain-test-quality)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
- 🟩 **[Match Specification Scenarios](#match-specification-scenarios)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.specification_match_scanner.SpecificationMatchScanner`
- 🟩 **[Mock Only Boundaries](#mock-only-boundaries)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.mock_boundaries_scanner.MockBoundariesScanner`
- 🟩 **[No Fallbacks In Tests](#no-fallbacks-in-tests)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.no_fallbacks_scanner.NoFallbacksScanner`
- 🟩 **[No Guard Clauses In Tests](#no-guard-clauses-in-tests)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Production Code Explicit Dependencies](#production-code-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Production Code Single Responsibility](#production-code-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Production Code Small Functions](#production-code-small-functions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟩 **[Self Documenting Tests](#self-documenting-tests)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟩 **[Test Observable Behavior](#test-observable-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
- 🟩 **[Ubiquitous Language](#ubiquitous-language)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner`
- 🟩 **[Use Ascii Only](#use-ascii-only)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.ascii_only_scanner.AsciiOnlyScanner`
- 🟩 **[Use Class Based Organization](#use-class-based-organization)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
- 🟩 **[Use Descriptive Function Names](#use-descriptive-function-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.descriptive_function_names_scanner.DescriptiveFunctionNamesScanner`
- 🟩 **[Use Exact Variable Names](#use-exact-variable-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
- 🟩 **[Use Given When Then Helpers](#use-given-when-then-helpers)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.given_when_then_helpers_scanner.GivenWhenThenHelpersScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Bug Fix Test First](#bug-fix-test-first)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Design Api Through Failing Tests](#design-api-through-failing-tests)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Pytest Bdd Orchestrator Pattern](#pytest-bdd-orchestrator-pattern)** - No scanner configured

## Validation Rules Checked

### 🟩 Rule: <span id="business-readable-test-names">Business Readable Test Names</span> - CLEAN (0 violations)
**Description:** Test names must read like plain English stories. Use domain language stakeholders understand, not technical jargon. Test names should read naturally when spoken aloud. Describe WHAT happens (behavior), not HOW it works (implementation). Principle adapted from BDD Rule 1 (Business Readable Language) for Given When Then story-based testing.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.business_readable_test_names_scanner.BusinessReadableTestNamesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="call-production-code-directly">Call Production Code Directly</span> - CLEAN (0 violations)
**Description:** Call production code directly - tests drive production code creation through RED-GREEN-REFACTOR. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries (file I/O, network, APIs) when necessary. Separate business logic from side effects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.real_implementations_scanner.RealImplementationsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="consistent-vocabulary">Consistent Vocabulary</span> - CLEAN (0 violations)
**Description:** Use ONE word per concept across entire test suite. Pick consistent vocabulary for common operations: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Inconsistent vocabulary confuses readers and makes codebase harder to navigate. From Clean Code Rule 2.2 and BDD Rule 1.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="cover-all-behavior-paths">Cover All Behavior Paths</span> - CLEAN (0 violations)
**Description:** Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent and can run in any order. From BDD Rule 3 (Comprehensive and Brief Coverage).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.cover_all_paths_scanner.CoverAllPathsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="define-fixtures-in-test-file">Define Fixtures In Test File</span> - CLEAN (0 violations)
**Description:** Define fixtures in the test file, not in separate conftest.py. Use pytest fixtures for shared setup. Truly reusable fixtures (file operations, location helpers) belong in agents/base/src/conftest.py.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.fixture_placement_scanner.FixturePlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="helper-extraction-and-reuse">Helper Extraction And Reuse</span> - CLEAN (0 violations)
**Description:** Extract duplicate test setup to reusable helper functions and factory functions. Keep test bodies focused on specific behavior being tested. Balance shared context with test-specific setup.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-test-quality">Maintain Test Quality</span> - CLEAN (0 violations)
**Description:** CRITICAL: Tests should be as clean as production code. Keep tests readable and maintainable, use descriptive test names, and follow FIRST principles (Fast, Independent, Repeatable, Self-validating, Timely).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.test_quality_scanner.TestQualityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="match-specification-scenarios">Match Specification Scenarios</span> - CLEAN (0 violations)
**Description:** CRITICAL: Test variables, test methods, test assertiosn etc must match specification scenarios . Test names and steps describe the behavior from specification. Assertions verify exactly what the scenario states - no more, no less. Use exact variable names and terminology from specification.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.specification_match_scanner.SpecificationMatchScanner`
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

### 🟩 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - CLEAN (0 violations)
**Description:** Place all import statements at the top of the test file, after module docstrings and comments, but before any executable code. This improves readability and makes test dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
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

### 🟩 Rule: <span id="self-documenting-tests">Self Documenting Tests</span> - CLEAN (0 violations)
**Description:** Tests are self-documenting through code structure. Do NOT add verbose comments explaining that tests will fail or what API is needed. The imports, constructor calls, method calls, and assertions clearly show the expected API design. Let the code speak for itself.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="test-observable-behavior">Test Observable Behavior</span> - CLEAN (0 violations)
**Description:** Test observable behavior, not implementation details. Verify public API behavior and visible state changes. Don't assert on private methods, internal flags, or how the code works internally. Test WHAT happens, not HOW it happens. This makes tests resilient to refactoring.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="ubiquitous-language">Ubiquitous Language</span> - CLEAN (0 violations)
**Description:** Base the API for code under test on concepts that are in the domain model. When suggesting new concepts, you must update the domain model. Use Ubiquitous Language (DDD): The SAME language EVERYWHERE - domain model, stories, acceptance criteria, scenarios, AND code. Class names = domain entities/nouns (GatherContextAction, BotConfig, Guardrails, REPLSession). Method names = domain responsibilities/verbs (inject_questions_and_evidence, load_and_merge_instructions, display_current_state). Do NOT reinvent with generic technical terms (execute, process, handle, manager, service, StdioHandler). You may refine for finer detail, but ALWAYS preserve domain terminology.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-ascii-only">Use Ascii Only</span> - CLEAN (0 violations)
**Description:** All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters in test code, assertions, print statements, or output messages. Use plain ASCII alternatives like [PASS], [ERROR], [FAIL].
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.ascii_only_scanner.AsciiOnlyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-class-based-organization">Use Class Based Organization</span> - CLEAN (0 violations)
**Description:** Test structure must match story graph exactly: file names match sub-epics (test_<sub_epic_name>.py), class names match stories exactly (Test<ExactStoryName>), method names match scenarios exactly (test_<scenario_name_snake_case>). Test classes appear in same order as stories in story map. Use pytest orchestrator pattern with helper functions/fixtures. Keep tests under 20 lines, helpers under 20 lines, classes under 300 lines.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 7 more rules*

## Violations Found

**Total Violations:** 19
- **File-by-File Violations:** 19
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="create-parameterized-tests-for-scenarios-violations">Create Parameterized Tests For Scenarios: 19 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[0].story_groups[0].stories[0].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[0].story_groups[0].stories[0].scenario_outlines[0].name): Scenario outline 'Launch REPL with existing state' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[0].story_groups[0].stories[2].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[0].story_groups[0].stories[2].scenario_outlines[1].name): Scenario outline 'User selects initial behavior' has 4 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[0].story_groups[0].stories[3].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[0].story_groups[0].stories[3].scenario_outlines[0].name): Scenario outline 'CLI displays existing state with progress' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[0].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[0].scenario_outlines[0].name): Scenario outline 'User requests help for current behavior' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[0].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[0].scenario_outlines[1].name): Scenario outline 'User requests detailed help for specific action' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[1].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[1].scenario_outlines[0].name): Scenario outline 'User requests status display' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[2].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[2].scenario_outlines[0].name): Scenario outline 'User navigates to different behavior' has 4 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[2].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[2].scenario_outlines[1].name): Scenario outline 'User navigates to invalid behavior' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[3].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[3].scenario_outlines[0].name): Scenario outline 'User navigates to action within current behavior' has 4 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[3].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[3].scenario_outlines[1].name): Scenario outline 'User navigates to invalid action' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[4].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[2].story_groups[0].stories[4].scenario_outlines[0].name): Scenario outline 'User executes workflow navigation commands' has 5 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[0].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[0].scenario_outlines[0].name): Scenario outline 'User executes current action (mock)' has 5 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[1].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[1].scenario_outlines[0].name): Scenario outline 'CLI prompts for missing action parameters' has 2 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[2].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[2].scenario_outlines[0].name): Scenario outline 'CLI handles invalid story scope and provides helpful prompt' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[3].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[3].story_groups[0].stories[3].scenario_outlines[0].name): Scenario outline 'CLI handles invalid file/story scope in dual-scope behaviors and provides helpful prompt' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[4].story_groups[0].stories[0].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[4].story_groups[0].stories[0].scenario_outlines[0].name): Scenario outline 'CLI displays action completion and prompts for continuation' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[0].sub_epics[3].sub_epics[4].story_groups[0].stories[1].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[0].sub_epics[3].sub_epics[4].story_groups[0].stories[1].scenario_outlines[0].name): Scenario outline 'User confirms action completion and advances workflow' has 3 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[0].name): Scenario outline 'Test node operations in autonomous mode for each behavior-action' has 42 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[1].name): Scenario outline 'Test node operations in interactive mode for each behavior-action' has 42 examples but may not use @pytest.mark.parametrize

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
*... and 247 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\tests-validation-report-2025-12-23_10-20-29.md`

