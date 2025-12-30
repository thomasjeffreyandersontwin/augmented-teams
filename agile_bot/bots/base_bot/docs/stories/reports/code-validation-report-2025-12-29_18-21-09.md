# Validation Report - Code

**Generated:** 2025-12-29 18:27:41
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 275 code file(s) against **32 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`
- **Code Files Scanned:**
  - `src\actions\action.py`
  - `src\actions\action_context.py`
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
  - `src\actions\clarify\required_context.py`
  - `src\actions\clarify\requirements_clarifications.py`
  - `src\actions\content.py`
  - `src\actions\context_data_injector.py`
  - `src\actions\guardrails.py`
  - `src\actions\help_action.py`
  - `src\actions\instructions.py`
  - `src\actions\render\evidence.py`
  - `src\actions\render\render_action.py`
  - `src\actions\render\render_config_loader.py`
  - `src\actions\render\render_instruction_builder.py`
  - `src\actions\render\render_spec.py`
  - `src\actions\render\synchronizer.py`
  - `src\actions\render\template.py`
  - `src\actions\rules\rule.py`
  - `src\actions\rules\rule_filter.py`
  - `src\actions\rules\rule_loader.py`
  - `src\actions\rules\rules.py`
  - `src\actions\rules\rules_action.py`
  - `src\actions\rules\rules_digest_guidance.py`
  - `src\actions\scoping_parameter.py`
  - `src\actions\strategy\assumptions.py`
  - `src\actions\strategy\json_persistent.py`
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
  - `src\actions\validate\story_graph.py`
  - `src\actions\validate\validate_action.py`
  - `src\actions\validate\validation_executor.py`
  - `src\actions\validate\validation_report_builder.py`
  - `src\actions\validate\validation_report_formatter.py`
  - `src\actions\validate\validation_report_writer.py`
  - `src\actions\validate\validation_scope.py`
  - `src\actions\validate\validation_stats.py`
  - `src\actions\validate\validation_violations_builder.py`
  - `src\actions\validate\violation_formatter.py`
  - `src\actions\workflow_status_builder.py`
  - `src\base_bot_cli.py`
  - `src\bot\behavior.py`
  - `src\bot\behaviors.py`
  - `src\bot\bot.py`
  - `src\bot\bot_paths.py`
  - `src\bot\merged_instructions.py`
  - `src\bot\reminders.py`
  - `src\bot\workspace.py`
  - `src\cli\action_data_collector.py`
  - `src\cli\base_bot_cli.py`
  - `src\cli\cli_action_parsers.py`
  - `src\cli\cli_code_visitor.py`
  - `src\cli\cli_command_router.py`
  - `src\cli\cli_context_builder.py`
  - `src\cli\cli_executor.py`
  - `src\cli\cli_generator.py`
  - `src\cli\cli_help_generator.py`
  - `src\cli\cli_help_renderer_visitor.py`
  - `src\cli\cli_parameter_parser.py`
  - `src\cli\cli_parser_generator.py`
  - `src\cli\cli_parser_generator_visitor.py`
  - `src\cli\cli_script_generator.py`
  - `src\cli\cursor\command_file_visitor.py`
  - `src\cli\cursor\command_generator.py`
  - `src\cli\cursor\command_renderer_visitor.py`
  - `src\cli\cursor\help_renderer_visitor.py`
  - `src\cli\cursor_command_file_visitor.py`
  - `src\cli\cursor_command_generator.py`
  - `src\cli\cursor_command_renderer_visitor.py`
  - `src\cli\cursor_help_renderer_visitor.py`
  - `src\cli\description_extractor.py`
  - `src\cli\formatter.py`
  - `src\cli\help_renderer.py`
  - `src\cli\mcp_code_visitor.py`
  - `src\cli\parameter_info_builder.py`
  - `src\cli\type_hint_converter.py`
  - `src\ext\behavior_matcher.py`
  - `src\ext\bot_matcher.py`
  - `src\ext\trigger_domain.py`
  - `src\ext\trigger_router.py`
  - `src\ext\trigger_router_entry.py`
  - `src\ext\trigger_words.py`
  - `src\generator\action_data_collector.py`
  - `src\generator\help_context.py`
  - `src\generator\orchestrator.py`
  - `src\generator\visitor.py`
  - `src\mcp\mcp_code_generator.py`
  - `src\mcp\mcp_code_visitor.py`
  - `src\mcp\mcp_config_generator.py`
  - `src\mcp\mcp_server.py`
  - `src\mcp\mcp_server_generator.py`
  - `src\mcp\server_deployer.py`
  - `src\mcp\server_restart.py`
  - `src\repl_cli\cli_base.py`
  - `src\repl_cli\cli_bot\cli_actions\build_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\clarify_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\cli_action_factory.py`
  - `src\repl_cli\cli_bot\cli_actions\cli_actions.py`
  - `src\repl_cli\cli_bot\cli_actions\render_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\strategy_cli_action.py`
  - `src\repl_cli\cli_bot\cli_actions\validate_cli_action.py`
  - `src\repl_cli\cli_bot\cli_behavior.py`
  - `src\repl_cli\cli_bot\cli_behaviors.py`
  - `src\repl_cli\cli_bot\cli_bot.py`
  - `src\repl_cli\cli_scope.py`
  - `src\repl_cli\command_parser.py`
  - `src\repl_cli\formatters\formatter_factory.py`
  - `src\repl_cli\formatters\markdown_formatter.py`
  - `src\repl_cli\formatters\output_formatter.py`
  - `src\repl_cli\formatters\terminal_formatter.py`
  - `src\repl_cli\headless\cursor_api.py`
  - `src\repl_cli\headless\error_recovery.py`
  - `src\repl_cli\headless\execution_context.py`
  - `src\repl_cli\headless\execution_result.py`
  - `src\repl_cli\headless\headless_config.py`
  - `src\repl_cli\headless\headless_session.py`
  - `src\repl_cli\headless\non_recoverable_error.py`
  - `src\repl_cli\headless\recoverable_error.py`
  - `src\repl_cli\headless\session_log.py`
  - `src\repl_cli\repl_help.py`
  - `src\repl_cli\repl_main.py`
  - `src\repl_cli\repl_results.py`
  - `src\repl_cli\repl_session.py`
  - `src\repl_cli\repl_status.py`
  - `src\repl_cli\status_display.py`
  - `src\scanners\abstraction_levels_scanner.py`
  - `src\scanners\ac_consolidation_scanner.py`
  - `src\scanners\active_language_scanner.py`
  - `src\scanners\arrange_act_assert_scanner.py`
  - `src\scanners\ascii_only_scanner.py`
  - `src\scanners\background_common_setup_scanner.py`
  - `src\scanners\bad_comments_scanner.py`
  - `src\scanners\behavioral_ac_scanner.py`
  - `src\scanners\business_readable_test_names_scanner.py`
  - `src\scanners\calculation_timing_code_scanner.py`
  - `src\scanners\calculation_timing_scanner.py`
  - `src\scanners\class_based_organization_scanner.py`
  - `src\scanners\class_size_scanner.py`
  - `src\scanners\clear_parameters_scanner.py`
  - `src\scanners\code_representation_code_scanner.py`
  - `src\scanners\code_representation_scanner.py`
  - `src\scanners\code_scanner.py`
  - `src\scanners\communication_verb_scanner.py`
  - `src\scanners\complete_refactoring_scanner.py`
  - `src\scanners\complexity_metrics.py`
  - `src\scanners\consistent_indentation_scanner.py`
  - `src\scanners\consistent_naming_scanner.py`
  - `src\scanners\consistent_vocabulary_scanner.py`
  - `src\scanners\cover_all_paths_scanner.py`
  - `src\scanners\delegation_code_scanner.py`
  - `src\scanners\delegation_scanner.py`
  - `src\scanners\dependency_chaining_code_scanner.py`
  - `src\scanners\dependency_chaining_scanner.py`
  - `src\scanners\descriptive_function_names_scanner.py`
  - `src\scanners\domain_concept_node.py`
  - `src\scanners\domain_grouping_code_scanner.py`
  - `src\scanners\domain_grouping_scanner.py`
  - `src\scanners\domain_language_code_scanner.py`
  - `src\scanners\domain_language_scanner.py`
  - `src\scanners\domain_scanner.py`
  - `src\scanners\duplication_scanner.py`
  - `src\scanners\encapsulation_scanner.py`
  - `src\scanners\enumerate_ac_permutations_scanner.py`
  - `src\scanners\enumerate_stories_scanner.py`
  - `src\scanners\error_handling_isolation_scanner.py`
  - `src\scanners\exact_variable_names_scanner.py`
  - `src\scanners\exception_classification_scanner.py`
  - `src\scanners\exception_handling_scanner.py`
  - `src\scanners\excessive_guards_scanner.py`
  - `src\scanners\exhaustive_decomposition_scanner.py`
  - `src\scanners\explicit_dependencies_scanner.py`
  - `src\scanners\fixture_placement_scanner.py`
  - `src\scanners\function_size_scanner.py`
  - `src\scanners\generic_capability_scanner.py`
  - `src\scanners\given_precondition_scanner.py`
  - `src\scanners\given_state_not_actions_scanner.py`
  - `src\scanners\given_when_then_helpers_scanner.py`
  - `src\scanners\implementation_details_scanner.py`
  - `src\scanners\import_placement_scanner.py`
  - `src\scanners\increment_folder_structure_scanner.py`
  - `src\scanners\intention_revealing_names_scanner.py`
  - `src\scanners\invest_principles_scanner.py`
  - `src\scanners\meaningful_context_scanner.py`
  - `src\scanners\minimize_mutable_state_scanner.py`
  - `src\scanners\mock_boundaries_scanner.py`
  - `src\scanners\natural_english_code_scanner.py`
  - `src\scanners\natural_english_scanner.py`
  - `src\scanners\no_fallbacks_scanner.py`
  - `src\scanners\no_guard_clauses_scanner.py`
  - `src\scanners\noun_redundancy_scanner.py`
  - `src\scanners\observable_behavior_scanner.py`
  - `src\scanners\one_concept_per_test_scanner.py`
  - `src\scanners\open_closed_principle_scanner.py`
  - `src\scanners\parameterized_tests_scanner.py`
  - `src\scanners\plain_english_scenarios_scanner.py`
  - `src\scanners\prefer_object_model_over_config_scanner.py`
  - `src\scanners\present_ac_consolidation_scanner.py`
  - `src\scanners\primitive_vs_object_scanner.py`
  - `src\scanners\property_encapsulation_code_scanner.py`
  - `src\scanners\property_encapsulation_scanner.py`
  - `src\scanners\real_implementations_scanner.py`
  - `src\scanners\resource_oriented_code_scanner.py`
  - `src\scanners\resource_oriented_design_scanner.py`
  - `src\scanners\resources\ast_elements.py`
  - `src\scanners\resources\block.py`
  - `src\scanners\resources\block_extractor.py`
  - `src\scanners\resources\file.py`
  - `src\scanners\resources\line.py`
  - `src\scanners\resources\scan.py`
  - `src\scanners\resources\scope.py`
  - `src\scanners\resources\violation.py`
  - `src\scanners\scanner.py`
  - `src\scanners\scanner_execution_error.py`
  - `src\scanners\scanner_loader.py`
  - `src\scanners\scanner_orchestrator.py`
  - `src\scanners\scanner_registry.py`
  - `src\scanners\scanner_status_formatter.py`
  - `src\scanners\scenario_outline_scanner.py`
  - `src\scanners\scenario_specific_given_scanner.py`
  - `src\scanners\scenarios_cover_all_cases_scanner.py`
  - `src\scanners\scenarios_on_story_docs_scanner.py`
  - `src\scanners\separate_concerns_scanner.py`
  - `src\scanners\simplify_control_flow_scanner.py`
  - `src\scanners\single_responsibility_scanner.py`
  - `src\scanners\specification_match_scanner.py`
  - `src\scanners\specificity_scanner.py`
  - `src\scanners\spine_optional_scanner.py`
  - `src\scanners\story_enumeration_scanner.py`
  - `src\scanners\story_filename_scanner.py`
  - `src\scanners\story_graph_match_scanner.py`
  - `src\scanners\story_map.py`
  - `src\scanners\story_scanner.py`
  - `src\scanners\story_sizing_scanner.py`
  - `src\scanners\swallowed_exceptions_scanner.py`
  - `src\scanners\technical_abstraction_code_scanner.py`
  - `src\scanners\technical_abstraction_scanner.py`
  - `src\scanners\technical_language_scanner.py`
  - `src\scanners\test_boundary_behavior_scanner.py`
  - `src\scanners\test_file_naming_scanner.py`
  - `src\scanners\test_quality_scanner.py`
  - `src\scanners\test_scanner.py`
  - `src\scanners\third_party_isolation_scanner.py`
  - `src\scanners\type_safety_scanner.py`
  - `src\scanners\ubiquitous_language_scanner.py`
  - `src\scanners\unnecessary_parameter_passing_scanner.py`
  - `src\scanners\useless_comments_scanner.py`
  - `src\scanners\validation_scanner_status_builder.py`
  - `src\scanners\verb_noun_scanner.py`
  - `src\scanners\vertical_density_scanner.py`
  - `src\scanners\vertical_slice_scanner.py`
  - `src\scanners\violation.py`
  - `src\scanners\vocabulary_helper.py`
  - `src\story_graph\domain.py`
  - `src\story_graph\nodes.py`
  - `src\utils.py`
  - **Total:** 275 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: GOOD - Minor Issues

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 25 | No violations found |
| 🟨 Rules with Warnings | 3 | Found 6 warning violation(s) |
| 🟥 Rules with Errors | 1 | Found 1 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟨 **[Use Domain Language](#use-domain-language)** - 72 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟨 **[Provide Meaningful Context](#provide-meaningful-context)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟩 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟩 **[Eliminate Duplication](#eliminate-duplication)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
- 🟩 **[Enforce Encapsulation](#enforce-encapsulation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Maintain Vertical Density](#maintain-vertical-density)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟩 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟩 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟩 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟩 **[Use Consistent Indentation](#use-consistent-indentation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.consistent_indentation_scanner.ConsistentIndentationScanner`
- 🟩 **[Use Consistent Naming](#use-consistent-naming)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.consistent_naming_scanner.ConsistentNamingScanner`
- 🟩 **[Use Exceptions Properly](#use-exceptions-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exception_handling_scanner.ExceptionHandlingScanner`
- 🟩 **[Use Explicit Dependencies](#use-explicit-dependencies)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.explicit_dependencies_scanner.ExplicitDependenciesScanner`
- 🟩 **[Use Natural English](#use-natural-english)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.natural_english_code_scanner.NaturalEnglishCodeScanner`
- 🟩 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 1 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 3 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 2 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 1 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - CLEAN (0 violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - CLEAN (0 violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="delegate-to-lowest-level">Delegate To Lowest Level</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.delegation_code_scanner.DelegationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - CLEAN (0 violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="favor-code-representation">Favor Code Representation</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code should represent domain concepts directly. Domain models should match code. If code doesn't match domain concepts, refactor the code rather than creating abstract domain models.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="group-by-domain">Group By Domain</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must be organized by domain area and relationships, not by technical layers, object types, or architectural concerns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-business-logic-behind-properties">Hide Business Logic Behind Properties</span> - CLEAN (0 violations)
**Description:** CRITICAL: Hide business logic behind properties. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must hide calculations. Properties hide logic that occurs—it may be computed on-demand, cached, pre-computed, or loaded from storage. The caller shouldn't know or care when the values are calculated / determined.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="keep-functions-single-responsibility">Keep Functions Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Functions should do one thing and do it well, with no hidden side effects. Each function must have a single, well-defined responsibility.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="maintain-vertical-density">Maintain Vertical Density</span> - CLEAN (0 violations)
**Description:** Related code should be visually close. Group related concepts together, declare variables close to usage, and keep files under 500 lines when possible.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.vertical_density_scanner.VerticalDensityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="place-imports-at-top">Place Imports At Top</span> - CLEAN (0 violations)
**Description:** Place all import statements at the top of the file, after module docstrings and comments, but before any executable code. This improves readability and makes dependencies clear.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="prefer-object-model-over-config">Prefer Object Model Over Config</span> - CLEAN (0 violations)
**Description:** Use existing object model to access information instead of directly accessing configuration files
**Scanner:** `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
**Execution Status:** EXECUTION_SUCCESS

*... and 12 more rules*

## Violations Found

**Total Violations:** 79
- **File-by-File Violations:** 79
- **Cross-File Violations:** 0

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:39): Function "starts_session" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return self._session_id
        
        def starts_session(self, instructions: str) -> APIResponse:
            headers = self._builds_headers()
            payload = {
                'instructions': instructions,
                'mode': 'headless'
            }
            
            try:
                response = requests.post(
                    f'{self.base_url}/sessions',
                    headers=headers,
                    json=payload,
                    timeout=30
                )
                
                if response.status_code == 401:
                    raise NonRecoverableError('Invalid API key - authentication failed')
                
                if response.status_code == 429:
                    raise RecoverableError('Rate limited - please retry')
                
                if response.status_code >= 500:
                    raise RecoverableError(f'Server error: {response.status_code}')
                
                response.raise_for_status()
                data = response.json()
                
                self._session_id = data.get('session_id')
                return APIResponse(
                    status='running',
                    message='Session started',
                    session_id=self._session_id,
                    progress=data.get('progress', '')
                )
                
            except requests.exceptions.ConnectionError as e:
                raise RecoverableError(f'Connection failed: {e}')
            except requests.exceptions.Timeout as e:
                raise RecoverableError(f'Request timed out: {e}')
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:79): Function "sends_instruction" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
                raise RecoverableError(f'Request timed out: {e}')
        
        def sends_instruction(self, instruction: str) -> APIResponse:
            if not self._session_id:
                raise NonRecoverableError('No active session - call starts_session first')
            
            headers = self._builds_headers()
            payload = {
                'instruction': instruction
            }
            
            try:
                response = requests.post(
                    f'{self.base_url}/sessions/{self._session_id}/messages',
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                
                if response.status_code == 401:
                    raise NonRecoverableError('Invalid API key')
                
                if response.status_code >= 500:
                    raise RecoverableError(f'Server error: {response.status_code}')
                
                response.raise_for_status()
                data = response.json()
                
                return self._parses_response(data)
                
            except requests.exceptions.ConnectionError as e:
                raise RecoverableError(f'Connection failed: {e}')
            except requests.exceptions.Timeout as e:
                raise RecoverableError(f'Request timed out: {e}')
        
    ```

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:145): Except block only contains pass at line 145 - exceptions must be logged or rethrown, never swallowed

    ```python
                    timeout=10
                )
            except requests.exceptions.RequestException:
                pass
            
    ```

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:60): Line 60 contains magic number - replace with named constant

    ```python
                
                if response.status_code >= 500:
                    raise RecoverableError(f'Server error: {response.status_code}')
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:93): Line 93 contains magic number - replace with named constant

    ```python
                    json=payload,
                    timeout=60
                )
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:99): Line 99 contains magic number - replace with named constant

    ```python
                
                if response.status_code >= 500:
                    raise RecoverableError(f'Server error: {response.status_code}')
    ```

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:151): Function "_executes_with_recovery" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return final
        
        def _executes_with_recovery(self, instructions: str, context_loaded: bool) -> ExecutionResult:
            while self._error_recovery.can_retry():
                try:
                    return self._executes_with_api(instructions, context_loaded)
                except RecoverableError as e:
                    self._error_recovery.increment_attempt()
                    self.log.appends_response(f'Recoverable error: {e}. Attempt {self._error_recovery.current_attempts}')
                    
                    if self._error_recovery.can_retry():
                        self._error_recovery.wait_before_retry(duration=2.0)
                        if self._api:
                            self._api.terminates_session()
                    else:
        # ... (truncated)
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 72 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:15): Class "CliExecutor" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:17): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:17): Function "__init__" uses parameter name "cli_instance" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:20): Function "execute_and_output" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:20): Function "execute_and_output" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:20): Function "execute_and_output" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:32): Function "_log_execution_info" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:32): Function "_log_execution_info" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:32): Function "_log_execution_info" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:38): Function "_execute_headless" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:38): Function "_execute_headless" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:82): Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:102): Function "_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:102): Function "_execute_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:102): Function "_execute_command" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:114): Function "_handle_working_dir_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:114): Function "_handle_working_dir_command" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_executor.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_executor.py:133): Function "_output_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:9): Function "parse_arguments" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:9): Function "parse_arguments" uses parameter name "description" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:18): Function "_build_remaining_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:18): Function "_build_remaining_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:18): Function "_build_remaining_args" uses parameter name "unknown" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:36): Function "_create_argument_parser" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:36): Function "_create_argument_parser" uses parameter name "description" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:55): Function "_relocate_file_path_from_action" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:55): Function "_relocate_file_path_from_action" uses parameter name "unknown" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:62): Function "_build_params_from_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:62): Function "_build_params_from_args" uses parameter name "unrecognized_flags" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:84): Function "_looks_like_file_path" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:89): Function "_looks_like_directory_path" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:96): Function "_append_to_param" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:105): Function "_parse_key_value_arg" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:105): Function "_parse_key_value_arg" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:105): Function "_parse_key_value_arg" uses parameter name "arg_list" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:147): Function "_parse_file_path_arg" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:155): Function "_parse_context_arg" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:155): Function "_parse_context_arg" uses parameter name "arg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:164): Function "_process_unrecognized_flags" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:164): Function "_process_unrecognized_flags" uses parameter name "unrecognized_flags" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:183): Function "_process_context_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\cli\cli_parameter_parser.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/cli/cli_parameter_parser.py:183): Function "_process_context_args" uses parameter name "context_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:18): Class "APIResponse" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:28): Class "CursorHeadlessAPI" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:30): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:30): Function "__init__" uses parameter name "api_key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:30): Function "__init__" uses parameter name "base_url" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:36): Function "session_id" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:39): Function "starts_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:39): Function "starts_session" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:79): Function "sends_instruction" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:79): Function "sends_instruction" uses parameter name "instruction" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:112): Function "polls_session_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:133): Function "terminates_session" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:150): Function "_builds_headers" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\cursor_api.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/cursor_api.py:157): Function "_parses_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:17): Class "HeadlessSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:19): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:27): Function "invokes" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:27): Function "invokes" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:47): Function "invokes_operation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:47): Function "invokes_operation" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:119): Function "_loads_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:124): Function "_prepares_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:124): Function "_prepares_instructions" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:124): Function "_prepares_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:151): Function "_executes_with_recovery" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:151): Function "_executes_with_recovery" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:151): Function "_executes_with_recovery" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:168): Function "_executes_with_api" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:168): Function "_executes_with_api" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:168): Function "_executes_with_api" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

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
*... and 56 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-29_18-21-09.md`

