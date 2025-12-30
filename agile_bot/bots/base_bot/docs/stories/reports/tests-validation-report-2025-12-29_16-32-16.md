# Validation Report - Tests

**Generated:** 2025-12-29 16:32:16
**Project:** base_bot
**Behavior:** tests
**Action:** validate

## Summary

Validated story map and domain model and 3 test file(s) against **22 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`
- **Test Files Scanned:**
  - `test\test_document_headless_mode_requirements.py`
  - `test\test_execute_in_headless_mode.py`
  - `test\test_monitor_session.py`
  - **Total:** 3 test file(s)

## Scanner Execution Status

### 🟥 Overall Status: CRITICAL ISSUES

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 15 | Scanners ran without errors |
| 🟩 Clean Rules | 14 | No violations found |
| 🟥 Load Failed | 7 | Scanner could not be loaded |

**Total Rules:** 22
- **Rules with Scanners:** 22
  - 🟩 **Executed Successfully:** 15
  - 🟥 **Load Failed:** 7

### 🟩 Successfully Executed Scanners

- 🟨 **[Create Parameterized Tests For Scenarios](#create-parameterized-tests-for-scenarios)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#create-parameterized-tests-for-scenarios-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.parameterized_tests_scanner.ParameterizedTestsScanner`
- 🟩 **[Call Production Code Directly](#call-production-code-directly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.real_implementations_scanner.RealImplementationsScanner`
- 🟩 **[Consistent Vocabulary](#consistent-vocabulary)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
- 🟩 **[Define Fixtures In Test File](#define-fixtures-in-test-file)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.fixture_placement_scanner.FixturePlacementScanner`
- 🟩 **[Match Specification Scenarios](#match-specification-scenarios)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.specification_match_scanner.SpecificationMatchScanner`
- 🟩 **[Mock Only Boundaries](#mock-only-boundaries)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.mock_boundaries_scanner.MockBoundariesScanner`
- 🟩 **[No Defensive Code In Tests](#no-defensive-code-in-tests)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Production Code Clean Functions](#production-code-clean-functions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Production Code Explicit Dependencies](#production-code-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Test Observable Behavior](#test-observable-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
- 🟩 **[Use Ascii Only](#use-ascii-only)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.ascii_only_scanner.AsciiOnlyScanner`
- 🟩 **[Use Class Based Organization](#use-class-based-organization)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
- 🟩 **[Use Exact Variable Names](#use-exact-variable-names)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
- 🟩 **[Use Given When Then Helpers](#use-given-when-then-helpers)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.given_when_then_helpers_scanner.GivenWhenThenHelpersScanner`

### 🟥 Scanner Load Failures

- 🟥 **[Use Domain Language](#use-domain-language)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner`
  - Error: `Error loading scanner agile_bot.bots.base_bot.src.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner: unexpected indent (ubiquitous_language_scanner.py, line 212)`
- 🟥 **[Bug Fix Test First](#bug-fix-test-first)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.bug_fix_test_first_scanner.BugFixTestFirstScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.bug_fix_test_first_scanner.BugFixTestFirstScanner`
- 🟥 **[Cover All Behavior Paths](#cover-all-behavior-paths)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.behavior_paths_scanner.BehaviorPathsScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.behavior_paths_scanner.BehaviorPathsScanner`
- 🟥 **[Design Api Through Failing Tests](#design-api-through-failing-tests)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.failing_test_api_scanner.FailingTestApiScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.failing_test_api_scanner.FailingTestApiScanner`
- 🟥 **[Helper Extraction And Reuse](#helper-extraction-and-reuse)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.helper_extraction_scanner.HelperExtractionScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.helper_extraction_scanner.HelperExtractionScanner`
- 🟥 **[Self Documenting Tests](#self-documenting-tests)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.self_documenting_scanner.SelfDocumentingScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.self_documenting_scanner.SelfDocumentingScanner`
- 🟥 **[Pytest Bdd Orchestrator Pattern](#pytest-bdd-orchestrator-pattern)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.orchestrator_pattern_scanner.OrchestratorPatternScanner`
  - Error: `Scanner class not found: agile_bot.bots.base_bot.src.scanners.orchestrator_pattern_scanner.OrchestratorPatternScanner`

## Validation Rules Checked

### 🟥 Rule: <span id="use-domain-language">Use Domain Language</span> - FAILED
**Description:** Use Ubiquitous Language (DDD): Same vocabulary in domain model, stories, scenarios, AND code. Class names = domain entities/nouns. Method names = domain responsibilities/verbs. Test names read like plain English stories. Example: test_agent_loads_configuration_when_file_exists (not test_agt_init_sets_vars)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner`
**Error:** `Error loading scanner agile_bot.bots.base_bot.src.scanners.ubiquitous_language_scanner.UbiquitousLanguageScanner: unexpected indent (ubiquitous_language_scanner.py, line 212)`

### 🟥 Rule: <span id="bug-fix-test-first">Bug Fix Test First</span> - FAILED
**Description:** When production code breaks, follow test-first workflow: write failing test, verify failure, fix code, verify success. Never fix bugs without a failing test first. Example: test_mcp_tool_initializes_bot() fails -> fix initialization -> test passes
**Scanner:** `agile_bot.bots.base_bot.src.scanners.bug_fix_test_first_scanner.BugFixTestFirstScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.bug_fix_test_first_scanner.BugFixTestFirstScanner`

### 🟥 Rule: <span id="cover-all-behavior-paths">Cover All Behavior Paths</span> - FAILED
**Description:** Cover all behavior paths: normal (happy path), edge cases, and failure scenarios. Each distinct behavior needs its own focused test. Tests must be independent. Example: test_loads_valid_config(), test_loads_empty_config(), test_raises_error_when_file_missing()
**Scanner:** `agile_bot.bots.base_bot.src.scanners.behavior_paths_scanner.BehaviorPathsScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.behavior_paths_scanner.BehaviorPathsScanner`

### 🟥 Rule: <span id="design-api-through-failing-tests">Design Api Through Failing Tests</span> - FAILED
**Description:** Write tests against the REAL expected API BEFORE implementing code. Tests MUST fail initially. Set up real test data and call real API. Failure reveals complete API design. Example: project = Project(path=path); project.initialize() (doesn't exist yet -> fails -> drives implementation)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.failing_test_api_scanner.FailingTestApiScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.failing_test_api_scanner.FailingTestApiScanner`

### 🟥 Rule: <span id="helper-extraction-and-reuse">Helper Extraction And Reuse</span> - FAILED
**Description:** Extract duplicate test setup to reusable helper functions. Keep test bodies focused on specific behavior. Example: create_agent_with_config(), create_config_file(), verify_agent_initialized() - reusable across tests
**Scanner:** `agile_bot.bots.base_bot.src.scanners.helper_extraction_scanner.HelperExtractionScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.helper_extraction_scanner.HelperExtractionScanner`

### 🟥 Rule: <span id="self-documenting-tests">Self Documenting Tests</span> - FAILED
**Description:** Tests are self-documenting through code structure. Don't add verbose comments explaining failures. Imports, calls, and assertions show the API design. Let code speak for itself. Example: generator = MCPServerGenerator(bot_name, config_path); server = generator.generate_server()
**Scanner:** `agile_bot.bots.base_bot.src.scanners.self_documenting_scanner.SelfDocumentingScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.self_documenting_scanner.SelfDocumentingScanner`

### 🟥 Rule: <span id="pytest-bdd-orchestrator-pattern">Pytest Bdd Orchestrator Pattern</span> - FAILED
**Description:** Use pytest with orchestrator pattern for story-based tests. NO FEATURE FILES. Test classes contain orchestrator methods (under 20 lines) showing Given-When-Then flow by calling helper functions. Example: def test_agent_loads_config(): given_config_exists(); agent = when_agent_initialized(); then_agent_is_configured(agent)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.orchestrator_pattern_scanner.OrchestratorPatternScanner`
**Error:** `Scanner class not found: agile_bot.bots.base_bot.src.scanners.orchestrator_pattern_scanner.OrchestratorPatternScanner`

### 🟩 Rule: <span id="call-production-code-directly">Call Production Code Directly</span> - CLEAN (0 violations)
**Description:** Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
**Scanner:** `agile_bot.bots.base_bot.src.scanners.real_implementations_scanner.RealImplementationsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="consistent-vocabulary">Consistent Vocabulary</span> - CLEAN (0 violations)
**Description:** Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
**Scanner:** `agile_bot.bots.base_bot.src.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="define-fixtures-in-test-file">Define Fixtures In Test File</span> - CLEAN (0 violations)
**Description:** Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
**Scanner:** `agile_bot.bots.base_bot.src.scanners.fixture_placement_scanner.FixturePlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="match-specification-scenarios">Match Specification Scenarios</span> - CLEAN (0 violations)
**Description:** Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
**Scanner:** `agile_bot.bots.base_bot.src.scanners.specification_match_scanner.SpecificationMatchScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="mock-only-boundaries">Mock Only Boundaries</span> - CLEAN (0 violations)
**Description:** Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.mock_boundaries_scanner.MockBoundariesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="no-defensive-code-in-tests">No Defensive Code In Tests</span> - CLEAN (0 violations)
**Description:** Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
**Scanner:** `agile_bot.bots.base_bot.src.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - CLEAN (0 violations)
**Description:** Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
**Scanner:** `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="production-code-clean-functions">Production Code Clean Functions</span> - CLEAN (0 violations)
**Description:** Production code functions should do ONE thing, be under 20 lines, and have one level of abstraction. No hidden side effects. Name reveals complete behavior. Extract multiple concerns into separate functions. Example: load_config(), validate_config(), apply_config() - each does one thing
**Scanner:** `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="production-code-explicit-dependencies">Production Code Explicit Dependencies</span> - CLEAN (0 violations)
**Description:** Production code: make dependencies explicit through constructor injection. Pass all external dependencies as constructor parameters. No hidden global state. Tests easily inject test doubles. Example: Agent(config_loader=loader, domain_graph=graph)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="test-observable-behavior">Test Observable Behavior</span> - CLEAN (0 violations)
**Description:** Test observable behavior, not implementation details. Verify public API and visible state changes. Don't assert on private methods or internal flags. Example: assert agent.config_path.exists() (observable); not assert agent._internal_flag (private)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-ascii-only">Use Ascii Only</span> - CLEAN (0 violations)
**Description:** All test code must use ASCII-only characters. No Unicode symbols, emojis, or special characters. Use plain ASCII alternatives. Example: print('[PASS] Success') not print('[checkmark] Success')
**Scanner:** `agile_bot.bots.base_bot.src.scanners.ascii_only_scanner.AsciiOnlyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-class-based-organization">Use Class Based Organization</span> - CLEAN (0 violations)
**Description:** Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="use-exact-variable-names">Use Exact Variable Names</span> - CLEAN (0 violations)
**Description:** Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
**Scanner:** `agile_bot.bots.base_bot.src.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 2 more rules*

## Violations Found

**Total Violations:** 2
- **File-by-File Violations:** 2
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="create-parameterized-tests-for-scenarios-violations">Create Parameterized Tests For Scenarios: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[0].name): Scenario outline 'Test node operations in autonomous mode for each behavior-action' has 42 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[1].name): Scenario outline 'Test node operations in interactive mode for each behavior-action' has 42 examples but may not use @pytest.mark.parametrize

## Validation Instructions

The following validation steps were performed:

1. ## Step 1: Scanner Violation Review
2. 
3. {{scanner_output}}
4. 
5. Carefully review all scanner-reported violations as follows:
6. 1. For each violation message, locate the corresponding element in the knowledge graph.
7. 2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
8. 3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
9. 4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
10. 5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
*... and 65 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\tests-validation-report-2025-12-29_16-32-16.md`

