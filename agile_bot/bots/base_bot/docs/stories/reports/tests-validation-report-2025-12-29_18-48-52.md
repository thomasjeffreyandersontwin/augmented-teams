# Validation Report - Tests

**Generated:** 2025-12-29 18:49:02
**Project:** base_bot
**Behavior:** tests
**Action:** validate

## Summary

Validated story map and domain model and 36 test file(s) against **22 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`
- **Test Files Scanned:**
  - `test\conftest.py`
  - `test\test_build_agile_bots.py`
  - `test\test_build_knowledge.py`
  - `test\test_current_initialize_repl_session.py`
  - `test\test_decide_strategy_criteria_action.py`
  - `test\test_display_bot_state_using_cli.py`
  - `test\test_display_bot_state_using_cli_current.py`
  - `test\test_document_headless_mode_requirements.py`
  - `test\test_execute_action_operation_through_cli.py`
  - `test\test_execute_action_operation_through_cli_current.py`
  - `test\test_execute_behavior_actions.py`
  - `test\test_execute_in_headless_mode.py`
  - `test\test_formatters.py`
  - `test\test_gather_context.py`
  - `test\test_generate_cli.py`
  - `test\test_generate_mcp_tools.py`
  - `test\test_generate_repl_cli.py`
  - `test\test_get_help_using_cli.py`
  - `test\test_get_help_using_cli_current.py`
  - `test\test_helpers.py`
  - `test\test_init_project.py`
  - `test\test_initialize_repl_session.py`
  - `test\test_initialize_repl_session_current.py`
  - `test\test_invoke_bot.py`
  - `test\test_invoke_cli.py`
  - `test\test_invoke_mcp.py`
  - `test\test_manage_bot_scope_through_cli.py`
  - `test\test_manage_bot_scope_through_cli_current.py`
  - `test\test_monitor_session.py`
  - `test\test_navigate_bot_behaviors_and_actions_with_cli.py`
  - `test\test_navigate_bot_behaviors_and_actions_with_cli_current.py`
  - `test\test_perform_behavior_action.py`
  - `test\test_render_output.py`
  - `test\test_resources.py`
  - `test\test_validate_knowledge_and_content_against_rules.py`
  - `test\test_validation_scope_and_file_filtering.py`
  - **Total:** 36 test file(s)

## Scanner Execution Status

### 🟥 Overall Status: CRITICAL ISSUES

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 15 | Scanners ran without errors |
| 🟩 Clean Rules | 7 | No violations found |
| 🟨 Rules with Warnings | 2 | Found 208 warning violation(s) |
| 🟥 Rules with Errors | 5 | Found 100 error violation(s) |
| 🟥 Load Failed | 7 | Scanner could not be loaded |

**Total Rules:** 22
- **Rules with Scanners:** 22
  - 🟩 **Executed Successfully:** 15
  - 🟥 **Load Failed:** 7

### 🟩 Successfully Executed Scanners

- 🟨 **[Match Specification Scenarios](#match-specification-scenarios)** - 187 violation(s) (EXECUTION_SUCCESS) - [View Details](#match-specification-scenarios-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.specification_match_scanner.SpecificationMatchScanner`
- 🟥 **[Use Given When Then Helpers](#use-given-when-then-helpers)** - 69 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-given-when-then-helpers-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.given_when_then_helpers_scanner.GivenWhenThenHelpersScanner`
- 🟨 **[Use Exact Variable Names](#use-exact-variable-names)** - 21 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-exact-variable-names-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
- 🟥 **[Use Class Based Organization](#use-class-based-organization)** - 11 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-class-based-organization-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
- 🟥 **[Call Production Code Directly](#call-production-code-directly)** - 8 violation(s) (EXECUTION_SUCCESS) - [View Details](#call-production-code-directly-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.real_implementations_scanner.RealImplementationsScanner`
- 🟥 **[Place Imports At Top](#place-imports-at-top)** - 8 violation(s) (EXECUTION_SUCCESS) - [View Details](#place-imports-at-top-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟥 **[No Defensive Code In Tests](#no-defensive-code-in-tests)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#no-defensive-code-in-tests-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
- 🟨 **[Create Parameterized Tests For Scenarios](#create-parameterized-tests-for-scenarios)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#create-parameterized-tests-for-scenarios-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.parameterized_tests_scanner.ParameterizedTestsScanner`
- 🟩 **[Consistent Vocabulary](#consistent-vocabulary)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
- 🟩 **[Define Fixtures In Test File](#define-fixtures-in-test-file)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.fixture_placement_scanner.FixturePlacementScanner`
- 🟩 **[Mock Only Boundaries](#mock-only-boundaries)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.mock_boundaries_scanner.MockBoundariesScanner`
- 🟩 **[Production Code Clean Functions](#production-code-clean-functions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Production Code Explicit Dependencies](#production-code-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Test Observable Behavior](#test-observable-behavior)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.observable_behavior_scanner.ObservableBehaviorScanner`
- 🟩 **[Use Ascii Only](#use-ascii-only)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.ascii_only_scanner.AsciiOnlyScanner`

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

### 🟥 Rule: <span id="use-given-when-then-helpers">Use Given When Then Helpers</span> - 69 ERROR(S) - [View Details](#use-given-when-then-helpers-violations)
**Description:** Use reusable helper functions instead of inline code blocks of 4+ lines. Optimize for reusability, not exact step names. Place helpers at correct scope: story-level in class, sub-epic in module, epic in separate file. Example: given_config_exists(), when_agent_initialized(), then_agent_is_configured()
**Scanner:** `agile_bot.bots.base_bot.src.scanners.given_when_then_helpers_scanner.GivenWhenThenHelpersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="use-class-based-organization">Use Class Based Organization</span> - 11 ERROR(S) - [View Details](#use-class-based-organization-violations)
**Description:** Test structure matches story graph: file = sub-epic (test_<sub_epic>.py), class = story (Test<ExactStoryName>), method = scenario (test_<scenario_snake_case>). Classes in story map order. Example: test_generate_bot_tools.py, class TestGenerateBotTools, def test_generator_creates_tool_for_test_bot
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_based_organization_scanner.ClassBasedOrganizationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="call-production-code-directly">Call Production Code Directly</span> - 8 ERROR(S) - [View Details](#call-production-code-directly-violations)
**Description:** Call production code directly in tests. Let tests fail naturally if code doesn't exist. Don't comment out calls, mock business logic, or fake state. Only mock external boundaries. Example: agent = Agent(); agent.initialize() (not agent = Mock())
**Scanner:** `agile_bot.bots.base_bot.src.scanners.real_implementations_scanner.RealImplementationsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - 8 ERROR(S) - [View Details](#place-imports-at-top-violations)
**Description:** Place all imports at top of test file, after docstrings, before code. Group: stdlib, third-party, then local. Example: import json; import pytest; from mymodule import MyClass
**Scanner:** `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="no-defensive-code-in-tests">No Defensive Code In Tests</span> - 4 ERROR(S) - [View Details](#no-defensive-code-in-tests-violations)
**Description:** Tests must NEVER contain guard clauses, defensive conditionals, or fallback paths. We control test setup - if it's wrong, the test MUST fail immediately. Guard clauses hide problems. Tests should assume positive outcomes. Example: Just call the code directly, don't wrap in if-checks
**Scanner:** `agile_bot.bots.base_bot.src.scanners.no_guard_clauses_scanner.NoGuardClausesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="match-specification-scenarios">Match Specification Scenarios</span> - 187 WARNING(S) - [View Details](#match-specification-scenarios-violations)
**Description:** Tests must match specification scenarios exactly. Test names, steps, and assertions verify exactly what the scenario states. Use exact variable names and terminology from specification. Example: agent_name='story_bot' (from spec), not name='bot'
**Scanner:** `agile_bot.bots.base_bot.src.scanners.specification_match_scanner.SpecificationMatchScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-exact-variable-names">Use Exact Variable Names</span> - 21 WARNING(S) - [View Details](#use-exact-variable-names-violations)
**Description:** Use exact variable names from specification scenarios. When spec mentions agent_name, workspace_root, config_path - use those exact names in tests and production code. Example: agent_name = 'story_bot' (from spec), not name = 'story_bot'
**Scanner:** `agile_bot.bots.base_bot.src.scanners.exact_variable_names_scanner.ExactVariableNamesScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="consistent-vocabulary">Consistent Vocabulary</span> - CLEAN (0 violations)
**Description:** Use ONE word per concept across entire codebase. Pick consistent vocabulary: create (not build/make/construct), verify (not check/assert/validate), load (not fetch/get/retrieve). Use intention-revealing names that describe behavior. Example: create_agent(), verify_initialized(), load_config() - same verbs everywhere
**Scanner:** `agile_bot.bots.base_bot.src.scanners.consistent_vocabulary_scanner.ConsistentVocabularyScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="define-fixtures-in-test-file">Define Fixtures In Test File</span> - CLEAN (0 violations)
**Description:** Define fixtures in the test file, not separate conftest.py. Truly reusable fixtures (file ops, location helpers) go in base conftest.py. Example: @pytest.fixture def workspace_root(tmp_path): return tmp_path / 'workspace'
**Scanner:** `agile_bot.bots.base_bot.src.scanners.fixture_placement_scanner.FixturePlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="mock-only-boundaries">Mock Only Boundaries</span> - CLEAN (0 violations)
**Description:** Mock ONLY at architectural boundaries: external APIs, network, uncontrollable services. Don't mock internal business logic, classes under test, or file operations (use temp files). Example: patch('requests.get') (OK); patch('agent.validate') (wrong)
**Scanner:** `agile_bot.bots.base_bot.src.scanners.mock_boundaries_scanner.MockBoundariesScanner`
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

*... and 2 more rules*

## Violations Found

**Total Violations:** 310
- **File-by-File Violations:** 307
- **Cross-File Violations:** 3

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="no-defensive-code-in-tests-violations">No Defensive Code In Tests: 4 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4217): Line 4217: CRITICAL - Variable truthiness check - test should fail if variable is None/empty. Guard clauses are FORBIDDEN in tests. Assume test code works - if setup is wrong, let the test fail. Remove the guard clause.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4219): Line 4219: CRITICAL - Variable truthiness check - test should fail if variable is None/empty. Guard clauses are FORBIDDEN in tests. Assume test code works - if setup is wrong, let the test fail. Remove the guard clause.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4217): Line 4217: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4219): Line 4219: CRITICAL - Guard clause detected. Guard clauses are FORBIDDEN in tests. Assume test code works correctly - if setup is wrong, let the test fail. Remove defensive checks.

#### <span id="call-production-code-directly-violations">Call Production Code Directly: 8 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\conftest.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/conftest.py:97): Line 97 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\conftest.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/conftest.py:101): Line 101 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\conftest.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/conftest.py:104): Line 104 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\conftest.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/conftest.py:183): Line 183 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:4): Line 4 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1631): Test method [test_behavior_requires_actions_workflow_json_no_fallback](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1631) (line 1631) is empty or only contains TODO comments. Tests must call production code directly from src folder, even if the code doesn't exist yet. The test should fail with ImportError or AttributeError if production code is missing.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:741): Line 741 uses fake/stub implementation - tests should call real production code directly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:787): Line 787 uses fake/stub implementation - tests should call real production code directly

#### <span id="create-parameterized-tests-for-scenarios-violations">Create Parameterized Tests For Scenarios: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[0].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[0].name): Scenario outline 'Test node operations in autonomous mode for each behavior-action' has 42 examples but may not use @pytest.mark.parametrize
- <span style="color: orange;">[!]</span> **WARNING** - [`epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[1].name`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/epics[1].sub_epics[4].story_groups[0].stories[2].scenario_outlines[1].name): Scenario outline 'Test node operations in interactive mode for each behavior-action' has 42 examples but may not use @pytest.mark.parametrize

#### <span id="match-specification-scenarios-violations">Match Specification Scenarios: 187 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:449): Line 449 uses generic variable name "config" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:462): Line 462 uses generic variable name "config" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:249): Test method [test_generator_creates_command_files](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:249) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates command files
        GIVEN: Bot configuration exists with beha...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:271): Test method [test_generator_removes_obsolete_command_files](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:271) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator removes obsolete command files
        GIVEN: Bot configuration exists
...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:292): Test method [test_generator_updates_bot_registry](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:292) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator updates bot registry
        GIVEN: Bot configuration exists
        AN...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:324): Test method [test_generator_creates_cli_help_content](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:324) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates CLI help content
        GIVEN: Bot has behaviors configured
  ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:359): Test method [test_generator_creates_cli_help_with_cli_syntax](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:359) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates CLI help with CLI syntax
        GIVEN: Bot has behaviors confi...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:388): Test method [test_generator_creates_cursor_help_for_behaviors](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:388) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates cursor help for behaviors
        GIVEN: Bot has behaviors conf...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:424): Test method [test_generator_creates_workspace_rules_file_with_trigger_patterns](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:424) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Generator creates workspace rules file with trigger patterns
        GIVEN: Bot c...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:458): Test method [test_rules_file_includes_bot_goal_and_behavior_descriptions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:458) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules file includes bot goal and behavior descriptions
        GIVEN: Bot config ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:507): Test method [test_rules_file_maps_trigger_patterns_to_tool_naming_conventions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:507) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules file maps trigger patterns to tool naming conventions
        GIVEN: A bot ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:553): Test method [test_full_awareness_generation_workflow](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:553) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Full awareness generation workflow
        GIVEN: MCP Server Generator initialize...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:627): Test method [test_action_factory_returns_clarify_action_class](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:627) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionFactory returns ClarifyContextAction for clarify
        GIVEN: ActionFacto...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:643): Test method [test_action_factory_returns_strategy_action_class](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:643) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionFactory returns StrategyAction for strategy
        GIVEN: ActionFactory is...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:659): Test method [test_action_factory_returns_none_for_unknown_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:659) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionFactory returns None for unknown action
        GIVEN: ActionFactory is ava...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:675): Test method [test_parameters_extracted_from_clarify_context_use_dashes](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:675) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Parameters from ClarifyActionContext use dashes
        GIVEN: ClarifyActionConte...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:692): Test method [test_parameters_extracted_from_strategy_context_use_dashes](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:692) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Parameters from StrategyActionContext use dashes
        GIVEN: StrategyActionCon...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:709): Test method [test_all_known_actions_have_context_classes](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:709) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: All known actions have context classes
        GIVEN: List of known action names
