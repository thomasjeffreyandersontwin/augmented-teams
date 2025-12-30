# Validation Report - Code

**Generated:** 2025-12-30 02:52:27
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
| 🟩 Clean Rules | 21 | No violations found |
| 🟨 Rules with Warnings | 5 | Found 13 warning violation(s) |
| 🟥 Rules with Errors | 2 | Found 5 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟨 **[Use Domain Language](#use-domain-language)** - 32 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-domain-language-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.domain_language_code_scanner.DomainLanguageCodeScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 6 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 4 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟩 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟩 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.delegation_code_scanner.DelegationCodeScanner`
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
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
- 🟩 **[Provide Meaningful Context](#provide-meaningful-context)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟩 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
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

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 4 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 1 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 6 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 3 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** CRITICAL: Function signatures must be simple and intention-revealing. Prefer 0-2 parameters. NEVER pass Dict[str, Any] or List[str] for complex data - create typed objects instead. Examples: parameters dict → ParametersObject, files dict → FilesCollection, exclude list → ExcludePatterns.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 2 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 1 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 1 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.class_size_scanner.ClassSizeScanner`
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

### 🟩 Rule: <span id="keep-functions-single-responsibility">Keep Functions Single Responsibility</span> - CLEAN (0 violations)
**Description:** CRITICAL: Functions should do one thing and do it well, with no hidden side effects. Each function must have a single, well-defined responsibility.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - CLEAN (0 violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
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

**Total Violations:** 54
- **File-by-File Violations:** 50
- **Cross-File Violations:** 4

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:67): Line 67: Variable truthiness check detected (if is_agent:). Assume variable exists - let code fail fast if missing.

    ```python
                        # Check if class name is an agent noun using NLTK
                        is_agent, base_verb, suffix = VocabularyHelper.is_agent_noun(cls.node.name)
                        if is_agent:
                            loader_classes[cls.node.name] = (file_path, cls.node, suffix)
                except (SyntaxError, UnicodeDecodeError) as e:
    ```

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 1 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:12): Class "GivenWhenThenHelpersScanner" is 313 lines - should be under 300 lines (extract related methods into separate classes)

```python


class GivenWhenThenHelpersScanner(TestScanner):
    
    # Minimum number of consecutive non-helper lines to flag as violation
    # Only flag 4+ lines to optimize for reusable functions, not exact step names
    MIN_INLINE_LINES = 4
    
    # Helper function name patterns (these are OK - code calling these is not a violation)
    HELPER_PATTERNS = [
    # ... (truncated)
```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:270): Function "scan_cross_file" is 43 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return None, [], False, 0
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None,
            max_cross_file_comparisons: Optional[int] = None
        ) -> List[Dict[str, Any]]:
            violations = []
            
            if not test_files or len(test_files) < 2:
                # Need at least 2 files to detect cross-file issues
                return violations
            
            # Reuse base class method to parse all test files
            parsed_files = self._get_all_test_files_parsed(test_files)
            
            helper_definitions = {}  # func_name -> list of (file_path, line_number)
            
            for file_path, content, tree in parsed_files:
                # Reuse existing method to get defined helpers
                defined_helpers = self._get_defined_helper_functions(tree)
                
                for func_name, line_number in defined_helpers.items():
                    if func_name not in helper_definitions:
                        helper_definitions[func_name] = []
                    helper_definitions[func_name].append((
                        str(file_path),
                        line_number
                    ))
            
            # Check: Duplicate helper functions across files (ONLY - no usage warnings)
            for func_name, definitions in helper_definitions.items():
                if len(definitions) > 1:
                    # Same helper function defined in multiple files - should be consolidated
                    files_list = ', '.join([f"{Path(f).name}:{line}" for f, line in definitions])
                    violation = Violation(
                        rule=rule_obj,
                        violation_message=(
                            f'Helper function "{func_name}" is defined in {len(definitions)} different files. '
                            f'Consolidate into a shared helper file based on reuse scope. '
                            f'Found in: {files_list}'
                        ),
                        location=definitions[0][0],  # First occurrence
                        line_number=definitions[0][1],
                        severity='error'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" is 48 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None,
            max_cross_file_comparisons: Optional[int] = None
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
        # ... (truncated)
    ```

#### <span id="maintain-vertical-density-violations">Maintain Vertical Density: 4 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" is 74 lines - consider improving vertical density by declaring variables near usage

    ```python
            return None
        
        def _find_inline_code_blocks(self, test_node: ast.FunctionDef, test_body_lines: List[str],
                                     helper_functions: Set[str], tree: ast.AST) -> List[Tuple[int, int, List[str]]]:
            blocks = []
            current_block_start = None
            current_block_lines = []
            
            # test_body_lines includes the def line, so body starts at lineno + 1
            body_start_line = test_node.lineno
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:270): Function "scan_cross_file" is 55 lines - consider improving vertical density by declaring variables near usage

    ```python
            return None, [], False, 0
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None,
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" is 60 lines - consider improving vertical density by declaring variables near usage

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
            test_files: Optional[List[Path]] = None,
            code_files: Optional[List[Path]] = None,
            all_test_files: Optional[List[Path]] = None,
            all_code_files: Optional[List[Path]] = None,
            status_writer: Optional[Any] = None,
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:106): Function "_class_uses_as_attribute" is 51 lines - consider improving vertical density by declaring variables near usage

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

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 6 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:48): Function "_get_helper_functions" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return violations
        
        def _get_helper_functions(self, tree: ast.AST, content: str) -> Set[str]:
            helpers = set()
            
            defined_helpers = self._get_defined_helper_functions(tree)
            helpers.update(defined_helpers.keys())
            
            # Also check for imported helper functions (from conftest, test_helpers, etc.)
            # Look for imports and add any functions that match helper patterns
            for node in ast.walk(tree):
                if isinstance(node, ast.ImportFrom):
                    module = node.module or ''
                    if any(helper_mod in module for helper_mod in ['conftest', 'test_helpers', '_helpers']):
                        for alias in node.names:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:69): Function "_get_defined_helper_functions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return helpers
        
        def _get_defined_helper_functions(self, tree: ast.AST) -> Dict[str, int]:
            helpers = {}
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_name = node.name
                    for pattern in self.HELPER_PATTERNS:
                        if re.match(pattern, func_name, re.IGNORECASE):
                            helpers[func_name] = node.lineno
                            break
            
            return helpers
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:82): Function "_get_helper_calls_in_file" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return helpers
        
        def _get_helper_calls_in_file(self, tree: ast.AST, content: str) -> Set[str]:
            helper_calls = set()
            helper_functions = self._get_helper_functions(tree, content)
            
            # Walk through all call nodes to find helper function calls
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    func_name = None
                    if isinstance(node.func, ast.Name):
                        func_name = node.func.id
                    elif isinstance(node.func, ast.Attribute):
                        if isinstance(node.func.value, ast.Name) and node.func.value.id == 'self':
                            func_name = node.func.attr
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return None
        
        def _find_inline_code_blocks(self, test_node: ast.FunctionDef, test_body_lines: List[str],
                                     helper_functions: Set[str], tree: ast.AST) -> List[Tuple[int, int, List[str]]]:
            blocks = []
            current_block_start = None
            current_block_lines = []
            
            # test_body_lines includes the def line, so body starts at lineno + 1
            body_start_line = test_node.lineno
            
            docstring_range = self._get_docstring_line_range(test_node)
            
            # Track if we're in a multi-line function call and parenthesis balance
            in_multiline_call = False
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
            status_writer: Optional[Any] = None,
            max_cross_file_comparisons: Optional[int] = None
        ) -> List[Dict[str, Any]]:
            violations = []
            
            all_files = []
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:106): Function "_class_uses_as_attribute" has nesting depth of 10 - use guard clauses and extract nested blocks to reduce nesting

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

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:17): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
    class ResourceOrientedCodeScanner(CodeScanner):
        """
        Validates that code classes are named after resources (what they ARE)
        rather than actions (what they DO).
        
        Uses NLTK to detect agent nouns (Manager, Loader, Handler, etc.)
        """
        
    ```

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:112): Function "_check_test_method" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                return None
        
        def _check_test_method(self, test_node: ast.FunctionDef, content: str, file_path: Path, 
                              rule_obj: Any, helper_functions: Set[str], tree: ast.AST) -> List[Dict[str, Any]]:
            violations = []
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:270): Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return None, [], False, 0
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return []
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
        # ... (truncated)
    ```

