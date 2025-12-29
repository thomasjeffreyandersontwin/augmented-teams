# Validation Report - Code

**Generated:** 2025-12-29 00:33:01
**Project:** base_bot
**Behavior:** code
**Action:** validate

## Summary

Validated story map and domain model and 265 code file(s) against **32 validation rules**.

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
  - `src\story_graph\domain.py`
  - `src\story_graph\nodes.py`
  - `src\utils.py`
  - **Total:** 265 src file(s)

## Scanner Execution Status

### 🟨 Overall Status: NEEDS ATTENTION

| Status | Count | Description |
|--------|-------|-------------|
| 🟩 Executed Successfully | 30 | Scanners ran without errors |
| 🟩 Clean Rules | 16 | No violations found |
| 🟨 Rules with Warnings | 9 | Found 138 warning violation(s) |
| 🟥 Rules with Errors | 4 | Found 152 error violation(s) |
| [i] No Scanner | 2 | Rule has no scanner configured |

**Total Rules:** 32
- **Rules with Scanners:** 30
  - 🟩 **Executed Successfully:** 30
- [i] **Rules without Scanners:** 2

### 🟩 Successfully Executed Scanners

- 🟥 **[Eliminate Duplication](#eliminate-duplication)** - 83 violation(s) (EXECUTION_SUCCESS) - [View Details](#eliminate-duplication-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
- 🟨 **[Provide Meaningful Context](#provide-meaningful-context)** - 76 violation(s) (EXECUTION_SUCCESS) - [View Details](#provide-meaningful-context-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
- 🟥 **[Stop Writing Useless Comments](#stop-writing-useless-comments)** - 66 violation(s) (EXECUTION_SUCCESS) - [View Details](#stop-writing-useless-comments-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
- 🟨 **[Simplify Control Flow](#simplify-control-flow)** - 33 violation(s) (EXECUTION_SUCCESS) - [View Details](#simplify-control-flow-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
- 🟨 **[Maintain Vertical Density](#maintain-vertical-density)** - 14 violation(s) (EXECUTION_SUCCESS) - [View Details](#maintain-vertical-density-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.vertical_density_scanner.VerticalDensityScanner`
- 🟨 **[Keep Functions Small Focused](#keep-functions-small-focused)** - 7 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-functions-small-focused-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
- 🟨 **[Use Clear Function Parameters](#use-clear-function-parameters)** - 7 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-clear-function-parameters-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
- 🟨 **[Avoid Excessive Guards](#avoid-excessive-guards)** - 5 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-excessive-guards-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
- 🟨 **[Keep Classes Small With Single Responsibility](#keep-classes-small-with-single-responsibility)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#keep-classes-small-with-single-responsibility-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
- 🟨 **[Refactor Completely Not Partially](#refactor-completely-not-partially)** - 3 violation(s) (EXECUTION_SUCCESS) - [View Details](#refactor-completely-not-partially-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
- 🟨 **[Avoid Unnecessary Parameter Passing](#avoid-unnecessary-parameter-passing)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#avoid-unnecessary-parameter-passing-violations)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
- 🟨 **[Enforce Encapsulation](#enforce-encapsulation)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#enforce-encapsulation-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
- 🟥 **[Never Swallow Exceptions](#never-swallow-exceptions)** - 2 violation(s) (EXECUTION_SUCCESS) - [View Details](#never-swallow-exceptions-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
- 🟥 **[Use Resource Oriented Design](#use-resource-oriented-design)** - 1 violation(s) (EXECUTION_SUCCESS) - [View Details](#use-resource-oriented-design-violations)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
- 🟩 **[Chain Dependencies Properly](#chain-dependencies-properly)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
- 🟩 **[Classify Exceptions By Caller Needs](#classify-exceptions-by-caller-needs)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
- 🟩 **[Delegate To Lowest Level](#delegate-to-lowest-level)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
- 🟩 **[Favor Code Representation](#favor-code-representation)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.code_representation_code_scanner.CodeRepresentationCodeScanner`
- 🟩 **[Group By Domain](#group-by-domain)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.domain_grouping_code_scanner.DomainGroupingCodeScanner`
- 🟩 **[Hide Business Logic Behind Properties](#hide-business-logic-behind-properties)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Hide Calculation Timing](#hide-calculation-timing)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.calculation_timing_code_scanner.CalculationTimingCodeScanner`
- 🟩 **[Keep Functions Single Responsibility](#keep-functions-single-responsibility)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.single_responsibility_scanner.SingleResponsibilityScanner`
- 🟩 **[Place Imports At Top](#place-imports-at-top)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.actions.validate.scanners.import_placement_scanner.ImportPlacementScanner`
- 🟩 **[Prefer Object Model Over Config](#prefer-object-model-over-config)** - 0 violations (EXECUTION_SUCCESS)
  - Scanner: `agile_bot.bots.base_bot.src.scanners.prefer_object_model_over_config_scanner.PreferObjectModelOverConfigScanner`
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

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Detect Legacy Unused Code](#detect-legacy-unused-code)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Refactor Tests With Production Code](#refactor-tests-with-production-code)** - No scanner configured

## Validation Rules Checked

### 🟥 Rule: <span id="eliminate-duplication">Eliminate Duplication</span> - 83 ERROR(S) - [View Details](#eliminate-duplication-violations)
**Description:** CRITICAL: Every piece of knowledge should have a single, authoritative representation (DRY principle). Extract repeated logic into reusable functions and use abstraction to capture common patterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.duplication_scanner.DuplicationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="stop-writing-useless-comments">Stop Writing Useless Comments</span> - 66 ERROR(S) - [View Details](#stop-writing-useless-comments-violations)
**Description:** CRITICAL: DO NOT WRITE COMMENTS. Delete all comments written by the AI chat. Code must be self-explanatory through clear naming and structure. ONLY exception: legal/license requirements. If you think a comment is needed, the code is wrong - fix the code instead.
**Scanner:** `agile_bot.bots.base_bot.src.actions.scanners.useless_comments_scanner.UselessCommentsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="never-swallow-exceptions">Never Swallow Exceptions</span> - 2 ERROR(S) - [View Details](#never-swallow-exceptions-violations)
**Description:** CRITICAL: Never swallow exceptions silently. Empty catch blocks hide failures and make debugging impossible. Always log, handle, or rethrow exceptions with context.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.swallowed_exceptions_scanner.SwallowedExceptionsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟥 Rule: <span id="use-resource-oriented-design">Use Resource Oriented Design</span> - 1 ERROR(S) - [View Details](#use-resource-oriented-design-violations)
**Description:** CRITICAL: Code must use resource-oriented, object-oriented design. Use object-oriented classes (singular or collection) with responsibilities that encapsulate logic over manager/doer/loader patterns. Maximize encapsulation through collaborator relationships.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.resource_oriented_code_scanner.ResourceOrientedCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="provide-meaningful-context">Provide Meaningful Context</span> - 76 WARNING(S) - [View Details](#provide-meaningful-context-violations)
**Description:** Names should provide appropriate context without redundancy. Use longer names for longer scopes and replace magic numbers with named constants.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.meaningful_context_scanner.MeaningfulContextScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="simplify-control-flow">Simplify Control Flow</span> - 33 WARNING(S) - [View Details](#simplify-control-flow-violations)
**Description:** Keep nesting minimal and control flow straightforward. Use guard clauses to reduce nesting and extract nested blocks into separate functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.simplify_control_flow_scanner.SimplifyControlFlowScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-functions-small-focused">Keep Functions Small Focused</span> - 7 WARNING(S) - [View Details](#keep-functions-small-focused-violations)
**Description:** Functions should be small enough to understand at a glance. Keep functions under 20 lines when possible and extract complex logic into named helper functions.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.function_size_scanner.FunctionSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="use-clear-function-parameters">Use Clear Function Parameters</span> - 7 WARNING(S) - [View Details](#use-clear-function-parameters-violations)
**Description:** CRITICAL: Function signatures must be simple and intention-revealing. Prefer 0-2 parameters. NEVER pass Dict[str, Any] or List[str] for complex data - create typed objects instead. Examples: parameters dict → ParametersObject, files dict → FilesCollection, exclude list → ExcludePatterns.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.clear_parameters_scanner.ClearParametersScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-excessive-guards">Avoid Excessive Guards</span> - 5 WARNING(S) - [View Details](#avoid-excessive-guards-violations)
**Description:** Excessive guard clauses add to cyclomatic complexity and make code harder to read. Centralize error handling in one place rather than scattering defensive checks throughout the code. Let code fail fast with clear errors rather than silently handling missing components.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.excessive_guards_scanner.ExcessiveGuardsScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="keep-classes-small-with-single-responsibility">Keep Classes Small With Single Responsibility</span> - 3 WARNING(S) - [View Details](#keep-classes-small-with-single-responsibility-violations)
**Description:** CRITICAL: Classes should be small (under 200-300 lines) with a single responsibility. Keep classes cohesive (methods/data interdependent), eliminate dead code, and favor many small focused classes over few large ones.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.class_size_scanner.ClassSizeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="refactor-completely-not-partially">Refactor Completely Not Partially</span> - 3 WARNING(S) - [View Details](#refactor-completely-not-partially-violations)
**Description:** CRITICAL: When refactoring, replace old code completely - don't try to support both legacy and new patterns. Write new code, delete old code, fix tests. Clean breaks are better than compatibility bridges that create technical debt.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.complete_refactoring_scanner.CompleteRefactoringScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="avoid-unnecessary-parameter-passing">Avoid Unnecessary Parameter Passing</span> - 2 WARNING(S) - [View Details](#avoid-unnecessary-parameter-passing-violations)
**Description:** Don't pass parameters to internal methods when the value is already accessible through instance variables. Access instance properties directly instead of passing them around unnecessarily.
**Scanner:** `agile_bot.bots.base_bot.src.scanners.unnecessary_parameter_passing_scanner.UnnecessaryParameterPassingScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟨 Rule: <span id="enforce-encapsulation">Enforce Encapsulation</span> - 2 WARNING(S) - [View Details](#enforce-encapsulation-violations)
**Description:** CRITICAL: Hide implementation details and expose minimal interface. Make fields private by default, expose behavior not data. NEVER pass raw dicts/lists that expose internal structure - use typed objects that encapsulate the data. Follow Law of Demeter (principle of least knowledge).
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.encapsulation_scanner.EncapsulationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="chain-dependencies-properly">Chain Dependencies Properly</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must chain dependencies properly with constructor injection. Map dependencies in a chain: highest-level object → collaborator → sub-collaborator. Inject collaborators at construction time so methods can use them without passing them as parameters. Access sub-collaborators through their owning objects.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.dependency_chaining_code_scanner.DependencyChainingCodeScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="classify-exceptions-by-caller-needs">Classify Exceptions By Caller Needs</span> - CLEAN (0 violations)
**Description:** Design exceptions based on how callers will handle them. Create exception types based on caller's needs, use special case objects for predictable failures, and wrap third-party exceptions at boundaries.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.exception_classification_scanner.ExceptionClassificationScanner`
**Execution Status:** EXECUTION_SUCCESS

### 🟩 Rule: <span id="delegate-to-lowest-level">Delegate To Lowest Level</span> - CLEAN (0 violations)
**Description:** CRITICAL: Code must delegate responsibilities to the lowest-level object that can handle them. If a collection class can do something, delegate to it rather than implementing it in the parent.
**Scanner:** `agile_bot.bots.base_bot.src.actions.validate.scanners.delegation_code_scanner.DelegationCodeScanner`
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

*... and 12 more rules*

## Violations Found

**Total Violations:** 304
- **File-by-File Violations:** 224
- **Cross-File Violations:** 80

### File-by-File Violations (Pass 1)

These violations were detected by scanning each file individually.

#### <span id="avoid-excessive-guards-violations">Avoid Excessive Guards: 5 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1109): Line 1109: Variable truthiness check detected (if not args:). Assume variable exists - let code fail fast if missing.

    ```python
        def parse_command_parameters(self, args: str) -> Dict[str, Any]:
            params = {}
            if not args:
                return params
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:44): Line 44: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
        @property
        def help(self) -> REPLHelp:
            if self._help is None:
                self._help = REPLHelp(self._bot)
            return self._help
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:50): Line 50: None check guard clause detected. Assume variables are initialized - let code fail fast if None.

    ```python
        @property
        def status(self) -> REPLStatus:
            if self._status is None:
                self._status = REPLStatus(self, self._session, self._session.formatter)
            return self._status
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\formatters\markdown_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/markdown_formatter.py:15): Line 15: Variable truthiness check detected (if is_completed:). Assume variable exists - let code fail fast if missing.

    ```python
        
        def status_marker(self, is_current: bool, is_completed: bool) -> str:
            if is_completed:
                return "- ☑"
            elif is_current:
                return "- ➤"
            else:
                return "- ☐"
        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\formatters\markdown_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/markdown_formatter.py:17): Line 17: Variable truthiness check detected (if is_current:). Assume variable exists - let code fail fast if missing.

    ```python
            if is_completed:
                return "- ☑"
            elif is_current:
                return "- ➤"
            else:
                return "- ☐"
        
    ```

#### <span id="avoid-unnecessary-parameter-passing-violations">Avoid Unnecessary Parameter Passing: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:50): Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:84): Instance property "self._render_specs" is extracted to variable "render_specs" and passed to internal method "_execute_synchronizers". Access via self._render_specs directly instead.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 4 violation(s)</span>

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:449): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_handle_next_command:449-468):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```

  Location (_handle_back_command:485-504):
    ```python
    if not self.has_current_action:
        return REPLCommandResponse(output='ERROR: No current action', response='ERROR: No current action', status='error')
    behavior = self.current_behavior
    if not behavior:...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:46): Duplicate code blocks detected (2 locations) - extract to helper function.

  Location (_prepare_instructions:46-61):
    ```python
    render_instructions = self._config_loader.load_render_instructions()
    render_specs = self._render_specs
    self._execute_synchronizers(render_specs)
    merged_instructions = MergedInstructions(base_instructi...
    ```

  Location (do_execute:82-88):
    ```python
    render_instructions = self._config_loader.load_render_instructions()
    render_specs = self._render_specs
    self._execute_synchronizers(render_specs)
    instructions = MergedInstructions(base_instructions=sel...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:16): Duplicate code detected: functions status_marker, list_item, highlight have identical bodies - extract to shared function

#### <span id="enforce-encapsulation-violations">Enforce Encapsulation: 2 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:669): Method "_handle_scope_command" in Test class [REPLSession](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:669) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:154): Method "_format_rules_with_file_paths" in Test class [ValidateRulesAction](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:154) has Law of Demeter violation (method chain depth 3) - encapsulate access to related objects

#### <span id="keep-classes-small-with-single-responsibility-violations">Keep Classes Small With Single Responsibility: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:16): Class "Behaviors" is 380 lines - should be under 300 lines (extract related methods into separate classes)

```python
logger = logging.getLogger(__name__)

class Behaviors:

    def __init__(self, bot_name: str, bot_paths: BotPaths):
        self.bot_name = bot_name
        self.bot_paths = bot_paths
        self._behaviors: List['Behavior'] = []
        self._discover_behaviors()
        self._current_index: Optional[int] = None
    # ... (truncated)
```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:17): Class "REPLSession" is 1225 lines - should be under 300 lines (extract related methods into separate classes)

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:36): Class "DuplicationScanner" is 1903 lines - should be under 300 lines (extract related methods into separate classes)

```python


class DuplicationScanner(CodeScanner):
    
    SCANNER_VERSION = "1.0"
    
    def _get_cache_dir(self, file_path: Optional[Path] = None) -> Path:
        if file_path:
            current = file_path.parent
            while current and current.parent != current:
    # ... (truncated)
```

#### <span id="keep-functions-small-focused-violations">Keep Functions Small Focused: 7 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:204): Function "navigate_to" is 45 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return self.find_by_name(behavior_name) is not None
    
        def navigate_to(self, behavior_name: str):
            behavior = self.find_by_name(behavior_name)
            if behavior is None:
                raise ValueError(f"Behavior '{behavior_name}' not found")
            
            target_index = None
            for i, b in enumerate(self._behaviors):
                if b.name == behavior.name:
                    target_index = i
                    self._current_index = i
                    break
            
            # When navigating to a behavior: mark all actions in previous behaviors as complete,
            # clear all actions in future behaviors
            if target_index is not None and self.bot_paths:
                workspace_dir = self.bot_paths.workspace_directory
                state_file = workspace_dir / 'behavior_action_state.json'
                
                import json
                if state_file.exists():
                    state_data = json.loads(state_file.read_text(encoding='utf-8'))
                else:
                    state_data = {}
                
                completed_actions = state_data.get('completed_actions', [])
                
                # Mark all actions in previous behaviors as complete
                for i in range(target_index):
                    past_behavior = self._behaviors[i]
                    for action_name in past_behavior.actions.names:
                        action_state = f"{self.bot_name}.{past_behavior.name}.{action_name}"
                        # Check if already completed
                        is_completed = any(a.get('action_state') == action_state for a in completed_actions if isinstance(a, dict))
                        if not is_completed:
                            from datetime import datetime
                            completed_actions.append({
                                'action_state': action_state,
                                'timestamp': datetime.now().isoformat()
                            })
                
                # Remove completed actions from future behaviors
                actions_to_remove = set()
                for i in range(target_index + 1, len(self._behaviors)):
                    future_behavior = self._behaviors[i]
                    for action_name in future_behavior.actions.names:
                        action_state = f"{self.bot_name}.{future_behavior.name}.{action_name}"
                        actions_to_remove.add(action_state)
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 69 lines - should be under 20 lines (extract complex logic to helper functions)

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:108): Function "scan_file" is 63 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
                logger.debug(f"Cache write failed for {file_path}: {e}")
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            _safe_print(f"[DuplicationScanner.scan_code_file] Called for: {file_path}")
            
            if not file_path.exists():
                _safe_print(f"[DuplicationScanner.scan_code_file] File does not exist: {file_path}")
                return violations
            
            # Track time for timeout detection
            file_start_time = datetime.now()
            
            try:
                file_size = file_path.stat().st_size
                if file_size > 500_000:  # Skip files larger than 500KB
                    _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                    return violations
            except Exception as e:
                _safe_print(f"Could not check file size for {file_path}: {e}")
            
            try:
                content = file_path.read_text(encoding='utf-8')
                tree = ast.parse(content, filename=str(file_path))
                lines = content.split('\n')
                
                functions = []
                
                def extract_functions_from_node(node: ast.AST, parent_class: str = None):
                    if isinstance(node, ast.ClassDef):
                        # Found a class - extract its methods
                        for child in node.body:
                            extract_functions_from_node(child, node.name)
                    elif isinstance(node, ast.FunctionDef):
                        # Found a function - extract it with class context
                        func_body = ast.unparse(node.body) if hasattr(ast, 'unparse') else str(node.body)
                        functions.append((node.name, func_body, node.lineno, node, parent_class))
                
                for node in tree.body:
                    extract_functions_from_node(node, None)
                
                func_violations = self._check_duplicate_functions(functions, file_path, rule_obj, lines)
                violations.extend(func_violations)
                
                elapsed = (datetime.now() - file_start_time).total_seconds()
                if elapsed > FILE_SCAN_TIMEOUT:
                    _safe_print(f"TIMEOUT: File scan exceeded {FILE_SCAN_TIMEOUT}s: {file_path} (stopping early)")
                    return violations
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1642): Function "scan_cross_file" is 250 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            _safe_print("")  # Blank line after violations
        
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
            
            # If all_* not provided, fall back to regular behavior
            if all_test_files is None:
                all_test_files = test_files
            if all_code_files is None:
                all_code_files = code_files
            
            # Combine changed files (to scan)
            changed_files = []
            if code_files:
                changed_files.extend(code_files)
            if test_files:
                changed_files.extend(test_files)
            
            # Combine all files (for reference)
            all_files = []
            if all_code_files:
                all_files.extend(all_code_files)
            if all_test_files:
                all_files.extend(all_test_files)
            
            if not changed_files or not all_files:
                return violations
            
            if len(changed_files) < len(all_files):
                _safe_print(f"\n[CROSS-FILE] Incremental scan: Checking {len(changed_files)} changed file(s) against {len(all_files)} total files...")
            else:
                _safe_print(f"\n[CROSS-FILE] Full scan: Scanning {len(all_files)} files for cross-file duplication...")
            import sys
            
            def write_status(msg: str):
                if status_writer and hasattr(status_writer, 'write_cross_file_progress'):
                    try:
                        status_writer.write_cross_file_progress(msg)
                    except Exception as e:
                        logger.debug(f'Could not write to status file: {type(e).__name__}: {e}')
            
            write_status(f"\n## Cross-File Duplication Analysis")
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:784): Function "extract_from_node" has high cyclomatic complexity (18) - should be under 10. Extract decision logic to helper functions.

    ```python
                                 ast.AsyncFor, ast.AsyncWith)
            
            def extract_from_node(node):
                if isinstance(node, control_structures):
                    # Count nodes in this subtree
                    num_nodes = len(list(ast.walk(node)))
                    if min_nodes <= num_nodes <= max_nodes:
                        subtrees.append(node)
                
                if hasattr(node, 'body') and isinstance(node.body, list):
                    for child in node.body:
                        extract_from_node(child)
                
                if hasattr(node, 'orelse') and isinstance(node.orelse, list):
                    for child in node.orelse:
                        extract_from_node(child)
                
                if hasattr(node, 'handlers') and isinstance(node.handlers, list):
                    for handler in node.handlers:
                        if hasattr(handler, 'body') and isinstance(handler.body, list):
                            for child in handler.body:
                                extract_from_node(child)
                
                if hasattr(node, 'finalbody') and isinstance(node.finalbody, list):
                    for child in node.finalbody:
                        extract_from_node(child)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:105): Function "get_last_report_timestamp" is 22 lines - should be under 20 lines (extract complex logic to helper functions)

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:225): Function "formatted_rules_digest" is 24 lines - should be under 20 lines (extract complex logic to helper functions)

    ```python
            return '\n'.join(sections) if sections else 'No validation rules found.'
    
        def formatted_rules_digest(self) -> str:
            rules = self._load_rules()
            if not rules:
                return 'No validation rules found.'
            
            # Sort by priority (lower number = higher priority)
            rules = sorted(rules, key=lambda r: r.priority)
            
            lines = []
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

- <span style="color: blue;">[i]</span> **INFO** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:204): Function "navigate_to" is 57 lines - consider improving vertical density by declaring variables near usage

    ```python
            return self.find_by_name(behavior_name) is not None
    
        def navigate_to(self, behavior_name: str):
            behavior = self.find_by_name(behavior_name)
            if behavior is None:
                raise ValueError(f"Behavior '{behavior_name}' not found")
            
            target_index = None
            for i, b in enumerate(self._behaviors):
                if b.name == behavior.name:
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:144): Function "display_current_state" is 98 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:252): Function "_convert_domain_result_to_repl_response" is 57 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:323): Function "_handle_simple_command" is 55 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:571): Function "_handle_confirm_command" is 54 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:645): Function "_handle_scope_command" is 65 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:821): Function "_handle_dot_notation" is 127 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:949): Function "_handle_action_shortcut" is 60 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1017): Function "_execute_action_with_args" is 65 lines - consider improving vertical density by declaring variables near usage

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
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:108): Function "scan_file" is 78 lines - consider improving vertical density by declaring variables near usage

    ```python
                logger.debug(f"Cache write failed for {file_path}: {e}")
        
        def scan_file(self, file_path: Path, rule_obj: Any = None, knowledge_graph: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
            violations = []
            
            _safe_print(f"[DuplicationScanner.scan_code_file] Called for: {file_path}")
            
            if not file_path.exists():
                _safe_print(f"[DuplicationScanner.scan_code_file] File does not exist: {file_path}")
                return violations
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:335): Function "_check_duplicate_code_blocks" is 292 lines - consider improving vertical density by declaring variables near usage

    ```python
            return False
        
        def _check_duplicate_code_blocks(self, functions: List[tuple], lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            all_blocks = []
            for func_tuple in functions:
                func_name, func_body, func_line, func_node, _ = func_tuple
                blocks = self._extract_code_blocks(func_node, func_line, func_name)
                all_blocks.extend(blocks)
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:628): Function "_extract_code_blocks" is 148 lines - consider improving vertical density by declaring variables near usage

    ```python
            return violations
        
        def _extract_code_blocks(self, func_node: ast.FunctionDef, func_start_line: int, func_name: str) -> List[Dict[str, Any]]:
            blocks = []
            MIN_NODES = 5  # Minimum AST nodes for a meaningful subtree
            MAX_NODES = 80  # Maximum nodes to avoid overly large blocks
            MIN_LINES = 5  # Minimum lines of code
            MAX_LINES = 20  # Maximum lines (goldilocks zone)
            
            # Skip blocks in test methods - test structure similarity is expected, not duplication
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1584): Function "_log_violation_details" is 57 lines - consider improving vertical density by declaring variables near usage

    ```python
                return 0.7
        
        def _log_violation_details(self, file_path: Path, violations: List[Dict[str, Any]], lines: List[str]) -> None:
            if not violations:
                return
            
            # Log detailed violation information
            # Note: This can be verbose, but provides valuable debugging info
            
            _safe_print(f"\n[{file_path}] Found {len(violations)} duplication violation(s):")
        # ... (truncated)
    ```
- <span style="color: blue;">[i]</span> **INFO** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1642): Function "scan_cross_file" is 297 lines - consider improving vertical density by declaring variables near usage

    ```python
            _safe_print("")  # Blank line after violations
        
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

#### <span id="never-swallow-exceptions-violations">Never Swallow Exceptions: 2 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:818): Except block only contains pass at line 818 - exceptions must be logged or rethrown, never swallowed

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

#### <span id="provide-meaningful-context-violations">Provide Meaningful Context: 76 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:17): Line 17 contains magic number - replace with named constant

    ```python
    # Timeout for individual file scans (seconds)
    FILE_SCAN_TIMEOUT = 60  # 60 seconds per file max
    
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:123): Line 123 contains magic number - replace with named constant

    ```python
                if file_size > 500_000:  # Skip files larger than 500KB
                    _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                    return violations
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:408): Line 408 contains magic number - replace with named constant

    ```python
                        max_similarity = max(ast_similarity, content_similarity)
                    elif max(ast_similarity, content_similarity) >= 0.90 and min(ast_similarity, content_similarity) >= 0.60:
                        max_similarity = max(ast_similarity, content_similarity)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:604): Line 604 contains magic number - replace with named constant

    ```python
                    location = f"{block['func_name']}:{block['start_line']}-{block['end_line']}"
                    preview = block['preview'][:200] + '...' if len(block['preview']) > 200 else block['preview']
                    previews.append(f"Location ({location}):\n```python\n{preview}\n```")
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:942): Line 942 contains magic number - replace with named constant

    ```python
            
            # If >= 60% are helper calls, consider it mostly helpers
            return (helper_count / total_count) >= 0.6
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1709): Line 1709 contains magic number - replace with named constant

    ```python
                    if file_size > 500_000:  # Skip files larger than 500KB
                        _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                        continue
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1778): Line 1778 contains magic number - replace with named constant

    ```python
                    if file_size > 500_000:  # Skip files larger than 500KB
                        _safe_print(f"Skipping large file ({file_size/1024:.1f}KB): {file_path}")
                        continue
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1229): Line 1229 uses numbered variable "block1" - use meaningful descriptive name

    ```python
        
        def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
            domain_patterns1 = self._extract_domain_entities(block1)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1229): Line 1229 uses numbered variable "block2" - use meaningful descriptive name

    ```python
        
        def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
            domain_patterns1 = self._extract_domain_entities(block1)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1362): Line 1362 uses numbered variable "block1" - use meaningful descriptive name

    ```python
        
        def _compare_ast_blocks(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
            if len(block1) == 0 and len(block2) == 0:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1362): Line 1362 uses numbered variable "block2" - use meaningful descriptive name

    ```python
        
        def _compare_ast_blocks(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
            if len(block1) == 0 and len(block2) == 0:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1380): Line 1380 uses numbered variable "block1" - use meaningful descriptive name

    ```python
        
        def _compare_ast_structures(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
            if not block1 or not block2:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1380): Line 1380 uses numbered variable "block2" - use meaningful descriptive name

    ```python
        
        def _compare_ast_structures(self, block1: List[ast.stmt], block2: List[ast.stmt]) -> float:
            if not block1 or not block2:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1435): Line 1435 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
            if type(node1) != type(node2):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1435): Line 1435 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
            if type(node1) != type(node2):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1469): Line 1469 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_assign_nodes(self, node1: ast.Assign, node2: ast.Assign) -> float:
            # Compare number of targets
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1469): Line 1469 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_assign_nodes(self, node1: ast.Assign, node2: ast.Assign) -> float:
            # Compare number of targets
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1478): Line 1478 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_augassign_nodes(self, node1: ast.AugAssign, node2: ast.AugAssign) -> float:
            if type(node1.op) != type(node2.op):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1478): Line 1478 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_augassign_nodes(self, node1: ast.AugAssign, node2: ast.AugAssign) -> float:
            if type(node1.op) != type(node2.op):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1483): Line 1483 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
            arg_count1 = len(node1.args) + len(node1.keywords)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1483): Line 1483 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
            arg_count1 = len(node1.args) + len(node1.keywords)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1501): Line 1501 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_assert_nodes(self, node1: ast.Assert, node2: ast.Assert) -> float:
            test_sim = self._compare_expr_structure(node1.test, node2.test)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1501): Line 1501 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_assert_nodes(self, node1: ast.Assert, node2: ast.Assert) -> float:
            test_sim = self._compare_expr_structure(node1.test, node2.test)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1505): Line 1505 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_return_nodes(self, node1: ast.Return, node2: ast.Return) -> float:
            if node1.value is None and node2.value is None:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1505): Line 1505 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_return_nodes(self, node1: ast.Return, node2: ast.Return) -> float:
            if node1.value is None and node2.value is None:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1512): Line 1512 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_if_nodes(self, node1: ast.If, node2: ast.If) -> float:
            test_sim = self._compare_expr_structure(node1.test, node2.test)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1512): Line 1512 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_if_nodes(self, node1: ast.If, node2: ast.If) -> float:
            test_sim = self._compare_expr_structure(node1.test, node2.test)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1518): Line 1518 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_for_nodes(self, node1: ast.For, node2: ast.For) -> float:
            body_sim = self._compare_ast_structures(node1.body, node2.body)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1518): Line 1518 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_for_nodes(self, node1: ast.For, node2: ast.For) -> float:
            body_sim = self._compare_ast_structures(node1.body, node2.body)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1523): Line 1523 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_while_nodes(self, node1: ast.While, node2: ast.While) -> float:
            test_sim = self._compare_expr_structure(node1.test, node2.test)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1523): Line 1523 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_while_nodes(self, node1: ast.While, node2: ast.While) -> float:
            test_sim = self._compare_expr_structure(node1.test, node2.test)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1528): Line 1528 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_with_nodes(self, node1: ast.With, node2: ast.With) -> float:
            if len(node1.items) != len(node2.items):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1528): Line 1528 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_with_nodes(self, node1: ast.With, node2: ast.With) -> float:
            if len(node1.items) != len(node2.items):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1534): Line 1534 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_try_nodes(self, node1: ast.Try, node2: ast.Try) -> float:
            body_sim = self._compare_ast_structures(node1.body, node2.body)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1534): Line 1534 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_try_nodes(self, node1: ast.Try, node2: ast.Try) -> float:
            body_sim = self._compare_ast_structures(node1.body, node2.body)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1541): Line 1541 uses numbered variable "node1" - use meaningful descriptive name

    ```python
        
        def _compare_raise_nodes(self, node1: ast.Raise, node2: ast.Raise) -> float:
            if node1.exc is None and node2.exc is None:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1541): Line 1541 uses numbered variable "node2" - use meaningful descriptive name

    ```python
        
        def _compare_raise_nodes(self, node1: ast.Raise, node2: ast.Raise) -> float:
            if node1.exc is None and node2.exc is None:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1548): Line 1548 uses numbered variable "expr1" - use meaningful descriptive name

    ```python
        
        def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
            if type(expr1) != type(expr2):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1548): Line 1548 uses numbered variable "expr2" - use meaningful descriptive name

    ```python
        
        def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
            if type(expr1) != type(expr2):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:359): Line 359 uses numbered variable "block1" - use meaningful descriptive name

    ```python
            compared_pairs = set()
            for i, block1 in enumerate(all_blocks):
                for j, block2 in enumerate(all_blocks[i+1:], start=i+1):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1230): Line 1230 uses numbered variable "domain_patterns1" - use meaningful descriptive name

    ```python
        def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
            domain_patterns1 = self._extract_domain_entities(block1)
            domain_patterns2 = self._extract_domain_entities(block2)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1231): Line 1231 uses numbered variable "domain_patterns2" - use meaningful descriptive name

    ```python
            domain_patterns1 = self._extract_domain_entities(block1)
            domain_patterns2 = self._extract_domain_entities(block2)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1254): Line 1254 uses numbered variable "calls1" - use meaningful descriptive name

    ```python
        def _calls_different_methods(self, block1_nodes: List[ast.stmt], block2_nodes: List[ast.stmt]) -> bool:
            calls1 = self._extract_method_calls(block1_nodes)
            calls2 = self._extract_method_calls(block2_nodes)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1255): Line 1255 uses numbered variable "calls2" - use meaningful descriptive name

    ```python
            calls1 = self._extract_method_calls(block1_nodes)
            calls2 = self._extract_method_calls(block2_nodes)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1374): Line 1374 uses numbered variable "node1" - use meaningful descriptive name

    ```python
            similarities = []
            for node1, node2 in zip(block1, block2):
                similarity = self._compare_ast_nodes_deep(node1, node2)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1374): Line 1374 uses numbered variable "node2" - use meaningful descriptive name

    ```python
            similarities = []
            for node1, node2 in zip(block1, block2):
                similarity = self._compare_ast_nodes_deep(node1, node2)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1385): Line 1385 uses numbered variable "node1" - use meaningful descriptive name

    ```python
            similarities = []
            for node1 in block1:
                best_match = 0.0
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1484): Line 1484 uses numbered variable "arg_count1" - use meaningful descriptive name

    ```python
        def _compare_call_nodes(self, node1: ast.Call, node2: ast.Call) -> float:
            arg_count1 = len(node1.args) + len(node1.keywords)
            arg_count2 = len(node2.args) + len(node2.keywords)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1485): Line 1485 uses numbered variable "arg_count2" - use meaningful descriptive name

    ```python
            arg_count1 = len(node1.args) + len(node1.keywords)
            arg_count2 = len(node2.args) + len(node2.keywords)
            
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1494): Line 1494 uses numbered variable "a1" - use meaningful descriptive name

    ```python
            arg_sims = []
            for a1, a2 in zip(node1.args, node2.args):
                arg_sims.append(self._compare_expr_structure(a1, a2))
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1494): Line 1494 uses numbered variable "a2" - use meaningful descriptive name

    ```python
            arg_sims = []
            for a1, a2 in zip(node1.args, node2.args):
                arg_sims.append(self._compare_expr_structure(a1, a2))
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1840): Line 1840 uses numbered variable "block1" - use meaningful descriptive name

    ```python
            # Compare each changed block against all blocks
            for i, block1 in enumerate(changed_blocks):
                for j, block2 in enumerate(all_blocks):
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:360): Line 360 uses numbered variable "block2" - use meaningful descriptive name

    ```python
            for i, block1 in enumerate(all_blocks):
                for j, block2 in enumerate(all_blocks[i+1:], start=i+1):
                    # Skip if same block
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1263): Line 1263 uses numbered variable "method_names1" - use meaningful descriptive name

    ```python
            if len(calls1) == len(calls2) and len(calls1) >= 2:
                method_names1 = {call for call in calls1}
                method_names2 = {call for call in calls2}
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1264): Line 1264 uses numbered variable "method_names2" - use meaningful descriptive name

    ```python
                method_names1 = {call for call in calls1}
                method_names2 = {call for call in calls2}
                
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1387): Line 1387 uses numbered variable "node2" - use meaningful descriptive name

    ```python
                best_match = 0.0
                for node2 in block2:
                    similarity = self._compare_ast_nodes_deep(node1, node2)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1841): Line 1841 uses numbered variable "block2" - use meaningful descriptive name

    ```python
            for i, block1 in enumerate(changed_blocks):
                for j, block2 in enumerate(all_blocks):
                    # Skip if same file (within-file duplication already checked in scan_file)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1238): Line 1238 uses numbered variable "func1" - use meaningful descriptive name

    ```python
                    # If so, this is likely legitimate - each domain needs its own handlers
                    func1 = block1['func_name']
                    func2 = block2['func_name']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1239): Line 1239 uses numbered variable "func2" - use meaningful descriptive name

    ```python
                    func1 = block1['func_name']
                    func2 = block2['func_name']
                    if abs(len(func1) - len(func2)) <= 3:  # Similar length names
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:519): Line 519 uses numbered variable "block1" - use meaningful descriptive name

    ```python
                        overlaps = False
                        for block1 in group_blocks:
                            for block2 in other_blocks:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1893): Line 1893 uses numbered variable "file1" - use meaningful descriptive name

    ```python
                        # Found duplicate across files
                        file1 = block1['file_path']
                        file2 = block2['file_path']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1894): Line 1894 uses numbered variable "file2" - use meaningful descriptive name

    ```python
                        file1 = block1['file_path']
                        file2 = block2['file_path']
                        func1 = block1['func_name']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1895): Line 1895 uses numbered variable "func1" - use meaningful descriptive name

    ```python
                        file2 = block2['file_path']
                        func1 = block1['func_name']
                        func2 = block2['func_name']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1896): Line 1896 uses numbered variable "func2" - use meaningful descriptive name

    ```python
                        func1 = block1['func_name']
                        func2 = block2['func_name']
                        start1 = block1['start_line']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1897): Line 1897 uses numbered variable "start1" - use meaningful descriptive name

    ```python
                        func2 = block2['func_name']
                        start1 = block1['start_line']
                        end1 = block1['end_line']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1898): Line 1898 uses numbered variable "end1" - use meaningful descriptive name

    ```python
                        start1 = block1['start_line']
                        end1 = block1['end_line']
                        start2 = block2['start_line']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1899): Line 1899 uses numbered variable "start2" - use meaningful descriptive name

    ```python
                        end1 = block1['end_line']
                        start2 = block2['start_line']
                        end2 = block2['end_line']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1900): Line 1900 uses numbered variable "end2" - use meaningful descriptive name

    ```python
                        start2 = block2['start_line']
                        end2 = block2['end_line']
                        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1902): Line 1902 uses numbered variable "preview1" - use meaningful descriptive name

    ```python
                        
                        preview1 = block1['preview']
                        preview2 = block2['preview']
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1903): Line 1903 uses numbered variable "preview2" - use meaningful descriptive name

    ```python
                        preview1 = block1['preview']
                        preview2 = block2['preview']
                        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1911): Line 1911 uses numbered variable "location1" - use meaningful descriptive name

    ```python
                        
                        location1 = f"{file1.name}:{func1} (lines {start1}-{end1})"
                        location2 = f"{file2.name}:{func2} (lines {start2}-{end2})"
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1912): Line 1912 uses numbered variable "location2" - use meaningful descriptive name

    ```python
                        location1 = f"{file1.name}:{func1} (lines {start1}-{end1})"
                        location2 = f"{file2.name}:{func2} (lines {start2}-{end2})"
                        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:520): Line 520 uses numbered variable "block2" - use meaningful descriptive name

    ```python
                        for block1 in group_blocks:
                            for block2 in other_blocks:
                                if (block1['func_name'] == block2['func_name'] and
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1907): Line 1907 uses numbered variable "preview1" - use meaningful descriptive name

    ```python
                        if len(preview1) > 300:
                            preview1 = preview1[:300] + '...'
                        if len(preview2) > 300:
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1909): Line 1909 uses numbered variable "preview2" - use meaningful descriptive name

    ```python
                        if len(preview2) > 300:
                            preview2 = preview2[:300] + '...'
                        
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\formatters\markdown_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/markdown_formatter.py:12): Line 12 contains magic number - replace with named constant

    ```python
            """Light line for subsection breaks"""
            return "─" * 60
        
    ```