...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2036): Test method [test_finds_exploration_folder_with_number_prefix](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2036) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find exploration folder with number prefix
        GIVEN: Behavior folder exists ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2056): Test method [test_handles_prioritization_folder_with_prefix](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2056) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Handles Prioritization Folder With Prefix
        GIVEN: Behavior folder exists a...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2074): Test method [test_handles_scenarios_folder_with_prefix](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2074) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Handles Scenarios Folder With Prefix
        GIVEN: Behavior folder exists as 'sc...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2092): Test method [test_handles_examples_folder_with_prefix](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2092) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Handles Examples Folder With Prefix
        GIVEN: Behavior folder exists as 'exa...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:80): Test method [test_user_sets_knowledge_graph_scope_filter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:80) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User sets knowledge graph scope filter
        GIVEN: CLI is at shape.build.instr...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:109): Test method [test_user_executes_build_with_active_knowledge_graph_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:109) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User executes build with active knowledge graph scope
        GIVEN: CLI is at sh...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:145): Test method [test_user_sets_files_scope_filter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:145) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User sets files scope filter
        GIVEN: CLI is at code.validate.instructions
...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:174): Test method [test_user_executes_validate_with_active_files_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:174) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User executes validate with active files scope
        GIVEN: CLI is at code.vali...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:214): Test method [test_setting_file_scope_replaces_story_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:214) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Setting file scope replaces existing story scope
        GIVEN: CLI has story sco...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:252): Test method [test_setting_story_scope_replaces_file_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:252) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Setting story scope replaces existing file scope
        GIVEN: CLI has file scop...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:290): Test method [test_scope_only_has_one_type](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:290) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scope object can only have one type at a time
        GIVEN: Any scope is set
   ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:318): Test method [test_user_clears_all_scope_filters](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:318) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User clears all scope filters
        GIVEN: CLI is at shape.build.instructions
 ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:351): Test method [test_user_executes_build_after_clearing_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:351) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: User executes build after clearing scope
        GIVEN: CLI is at shape.build.ins...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4195): Test method [test_bot_paths_uses_default_paths_when_environment_variables_not_set](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4195) has vague name - should clearly describe behavior from specification scenario
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3975): Line 3975 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3995): Line 3995 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4014): Line 4014 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4033): Line 4033 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4053): Line 4053 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:630): Test method [test_next_behavior_reminder_injected_when_final_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:630) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Next behavior reminder is injected when action is final action
        GIVEN: val...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:652): Test method [test_next_behavior_reminder_not_injected_when_not_final_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:652) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Next behavior reminder is NOT injected when action is not final
        GIVEN: va...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:672): Test method [test_next_behavior_reminder_not_injected_when_no_next_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:672) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Next behavior reminder is NOT injected when current behavior is last in sequence