#### <span id="use-domain-language-violations">Use Domain Language: 32 violation(s)</span>

- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:27): Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:48): Function "_get_helper_functions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:48): Function "_get_helper_functions" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:48): Function "_get_helper_functions" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:69): Function "_get_defined_helper_functions" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:69): Function "_get_defined_helper_functions" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:82): Function "_get_helper_calls_in_file" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:82): Function "_get_helper_calls_in_file" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:112): Function "_check_test_method" uses parameter name "test_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:112): Function "_check_test_method" uses parameter name "content" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:112): Function "_check_test_method" uses parameter name "helper_functions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:112): Function "_check_test_method" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:146): Function "_get_docstring_line_range" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:146): Function "_get_docstring_line_range" uses parameter name "test_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" uses parameter name "test_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" uses parameter name "test_body_lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" uses parameter name "helper_functions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:168): Function "_find_inline_code_blocks" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:243): Function "_is_helper_function_call" uses parameter name "line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:243): Function "_is_helper_function_call" uses parameter name "helper_functions" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:243): Function "_is_helper_function_call" uses parameter name "tree" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:264): Function "_end_current_block" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:264): Function "_end_current_block" uses parameter name "blocks" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:264): Function "_end_current_block" uses parameter name "current_block_start" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:264): Function "_end_current_block" uses parameter name "end_line" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:264): Function "_end_current_block" uses parameter name "current_block_lines" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:270): Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:24): Function "scan_file" uses parameter name "knowledge_graph" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:28): Function "scan_cross_file" uses parameter name "status_writer" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:89): Function "_is_owned_by_domain_object" doesn't match domain terms. Use domain-specific language from specification: action, agent, behavior, bot, call, calls, catalog, class, classes, config...
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\resource_oriented_code_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/resource_oriented_code_scanner.py:89): Function "_is_owned_by_domain_object" uses parameter name "loader_node" that doesn't match domain terms. Use domain-specific language: action, agent, behavior, bot, call, calls, catalog, class, classes, config...

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 4 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (given_when_then_helpers_scanner.py:scan_file (lines 28-36)):
    ```python
    violations = []
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    content, lines, tree = parsed
    helper_functions = self._get_helper_functions(tree, content)
    ```

  Location 2 (abstraction_levels_scanner.py:scan_file (lines 17-25)):
    ```python
    violations = []
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    content, lines, tree = parsed
    functions = Functions(tree)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (given_when_then_helpers_scanner.py:scan_file (lines 28-36)):
    ```python
    violations = []
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    content, lines, tree = parsed
    helper_functions = self._get_helper_functions(tree, content)
    ```

  Location 2 (arrange_act_assert_scanner.py:scan_file (lines 17-25)):
    ```python
    violations = []
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    content, lines, tree = parsed
    functions = Functions(tree)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:28): Duplicate code detected across files - extract to shared function.

  Location 1 (given_when_then_helpers_scanner.py:scan_file (lines 28-36)):
    ```python
    violations = []
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    content, lines, tree = parsed
    helper_functions = self._get_helper_functions(tree, content)
    ```

  Location 2 (calculation_timing_code_scanner.py:scan_file (lines 25-33)):
    ```python
    violations = []
    parsed = self._read_and_parse_file(file_path)
    if not parsed:
        return violations
    content, lines, tree = parsed
    functions = Functions(tree)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\scanners\given_when_then_helpers_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/given_when_then_helpers_scanner.py:105): Duplicate code detected across files - extract to shared function.

  Location 1 (given_when_then_helpers_scanner.py:_parse_test_file (lines 105-110)):
    ```python
    content = file_path.read_text(encoding='utf-8')
    tree = ast.parse(content, filename=str(file_path))
    return (content, tree)
    ```

  Location 2 (code_scanner.py:_parse_code_file (lines 194-199)):
    ```python
    content = file_path.read_text(encoding='utf-8')
    tree = ast.parse(content, filename=str(file_path))
    return (content, tree)
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
*... and 60 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-30_02-52-21.md`