#### <span id="refactor-completely-not-partially-violations">Refactor Completely Not Partially: 3 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:72): Fallback/legacy support code found (comment at line 72, code at line 73) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1152): Fallback/legacy support code found (comment at line 1152, code at line 1153) - complete refactoring by removing old pattern support
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\validate\validate_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validate_action.py:104): Fallback/legacy support code found (comment at line 104, code at line 105) - complete refactoring by removing old pattern support

#### <span id="simplify-control-flow-violations">Simplify Control Flow: 33 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:204): Function "navigate_to" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return self.find_by_name(behavior_name) is not None
    
        def navigate_to(self, behavior_name: str):
            behavior = self.find_by_name(behavior_name)
            if behavior is None:
                raise ValueError(f"Behavior '{behavior_name}' not found")
            
            target_index = None
            for i, b in enumerate(self._behaviors):
                if b.name == behavior.name:
                    target_index = i
                    self._current_index = i
                    break
            
            # When navigating to a behavior: mark all actions in previous behaviors as complete,
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:418): Function "_handle_current_command" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:645): Function "_handle_scope_command" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:821): Function "_handle_dot_notation" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

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
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:263): Function "_is_simple_delegation" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _is_simple_delegation(self, func_node: ast.FunctionDef) -> bool:
            if self._is_simple_property_getter(func_node):
                return True
            
            # Check if it's a simple method that just returns self.attr.method() or self.attr[item]
            executable_body = [stmt for stmt in func_node.body if not self._is_docstring_or_comment(stmt, func_node)]
            if len(executable_body) == 1:
                stmt = executable_body[0]
                if isinstance(stmt, ast.Return) and stmt.value:
                    if isinstance(stmt.value, (ast.Call, ast.Subscript)):
                        # Method call or subscript - check if it's on self.attribute
                        if isinstance(stmt.value, ast.Call):
                            if isinstance(stmt.value.func, ast.Attribute):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:296): Function "_is_simple_property_getter" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _is_simple_property_getter(self, func_node: ast.FunctionDef) -> bool:
            is_property = False
            for decorator in func_node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == 'property':
                    is_property = True
                    break
                elif isinstance(decorator, ast.Attribute):
                    if decorator.attr in ('setter', 'deleter'):
                        # Setter/deleter, check if it's simple
                        pass
                    elif hasattr(decorator, 'value') and isinstance(decorator.value, ast.Name):
                        if decorator.value.id == 'property':
                            is_property = True
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:335): Function "_check_duplicate_code_blocks" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _check_duplicate_code_blocks(self, functions: List[tuple], lines: List[str], file_path: Path, rule_obj: Any) -> List[Dict[str, Any]]:
            violations = []
            
            all_blocks = []
            for func_tuple in functions:
                func_name, func_body, func_line, func_node, _ = func_tuple
                blocks = self._extract_code_blocks(func_node, func_line, func_name)
                all_blocks.extend(blocks)
            
            # Use similarity checking to find duplicate blocks
            SIMILARITY_THRESHOLD = 0.90  # Increased to 90% to reduce false positives
            
            # Debug: track comparison attempts
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:777): Function "_extract_subtrees_from_function" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return blocks
        
        def _extract_subtrees_from_function(self, func_node: ast.FunctionDef, min_nodes: int, max_nodes: int) -> List[ast.AST]:
            subtrees = []
            
            # Control structures that represent semantic units
            control_structures = (ast.If, ast.For, ast.While, ast.Try, ast.With, 
                                 ast.AsyncFor, ast.AsyncWith)
            
            def extract_from_node(node):
                if isinstance(node, control_structures):
                    # Count nodes in this subtree
                    num_nodes = len(list(ast.walk(node)))
                    if min_nodes <= num_nodes <= max_nodes:
                        subtrees.append(node)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:831): Function "_get_statement_end_line" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _get_statement_end_line(self, stmt: ast.stmt) -> int:
            if hasattr(stmt, 'end_lineno') and stmt.end_lineno:
                return stmt.end_lineno
            
            # For control structures, find the end of their body
            if isinstance(stmt, ast.If):
                end_line = stmt.lineno
                if stmt.body:
                    end_line = max(end_line, self._get_body_end_line(stmt.body))
                if stmt.orelse:
                    end_line = max(end_line, self._get_body_end_line(stmt.orelse))
                return end_line
            elif isinstance(stmt, (ast.For, ast.While, ast.AsyncFor)):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:896): Function "_is_mostly_helper_calls" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _is_mostly_helper_calls(self, statements: List[ast.stmt]) -> bool:
            if not statements:
                return False
            
            helper_count = 0
            total_count = 0
            
            for stmt in statements:
                if self._is_docstring_or_comment(stmt):
                    continue
                
                total_count += 1
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:945): Function "_is_only_helper_calls" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return (helper_count / total_count) >= 0.6
        
        def _is_only_helper_calls(self, statements: List[ast.stmt]) -> bool:
            helper_patterns = [
                'given_', 'when_', 'then_',
                'create_', 'build_', 'make_', 'generate_',
                'verify_', 'assert_', 'check_', 'ensure_',
                'setup_', 'bootstrap_', 'initialize_',
                'get_', 'load_', 'fetch_'
            ]
            
            for stmt in statements:
                if isinstance(stmt, ast.Assign):
                    if isinstance(stmt.value, ast.Call):
                        func_name = self._get_function_name(stmt.value.func)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1023): Function "_count_actual_code_statements" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _count_actual_code_statements(self, statements: List[ast.stmt]) -> int:
            count = 0
            for stmt in statements:
                if self._is_docstring_or_comment(stmt):
                    continue
                
                if isinstance(stmt, ast.Pass):
                    continue
                
                # Count simple executable statements
                if isinstance(stmt, (ast.Assign, ast.AnnAssign, ast.AugAssign, 
                                     ast.Expr, ast.Return, ast.Raise, ast.Assert,
                                     ast.Delete, ast.Import, ast.ImportFrom,
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1077): Function "_is_test_pattern" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return (assertion_count / total_count) >= 0.6
        
        def _is_test_pattern(self, statements: List[ast.stmt]) -> bool:
            if not statements:
                return False
            
            # Count helper calls and assertions
            helper_count = 0
            assertion_count = 0
            other_count = 0
            
            for stmt in statements:
                if self._is_docstring_or_comment(stmt):
                    continue
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1115): Function "_is_list_building_pattern" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return test_pattern_ratio >= 0.75 and other_count <= 1
        
        def _is_list_building_pattern(self, statements: List[ast.stmt]) -> bool:
            if not statements:
                return False
            
            list_building_count = 0
            total_count = 0
            
            for stmt in statements:
                if self._is_docstring_or_comment(stmt):
                    continue
                
                total_count += 1
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1145): Function "_is_simple_property" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return (list_building_count / total_count) >= 0.75
        
        def _is_simple_property(self, func_node: ast.FunctionDef) -> bool:
            if not func_node.decorator_list:
                return False
            
            has_property_decorator = False
            for decorator in func_node.decorator_list:
                if isinstance(decorator, ast.Name) and decorator.id == 'property':
                    has_property_decorator = True
                    break
                elif isinstance(decorator, ast.Attribute):
                    if decorator.attr in ('setter', 'deleter'):
                        has_property_decorator = True
                        break
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1172): Function "_is_simple_constructor" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _is_simple_constructor(self, func_node: ast.FunctionDef) -> bool:
            if func_node.name != '__init__':
                return False
            
            # Count statements that are just assignments to self
            executable_body = [stmt for stmt in func_node.body if not self._is_docstring_or_comment(stmt, func_node)]
            
            self_assignments = 0
            other_statements = 0
            
            for stmt in executable_body:
                if isinstance(stmt, (ast.Assign, ast.AnnAssign)):
                    if isinstance(stmt, ast.Assign):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1229): Function "_operates_on_different_domains" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return entities
        
        def _operates_on_different_domains(self, block1: Dict[str, Any], block2: Dict[str, Any]) -> bool:
            domain_patterns1 = self._extract_domain_entities(block1)
            domain_patterns2 = self._extract_domain_entities(block2)
            
            # If they have different domain entities and function names are similar,
            # they're likely legitimate separate implementations
            if domain_patterns1 and domain_patterns2:
                if domain_patterns1 != domain_patterns2:
                    # If so, this is likely legitimate - each domain needs its own handlers
                    func1 = block1['func_name']
                    func2 = block2['func_name']
                    if abs(len(func1) - len(func2)) <= 3:  # Similar length names
                        # Extract common prefixes (CRUD operations: create, read, update, delete, get, set)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1253): Function "_calls_different_methods" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _calls_different_methods(self, block1_nodes: List[ast.stmt], block2_nodes: List[ast.stmt]) -> bool:
            calls1 = self._extract_method_calls(block1_nodes)
            calls2 = self._extract_method_calls(block2_nodes)
            
            if not calls1 or not calls2:
                return False
            
            # If blocks have same number of calls but different method names, they're likely
            # structural patterns calling different methods (not duplication)
            if len(calls1) == len(calls2) and len(calls1) >= 2:
                method_names1 = {call for call in calls1}
                method_names2 = {call for call in calls2}
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1279): Function "_extract_method_calls" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _extract_method_calls(self, nodes: List[ast.stmt]) -> List[str]:
            method_calls = []
            
            for node in nodes:
                if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                    call = node.value
                    if isinstance(call.func, ast.Attribute):
                        # Method call: obj.method()
                        method_calls.append(call.func.attr)
                    elif isinstance(call.func, ast.Name):
                        # Function call: func()
                        method_calls.append(call.func.id)
                elif isinstance(node, ast.Assign):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1304): Function "_normalize_block" has nesting depth of 7 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return False
        
        def _normalize_block(self, statements: List[ast.stmt]) -> Optional[str]:
            try:
                normalized_parts = []
                for stmt in statements:
                    stmt_type = type(stmt).__name__
                    
                    # Skip docstrings and comments
                    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant):
                        if isinstance(stmt.value.value, str) and stmt.value.value.strip().startswith('"""'):
                            continue
                    
                    # Normalize assignment: var = value -> ASSIGN
                    if isinstance(stmt, ast.Assign):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1345): Function "_get_block_preview" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return None
        
        def _get_block_preview(self, statements: List[ast.stmt]) -> str:
            try:
                if hasattr(ast, 'unparse'):
                    preview_lines = []
                    for stmt in statements:
                        # Skip docstrings when generating preview
                        if self._is_docstring_or_comment(stmt):
                            continue
                        preview_lines.append(ast.unparse(stmt))
                    return "\n".join(preview_lines)
                else:
                    return str(statements)
            except Exception as e:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1407): Function "_get_node_signature" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return "|".join(signatures)
        
        def _get_node_signature(self, node: ast.AST) -> str:
            node_type = type(node).__name__
            
            if isinstance(node, ast.Assign):
                return f"ASSIGN({len(node.targets)}_targets)"
            elif isinstance(node, ast.AugAssign):
                return f"AUGASSIGN({type(node.op).__name__})"
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                return "CALL"
            elif isinstance(node, ast.Assert):
                return "ASSERT"
            elif isinstance(node, ast.Return):
                return "RETURN"
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1435): Function "_compare_ast_nodes_deep" has nesting depth of 11 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return node_type
        
        def _compare_ast_nodes_deep(self, node1: ast.AST, node2: ast.AST) -> float:
            if type(node1) != type(node2):
                return 0.0
            
            # Compare based on node type
            if isinstance(node1, ast.Assign):
                return self._compare_assign_nodes(node1, node2)
            elif isinstance(node1, ast.AugAssign):
                return self._compare_augassign_nodes(node1, node2)
            elif isinstance(node1, ast.Expr) and isinstance(node1.value, ast.Call):
                # Both are Expr nodes with Call values
                if isinstance(node2, ast.Expr) and isinstance(node2.value, ast.Call):
                    return self._compare_call_nodes(node1.value, node2.value)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1548): Function "_compare_expr_structure" has nesting depth of 8 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return 0.7 + 0.3 * self._compare_expr_structure(node1.exc, node2.exc)
        
        def _compare_expr_structure(self, expr1: ast.expr, expr2: ast.expr) -> float:
            if type(expr1) != type(expr2):
                return 0.0
            
            if isinstance(expr1, ast.Call):
                return self._compare_call_nodes(expr1, expr2)
            elif isinstance(expr1, ast.Attribute):
                # Compare attribute access structure (ignore attribute name)
                return 0.8 + 0.2 * self._compare_expr_structure(expr1.value, expr2.value)
            elif isinstance(expr1, ast.Name):
                # Names are different but structure is same
                return 0.9
            elif isinstance(expr1, ast.Constant):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1584): Function "_log_violation_details" has nesting depth of 6 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                return 0.7
        
        def _log_violation_details(self, file_path: Path, violations: List[Dict[str, Any]], lines: List[str]) -> None:
            if not violations:
                return
            
            # Log detailed violation information
            # Note: This can be verbose, but provides valuable debugging info
            
            _safe_print(f"\n[{file_path}] Found {len(violations)} duplication violation(s):")
            
            for idx, violation in enumerate(violations, 1):
                line_num = violation.get('line_number', '?')
                msg = violation.get('violation_message', '')
                
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1642): Function "scan_cross_file" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            _safe_print("")  # Blank line after violations
        
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
            
            # If all_* not provided, fall back to regular behavior
            if all_test_files is None:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:784): Function "extract_from_node" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
                                 ast.AsyncFor, ast.AsyncWith)
            
            def extract_from_node(node):
                if isinstance(node, control_structures):
                    # Count nodes in this subtree
                    num_nodes = len(list(ast.walk(node)))
                    if min_nodes <= num_nodes <= max_nodes:
                        subtrees.append(node)
                
                if hasattr(node, 'body') and isinstance(node.body, list):
                    for child in node.body:
                        extract_from_node(child)
                
                if hasattr(node, 'orelse') and isinstance(node.orelse, list):
                    for child in node.orelse:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:31): Function "_add_spec_instructions" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return working_dir
    
        def _add_spec_instructions(self, base_instructions_list: List[str], executed_specs: List['RenderSpec'], template_specs: List['RenderSpec']) -> None:
            if executed_specs:
                # Find the end of context sources section (after the blank line following context sources)
                # Context sources typically look like:
                # [0]: "**Look for context in the following locations:**"
                # [1]: "- in this message and chat history"
                # [2]: "- in `{workspace}/docs/context/`"
                # [3]: "- generated files in `{workspace}/docs/stories/`"
                # [4]: "  clarification.json, planning.json"
                # [5]: ""  <- blank line
                # We want to insert AFTER this blank line
                insert_position = 1  # Default to position 1 if we can't find the pattern
                for i, line in enumerate(base_instructions_list):
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:149): Function "_process_for_each_loops" has nesting depth of 4 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            parts.append('')
        
        def _process_for_each_loops(self, instructions_list: List[str], render_specs: List['RenderSpec']) -> List[str]:
            """Process {{#for_each_render_config}}...{{/for_each_render_config}} loops."""
            new_instructions = []
            i = 0
            while i < len(instructions_list):
                line = instructions_list[i]
                
                if '{{#for_each_render_config}}' in line:
                    # Find the end of the loop
                    loop_start = i + 1
                    loop_end = None
                    for j in range(loop_start, len(instructions_list)):
                        if '{{/for_each_render_config}}' in instructions_list[j]:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:187): Function "_expand_template_for_spec" has nesting depth of 5 - use guard clauses and extract nested blocks to reduce nesting

    ```python
            return new_instructions
        
        def _expand_template_for_spec(self, template_lines: List[str], spec: 'RenderSpec') -> List[str]:
            """Expand template lines with render_config placeholders replaced."""
            # Handle instructions - can be string or list
            instructions = spec.config_data.get('instructions', 'No instructions provided')
            if isinstance(instructions, list):
                instructions = '\n'.join(instructions)
            
            replacements = {
                '{render_config.name}': spec.name,
                '{render_config.instructions}': instructions,
                '{render_config.synchronizer}': spec.synchronizer.synchronizer_class_path if spec.synchronizer else 'N/A',
                '{render_config.template}': spec.config_data.get('template', 'N/A'),
                '{render_config.input}': spec.input or 'N/A',
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

#### <span id="stop-writing-useless-comments-violations">Stop Writing Useless Comments: 66 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:66): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @property
        def completed_behaviors(self) -> List[str]:
            """Get list of completed behavior names."""
            completed = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:104): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def next(self) -> Optional['Behavior']:
            """Get the next behavior without changing current state."""
            next_index = self._current_index + 1
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:111): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def previous(self) -> Optional['Behavior']:
            """Get the previous behavior without changing current state."""
            if self._current_index is None or self._current_index <= 0:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:120): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def advance(self) -> Dict[str, Any]:
            """Advance to the next action in the current behavior, or next behavior if at end.
            
            Returns:
                Dict with status and information about the advancement
            """
            if not self.current:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\bot\behaviors.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/bot/behaviors.py:159): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def go_back(self) -> Dict[str, Any]:
            """Go back to the previous action in the current behavior, or previous behavior if at start.
            
            Returns:
                Dict with status and information about going back
            """
            if not self.current:
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:244): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def get_context_header_for_ai(self) -> str:
            """Get status display as a string for AI context headers.
            
            This is a convenience method that extracts just the output string
            from display_current_state().
            """
            state_display = self.display_current_state()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:253): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:380): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_help_command(self, args: str = "") -> REPLCommandResponse:
            """Handle help command using bot.help"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:410): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_status_command(self) -> REPLCommandResponse:
            """Handle status command using bot.status"""
            state_display = self.display_current_state(full=True)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:419): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_current_command(self) -> REPLCommandResponse:
            """Re-execute current operation based on progress state"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:448): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_next_command(self) -> REPLCommandResponse:
            """Handle next/advance navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:484): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_back_command(self) -> REPLCommandResponse:
            """Handle back/previous navigation"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:530): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_instructions_command(self, args: str = "") -> REPLCommandResponse:
            """Handle instructions command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:551): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_submit_command(self, args: str = "") -> REPLCommandResponse:
            """Handle submit command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:572): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_confirm_command(self) -> REPLCommandResponse:
            """Handle confirm command"""
            if not self.has_current_action:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:627): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_path_command(self, args: str = "") -> REPLCommandResponse:
            """Handle path/workspace command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:646): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_scope_command(self, args: str = "") -> REPLCommandResponse:
            """Handle scope command"""
            if not args:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:712): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _handle_behavior_command(self, behavior_name: str) -> REPLCommandResponse:
            """Handle behavior navigation"""
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:741): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def navigate_to_behavior_action(self, behavior_name: str, action_name: str):
            """Navigate to a specific behavior and action
            
            Raises:
                ValueError: If behavior or action not found
            """
            # Navigate to behavior
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:762): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_navigation_with_instructions(self) -> REPLCommandResponse:
            """After navigation, auto-execute instructions for new position"""
            return self._handle_instructions_command()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:766): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _wrap_with_context_header(self, content: str, response_msg: str) -> REPLCommandResponse:
            """Wrap content with instructions header and CLI status section"""
            formatter = self.formatter
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:807): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _mark_behavior_complete(self, behavior_name: str) -> None:
            """Mark a behavior as complete in the state file"""
            state_file = self.workspace_directory / 'behavior_action_state.json'
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:822): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:701): Useless comment: "# Get the scope display lines" - delete it or improve the code instead

    ```python
            result = self.cli_bot.set_scope(scope)
            
            # Get the scope display lines
            output = self.cli_bot.get_scope_display()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:748): Useless comment: "# Get the behavior" - delete it or improve the code instead

    ```python
            # Navigate to behavior
            self.cli_bot.behaviors.domain_behaviors.navigate_to(behavior_name)
            # Get the behavior
            behavior = self.cli_bot.behaviors.domain_behaviors.find_by_name(behavior_name)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
    
        def _execute_synchronizers(self, render_specs: List['RenderSpec']) -> None:
            """Execute synchronizers for all render specs."""
            for spec in render_specs:
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _prepare_instructions(self, instructions, context: ScopeActionContext):
            """Prepare render instructions with render specs and templates."""
            render_instructions = self._config_loader.load_render_instructions()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:74): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _do_submit(self, context: ScopeActionContext) -> Dict[str, Any]:
            """Render actions execute synchronizers during preparation - nothing to submit."""
            return {
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:81): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def do_execute(self, context: ScopeActionContext) -> Dict[str, Any]:
            """Legacy method for backwards compatibility."""
            render_instructions = self._config_loader.load_render_instructions()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:49): Useless comment: "# Execute synchronizers during preparation" - delete it or improve the code instead

    ```python
            render_specs = self._render_specs
            
            # Execute synchronizers during preparation
            self._execute_synchronizers(render_specs)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_action.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_action.py:63): Useless comment: "# Update instructions with properly formatted data from merg" - delete it or improve the code instead

    ```python
            template_specs = [spec for spec in render_specs if spec.requires_ai_handling and (not spec.is_executed)]
            
            # Update instructions with properly formatted data from merged_instructions dict
            instructions._data['base_instructions'] = merged_instructions.get('base_instructions', [])
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:150): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _process_for_each_loops(self, instructions_list: List[str], render_specs: List['RenderSpec']) -> List[str]:
            """Process {{#for_each_render_config}}...{{/for_each_render_config}} loops."""
            new_instructions = []
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:188): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def _expand_template_for_spec(self, template_lines: List[str], spec: 'RenderSpec') -> List[str]:
            """Expand template lines with render_config placeholders replaced."""
            # Handle instructions - can be string or list
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:19): Useless comment: "# Process action_config.json placeholders with ALL render_sp" - delete it or improve the code instead

    ```python
            
            self._add_spec_instructions(base_instructions_list, executed_specs, template_specs)
            # Process action_config.json placeholders with ALL render_specs (for {{#for_each_render_config}} loops)
            self.inject_render_template_variables(base_instructions_list, render_instructions, template_specs, all_render_specs=render_specs)
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:124): Useless comment: "# Create single instruction line" - delete it or improve the code instead

    ```python
                template_path = spec.config_data.get('template', 'N/A')
            
            # Create single instruction line
            formatted_parts.append(f'{index}. {config_name} > manually generate {output_path} by taking {input_path} and transform using {template_path}')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:189): Useless comment: "# Handle instructions - can be string or list" - delete it or improve the code instead

    ```python
        def _expand_template_for_spec(self, template_lines: List[str], spec: 'RenderSpec') -> List[str]:
            """Expand template lines with render_config placeholders replaced."""
            # Handle instructions - can be string or list
            instructions = spec.config_data.get('instructions', 'No instructions provided')
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:55): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def change_path(self, new_path: str) -> dict:
            """Change the workspace path. Returns result dict with status and message."""
            import json
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:78): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def set_scope(self, scope) -> dict:
            """Set the scope filter. Scope manages its own persistence, ensuring only one scope exists."""
            # Scope object handles clearing old scope and storing itself
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:90): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def clear_scope(self) -> dict:
            """Clear the scope filter. Scope manages its own removal from state."""
            from agile_bot.bots.base_bot.src.actions.action_context import Scope
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:99): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def get_scope_display(self) -> str:
            """Get the current scope display formatted by CLIScope."""
            scope_data = self._session.get_stored_scope()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\cli_bot\cli_bot.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/cli_bot/cli_bot.py:109): Useless comment: "# Return formatted error with details for debugging" - delete it or improve the code instead

    ```python
                    return cli_scope.to_formatted_display()
                except Exception as e:
                    # Return formatted error with details for debugging
                    return f"{self._session.formatter.scope_icon()} **Scope**\n{self._session.formatter.scope_icon()} Error loading scope: {str(e)}"
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\markdown_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/markdown_formatter.py:7): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def section_separator(self) -> str:
            """Heavy line for major section breaks"""
            return "━" * 90
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\markdown_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/markdown_formatter.py:11): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def subsection_separator(self) -> str:
            """Light line for subsection breaks"""
            return "─" * 60
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:8): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        @abstractmethod
        def section_separator(self) -> str:
            """Heavy line for major section breaks"""
            pass
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:12): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def subsection_separator(self) -> str:
            """Light line for subsection breaks - defaults to same as section_separator"""
            return self.section_separator()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:29): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        # Emoji/icon methods for different contexts
        def bot_icon(self) -> str:
            """Icon for bot/AI context"""
            return ""
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:33): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def workspace_icon(self) -> str:
            """Icon for workspace/folder context"""
            return ""
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:37): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def path_icon(self) -> str:
            """Icon for file path context"""
            return ""
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:41): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def scope_icon(self) -> str:
            """Icon for scope/target context"""
            return ""
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:45): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def position_icon(self) -> str:
            """Icon for current position/location"""
            return ""
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:49): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def currently_executing_icon(self) -> str:
            """Icon for currently executing action"""
            return ""
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\formatters\output_formatter.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/formatters/output_formatter.py:53): Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

    ```python
        
        def file_icon(self) -> str:
            """Icon for file references"""
            return ""
    ```

#### <span id="use-clear-function-parameters-violations">Use Clear Function Parameters: 7 violation(s)</span>

- <span style="color: orange;">[!]</span> **WARNING** - [`src\scanners\duplication_scanner.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/scanners/duplication_scanner.py:1642): Function "scan_cross_file" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            _safe_print("")  # Blank line after violations
        
        def scan_cross_file(
            self,
            rule_obj: Any = None,
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\render\render_instruction_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/render/render_instruction_builder.py:58): Function "_update_instructions_dict" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                    base_instructions_list.insert(insert_position, line)
    
        def _update_instructions_dict(self, instructions: Dict[str, Any], base_instructions_list: List[str], render_instructions: Dict[str, Any], template_specs: List['RenderSpec'], executed_specs: List['RenderSpec'], render_specs: List['RenderSpec'], working_dir: Path) -> None:
            instructions['base_instructions'] = base_instructions_list
            instructions['render_instructions'] = render_instructions
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:292): Function "_process_scanner_result" has 7 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                return data
    
        def _process_scanner_result(self, rule, rule_result: dict, scanner_results: Any, scanner_path: str, scanner_name: str, logger) -> str:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            execution_status = rule.scanner_execution_status or 'SUCCESS'
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:308): Function "_execute_scanner" has 9 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return f'  [OK] {rule.rule_file}: Scanner executed successfully ({violations_count} violations)'
    
        def _execute_scanner(self, rule, rule_result: dict, context: ValidationContext, scanner_path: str, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
            scanner_name = scanner_path.split('.')[-1] if '.' in scanner_path else scanner_path
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:328): Function "_process_rule" has 8 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
                raise
    
        def _process_rule(self, rule, rule_result: dict, context: ValidationContext, logger, files: Dict, changed_files: Dict, all_files: Dict) -> str:
            scanner_path = rule.scanner_path
            if not scanner_path:
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:340): Function "validate" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return self._execute_scanner(rule, rule_result, context, scanner_path, logger, files, changed_files, all_files)
    
        def validate(self, context: ValidationContext, files: Optional[Dict[str, List[Path]]]=None, callbacks: Optional[ValidationCallbacks]=None, skiprule: Optional[List[str]]=None, exclude: Optional[List[str]]=None) -> List[Dict[str, Any]]:
            if isinstance(context, ValidationContext):
                return self._execute_validation(context)
        # ... (truncated)
    ```
- <span style="color: orange;">[!]</span> **WARNING** - [`src\actions\rules\rules.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/rules/rules.py:345): Function "_create_legacy_context" has 6 parameters - consider using existing domain objects with properties instead of passing primitives. Extend domain objects (Behaviors, Behavior, Actions, RenderSpec, etc.) with properties that encapsulate the needed data rather than creating new parameter objects.

    ```python
            return self._execute_validation(self._create_legacy_context(context, files, callbacks, skiprule, exclude))
    
        def _create_legacy_context(self, knowledge_graph: Dict, files: Optional[Dict], callbacks: Optional[ValidationCallbacks], skiprule: Optional[List[str]], exclude: Optional[List[str]]) -> ValidationContext:
            return ValidationContext(knowledge_graph=knowledge_graph, files=files or {}, callbacks=callbacks or ValidationCallbacks(), skiprule=skiprule or [], exclude=exclude or [], skip_cross_file=True, all_files=False, behavior=self.behavior, bot_paths=getattr(self, 'bot_paths', None), working_dir=Path.cwd())
    
    ```