...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:726): Test method [test_close_action_at_final_action_stays_at_final](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:726) has scenario but no matching story found in specification. Scenario: Scenario: Close final action stays at final action...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:745): Test method [test_close_final_action_transitions_to_next_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:745) has scenario but no matching story found in specification. Scenario: Scenario: Close final action and verify it's marked complete...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:762): Test method [test_close_action_saves_to_completed_actions_list](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:762) has scenario but no matching story found in specification. Scenario: Scenario: Closing action saves it to completed_actions list...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:777): Test method [test_close_handles_action_already_completed_gracefully](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:777) has scenario but no matching story found in specification. Scenario: Scenario: Idempotent close (already completed)...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:796): Test method [test_bot_class_has_close_current_action_method](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:796) has scenario but no matching story found in specification. Scenario: Scenario: Bot class exposes close_current_action method...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1025): Test method [test_complete_workflow_end_to_end](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1025) has scenario but no matching story found in specification. Scenario: 
        Complete end-to-end workflow test demonstrating all fixes working together.

        Flow:
...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1530): Test method [test_behavior_action_order_determines_next_action_from_current_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1530) has scenario but no matching story found in specification. Scenario: Scenario: Behavior action order determines next action from current_action (source of truth)...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1545): Test method [test_behavior_action_order_starts_at_first_action_when_no_completed_actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1545) has scenario but no matching story found in specification. Scenario: Scenario: No completed actions yet...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1556): Test method [test_behavior_action_order_uses_current_action_when_provided](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1556) has scenario but no matching story found in specification. Scenario: Scenario: Behavior action order uses current_action when provided...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1569): Test method [test_behavior_action_order_falls_back_to_completed_actions_when_current_action_missing](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1569) has scenario but no matching story found in specification. Scenario: Scenario: Behavior action order falls back to completed_actions when current_action is missing...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1581): Test method [test_behavior_action_order_starts_at_first_action_when_no_state_file_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1581) has scenario but no matching story found in specification. Scenario: Scenario: No behavior_action_state.json file exists (fresh start)...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1594): Test method [test_behavior_action_order_out_of_order_navigation_removes_completed_actions_after_target](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1594) has scenario but no matching story found in specification. Scenario: Scenario: When navigating out of order, completed actions after target are removed...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1619): Test method [test_behavior_loads_workflow_order_from_behavior_specific_actions_workflow](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1619) has scenario but no matching story found in specification. Scenario: Scenario: Behavior loads workflow order from behaviors/{behavior_name}/behavior.json...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1631): Test method [test_behavior_requires_actions_workflow_json_no_fallback](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1631) has scenario but no matching story found in specification. Scenario: Scenario: Behavior REQUIRES behavior.json - no fallback exists...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1636): Test method [test_behavior_loads_from_actions_workflow_json](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1636) has scenario but no matching story found in specification. Scenario: Scenario: Behavior loads workflow order from behavior.json...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1673): Test method [test_different_behaviors_can_have_different_action_orders](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1673) has scenario but no matching story found in specification. Scenario: Scenario: Different behaviors can have different action orders...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1684): Test method [test_workflow_transitions_built_correctly_from_actions_workflow_json](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1684) has scenario but no matching story found in specification. Scenario: Scenario: Workflow transitions are built correctly from behavior.json...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1927): Test method [test_execute_behavior_with_action_parameter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1927) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior with action parameter
        GIVEN: Bot has behavior 'shape' wi...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1940): Test method [test_execute_behavior_without_action_forwards_to_current](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1940) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior without action parameter forwards to current action
        GIVE...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1956): Test method [test_execute_behavior_requires_confirmation_when_out_of_order](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1956) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior executes directly when called (no order checking)
        GIVEN:...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1971): Test method [test_execute_behavior_handles_entry_workflow_when_no_state](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1971) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Execute behavior executes directly when no workflow state exists
        GIVEN: N...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2023): Test method [test_action_loads_context_data_into_instructions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2023) has scenario but no matching story found in specification. Scenario: Test that Action loads clarification, strategy, and context files into instructions....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2169): Test method [test_action_injects_workflow_breadcrumbs_when_bot_instance_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2169) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action injects workflow breadcrumbs when bot instance exists
        GIVEN: Bot i...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2201): Test method [test_breadcrumbs_show_completed_behaviors_when_all_actions_completed](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2201) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Breadcrumbs show completed behaviors when all actions completed
        GIVEN: Mu...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2224): Test method [test_breadcrumbs_show_next_step_command_when_next_action_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2224) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Breadcrumbs show next step command when next action exists
        GIVEN: Current...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2247): Test method [test_breadcrumbs_not_injected_when_no_bot_instance](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2247) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Breadcrumbs are not injected when behavior has no bot instance
        GIVEN: Beh...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2574): Test method [test_bot_instantiation_with_bot_name_and_workspace](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2574) has scenario but no matching story found in specification. Scenario: Scenario: Bot can be instantiated with bot_name and workspace (BotConfig merged into Bot)....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2590): Test method [test_bot_name_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2590) has scenario but no matching story found in specification. Scenario: Scenario: Bot.name property returns bot name from config (BotConfig merged into Bot)....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2605): Test method [test_behaviors_names_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2605) has scenario but no matching story found in specification. Scenario: Scenario: Behaviors.names property discovers from folders....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2628): Test method [test_behaviors_names_empty_when_missing](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2628) has scenario but no matching story found in specification. Scenario: Scenario: Behaviors.names returns empty list when behaviors missing....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2643): Test method [test_bot_base_actions_path_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2643) has scenario but no matching story found in specification. Scenario: Scenario: Bot.base_actions_path property returns path to base_actions directory (BotConfig merged in...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2670): Test method [test_behavior_config_loads_fields_and_actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2670) has scenario but no matching story found in specification. Scenario: Scenario: BehaviorConfig loads fields and sorts actions_workflow by order....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2834): Test method [test_load_behaviors_from_bot_config](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2834) has scenario but no matching story found in specification. Scenario: Scenario: Bot behaviors are loaded from BotConfig....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2846): Test method [test_load_behaviors_sets_first_as_current](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2846) has scenario but no matching story found in specification. Scenario: Scenario: When behaviors are loaded, first behavior is set as current....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2858): Test method [test_find_behavior_by_name](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2858) has scenario but no matching story found in specification. Scenario: Scenario: Behavior can be found by name when it exists....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2872): Test method [test_find_behavior_returns_none_when_not_found](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2872) has scenario but no matching story found in specification. Scenario: Scenario: Finding behavior by name returns None when behavior doesn't exist....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2885): Test method [test_get_next_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2885) has scenario but no matching story found in specification. Scenario: Scenario: Next behavior in sequence can be retrieved....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2899): Test method [test_get_next_behavior_returns_none_at_end](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2899) has scenario but no matching story found in specification. Scenario: Scenario: Getting next behavior returns None when at last behavior....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2913): Test method [test_iterate_all_behaviors](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2913) has scenario but no matching story found in specification. Scenario: Scenario: All behaviors can be iterated....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2929): Test method [test_check_behavior_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2929) has scenario but no matching story found in specification. Scenario: Scenario: Can check if a behavior exists....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2944): Test method [test_navigate_to_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2944) has scenario but no matching story found in specification. Scenario: Scenario: Can navigate to a specific behavior....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2957): Test method [test_save_current_behavior_state](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2957) has scenario but no matching story found in specification. Scenario: Scenario: Current behavior state is persisted to behavior_action_state.json....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2971): Test method [test_load_behavior_state_from_file](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2971) has scenario but no matching story found in specification. Scenario: Scenario: Current behavior state is restored from behavior_action_state.json....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3125): Test method [test_load_actions_from_behavior_config](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3125) has scenario but no matching story found in specification. Scenario: Scenario: Actions are loaded from BehaviorConfig....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3147): Test method [test_load_actions_sets_first_as_current](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3147) has scenario but no matching story found in specification. Scenario: Scenario: When actions are loaded, first action is set as current....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3169): Test method [test_find_action_by_name](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3169) has scenario but no matching story found in specification. Scenario: Scenario: Action can be found by name when it exists....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3195): Test method [test_find_action_returns_none_when_not_found](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3195) has scenario but no matching story found in specification. Scenario: Scenario: Finding action by name returns None when action doesn't exist....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3216): Test method [test_find_action_by_order](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3216) has scenario but no matching story found in specification. Scenario: Scenario: Action can be found by order when it exists....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3241): Test method [test_get_next_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3241) has scenario but no matching story found in specification. Scenario: Scenario: Next action in sequence can be retrieved....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3267): Test method [test_get_next_action_returns_none_at_end](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3267) has scenario but no matching story found in specification. Scenario: Scenario: Getting next action returns None when at last action....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3291): Test method [test_iterate_all_actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3291) has scenario but no matching story found in specification. Scenario: Scenario: All actions can be iterated....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3319): Test method [test_navigate_to_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3319) has scenario but no matching story found in specification. Scenario: Scenario: Can navigate to a specific action....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3344): Test method [test_save_current_action_state](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3344) has scenario but no matching story found in specification. Scenario: Scenario: Current action state is persisted to behavior_action_state.json....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3369): Test method [test_load_action_state_from_file](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3369) has scenario but no matching story found in specification. Scenario: Scenario: Current action state is restored from behavior_action_state.json....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3394): Test method [test_close_current_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3394) has scenario but no matching story found in specification. Scenario: Scenario: Closing current action marks it complete and moves to next....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3426): Test method [test_action_merges_instructions_from_base_and_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3426) has scenario but no matching story found in specification. Scenario: Scenario: Action merges instructions from BaseActionConfig and Behavior config....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3487): Test method [test_action_loads_config_fields](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3487) has scenario but no matching story found in specification. Scenario: Scenario: Action loads fields from action_config.json (BaseActionConfig merged into Action)....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3588): Test method [test_bot_paths_instantiation_with_environment_variables](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3588) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths can be instantiated when environment variables are set....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3600): Test method [test_bot_paths_workspace_directory_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3600) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.workspace_directory property returns workspace path from WORKING_AREA....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3611): Test method [test_bot_paths_bot_directory_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3611) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.bot_directory property returns bot directory from BOT_DIRECTORY....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3622): Test method [test_bot_paths_base_actions_directory_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3622) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.base_actions_directory property returns base_actions directory.
        
        ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3639): Test method [test_bot_paths_python_workspace_root_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3639) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.python_workspace_root property returns Python workspace root....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3650): Test method [test_bot_paths_find_repo_root_method](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3650) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths.find_repo_root() method returns repository root....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3662): Test method [test_bot_paths_instantiation_with_workspace_path](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3662) has scenario but no matching story found in specification. Scenario: Scenario: BotPaths can be instantiated with explicit workspace path....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3859): Test method [test_base_instructions_property_returns_instructions_from_config](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3859) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Base instructions property returns instructions from config
        GIVEN: BaseAc...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3883): Test method [test_behavior_config_loads_correct_behavior_from_behavior_json_file](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3883) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behavior config loads correct behavior from behavior.json file
        GIVEN: beh...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3907): Test method [test_behavior_config_provides_access_to_config_objects](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3907) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behavior config provides access to config objects
        GIVEN: BehaviorConfig l...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3942): Test method [test_behaviors_collection_loads_behaviors_from_bot_config](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3942) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors collection loads behaviors from bot config
        GIVEN: BotConfig wit...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3961): Test method [test_behaviors_find_by_name_returns_behavior_when_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3961) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors find by name returns behavior when exists
        GIVEN: Behaviors coll...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3981): Test method [test_behaviors_find_by_name_returns_none_when_does_not_exist](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3981) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors find by name returns none when does not exist
        GIVEN: Behaviors ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4000): Test method [test_behaviors_check_exists_returns_true_when_behavior_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4000) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors check exists returns true when behavior exists
        GIVEN: Behaviors...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4019): Test method [test_behaviors_check_exists_returns_false_when_behavior_does_not_exist](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4019) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors check exists returns false when behavior does not exist
        GIVEN: ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4038): Test method [test_behaviors_current_property_returns_current_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4038) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors current property returns current behavior
        GIVEN: Behaviors coll...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4059): Test method [test_behaviors_next_property_returns_next_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4059) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors next property returns next behavior
        GIVEN: Behaviors collection...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4080): Test method [test_behaviors_navigate_to_behavior_updates_current_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4080) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors navigate to behavior updates current behavior
        GIVEN: Behaviors ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4099): Test method [test_behaviors_close_current_marks_behavior_and_action_complete](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4099) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors close current marks behavior and action complete
        GIVEN: Behavio...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4121): Test method [test_behaviors_execute_current_executes_current_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4121) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behaviors execute current executes current behavior
        GIVEN: Behaviors coll...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4145): Test method [test_bot_paths_resolves_bot_directory_from_environment](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4145) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths resolves bot directory from environment
        GIVEN: BOT_DIRECTORY en...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4161): Test method [test_bot_paths_resolves_workspace_directory_from_environment](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4161) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths resolves workspace directory from environment
        GIVEN: WORKING_AR...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4177): Test method [test_bot_paths_properties_return_resolved_paths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4177) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths properties return resolved paths
        GIVEN: BotPaths with resolved ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4195): Test method [test_bot_paths_uses_default_paths_when_environment_variables_not_set](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4195) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Bot paths uses default paths when environment variables not set
        GIVEN: No...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4380): Test method [test_build_scope_filters_by_story_names](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4380) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope filters story graph by story names
        GIVEN: Story graph with mul...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4398): Test method [test_build_scope_filters_by_epic_names](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4398) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope filters story graph by epic names
        GIVEN: Story graph with mult...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4416): Test method [test_build_scope_filters_by_increment_priorities](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4416) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope filters story graph by increment priorities
        GIVEN: Story graph...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4434): Test method [test_build_scope_returns_all_when_scope_is_all](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4434) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: BuildScope returns all when scope is all
        GIVEN: Story graph with multiple...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4451): Test method [test_validation_scope_filters_by_story_names](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4451) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidationScope filters story graph by story names
        GIVEN: Story graph wit...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4469): Test method [test_validation_scope_filters_by_epic_names](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4469) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidationScope filters story graph by epic names
        GIVEN: Story graph with...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4487): Test method [test_action_scope_filters_by_story_names](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4487) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionScope filters story graph by story names
        GIVEN: Story graph with mu...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4505): Test method [test_action_scope_filters_by_epic_names](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4505) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionScope filters story graph by epic names
        GIVEN: Story graph with mul...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4523): Test method [test_action_scope_returns_all_when_scope_is_all](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4523) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ActionScope returns all when scope is all
        GIVEN: Story graph with multipl...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5472): Line 5472 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5509): Line 5509 uses generic variable name "result" - use exact variable names from specification
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2254): Test method [test_track_activity_when_validate_action_starts](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2254) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Track activity when validate action starts
        GIVEN: behavior is 'exploratio...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2271): Test method [test_track_activity_when_validate_action_completes](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2271) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Track activity when validate action completes
        GIVEN: validate action star...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2304): Test method [test_track_multiple_validate_invocations_across_behaviors](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2304) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Track multiple validate invocations across behaviors
        GIVEN: activity log ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2335): Test method [test_activity_log_maintains_chronological_order](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2335) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Activity Log Maintains Chronological Order
        GIVEN: activity log contains 1...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2368): Test method [test_validate_marks_workflow_as_complete](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2368) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate marks workflow as complete
        GIVEN: validate action is complete
  ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2385): Test method [test_validate_does_not_inject_next_action_instructions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2385) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate does NOT inject next action instructions
        GIVEN: validate action ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2446): Test method [test_workflow_does_not_transition_after_validate](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2446) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Workflow does NOT transition after validate
        GIVEN: validate action is com...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2464): Test method [test_behavior_workflow_completes_at_terminal_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2464) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Behavior workflow completes at terminal action
        GIVEN: exploration behavio...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2503): Test method [test_validate_returns_instructions_with_rules_as_context](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2503) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate returns instructions with rules as supporting context
        GIVEN: val...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2516): Test method [test_validate_provides_report_path_for_saving_validation_report](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2516) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: validate provides report_path for saving validation report
        GIVEN: validat...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2682): Test method [test_validate_raises_exception_when_story_graph_not_found](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2682) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidateRulesAction raises exception when story graph not found
        GIVEN: St...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2697): Test method [test_validate_raises_exception_when_story_graph_invalid_json](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:2697) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ValidateRulesAction raises exception when story graph has syntax error
        GI...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3315): Test method [test_validate_respects_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3315) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validate that validate only processes stories within specified scope.
        
  ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3356): Test method [test_validate_scope_extraction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3356) has scenario but no matching story found in specification. Scenario: Test that scope extraction functions work correctly....
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3396): Test method [test_validate_with_test_file_scope_parameter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3396) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validate test file using test_file scope parameter
        GIVEN: A test file exi...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3414): Test method [test_validate_with_test_files_scope_parameter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3414) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validate multiple test files using test_files scope parameter
        GIVEN: Mult...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3432): Test method [test_validate_verifies_test_files_passed_to_scanner](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3432) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Verify that test files from scope parameters are actually passed to TestScanner
 ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3646): Test method [test_scanner_detects_violations](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3646) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner detects violations in bad examples
        GIVEN: Scanner class path, beh...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3685): Test method [test_validate_code_files_action_accepts_test_files_parameter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3685) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction accepts test files via test_files parameter...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3714): Test method [test_validate_code_files_action_validates_each_file_from_parameters](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3714) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction validates each file provided via test_files parameter...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3727): Test method [test_validate_code_files_action_merges_violations_from_knowledge_graph_and_files](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3727) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction merges violations from knowledge graph validation and code file va...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3740): Test method [test_validate_code_files_action_works_for_tests_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3740) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction works for tests behavior (test files)...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3769): Test method [test_validate_code_files_action_accepts_code_files_parameter](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3769) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction accepts source files via code_files parameter...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3794): Test method [test_validate_code_files_action_works_for_code_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3794) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction works for code behavior (source files)...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3813): Test method [test_validate_code_files_action_returns_early_when_no_files_provided](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3813) has scenario but no matching story found in specification. Scenario: Scenario: ValidateCodeFilesAction returns knowledge graph results when no files provided...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4279): Test method [test_rules_loads_both_bot_level_and_behavior_specific_rules_when_instantiated_with_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4279) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules loads both bot-level and behavior-specific rules when instantiated with beh...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4312): Test method [test_find_by_name_returns_rule_when_rule_exists](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4312) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find by name returns rule when rule exists
        GIVEN: Rules collection with r...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4336): Test method [test_find_by_name_returns_none_when_rule_does_not_exist](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4336) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find by name returns none when rule does not exist
        GIVEN: Rules collectio...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4355): Test method [test_find_by_name_searches_both_bot_level_and_behavior_specific_rules](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4355) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Find by name searches both bot-level and behavior-specific rules
        GIVEN: R...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4389): Test method [test_iterate_returns_all_rules_in_collection](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4389) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Iterate returns all rules in collection
        GIVEN: Rules collection with mult...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4413): Test method [test_iterate_returns_empty_iterator_when_no_rules_loaded](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4413) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Iterate returns empty iterator when no rules loaded
        GIVEN: Rules collecti...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4432): Test method [test_iterate_includes_both_bot_level_and_behavior_specific_rules](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4432) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Iterate includes both bot-level and behavior-specific rules
        GIVEN: Rules ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4462): Test method [test_rule_loads_from_json_file_path](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4462) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule loads from JSON file path
        GIVEN: Rule JSON file exists
        WHEN:...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4481): Test method [test_rule_loads_embedded_rule_from_validation_rules_json](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4481) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule loads embedded rule from validation_rules.json
        GIVEN: validation_rul...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4498): Test method [test_rule_extracts_name_from_file_path](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4498) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule extracts name from file path
        GIVEN: Rule file 'test_rule.json'
     ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4515): Test method [test_rule_extracts_name_from_embedded_rule_data](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4515) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule extracts name from embedded rule data
        GIVEN: Embedded rule data with...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4545): Test method [test_rule_scanner_properties_return_scanner_instance_or_none](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4545) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule scanner properties return scanner instance or None
        GIVEN: Rule with ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4567): Test method [test_rule_provides_access_to_config_properties](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4567) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rule provides access to config properties
        GIVEN: Rule loaded with complet...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4603): Test method [test_validation_scope_created_with_different_parameter_combinations](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4603) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Validation scope created with different parameter combinations
        GIVEN: Par...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4621): Test method [test_scanner_loader_loads_scanner_from_exact_module_path](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4621) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader loads scanner from exact module path
        GIVEN: Valid scanner ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4638): Test method [test_scanner_loader_loads_scanner_from_base_bot_scanners_directory](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4638) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader loads scanner from base_bot scanners directory
        GIVEN: Scan...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4655): Test method [test_scanner_loader_loads_scanner_from_bot_specific_scanners_directory](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4655) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader loads scanner from bot-specific scanners directory
        GIVEN: ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4673): Test method [test_scanner_loader_validates_scanner_inherits_from_scanner_base_class](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4673) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Scanner loader validates scanner inherits from Scanner base class
        GIVEN: ...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4699): Test method [test_action_uses_rules_collection_to_load_rules](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4699) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses Rules collection to load rules
        GIVEN: ValidateRulesAction wit...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4715): Test method [test_action_uses_rule_class_to_access_rule_properties](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4715) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses Rule class to access rule properties
        GIVEN: ValidateRulesActi...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4732): Test method [test_action_uses_scanner_loader_to_load_scanner_classes](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4732) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses ScannerLoader to load scanner classes
        GIVEN: ValidateRulesAct...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4749): Test method [test_action_uses_validation_scope_to_define_validation_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4749) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses ValidationScope to define validation scope
        GIVEN: ValidateRul...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4770): Test method [test_action_uses_scanner_loader_service_to_load_scanner_classes](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4770) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Action uses ScannerLoader service to load scanner classes
        GIVEN: Rule wit...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4786): Test method [test_scanner_loader_loads_scanner_from_multiple_possible_paths](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4786) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ScannerLoader loads scanner from multiple possible paths
        GIVEN: ScannerLo...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4803): Test method [test_scanner_loader_validates_scanner_inherits_from_scanner_base_class](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4803) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: ScannerLoader validates scanner inherits from Scanner base class
        GIVEN: S...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5372): Test method [test_rules_action_loads_rules_for_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5372) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action loads rules for behavior
        GIVEN: behavior is 'code' with rule...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5403): Test method [test_formatted_rules_digest_returns_compact_format](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5403) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: formatted_rules_digest returns compact format
        GIVEN: behavior has 2 rules...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5443): Test method [test_rules_action_includes_message_in_context](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5443) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action includes user message in context
        GIVEN: behavior is 'code' a...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5480): Test method [test_rules_action_outputs_to_ai_context_only](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5480) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action outputs digest to AI context only (not display)
        GIVEN: behav...
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5523): Test method [test_rules_action_is_not_workflow_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5523) has scenario but no matching story found in specification. Scenario: 
        SCENARIO: Rules action is not part of workflow
        GIVEN: rules action is initialized
 ...

