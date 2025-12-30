# Validation Report - Code

**Generated:** 2025-12-30 02:59:40
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

### 🟨 Overall Status: NEEDS ATTENTION

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 19 | No violations found |
| 🟨 Rules with Warnings | 6 | Found 24 warning violation(s) |
| 🟥 Rules with Errors | 3 | Found 77 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟨 **[Use Domain Language](#use-domain-language)** - 105 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 59 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 11 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
- 🟨 **[Enforce Encapsulation](#enforce-encapsulation)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-encapsulation-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟩 **[Provide Meaningful Context](#provide-meaningful-context)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
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

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 59 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 14 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 4 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 9 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 5 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 4 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 3 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 2 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - 1 WARNING(S) - [View Details](#enforce-encapsulation-violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
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

### 🟩 Rule: <span id="keep-functions-single-responsibility">Keep Functions Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Functions should do one thing and do it well, with no hidden side effects. Each function must have a single, well-defined responsibility.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
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

**Total Violations:** 217
- **File-by-File Violations:** 205
- **Cross-File Violations:** 12

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 4 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:97): Line 97: Variable truthiness check detected (if not matches_include:). Assume variable exists - let code fail fast if missing.

    ```python
                            pass
                    
                    if not matches_include:
                        continue
                
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:111): Line 111: Variable truthiness check detected (if matches_exclude:). Assume variable exists - let code fail fast if missing.

    ```python
                            pass
                    
                    if matches_exclude:
                        continue
                
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:182): Line 182: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

    ```python
        @classmethod
        def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
            if not data:
                return cls()
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1484): Line 1484: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

    ```python
        def parse_command_parameters(self, args: str) -> Dict[str, Any]:
            params = {}
            if not args:
                return params
            
    ```

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:191): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (display_current_state:191-202):
    ```python
    lines.append('```')
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion             ...
    ```

  Location (display_current_state:226-234):
    ```python
    lines.append(formatter.subsection_separator())
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:469): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_handle_next_command:469-488):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```

  Location (_handle_back_command:505-524):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```

#### <span id="enforce-encapsulation-violations">Enforce Encapsulation: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:725): Method "_handle_scope_command" in Test class [REPLSession](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:725) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:126): Class "Scope" is 314 lines - should be under 300 lines (extract related methods into separate classes)

```python

@dataclass
class Scope:
    """Scope for filtering bot operations to specific content.
    
    Uses KnowledgeGraphFilter for story/epic/increment scoping
    and FileFilter for file-based scoping. Maintains backward compatibility
    with type/value/exclude API.
    
    The Scope object is responsible for its own persistence to the bot state file.
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" is 1582 lines - should be under 300 lines (extract related methods into separate classes)

```python


class REPLSession:
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        tty_result = self.detect_tty()
        self.formatter = FormatterFactory.create_formatter(tty_detected=tty_result.tty_detected)
    
    @property
    # ... (truncated)