### Cross-File Violations (Pass 2)

These violations were detected by analyzing all files together to find patterns that span multiple files.

#### <span id="eliminate-duplication-violations">Eliminate Duplication: 79 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1168): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_find_scope_matches (lines 1168-1173)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```

  Location 2 (action_context.py:_find_scope_matches_in_graph (lines 315-320)):
    ```python
    match_lines = self._search_for_scope_match(epics, scope_val)
    if match_lines:
        lines.extend(match_lines)
    else:
        lines.append(f'  - {scope_val} (no match)')
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1178): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_for_scope_match (lines 1178-1184)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_for_scope_match (lines 326-332)):
    ```python
    if self._matches_name(epic.get('name', ''), scope_val):
        return self._format_node_with_children(epic, 'epic', 0)
    match_lines = self._search_sub_epics(epic.get('sub_epics', []), scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1189): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_search_sub_epics (lines 1189-1195)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```

  Location 2 (action_context.py:_search_sub_epics (lines 338-344)):
    ```python
    if self._matches_name(sub_epic.get('name', ''), scope_val):
        return self._format_node_with_children(sub_epic, 'sub epic', 0)
    match_lines = self._search_stories(sub_epic, scope_val)
    if match_lines:
        return match_lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1217): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1217-1231)):
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

  Location 2 (action_context.py:_format_node_with_children (lines 377-391)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1218): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1218-1235)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 378-395)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1218): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1218-1235)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 378-397)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1221): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1221-1237)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 381-397)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1221): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1221-1237)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 378-397)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1217): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1217-1235)):
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

  Location 2 (action_context.py:_format_node_with_children (lines 377-395)):
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1218): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1218-1237)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 378-395)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1218): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1218-1237)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 381-397)):
    ```python
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories', []):
            lines.extend(self._format...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\repl_cli\repl_session.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/repl_cli/repl_session.py:1218): Duplicate code detected across files - extract to shared function.

  Location 1 (repl_session.py:_format_node_with_children (lines 1218-1237)):
    ```python
    lines.append(f'{prefix}[{node_type}] {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('st...
    ```

  Location 2 (action_context.py:_format_node_with_children (lines 378-397)):
    ```python
    lines.append(f'{prefix}{emoji} {name}')
    if node_type == 'story':
        return lines
    for sub_epic in node.get('sub_epics', []):
        lines.extend(self._format_node_with_children(sub_epic, 'sub epic', indent + 1))
    for story_group in node.get('story_groups', []):
        for story in story_group.get('stories'...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:126): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_check_for_errors (lines 126-131)):
    ```python
    scanner_results = rule_result.get('scanner_results', {})
    file_by_file_violations = scanner_results.get('file_by_file', {}).get('violations', [])
    cross_file_violations = scanner_results.get('cross_file', {}).get('violations', [])
    file_by_file_errors = any((v.severity == 'error' if hasattr(v, 'severit...
    ```

  Location 2 (validation_scanner_status_builder.py:_format_rule_entry (lines 228-232)):
    ```python
    description = rule_dict.get('rule_content', rule_dict).get('description', 'No description')
    info = lookup.get(rule_file, {})
    status_indicator, status_text = self._get_rule_status_display(info)
    anchor_id = rule_name.replace('_', '-').lower()
    rule_title = rule_name.replace('_', ' ').title()
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:273): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 273-277)):
    ```python
    lines.extend(self.builder.build_header())
    lines.extend(self.builder.build_metadata())
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 19-23)):
    ```python
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(categorized['execution_failed'], 'Scanner Execut...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:273): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 273-277)):
    ```python
    lines.extend(self.builder.build_header())
    lines.extend(self.builder.build_metadata())
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 21-25)):
    ```python
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_failed'], 'Scanner Execution Failures', 'EXECU...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:274): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 274-278)):
    ```python
    lines.extend(self.builder.build_metadata())
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanne...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 19-23)):
    ```python
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(categorized['execution_failed'], 'Scanner Execut...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:274): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 274-278)):
    ```python
    lines.extend(self.builder.build_metadata())
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanne...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 21-25)):
    ```python
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_failed'], 'Scanner Execution Failures', 'EXECU...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:276): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 276-280)):
    ```python
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 19-23)):
    ```python
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(categorized['execution_failed'], 'Scanner Execut...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:276): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 276-280)):
    ```python
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 21-25)):
    ```python
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_failed'], 'Scanner Execution Failures', 'EXECU...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:277): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 277-281)):
    ```python
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    ...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 18-22)):
    ```python
    lines.extend(self.build_status_summary(stats))
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(c...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:277): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 277-281)):
    ```python
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    ...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 19-23)):
    ```python
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(categorized['execution_failed'], 'Scanner Execut...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:277): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 277-281)):
    ```python
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    ...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 21-25)):
    ```python
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_failed'], 'Scanner Execution Failures', 'EXECU...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:278): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 278-282)):
    ```python
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    lines.extend(self.builder.build_report_location(report_path))
    return lines
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 20-24)):
    ```python
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(categorized['execution_failed'], 'Scanner Execution Failures', 'E...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:278): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 278-282)):
    ```python
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    lines.extend(self.builder.build_report_location(report_path))
    return lines
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 22-26)):
    ```python
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_failed'], 'Scanner Execution Failures', 'EXECUTION FAILED'))
    li...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:278): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 278-282)):
    ```python
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    lines.extend(self.builder.build_report_location(report_path))
    return lines
    ```

  Location 2 (validation_scanner_status_builder.py:build_status_summary (lines 124-128)):
    ```python
    lines.append(f'### {overall_status} Overall Status: {overall_text}')
    lines.append('')
    lines.extend(self._build_summary_table(stats))
    lines.extend(self._build_totals_summary(stats))
    return lines
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:273): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 273-278)):
    ```python
    lines.extend(self.builder.build_header())
    lines.extend(self.builder.build_metadata())
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 18-23)):
    ```python
    lines.extend(self.build_status_summary(stats))
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(c...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:273): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 273-278)):
    ```python
    lines.extend(self.builder.build_header())
    lines.extend(self.builder.build_metadata())
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 20-25)):
    ```python
    lines.extend(build_status_summary_fn(stats))
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_f...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:275): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 275-280)):
    ```python
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(sel...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 18-23)):
    ```python
    lines.extend(self.build_status_summary(stats))
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(c...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:275): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 275-280)):
    ```python
    lines.extend(self.builder.build_summary(validation_rules, files))
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(sel...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 20-25)):
    ```python
    lines.extend(build_status_summary_fn(stats))
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_f...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:276): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 276-281)):
    ```python
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 18-23)):
    ```python
    lines.extend(self.build_status_summary(stats))
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(c...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:276): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 276-281)):
    ```python
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 20-25)):
    ```python
    lines.extend(build_status_summary_fn(stats))
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_f...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:277): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 277-282)):
    ```python
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    ...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 19-24)):
    ```python
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(categorized['execution_failed'], 'Scanner Execut...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:277): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 277-282)):
    ```python
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))
    lines.extend(self.violation_formatter.build_violations(validation_rules))
    lines.extend(self.builder.build_instructions(instructions))
    ...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 21-26)):
    ```python
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_failed'], 'Scanner Execution Failures', 'EXECU...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:276): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 276-282)):
    ```python
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))...
    ```

  Location 2 (scanner_status_formatter.py:build_scanner_status (lines 18-24)):
    ```python
    lines.extend(self.build_status_summary(stats))
    lines.append('')
    lines.extend(self.format_executed_rules_section(categorized['executed']))
    lines.extend(self.format_failed_rules_section(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self.format_failed_rules_section(c...
    ```
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_report_writer.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_report_writer.py:276): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_report_writer.py:_build_report_lines (lines 276-282)):
    ```python
    lines.extend(self.builder.build_content_validated(files, self.file_link_builder.get_relative_path, self._build_scanned_files_section))
    lines.extend(self.scanner_status_formatter.build_scanner_status(validation_rules))
    lines.extend(self.scanner_status_builder.build_validation_rules(validation_rules))...
    ```

  Location 2 (validation_scanner_status_builder.py:build_scanner_status (lines 20-26)):
    ```python
    lines.extend(build_status_summary_fn(stats))
    lines.append('')
    lines.extend(self._format_executed_rules(categorized['executed']))
    lines.extend(self._format_failed_rules(categorized['load_failed'], 'Scanner Load Failures', 'LOAD FAILED'))
    lines.extend(self._format_failed_rules(categorized['execution_f...
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
- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_violations_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_violations_builder.py:12): Duplicate code detected across files - extract to shared function.

  Location 1 (validation_violations_builder.py:build_violations (lines 12-16)):
    ```python
    lines = [self._formatter.format_heading('Violations Found', level=2), '']
    file_by_file_violations_by_rule, cross_file_violations_by_rule = self._organize_violations(validation_rules)
    total_file_by_file = sum((len(v) for v in file_by_file_violations_by_rule.values()))
    total_cross_file = sum((len(v) f...
    ```

  Location 2 (violation_formatter.py:build_violations (lines 16-20)):
    ```python
    lines = ['## Violations Found', '']
    file_by_file_violations_by_rule, cross_file_violations_by_rule = self.organize_violations(validation_rules)
    total_file_by_file = sum((len(v) for v in file_by_file_violations_by_rule.values()))
    total_cross_file = sum((len(v) for v in cross_file_violations_by_rule.v...
    ```

#### <span id="use-resource-oriented-design-violations">Use Resource Oriented Design: 1 violation(s)</span>

- <span style="color: red;">[X]</span> **ERROR** - [`src\actions\validate\validation_violations_builder.py`](vscode://file/C:/dev/augmented-teams/agile_bot/bots/base_bot/src/actions/validate/validation_violations_builder.py:5): Class "ValidationViolationsBuilder" uses manager/doer/loader pattern but is not owned by a domain object. Use resource-oriented design instead (e.g., make it a property of a domain object like "ValidationViolations").

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
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\code-validation-report-2025-12-29_00-08-50.md`