#### <span id="place-imports-at-top-violations">Place Imports At Top: 8 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3682): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    # ============================================================================
    
    from unittest.mock import Mock
    from agile_bot.bots.base_bot.src.bot.merged_instructions import MergedInstructions
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3683): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    
    from unittest.mock import Mock
    from agile_bot.bots.base_bot.src.bot.merged_instructions import MergedInstructions
    # BaseActionConfig deleted - Action already has config loading
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3686): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    # BaseActionConfig deleted - Action already has config loading
    # BehaviorConfig merged into Behavior - use Behavior directly
    from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors
    # BotConfig merged into Bot - use Bot directly
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3688): Import statement found after non-import code. Move all imports to the top of the file.

    ```python
    from agile_bot.bots.base_bot.src.bot.behaviors import Behaviors
    # BotConfig merged into Bot - use Bot directly
    from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
    
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

#### <span id="use-class-based-organization-violations">Use Class Based Organization: 11 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\conftest.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/conftest.py): Test file name "conftest" does not match any sub-epic name and test methods do not span multiple sub-epics - file should be named test_<sub_epic_name>.py.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py): Test method [test_appends_total_loops](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py): Test file name "test_helpers" does not match any sub-epic name and test methods do not span multiple sub-epics - file should be named test_<sub_epic_name>.py.
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py): Test method [test_bot_name_property](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py): Test method [test_get_next_behavior](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py): Test method [test_find_action_by_name](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py): Test method [test_get_next_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py): Test method [test_iterate_all_actions](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py): Test method [test_navigate_to_action](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py): Test method [test_skiprule_via_scope](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py) appears abbreviated - should match scenario name exactly
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py): Test class [TestScanner](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py) appears abbreviated - should match story name exactly (Test<ExactStoryName>)

#### <span id="use-exact-variable-names-violations">Use Exact Variable Names: 21 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:255): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:277): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:298): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:319): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:342): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:369): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_execute_in_headless_mode.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_execute_in_headless_mode.py:394): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3871): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3975): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3995): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4014): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4033): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4053): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4074): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4330): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4350): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4408): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4427): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:4453): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5472): Variable "result" uses generic name - use exact domain concept name from scenario/AC
- <span style="color: orange;">[!]</span> **WARNING** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5509): Variable "result" uses generic name - use exact domain concept name from scenario/AC

#### <span id="use-given-when-then-helpers-violations">Use Given When Then Helpers: 66 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:340): Lines 340-345: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.src.bot.bot import Bot
  bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
  formatter = Mock()
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:374): Lines 374-379: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.src.bot.bot import Bot
  bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
  formatter = Mock()
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:406): Lines 406-412: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.src.bot.bot import Bot
  bot = Bot(bot_name=bot_name, bot_directory=bot_dir, config_path=bot_config)
  formatter = Mock()
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_generate_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_generate_cli.py:540): Lines 540-546: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
  """
  SCENARIO: Generator handles file write errors with clear error message
  GIVEN: .cursor/rules/ directory is write-protected
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:96): Lines 96-102: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:126): Lines 126-131: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:161): Lines 161-167: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:191): Lines 191-196: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:230): Lines 230-235: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:268): Lines 268-273: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:335): Lines 335-340: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_manage_bot_scope_through_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_manage_bot_scope_through_cli.py:368): Lines 368-373: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  bot = Bot(
  bot_name='story_bot',
  bot_directory=bot_directory,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_navigate_bot_behaviors_and_actions_with_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py:48): Lines 48-51: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  state = _read_state(workspace_dir)
  assert state["current_behavior"] == "story_bot.shape"
  if state.get("current_action"):
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_navigate_bot_behaviors_and_actions_with_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py:61): Lines 61-65: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  assert actions.current_action_name == "strategy"
  state = _read_state(workspace_dir)
  completed = [a.get("action_state") for a in state.get("completed_actions", [])]
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_navigate_bot_behaviors_and_actions_with_cli.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_navigate_bot_behaviors_and_actions_with_cli.py:75): Lines 75-78: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions.close_current()  # completes clarify, moves to strategy
  remaining = actions.remaining_actions
  assert "clarify" not in remaining
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:1699): Lines 1699-1704: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  actions = actions_workflow.get('actions', [])
  if any(action.get('name') == 'build' for action in actions):
  from agile_bot.bots.base_bot.test.test_build_knowledge import (
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2026): Lines 2026-2029: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  workspace_dir = tmp_path / "workspace"
  workspace_dir.mkdir()
  docs_dir = workspace_dir / "docs" / "stories"
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2031): Lines 2031-2052: Multiple inline steps (22 lines) should be extracted into a Given/When/Then helper function. Block:
  clarification_data = {
  "shape": {
  "key_questions": {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2058): Lines 2058-2069: Multiple inline steps (12 lines) should be extracted into a Given/When/Then helper function. Block:
  strategy_data = {
  "shape": {
  "strategy_criteria": {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2075): Lines 2075-2079: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  context_dir = docs_dir / "context"
  context_dir.mkdir(parents=True)
  (context_dir / "input.txt").write_text("Original input content")
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2113): Lines 2113-2118: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  assert 'context_files' in instructions
  context_files = instructions['context_files']
  assert isinstance(context_files, list)
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2152): Lines 2152-2155: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  import shutil
  shutil.rmtree(context_dir)
  action4 = Action(action_name="build", behavior=behavior, action_config=None)
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2677): Lines 2677-2693: Multiple inline steps (17 lines) should be extracted into a Given/When/Then helper function. Block:
  workspace_dir = tmp_path
  behavior = "tests"
  behavior_config_data = {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:2924): Lines 2924-2927: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  assert len(behavior_names) == 3
  assert 'shape' in behavior_names
  assert 'prioritization' in behavior_names
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3132): Lines 3132-3135: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1, "next_action": "strategy"},
  {"name": "strategy", "order": 2, "next_action": "build"},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3154): Lines 3154-3157: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3176): Lines 3176-3180: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3223): Lines 3223-3226: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3248): Lines 3248-3252: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3274): Lines 3274-3277: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3298): Lines 3298-3302: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3314): Lines 3314-3317: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  assert len(action_names) == 3
  assert 'clarify' in action_names
  assert 'strategy' in action_names
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3326): Lines 3326-3330: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3351): Lines 3351-3354: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3377): Lines 3377-3381: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3401): Lines 3401-3404: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {"name": "clarify", "order": 1},
  {"name": "strategy", "order": 2},
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3419): Lines 3419-3424: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  state_file = bot_paths.workspace_directory / 'behavior_action_state.json'
  assert state_file.exists()
  state_data = json.loads(state_file.read_text(encoding='utf-8'))
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3444): Lines 3444-3454: Multiple inline steps (11 lines) should be extracted into a Given/When/Then helper function. Block:
  actions_list = [
  {
  "name": "clarify",
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3493): Lines 3493-3498: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  action_config_data = {
  "name": "clarify",
  "workflow": True,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:3919): Lines 3919-3929: Multiple inline steps (11 lines) should be extracted into a Given/When/Then helper function. Block:
  workspace_dir = tmp_path
  behavior = "shape"
  behavior_config_data = {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4207): Lines 4207-4211: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  try:
  if 'BOT_DIRECTORY' in os.environ:
  del os.environ['BOT_DIRECTORY']
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_perform_behavior_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_perform_behavior_action.py:4214): Lines 4214-4220: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
  with pytest.raises(RuntimeError):
  BotPaths()
  finally:
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3665): Lines 3665-3668: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  if 'code' in behavior:
  bad_example = {'code_files': [str(test_file)]}
  elif 'tests' in behavior:
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3694): Lines 3694-3698: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  class TestExampleStory:
  def test_example_scenario(self):
  assert True
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3700): Lines 3700-3705: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  class TestAnotherStory:
  def test_another_scenario(self):
  assert True
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:3749): Lines 3749-3752: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  class TestExampleStory:
  def test_example_scenario(self):
  assert True
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5078): Lines 5078-5085: Multiple inline steps (8 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'scope': {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5097): Lines 5097-5103: Multiple inline steps (7 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'scope': {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5115): Lines 5115-5123: Multiple inline steps (9 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'scope': {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5131): Lines 5131-5135: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  def test_force_full_flag_triggers_full_scan(self, bot_directory, workspace_directory):
  from agile_bot.bots.base_bot.src.actions.rules.rules import ValidationContext
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5151): Lines 5151-5155: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  def test_skip_cross_file_flag_disables_cross_file_scan(self, bot_directory, workspace_directory):
  from agile_bot.bots.base_bot.src.actions.rules.rules import ValidationContext
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5255): Lines 5255-5263: Multiple inline steps (9 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'scope': {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5276): Lines 5276-5283: Multiple inline steps (8 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'scope': {
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5299): Lines 5299-5309: Multiple inline steps (11 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'force_full': True,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5325): Lines 5325-5337: Multiple inline steps (13 lines) should be extracted into a Given/When/Then helper function. Block:
  bot_paths = BotPaths(workspace_path=workspace_directory, bot_directory=bot_directory)
  parameters = {
  'force_full': True,
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5339): Lines 5339-5344: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  assert context.all_files is True
  assert context.skip_cross_file is True
  assert 'exclude' in parameters['scope']
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5379): Lines 5379-5382: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
  from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5387): Lines 5387-5392: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
  rules_dir.mkdir(parents=True, exist_ok=True)
  (rules_dir / 'test_rule.json').write_text(json.dumps({
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5410): Lines 5410-5413: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
  from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5418): Lines 5418-5427: Multiple inline steps (10 lines) should be extracted into a Given/When/Then helper function. Block:
  rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
  rules_dir.mkdir(parents=True, exist_ok=True)
  (rules_dir / 'rule_one.json').write_text(json.dumps({
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5450): Lines 5450-5454: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
  from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5459): Lines 5459-5464: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
  rules_dir.mkdir(parents=True, exist_ok=True)
  (rules_dir / 'test_rule.json').write_text(json.dumps({
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5475): Lines 5475-5478: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  instructions = result['instructions']
  base_instructions = instructions.get('base_instructions', [])
  instructions_text = '\n'.join(str(i) for i in base_instructions)
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5487): Lines 5487-5491: Multiple inline steps (5 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
  from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5496): Lines 5496-5501: Multiple inline steps (6 lines) should be extracted into a Given/When/Then helper function. Block:
  rules_dir = bot_directory / 'behaviors' / 'code' / 'rules'
  rules_dir.mkdir(parents=True, exist_ok=True)
  (rules_dir / 'my_rule.json').write_text(json.dumps({
  ...
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_validate_knowledge_and_content_against_rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_validate_knowledge_and_content_against_rules.py:5530): Lines 5530-5533: Multiple inline steps (4 lines) should be extracted into a Given/When/Then helper function. Block:
  from agile_bot.bots.base_bot.test.test_helpers import create_actions_workflow_json
  from agile_bot.bots.base_bot.src.bot.bot_paths import BotPaths
  from agile_bot.bots.base_bot.src.bot.behavior import Behavior
  ...

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="use-given-when-then-helpers-violations">Use Given When Then Helpers: 3 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:442): Helper function "when_bot_is_created" is defined in 2 different files. Consolidate into a shared helper file based on reuse scope. Found in: test_helpers.py:442, test_perform_behavior_action.py:2523
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:753): Helper function "given_workflow_config" is defined in 2 different files. Consolidate into a shared helper file based on reuse scope. Found in: test_helpers.py:753, test_perform_behavior_action.py:315
- <span style="color: red;">[X]</span> **ERROR** - [`test\test_helpers.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/test/test_helpers.py:2525): Helper function "then_stories_match" is defined in 2 different files. Consolidate into a shared helper file based on reuse scope. Found in: test_helpers.py:2525, test_validate_knowledge_and_content_against_rules.py:445

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
*... and 72 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\tests-validation-report-2025-12-29_18-48-52.md`

