# Validation Report - Code

**Generated:** 2025-12-29 17:46:54
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 274 code file(s) against **32 validation rules**.

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
  - **Total:** 274 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: NEEDS ATTENTION

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 29 | Scanners ran without errors |
| 🟩 Clean Rules | 16 | No violations found |
| 🟨 Rules with Warnings | 8 | Found 57 warning violation(s) |
| 🟥 Rules with Errors | 3 | Found 355 error violation(s) |
| 🟥 Load Failed | 1 | Scanner could not be loaded |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 29
  - 🟥 **Load Failed:** 1
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟨 **[Use Domain Language](#use-domain-language)** - 448 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 258 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 93 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 19 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 11 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 9 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 6 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟨 **[Enforce Encapsulation](#enforce-encapsulation)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-encapsulation-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
- 🟨 **[Provide Meaningful Context](#provide-meaningful-context)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
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

### 🟥 Scanner Load Failures

- 🟥 **[Use Resource Oriented Design](#use-resource-oriented-design)** - LOAD FAILED
  - Scanner Path: `agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
  - Error: `Error loading scanner agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner: unexpected indent (resource_oriented_code_scanner.py, line 161)`

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="use-resource-oriented-design">Use Resource Oriented Design</span> - FAILED
**Description:** CRITICAL: Code must use resource-oriented, object-oriented design. Use object-oriented classes (singular or collection) with responsibilities that encapsulate logic over manager/doer/loader patterns. Maximize encapsulation through collaborator relationships.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
**Error:** `Error loading scanner agile_bot.bots.base_bot.src.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner: unexpected indent (resource_oriented_code_scanner.py, line 161)`

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 258 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 93 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 4 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 19 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 11 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 9 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** CRITICAL: Function signatures must be simple and intention-revealing. Prefer 0-2 parameters. NEVER pass Dict[str, Any] or List[str] for complex data - create typed objects instead. Examples: parameters dict → ParametersObject, files dict → FilesCollection, exclude list → ExcludePatterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 6 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 5 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - 3 WARNING(S) - [View Details](#enforce-encapsulation-violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 3 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 1 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
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

*... and 12 more rules*

## Violations Found

**Total Violations:** 874
- **File-by-File Violations:** 621
- **Cross-File Violations:** 253

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 5 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:101): Line 101: Variable truthiness check detected (if not matches_include:). Assume variable exists - let code fail fast if missing.

    ```python
                            break
                    
                    if not matches_include:
                        continue
                
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:117): Line 117: Variable truthiness check detected (if matches_exclude:). Assume variable exists - let code fail fast if missing.

    ```python
                            break
                    
                    if matches_exclude:
                        continue
                
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:188): Line 188: Variable truthiness check detected (if not data:). Assume variable exists - let code fail fast if missing.

    ```python
        @classmethod
        def from_dict(cls, data: Dict[str, Any]) -> 'Scope':
            if not data:
                return cls()
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1161): Line 1161: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

    ```python
        def parse_command_parameters(self, args: str) -> Dict[str, Any]:
            params = {}
            if not args:
                return params
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:174): Line 174: Variable truthiness check detected (if not synsets:). Assume variable exists - let code fail fast if missing.

    ```python
                synsets = wn.synsets(word_lower)
                
                if not synsets:
                    return False
                
    ```

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 5 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:88): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (filter_files:88-102):
    ```python
    matches_include = False
    for pattern in self.include_patterns:
        pattern_normalized = pattern.replace('\\', '/')
        if file_str == pattern_normalized or file_str.endswith(pattern_normalized) or fnma...
    ```

  Location (filter_files:105-118):
    ```python
    matches_exclude = False
    for pattern in self.exclude_patterns:
        pattern_normalized = pattern.replace('\\', '/')
        if file_str == pattern_normalized or file_str.endswith(pattern_normalized) or fnma...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:192): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (display_current_state:192-205):
    ```python
    lines.append(str(self.workspace_directory))
    lines.append('```')
    lines.append('')
    lines.append('To change path:')
    lines.append('```')
    lines.append('path demo/mob_minion              # Change to specifi...
    ```

  Location (display_current_state:220-228):
    ```python
    lines.append(formatter.subsection_separator())
    lines.append(f'## {formatter.position_icon()} **Progress**')
    lines.append('**Current Position:**')
    lines.append('```')
    lines.append(f'{self.progress_path...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:459): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_handle_next_command:459-478):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```

  Location (_handle_back_command:495-514):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:40): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (is_verb:40-45):
    ```python
    word_lower = word.lower()
    synsets = wn.synsets(word_lower, pos=wn.VERB)
    return len(synsets) > 0
    ```

  Location (is_noun:50-55):
    ```python
    word_lower = word.lower()
    synsets = wn.synsets(word_lower, pos=wn.NOUN)
    return len(synsets) > 0
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:79): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (invokes_action:79-94):
    ```python
    result.blocked_operation = 'submit'
    result.operations_executed = ['instructions', 'submit']
    result.operations_status = {'instructions': 'completed', 'submit': 'blocked'}
    ```

  Location (invokes_behavior:108-122):
    ```python
    result.blocked_action = 'clarify'
    result.actions_executed = ['clarify']
    result.actions_status = {'clarify': 'blocked'}
    ```

#### <span id="enforce-encapsulation-violations">Enforce Encapsulation: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:712): Method "_handle_scope_command" in Test class [REPLSession](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:712) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:74): Method "_format_instructions_for_display" in Test class [StrategyAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:74) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:154): Method "_format_rules_with_file_paths" in Test class [ValidateRulesAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:154) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 3 violation(s)</span>

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" is 1276 lines - should be under 300 lines (extract related methods into separate classes)

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:28): Class "VerbNounScanner" is 414 lines - should be under 300 lines (extract related methods into separate classes)

```python


class VerbNounScanner(StoryScanner):
    
    def scan_domain_concept(self, node: Any, rule_obj: Any) -> List[Dict[str, Any]]:
        return []
    
    def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
        violations = []
        name = node.name
    # ... (truncated)
```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 11 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:75): Function "filter_files" is 39 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return False
        
        def filter_files(self, file_list: List[Path]) -> List[Path]:
            """Filter file list to only files matching this filter."""
            if not self.include_patterns and not self.exclude_patterns:
                return file_list
            
            from fnmatch import fnmatch
            filtered = []
            
            for file_path in file_list:
                # Convert to string with forward slashes for consistent matching
                file_str = str(file_path).replace('\\', '/')
                
                # Check include patterns
                if self.include_patterns:
                    matches_include = False
                    for pattern in self.include_patterns:
                        pattern_normalized = pattern.replace('\\', '/')
                        # Try exact match, ends-with match, and glob match
                        if (file_str == pattern_normalized or 
                            file_str.endswith(pattern_normalized) or
                            fnmatch(file_str, pattern_normalized) or
                            fnmatch(file_str, f'*/{pattern_normalized}') or
                            fnmatch(file_str, f'**/{pattern_normalized}')):
                            matches_include = True
                            break
                    
                    if not matches_include:
                        continue
                
                # Check exclude patterns
                if self.exclude_patterns:
                    matches_exclude = False
                    for pattern in self.exclude_patterns:
                        pattern_normalized = pattern.replace('\\', '/')
                        if (file_str == pattern_normalized or 
                            file_str.endswith(pattern_normalized) or
                            fnmatch(file_str, pattern_normalized) or
                            fnmatch(file_str, f'*/{pattern_normalized}') or
                            fnmatch(file_str, f'**/{pattern_normalized}')):
                            matches_exclude = True
                            break
                    
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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 78 lines - should be under 20 lines (extract complex logic to helper functions)

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" is 47 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            violations = []
            
            all_files = []
            if code_files:
                all_files.extend(code_files)
            if test_files:
                all_files.extend(test_files)
            
            if not all_files:
                return violations
            
            # First pass: collect all loader/manager classes and all classes
            loader_classes = {}  # class_name -> (file_path, class_node, pattern)
            all_classes = {}  # (file_path, class_name) -> class_node
            
            for file_path in all_files:
                if not file_path.exists():
                    continue
                
                try:
                    content = file_path.read_text(encoding='utf-8')
                    tree = ast.parse(content, filename=str(file_path))
                    
                    classes = Classes(tree)
                    for cls in classes.get_many_classes:
                        all_classes[(file_path, cls.node.name)] = cls.node
                        
                        # Check if class name is an agent noun using NLTK
                        is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(cls.node.name)
                        if is_agent:
                            loader_classes[cls.node.name] = (file_path, cls.node, suffix)
                except (SyntaxError, UnicodeDecodeError) as e:
                    logger.debug(f'Skipping file {file_path} due to {type(e).__name__}: {e}')
                    continue
            
            # Second pass: check if each agent noun class is owned by a domain object
            for loader_class_name, (loader_file, loader_node, suffix) in loader_classes.items():
                if not self._is_owned_by_domain_object(loader_class_name, loader_node, all_files, all_classes):
                    suggested_name = loader_class_name[:-len(suffix)] if loader_class_name.endswith(suffix) else loader_class_name
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:35): Function "map_location" has high cognitive complexity (22) - should be under 15. Reduce nesting and extract complex logic.

    ```python
            return self.data.get('name', '')
        
        def map_location(self, field: str = 'name') -> str:
            if isinstance(self, Epic):
                return f"epics[{self.epic_idx}].{field}"
            elif isinstance(self, SubEpic):
                if self.sub_epic_path:
                    path_str = "".join([f".sub_epics[{idx}]" for idx in self.sub_epic_path])
                    return f"epics[{self.epic_idx}]{path_str}.{field}"
                else:
                    return f"epics[{self.epic_idx}].{field}"
            elif isinstance(self, Story):
                path_parts = [f"epics[{self.epic_idx}]"]
                if self.sub_epic_path:
                    for idx in self.sub_epic_path:
                        path_parts.append(f"sub_epics[{idx}]")
                if self.story_group_idx is not None:
                    path_parts.append(f"story_groups[{self.story_group_idx}]")
                path_parts.append(f"stories[{self.story_idx}]")
                path_parts.append(field)
                return ".".join(path_parts)
            return ""
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\technical_abstraction_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_scanner.py:24): Function "scan_domain_concept" is 31 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        ]
        
        def scan_domain_concept(self, node: DomainConceptNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            # Check if concept name is an agent noun related to technical operations
            is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(node.name)
            if is_agent and base_verb in ['save', 'load', 'store']:
                violations.append(
                    Violation(
                        rule=rule_obj,
                        violation_message=f'Domain concept "{node.name}" separates technical abstraction (derived from verb "{base_verb}"). Keep technical details (saving, loading) as part of domain concepts instead.',
                        location=node.map_location('name'),
                        line_number=None,
                        severity='warning'
                    ).to_dict()
                )
            
            # Check responsibilities for technical file operation patterns
            for i, responsibility_data in enumerate(node.responsibilities):
                responsibility_name = responsibility_data.get('name', '')
                resp_lower = responsibility_name.lower()
                for pattern in self.TECHNICAL_FILE_PATTERNS:
                    if re.search(pattern, resp_lower):
                        violations.append(
                            Violation(
                                rule=rule_obj,
                                violation_message=f'Responsibility "{responsibility_name}" exposes technical abstraction. Stay at domain level (e.g., "Saves portfolio" not "Saves portfolio to file").',
                                location=node.map_location(f'responsibilities[{i}].name'),
                                line_number=None,
                                severity='warning'
                            ).to_dict()
                        )
                        break
            
            return violations
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:33): Function "scan_story_node" is 28 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_story_node(self, node: StoryNode, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            name = node.name
            
            if not name:
                return violations
            
            node_type = self._get_node_type(node)
            
            violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_gerund_ending(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_actor_prefix(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_noun_only(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            violation = self._check_third_person_singular(name, node, node_type, rule_obj)
            if violation:
                violations.append(violation)
            
            return violations
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:58): Function "is_agent_noun" has high cognitive complexity (20) - should be under 15. Reduce nesting and extract complex logic.

    ```python
        
        @staticmethod
        def is_agent_noun(word: str) -> tuple[bool, Optional[str], Optional[str]]:
            """
            Check if word is an agent noun (doer of action).
            Returns: (is_agent, base_verb, suffix) or (False, None, None)
            
            Examples:
                'Manager' -> (True, 'manage', 'er')
                'Processor' -> (True, 'process', 'or')
                'Portfolio' -> (False, None, None)
            """
            word_lower = word.lower()
            
            for suffix in VocabularyHelper.AGENT_SUFFIXES:
                if word_lower.endswith(suffix) and len(word_lower) > len(suffix) + 2:
                    base = word_lower[:-len(suffix)]
                    
                    # Check if base is a verb
                    if VocabularyHelper.is_verb(base):
                        return (True, base, suffix)
                    
                    # Check common irregular forms
                    # manage -> manager, coordinate -> coordinator
                    if suffix == 'er' or suffix == 'or':
                        # Try adding 'e' back
                        base_with_e = base + 'e'
                        if VocabularyHelper.is_verb(base_with_e):
                            return (True, base_with_e, suffix)
            
            return (False, None, None)
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:155): Function "is_actor_or_role" is 21 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
        
        @staticmethod
        def is_actor_or_role(word: str) -> bool:
            """
            Check if word represents an actor or role (person, system, agent).
            Uses WordNet to check if word is a hyponym of 'person' or 'system'.
            
            Examples:
                'customer' -> True (person who buys)
                'user' -> True (person who uses)
                'developer' -> True (person who develops)
                'system' -> True (computing system)
                'api' -> True (system interface)
                'order' -> False (not a person/system)
            """
            try:
                word_lower = word.lower()
                
                # Get all synsets for the word
                synsets = wn.synsets(word_lower)
                
                if not synsets:
                    return False
                
                # Get hypernym paths for all synsets
                for synset in synsets:
                    # Get all hypernyms (parent concepts)
                    hypernyms = set()
                    for path in synset.hypernym_paths():
                        hypernyms.update(path)
                    
                    # Check if any hypernym is 'person', 'user', 'system', or 'agent'
                    for hypernym in hypernyms:
                        name = hypernym.name().split('.')[0]
                        if name in ['person', 'user', 'system', 'agent', 'entity', 'causal_agent']:
                            return True
                
                return False
            except Exception:
                return False
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:137): Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:264): Function "formatted_rules_digest" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return '\n'.join(sections) if sections else 'No validation rules found.'
    
        def formatted_rules_digest(self) -> str:
            rules = self._load_rules()
            if not rules:
                return 'No validation rules found.'
            
            # Sort by priority (lower number = higher priority)
            rules = sorted(rules, key=lambda r: r.priority)
            
            lines = ['Rules to follow:', '']
            for i, rule in enumerate(rules):
                description = rule.description or 'No description'
                lines.append(f"- **{rule.name}**: {description}")
                
                # Add DO description if present
                do_section = rule.rule_content.get('do', {})
                do_desc = do_section.get('description', '')
                if do_desc:
                    lines.append(f"  DO: {do_desc}")
                
                # Add DON'T description if present
                dont_section = rule.rule_content.get('dont', {})
                dont_desc = dont_section.get('description', '')
                if dont_desc:
                    lines.append(f"  DON'T: {dont_desc}")
                
                # Add blank line between rules, but not after the last rule
                if i < len(rules) - 1:
                    lines.append("")
            
            return '\n'.join(lines)
    
    ```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 14 violation(s)</span>

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 108 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:262): Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:333): Function "_handle_simple_command" is 55 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:539): Function "_handle_instructions_command" is 53 lines - consider improving vertical density by declaring variables near usage

    ```python
            )
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            if not self.has_current_action:
                return REPLCommandResponse(
                    output="ERROR: No current action to get instructions for",
                    response="ERROR: No current action",
                    status="error"
                )
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:614): Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:688): Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:864): Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:992): Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1060): Function "_execute_action_with_args" is 73 lines - consider improving vertical density by declaring variables near usage

    ```python
                return args_str.split()
        
        def _execute_action_with_args(self, action_name: str, cli_args: list, operation: str = None) -> REPLCommandResponse:
            if not self.has_current_behavior:
                return REPLCommandResponse(
                    output="ERROR: No current behavior set. Please select a behavior first.",
                    response="ERROR: No current behavior set",
                    status="error"
                )
            
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" is 59 lines - consider improving vertical density by declaring variables near usage

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:105): Function "_class_uses_as_attribute" is 51 lines - consider improving vertical density by declaring variables near usage

    ```python
            return False
        
        def _class_uses_as_attribute(self, class_node: ast.ClassDef, loader_class_name: str, file_path: Path) -> bool:
            try:
                content = file_path.read_text(encoding='utf-8')
                # Simple check: see if loader class name appears in the file
                if loader_class_name not in content:
                    return False
            except (UnicodeDecodeError, IOError):
                return False
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:247): Function "_check_noun_verb_pattern" is 63 lines - consider improving vertical density by declaring variables near usage

    ```python
            return None
        
        def _check_noun_verb_pattern(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
            try:
                tokens, tags = self._get_tokens_and_tags(name)
                
                if len(tags) < 2:
                    return None
                
                first_word = tags[0][0]
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:330): Function "_check_noun_only" is 112 lines - consider improving vertical density by declaring variables near usage

    ```python
            return None
        
        def _check_noun_only(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
            try:
                tokens, tags = self._get_tokens_and_tags(name)
                
                if not tags:
                    return None
                
                has_verb = any(self._is_verb(tag[1]) for tag in tags)
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:861): Except block only contains pass at line 861 - exceptions must be logged or rethrown, never swallowed

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:437): Except block only contains pass at line 437 - exceptions must be logged or rethrown, never swallowed

    ```python
                    ).to_dict()
            
            except Exception:
                # NLTK POS tagging failed - return None to avoid false positives
                pass
            
    ```

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:8): Line 8 contains magic number - replace with named constant

    ```python
    DEFAULT_MAX_ATTEMPTS = 3
    DEFAULT_WAIT_TIME_SECONDS = 60.0
    
    ```

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 6 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:280): Fallback/legacy support code found (comment at line 280, code at line 281) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:298): Fallback/legacy support code found (comment at line 298, code at line 299) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:72): Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:233): Fallback/legacy support code found (comment at line 233, code at line 234) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1203): Fallback/legacy support code found (comment at line 1203, code at line 1204) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:104): Fallback/legacy support code found (comment at line 104, code at line 105) - complete refactoring by removing old pattern support

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 19 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:75): Function "filter_files" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def filter_files(self, file_list: List[Path]) -> List[Path]:
            """Filter file list to only files matching this filter."""
            if not self.include_patterns and not self.exclude_patterns:
                return file_list
            
            from fnmatch import fnmatch
            filtered = []
            
            for file_path in file_list:
                # Convert to string with forward slashes for consistent matching
                file_str = str(file_path).replace('\\', '/')
                
                # Check include patterns
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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:428): Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:688): Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:864): Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None
        ) -> List[Dict[str, Any]]:
            violations = []
            
            all_files = []
            if code_files:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:105): Function "_class_uses_as_attribute" has nesting depth of 10 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _class_uses_as_attribute(self, class_node: ast.ClassDef, loader_class_name: str, file_path: Path) -> bool:
            try:
                content = file_path.read_text(encoding='utf-8')
                # Simple check: see if loader class name appears in the file
                if loader_class_name not in content:
                    return False
            except (UnicodeDecodeError, IOError):
                return False
            
            for node in class_node.body:
                if isinstance(node, ast.FunctionDef) and node.name == '__init__':
                    for stmt in ast.walk(node):
                        if isinstance(stmt, ast.Assign):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:35): Function "map_location" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return self.data.get('name', '')
        
        def map_location(self, field: str = 'name') -> str:
            if isinstance(self, Epic):
                return f"epics[{self.epic_idx}].{field}"
            elif isinstance(self, SubEpic):
                if self.sub_epic_path:
                    path_str = "".join([f".sub_epics[{idx}]" for idx in self.sub_epic_path])
                    return f"epics[{self.epic_idx}]{path_str}.{field}"
                else:
                    return f"epics[{self.epic_idx}].{field}"
            elif isinstance(self, Story):
                path_parts = [f"epics[{self.epic_idx}]"]
                if self.sub_epic_path:
                    for idx in self.sub_epic_path:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:330): Function "_check_noun_only" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return None
        
        def _check_noun_only(self, name: str, node: StoryNode, node_type: str, rule_obj: Any) -> Optional[Dict[str, Any]]:
            try:
                tokens, tags = self._get_tokens_and_tags(name)
                
                if not tags:
                    return None
                
                has_verb = any(self._is_verb(tag[1]) for tag in tags)
                
                # If NLTK didn't find a verb, check if first word can be a verb using WordNet
                # (NLTK often tags capitalized verbs as proper nouns NNP)
                if not has_verb and tokens:
                    # Strip punctuation from first word (e.g., "Load+" -> "Load")
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:58): Function "is_agent_noun" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
        
        @staticmethod
        def is_agent_noun(word: str) -> tuple[bool, Optional[str], Optional[str]]:
            """
            Check if word is an agent noun (doer of action).
            Returns: (is_agent, base_verb, suffix) or (False, None, None)
            
            Examples:
                'Manager' -> (True, 'manage', 'er')
                'Processor' -> (True, 'process', 'or')
                'Portfolio' -> (False, None, None)
            """
            word_lower = word.lower()
            
            for suffix in VocabularyHelper.AGENT_SUFFIXES:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:155): Function "is_actor_or_role" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
        
        @staticmethod
        def is_actor_or_role(word: str) -> bool:
            """
            Check if word represents an actor or role (person, system, agent).
            Uses WordNet to check if word is a hyponym of 'person' or 'system'.
            
            Examples:
                'customer' -> True (person who buys)
                'user' -> True (person who uses)
                'developer' -> True (person who develops)
                'system' -> True (computing system)
                'api' -> True (system interface)
                'order' -> False (not a person/system)
            """
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:71): Function "_format_instructions_for_display" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return {'status': 'submitted', 'message': 'No strategy data to save'}
        
        def _format_instructions_for_display(self, instructions) -> str:
            """Format strategy data for REPL display."""
            # Get base formatting first (includes scope warning if set)
            output_lines = super()._format_instructions_for_display(instructions).split('\n')
            
            # Get the instruction data
            instructions_dict = instructions.to_dict()
            
            # Format strategy criteria
            strategy_criteria = instructions_dict.get('strategy_criteria', {})
            if strategy_criteria:
                output_lines.append("")
                output_lines.append("**Decisions:**")
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:32): Function "_prepare_instructions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return self._rules
    
        def _prepare_instructions(self, instructions, context: ValidateActionContext):
            """Prepare validation instructions with rules and validation data."""
            # Get rules with file paths for AI to read
            rules_text = self._format_rules_with_file_paths()
            
            # Get story graph schema path
            schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
            
            # Get scope description
            scope_text = self._format_scope_description(context)
            
            # Run scanners and get formatted results
            scanner_output = self._run_scanners_and_format_results(context)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:74): Function "_run_scanners_and_format_results" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            instructions._data['base_instructions'] = new_instructions
    
        def _run_scanners_and_format_results(self, context: ValidateActionContext) -> str:
            """Run validation scanners and format results for display in instructions."""
            logger.info('Running scanners for instructions display...')
            
            try:
                # Execute validation synchronously
                result = self._executor.execute_synchronous(context)
                
                # Get the report path from the result
                instructions_dict = result.get('instructions', {})
                report_link = instructions_dict.get('report_link', '')
                
                # Read the generated validation report file
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:117): Function "_format_scope_description" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return f'Error running scanners: {e}\n\nPlease review the validation report file in docs/stories/reports/'
        
        def _format_scope_description(self, context: ValidateActionContext) -> str:
            """Format scope description for validation instructions."""
            if context.scope:
                scope_type = context.scope.type.value  # ScopeType enum
                scope_value = context.scope.value
                
                if scope_type == 'epic':
                    return f"epic(s): {', '.join(scope_value)}"
                elif scope_type == 'story':
                    return f"story/stories: {', '.join(scope_value)}"
                elif scope_type == 'files':
                    return f"file(s): {', '.join(scope_value)}"
                else:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:152): Function "_get_explicit_files_for_behavior" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return 'src'
    
        def _get_explicit_files_for_behavior(self, file_key, behavior_dir):
            # Check if we have a files scope - if so, try both file_key and 'test'/'src' explicitly
            has_files_scope = (self._parameters.get('scope', {}).get('type') == 'files' if isinstance(self._parameters.get('scope'), dict) else False)
            
            if file_key in self._scope_config:
                files = self.files(file_key)
                if files:
                    return files
            
            if behavior_dir in self._scope_config:
                files = self.files(behavior_dir)
                if files:
                    return files
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:42): Function "processes_line" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            self._current_section = None
        
        def processes_line(self, line: str) -> None:
            if line.startswith('User Intent:'):
                self._current_section = 'user_message'
                self.user_message = line.replace('User Intent:', '').strip()
            elif line.startswith('Chat History:'):
                self._current_section = 'chat_history'
            elif line.startswith('File References:'):
                self._current_section = 'file_references'
            elif line.startswith('-'):
                self._appends_list_item(line[1:].strip())
        
    ```

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 93 violation(s)</span>

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:34): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def scope(self) -> Optional['Scope']:
            """Get the scope filter if set."""
            return self._scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def context_sources_text(self) -> List[str]:
            """Generate standard 'Look for context in the following locations' section with actual paths."""
            if not self._bot_paths:
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:254): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def get_context_header_for_ai(self) -> str:
            """Get status display as a string for AI context headers.
            
            This is a convenience method that extracts just the output string
            from display_current_state().
            """
            state_display = self.display_current_state()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:263): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:390): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
            """Handle help command using bot.help"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:420): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_status_command(self) -> REPLCommandResponse:
            """Handle status command using bot.status"""
            state_display = self.display_current_state(full=True)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:429): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_current_command(self) -> REPLCommandResponse:
            """Re-execute current operation based on progress state"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:458): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_next_command(self) -> REPLCommandResponse:
            """Handle next/advance navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:494): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_back_command(self) -> REPLCommandResponse:
            """Handle back/previous navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:540): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:594): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
            """Handle submit command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:615): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_confirm_command(self) -> REPLCommandResponse:
            """Handle confirm command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:670): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
            """Handle path/workspace command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:689): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:755): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
            """Handle behavior navigation"""
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:784): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
            """Navigate to a specific behavior and action
            
            Raises:
                ValueError: If behavior or action not found
            """
            # Navigate to behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:805): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
            """After navigation, auto-execute instructions for new position"""
            return self._handle_instructions_command()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:809): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
            """Wrap content with instructions header and CLI status section"""
            formatter = self.formatter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:850): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _mark_behavior_complete(self, behavior_name: str) -> None:
            """Mark a behavior as complete in the state file"""
            state_file = self.workspace_directory / 'behavior_action_state.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:865): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_dot_notation(self, command: str) -> REPLCommandResponse:
            """Handle dot notation commands (behavior.action.operation)"""
            # Parse dot notation: behavior.action.operation or action.operation or .operation
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:204): Useless comment: "# Get scope display" - delete it or improve the code instead

    ```python
            lines.append(formatter.subsection_separator())
            
            # Get scope display
            scope_display = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:744): Useless comment: "# Get the scope display lines" - delete it or improve the code instead

    ```python
            result = self.cli_bot.set_scope(scope)
            
            # Get the scope display lines
            output = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:791): Useless comment: "# Get the behavior" - delete it or improve the code instead

    ```python
            # Navigate to behavior
            self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
            # Get the behavior
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:13): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class ActiveLanguageScanner(StoryScanner):
        """
        Validates that story names use active language without actor prefixes.
        Uses NLTK to detect actor/role words at the beginning of story names.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class ResourceOrientedCodeScanner(CodeScanner):
        """
        Validates that code classes are named after resources (what they ARE)
        rather than actions (what they DO).
        
        Uses NLTK to detect agent nouns (Manager, Loader, Handler, etc.)
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_design_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_design_scanner.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class ResourceOrientedDesignScanner(DomainScanner):
        """
        Validates that domain concepts are named after resources (what they ARE)
        rather than actions (what they DO).
        
        Uses NLTK to detect agent nouns (Manager, Loader, Handler, etc.)
        which are nouns derived from verbs that describe doers of actions.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:77): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def all_stories(self) -> List['Story']:
            """Return all Story nodes within this epic (including nested sub-epics)."""
            stories: List['Story'] = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:293): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def find_epic_by_name(self, epic_name: str) -> 'Epic':
            """Find an epic by name."""
            for epic in self.epics():
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\technical_abstraction_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_scanner.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class TechnicalAbstractionScanner(DomainScanner):
        """
        Validates that domain concepts avoid exposing technical abstractions.
        Uses NLTK to detect agent nouns like Saver, Loader, Storage.
        """
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:203): Useless comment: "# Handle verbs ending in -es (e.g., "fixes" -> "fix", "watch" - delete it or improve the code instead

    ```python
            if verb_lower.endswith("ies") and len(verb_lower) > 3:
                base = verb_lower[:-3] + "y"
            # Handle verbs ending in -es (e.g., "fixes" -> "fix", "watches" -> "watch", "goes" -> "go")
            elif verb_lower.endswith("es") and len(verb_lower) > 2:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class VocabularyHelper:
        """Helper class for linguistic analysis using NLTK."""
        
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:39): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_verb(word: str) -> bool:
            """Check if word can function as a verb using WordNet."""
            try:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_noun(word: str) -> bool:
            """Check if word can function as a noun using WordNet."""
            try:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:59): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_agent_noun(word: str) -> tuple[bool, Optional[str], Optional[str]]:
            """
            Check if word is an agent noun (doer of action).
            Returns: (is_agent, base_verb, suffix) or (False, None, None)
            
            Examples:
                'Manager' -> (True, 'manage', 'er')
                'Processor' -> (True, 'process', 'or')
                'Portfolio' -> (False, None, None)
            """
            word_lower = word.lower()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:90): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_gerund(word: str) -> tuple[bool, Optional[str]]:
            """
            Check if word is a gerund (verb + ing).
            Returns: (is_gerund, base_verb) or (False, None)
            
            Examples:
                'Loading' -> (True, 'load')
                'Running' -> (True, 'run')
                'Thing' -> (False, None)
            """
            word_lower = word.lower()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:128): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def get_pos_tags(text: str) -> List[tuple[str, str]]:
            """Get part-of-speech tags for text."""
            try:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:138): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_verb_tag(tag: str) -> bool:
            """Check if POS tag indicates a verb."""
            verb_tags = ['VB', 'VBP', 'VBZ', 'VBD', 'VBG', 'VBN']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:144): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_noun_tag(tag: str) -> bool:
            """Check if POS tag indicates a noun."""
            noun_tags = ['NN', 'NNS', 'NNP', 'NNPS']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:150): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_proper_noun_tag(tag: str) -> bool:
            """Check if POS tag indicates a proper noun."""
            proper_noun_tags = ['NNP', 'NNPS']
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:156): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @staticmethod
        def is_actor_or_role(word: str) -> bool:
            """
            Check if word represents an actor or role (person, system, agent).
            Uses WordNet to check if word is a hyponym of 'person' or 'system'.
            
            Examples:
                'customer' -> True (person who buys)
                'user' -> True (person who uses)
                'developer' -> True (person who develops)
                'system' -> True (computing system)
                'api' -> True (system interface)
                'order' -> False (not a person/system)
            """
            try:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:171): Useless comment: "# Get all synsets for the word" - delete it or improve the code instead

    ```python
                word_lower = word.lower()
                
                # Get all synsets for the word
                synsets = wn.synsets(word_lower)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:179): Useless comment: "# Get all hypernyms (parent concepts)" - delete it or improve the code instead

    ```python
                # Get hypernym paths for all synsets
                for synset in synsets:
                    # Get all hypernyms (parent concepts)
                    hypernyms = set()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:68): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @classmethod
        def _get_files_for_validation(cls, behavior, context: 'ValidateActionContext') -> Dict[str, List[Path]]:
            """Get files to validate based on behavior and scope."""
            from agile_bot.bots.base_bot.src.actions.validate.file_discovery import FileDiscovery
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:47): Useless comment: "# Get files - either from scope filter or discover all" - delete it or improve the code instead

    ```python
                knowledge_graph_content = validation_scope.filter_story_graph(knowledge_graph_content)
            
            # Get files - either from scope filter or discover all
            files = cls._get_files_for_validation(behavior, context)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:208): Useless comment: "# Load bot-level rules" - delete it or improve the code instead

    ```python
            all_rules = []
            
            # Load bot-level rules
            bot_rules = self._rule_loader.load_bot_rules()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\rules\rule_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule_loader.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def load_bot_rules(self) -> List[Rule]:
            """Load bot-level rules from <bot_directory>/rules/"""
            bot_rules_dir = self.bot_paths.bot_directory / 'rules'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:36): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _prepare_instructions(self, instructions, context: StrategyActionContext):
            """Add strategy data (criteria, assumptions, activities) to instructions."""
            instructions.update(self.strategy.instructions)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:40): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _do_submit(self, context: StrategyActionContext) -> Dict[str, Any]:
            """Save strategy decisions and assumptions to strategy.json."""
            decisions = context.get_decisions()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:72): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _format_instructions_for_display(self, instructions) -> str:
            """Format strategy data for REPL display."""
            # Get base formatting first (includes scope warning if set)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:107): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _format_option(self, option) -> list:
            """Format a single decision criteria option for display."""
            lines = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:58): Useless comment: "# Get file path" - delete it or improve the code instead

    ```python
                saved_items = " and ".join(message_parts) if message_parts else "data"
                
                # Get file path
                saved_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'strategy.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:76): Useless comment: "# Get the instruction data" - delete it or improve the code instead

    ```python
            output_lines = super()._format_instructions_for_display(instructions).split('\n')
            
            # Get the instruction data
            instructions_dict = instructions.to_dict()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _prepare_instructions(self, instructions, context: ValidateActionContext):
            """Prepare validation instructions with rules and validation data."""
            # Get rules with file paths for AI to read
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:75): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _run_scanners_and_format_results(self, context: ValidateActionContext) -> str:
            """Run validation scanners and format results for display in instructions."""
            logger.info('Running scanners for instructions display...')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:118): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _format_scope_description(self, context: ValidateActionContext) -> str:
            """Format scope description for validation instructions."""
            if context.scope:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:135): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _format_rules_with_file_paths(self) -> str:
            """Format rules with file paths for AI to read and analyze."""
            rules_data = self.inject_behavior_specific_rules()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:182): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _do_submit(self, context: ValidateActionContext) -> Dict[str, Any]:
            """Run validation scanners and generate reports."""
            logger.info('=== Starting validation ===')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:196): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def do_execute(self, context: ValidateActionContext) -> Dict[str, Any]:
            """Legacy method for backwards compatibility."""
            logger.info('=== Starting validation ===')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:34): Useless comment: "# Get rules with file paths for AI to read" - delete it or improve the code instead

    ```python
        def _prepare_instructions(self, instructions, context: ValidateActionContext):
            """Prepare validation instructions with rules and validation data."""
            # Get rules with file paths for AI to read
            rules_text = self._format_rules_with_file_paths()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:37): Useless comment: "# Get story graph schema path" - delete it or improve the code instead

    ```python
            rules_text = self._format_rules_with_file_paths()
            
            # Get story graph schema path
            schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:40): Useless comment: "# Get scope description" - delete it or improve the code instead

    ```python
            schema_path = self.behavior.bot_paths.workspace_directory / 'docs' / 'stories' / 'story-graph.json'
            
            # Get scope description
            scope_text = self._format_scope_description(context)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:79): Useless comment: "# Execute validation synchronously" - delete it or improve the code instead

    ```python
            
            try:
                # Execute validation synchronously
                result = self._executor.execute_synchronous(context)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:82): Useless comment: "# Get the report path from the result" - delete it or improve the code instead

    ```python
                result = self._executor.execute_synchronous(context)
                
                # Get the report path from the result
                instructions_dict = result.get('instructions', {})
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:19): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    def ensure_reports_directory(bot_paths: BotPaths, workspace_directory: Path) -> Path:
        """Module-level helper to create and return the reports directory."""
        docs_path = bot_paths.documentation_path
    ```

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 9 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:127): Function "_create_capability_noun_violation" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return None
        
        def _create_capability_noun_violation(self, name: str, node: StoryNode, node_type: str, rule_obj: Any, noun_type: str) -> Dict[str, Any]:
            location = node.map_location()
            message = f'{node_type.capitalize()} name "{name}" uses capability noun'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:331): Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                return data
    
        def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            execution_status = rule.scanner_execution_status or 'SUCCESS'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:347): Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'
    
        def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
            scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:367): Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                raise
    
        def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
            scanner_path = rule.scanner_path
            if not scanner_path:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:379): Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)
    
        def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
            if isinstance(context, ValidationContext):
                return self._execute_validation(context)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:384): Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))
    
        def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
            return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
        
        @classmethod
        def creates_blocked(
            cls,
            log_path: Path,
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
        
        @classmethod
        def creates_completed(
            cls,
            log_path: Path,
        # ... (truncated)
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 448 violation(s)</span>

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:504): Function "__post_init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:9): Class "Instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:11): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:11): Function "__init__" uses parameter name "base_instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:11): Function "__init__" uses parameter name "scope" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:18): Function "add" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:23): Function "add_display" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:29): Function "display_content" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:33): Function "scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:38): Function "context_sources_text" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:76): Function "set" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:76): Function "set" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:82): Function "update" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:92): Function "to_dict" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:97): Function "copy" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:104): Function "get" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:104): Function "get" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:104): Function "get" uses parameter name "default" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:107): Function "__getitem__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:107): Function "__getitem__" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:110): Function "__setitem__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:110): Function "__setitem__" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:115): Function "__contains__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:115): Function "__contains__" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\instructions.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/instructions.py:118): Function "__repr__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:18): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:82): Function "set_action_phase" uses parameter name "phase" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:96): Function "stage_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:120): Function "detect_tty" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:127): Function "get_progress_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" uses parameter name "full" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:253): Function "get_context_header_for_ai" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:262): Function "_convert_domain_result_to_repl_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:262): Function "_convert_domain_result_to_repl_response" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:320): Function "read_and_execute_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:320): Function "read_and_execute_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:333): Function "_handle_simple_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:333): Function "_handle_simple_command" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:389): Function "_handle_help_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:389): Function "_handle_help_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:419): Function "_handle_status_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:428): Function "_handle_current_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:457): Function "_handle_next_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:493): Function "_handle_back_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:539): Function "_handle_instructions_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:539): Function "_handle_instructions_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:593): Function "_handle_submit_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:593): Function "_handle_submit_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:614): Function "_handle_confirm_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:669): Function "_handle_path_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:688): Function "_handle_scope_command" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:688): Function "_handle_scope_command" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:804): Function "_wrap_navigation_with_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:808): Function "_wrap_with_context_header" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:808): Function "_wrap_with_context_header" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:808): Function "_wrap_with_context_header" uses parameter name "response_msg" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:864): Function "_handle_dot_notation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:864): Function "_handle_dot_notation" uses parameter name "command" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:992): Function "_handle_action_shortcut" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1053): Function "_tokenize_cli_args" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1053): Function "_tokenize_cli_args" uses parameter name "args_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1060): Function "_execute_action_with_args" uses parameter name "cli_args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1060): Function "_execute_action_with_args" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1134): Function "display_confirm_prompt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1159): Function "parse_command_parameters" uses parameter name "args" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1173): Function "parse_scope_from_string" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1173): Function "parse_scope_from_string" uses parameter name "scope_str" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1182): Function "get_stored_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1192): Function "_get_scope_display_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1216): Function "_find_scope_matches" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1216): Function "_find_scope_matches" uses parameter name "scope_values" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1229): Function "_search_for_scope_match" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1229): Function "_search_for_scope_match" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1240): Function "_search_sub_epics" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1251): Function "_search_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1251): Function "_search_stories" uses parameter name "scope_val" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1263): Function "_matches_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1263): Function "_matches_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1263): Function "_matches_name" uses parameter name "pattern" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1266): Function "_format_node_with_children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1266): Function "_format_node_with_children" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1266): Function "_format_node_with_children" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1266): Function "_format_node_with_children" uses parameter name "indent" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:18): Function "scan_story_node" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:41): Function "_check_actor_in_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:41): Function "_check_actor_in_name" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:41): Function "_check_actor_in_name" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:41): Function "_check_actor_in_name" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:75): Function "_get_node_type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:75): Function "_get_node_type" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:84): Function "_check_passive_voice" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:84): Function "_check_passive_voice" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:84): Function "_check_passive_voice" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:84): Function "_check_passive_voice" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:96): Function "_create_passive_voice_violation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:96): Function "_create_passive_voice_violation" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:96): Function "_create_passive_voice_violation" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:96): Function "_create_passive_voice_violation" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:105): Function "_check_capability_nouns" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:105): Function "_check_capability_nouns" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:105): Function "_check_capability_nouns" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:105): Function "_check_capability_nouns" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:127): Function "_create_capability_noun_violation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:127): Function "_create_capability_noun_violation" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:127): Function "_create_capability_noun_violation" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:127): Function "_create_capability_noun_violation" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:127): Function "_create_capability_noun_violation" uses parameter name "noun_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:24): Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:88): Function "_is_owned_by_domain_object" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:88): Function "_is_owned_by_domain_object" uses parameter name "loader_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_design_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_design_scanner.py:19): Function "scan_domain_concept" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_design_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_design_scanner.py:19): Function "scan_domain_concept" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\scanner_execution_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_execution_error.py:4): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\scanner_execution_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/scanner_execution_error.py:4): Function "__init__" uses parameter name "original_error" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:18): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:28): Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:32): Function "name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:35): Function "map_location" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:35): Function "map_location" uses parameter name "field" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:60): Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:76): Function "all_stories" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:93): Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:113): Function "children" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:127): Function "steps" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:145): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:151): Function "name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:155): Function "type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:159): Function "background" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:166): Function "map_location" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:166): Function "map_location" uses parameter name "field" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:173): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:179): Function "name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:183): Function "type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:187): Function "background" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:191): Function "examples" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:195): Function "examples_columns" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:199): Function "examples_rows" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:206): Function "map_location" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:206): Function "map_location" uses parameter name "field" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:214): Function "sizing" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:218): Function "users" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:226): Function "connector" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:230): Function "sequential_order" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:261): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:261): Function "__init__" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:265): Function "from_bot" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:299): Function "walk" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:299): Function "walk" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\technical_abstraction_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_scanner.py:24): Function "scan_domain_concept" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\technical_abstraction_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/technical_abstraction_scanner.py:24): Function "scan_domain_concept" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:30): Function "scan_domain_concept" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:30): Function "scan_domain_concept" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:33): Function "scan_story_node" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:72): Function "_get_node_type" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:72): Function "_get_node_type" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:81): Function "_get_tokens_and_tags" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:81): Function "_get_tokens_and_tags" uses parameter name "text" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:90): Function "_is_verb" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:90): Function "_is_verb" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:94): Function "_is_noun" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:94): Function "_is_noun" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:98): Function "_is_proper_noun" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:98): Function "_is_proper_noun" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:102): Function "_can_be_verb" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:102): Function "_can_be_verb" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:119): Function "_check_verb_noun_order" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:119): Function "_check_verb_noun_order" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:119): Function "_check_verb_noun_order" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:119): Function "_check_verb_noun_order" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:137): Function "_check_gerund_ending" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:137): Function "_check_gerund_ending" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:137): Function "_check_gerund_ending" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:137): Function "_check_gerund_ending" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:158): Function "_check_third_person_singular" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:158): Function "_check_third_person_singular" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:158): Function "_check_third_person_singular" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:158): Function "_check_third_person_singular" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:183): Function "_convert_to_base_form" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:183): Function "_convert_to_base_form" uses parameter name "verb" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:217): Function "_check_noun_verb_noun_pattern" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:217): Function "_check_noun_verb_noun_pattern" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:217): Function "_check_noun_verb_noun_pattern" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:217): Function "_check_noun_verb_noun_pattern" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:247): Function "_check_noun_verb_pattern" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:247): Function "_check_noun_verb_pattern" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:247): Function "_check_noun_verb_pattern" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:247): Function "_check_noun_verb_pattern" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:311): Function "_check_actor_prefix" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:311): Function "_check_actor_prefix" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:311): Function "_check_actor_prefix" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:311): Function "_check_actor_prefix" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:330): Function "_check_noun_only" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:330): Function "_check_noun_only" uses parameter name "name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:330): Function "_check_noun_only" uses parameter name "node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:330): Function "_check_noun_only" uses parameter name "node_type" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:28): Class "VocabularyHelper" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:38): Function "is_verb" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:38): Function "is_verb" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:48): Function "is_noun" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:48): Function "is_noun" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:58): Function "is_agent_noun" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:89): Function "is_gerund" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:89): Function "is_gerund" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:127): Function "get_pos_tags" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:127): Function "get_pos_tags" uses parameter name "text" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:137): Function "is_verb_tag" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:137): Function "is_verb_tag" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:143): Function "is_noun_tag" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:143): Function "is_noun_tag" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:149): Function "is_proper_noun_tag" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:149): Function "is_proper_noun_tag" uses parameter name "tag" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:155): Function "is_actor_or_role" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\vocabulary_helper.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/vocabulary_helper.py:155): Function "is_actor_or_role" uses parameter name "word" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:38): Function "from_action_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:38): Function "from_action_context" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:67): Function "_get_files_for_validation" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:67): Function "_get_files_for_validation" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:98): Function "from_parameters" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:137): Function "get_last_report_timestamp" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:183): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:220): Function "find_by_name" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:227): Function "__iter__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:232): Function "__len__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:235): Function "add_violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:235): Function "add_violations" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:239): Function "violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:243): Function "violation_summary" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:295): Function "_has_scanner_error" uses parameter name "execution_status" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:305): Function "_extract_error_message" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:305): Function "_extract_error_message" uses parameter name "execution_status" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:317): Function "_flush_logger_handlers" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:317): Function "_flush_logger_handlers" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:321): Function "_convert_violations_to_dicts" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:331): Function "_process_scanner_result" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:347): Function "_execute_scanner" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:347): Function "_execute_scanner" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:367): Function "_process_rule" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:367): Function "_process_rule" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:379): Function "validate" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:379): Function "validate" uses parameter name "exclude" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:384): Function "_create_legacy_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:384): Function "_create_legacy_context" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:384): Function "_create_legacy_context" uses parameter name "exclude" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:387): Function "_execute_validation" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:393): Function "_log_validation_start" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:393): Function "_log_validation_start" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:408): Function "_process_all_rules" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:408): Function "_process_all_rules" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:434): Function "_log_scanner_status_summary" uses parameter name "logger" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rule_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule_loader.py:10): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rule_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule_loader.py:52): Function "_load_rules_from_subdir" uses parameter name "subdir" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\rules\rule_loader.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rule_loader.py:67): Function "_is_in_disabled_folder" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:11): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:24): Function "strategy" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:28): Function "strategy_criteria" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:32): Function "typical_assumptions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:35): Function "_prepare_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:35): Function "_prepare_instructions" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:35): Function "_prepare_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:39): Function "_do_submit" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:39): Function "_do_submit" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:71): Function "_format_instructions_for_display" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:71): Function "_format_instructions_for_display" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:106): Function "_format_option" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:106): Function "_format_option" uses parameter name "option" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:128): Function "do_execute" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:128): Function "do_execute" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:136): Function "save_strategy" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\strategy\strategy_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/strategy/strategy_action.py:136): Function "save_strategy" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:15): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:32): Function "_prepare_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:32): Function "_prepare_instructions" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:32): Function "_prepare_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:74): Function "_run_scanners_and_format_results" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:117): Function "_format_scope_description" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:117): Function "_format_scope_description" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:181): Function "_do_submit" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:181): Function "_do_submit" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:195): Function "do_execute" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:195): Function "do_execute" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:222): Function "finalize_and_transition" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:226): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:28): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:28): Function "__init__" uses parameter name "timestamp" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:43): Function "start" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:63): Function "on_file_scanned" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:76): Function "_write_file_violations_header" uses parameter name "count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:81): Function "_write_violations" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:81): Function "_write_violations" uses parameter name "violations" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:85): Function "_extract_violation_fields" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:85): Function "_extract_violation_fields" uses parameter name "violation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:96): Function "_write_single_violation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:96): Function "_write_single_violation" uses parameter name "violation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:115): Function "_handle_executed_status" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:125): Function "_check_for_errors" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:134): Function "finish" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:134): Function "finish" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:145): Function "_write_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:145): Function "_write_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:149): Function "_flush" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:153): Function "write_cross_file_progress" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:163): Function "timestamp" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:168): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:168): Function "__init__" uses parameter name "timestamp" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:184): Function "_check_violation_severities" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:199): Function "_check_violations_in_key" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:212): Function "write" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:212): Function "write" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:222): Function "_write_report_file" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:237): Function "_write_section" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:237): Function "_write_section" uses parameter name "lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:241): Function "_log_write_error" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:254): Function "get_report_hyperlink" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:271): Function "_build_report_lines" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:271): Function "_build_report_lines" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:284): Function "_build_scanned_files_section" uses parameter name "section_title" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:299): Function "_format_violation_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:299): Function "_format_violation_line" uses parameter name "violation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:324): Function "_extract_test_info" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:324): Function "_extract_test_info" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:324): Function "_extract_test_info" uses parameter name "location" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:324): Function "_extract_test_info" uses parameter name "line_number" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:16): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:29): Function "from_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:29): Function "from_context" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:29): Function "from_context" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:63): Function "_build_scope" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:71): Function "_handle_scope_parameter" uses parameter name "scope_value" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:98): Function "files" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:105): Function "_auto_discover_if_needed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:105): Function "_auto_discover_if_needed" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:200): Function "_discover_files_from_directory" uses parameter name "dir_name" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\actions\validate\validation_scope.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_scope.py:203): Function "_auto_discover_files" uses parameter name "key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:11): Class "ErrorRecovery" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:13): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:13): Function "__init__" uses parameter name "max_attempts" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:13): Function "__init__" uses parameter name "current_attempts" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:13): Function "__init__" uses parameter name "wait_time" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:24): Function "can_retry" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:27): Function "increment_attempt" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:30): Function "wait_before_retry" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:30): Function "wait_before_retry" uses parameter name "duration" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:33): Function "is_recoverable" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:33): Function "is_recoverable" uses parameter name "error" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:36): Function "determines_if_error_is_recoverable" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:36): Function "determines_if_error_is_recoverable" uses parameter name "error" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\error_recovery.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/error_recovery.py:39): Function "raise_if_max_attempts_exceeded" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:7): Class "ExecutionContext" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:13): Function "loads_from_context_file" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:21): Function "_parses_content" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:21): Function "_parses_content" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:21): Function "_parses_content" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:34): Class "_ContextSections" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:36): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:42): Function "processes_line" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:42): Function "processes_line" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_context.py:53): Function "_appends_list_item" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:7): Class "ExecutionResult" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:37): Function "had_not_done_responses" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:40): Function "set_blocked_at_operation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:40): Function "set_blocked_at_operation" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:40): Function "set_blocked_at_operation" uses parameter name "operations_executed" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" uses parameter name "session_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" uses parameter name "loop_count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:53): Function "creates_blocked" uses parameter name "loop_responses" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "session_id" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "loop_count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "loop_responses" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\execution_result.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/execution_result.py:80): Function "creates_completed" uses parameter name "completed" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_config.py:9): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_config.py:9): Function "__init__" uses parameter name "api_key" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_config.py:9): Function "__init__" uses parameter name "log_dir" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_config.py:14): Function "load" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_config.py:14): Function "load" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_config.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_config.py:33): Function "api_key_prefix" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:13): Class "HeadlessSession" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:15): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:21): Function "invokes" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:21): Function "invokes" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:45): Function "invokes_operation" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:45): Function "invokes_operation" uses parameter name "operation" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:120): Function "_load_context" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:125): Function "_prepare_instructions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:125): Function "_prepare_instructions" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:125): Function "_prepare_instructions" uses parameter name "context" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:153): Function "_execute_with_monitoring" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:153): Function "_execute_with_monitoring" uses parameter name "instructions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:153): Function "_execute_with_monitoring" uses parameter name "context_loaded" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:153): Function "_execute_with_monitoring" uses parameter name "should_block" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:201): Function "_simulate_ai_execution" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:201): Function "_simulate_ai_execution" uses parameter name "loop_count" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\headless_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/headless_session.py:201): Function "_simulate_ai_execution" uses parameter name "should_block" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\non_recoverable_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/non_recoverable_error.py:1): Class "NonRecoverableError" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\non_recoverable_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/non_recoverable_error.py:3): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\non_recoverable_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/non_recoverable_error.py:3): Function "__init__" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\recoverable_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/recoverable_error.py:1): Class "RecoverableError" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\recoverable_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/recoverable_error.py:3): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\recoverable_error.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/recoverable_error.py:3): Function "__init__" uses parameter name "message" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:6): Class "SessionLog" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:8): Function "__init__" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:15): Function "creates_with_timestamped_path" uses parameter name "cls" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:15): Function "creates_with_timestamped_path" uses parameter name "base_dir" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:20): Function "appends_response" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:20): Function "appends_response" uses parameter name "response" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:34): Function "appends_total_loops" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:34): Function "appends_total_loops" uses parameter name "total_loops" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\headless\session_log.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/headless/session_log.py:39): Function "get_transcript" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 253 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:357): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_find_scope_matches_in_graph (lines 357-362)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```

  Location 2 (repl_session.py:_find_scope_matches (lines 1220-1225)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:368): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_search_for_scope_match (lines 368-374)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (repl_session.py:_search_for_scope_match (lines 1230-1236)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:380): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_search_sub_epics (lines 380-386)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (repl_session.py:_search_sub_epics (lines 1241-1247)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:419): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 419-433)):
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

  Location 2 (repl_session.py:_format_node_with_children (lines 1269-1283)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:420): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 420-437)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1270-1287)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:420): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 420-437)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1270-1289)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:423): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 423-439)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1273-1289)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:423): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 423-439)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1270-1289)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:419): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 419-437)):
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

  Location 2 (repl_session.py:_format_node_with_children (lines 1269-1287)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:420): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1270-1287)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:420): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1273-1289)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\action_context.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/action_context.py:420): Duplicate code detected across files - extract to shared function.

  Location 1 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```

  Location 2 (repl_session.py:_format_node_with_children (lines 1270-1289)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1220): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_find_scope_matches (lines 1220-1225)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```

  Location 2 (action_context.py:_find_scope_matches_in_graph (lines 357-362)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1230): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_for_scope_match (lines 1230-1236)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_for_scope_match (lines 368-374)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1241): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_sub_epics (lines 1241-1247)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_sub_epics (lines 380-386)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1269): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1269-1283)):
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

  Location 2 (action_context.py:_format_node_with_children (lines 419-433)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1270): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1270-1287)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-437)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1270): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1270-1287)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1273): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1273-1289)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 423-439)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1273): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1273-1289)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1269): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1269-1287)):
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

  Location 2 (action_context.py:_format_node_with_children (lines 419-437)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1270): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1270-1289)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-437)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1270): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1270-1289)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 423-439)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1270): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1270-1289)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 420-439)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-18)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-18)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-19)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-42)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-29)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-20)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-29)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-20)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-29)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-21)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-29)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-44)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-31)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 13-22)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-31)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-23)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-31)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 37-46)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 16-26)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 16-24)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 13-24)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.appen...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 17-25)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-25)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 17-27)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-33)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 40-48)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-35)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 58-66)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 43-52)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 51-60)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 55-64)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 59-68)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 59-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violat...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:31): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 31-39)):
    ```python
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 22-30)):
    ```python
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:31): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 31-39)):
    ```python
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:31): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 31-39)):
    ```python
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 62-70)):
    ```python
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-29)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-20)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-29)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-20)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-29)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-21)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-29)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-44)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-31)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-22)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-31)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-22)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-31)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-24)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
       ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-31)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-23)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-31)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-46)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 13-24)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation:
        violations....
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 13-26)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation:
        violations....
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 13-24)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.appen...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-25)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-27)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 37-48)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:25): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 25-35)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_ca...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 40-50)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 54-64)):
    ```python
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 58-68)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 58-70)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 43-52)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 51-60)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 55-64)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 59-68)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 59-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violat...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-31)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-22)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-31)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-22)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-31)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-24)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    i...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-31)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-23)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-31)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-46)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-24)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-26)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-22)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-24)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
       ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-25)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violat...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-27)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violat...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-48)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 54-64)):
    ```python
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 58-68)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 58-70)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:27): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 55-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._chec...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-24)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-26)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-22)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-24)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    i...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-25)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-48)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-35)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-50)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-35)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-50)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-37)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 37-52)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-37)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-52)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-35)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-50)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-35)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-50)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-37)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-28)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
       ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-37)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-52)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-37)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-52)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:22): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 22-39)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 37-52)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-37)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-28)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    i...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:19): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 19-37)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 34-52)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\active_language_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/active_language_scanner.py:20): Duplicate code detected across files - extract to shared function.

  Location 1 (active_language_scanner.py:scan_story_node (lines 20-39)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```

  Location 2 (verb_noun_scanner.py:scan_story_node (lines 35-52)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:269): Duplicate code detected across files - extract to shared function.

  Location 1 (story_map.py:from_bot (lines 269-286)):
    ```python
    if hasattr(bot, 'bot_paths') and hasattr(bot.bot_paths, 'bot_directory'):
        bot_directory = Path(bot.bot_paths.bot_directory)
    elif hasattr(bot, 'bot_directory'):
        bot_directory = Path(bot.bot_directory)
    elif isinstance(bot, (str, Path)):
        bot_directory = Path(bot)
    else:
        raise TypeError(f...
    ```

  Location 2 (nodes.py:from_bot (lines 350-363)):
    ```python
    if hasattr(bot, 'bot_paths') and hasattr(bot.bot_paths, 'bot_directory'):
        bot_directory = Path(bot.bot_paths.bot_directory)
    elif hasattr(bot, 'bot_directory'):
        bot_directory = Path(bot.bot_directory)
    elif isinstance(bot, (str, Path)):
        bot_directory = Path(bot)
    else:
        raise TypeError(f...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\story_map.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/story_map.py:267): Duplicate code detected across files - extract to shared function.

  Location 1 (story_map.py:from_bot (lines 267-286)):
    ```python
    import json
    if hasattr(bot, 'bot_paths') and hasattr(bot.bot_paths, 'bot_directory'):
        bot_directory = Path(bot.bot_paths.bot_directory)
    elif hasattr(bot, 'bot_directory'):
        bot_directory = Path(bot.bot_directory)
    elif isinstance(bot, (str, Path)):
        bot_directory = Path(bot)
    else:
        raise...
    ```

  Location 2 (nodes.py:from_bot (lines 350-363)):
    ```python
    if hasattr(bot, 'bot_paths') and hasattr(bot.bot_paths, 'bot_directory'):
        bot_directory = Path(bot.bot_paths.bot_directory)
    elif hasattr(bot, 'bot_directory'):
        bot_directory = Path(bot.bot_directory)
    elif isinstance(bot, (str, Path)):
        bot_directory = Path(bot)
    else:
        raise TypeError(f...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-42)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-42)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-18)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-42)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-18)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-42)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-19)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-44)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-29)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-44)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-20)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-44)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-20)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-44)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-21)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-46)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 22-31)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-46)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 13-22)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-46)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-23)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 40-48)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 16-26)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 40-48)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-25)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 40-48)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 17-27)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:43): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 43-52)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:43): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 43-52)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:43): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 43-52)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:47): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 47-56)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:47): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 47-56)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:47): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 47-56)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:47): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 47-56)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:50): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 50-58)):
    ```python
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, no...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-35)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:51): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 51-60)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:51): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 51-60)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:51): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 51-60)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:51): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 51-60)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:54): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 54-62)):
    ```python
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-35)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:55): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 55-64)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:55): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 55-64)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:55): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 55-64)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:55): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 55-64)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:58): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 58-66)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-35)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-68)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-68)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-68)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-68)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:62): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 62-70)):
    ```python
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 31-39)):
    ```python
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:62): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 62-70)):
    ```python
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 22-30)):
    ```python
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:62): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 62-70)):
    ```python
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 19-27)):
    ```python
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violations
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-44)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-29)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-44)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-20)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-44)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-20)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-44)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-21)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-46)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-31)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-46)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-22)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-46)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-23)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-48)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 22-33)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-48)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 13-26)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation:
        violations....
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-48)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 13-24)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.appen...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-48)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-25)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-48)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 14-27)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violations.append(viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 40-50)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 25-35)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_ca...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:50): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 50-60)):
    ```python
    violation = self._check_noun_verb_noun_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, no...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:54): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 54-64)):
    ```python
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:54): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 54-64)):
    ```python
    violation = self._check_noun_verb_pattern(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:58): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 58-68)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:58): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 58-68)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violat...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-37)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violat...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 28-39)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violati...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violat...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-28)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:59): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 59-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return violat...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 19-30)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_generic_technical_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    return...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-46)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-31)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-46)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-22)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-46)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-23)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-48)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-33)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-48)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 11-26)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_obj)
    if violation...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-48)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 11-24)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    if violation:
       ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-48)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-25)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violat...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-48)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 12-27)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if violation:
        violat...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-50)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 22-35)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 40-52)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 22-37)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:40): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 40-52)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 25-39)):
    ```python
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_ca...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:58): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 58-70)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-37)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:58): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 58-70)):
    ```python
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_third_person_singular(name, node, node_type, ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-48)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-33)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-48)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (communication_verb_scanner.py:scan_story_node (lines 10-26)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_communication_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_enablement_verbs(name, node, node_type, rule_o...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-48)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (generic_capability_scanner.py:scan_story_node (lines 10-24)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_capability_verbs(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_states(name, node, node_type, rule_obj)
    i...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-48)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-25)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-48)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (specificity_scanner.py:scan_story_node (lines 11-27)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_too_generic(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_too_specific(name, node, node_type, rule_obj)
    if viola...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-50)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-35)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-50)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-35)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-52)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 22-37)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-52)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-37)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:37): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 37-52)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        violations.append(...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 22-39)):
    ```python
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:55): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 55-70)):
    ```python
    if violation:
        violations.append(violation)
    violation = self._check_actor_prefix(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_noun_only(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._chec...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 27-39)):
    ```python
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_capability_nouns(name, node, node_type, ...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-50)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-35)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-50)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-35)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-50)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-37)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-52)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-37)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-52)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-37)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:35): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 35-52)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if violation:
        v...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 20-39)):
    ```python
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if violation:
        vio...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-52)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-35)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\verb_noun_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/verb_noun_scanner.py:34): Duplicate code detected across files - extract to shared function.

  Location 1 (verb_noun_scanner.py:scan_story_node (lines 34-52)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_verb_noun_order(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_gerund_ending(name, node, node_type, rule_obj)
    if ...
    ```

  Location 2 (active_language_scanner.py:scan_story_node (lines 19-37)):
    ```python
    violations = []
    name = node.name
    if not name:
        return violations
    node_type = self._get_node_type(node)
    violation = self._check_actor_in_name(name, node, node_type, rule_obj)
    if violation:
        violations.append(violation)
    violation = self._check_passive_voice(name, node, node_type, rule_obj)
    if vi...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-318)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-26)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-319)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-27)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-320)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-28)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-320)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-29)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-320)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-30)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:316): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 316-321)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 24-29)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:316): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 316-321)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-29)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:316): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 316-321)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 24-30)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:318): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 318-322)):
    ```python
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_line}']
    lines.extend(self.violation_formatter.format_multiline_message_parts(parts[1:]))
    return lines
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 26-30)):
    ```python
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_line}']
    lines.extend(self._format_multiline_message_parts(parts[1:]))
    return lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-319)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-27)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-320)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-28)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-320)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-29)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-320)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-30)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-321)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-28)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-321)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 24-29)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-321)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-29)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-321)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-30)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:316): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 316-322)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 24-29)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:316): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 316-322)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 24-30)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:316): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 316-322)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-30)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-320)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-28)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-320)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 19-28)):
    ```python
    location_link = create_file_link_fn(location, line_number)
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in fo...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-320)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-29)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-320)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-30)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-321)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-28)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-321)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-29)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-321)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-29)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-321)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-30)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-322)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-28)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-322)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-29)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-322)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 24-30)):
    ```python
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts else formatted_message
    lines = [f'- {severity_icon} **{severity.upper()}** - {location_link}: {first_...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:314): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 314-322)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 22-30)):
    ```python
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = formatted_message.split('\n')
    first_line = parts[0] if parts...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-321)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-28)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-321)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-29)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-321)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 19-29)):
    ```python
    location_link = create_file_link_fn(location, line_number)
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in fo...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-321)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-30)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-322)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-29)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-322)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 21-30)):
    ```python
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']
    parts = for...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:313): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 313-322)):
    ```python
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {formatted_message}']...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-30)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-322)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-28)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-322)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-29)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-322)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 20-30)):
    ```python
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_icon} **{severit...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:312): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_format_violation_line (lines 312-322)):
    ```python
    test_info = self._extract_test_info(message, location, line_number)
    formatted_message = self.formatter.format_violation_message(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in formatted_message:
        return [f'- {severity_i...
    ```

  Location 2 (validation_report_formatter.py:format_violation_line (lines 19-30)):
    ```python
    location_link = create_file_link_fn(location, line_number)
    test_info = extract_test_info_fn(message, location, line_number)
    formatted_message = format_violation_message_fn(message)
    if test_info:
        return [f'- {severity_icon} **{severity.upper()}** - {location_link}: {test_info}']
    if '\n' not in fo...
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
*... and 65 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-29_17-25-11.md`