```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:75): Function "filter_files" is 39 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return False
        
        def filter_files(self, file_list: List[Path]) -> List[Path]:
            """Filter file list to only files matching this filter."""
            if not self.include_patterns and not self.exclude_patterns:
                return file_list
            
            from pathlib import PurePath
            filtered = []
            
            for file_path in file_list:
                file_str = str(file_path).replace('\\', '/')
                file_path_obj = PurePath(file_str)
                
                if self.include_patterns:
                    matches_include = False
                    for pattern in self.include_patterns:
                        pattern_normalized = pattern.replace('\\', '/')
                        try:
                            if (file_path_obj.match(pattern_normalized) or
                                file_path_obj.match(f'**/{pattern_normalized}') or
                                pattern_normalized in file_str):
                                matches_include = True
                                break
                        except (ValueError, TypeError):
                            if pattern_normalized in file_str:
                                matches_include = True
                                break
                    
                    if not matches_include:
                        continue
                
                if self.exclude_patterns:
                    matches_exclude = False
                    for pattern in self.exclude_patterns:
                        pattern_normalized = pattern.replace('\\', '/')
                        try:
                            if (file_path_obj.match(pattern_normalized) or
                                file_path_obj.match(f'**/{pattern_normalized}')):
                                matches_exclude = True
                                break
                        except (ValueError, TypeError):
                            pass
                    
                    if matches_exclude:
                        continue
                
                filtered.append(file_path)
            
            return filtered
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:258): Function "to_display_lines" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return workspace_directory / 'behavior_action_state.json'
        
        def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
            """Render scope as display lines with hierarchical expansion.
            
            Returns plain text lines showing scope filter and matched items.
            """
            from pathlib import Path
            import json
            
            lines = []
            
            # Show the scope filter value
            filter_str = ', '.join(self.value) if isinstance(self.value, list) else str(self.value)
            lines.append(f"Scope Filter: {filter_str}")
            
            if self.type == ScopeType.STORY:
                story_graph_path = workspace_directory / 'docs' / 'stories' / 'story-graph.json'
                if story_graph_path.exists():
                    try:
                        graph_data = json.loads(story_graph_path.read_text(encoding='utf-8'))
                        matched_items = self._find_scope_matches_in_graph(graph_data, self.value)
                        lines.extend(matched_items)
                    except Exception:
                        # Fallback to simple list
                        for item in (self.value if isinstance(self.value, list) else [self.value]):
                            lines.append(f"  - {item}")
                else:
                    for item in (self.value if isinstance(self.value, list) else [self.value]):
                        lines.append(f"  - {item}")
            elif self.type == ScopeType.FILES:
                # Expand file paths to show all actual files that will be scanned
                expanded_files = self._expand_file_paths(workspace_directory)
                if expanded_files:
                    for file_path in sorted(expanded_files):
                        # Show relative path from workspace
                        try:
                            rel_path = file_path.relative_to(workspace_directory)
                            lines.append(f"  - {rel_path}")
                        except ValueError:
                            lines.append(f"  - {file_path}")
                else:
                    # Fallback to showing the scope value if expansion fails
                    for item in (self.value if isinstance(self.value, list) else [self.value]):
                        lines.append(f"  - {item} (no files found)")
            else:
                if isinstance(self.value, list):
                    for item in self.value:
                        lines.append(f"  - {item}")
                else:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 83 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return True
        
        def display_current_state(self, full=False) -> REPLStateDisplay:
            """Single source of truth for displaying current bot state.
            
            Returns REPLStateDisplay with formatted status output showing:
            - Bot name and paths
            - Current position header
            - Scope filter (if set)
            - Progress in workflow
            - Hierarchical behavior/action/operation tree
            """
            if not self.has_current_action:
                if not self._initialize_to_first_behavior_action():
                    return REPLStateDisplay(
                        output="No behaviors available\n\n  help          - Show detailed help\n  exit          - Exit REPL",
                        state_loaded=False
                    )
                return self.display_current_state(full=full)
            
            lines = []
            formatter = self.formatter
            
            # Get bot name from bot_directory
            if self.bot and hasattr(self.bot, 'bot_paths'):
                bot_name = self.bot.bot_paths.bot_directory.name
            else:
                bot_name = 'UNKNOWN'
            
            # THICK LINE at top
            lines.append(formatter.section_separator())
            lines.append("")
            
            # Bot section header
            lines.append(f"## {formatter.bot_icon()} Bot: {bot_name}")
            
            if self.bot:
                bot_path = self.bot.bot_paths.bot_directory if hasattr(self.bot, 'bot_paths') else 'Unknown'
                lines.append(f"**Bot Path:**")
                lines.append("```")
                lines.append(str(bot_path))
                lines.append("```")
            
            lines.append("")
            
            # Workspace section
            workspace_name = self.workspace_directory.name if hasattr(self.workspace_directory, 'name') else 'base_bot'
            lines.append(f"{formatter.workspace_icon()} **Workspace:** {workspace_name}")
            lines.append(f"**Path:**")
            lines.append("```")
        # ... (truncated)
    ```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 11 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:258): Function "to_display_lines" is 51 lines - consider improving vertical density by declaring variables near usage

    ```python
            return workspace_directory / 'behavior_action_state.json'
        
        def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
            """Render scope as display lines with hierarchical expansion.
            
            Returns plain text lines showing scope filter and matched items.
            """
            from pathlib import Path
            import json
            
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 114 lines - consider improving vertical density by declaring variables near usage

    ```python
            return True
        
        def display_current_state(self, full=False) -> REPLStateDisplay:
            """Single source of truth for displaying current bot state.
            
            Returns REPLStateDisplay with formatted status output showing:
            - Bot name and paths
            - Current position header
            - Scope filter (if set)
            - Progress in workflow
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:268): Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

    ```python
            return state_display.output
        
        def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
            """Convert a domain method result to a REPL response.
            
            Args:
                result: Dict returned from domain method
                command: The command that was executed
            
            Returns:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:339): Function "_handle_simple_command" is 59 lines - consider improving vertical density by declaring variables near usage

    ```python
            return self._handle_simple_command(command)
        
        def _handle_simple_command(self, command: str) -> REPLCommandResponse:
            parts = command.split(maxsplit=1)
            command_verb = parts[0].lower()
            command_args = parts[1] if len(parts) > 1 else ""
            
            # Meta commands
            if command_verb == 'help':
                return self._handle_help_command(command_args)
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:549): Function "_handle_instructions_command" is 56 lines - consider improving vertical density by declaring variables near usage

    ```python
            )
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            import sys
            print(f"[DEBUG] _handle_instructions_command called with args: '{args}'", file=sys.stderr)
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action to get instructions for",
                    response="ERROR: No current action",
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:627): Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

    ```python
                )
        
        def _handle_confirm_command(self) -> REPLCommandResponse:
            """Handle confirm command"""
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action to confirm",
                    response="ERROR: No current action",
                    status="error"
                )
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:701): Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

    ```python
            )
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
                # Show current scope
                output = self.cli_bot.get_scope_display()
                return REPLCommandResponse(
                    output=output,
                    response=output,
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:842): Function "_execute_operation_locally" is 60 lines - consider improving vertical density by declaring variables near usage

    ```python
                return None, args.strip().strip('"').strip("'")
        
        def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
            """Execute a CLI operation locally and return its output.
            
            Args:
                target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
                cli_args: CLI arguments like '--scope "X"'
            
            Returns:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1133): Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

    ```python
                pass
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
            parts = command.split()
            dot_path = parts[0]
            args = ' '.join(parts[1:]) if len(parts) > 1 else ""
            
            path_parts = dot_path.split('.')
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1261): Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

    ```python
                )
        
        def _handle_action_shortcut(self, action_name: str, args_str: str) -> REPLCommandResponse:
            args_str = args_str.strip()
            
            # Parse CLI-style arguments (--message, --scope, etc.)
            cli_args = []
            subcommand = None
            
            if args_str:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1366): Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

    ```python
            return converted_args
        
        def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
            if not self.has_current_behavior:
                return REPLCommandResponse(
                    output="ERROR: No current behavior set. Please select a behavior first.",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            
        # ... (truncated)
    ```

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 4 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:250): Except block only contains pass at line 250 - exceptions must be logged or rethrown, never swallowed

    ```python
                    del state_data['scope']
                    state_file.write_text(json.dumps(state_data, indent=2))
            except (json.JSONDecodeError, IOError):
                pass
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:114): Except block only contains pass at line 114 - exceptions must be logged or rethrown, never swallowed

    ```python
                                matches_exclude = True
                                break
                        except (ValueError, TypeError):
                            pass
                    
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1130): Except block only contains pass at line 1130 - exceptions must be logged or rethrown, never swallowed

    ```python
                state_data['completed_behaviors'] = completed
                state_file.write_text(json.dumps(state_data, indent=2))
            except (json.JSONDecodeError, IOError):
                pass
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:78): Except block only contains pass at line 78 - exceptions must be logged or rethrown, never swallowed

    ```python
                    state_data = json.loads(state_file.read_text())
                    return state_data.get('action_phase', 'not_started')
                except (json.JSONDecodeError, IOError):
                    pass
            return 'not_started'
    ```

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 5 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:280): Fallback/legacy support code found (comment at line 280, code at line 281) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:298): Fallback/legacy support code found (comment at line 298, code at line 299) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:72): Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:239): Fallback/legacy support code found (comment at line 239, code at line 240) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1509): Fallback/legacy support code found (comment at line 1509, code at line 1510) - complete refactoring by removing old pattern support

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 9 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:75): Function "filter_files" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def filter_files(self, file_list: List[Path]) -> List[Path]:
            """Filter file list to only files matching this filter."""
            if not self.include_patterns and not self.exclude_patterns:
                return file_list
            
            from pathlib import PurePath
            filtered = []
            
            for file_path in file_list:
                file_str = str(file_path).replace('\\', '/')
                file_path_obj = PurePath(file_str)
                
                if self.include_patterns:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:144): Function "__post_init__" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
        _file_filter: Optional[FileFilter] = field(default=None, repr=False)
        
        def __post_init__(self):
            """Initialize filter objects from type/value/exclude."""
            # Create knowledge graph filter for story/epic/increment types
            if self.type in (ScopeType.STORY, ScopeType.EPIC, ScopeType.INCREMENT):
                if self.type == ScopeType.STORY:
                    self._knowledge_graph_filter = KnowledgeGraphFilter(stories=self.value)
                elif self.type == ScopeType.EPIC:
                    self._knowledge_graph_filter = KnowledgeGraphFilter(epics=self.value)
                elif self.type == ScopeType.INCREMENT:
                    # Convert string values to integers
                    increments = [int(v) if isinstance(v, str) and v.isdigit() else v for v in self.value]
                    self._knowledge_graph_filter = KnowledgeGraphFilter(increments=increments)
            
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:258): Function "to_display_lines" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return workspace_directory / 'behavior_action_state.json'
        
        def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
            """Render scope as display lines with hierarchical expansion.
            
            Returns plain text lines showing scope filter and matched items.
            """
            from pathlib import Path
            import json
            
            lines = []
            
            # Show the scope filter value
            filter_str = ', '.join(self.value) if isinstance(self.value, list) else str(self.value)
            lines.append(f"Scope Filter: {filter_str}")
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:310): Function "_expand_file_paths" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return lines
        
        def _expand_file_paths(self, workspace_directory: 'Path') -> List['Path']:
            """Expand file scope paths to actual files that will be scanned."""
            from pathlib import Path
            import glob as glob_module
            
            all_files = []
            # Ensure value is treated as a list
            paths = self.value if isinstance(self.value, list) else [self.value]
            
            for path_str in paths:
                # Check if path contains glob patterns
                has_glob = any(char in path_str for char in ['*', '?', '['])
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:438): Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            )
        
        def _handle_current_command(self) -> REPLCommandResponse:
            """Re-execute current operation based on progress state"""
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action",
                    response="ERROR: No current action",
                    status="error"
                )
            
            # Extract operation from progress (behavior.action.operation)
            progress = self.get_progress_line()
            if '.' in progress and 'Progress: ' in progress:
                parts = progress.replace('Progress: ', '').split('.')
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:701): Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            )
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
                # Show current scope
                output = self.cli_bot.get_scope_display()
                return REPLCommandResponse(
                    output=output,
                    response=output,
                    status="success"
                )
            
            # Handle "all" - clears the scope filter
            if args.lower() == 'all':
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:842): Function "_execute_operation_locally" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return None, args.strip().strip('"').strip("'")
        
        def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
            """Execute a CLI operation locally and return its output.
            
            Args:
                target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
                cli_args: CLI arguments like '--scope "X"'
            
            Returns:
                Output from the operation (instructions, submit result, confirm result, etc.)
            """
            # Parse target
            parts = target.split('.')
            if len(parts) < 2:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1133): Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                pass
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
            parts = command.split()
            dot_path = parts[0]
            args = ' '.join(parts[1:]) if len(parts) > 1 else ""
            
            path_parts = dot_path.split('.')
            
            # . alone means current position
            if dot_path == '.':
                return self._handle_current_command()
            
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1329): Function "_convert_repl_scope_to_cli_format" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return args_str.split()
        
        def _convert_repl_scope_to_cli_format(self, cli_args: list) -> list:
            import json
            converted_args = []
            i = 0
            while i < len(cli_args):
                arg = cli_args[i]
                if arg == '--scope' and i + 1 < len(cli_args):
                    scope_value = cli_args[i + 1]
                    if scope_value.startswith(('file:', 'files:')):
                        prefix = 'file:' if scope_value.startswith('file:') else 'files:'
                        paths = scope_value[len(prefix):].split(',')
                        paths = [p.strip() for p in paths if p.strip()]
                        json_scope = json.dumps({"type": "files", "value": paths})
        # ... (truncated)
    ```

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 59 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:26): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    @dataclass
    class KnowledgeGraphFilter:
        """Filters content by knowledge graph nodes (stories, epics, increments).
        
        Used for filtering operations to specific parts of the story graph.
        """
        stories: List[str] = field(default_factory=list)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:35): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def matches_story(self, story_name: str) -> bool:
            """Check if story matches filter."""
            if not self.stories:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def matches_epic(self, epic_name: str) -> bool:
            """Check if epic matches filter."""
            if not self.epics:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:47): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def filter_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
            """Filter knowledge graph to only nodes matching this filter."""
            # For now, return full graph if no filters specified
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:57): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    @dataclass
    class FileFilter:
        """Filters files by path patterns.
        
        Supports glob patterns for include/exclude.
        """
        include_patterns: List[str] = field(default_factory=list)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:65): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def matches_file(self, file_path: Path) -> bool:
            """Check if file matches the filter."""
            if not self.include_patterns:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:76): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def filter_files(self, file_list: List[Path]) -> List[Path]:
            """Filter file list to only files matching this filter."""
            if not self.include_patterns and not self.exclude_patterns:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:127): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    @dataclass
    class Scope:
        """Scope for filtering bot operations to specific content.
        
        Uses KnowledgeGraphFilter for story/epic/increment scoping
        and FileFilter for file-based scoping. Maintains backward compatibility
        with type/value/exclude API.
        
        The Scope object is responsible for its own persistence to the bot state file.
        """
        type: ScopeType = ScopeType.ALL
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:145): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def __post_init__(self):
            """Initialize filter objects from type/value/exclude."""
            # Create knowledge graph filter for story/epic/increment types
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:166): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def knowledge_graph_filter(self) -> Optional[KnowledgeGraphFilter]:
            """Get knowledge graph filter (lazy init if needed)."""
            return self._knowledge_graph_filter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:171): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def file_filter(self) -> Optional[FileFilter]:
            """Get file filter (lazy init if needed)."""
            return self._file_filter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:175): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def filters_knowledge_graph(self, knowledge_graph: Dict[str, Any]) -> Dict[str, Any]:
            """Filter knowledge graph using knowledge graph filter."""
            if self._knowledge_graph_filter:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:181): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def filters_files(self, file_list: List[Path]) -> List[Path]:
            """Filter file list using file filter."""
            if self._file_filter:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:213): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def apply_to_bot(self, workspace_directory: 'Path') -> None:
            """Clear old scope and store this scope to the bot state file.
            
            The Scope object is responsible for its own persistence.
            """
            import json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:238): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def clear_from_bot(workspace_directory: 'Path') -> None:
            """Remove scope from the bot state file."""
            import json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:255): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def _get_state_file_path(workspace_directory: 'Path') -> 'Path':
            """Get path to the bot state file."""
            return workspace_directory / 'behavior_action_state.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:259): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def to_display_lines(self, workspace_directory: 'Path') -> List[str]:
            """Render scope as display lines with hierarchical expansion.
            
            Returns plain text lines showing scope filter and matched items.
            """
            from pathlib import Path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:311): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _expand_file_paths(self, workspace_directory: 'Path') -> List['Path']:
            """Expand file scope paths to actual files that will be scanned."""
            from pathlib import Path
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:353): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _find_scope_matches_in_graph(self, graph_data: Dict[str, Any], scope_values: List[str]) -> List[str]:
            """Find and display scope matches from story graph."""
            lines = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:367): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _search_for_scope_match(self, epics: List[Dict], scope_val: str) -> Optional[List[str]]:
            """Search for scope match and return formatted lines with full hierarchy."""
            for epic in epics:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:379): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _search_sub_epics(self, sub_epics: List[Dict], scope_val: str) -> Optional[List[str]]:
            """Search sub-epics for scope match."""
            for sub_epic in sub_epics:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:391): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _search_stories(self, sub_epic: Dict, scope_val: str) -> Optional[List[str]]:
            """Search stories for scope match."""
            for story_group in sub_epic.get('story_groups', []):
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:404): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _matches_name(self, name: str, pattern: str) -> bool:
            """Check if pattern matches name (case-insensitive)."""
            return pattern.lower() in name.lower()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:408): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _format_node_with_children(self, node: Dict[str, Any], node_type: str, indent: int) -> List[str]:
            """Format a node and its children recursively."""
            lines = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:466): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def __post_init__(self):
            """Normalize strategy context fields and keep backward compatibility."""
            # Default collections to empty to simplify downstream checks
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:477): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def get_decisions(self) -> Dict[str, Any]:
            """Get all decision attributes (exclude assumption fields and internals)."""
            excluded = {'assumptions', 'assumptions_made', 'decisions_made'}
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:488): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def assumptions_list(self) -> Optional[List[str]]:
            """Alias to keep existing code using context.assumptions working."""
            return self.assumptions or self.assumptions_made
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:324): Useless comment: "# Handle glob patterns" - delete it or improve the code instead

    ```python
                
                if has_glob:
                    # Handle glob patterns
                    # If not absolute, make it relative to workspace
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:145): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def display_current_state(self, full=False) -> REPLStateDisplay:
            """Single source of truth for displaying current bot state.
            
            Returns REPLStateDisplay with formatted status output showing:
            - Bot name and paths
            - Current position header
            - Scope filter (if set)
            - Progress in workflow
            - Hierarchical behavior/action/operation tree
            """
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:260): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def get_context_header_for_ai(self) -> str:
            """Get status display as a string for AI context headers.
            
            This is a convenience method that extracts just the output string
            from display_current_state().
            """
            state_display = self.display_current_state()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:269): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _convert_domain_result_to_repl_response(self, result: Dict[str, Any], command: str) -> REPLCommandResponse:
            """Convert a domain method result to a REPL response.
            
            Args:
                result: Dict returned from domain method
                command: The command that was executed
            
            Returns:
                REPLCommandResponse with appropriate formatting
            """
            status = result.get('status', 'success')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:400): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
            """Handle help command using bot.help"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:430): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_status_command(self) -> REPLCommandResponse:
            """Handle status command using bot.status"""
            state_display = self.display_current_state(full=True)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:439): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_current_command(self) -> REPLCommandResponse:
            """Re-execute current operation based on progress state"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:468): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_next_command(self) -> REPLCommandResponse:
            """Handle next/advance navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:504): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_back_command(self) -> REPLCommandResponse:
            """Handle back/previous navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:550): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            import sys
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:607): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
            """Handle submit command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:628): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_confirm_command(self) -> REPLCommandResponse:
            """Handle confirm command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:683): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
            """Handle path/workspace command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:702): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:768): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _validate_headless_ready(self, args: str) -> tuple[bool, REPLCommandResponse | None, any]:
            """Validate that headless mode is ready to execute.
            
            Returns:
                Tuple of (is_valid, error_response, config)
                - If is_valid is False, error_response contains the error to return
                - If is_valid is True, config contains the loaded configuration
            """
            from agile_bot.bots.base_bot.src.repl_cli.headless.headless_config import HeadlessConfig
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:809): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _parse_headless_args(self, args: str) -> tuple[str | None, str]:
            """Parse headless command args into target and message.
            
            Args:
                args: Raw argument string (e.g., 'test.build "message" --scope "X"')
            
            Returns:
                Tuple of (target, message) where:
                - target is the CLI target (e.g., 'test.build') or None
                - message is the rest (message + CLI args)
            """
            import shlex
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:843): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _execute_operation_locally(self, target: str, cli_args: str = "") -> str:
            """Execute a CLI operation locally and return its output.
            
            Args:
                target: CLI target (e.g., 'tests.build', 'tests.build.instructions', 'tests.build.submit')
                cli_args: CLI arguments like '--scope "X"'
            
            Returns:
                Output from the operation (instructions, submit result, confirm result, etc.)
            """
            # Parse target
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:904): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _prepare_headless_message(self, target: str | None, message: str) -> str:
            """Prepare the final message for headless execution.
            
            If a target is provided (behavior.action), gets instructions and combines with message.
            
            Args:
                target: Optional CLI target (e.g., 'tests.build')
                message: User message (may include CLI args like --scope)
            
            Returns:
                Final message to send to headless session
            """
            if target:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:952): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _format_headless_result(self, execution_result) -> REPLCommandResponse:
            """Format headless execution result as a REPL response.
            
            Args:
                execution_result: Result from HeadlessSession.invokes()
            
            Returns:
                REPLCommandResponse with formatted output
            """
            output_lines = [
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:979): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_headless_command(self, args: str = "") -> REPLCommandResponse:
            """Handle headless command - execute instruction in headless mode"""
            from agile_bot.bots.base_bot.src.repl_cli.headless.headless_session import HeadlessSession
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1024): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
            """Handle behavior navigation"""
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1053): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
            """Navigate to a specific behavior and action
            
            Raises:
                ValueError: If behavior or action not found
            """
            # Navigate to behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1074): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
            """After navigation, auto-execute instructions for new position"""
            return self._handle_instructions_command()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1078): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
            """Wrap content with instructions header and CLI status section"""
            formatter = self.formatter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1119): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _mark_behavior_complete(self, behavior_name: str) -> None:
            """Mark a behavior as complete in the state file"""
            state_file = self.workspace_directory / 'behavior_action_state.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1134): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:210): Useless comment: "# Get scope display" - delete it or improve the code instead

    ```python
            lines.append(formatter.subsection_separator())
            
            # Get scope display
            scope_display = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:757): Useless comment: "# Get the scope display lines" - delete it or improve the code instead

    ```python
            result = self.cli_bot.set_scope(scope)
            
            # Get the scope display lines
            output = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:938): Useless comment: "# Execute the target operation locally to get output" - delete it or improve the code instead

    ```python
                cli_args = ' '.join(cli_args_parts)
                
                # Execute the target operation locally to get output
                operation_output = self._execute_operation_locally(target, cli_args)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:991): Useless comment: "# Execute in headless mode" - delete it or improve the code instead

    ```python
            target, message = self._parse_headless_args(args)
            
            # Execute in headless mode
            try:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1005): Useless comment: "# Execute in headless mode" - delete it or improve the code instead

    ```python
                    final_message = message
                
                # Execute in headless mode
                execution_result = session.invokes(message=final_message, context_file=None)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1060): Useless comment: "# Get the behavior" - delete it or improve the code instead

    ```python
            # Navigate to behavior
            self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
            # Get the behavior
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 105 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:16): Class "ScopeType" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:25): Class "KnowledgeGraphFilter" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:46): Function "filter_knowledge_graph" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:46): Function "filter_knowledge_graph" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:126): Class "Scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:144): Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:165): Function "knowledge_graph_filter" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:174): Function "filters_knowledge_graph" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:174): Function "filters_knowledge_graph" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:187): Function "from_dict" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:187): Function "from_dict" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:204): Function "to_dict" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:258): Function "to_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:352): Function "_find_scope_matches_in_graph" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:352): Function "_find_scope_matches_in_graph" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:366): Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:366): Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:378): Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:390): Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:390): Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:403): Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:403): Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:403): Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:407): Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:407): Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:407): Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:407): Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:465): Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:476): Function "get_decisions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:487): Function "assumptions_list" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:492): Function "assumptions_list" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:505): Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:18): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:82): Function "set_action_phase" uses parameter name "phase" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:96): Function "stage_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:120): Function "detect_tty" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:127): Function "get_progress_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" uses parameter name "full" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:259): Function "get_context_header_for_ai" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:268): Function "_convert_domain_result_to_repl_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:268): Function "_convert_domain_result_to_repl_response" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:326): Function "read_and_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:326): Function "read_and_execute_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:339): Function "_handle_simple_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:339): Function "_handle_simple_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:399): Function "_handle_help_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:399): Function "_handle_help_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:429): Function "_handle_status_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:438): Function "_handle_current_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:467): Function "_handle_next_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:503): Function "_handle_back_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:549): Function "_handle_instructions_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:549): Function "_handle_instructions_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:606): Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:606): Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:627): Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:682): Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:701): Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:701): Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:767): Function "_validate_headless_ready" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:808): Function "_parse_headless_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:808): Function "_parse_headless_args" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:842): Function "_execute_operation_locally" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:842): Function "_execute_operation_locally" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:903): Function "_prepare_headless_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:903): Function "_prepare_headless_message" uses parameter name "target" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:903): Function "_prepare_headless_message" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:951): Function "_format_headless_result" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:951): Function "_format_headless_result" uses parameter name "execution_result" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:978): Function "_handle_headless_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:978): Function "_handle_headless_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1073): Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1077): Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1077): Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1077): Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1133): Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1133): Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1261): Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1322): Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1322): Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1329): Function "_convert_repl_scope_to_cli_format" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1329): Function "_convert_repl_scope_to_cli_format" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1366): Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1366): Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1440): Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1465): Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1479): Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1479): Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1488): Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1498): Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1522): Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1522): Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1535): Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1535): Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1546): Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1557): Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1557): Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1569): Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1569): Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1569): Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1572): Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 12 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1543): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_find_scope_matches (lines 1543-1548)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```

  Location 2 (action_context.py:_find_scope_matches_in_graph (lines 351-356)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1553): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_for_scope_match (lines 1553-1559)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_for_scope_match (lines 362-368)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1564): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_sub_epics (lines 1564-1570)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_sub_epics (lines 374-380)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1592): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1592-1606)):
    ```python
    name = node.get('name', 'Unknown')
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
     ...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 413-427)):
    ```python
    emoji = emoji_map.get(node_type, '•')
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1593): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1593-1610)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 414-431)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1593): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1593-1610)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 414-433)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1596): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1596-1612)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 417-433)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1596): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1596-1612)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 414-433)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1592): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1592-1610)):
    ```python
    name = node.get('name', 'Unknown')
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
     ...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 413-431)):
    ```python
    emoji = emoji_map.get(node_type, '•')
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1593): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1593-1612)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 414-431)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1593): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1593-1612)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 417-433)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1593): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1593-1612)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 414-433)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

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
*... and 62 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-30_02-58-30.md`

